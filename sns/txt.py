# csvをランキング順位でBash出力する。txt.py > という形でこれを使って保存する
#あるいはsplitで初めにtop100のリストを百人づつで分割して、それをtwintしてフォルダに分けて入れて、catする
#それかページネーション使う
import os
import pandas as pd
import glob
import sys,os
args = sys.argv

num=0

# sort files in directory with date, and forloop
for i in sorted(glob.iglob(sys.argv[1]+'/*csv'),key=os.path.getmtime):
    df=pd.read_csv(i)
    val = df['name'].values[0]
    print(val)
    print(df[['date','tweet']])
    df=df.style.set_properties(**{'text-align': 'left'})
    print("=======================================")
