# Generated by Django 4.1.5 on 2023-03-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0004_miss_tbl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='agree',
            new_name='dt',
        ),
        migrations.RenameField(
            model_name='miss_tbl',
            old_name='age1',
            new_name='nmb',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='sts',
        ),
        migrations.AddField(
            model_name='miss_tbl',
            name='eml',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]