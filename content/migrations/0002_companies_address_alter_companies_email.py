# Generated by Django 4.2.2 on 2023-06-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
