
=== install mecab on ubuntu
sudo apt install -y mecab libmecab-dev mecab-ipadic-utf8

> check mecab
$ mecab
> put some words, enter

pip3 install mecab-python3
pip3 install unidic-lite



##### 
install neologd for Normalization

> see not 固有名詞
mecab
小泉純一郎

>>> install

git clone https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
sudo ./bin/install-mecab-ipadic-neologd -n -a -y





=== for ubuntu debian, add
sudo vim /etc/mecabrc
# dicdir =  /usr/local/lib/mecab/dic/ipadic
dicdir = /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd


>
default neologd directory
mecab -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd
>



> 
> check result 固有名詞
mecab           
小泉純一郎
>


> 
example
$ echo "8月3日に放送された「中居正広の金曜日のスマイルたちへ」(TBS系)で、1日たった5分でぽっこりおなかを解消するというダイエット方法を紹介。ダイエットにも密着。" | mecab -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd




mkdir gott; cd gott

go get -u github.com/n0madic/twitter-scraper


vi main.go
package main

import (
    "fmt"
    "os"
    "context"
    twitterscraper "github.com/n0madic/twitter-scraper"

)

func main() {

    argsWithProg := os.Args
    argsWithoutProg := os.Args[1:]

//引数の数を指定 
// ./main jackとすると、0が./main 1がjackになる
    arg := os.Args[1]

    fmt.Println(argsWithProg)
    fmt.Println(argsWithoutProg)
    fmt.Println(arg)

    scraper := twitterscraper.New()

// 3200 tweets
    for tweet := range scraper.GetTweets(context.Background(),arg, 3200) {
        if tweet.Error != nil {
            panic(tweet.Error)
        }
        fmt.Println(tweet.Text)
}
}

go build main.go
chmod +x main.go

./main jack


sudo apt-get install moreutils
sudo apt install -y mecab libmecab-dev mecab-ipadic-utf8


git clone ytytgo/udeep
source env/bin/activate
pip3 install -r requirements.txt

python3 manage.py runserver 0.0.0.0:9999














# udeep

sudo apt install virtualenv
virtualenv env


