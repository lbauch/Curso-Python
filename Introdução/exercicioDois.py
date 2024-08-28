nome = input('Digite seu nome\n')
idade = input('Digite sua idade\n')

nomeInvertido = nome[::-1]
n = len(nome)

if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nomeInvertido}')
    if " " in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f'seu nome contém {n} letras')