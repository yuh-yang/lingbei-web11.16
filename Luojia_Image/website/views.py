import datetime

from django.shortcuts import render
from website.models import save_tweets, Tweet

def make_tweet(request):
    username =  #获取用户名
    date = request.GET.get('date')
    time = request.GET.get('time')
    place = request.GET.get('place')
    thing = request.GET.get('thing')
    save_tweets(username, date, time, place, thing)
    return #提示发布成功

def make_timeline(request):
    username = #获取用户名
    today = datetime.date.today() #获取今天日期
    post_list = Tweet.objects.filter(username_icontains = username).filter(date_icontains = today).order_by('time')
    return render(request, 'Time-line.html', {'post_list': post_list})
# Create your views here.
