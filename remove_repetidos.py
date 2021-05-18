lista = [2, 4, 2, 2, 3, 3, 1]

def remove_repetidos(lista):
	aux = []
	for i in lista:
		if i not in aux:
			aux.append(i)
	aux.sort()
	return aux
	
print(remove_repetidos(lista))
