# Generated by Django 4.1.7 on 2023-10-02 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100, null=True)),
                ('cat_img', models.ImageField(null=True, upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=100, null=True)),
                ('pro_size', models.CharField(choices=[('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE'), ('XL', 'EXTRA LARGE')], default='S', max_length=2)),
                ('pro_price', models.CharField(max_length=100, null=True)),
                ('pro_img', models.ImageField(null=True, upload_to='image')),
                ('pro_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efashionapp.category')),
            ],
        ),
    ]
