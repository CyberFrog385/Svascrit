import os
import json
file = open('scryt.html', 'w+')
with open('/home/cybertoad/Documents/Pythonscripts/djubiyar.json') as sl:
	alf = json.load(sl)

print("Welcome to Shvascrit translator!")
#letter = input('Введите букву: ')
text = input('Введите текст: ')
#tekst = text.replace(" ", "/").split("/")#hhh
tekst = list(text)
i = 0
j = 0
final = '<table><td valign = "top">'

for i in range(len(tekst)):
	final = final + "<br>" + '<img src = "img/' + alf[tekst[i]] + '"' + 'width = "20" height = "20"' + '></img>'
	j = j + 1
	if j == 48:
		j = 0
		final = final + '<br><img src = "img/propusk.png"></br></td><td valign = "top">'
	

file.write("<html> \n<head> \n<title>shvascrit</title> \n<body>"+final+" \n</body> \n</html>")
print("Check html page")
#print(test_text)
file.close()
sl.close()

#120 symbols - max, then new line
