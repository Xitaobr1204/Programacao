#Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.
email_cadastrado = "washingtonalves1204@email.com"
senha_cadastrada = "12344321"


while True:
    email_usuario = input("Digite o seu email: ")
    senha_usuario = input("Digite a senha: ")


    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Acesso permitido!")
        break

    else:
        print("Credenciais incorretas. Tente novamente.")
