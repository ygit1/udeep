while IFS= read -r user; do
twint -u $user --limit 20 -o ${user}.csv --csv \
--proxy-type http --proxy-host 127.1 --proxy-port 5566 &
done< $1
