import os
import time

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def efeito_carregamento():
    print("\n  Calculando", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

def menu():
    while True:
        limpar_tela()
        # Cores no terminal usando códigos ANSI
        print("\033[95m" + "="*35)
        print("     MINHA CALCULADORA LEGAL ")
        print("="*35 + "\033[0m")
        print("  [1]  Somar")
        print("  [2]  Subtrair")
        print("  [3]  Sair")
        print("\033[95m" + "="*35 + "\033[0m")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '3':
            print("\n Até logo! Obrigado por usar a calculadora.")
            break
            
        if opcao in ['1', '2']:
            try:
                num1 = float(input("\nDigite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("\n Opa! Digite apenas números válidos.")
                time.sleep(2)
                continue
            
            efeito_carregamento()
            
            if opcao == '1':
                resultado = soma(num1, num2)
                print(f" \033[92mO resultado da soma é: {resultado}\033[0m")
            elif opcao == '2':
                resultado = sub(num1, num2)
                print(f" \033[92mO resultado da subtração é: {resultado}\033[0m")
                
            input("\nPressione [Enter] para continuar...")
        else:
            print("\n Opção inválida! Tente novamente.")
            time.sleep(1.5)

# Executa o programa
if __name__ == "__main__":
    menu()