# Generated by Django 2.2.7 on 2020-02-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200129_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nick',
            field=models.CharField(blank=True, max_length=50, unique=True, verbose_name='NickName'),
        ),
    ]