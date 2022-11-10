read -t 20 -p "请输入名字(1个字):" name
read -t 20 -p "请输入名字(1个字):" nam
echo "称呼(实用2个字名字):"$name$nam

echo -e "\n"
y=1250
for (( yy = 36; yy > 0; yy-- )); do
x=-1140
	for (( xx = -39; xx < 0; xx++ )); do
		ff=$(echo `awk -v x=${x} -v y=${y} 'BEGIN{printf "%.0f\n",(((x/1000)*(x/1000)+(y/1000)*(y/1000)-1)*((x/1000)*(x/1000)+(y/1000)*(y/1000)-1)*((x/1000)*(x/1000)+(y/1000)*(y/1000)-1)-(x/1000)*(x/1000)*(y/1000)*(y/1000)*(y/1000))*10000000}'`)
		if [[ ff -le 0 ]]; then
			printf "\e[1;41m${name}\e[0m"
		else
		    printf "${nam}"
		fi
	x=$((${x}+60))
	done
printf "\n"
y=$((${y}-70))
done
