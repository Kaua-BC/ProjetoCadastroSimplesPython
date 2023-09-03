email_cadastrado = ['kaua.coelho11@gmail.com']
senha_cadastrada = ['coelho123']

while True:
    usuario_entrada = str(input('Bem vindo, você possui cadastro? [S]im / [N]ão: ')).upper()
    # Verifica se o usuário já possui um cadastro
    if usuario_entrada == 'S':
        email_login = input('Digite seu email: ')
        senha_login = input('Digite sua senha: ')
        # Verifica se as informações de login são válidas
        if email_login in email_cadastrado and senha_login in senha_cadastrada:
            print('Entrando...')
            break   #Isso encerrará o loop quando o login for bem-sucedido
        else:
            print('Suas informações de login estão incorretas.')
        
 
    else:
        pergunta_cadastro = input('Deseja se cadastrar? Se sim, Digite "Cadastro", se não digite "Sair": ')
        # Verifica se o usuário deseja se cadastrar
        if pergunta_cadastro == 'Cadastro':
            while True:
                novo_email = input('Cadastre um email: ').lower()
                nova_senha = input('Cadastre sua senha: ')
                confirmação_senha = input('Repita a senha: ')
                # Verifica a validade do novo email e da nova senha
                if '@gmail' not in novo_email or '.com' not in novo_email:
                    print('E-mail inválido')
                elif nova_senha != confirmação_senha:
                    print('As senhas não conferem')
                else:
                    # Adiciona o novo email e senha às listas de cadastro
                    email_cadastrado.append(novo_email)
                    senha_cadastrada.append(nova_senha)
                    print('Conta cadastrada com sucesso!!')
                    break # Sai do loop de cadastro após o sucesso
        else:
            print('Saindo...')
            break # Sai do loop se o usuário escolher "Sair"
print('Fim do programa')

