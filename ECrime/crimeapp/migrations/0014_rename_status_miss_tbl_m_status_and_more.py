# Generated by Django 4.1.5 on 2023-03-27 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0013_crime_tbl_status_miss_tbl_status_report_tbl_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miss_tbl',
            old_name='status',
            new_name='m_status',
        ),
        migrations.RenameField(
            model_name='report_tbl',
            old_name='status',
            new_name='r_status',
        ),
    ]
