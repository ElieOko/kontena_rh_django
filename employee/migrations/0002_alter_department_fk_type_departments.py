# Generated by Django 5.0.6 on 2024-05-20 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='fk_type_departments',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.typedepartment'),
        ),
    ]
