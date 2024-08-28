nome = 'Lucas B'
altura = 1.8
peso = 95

imc = peso/altura**2

#FORMATAÇÃO TIPO 1
texto = f'{nome} tem {peso:.1f} kg e {altura:.2f} m'
print(texto + "\n")

print(f'SEM VARIÁVEL - {nome} tem {peso :.1f} kg e {altura :.2f} m. \nPortanto, seu imc é {imc :.4f}')


#FORMATAÇÃO TIPO 2
#Outra opção de formatação: - adicionar o format após a variável
a = 'AAA'
b = 'BB'
c = 5
var1 = ''.format(a, b, c)
print (var1)

#cada chave referencia um valor do format
var1 = 'a={} b={} c={:.3f}'.format(a, b, c)
print(var1)

var2 = 'a={} b={} c={:.5f}'
print('print format ' +  var2.format(a, b, c))


#FORMATAÇÃO TIPO 3
var3 = 'a={1} b={0} c={teste:.5f} IMC = {1}'
formatoVar3 = var3.format(
    b, a, teste = imc
)
print(formatoVar3)
#Após alguma variável receber um parâmetro, todas as outras também deverão receber As anteriores a ela não precisam

#FORMATAÇÃO TIPO 4
var4 = 'a={1} b={0} c={2} IMC = {1}'
formatoVar4 = var4.format(
    b, a, imc
)
print(formatoVar3)

#O código abaixo resultará em erro, devido ao excesso de variáveis.
# var1 = 'a={} b={} c={:.3f} {}'.format(a, b, c)
# print (var1)