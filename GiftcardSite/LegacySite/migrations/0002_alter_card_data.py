# Generated by Django 4.1.1 on 2022-11-02 02:19

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LegacySite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='data',
            field=django_cryptography.fields.encrypt(models.BinaryField(unique=True)),
        ),
    ]
