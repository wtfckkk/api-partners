# Generated by Django 2.1.5 on 2020-02-28 01:13

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradingName', models.CharField(max_length=60)),
                ('ownerName', models.CharField(max_length=60)),
                ('cnpj', models.CharField(max_length=35, unique=True)),
                ('coverageArea', django_mysql.models.JSONField(default=dict)),
                ('address', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]