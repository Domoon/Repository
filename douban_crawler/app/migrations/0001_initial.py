# Generated by Django 3.1 on 2020-08-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='电影名')),
                ('director', models.CharField(blank=True, max_length=64, verbose_name='导演')),
                ('writers', models.CharField(blank=True, max_length=64, verbose_name='编剧')),
                ('starring', models.CharField(blank=True, max_length=64, verbose_name='主演')),
                ('type', models.CharField(blank=True, max_length=64, verbose_name='类型')),
                ('made', models.CharField(blank=True, max_length=64, verbose_name='制片国家/地区')),
                ('language', models.CharField(blank=True, max_length=64, verbose_name='语言')),
                ('time', models.CharField(blank=True, max_length=64, verbose_name='上映日期')),
                ('run_time', models.CharField(max_length=64, verbose_name='片长')),
                ('nickname', models.CharField(max_length=64, verbose_name='又名')),
                ('imdb_url', models.CharField(max_length=127, verbose_name='IMDb链接')),
                ('socre', models.CharField(max_length=64, verbose_name='评分')),
                ('buy_url', models.CharField(max_length=127, verbose_name='购票链接')),
            ],
            options={
                'verbose_name': '电影信息',
                'db_table': 'movie_info',
            },
        ),
    ]
