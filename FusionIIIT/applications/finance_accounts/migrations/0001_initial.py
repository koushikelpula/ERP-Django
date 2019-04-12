# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-12 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_no', models.IntegerField(default=0)),
                ('Bank_Name', models.CharField(max_length=50)),
                ('IFSC_Code', models.CharField(max_length=20)),
                ('Branch_Name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('Company_Name', models.CharField(max_length=20)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('Description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('TransactionId', models.IntegerField(default=0)),
                ('ToWhom', models.CharField(max_length=80)),
                ('FromWhom', models.CharField(max_length=80)),
                ('Purpose', models.CharField(max_length=20)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paymentscheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=70, null=True)),
                ('year', models.IntegerField(null=True)),
                ('pf', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=70)),
                ('designation', models.CharField(max_length=50)),
                ('pay', models.IntegerField()),
                ('gr_pay', models.IntegerField()),
                ('da', models.IntegerField()),
                ('ta', models.IntegerField()),
                ('hra', models.IntegerField()),
                ('fpa', models.IntegerField()),
                ('special_allow', models.IntegerField()),
                ('nps', models.IntegerField()),
                ('gpf', models.IntegerField()),
                ('income_tax', models.IntegerField()),
                ('p_tax', models.IntegerField()),
                ('gslis', models.IntegerField()),
                ('gis', models.IntegerField()),
                ('license_fee', models.IntegerField()),
                ('electricity_charges', models.IntegerField()),
                ('others', models.IntegerField()),
                ('senior_verify', models.BooleanField(default=False)),
                ('ass_registrar_verify', models.BooleanField(default=False)),
                ('ass_registrar_aud_verify', models.BooleanField(default=False)),
                ('registrar_director_verify', models.BooleanField(default=False)),
                ('runpayroll', models.BooleanField(default=False)),
                ('view', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('receipt_id', models.AutoField(primary_key=True, serialize=False)),
                ('TransactionId', models.IntegerField(default=0)),
                ('ToWhom', models.CharField(max_length=80)),
                ('FromWhom', models.CharField(max_length=80)),
                ('Purpose', models.CharField(max_length=20)),
                ('Date', models.DateField()),
            ],
        ),
    ]
