# Generated by Django 2.2.7 on 2019-11-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]
