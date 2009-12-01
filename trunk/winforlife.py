import random

### Array che contiene i numeri da giocare ###
numerivincenti = []
### Totale numeri da estrarre ###
numeridagiocare = 10
### Numero da cui partire ###
primonumero = 1
### Numero massimo da poter giocare ###
ultimonumero = 90
while len(numerivincenti) < numeridagiocare:
	### Genero un numero 'casuale' tra 1 e 90 ###
	numero = random.randint(primonumero, ultimonumero)
	### Verifico se ho gia' inserito il numero nell'array dei numeri da giocare ###
	### Se non e' stato inserito lo aggiungo, altrimenti proseguo ###
	if not numero in numerivincenti:
		numerivincenti.append(numero)
print numerivincenti