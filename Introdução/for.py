# Neste caso, entende o for dentro de uma determinada condição, percorrendo a string ou array
#Chamado de for in
texto = 'Python é bom'

novo_texto = ''
for letra in texto:
    print(letra)
    novo_texto += f'*{letra}'
print(novo_texto)

#For com range: range(start, stop, step)
numero = range(10)
print(numero)

numero = range(5, 10)
print(numero)

numero = range(5, 10, 2)
numero = range(-1, -10, -1)

for num in numero:
    print(numero)

#Imprimir todos os números múltiplos de 3 de 0 a 100:
multDe3 = range(0, 100, 3)
for num2 in multDe3:
    print(num2)

#a função __iter__ cria um iterador para uma string
txt = 'Lucas'.__iter__()
#também pode ser utilizado da seguinte forma:
txt = iter('Lucas')

print(txt.__next__())
print(txt.__next__())
print(txt.__next__())
print(txt.__next__())

#também pode ser feito da seguinte forma:
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

while True:
    try:
        letra = next(txt)
        print(letra)
    except StopIteration:
        break

for letra in txt:
    print(letra)