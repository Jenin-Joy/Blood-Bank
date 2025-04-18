# Generated by Django 5.1.6 on 2025-03-01 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_blooddonate',
            old_name='bloodbank_id',
            new_name='bloodbank',
        ),
        migrations.RenameField(
            model_name='tbl_blooddonate',
            old_name='donor_id',
            new_name='donor',
        ),
        migrations.RenameField(
            model_name='tbl_complaint',
            old_name='bloodgroup_id',
            new_name='bloodgroup',
        ),
        migrations.RenameField(
            model_name='tbl_complaint',
            old_name='donor_id',
            new_name='donor',
        ),
        migrations.RenameField(
            model_name='tbl_complaint',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RemoveField(
            model_name='tbl_blooddonate',
            name='bloodgroup_id',
        ),
    ]
