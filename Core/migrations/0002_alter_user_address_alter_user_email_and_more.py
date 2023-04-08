# Generated by Django 4.2 on 2023-04-08 09:59

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=1, max_length=255, null=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=1, max_length=254, null=1, unique=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=1, max_length=255, null=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=1, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=1, max_length=255, null=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(blank=1, max_length=14, null=1, unique=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=1, max_length=128, null=1, region=None),
        ),
    ]