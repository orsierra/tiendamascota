# Generated by Django 4.0.2 on 2022-06-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=20)),
                ('peso', models.IntegerField()),
                ('estatura', models.IntegerField()),
                ('annos_de_vida', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
