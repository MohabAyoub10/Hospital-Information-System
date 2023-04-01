# Generated by Django 4.1.7 on 2023-04-01 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Appointments', '0001_initial'),
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_schedule',
            name='doctor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor'),
        ),
        migrations.AddField(
            model_name='booked_appointment',
            name='doctor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor'),
        ),
        migrations.AddField(
            model_name='booked_appointment',
            name='patient_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient'),
        ),
        migrations.AddField(
            model_name='booked_appointment',
            name='slot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Appointments.slot'),
        ),
    ]
