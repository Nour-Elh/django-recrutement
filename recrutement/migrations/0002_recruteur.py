# Generated by Django 5.2.1 on 2025-05-30 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recrutement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('entreprise', models.CharField(max_length=100)),
            ],
        ),
    ]
