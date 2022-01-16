# Generated by Django 4.0 on 2022-01-15 22:23

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
                ('nombre', models.CharField(max_length=40)),
                ('nacionalidad', models.CharField(max_length=40)),
                ('cantidad_integrantes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('pais', models.CharField(max_length=40)),
                ('premio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
            ],
        ),
    ]
