#!/usr/bin/env python
import requests, os, sys
try :
	CGR = '\33[34m'
	CEN = '\33[0m'

	os.system('clear')
	print(CGR+"""_  _ ____ _  _ ___ ____ ____ ____ _ ___ 
|\/| |__|  \/   |  |___ |__/ |  | |  |  
|  | |  | _/\_  |  |___ |  \ |__| |  |  
                                        
Subdomain Finder"""+CEN)
	#domain = raw_input("Masukkan Domain (Example =  maxteroit.com) : ")
	wordlist=""
	print("1. Bruteforce Subdomain Using Small Wordlist [500++ List]")
	print("2. Bruteforce Subdomain Using Big Wordlist [500k++ List]")
	choose = raw_input("Choose "+CGR+"[1/2]"+CEN+" : ")



	def request(url):
		try :
			return requests.get("http://"+url)
		except requests.exceptions.ConnectionError:
			pass
		except requests.exceptions.InvalidURL:
			pass
		except UnicodeError:
			pass
		except KeyboardInterrupt:
			print("Program Terminated")
			sys.exit(0)

	if choose==str("1"):
		wordlist="small.txt"
		domain = raw_input("Input Target Domain Here (ex:"+CGR+"maxteroit.com"+CEN+") : ")
		request(domain)
	elif choose==str("2"):
		wordlist="subdomain.list"
		domain = raw_input("Input Target Domain Here (ex:"+CGR+"maxteroit.com"+CEN+") : ")
		request(domain)
	else :
		print("Wrong Input")
		sys.exit(0)


	with open(wordlist,"r") as wordlist:
		for line in wordlist:
			word = line.strip()
			test_url = word+"."+domain
			response = request(test_url)
			if response:
				print(CGR+"[+]"+CEN+" Subdomain Ditemukan >> "+CGR+test_url+CEN)

except KeyboardInterrupt:
			print("Program Terminated")
			sys.exit(0)