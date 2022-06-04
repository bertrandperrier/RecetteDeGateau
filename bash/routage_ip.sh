#!/bin/bash
#ip_wifi=$(ip -f inet -o addr show enp3s0  | cut -d\  -f 7 | cut -d/ -f 1)
ip_wifi=$(ip -f inet -o addr | grep 3: | cut -d\  -f 7 | cut -d/ -f 1)

if [ "$ip_wifi" != "192.168.1.28" ]
then
	#python /home/bertrand/linux/script/send_mail_ip.py $ip_wifi
	echo "****** ip wifi diff envoie mail *****"
	echo $ip_wifi
fi
