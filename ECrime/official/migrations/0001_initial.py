# Generated by Django 4.1.5 on 2023-03-29 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='offreg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unm', models.CharField(max_length=50)),
                ('em', models.EmailField(max_length=254)),
                ('des', models.CharField(max_length=50)),
                ('oid', models.CharField(max_length=50)),
                ('psw', models.CharField(max_length=16)),
            ],
        ),
    ]
