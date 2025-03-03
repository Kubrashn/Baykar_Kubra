# Generated by Django 5.1.6 on 2025-03-02 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Takim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ucak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parca_adi', models.CharField(default='', max_length=100)),
                ('takim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.takim')),
                ('ucak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ucak')),
            ],
        ),
        migrations.CreateModel(
            name='Uretim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('parca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.parca')),
            ],
        ),
    ]
