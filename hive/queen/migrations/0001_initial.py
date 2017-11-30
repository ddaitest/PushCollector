# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cotent', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='MsgRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plaform', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('sent_on', models.DateTimeField(verbose_name='sent')),
                ('reach_on', models.DateTimeField(verbose_name='reach')),
                ('msg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queen.Message')),
            ],
        ),
    ]