# Generated by Django 4.1.7 on 2023-04-01 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='current_medication',
            fields=[
                ('current_medication_id', models.AutoField(primary_key=True, serialize=False)),
                ('Appointment_id', models.IntegerField()),
                ('time_date', models.DateTimeField()),
                ('patient_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='dispensin',
            fields=[
                ('dispensin_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('drug_id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_name', models.CharField(max_length=50)),
                ('drug_type', models.CharField(max_length=50)),
                ('brand_name', models.CharField(max_length=50)),
                ('drug_price', models.IntegerField()),
                ('drug_quantity', models.IntegerField()),
                ('drug_company', models.CharField(max_length=50)),
                ('drug_description', models.CharField(max_length=100)),
                ('stock_level', models.IntegerField()),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pharmacist_license', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DrugReDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('frquency', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('dispense', models.IntegerField()),
                ('Current_medication_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.current_medication')),
                ('drug_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.drug')),
            ],
        ),
        migrations.CreateModel(
            name='dispensin_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensin_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.dispensin')),
                ('drug_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.drug')),
            ],
        ),
        migrations.AddField(
            model_name='dispensin',
            name='Pharmacist_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.pharmacist'),
        ),
        migrations.AddField(
            model_name='dispensin',
            name='current_medication_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pharmacy.current_medication'),
        ),
    ]
