# Generated by Django 5.0 on 2024-06-17 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRequisitoPrevioVehicular', '0007_provincia_canton'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agencias', to='appRequisitoPrevioVehicular.canton')),
            ],
        ),
    ]