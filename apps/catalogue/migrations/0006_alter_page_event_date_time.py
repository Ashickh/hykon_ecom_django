# Generated by Django 4.1.2 on 2023-03-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_alter_page_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='event_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
