# Generated by Django 5.0.7 on 2024-07-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_expense_purchase_payment_method_sales_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
