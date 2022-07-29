import random

while True:
    # Decisão se quer jogar
    sair = input('Deseja sair? Digite 1 para sair ou qualquer outra coisa para continuar... \n :  ')
    if sair == '1':
        print('Encerrado')
        break
    else:
        print('continuando')
    # Decisão para escolher o tipo de palavra
    escolha = int(input('Escolha uma opção \n 1 - Comidas \n 2 - Países \n 3 - Marcas de celulares \n '
                        'Dgite o número correspondente a sua escolha: '))
    comidas = ['banana', 'arroz', 'carne', 'frango', 'verdura']
    paises = ['brasil', 'argentina', 'inglaterra', 'espanha']
    marcas_de_celulares = ['lg', 'xiaomi', 'motorola']
    digitados = []
    chances = 3
    # Teste para verificar a escolha
    if escolha == 1:
        palavra_secreta = random.choice(comidas)
    elif escolha == 2:
        palavra_secreta = random.choice(paises)

    else:
        palavra_secreta = random.choice(marcas_de_celulares)
    while True:
        if chances <= 0:
            print(f'Suas chances acabaram. A palavra secreta era {palavra_secreta}')
            break
        letra_do_usuario = input('Digite uma letra: ')
        if len(letra_do_usuario) > 1:
            print('Erro digite apenas uma letra...')
            continue
        digitados.append(letra_do_usuario)
        if letra_do_usuario in palavra_secreta:
            print(f'AEEEE, você acertou uma letra >>> {letra_do_usuario}')
        else:
            print(f'Ahhh, que pena. A letra >>>{letra_do_usuario}<<< não está contido na palavra secreta')
            digitados.pop()
        asteriscos = ''
        for teste_letra in palavra_secreta:
            if teste_letra in digitados:
                asteriscos += teste_letra
            else:
                asteriscos += '*'
        if asteriscos == palavra_secreta:
            print(f'Parabéns, você acertou a palavra "{asteriscos}"')
            break
        else:
            print(f'A palavra está assim {asteriscos}')
        if letra_do_usuario not in palavra_secreta:
            chances -= 1
            print(f'Você ainda tem {chances} chances')
            print()
