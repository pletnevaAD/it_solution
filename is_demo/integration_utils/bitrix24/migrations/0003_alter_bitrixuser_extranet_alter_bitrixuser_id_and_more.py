# Generated by Django 4.0.2 on 2022-02-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrix24', '0002_auto_20200721_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitrixuser',
            name='extranet',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bitrixuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bitrixusertoken',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
