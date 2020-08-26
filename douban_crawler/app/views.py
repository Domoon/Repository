from django.http import HttpResponse
from django.shortcuts import render
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "douban_crawler.settings")
django.setup()
# Create your views here.
import requests
from pyquery import PyQuery as pq
from app.models import *
import pymysql

def home(request):

    return HttpResponse('Hello, world!')



def crawl():
    headers = {
        'User-Agent': ('Mozilla/5.0 (compatible; MSIE 9.0; '
                       'Windows NT 6.1; Win64; x64; Trident/5.0)'),
    }
    res = requests.get('https://movie.douban.com/cinema/nowplaying/xiamen/', headers=headers)
    doc = pq(res.text)
    move_list = doc('#nowplaying ul .list-item').items()
    for i in move_list:
        url = i('li .ticket-btn').attr('href')
        # print(i)
        r = requests.get(url, headers=headers)
        c = pq(r.text)
        name1 = c('#content h1 span').text().split(' ')[0]
        # a = c('.subject.clearfix #info').text()
        director1 = c('.subject.clearfix #info').text().split('导演: ')[-1].split('编剧')[0].strip()
        writers1 = c('.subject.clearfix #info').text().split('编剧:')[-1].split('主演')[0].strip()
        starring1 = c('.subject.clearfix #info').text().split('主演:')[-1].split('类型:')[0].strip()
        type1 = c('.subject.clearfix #info').text().split('类型:')[-1].split('制片国家/地区:')[0].split('官方网站:')[0].strip()
        imdb_url1 = c('.subject.clearfix #info').text().strip().split("IMDb链接:")[-1].strip()
        if '\n' or ':'in imdb_url1:
            imdb_url1 = ''
        socre1 = c('#interest_sectl .ll.rating_num').text().strip()
        buy_url1 = c('.aside .ticket a').attr('href')
        time1 = c('.subject.clearfix #info').text().split('上映日期:')[-1].split('片长:')[0].strip()
        run_time1 = c('.subject.clearfix #info').text().split('片长:')[-1].split('又名:')[0].strip()
        made1 = c('.subject.clearfix #info').text().split('制片国家/地区:')[-1].split('语言:')[0].strip()
        language1 = c('.subject.clearfix #info').text().split('语言:')[-1].split('上映日期:')[0].strip()
        nickname1 = c('.subject.clearfix #info').text().split('又名:')[-1].split('IMDb链接:')[0].strip()


        # data = {
        #     'name': name1,
        #     'director': director1,
        #     'writers': writers1,
        #     'starring': starring1,
        #     'type': type1,
        #     'made': made1,
        #     'language': language1,
        #     'time': time1,
        #     'run_time': run_time1,
        #     'nickname': nickname1,
        #     'imdb_url': imdb_url1,
        #     'socre': socre1,
        #     'buy_url': buy_url1,
        #
        # }
        # print(data)
        # Student.objects.create(data['name'])

        conn = pymysql.Connection(host='127.0.0.1', port=3306, db='crawl_data', user='root', password='dx123.')
        cursor = conn.cursor()
        sql = 'insert into movie_info(name_s,director,writers,starring,type_s,made,language_s,time_s,run_time,nickname,imdb_url,socre,buy_url)' \
              'values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(str(name1),str(director1),str(writers1),str(starring1),str(type1),str(made1),str(language1),str(time1),str(run_time1),str(nickname1),str(imdb_url1),str(socre1),str(buy_url1))
        # print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()


def index(request):
    info = Student.objects.all()
    return render(request, 'index.html', {'info':info})

