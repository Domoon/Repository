
# Create your models here.
from django.db import models


class Student(models.Model):
     name_s = models.CharField(max_length=128, blank=True, verbose_name="电影名")
     director = models.CharField(max_length=128, blank=True, verbose_name="导演")
     writers = models.CharField(max_length=128, blank=True, verbose_name="编剧")
     starring = models.CharField(max_length=600, blank=True, verbose_name="主演")
     type_s = models.CharField(max_length=128, blank=True, verbose_name="类型")
     made = models.CharField(max_length=128, blank=True, verbose_name="制片国家/地区")
     language_s = models.CharField(max_length=128, blank=True, verbose_name="语言")
     time_s = models.CharField(max_length=128, blank=True, verbose_name="上映日期")
     run_time = models.CharField(max_length=128, verbose_name="片长")
     nickname = models.CharField(max_length=128, verbose_name="又名")
     imdb_url = models.CharField(max_length=300, verbose_name="IMDb链接")
     socre = models.CharField(max_length=128, verbose_name="评分")
     buy_url = models.CharField(max_length=128, verbose_name="购票链接")


     class Meta:
          verbose_name = "电影信息"
          db_table = "movie_info"
