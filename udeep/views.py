import tweepy
import time
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
import subprocess
import twint
import sys


#ターミナルの出力をそのままdjangoに
#https://chase-seibert.github.io/blog/2010/08/06/redirect-console-output-to-a-django-httpresponse.html
def print_http_response(f):
    """ Wraps a python function that prints to the console, and
    returns those results as a HttpResponse (HTML)"""

    class WritableObject:
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)

    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return HttpResponse(['<BR>' if c == '\n' else c for c in printed.content ])
    return new_f




import os
#os.path.joinなんだけど、単純に初期設定でmanage.pyのところに指定されてるからそこを指定すればファイルを呼べる

from rest_framework.response import Response


def gott(request):
    res = request.GET['id'] #キーボードからyour_nameというresponseを受け取り
# このviewsからの場所でファイルを指定
    cmd = './a.sh {}'.format(res) 
    pipe=subprocess.run(cmd, shell=True)
    import pandas as pd
    df = pd.read_csv(res+".txt")
    dfo = df.to_html()
    return HttpResponse(dfo)



def top(request):
    f = open('sns/txt/x00' , 'r')
   # f = open('jack.txt' , 'r')
 
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "text.html", context)


def topnext(request):
    res = request.GET['next'] #キーボードからyour_nameというresponseを受け取り
    with open('sns/txt/' + res, 'r',encoding="utf8", errors='ignore') as f:
    #f = open('sns/txt/' + res , 'r')
        file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "text.html", context)



@print_http_response
def txt(request):
    import pandas as pd
    import glob
    #show only 1 cell
    for i in glob.iglob('sns/data4/*csv'):
        df=pd.read_csv(i)
        val = df['name'].values[0]
        print(val)
        print(df[['date','tweet']])
        print("=================")
    return HttpResponse()




def html(request):
    import pandas as pd
    import glob
    #show only 1 cell
    for i in glob.iglob('sns/dat5/*csv'):
        df=pd.read_csv(i)
        val = df['name'].values[0]
        print(val)
        df=df[['date','tweet']]        
    obj=df.to_html()
    return HttpResponse(obj)





# twint -u jack > out これで出力をテキストにできる　sherlockも同じ　で、
#最後にそのtxtを組み合わせてレンダーすればいいのココロ







def test(request):
    df=pd.read_csv('csv/a.csv')
    obj=df.to_html()
    return HttpResponse(obj)


class Home(TemplateView):
    template_name = 'home.html'





#@print_http_response
def dl(request):
    import twint
    res = request.GET['your_name'] #キーボードからyour_nameというresponseを受け取り
    limit = request.GET['limit'] #キーボードからyour_nameというresponse
    c=twint.Config()
    c.Username=res
    c.Limit=limit #20倍数でないと動かない
    c.Proxy_host = "127.0.0.1"
    c.Proxy_port = 5566
    c.Proxy_type = "http"
    c.Store_csv = True
   # c.Custom_csv = ["date","time","tweet"]
    c.Output = res+".csv"
    twint.run.Search(c)
    import pandas as pd
    df=pd.read_csv(res+'.csv')
    df2=df['tweet']
    df2.to_csv(res+'.txt')

    cmd = 'pandoc {}.txt -o {}.epub -f markdown+hard_line_breaks'.format(res,res) 

#    cmd = 'pandoc {}.csv -o {}.epub'.format(res,res) 
    #受け取ったresを2つ{}に代入
    subprocess.run(cmd, shell=True)

    #import pypandoc
    #pypandoc.convert_file(res+'.txt', 'a.epub')

#    df=pd.read_csv('twitter.csv')
#    print(df)
#file download to pc/phone
    import os
    from django.views.static import serve
    filepath = res+'.epub'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))



from django.shortcuts import render
from django.template.loader import render_to_string

def my_view(request):
    as_file = request.GET.get('as_file')
    context = {'some_key': 'some_value'}

    if as_file:
        content = render_to_string('your-template.html', context)                
        with open('path/to/your-template-static.html', 'w') as static_file:
            static_file.write(content)

    return render('your-template.html', context)











def tweet(request):
    res = request.GET['your_name'] #キーボードからyour_nameというresponseを受け取り
    cmd = 'twint -u {} limit -o {}.csv --csv --proxy-type http --proxy-host 127.1 --proxy-port 5566'.format(res,res) 
    #受け取ったresを2つ{}に代入
    subprocess.run(cmd, shell=True)
    return HttpResponse()





