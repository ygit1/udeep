from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView   # 追加
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gott/',views.gott, name='gott'),
    path('home2', TemplateView.as_view(template_name='home2.html'), name='home2'),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('book', TemplateView.as_view(template_name='book.html'), name='book'),
    path('test', TemplateView.as_view(template_name='test.html'), name='test'),

    path('accounts/', include('allauth.urls')),    
    path('auth/', views.auth, name='auth'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet2/', views.tweet2, name='tweet2'),

    path('unfollow/', views.unfollow, name='unfollow'),
    path('ff/', views.ff, name='ff'),
    path('followers/', views.followers, name='followers'),
    path('tweet/', views.tweet, name='tweet'),
    path('reply/', views.reply, name='reply'),
    path('dm/', views.dm, name='dm'),
    path('rss/', views.rss, name='rss'),
    path('my_view/', views.my_view, name='my_view'),
    path('twint/', views.twint, name='twint'),
    path('pub/', views.pub, name='pub'),
    path('dl/', views.dl, name='dl'),
    path('', views.top, name='top'),
    path('html', views.html, name='html'),
    path('txt', views.txt, name='txt'),
    path('block', views.block, name='block'),

    path('topnext', views.topnext, name='topnext'),
    path('switch', views.switch, name='switch'),





#    path('tweepy/', views.tweepy, name='tweepy'),

]


