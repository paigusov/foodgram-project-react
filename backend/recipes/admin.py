from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientContained, Recipe,
                     ShoppingCart, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    empty_value_display = '-пусто-'


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientContained
    min_num = 1
    max_num = 2000

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = (IngredientRecipeInline,)
    
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('author', 'name', 'tags')
    inlines = (IngredientRecipeInline,)

    def is_favorited(self, obj):
        return Favorite.objects.filter(recipe=obj).count()

    @staticmethod
    def amount_favorites(obj):
        return obj.favorites.count()

    @staticmethod
    def amount_tags(obj):
        return '\n'.join([i[0] for i in obj.tags.values_list('name')])

    @staticmethod
    def amount_ingredients(obj):
        return '\n'.join([i[0] for i in obj.ingredients.values_list('name')])


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-пусто-'
