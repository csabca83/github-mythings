from collections import OrderedDict
dic=OrderedDict()                       #ez nekunk mindig abba sorba lesznek a key,value parok ahogy beleraktuk,en meg nem tapasztaltam hogy nem lenne sorba de majd meglassuk milyen
dic['lali']='kiraly'
dic['csicso']='cigany'
for x in dic.items():
	print(x)
