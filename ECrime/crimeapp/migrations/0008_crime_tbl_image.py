# Generated by Django 4.1.5 on 2023-03-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0007_rename_mob_crime_tbl_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crime_tbl',
            name='image',
            field=models.FileField(default=1, upload_to='image'),
            preserve_default=False,
        ),
    ]
