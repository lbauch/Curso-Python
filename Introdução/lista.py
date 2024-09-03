# Em outras linguagens de programação, é utilizado chamado de array
# É um tipo mutável
# Suporta diversos valores de qualquer tipo

lista = []
# Caso a lista esteja vazia, seu bool é falsy
print(bool(lista))
print(lista, type(lista))

lista = [123, True, 'Lucas B', 1.2, []]
print(lista)

lista[2] = False
print(lista)

# Para adicionar coisas à lista:
lista.append('Lucas B')
lista.append(56)
print(lista)

# Funciona como uma fila - FIFO - pop remove o último valor adicionado
# Pop retorna e remove o último valor
valorRemovido = lista.pop()
# Para remover um item específico da lista:
valorMeio = lista.pop(2)
print(lista, f'removidos: final: {valorRemovido}, meio: {valorMeio}')

