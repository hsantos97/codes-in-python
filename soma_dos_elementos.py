lista = [1,2,3]

def soma_elementos(lista):
    l = lista
    soma = 0 
    for i in range(len(l)): 
    	soma += l[i] 
    return soma

print(soma_elementos(lista))
