# Generated by Django 3.1 on 2020-08-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200826_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='starring',
            field=models.CharField(blank=True, max_length=600, verbose_name='主演'),
        ),
    ]
