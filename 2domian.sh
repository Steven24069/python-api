timetd=$(date "+%Y%m%d")
echo $timetd



log_file="/Users/steven/Desktop/ceshicunchu/logdm.txt"

while read -r domain; do
    status_code=$(curl --head --silent --output /dev/null --write-out "%{http_code}" https://"$domain")
    #if [ "$status_code" = "200" ]; then
    if [ "$status_code" -ge 200 ] && [ "$status_code" -le 302 ]; then
        echo "Domain $domain is using HTTPS."
    else
        echo "$timetd Domain $domain is not using HTTPS. =>>>>>>>>>>>>>>>>>>>>>>> check" >>  "$log_file"
    fi
done < /Users/steven/Desktop/ceshicunchu/dm.txt


cat  $log_file 