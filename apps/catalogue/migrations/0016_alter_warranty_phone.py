# Generated by Django 3.2.18 on 2023-05-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_auto_20230502_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
