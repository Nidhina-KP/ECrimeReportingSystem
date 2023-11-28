# Generated by Django 4.1.5 on 2023-03-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0006_remove_miss_tbl_nmbr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='mob',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='city',
            new_name='comptyp',
        ),
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='country',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='dt',
            new_name='gen',
        ),
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='hdate',
            new_name='pname',
        ),
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='idno',
            new_name='regdt',
        ),
        migrations.RenameField(
            model_name='crime_tbl',
            old_name='inc',
            new_name='sec',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='email',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='image',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='img',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='ltn',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='person',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='crime_tbl',
            name='proof',
        ),
        migrations.AddField(
            model_name='crime_tbl',
            name='add',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crime_tbl',
            name='comp',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
