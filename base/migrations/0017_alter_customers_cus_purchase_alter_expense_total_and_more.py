# Generated by Django 5.0.7 on 2024-08-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_purchasedetails_sellrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Cus_Purchase',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='expensedetails',
            name='Amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='expensedetails',
            name='quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='expensedetails',
            name='rate',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='products',
            name='Rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='Stock',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='costPrice',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Discount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='totalAmtPur',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='purchasedetails',
            name='Quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='purchasedetails',
            name='Rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='purchasedetails',
            name='sellRate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='saledetails',
            name='Quantity',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='saledetails',
            name='Rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Discount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='TotalAmt',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='Sup_Purchase',
            field=models.FloatField(default=0, null=True),
        ),
    ]
