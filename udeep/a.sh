#!/bin/bash
./gott $1 > $1.txt

#delete https:
sed 's/http[^ ]*//g' $1.txt |sponge $1.txt

#名詞を抽出
mecab -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd $1.txt | grep -e "名詞,一般" -e "固有名詞" -e "名詞,サ変接続"  | cut -f1 | tr '\n' ' ' | sponge $1.txt

#頻度を出す
cat $1.txt | tr ' ' '\n' | sort | uniq -c | sort -nr |sponge $1.txt > $1.txt

#cat $1.txt
