# Generated by Django 3.2.16 on 2022-12-23 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientcontained',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Количество не может быть меньше 1'), django.core.validators.MaxValueValidator(2000, message='Количество не может быть больше 2000')], verbose_name='Количество ингредиента'),
        ),
    ]
