# Generated by Django 2.2.11 on 2020-07-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0134_auto_20200713_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilityrelatedsummary',
            name='s_type',
            field=models.CharField(choices=[('FacilityCapacity', 'FacilityCapacity'), ('PatientSummary', 'PatientSummary'), ('TestSummary', 'TestSummary'), ('TriageSummary', 'TriageSummary')], max_length=100),
        ),
    ]