date=$(echo $(date '+%Y-%m-%d'))
filename="weatherdata_${date}.csv"
cp /home/pi/Hygrometer/data.tsv /home/pi/Hygrometer/archiv/${filename}
