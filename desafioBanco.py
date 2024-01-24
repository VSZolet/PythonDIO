menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

===> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao  == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Valor invalido. Tente novamente.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_limite = valor > limite
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques >=  LIMITE_SAQUES
        
        if excedeu_limite:
            print("Operaçao cancelada, valor acima do limite de saque.")
        
        elif excedeu_saldo:
            print("Operaçao cancelada, saldo insuficiente.")
            
        elif excedeu_saques:
            print("Operaçao cancelada, voce nao possui mais saques.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação falhou, algo deu errado. Tente novamente.")
    
    elif opcao == "e":
        print("Nao foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        
    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema. Volte sempre.")
        break
    else:
        print("Operação inválida, por favor selecione uma opção válida do menu.")
