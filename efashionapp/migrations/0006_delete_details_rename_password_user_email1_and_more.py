# Generated by Django 4.1.7 on 2023-10-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efashionapp', '0005_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Details',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='user',
            name='phone1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username1',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
