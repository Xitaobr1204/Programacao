import random

def simular_loteria():
    numeros_sorteados = random.sample(range(1, 61), 6)
    
    print("Bem-vindo à Loteria! Tente a sorte e escolha 6 números de 1 a 60.")
    
    numeros_usuario = []
    for _ in range(6):
        while True:
            try:
                numero = int(input("Digite um número: "))
                if 1 <= numero <= 60 and numero not in numeros_usuario:
                    break
                else:
                    print("Por favor, insira um número válido de 1 a 60 e que ainda não tenha sido escolhido.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.")

        numeros_usuario.append(numero)

    acertos = set(numeros_usuario).intersection(numeros_sorteados)

    print(f"\nNúmeros sorteados: {numeros_sorteados}")
    print(f"Seus números: {numeros_usuario}")
    print(f"Números corretos: {acertos}")

    if len(acertos) >= 4:
        premio = calcular_premio(len(acertos))
        print(f"Parabéns! Você acertou {len(acertos)} números e ganhou um prêmio de R$ {premio:.2f}.")
    else:
        print("Você não ganhou desta vez. Tente novamente!")

def calcular_premio(acertos):
    premio_base = 1000
    premio_por_acerto = 200
    return premio_base + (acertos - 4) * premio_por_acerto

# Chamada da função para simular a loteria
simular_loteria()