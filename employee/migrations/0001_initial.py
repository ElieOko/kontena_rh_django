# Generated by Django 5.0.6 on 2024-05-20 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoOccurentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='TypeDepartment',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='TypePoste',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='TypeProfession',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('date_birthday', models.DateTimeField()),
                ('marital_status', models.CharField(blank=True, max_length=12)),
                ('level_of_study', models.CharField(blank=True, max_length=255)),
                ('job_description', models.CharField(blank=True, max_length=255)),
                ('fk_department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.department')),
                ('fk_poste', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.poste')),
                ('fk_profession', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.profession')),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.CreateModel(
            name='AdresseEmployee',
            fields=[
                ('nooccurentdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.nooccurentdata')),
                ('city', models.CharField(blank=True, max_length=25)),
                ('street', models.CharField(blank=True, max_length=255)),
                ('fk_employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            bases=('employee.nooccurentdata',),
        ),
        migrations.AddField(
            model_name='department',
            name='fk_type_departments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.typedepartment'),
        ),
        migrations.AddField(
            model_name='poste',
            name='fk_type_poste',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.typeposte'),
        ),
        migrations.AddField(
            model_name='profession',
            name='fk_type_profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.typeprofession'),
        ),
    ]
