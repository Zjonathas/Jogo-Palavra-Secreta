import random

letra_do_usuario = ''
while True:
    # Decisão se quer jogar
    print('#' * 100)
    sair = input(f'Deseja sair? Digite 1 para sair ou qualquer outra coisa para continuar... \n{"#" * 100} \n ')

    if sair == '1':
        print('Encerrado')
        break
    else:
        print('continuando')
    # Decisão para escolher o tipo de palavra

    escolha = input('Escolha uma opção \n 1 - Comidas \n 2 - Países \n 3 - Marcas de celulares \n '
                    'Dgite o número correspondente a sua escolha: ')
    comidas = ['banana', 'arroz', 'carne', 'frango', 'verdura', 'sopa', 'feijao', 'melancia', 'salcisha', ]
    paises = ['brasil', 'argentina', 'inglaterra', 'espanha']
    marcas_de_celulares = ['lg', 'xiaomi', 'motorola']
    digitados = []
    chances = 4

    # Teste para verificar a escolha
    if escolha == '1':
        palavra_secreta = random.choice(comidas)
        print(f'A palavra secreta tem {len(palavra_secreta)} caracteres')

    elif escolha == '2':
        palavra_secreta = random.choice(paises)
        print(f'A palavra secreta tem {len(palavra_secreta)} caracteres')

    elif escolha == '3':
        palavra_secreta = random.choice(marcas_de_celulares)
        print(f'A palavra secreta tem {len(palavra_secreta)} caracteres')
    else:
        print(f'Por favor digite uma opção válida: ')
        continue

    # Iniciando o jogo
    while True:
        if chances <= 0:
            print(f'Suas chances acabaram. A palavra secreta era {palavra_secreta}')
            break
        print()
        escolha2 = input('Dejesa digitar apenas uma letra ou a palavra inteira? [1] para letra [2] para a palavra: ')
        if escolha2 == '1':
            print()
            letra_do_usuario = input('Digite uma letra: ')
        elif escolha2 == '2':
            print()
            palavra_do_usuario = input('Digite a palavra: ')
            if palavra_do_usuario == palavra_secreta:
                print()
                print(f'Parabéns, você acertou a palavra "{palavra_secreta}"')
                break
            else:
                print()
                chances -= 1
                print(f'Você ainda tem {chances} chances')
                print()
                continue
        else:
            print(f'Você digitou uma opçaão inválida...')
            continue
        digitados.append(letra_do_usuario)
        if letra_do_usuario in palavra_secreta:
            print()
            print(f'AEEEE, você acertou uma letra >>> {letra_do_usuario}')
        else:
            print()
            print(f'Ahhh, que pena. A letra >>>{letra_do_usuario}<<< não está contido na palavra secreta')
            digitados.pop()
        asteriscos = ''
        for teste_letra in palavra_secreta:
            if teste_letra in digitados:
                asteriscos += teste_letra
            else:
                asteriscos += '*'
        if asteriscos == palavra_secreta:
            print()
            print(f'Parabéns, você acertou a palavra "{asteriscos}"')
            break
        else:
            print(f'A palavra está assim {asteriscos}')
        if letra_do_usuario not in palavra_secreta:
            chances -= 1
            print()
            print(f'Você ainda tem {chances} chances')
            print()
