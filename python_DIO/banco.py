menu = """
 [d] Deposito
 [s] Saque
 [e] Extrato
 [q] Sair
"""

saldo = 0
saldoNovo = 0
extrato = ""
qtdSaque = 0
LIMITE_SAQUE = 3

while True: 

    opcao = input(menu)

    if opcao == "d":
        valor = float(input(f'Digite o valor do deposito:'))
        
        if valor > 0:
            saldo = saldo + valor
            extrato += f"Deposito: R$ {valor:.2f}"
            print(f'Deposito realizado!')
        else:
            print(f'Valor para depósito invalido!') 


    elif opcao == "s":
        valor = float(input(f'Digite o valor do saque:'))
        
        if qtdSaque < 3 and qtdSaque > 0 :    
         
         if valor < 500 and valor > 0:
            extrato += f"Saque: R$ {valor:.2f}"
         else:    
            print(f'Ops! Valor invalido, seu limite de saque é R$500!') 
        
         qtdSaque += 1  

        else:
         print('Quantidade de Saques Diários excedidos!')



    elif opcao == "e":
        print(f"""==========EXTRATO==========
{extrato}""")

    elif opcao == "q":
        break
    else: 
     print(f"operação invalida, selecione a operação desejada:")
