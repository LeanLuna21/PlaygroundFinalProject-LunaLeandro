# Generated by Django 4.2.7 on 2023-12-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_cliente_transaccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='fecha_venta',
            field=models.DateField(),
        ),
    ]
