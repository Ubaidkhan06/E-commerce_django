# Generated by Django 3.2.6 on 2021-08-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.IntegerField(max_length=50),
        ),
    ]