def logcad(arquivo, login='',senha=''):
    a = open(arquivo, 'at')
    login=str(input("Digite um login: "))
    senha=str(input("Digite uma senha: "))
    log = {"login": login, "senha": senha}
    a.write(f"{log}\n")
    a.close()
    print(">>>>>>>>>>>>>>>>> Cadastro efetuado com sucesso <<<<<<<<<<<<<<<<<<<<")



def registro(arquivo):
    from datetime import datetime
    cadastro = {}
    info = list()
    while True:
        cadastro.clear()
        cadastro["nome"] = str(input("Digite seu nome: "))
        idade = int(input("Digite seu ano de nascimento: "))
        cadastro["idade"] = datetime.now().year - idade
        print("[0] Ensino fundamental completo\n"
              "[1] Ensino Médio completo\n"
              "[2] Ensino superior completo\n"
              "[3] Ensino Técnico completo\n"
              "[4] Nenhuma das opções\n")
        while True:
            academico = int(input("Qual seu grau acadêmico? "))
            if 0 <= academico <= 4:
                if academico == 0:
                    cadastro["curso"] = "Ensino fundamental completo"
                if academico == 1:
                    cadastro["curso"] = "Ensino médio completo"
                if academico == 3:
                    cadastro["curso"] = str(input("Qual curso? "))
                elif academico == 2:
                    cadastro["curso"] = str(input("Qual curso? "))
                elif academico == 4:
                    cadastro["curso"] = str(input("Qual curso? "))
                break
            else:
                print("ERRO. Digite um número dentro da lista: ")
        trabalho = str(input("Possui expêriencia em sua formação? [SIM/NÃO] ")).upper()
        if trabalho in "NÃO":
            cadastro["trabalho"] = "Não possui experiência na função"
        elif trabalho in "SIM":
            cadastro["trabalho"] = "Possui experiência na função"
        info.append(cadastro.copy())
        askto = str(input("Deseja cadastrar mais um curriculo? [SIM/NÃO] ")).upper()
        if askto in "NÃO":
            break
    for i in info:
        print("========================================================")
        for k, v in i.items():
            print(f"{k}: {v}")
    print("========================================================")
    print()
    print(">>>>>>>>> OBRIGADO POR SE CADASTRAR EM NOSSO SISTEMA <<<<<<<<<")
    print()
    a = open(arquivo, "at")
    a.write(f'{info}\n')


def pagar():
    infos = list()
    for c in range(0, 1):
        nome = str(input("Digite seu nome: "))
        valorpago = float(input("Digite o valor a ser pago: "))
        valordivida = float(input("Digite o valor da sua divida total: "))
        saldo = (valorpago - valordivida)
        infos.append([nome, valorpago, valordivida, saldo])
    print('=-' * 40)
    for c, i in enumerate(infos):
        print(f"{c}|---------| {i[0]} |-----------| R$ {i[3]:.2f} |------------|")
    print(f'Valor pago de {i[1]}     |      Valor da Divida de {i[2]}')
    print(f'=====================   Restante da divida {i[3]} =========================')
    print('=-' * 40)


def imparoupar():
    import random
    sum2 = 0
    r = random.randint(1, 10)
    while True:
        w = int(input("Digite um número: "))
        ip = str(input("impar ou par?: ")).upper()
        sum = w + r
        print(f"Você jogou {w} e o computador {r}, a soma foi {sum}")
        if ip == "PAR":
            if sum % 2 == 0:
                print("Você GANHOU!")
                sum2 += 1
            else:
                print("Você PERDEU")
        elif ip == "IMPAR":
            if sum % 2 == 1:
                print("Você GANHOU!")
                sum2 += 1
            else:
                print("Você PERDEU")
        n = " "
        while n not in "SIMNÃO":
            n = str(input("Deseja jogar novamente? ")).upper()
        if n == "NÃO":
            print("Obrigado por jogar conosco!")
            print(f"Você ganhou {sum2} vezes!")
            break


