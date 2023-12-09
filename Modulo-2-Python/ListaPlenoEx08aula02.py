#Considere a seguinte lista de palavras: ["Python", "é", "uma", "linguagem", "poderosa"]. Escreva
#um programa que itere sobre essa lista e exiba apenas as palavras que possuem mais de 4
#letras.
lista_de_palavras = ["Python", "é", "uma", "linguagem", "poderosa"]

for palavra in lista_de_palavras:
    if len(palavra) > 4:  
        print(palavra)
