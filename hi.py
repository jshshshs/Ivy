import rody
rody.ai()
while True:
    ask=(input("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n [0] Acessar Conta \n [1] Registrar Conta \n [2] Informações \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  \nQual serviço você deseja?  ")).upper()
    if ask in "1":
        test = "logins.py"
        rody.logcad()
    if ask in "0":
        rody.logar()
        print("Aguarde um momento")
        from time import sleep
        for c in range(0, 3):
            print(".", end="")
            sleep(2)
        print()

        op=["Mega-Sena", "Calculadora", "Par ou Impar", "Pagar Contas", "Cadastrar Currículos", "Chat", "Sair do Programa"]
        what = 0
        while True:
            print("=-"*20)
            for o, i in enumerate(op):
                print(f" [ {o} ]   {i}   ")
            print("=-" * 20)
            what = str(input("Qual aplicativo deseja usar? "))
            if what.__contains__("0"):
                rody.megasena()
            if what.__contains__("1"):
                rody.calculadora()
            if what.__contains__("2"):
                rody.imparoupar()
            if what.__contains__("3"):
                rody.pagar()
            if what.__contains__("4"):
                rody.registro("dados.py")
            if what.__contains__("5"):
                rody.chat()
            if what.__contains__("6"):
                print(f">>>>>>>>>>>> Obrigado por nos visitar, até logo! <<<<<<<<<<<<<<<")
                break
    elif ask == 2:
        print("Para mais informações acesse: https://www.rody.com/information")
    askto=str(input("Deseja voltar pra tela inicial? [Sim ou Não]: ")).upper()
    if askto in "SIM":
        continue
    else:
        break
