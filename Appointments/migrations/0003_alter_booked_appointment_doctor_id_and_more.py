# Generated by Django 4.1.7 on 2023-04-01 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
        ('Appointments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked_appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor'),
        ),
        migrations.AlterField(
            model_name='booked_appointment',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient'),
        ),
        migrations.AlterField(
            model_name='doctor_schedule',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor'),
        ),
    ]
