#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um 
#vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6)
#e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
def simularlancamentos():
    return[random.randint(1,6) for x in range (101)]

resultadolancamento = simularlancamentos()
contadores = [0]*6