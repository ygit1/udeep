while IFS= read -r user; do
snscrape --jsonl --progress --max-results 100 twitter-search "from:${user} exclude:replies" > ${user}.json
done< $1