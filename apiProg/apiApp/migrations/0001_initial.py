# Generated by Django 4.1 on 2022-08-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='backup_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='dipendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('descrizione', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='esperienza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azienda', models.CharField(max_length=200)),
                ('luogo', models.CharField(max_length=200)),
                ('mansioni', models.CharField(max_length=200)),
                ('rettribuzione', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=200)),
                ('descrizione', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='lavoratore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cognome', models.CharField(max_length=200)),
                ('data_nascita', models.DateField()),
                ('luogo_nascita', models.CharField(max_length=200)),
                ('nazionalita', models.CharField(max_length=200)),
                ('indirizzo', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
                ('lingue', models.CharField(max_length=200)),
                ('patente', models.CharField(max_length=200)),
                ('patente_data', models.DateField()),
                ('email', models.EmailField(max_length=200)),
                ('descrizione', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='lavoro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('mansioni', models.CharField(max_length=200)),
                ('luogo', models.CharField(max_length=200)),
                ('descrizione', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]