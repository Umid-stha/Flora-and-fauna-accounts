# Generated by Django 5.0.7 on 2025-03-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_customers_cus_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='wc_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
