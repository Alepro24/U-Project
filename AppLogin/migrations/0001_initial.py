# Generated by Django 3.1.1 on 2020-11-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Nro_Usuario', models.AutoField(primary_key=True, serialize=False)),
                ('Usuario', models.CharField(max_length=30)),
                ('Contrasena', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('Estado', models.BooleanField()),
            ],
        ),
    ]
