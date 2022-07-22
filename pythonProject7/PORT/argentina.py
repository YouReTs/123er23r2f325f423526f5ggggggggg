import requests,os,re
from time import sleep

def argentina():
	os.system('clear')
	print("|                        https://github.com/kancotdiq      - versi 1          |")
	print("\n   [01] 8080"
		  "\n   [02] 53281"
		  "\n   [03] 3128"
		  "\n   [04] 80"
		  "\n   [05] 41258"
		  "\n   [06] 20183"
		  "\n   [07] 9000"
		  "\n   [08] 8081"
		  "\n   [09] 8060"
		  "\n   [10] 8118"
		  "\n   [11] 41766"
		  "\n   [99] Keluar")

	select = input("select@port~#")
	if select == 1:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=8080&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 8080"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 2:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=53281&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 53281"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 3:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=3128&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 3128"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 4:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=80&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 80"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 5:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=41258&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 41258"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 6:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=20183&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 20183"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 7:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=9000&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 9000"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 8:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=8081&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 8081"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 9:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=8060&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 8060"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 10:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=8118&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 8118"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	elif select == 11:
		r = requests.get('http://www.gatherproxy.com/embed/?t=&p=41766&c=Argentina')
		if "There no proxy found." in r.text:
			os.system('clear')
			print "Proxy Not Found - Gunakan PORT / COUNTRY yang lain"
			os.sys.exit()
		ip = re.findall('PROXY_IP":"\d+.\d+.\d+.\d+', r.text)
		cnt = re.findall('PROXY_COUNTRY":"\w+', r.text)
		cns = re.findall('PROXY_TIME":"\d+"', r.text)
		os.system('clear')
		print "=================================="
		count = 1
		for hasil in ip:
			try:
				hasilip = ip[count]
				hasilcountry = cnt[count]
				hasilcns = cns[count]
				hasilIP = hasilip.replace('PROXY_IP":"', 'IP               : ')
				hasilCOUNTRY = hasilcountry.replace('PROXY_COUNTRY":"', 'COUNTRY          : ')
				hasilCNs = hasilcns.replace('PROXY_TIME":"', 'CONNECTION SPEED : ')
				hasilCNS = hasilCNs.replace('"', 'ms')
				print hasilIP
				print "PORT             : 41766"
				print hasilCOUNTRY
				print hasilCNS
				print "=================================="
				sleep(0.1)
				count += 1
			except:
				kentod = "asu"
	else:
		print ""
		print "Pilihan tidak ada"
		os.sys.exit()
		