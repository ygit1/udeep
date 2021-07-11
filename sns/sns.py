#テキストファイルをコマンドライン引数で取って、それをリストにして、twintでforloopさせる
import twint
import sys,os

args = sys.argv

print(args[0])

# テキストファイルを読み込み、リストから\nを除去する、\nがあるとscrapeできないので。
with open(sys.argv[1], 'r') as f:
    users = list(f)
    new_users = [x[:-1] for x in users]
    print(new_users)


for user in new_users:
    try:
        c=twint.Config()
        c.Limit = 20
        c.Username = user
        twint.run.Search(c)

        c.Proxy_host = "127.0.0.1"
        c.Proxy_port = 5566
        c.Proxy_type = "http"
        c.Store_csv = True

        c.Output = "./dat5/" + user + ".csv"
        twint.run.Search(c)
    except:
        pass


"""
#proxy
for user in new_users:
    try:
        c=twint.Config()
        c.Limit = 20
        c.Username = user
        twint.run.Search(c)

        c.Store_csv = True

        c.Output = "./data5/" + user + ".csv"
        twint.run.Search(c)
    except:
        pass
"""
