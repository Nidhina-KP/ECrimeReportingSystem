# Generated by Django 4.1.6 on 2023-04-23 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0019_remove_crime_tbl_sts_remove_miss_tbl_sts_m_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_tbl',
            name='btl',
        ),
    ]