def calculadora():
    s = 0
    n1 = int(input("Informe o número A:"))
    n2 = (input("Informe o operador aritmético: "))
    n3 = int(input("Informe o número B: "))

    if n2.__contains__("+"):
        print('O resultado é: ', n1 + n3)
    elif n2.__contains__("-"):
        print('O resultado é: ', n1 - n3)
    elif n2.__contains__("*"):
        print('O resultado é: ', n1 * n3)
    elif n2.__contains__("**"):
        print('O resultado é: ', n1 ** n3)
    elif n2.__contains__("raiz"):
        print('O resultado é: ', n1 ** (1 / 2))
    else:
        print('O resultado é: ', n1 / n3)


def megasena():
    import random
    roll1 = random.randint(1, 60)
    roll2 = random.randint(1, 60)
    roll3 = random.randint(1, 60)
    roll4 = random.randint(1, 60)
    roll5 = random.randint(1, 60)
    roll6 = random.randint(1, 60)
    print("Bem vindo ao Gerador de números para Mega-Sena")
    while roll6 == roll5 == roll4 == roll3 == roll2 == roll1:
        roll1 = random.randint(1, 3500)
        roll2 = random.randint(1, 3500)
        roll3 = random.randint(1, 3500)
        roll4 = random.randint(1, 3500)
        roll5 = random.randint(1, 3500)
        roll6 = random.randint(1, 3500)
        roll7 = random.randint(1, 3500)
    print(
        "Os números da sua Mega-Sena são: \033[32m{}\033[0m \033[33m{}\033[0m \033[34m{}\033[0m \033[36m{}\033[0m \033[31m{}\033[0m \033[35m{}\033[0m".format(
            roll1, roll2, roll3, roll4, roll5, roll6))
    print("Boa sorte em seus jogos")



def ai():
    from time import sleep
    nome = str(input('Olá! Eu me chamo \033[34mIvy\033[0m, qual é o seu primeiro nome? '))
    print("Olá \033[;33m{}\033[0m!".format(nome))
    bem = str(input("Como você está? ")).upper()
    if bem in "ESTOU BEM":
        print("Que ótimo {}!".format(nome))
        ask =  str(input("Deseja me contar sobre seu dia? [SIM/NÃO] ")).upper()
        if ask in "SIM":
            dia = str(input(f'E como está sendo seu dia {nome}? '))
            dia1 = str(input(f'O que você fez hoje {nome}? '))
            print("Interessante!")
            dia2 = str(input("O que você gostaria muito de fazer hoje? "))
            print("Então...")
            sleep(2)
            print(f'Mãos a obra {nome}!')
            print("Carpe Diem meu caro amigo :) ")
            print("Mas enfim...")
            sleep(4)
        else:
            print("Tudo bem, respeito sua escolha...")
            print("Mas enfim...")
            sleep(4)
    elif bem in "MAL NÃO ESTOU BEM":
        print("Ah que pena...")
        sad= str(input('Quer se abrir comigo? [SIM/NÃO] ')).upper()
        if sad in "SIM":
            sad1 = str(input("O que te fez se sentir mal? "))
            print("entendi... :( ")
            sleep(2)
            print(f"Mas pensa comigo {nome}, existe um lindo céu azul lá fora, ou uma linda noite estrelada.\n Mesmo nos dias nublados eles estão lá, por mais que não seja visível por conta das nuvens, mas toda nuvem é passageira.\n Se mantenha forte sempre {nome}!")
            sleep(4)
            ask = str(input("Deseja me contar sobre seu dia? [SIM/NÃO] "))
            if ask in "SIM":
                dia = str(input(f'E como está sendo seu dia {nome}? '))
                dia1 = str(input(f'O que você fez hoje {nome}? '))
                print("Interessante!")
                dia2 = str(input("O que você gostaria muito de fazer hoje? "))
                print("Então...")
                sleep(3)
                print(f"Mãos a obra {nome}!")
                print("Carpe Diem meu caro amigo :) ")
                print("Mas enfim...")
                sleep(4)
            else:
                print("Tudo bem, respeito sua escolha...")
                print("Mas enfim...")
                sleep(4)
        else:
            print("Tudo bem, respeito sua escolha...")
            print("Mas enfim...")
            sleep(4)



            
