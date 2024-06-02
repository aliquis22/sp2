# Generated by Django 5.0.6 on 2024-05-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Отображается на сайте'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]