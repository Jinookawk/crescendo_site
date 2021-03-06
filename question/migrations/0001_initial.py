# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('comment_num', models.IntegerField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question'),
        ),
    ]
