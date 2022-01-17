# Generated by Django 3.0 on 2022-01-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('tipo', models.CharField(choices=[('EN', 'Entrada'), ('SA', 'Salida')], default='EN', max_length=2)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
