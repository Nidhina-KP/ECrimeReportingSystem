# Generated by Django 4.1.5 on 2023-03-27 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0014_rename_status_miss_tbl_m_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miss_tbl',
            name='add',
        ),
        migrations.RemoveField(
            model_name='miss_tbl',
            name='alias',
        ),
    ]