def pub(request):
    import twint
    res = request.GET['your_name'] #キーボードからyour_nameというresponseを受け取り
    limit = request.GET['limit'] #キーボードからyour_nameというresponse
    c=twint.Config()
    c.Username=res
    c.Limit=limit #20倍数でないと動かない
    c.Proxy_host = "127.0.0.1"
    c.Proxy_port = 5566
    c.Proxy_type = "http"
    c.Store_csv = True
   # c.Custom_csv = ["date","time","tweet"]
    c.Output = res + ".csv"
    twint.run.Search(c)
#    twint.run.Followers(c)
    return HttpResponse()






@print_http_response
def twint(request):
    import twint
    res = request.GET['your_name'] #キーボードからyour_nameというresponseを受け取り
    limit = request.GET['limit'] #キーボードからyour_nameというresponse
    c=twint.Config()
    c.Username=res
    c.Limit=limit #20倍数でないと動かない
    c.Proxy_host = "127.0.0.1"
    c.Proxy_port = 5566
    c.Proxy_type = "http"
    c.Store_csv = True
    c.Output = res + "-p.csv"
    #twint.run.Lookup(c)

    res = request.GET['your_name'] #キーボードからyour_nameというresponseを受け取り
    limit = request.GET['limit'] #キーボードからyour_nameというresponse
    c=twint.Config()
    c.Username=res
    c.Limit=limit #20倍数でないと動かない
    c.Proxy_host = "127.0.0.1"
    c.Proxy_port = 5566
    c.Proxy_type = "http"
    c.Store_csv = True
    c.Output = res + ".csv"
    twint.run.Search(c)
    import pandas as pd
    df=pd.read_csv(res+".csv")
    print(df[["date","time","tweet"]])
#    df.

    return HttpResponse()












###########################################################################

import tweepy
CONSUMER_KEY = 'LYnLfIDAyzfsMC8noXHkKeBom'
CONSUMER_SECRET = '2ydDtvhKJefzxJR0BqjsPeKsLDql1dyPBs3HGQCsaU4UsK1gK4'


def auth(request):
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {
            'consumer_key':CONSUMER_KEY,
            'consumer_secret':CONSUMER_SECRET,            
            'access_token_key':token,
            'access_token_secret':token_secret
        }        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
#    me=api.me()
    api.update_status('e')
    a=[]

#get 20 followers
#    for follower in api.followers():
#        a.append(follower.screen_name + '\n')

#more than 20 use cursor
#    for follower in tweepy.Cursor(api.followers,id=me.id,count=50).items():
#        a.append(follower.screen_name + '\n')
#    print(len(a))    
#    #return render(request,'afterauth.html')
#    return HttpResponse(a)

# Counting the number of followers.





###########################################################################


def switch(request):

    import tweepy
    api = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGSPbwEAAAAAMQNZBThqpti8xuf9GPAzNGnXGI8%3DHWTztfxdZV1tK3Dyd9cWILlUk5yL8VLRu3VqvPqaBm54eQjAaB')


    #me=api.me()

    a=[]
    api.update_status(request)

   # match request:
    #    case 400:
            #
     #   case 400:
            #







