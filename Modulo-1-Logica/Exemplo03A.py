usuario = 'admin'
senha = '1234'

usuario_lido = input('Usuário: ')
senha_lida = input('Senha: ')

if usuario_lido == usuario or senha_lida == senha:
    print('Usuário ou senha incorretos. Tente novamente.')

else:
    print('Bem vindo ao sistema.')