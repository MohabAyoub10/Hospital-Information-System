# Generated by Django 4.1.7 on 2023-03-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appoitments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_schedule',
            name='day_of_week',
            field=models.CharField(choices=[('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=50),
        ),
    ]
