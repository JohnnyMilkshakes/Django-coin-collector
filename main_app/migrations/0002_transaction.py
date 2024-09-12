# Generated by Django 5.1.1 on 2024-09-12 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Transaction Date')),
                ('type', models.CharField(choices=[('B', 'Buy'), ('S', 'Sell')], default='B', max_length=1)),
                ('price', models.FloatField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.coin')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
