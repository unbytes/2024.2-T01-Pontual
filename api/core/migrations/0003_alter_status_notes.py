# Generated by Django 5.1.4 on 2025-01-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='notes',
            field=models.CharField(blank=True, choices=[('faltou', 'FALTOU'), ('esqueceu', 'ESQUECEU'), ('atestado', 'ATESTADO')], max_length=9, null=True),
        ),
    ]
