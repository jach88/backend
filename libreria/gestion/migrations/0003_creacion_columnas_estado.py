# Generated by Django 3.2.7 on 2021-09-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_creacion_tablas_operaciones_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientemodel',
            name='clienteEstado',
            field=models.BooleanField(db_column='estado', default=True),
        ),
        migrations.AddField(
            model_name='productomodel',
            name='productoEstado',
            field=models.BooleanField(db_column='estado', default=True),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='clienteDireccion',
            field=models.CharField(db_column='direccion', max_length=100, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='clienteDocumento',
            field=models.CharField(db_column='documento', max_length=12, unique=True, verbose_name='documento del cliente'),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='clienteNombre',
            field=models.CharField(db_column='nombre', help_text='Ingresa aqui el nombre', max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='productomodel',
            name='productoUnidadMedida',
            field=models.TextField(choices=[('UN', 'UNIDAD'), ('DOC', 'DOCENA'), ('CI', 'CIENTO'), ('MI', 'MILLAR')], db_column='unidad_medida', default='UN'),
        ),
    ]
