# Generated by Django 4.0.1 on 2022-02-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TipoIdentificacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoidentificacion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
