# Generated by Django 4.1.7 on 2023-10-24 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('efashionapp', '0008_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='cartid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='efashionapp.cart'),
        ),
    ]
