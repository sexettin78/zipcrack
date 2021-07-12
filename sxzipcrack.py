import os
import pyzipper
print('''
Wordlistiniz var mı 
(Yok seçeneği işaretlenirse program sizin için oluşturacak)
1-) Wordlistim var

2-) Wordlistim yok
''')
aaaas = input("Seç > ")

if(aaaas=="2"):
	import random 
	import pyzipper
	import os

	chars = input("İçinde olmasını istediğiniz harf rakam sembol vb giriniz: ")

	password_uzunluk = int(input("Ne kadar uzunlukta olsun? "))
	password_sayi = int(input("Kaç tane şifre oluşturulsun? "))
	for x in range(0,password_sayi):
		password = ""
		for x in range(0,password_uzunluk):
			password_sayi = random.choice(chars)
			password	= password + password_sayi
		#print(password)
		passworda = (password+"\n")
		dosya = open("wlist.txt","a")
		dosya.write(passworda)


	wordlist = ("wlist.txt")

	file = input("Zip dosya yolunu belirtiniz > ")	
	icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")

	fileobject = pyzipper.AESZipFile(file)

	with open(wordlist,"rb") as wordlist:
		for word in wordlist:
			try:
				fileobject.pwd = word.strip()
				fileobject.read(icdosya)
			except:
				print("\033[93mŞifre denendi = ",word.decode().strip())
				continue
			else:
				print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
				os.system("rm -rf wlist.txt")
				exit(0)
				
	os.system("rm -rf wlist.txt")
	print("\033[91mŞifre Bulunamadı")

elif(aaaas=="1"):
	import pyzipper
	import os
	os.system("pip install pyzipper")
	wordlist = input("Wordlist Yolunu Belirtiniz > ")

	file = input("Zip dosya yolunu belirtiniz > ")	
	icdosya = input("Zip dosyası içinden herhangi bi dosya adı+uzantı giriniz > ")

	fileobject = pyzipper.AESZipFile(file)

	with open(wordlist,"rb") as wordlist:
		for word in wordlist:
			try:
				fileobject.pwd = word.strip()
				fileobject.read(icdosya)
			except:
				print("\033[93mŞifre denendi = ",word.decode().strip())
				continue
			else:
				print("\033[92mŞifre bulundu! İşte şifre = ",word.decode().strip())
				exit(0)
	print("\033[91mŞifre Bulunamadı")




