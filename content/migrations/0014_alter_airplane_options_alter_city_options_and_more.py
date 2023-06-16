# Generated by Django 4.2.2 on 2023-06-16 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_alter_flight_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airplane',
            options={'ordering': ['model'], 'verbose_name': 'самолет', 'verbose_name_plural': 'самолеты'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'город', 'verbose_name_plural': 'города'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['last_name'], 'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'компания', 'verbose_name_plural': 'компании'},
        ),
        migrations.AlterModelOptions(
            name='flight',
            options={'ordering': ['data_departure'], 'verbose_name': 'рейс', 'verbose_name_plural': 'рейсы'},
        ),
        migrations.AlterModelOptions(
            name='seatclass',
            options={'ordering': ['name'], 'verbose_name': 'место', 'verbose_name_plural': 'места'},
        ),
        migrations.AlterModelTable(
            name='client',
            table='client',
        ),
    ]
