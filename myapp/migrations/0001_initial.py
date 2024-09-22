# Generated by Django 5.0.6 on 2024-06-19 01:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InquiryReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ReportParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField()),
                ('subject_type', models.CharField(max_length=10)),
                ('response_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SearchParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_type', models.CharField(max_length=10)),
                ('bvn_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RequestParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.application')),
                ('inquiry_reason', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.inquiryreason')),
                ('report_parameters', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.reportparameters')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('request_parameters', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.requestparameters')),
                ('search_parameters', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.searchparameters')),
            ],
        ),
    ]
