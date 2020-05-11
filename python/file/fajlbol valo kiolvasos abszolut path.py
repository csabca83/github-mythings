filepath='C:\\Users\\laliv\\Desktop\\faszom.txt'  #a windows szar ezert a file pathba kettes \ kellenek
with open (filepath) as file_object:              #abszolut path,relativ path csak azt mondja melyik folder tehat path/filename.txt
	#adat=file_object.read()
	adat2=file_object.readlines()
for adat in adat2:
	print(adat.rstrip())
