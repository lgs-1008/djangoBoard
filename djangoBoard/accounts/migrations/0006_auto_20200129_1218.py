# Generated by Django 2.2.7 on 2020-01-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200124_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(blank=True, help_text='ex) YYYY-MM-DD', null=True),
        ),
    ]
