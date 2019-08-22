import webbrowser 
import time
user={}
ertek=5
prompt='''Koszontelek Lali elso 100+ soros programjaban!
Ez egy regisztracios program!
Az egyes visszalepeseknel a q-t tudod hasznalni!'''
print(prompt)
def username(username):
	a=len(username)
	if a<5:
		return False
def password(password):
	a=len(password)
	if a<8:
		return False
while True:
	result=True
	result2=True
	if ertek==0:
		break
	r_b=input('Mit szeretnel regisztralni vagy bejelentkezni?(r/b)\t')
	if r_b.lower()=='regisztralni' or r_b.lower()=='r':
		while True:
			r_user=input('Add meg a usernamet!\t')
			if r_user=='q':
				break
			result=username(r_user)
			if result==False:
				print('A usernamenek legalabb 5 karaktert kell tartalmaznia!')
				continue
			if r_user in user:
				print('Ez mar foglalt!')
				continue
			while True:
				r_bejelentkezni=input('Add meg a passwordot!\t')
				if r_bejelentkezni=='q':
					break
				result2=password(r_bejelentkezni)
				if result2==False:
					print('A jelszonak legalabb 8 karaktert kell tartalmaznia!')
					continue
				user[r_user]=r_bejelentkezni
				print('Sikeresen regisztraltal!')
				break
			break
		continue
	elif r_b.lower()=='bejelentkezni'or r_b.lower()=='b' :
		index=len(user)
		if index==0:
			print('Elsore regisztralj!')
			continue
		while True:
			flag=False
			key1=False
			value1=False
			a=input('Add meg a usernamet!\t')
			if a.lower()=='q':
				break
			b=input('Add meg a passwordot!\t')
			if b.lower()=='q':
				continue
			a=str(a)
			b=str(b)
			for key,value in user.items():
				if key==a and value==b:
					flag=True
				elif key!=a and value==b:
					key1=True
				elif value!=b and key==a:
					value1=True							
			if flag==False:
				ertek-=1
			if flag==True:
				print('Induljon hat a bulee!!!')
				webbrowser.open('https://www.youtube.com/watch?v=QuGlOHKxMdA')
				break
			elif key1:
				print('rossz a username!')
				print('Meg ennyit probalkozhatsz:',ertek)
			elif value1:
				print('Rossz a password!')
				print('Meg ennyit probalkozhatsz:',ertek)
				password_valtoztatas=input('Szeretne uj jelszavat? ')
				if password_valtoztatas!='nem':
					while True:
						uj_jelszo=input('Mi legyen az uj jelszo? ')
						if uj_jelszo=='q':
							break
						result2=password(uj_jelszo)
						if result2==False:
							print('A jelszonak legalabb 8 karaktert kell tartalmaznia!')
							continue
						uj_jelszo2=input('Ismeteld meg a jelszot! ')
						if  uj_jelszo!=uj_jelszo2:
							print('A ket jelszo nem egyezik!')
							continue
						else:
							user[a]=uj_jelszo
							print('A jelszo megvaltozott!')
							break
					break
			else:
				print('Egyiksejo !')
				print('Meg ennyit probalkozhatsz:',ertek)
			if ertek==0:
				print('Ezt beszoptad kisgyerek!')
				time.sleep(1)
				for i in range(3):
					for x in range(5):
						webbrowser.open('https://www.gaymaletube.com/')
						time.sleep(2)
				break
	elif r_b.lower()=='q':
		break
	elif r_b.lower()=='admin':
		admin_password=input('Kerem a jelszot!\t')
		if admin_password=='987654321':
			print('Szoj Lali!')
			print(user)
		else:
			print('Huzz a faszba!')
			
