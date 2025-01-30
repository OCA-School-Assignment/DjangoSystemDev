# Generated by Django 5.1.5 on 2025-01-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='estimated_delivery_date',
            field=models.DateField(default='2099-01-30'),
            preserve_default=False,
        ),
    ]
