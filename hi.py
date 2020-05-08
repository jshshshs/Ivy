import rody
rody.ai()
print()
ask=(input("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n [0] Acessar Conta \n [1] Registrar Conta \n [2] Informações \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n \nQual serviço você deseja?  ")).upper()
print()
if ask in "1":
    test = "logins.py"
    rody.logcad(test)
if ask in "0":
    while True:
        login=(input("informe seu login: "))
        if login  == "Blitk" :
            break
        else:
           print("ACESSO NEGADO.")
    while True:
        senha=(input("Informe sua senha: "))
        if senha == "blitk123":
            break
        else:
            print("ACESSO NEGADO.")

    print("Aguarde um momento")
    from time import sleep
    for c in range(0, 3):
        print(".", end="")
        sleep(2)
    print()
    print()
    print("Olá {}! Sua conta está ativa!".format(login))

    op=["Mega-Sena", "Calculadora", "Par ou Impar", "Pagar Contas", "Cadastrar Currículos", "Sair do Programa"]
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
            print(f">>>>>>>>>>>> Obrigado por nos visitar, até logo! <<<<<<<<<<<<<<<")
            break
else:
    print("Para mais informações acesse: https://www.blitk.com/information")
