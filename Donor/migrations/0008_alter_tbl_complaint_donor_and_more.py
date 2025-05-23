# Generated by Django 5.1.6 on 2025-03-16 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0007_tbl_complaint'),
        ('Guest', '0002_alter_tbl_donor_donor_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_complaint',
            name='donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_donor'),
        ),
        migrations.AlterField(
            model_name='tbl_complaint',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_patient'),
        ),
    ]
