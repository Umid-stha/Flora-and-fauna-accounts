# Generated by Django 5.0.7 on 2024-07-16 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_sales_sale_saledetails_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='bill_no',
            field=models.IntegerField(default=0),
        ),
    ]
