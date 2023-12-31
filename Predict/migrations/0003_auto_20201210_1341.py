# Generated by Django 3.1.1 on 2020-12-10 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Predict', '0002_auto_20201210_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelousado',
            fields=[
                ('id_Modelo', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo_modelo', models.CharField(max_length=20)),
                ('Nombre_modelo', models.CharField(max_length=20)),
                ('Estado', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='prediccion',
            name='id_Modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Predict.modelousado'),
        ),
        migrations.DeleteModel(
            name='modelo',
        ),
    ]