@print_http_response
def block(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {
            'consumer_key':CONSUMER_KEY,
            'consumer_secret':CONSUMER_SECRET,            
            'access_token_key':token,
            'access_token_secret':token_secret
        }        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
    me=api.me()
#############################################################################
    followers = api.followers_ids() #get all followers
    friends = api.friends_ids() # get all follows
    for f in followers:
        api.create_block(f)

    return HttpResponse()



@print_http_response
def tweet2(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {
            'consumer_key':CONSUMER_KEY,
            'consumer_secret':CONSUMER_SECRET,            
            'access_token_key':token,
            'access_token_secret':token_secret
        }        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
    me=api.me()
#############################################################################
    followers = api.followers_ids() #get all followers
    friends = api.friends_ids() # get all follows
    for f in followers:
        print(f)

    return HttpResponse()





@print_http_response
def reply(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {'consumer_key':CONSUMER_KEY,'consumer_secret':CONSUMER_SECRET,'access_token_key':token,'access_token_secret':token_secret}        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)    
    me=api.me()
#############################################################################

@print_http_response
def dm(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {'consumer_key':CONSUMER_KEY,'consumer_secret':CONSUMER_SECRET,'access_token_key':token,'access_token_secret':token_secret}        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)    
    me=api.me()
#############################################################################


@print_http_response
def rss(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {'consumer_key':CONSUMER_KEY,'consumer_secret':CONSUMER_SECRET,'access_token_key':token,'access_token_secret':token_secret}        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)    
    me=api.me()
#############################################################################



@print_http_response
def ff(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {'consumer_key':CONSUMER_KEY,'consumer_secret':CONSUMER_SECRET,'access_token_key':token,'access_token_secret':token_secret}        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
    me=api.me()
#############################################################################
    screen_name="y80jp"
#    for follower in tweepy.Cursor(api.followers, sn,count=10).items():
    for follower in tweepy.Cursor(api.followers, me.id,count=50).items(100):
        print(follower.screen_name)

    followers = api.followers_ids() #get all followers
    friends = api.friends_ids() # get all follows
    print(friends)
    print("aaa")
    print(followers)
    return HttpResponse()

def unfollow(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {'consumer_key':CONSUMER_KEY,'consumer_secret':CONSUMER_SECRET,'access_token_key':token,'access_token_secret':token_secret}        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
    me=api.me()
#############################################################################
    followers = api.followers_ids() #get all followers
    friends = api.friends_ids() # get all follows
    print(friends)
    for f in friends:
        if f not in followers:
            print("Unfollow {0}?".format(api.get_user(f).screen_name))
            api.destroy_friendship(f)
    return HttpResponse()




@print_http_response
def followers(request):
#############################################################################
    t = SocialToken.objects.get(account__user_id=request.user.pk)
    token= t.token
    token_secret = t.token_secret
    twitter_keys = {'consumer_key':CONSUMER_KEY,'consumer_secret':CONSUMER_SECRET,'access_token_key':token,'access_token_secret':token_secret}        
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)    
    me=api.me()
#############################################################################
    
    import random
    import string
    hiragana = u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわをんゔァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤユヨラリルレロワン"
    random_ja = random.choice(hiragana)
    print(random_ja)
    new_search = random_ja + '-filter:links -https:// -bot -filter:retweets exclude:replies'
    tweets = api.search(q=new_search)
    #api.create_favorite('1408761922879557634')


    user = api.get_user(me.id)

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)
    #print("🐶"+user.tweet.text)

    print("Last 20 Followers:")
    """for follower in user.followers():
        try:
            for a in api.user_timeline(exclude_replies=True,include_rts=False,id=follower.id,count=1):
                #print(a)
                print(a.id)
                api.create_favorite(a.id)
                print("***")
                status = api.get_status(a.id)
                print("***")
                print(status.id)
                print(status.favorite_count)
                api.create_favorite(status.id)

                #favorite_count = status.favorite_count
            #print(tl.text)
            #print("🍏"+follower.name)
            #print("fav" + status.favorite_count)
            #api.create_friendship(follower.id)
            #api.create_favorite(tl.id)
        except:
            pass
#        follower.follow()
"""


    api.create_friendship("realpython") #follow
    #api.update_profile(description="I like Python") #change profile

    tweets = api.home_timeline(count=1)
    tweet = tweets[0]
    #print(f"Liking tweet {tweet.id} of {tweet.author.name}")
    #api.create_favorite(tweet.id)

    #block
    #for block in api.blocks():
    #    print(block.name)

    api.trends_available
    trends_result = api.trends_place(1)
    for trend in trends_result[0]["trends"]:
        print(trend["name"])


    #自分のタイムラインを表示
    timeline = api.home_timeline()
    print("🌈timeline")
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")    
        print(tweet.id)




    """
    class MyStreamListener(tweepy.StreamListener):
        def __init__(self, api):
            self.api = api
            self.me = api.me()

        def on_status(self, tweet):
            print(f"{tweet.user.name}:{tweet.text}")

        def on_error(self, status):
            print("Error detected")
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])
    """

    """
    #api.update_status("hello") #tweet
    # 自分にきたリプライをリストにしてラブする
    tweets = api.mentions_timeline()
    for tweet in tweets:
        tweet.favorite()
        tweet.user.follow()
    """

    
    #api.update_status("hello") #tweet

    tweets = api.home_timeline()
    for tweet in tweets:
        print("🔹"+ tweet.text)
        if not tweet.retweeted:
            try:
                tweet.favorite()
            except:
                pass
        #tweet.user.follow()
    

    #api.update_status("hello") #tweet
    try:
        tweets = api.get_status()
    except:
        pass
        for tweet in tweets:
            print(tweet.text)
    #        tweet.user.follow()



"""
    screen_name="GhinQuita"
    for follower in tweepy.Cursor(api.followers, screen_name ,count=50).items(100):
        print(follower.screen_name)

    followers = api.followers_ids() #get all followers
    friends = api.friends_ids() # get all follows
    print(friends)
    print(followers)
    return HttpResponse()
"""

