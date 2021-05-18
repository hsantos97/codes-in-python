def primo(x):
	i = 2
	cont = 0
	while i <= x:
		if (x % i) == 0:
			cont =  cont + 1
		i = i + 1
	if cont == 1:
		return 1
	else:
		return 0
		
def maior_primo(x):
	if primo(x) == 1:
		return x
	else:
		i = x - 1
		while primo(i) != 1:
			i = i -1
		return i
