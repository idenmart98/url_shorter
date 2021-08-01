# Generated by Django 3.2.5 on 2021-08-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_url', models.URLField(unique=True)),
                ('short_code', models.CharField(max_length=5, unique=True)),
            ],
        ),
    ]
