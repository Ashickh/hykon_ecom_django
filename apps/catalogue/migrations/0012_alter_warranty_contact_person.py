# Generated by Django 4.1.2 on 2023-03-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_remove_warranty_billing_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='contact_person',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
