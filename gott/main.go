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
