flag=True
def make_album():
	artist=input('artist?')
	album=input('album?')
	tracks=input('tracks?')
	if artist=='q' or album=='q' or tracks=='q':
		flag=False
	if tracks:
		int(tracks)
		dic={'artist':artist,'album':album,'tracks':tracks}
	else:
		dic={'artist':artist,'album':album}
	return dic

while flag:
	try:
		while flag:
			print(make_album())
	except ValueError:
		print('te okor a tracksbe szamkell,vagy ha nics akkor nyomjal el entert')
	
