# Generated by Django 4.0.5 on 2022-06-26 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
    ]
