# Generated by Django 5.1.3 on 2024-12-20 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego', models.CharField(max_length=40)),
                ('region', models.CharField(max_length=40)),
                ('rango', models.CharField(max_length=40)),
                ('cant_jugadores', models.IntegerField()),
                ('objetivo', models.TextField(verbose_name='')),
            ],
        ),
    ]
