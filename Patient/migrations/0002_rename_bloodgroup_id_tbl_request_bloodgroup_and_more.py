# Generated by Django 5.1.6 on 2025-03-02 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_request',
            old_name='bloodgroup_id',
            new_name='bloodgroup',
        ),
        migrations.RenameField(
            model_name='tbl_request',
            old_name='patient_id',
            new_name='patient',
        ),
        migrations.RenameField(
            model_name='tbl_request',
            old_name='place_id',
            new_name='place',
        ),
    ]
