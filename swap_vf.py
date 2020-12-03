# ===================================+ PROTOTIVO V1 CC +======================================== #

# ========= GABRIELA ALVES == GABRIEL PORTELA == LUCAS MENDES == LUCIA NEGREIROS =============== #

# ================================= IMPORTS E DECLARACOES ====================================== #
from func_swap import *
import difflib  # Para pesquisa por proximidade

opcao, opcao_log = '', ''

leitores = read_dict('leitores')
livros = {}
livros_por_usuario = {}
finalizar = ''

end, bold = '\033[0m', '\033[1m'
red, green, blue, orange, gray = '\033[91m', '\033[32m', '\033[34m', '\033[33m', '\033[1m\033[90m'
semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

# ========================= INICIO DO ACESSO DO USUARIO ============================== #

while opcao_log != '-1':
    opcao_log = input(f"\n{bold}{orange}--------SWAP--------{end}"
                      f"\n{bold}{blue}1{end} - Criar Conta"
                      f"\n{bold}{blue}2{end} - Log in"
                      f"\n{bold}{blue}-1{end} - Encerrar"
                      f"\n{gray}Selecione uma das opções: {end}")

    # ======================== CRIACAO DE CONTA (APPEND(FUNCAO)) =========================== #
    # A conta no modo de teste eh criada automaticamente apenas com o nome do usuario
    # e a senha sera 123456

    if opcao_log == '1':
        print(f"\n{bold}{orange}---------CRIAR CONTA---------{end}")

        leitor = {}
        username = check_username(leitores)
        senha = check_senha()
        email = check_email(leitores)
        nome = nome_completo()
        data_nascimento = check_data()
        pergunta = pergunta_secreta()
        resposta = input(f'{gray}{pergunta}{end}')
        leitor['user'] = username
        leitor['chats'] = {}
        leitor['nome'] = nome
        leitor['senha'] = senha
        leitor['email'] = email
        leitor['data'] = data_nascimento
        leitor['pergunta'] = pergunta
        leitor['resposta'] = resposta
        leitor['livros'] = {}
        leitor['pontos'] = 0

        leitores[username] = leitor
        save_dict(leitores, 'leitores')

        print(f"{green}Leitor cadastrado com sucesso!{end}")

    # ================================= ENTRAR NO SISTEMA =================================== #

    elif opcao_log == '2':
        while True:
            print(f"\n{bold}{orange}-------- ENTRAR --------{end}")
            usuario = input(f"{gray}Usuário: {end}")
            senha = input(f"{gray}Digite sua senha ou 5 se você esqueceu a sua senha: {end}")
            logado = False
            if usuario in leitores:
                if senha == leitores[usuario]['senha']:
                    logado = True
                    print(f"{green}Login feito com sucesso!{end}")
                    break
                elif senha == '5':
                    resposta_seguranca = input(
                        f"{gray}Digite a resposta da sua pergunta de segurança{end}\n: {leitores[usuario]['pergunta']}")
                    if resposta_seguranca == leitores[usuario]['resposta']:
                        leitores[usuario]['senha'] = check_senha()
                        save_dict(leitores, 'leitores')
                        print(
                            f"{green}Senha trocada com sucesso!\n{end}"
                        )
                        break
                    else:

                        print(f"{red}Resposta incorreta{end}")
                        continue


                else:
                    print(f"{red}Senha inválida{end}\n")
                    if input(
                            f"{gray}Digite {bold}{blue}-1{end}{gray} para voltar ao cadastro"
                            f"\nou aperte {bold}{blue}enter{end}{gray} para tentar novamente: {end}"
                    ) == '-1':
                        break
                    else:
                        continue

            else:
                print(f"{red}Usuário não encontrado!{end}\n")
                if input(
                        f"{gray}Digite {bold}{blue}-1{end}{gray} para voltar ao cadastro"
                        f"\nou aperte {bold}{blue}enter{end}{gray} para tentar novamente: {end}"
                ) == '-1':
                    break
                continue
        # ========================= APOS ENTRAR, INICIO DO CRUD ============================== #

        while logado:

            print(f"\n{orange}-------- POSTS --------{end}")
            try:
                if leitores['posts']:
                    for post in reversed(leitores['posts']):
                        print(f'\n{post}')
                        print(f"\n{orange}-----------------------{end}")
            except:
                print(f"{gray}Nenhum post feito.{bold}")

            opcao = input(f"\n{bold}{orange}-------- HOME ({leitores[usuario]['user']}) --------{end}"
                          f"\n{bold}{blue}1{end} - Buscar"
                          f"\n{bold}{blue}2{end} - Perfil"
                          f"\n{bold}{blue}3{end} - Publicar"
                          f"\n{bold}{blue}4{end} - Conversas"
                          f"\n{bold}{blue}5{end} - Livros"
                          f"\n{bold}{blue}6{end} - Pontos"
                          f"\n{bold}{blue}-1{end} - Sair"
                          f"\n{gray}Selecione uma das opções: {end}")

            # ========================= BUSCAR  ============================== #

            if opcao == '1':
                while True:
                    opcao_busca = input(f"\n{bold}{orange}-------- BUSCAR --------{end}"
                                        f"\n{bold}{blue}1{end} - Leitor"
                                        f"\n{bold}{blue}2{end} - Livro por titulo"
                                        f"\n{bold}{blue}3{end} - Livro por genero"
                                        f"\n{bold}{blue}-1{end} - Voltar"
                                        f"\n{gray}Selecione uma das opções: {end}")
                    if opcao_busca == '1':

                        print(f"\n{bold}{orange}---------BUSCAR LEITOR---------{end}")
                        if leitores[usuario]:
                            consulta_leitor = input(
                                f"{gray}Pesquisar por: {end}"
                            )
                            busca = listar_opcoes(
                                difflib.get_close_matches(consulta_leitor, leitores.keys(), cutoff=0.3))

                            if not busca:
                                print(f"{red}Leitor não encontrado!{end}\n")
                            else:
                                print(f"{bold}{orange}------ Livros de {busca} ------{end}")
                                i = 1
                                for book in leitores[busca]['livros'].keys():
                                    print(
                                        f"{bold}{blue}{i}{end} - {bold}{book}{end}\n\t{bold}{green}{leitores[busca]['livros'][book]['pontos']} Pontos {end}\n")
                                    i += 1

                                print(f"Enviar mensagem para {bold}{busca}{end}?")
                                escolha_chat = input(
                                    f"{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                                ).upper()

                                if escolha_chat == 'S':
                                    enviar_chat(usuario, busca, leitores)
                                    save_dict(leitores, 'leitores')

                                print(f"Enviar proposta de troca para algum dos livros?")
                                escolha_troca = input(
                                    f"{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                                ).upper()

                                if escolha_troca == 'S':
                                    while True:
                                        trocar_x = int(input(f'{bold}{gray}Selecione um dos listados: {end}')) - 1

                                        if 0 <= trocar_x < len(list(leitores[busca]['livros'].keys())):
                                            print(f'{bold}{gray}Selecione um dos listados: {end}')
                                            lista_livros_busca = list(leitores[busca]['livros'].keys())
                                            trocado = lista_livros_busca[trocar_x]
                                            if int(leitores[busca]['livros'][trocado]['pontos']) > int(
                                                    leitores[usuario]['pontos']):
                                                print(f"{red}Você não possui pontos suficientes!{end}\n")
                                                break
                                            else:
                                                leitores[usuario]['pontos'] = int(leitores[usuario]['pontos']) - int(
                                                    leitores[busca]['livros'][trocado]['pontos'])

                                                leitores[busca]['pontos'] = int(leitores[busca]['pontos']) + int(
                                                    leitores[busca]['livros'][trocado]['pontos'])

                                                leitores[busca]['livros'].pop(trocado)
                                                save_dict(leitores, 'leitores')
                                                break
                                        else:
                                            print(f"{red}Opcao inválida!{end}\n")
                                            continue

                        else:
                            print(f"{red}Não há leitores cadastrados!{end}\n")

                    elif opcao_busca == '2':

                        nome_consulta = input(
                            f"{gray}Digite o nome do livro para buscar: {end}")

                        semelhantes = []
                        i_livro = 0
                        for i in leitores:
                            if i == 'posts':
                                continue
                            semelhantes += difflib.get_close_matches(nome_consulta,
                                                                     leitores[i]['livros'].keys(),
                                                                     cutoff=0.5)

                            for livro in semelhantes:
                                if livro in leitores[i]['livros']:
                                    ponto_print = leitores[i]['livros'][semelhantes[i_livro]]['pontos']
                                    semelhantes[
                                        i_livro] = f'{bold}{semelhantes[i_livro]}{end} {gray}{i}{end}\n{bold}{green}{ponto_print} Pontos{end}'

                                    i_livro += 1

                        if not semelhantes:
                            print(f"{red}Nenhum livro encontrado!{end}\n")

                        else:

                            print(f"{orange}- LIVROS ENCONTRADOS -{end}\n")
                            for livro in sorted(semelhantes):
                                print(livro, '\n')
                            print(f"{orange}---------------------{end}")

                    elif opcao_busca == '3':

                        gen_consulta = escolha_genero()

                        livros_gen = []
                        for i in leitores:
                            if i == 'posts':
                                continue
                            for livro in leitores[i]['livros']:
                                if leitores[i]['livros'][livro]['genero'] == gen_consulta:
                                    ponto_print = leitores[i]['livros'][livro]['pontos']
                                    livros_gen.append(
                                        f'{bold}{livro}{end} {gray}{i}{end}\n{bold}{green}{ponto_print} Pontos{end}')

                        if not livros_gen:
                            print(f"{red}Nenhum livro encontrado!{end}\n")
                        else:
                            print(f"{orange}- LIVROS DE {gen_consulta.upper()} -{end}\n")
                            for livro in sorted(livros_gen):
                                print(livro, '\n')
                            print(f"{orange}---------------------{end}")

                    elif opcao_busca == '-1':
                        break
                    else:
                        print(f"{red}Opcao invalida{end}")
            # ========================= PERFIL ============================== #

            elif opcao == '2':
                while True:
                    print(
                        f'\n{bold}{orange}-----{usuario.upper()}-----{end}\n\n{bold}{green}Pontos: {leitores[usuario]["pontos"]}{end}')

                    opcao_perfil = input(f"\n{bold}{orange}----------------------{end}"
                                         f"\n{bold}{blue}1{end} - Editar Conta"
                                         f"\n{bold}{blue}2{end} - Deletar Conta"
                                         f"\n{bold}{blue}3{end} - Livros"
                                         f"\n{bold}{blue}-1{end} - Voltar"
                                         f"\n{gray}Selecione uma das opções: {end}")

                    # ========================= EDITAR CONTA ============================== #

                    if opcao_perfil == '1':
                        print(f"\n{bold}{orange}---------EDITAR CONTA---------{end}")
                        while True:
                            editar = input(
                                f"\n{blue}{bold}1{end} - Editar o Username"
                                f"\n{blue}{bold}2{end} - Editar o nome"
                                f"\n{blue}{bold}3{end} - Editar a data de nascimento"
                                f"\n{blue}{bold}4{end} - Editar a cidade"
                                f"\n{blue}{bold}5{end} - Editar o E-mail"
                                f"\n{blue}{bold}6{end} - Editar a senha:"
                                f"\n{blue}{bold}-1{end} - Sair e salvar alterações"
                                f"\n{gray}Selecione uma das opções:{end} ")

                            if editar == '1':
                                user_temp = check_username(leitores)
                                leitores[user_temp] = leitores.pop(usuario)
                                usuario = user_temp
                                leitores[usuario][user] = usuario
                                save_dict(leitores, 'leitores')
                                print(
                                    f"{green}Username editado com sucesso!{end}\n"
                                )

                            elif editar == '2':
                                leitores[usuario]['nome'] = nome_completo()
                                print(
                                    f"{green}Nome editado com sucesso!\n{end}")
                                save_dict(leitores, 'leitores')

                            elif editar == '3':
                                leitores[usuario]['data'] = check_data()
                                save_dict(leitores, 'leitores')
                                print(
                                    f"{green}Data de nascimento editada com sucesso!\n{end}"
                                )

                            elif editar == '4':
                                leitores[usuario]['cidade'] = cidade()
                                save_dict(leitores, 'leitores')
                                print(
                                    f"{green}Cidade editado com sucesso!\n{end}"
                                )

                            elif editar == '5':
                                leitores[usuario]['email'] = check_email(leitores)
                                save_dict(leitores, 'leitores')
                                print(
                                    f"{green}E-mail editado com sucesso!\n{end}"
                                )

                            elif editar == '6':
                                leitores[usuario]['senha'] = check_senha()
                                save_dict(leitores, 'leitores')
                                print(
                                    f"{green}Senha editada com sucesso!\n{end}"
                                )

                            elif editar == '-1':
                                print(f"{green}Alterações salvas!\n{end}")
                                break

                            else:
                                print(f"{red}Dígito incorreto!\n{end}")

                    # ========================= DELETAR CONTA ===================================== #

                    elif opcao_perfil == '2':
                        print(f"\n{bold}{orange}---------DELETAR CONTA---------{end}")
                        sim_nao = input(
                            f"Você deseja excluir sua conta?"
                            f"\n{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                        )

                        if sim_nao.upper() == 'S':
                            sim_nao = input(
                                f"Você tem certeza?"
                                f"\n{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                            )
                            if sim_nao.upper() == 'S':
                                del leitores[usuario]
                                save_dict(leitores, 'leitores')

                            print(f"{green}Conta removida com sucesso!{end}\n")

                        else:
                            print(f"{red}Conta não removida!{end}\n")

                    # ========================= INICIO DE CRUD(LIVRO) ============================== #

                    elif opcao_perfil == '3':
                        while True:
                            print(f"\n{bold}{orange}---------LIVROS---------{end}")
                            op = input(f"{bold}{blue}1{end} - Adicionar Livro"
                                       f"\n{bold}{blue}2{end} - Buscar Livro"
                                       f"\n{bold}{blue}3{end} - Editar Livro"
                                       f"\n{bold}{blue}4{end} - Deletar Livro"
                                       f"\n{bold}{blue}5{end} - Finalizar"
                                       f"\n{gray}Selecione uma das opções:{end} ")

                            # ========================= CADASTRAR LIVROS ============================== #

                            if op == '1':
                                livro = {}

                                print(f"\n{bold}{orange}---------ADICIONAR LIVRO---------{end}")

                                titulo = (input(f"{gray}Digite o título do livro: {end}"))
                                editora = (input(f"{gray}Digite a editora:  {end}"))
                                autor = (input(f"{gray}Digite o autor: {end}"))
                                ano = int(input(f"{gray}Digite o ano: {end}"))
                                genero = escolha_genero()
                                pontos = input('Selecione a categoria do seu livro:'
                                               f"\n{bold}{blue}1{end} - Capa Dura"
                                               f"\n{bold}{blue}2{end} - Capa Mole"
                                               f"\n{bold}{blue}3{end} - Técnico"
                                               f"\n{gray}Selecione uma das opções: {end}")
                                if pontos == '1':
                                    pontos = 20
                                elif pontos == '2':
                                    pontos = 15
                                elif pontos == '3':
                                    pontos = 30
                                else:
                                    print("Categoria inválida!")
                                    continue
                                livro['editora'] = editora
                                livro['autor'] = autor
                                livro['ano'] = ano
                                livro['genero'] = genero
                                livro['pontos'] = pontos

                                leitores[usuario]['livros'][titulo] = livro
                                save_dict(leitores, 'leitores')

                            # ========================= BUSCAR LIVRO ============================= #

                            elif op == '2':

                                nome_consulta = input(
                                    f"{gray}Digite o nome do livro para buscar: {end}")

                                semelhantes = []
                                i_livro = 0
                                for i in leitores:
                                    if i == 'posts':
                                        continue
                                    semelhantes += difflib.get_close_matches(nome_consulta,
                                                                             leitores[i]['livros'].keys(),
                                                                             cutoff=0.5)

                                    for livro in semelhantes:
                                        if livro in leitores[i]['livros']:
                                            ponto_print = leitores[i]['livros'][semelhantes[i_livro]]['pontos']
                                            semelhantes[
                                                i_livro] = f'{bold}{semelhantes[i_livro]}{end} {gray}{i}{end}\n{bold}{green}{ponto_print} Pontos{end}'

                                            i_livro += 1

                                if not semelhantes:
                                    print(f"{red}Nenhum livro encontrado!{end}\n")

                                else:

                                    print(f"{orange}- LIVROS ENCONTRADOS -{end}\n")
                                    for livro in sorted(semelhantes):
                                        print(livro, '\n')
                                    print(f"{orange}---------------------{end}")

                            # ========================= EDITAR LIVRO ============================== #

                            elif op == '3':
                                nome_consulta = input(
                                    f"{gray}Digite o nome do livro para editar: {end}")

                                semelhantes = difflib.get_close_matches(nome_consulta,
                                                                        leitores[usuario]['livros'].keys(),
                                                                        cutoff=0.5)
                                consulta = listar_opcoes(semelhantes)

                                if not semelhantes:
                                    print(f"{red}Livro não encontrado{end}\n")

                                while True:
                                    print(f"{bold}{blue}1{end} - Nome"
                                          f"\n{bold}{blue}2{end} - Editora"
                                          f"\n{bold}{blue}3{end} - Autor"
                                          f"\n{bold}{blue}4{end} - Ano"
                                          f"\n{bold}{blue}5{end} - Gênero"
                                          f"\n{bold}{blue}6{end} - Sair")

                                    op_editar = input(

                                        f"{gray}Escolha uma opção para editar ou '6' para sair:{end}")

                                    if op_editar == '1':

                                        novo_titulo = input(f"{gray}Digite um novo nome: {end}")

                                        leitores[usuario]['livros'][novo_titulo] = leitores[usuario]['livros'].pop(
                                            consulta)
                                        consulta = novo_titulo
                                        save_dict(leitores, 'leitores')

                                    elif op_editar == '2':

                                        nova_editora = input(f"{gray}Digite uma nova editora: {end}")
                                        leitores[usuario]['livros'][consulta]['editora'] = nova_editora
                                        save_dict(leitores, 'leitores')

                                    elif op_editar == '3':

                                        novo_autor = input(f"{gray}Digite um novo autor: {end}")
                                        leitores[usuario]['livros'][consulta]['autor'] = novo_autor
                                        save_dict(leitores, 'leitores')

                                    elif op_editar == '4':
                                        while True:
                                            ano = int(input(f"{gray}Digite o ano: {end}"))
                                            if ano <= int(str(date.today())[0:4]):
                                                break
                                            else:
                                                print(f"{red}Ano inválido{end}\n")
                                                continue
                                        leitores[usuario]['livros'][consulta]['ano'] = ano
                                        save_dict(leitores, 'leitores')

                                    elif op_editar == '5':
                                        leitores[usuario]['livros'][consulta]['genero'] = escolha_genero()
                                        save_dict(leitores, 'leitores')

                                    elif op_editar == '6':
                                        print(f"{green}Alterações Salvas!{end}")
                                        break

                            # ========================= DELETAR LIVRO ============================== #

                            elif op == '4':
                                if leitores[usuario]['livros']:

                                    nome_consulta = input(f"\n{gray}Qual o livro que deseja deletar? {end}")

                                    semelhantes = difflib.get_close_matches(nome_consulta,
                                                                            leitores[usuario]['livros'].keys(),
                                                                            cutoff=0.5)
                                    livros_usuario = listar_opcoes(semelhantes)

                                    print(f"{gray}Tem certeza que deseja deletar esta informação? {end}")

                                    op_cofirmacao = input(
                                        f"{bold}{blue}S{end}{bold}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}").upper()

                                    if op_cofirmacao.upper() == 'S':
                                        leitores[usuario]['livros'].pop(livros_usuario)
                                        save_dict(leitores, 'leitores')
                                    else:
                                        print(f"\n{red}O livro não foi deletado.{end}")
                                else:
                                    print(f"\n{red}Nenhum livro cadastrado.{end}")
                            # ========================= SAIR DO CRUD DE LIVROS ============================== #

                            elif op == '5':
                                break

                    elif opcao_perfil == '-1':
                        break

                    else:
                        print(f"{red}Opção inválida!{end}\n")

            # ========================= PUBLICAR =========================================== #

            elif opcao == '3':
                while True:
                    escolha_tipo = input(f"\n{bold}{orange}-------- PUBLICAR --------{end}"
                                         f"\n{bold}{blue}1{end} - Geral"
                                         f"\n{bold}{blue}2{end} - Resenha"
                                         f"\n{bold}{blue}3{end} - Avaliacao"
                                         f"\n{bold}{blue}-1{end} - Sair"
                                         f"\n{gray}Selecione uma das opções: {end}")

                    if escolha_tipo == '1':
                        tipo = "Geral"
                        text_publi = input(f"{gray}Escreva sua publicacao: {end}")
                        publicacao = f"{bold}{green}{usuario.upper()} ({tipo}){end} {gray}{semana[datetime.today().weekday()]}, {gray}{datetime.today().hour}:{datetime.today().minute:02d}:{end}\n{end}{bold}{text_publi}{end}"

                    elif escolha_tipo == '2':
                        tipo = "Resenha"
                        titulo_resenha = input(f"{gray}Titulo do Livro: {end}")
                        text_resenha = input(f"{gray}Escreva sua resenha: {end}")
                        publicacao = f"{bold}{green}{usuario.upper()} ({tipo}){end} {gray}{semana[datetime.today().weekday()]}, {gray}{datetime.today().hour}:{datetime.today().minute:02d}:{end}\n{end}{bold}{titulo_resenha.upper()}{end}\n{text_resenha}{end}"

                    elif escolha_tipo == '3':
                        tipo = "Avaliacao"
                        titulo_av = input(f"{gray}Titulo do Livro: {end}")
                        while True:
                            try:
                                nota = int(input(f"{gray}Qual nota (de 0 a 10): {end}"))
                            except:
                                print(f"{red}Valor inválido!{end}\n")
                                continue

                            if 0 <= nota <= 10:
                                break
                            else:
                                print(f"{red}Valor inválido!{end}\n")
                                continue
                        publicacao = f"{bold}{green}{usuario.upper()} ({tipo}){end} {gray}{semana[datetime.today().weekday()]}, {gray}{datetime.today().hour}:{datetime.today().minute:02d}:{end}\n{end}{bold}{titulo_av.upper()} - ({green}{nota}{end}{bold}/10){end}"

                    elif escolha_tipo == '-1':
                        break

                    else:
                        print(f"{red}Opcao inválida!{end}\n")

                    while True:

                        public = input(
                            f"{gray}Deseja publicar?{end}"
                            f"\n{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                        ).upper()

                        if public == 'S':
                            try:
                                leitores['posts'].append(publicacao)
                                print(f"{green}Publicação realizada.{end}\n")
                                save_dict(leitores, 'leitores')
                                break
                            except:
                                leitores['posts'] = []
                                leitores['posts'].append(publicacao)
                                print(f"{green}Publicação realizada.{end}\n")
                                save_dict(leitores, 'leitores')
                                break


                        elif public == 'N':
                            print(f"{red}Publicação deletada.{end}\n")
                            break

                        else:
                            print(f"{red}Opção inválida!{end}\n")
                            continue

            # ========================= CONVERSAS =========================================== #

            elif opcao == '4':
                if leitores[usuario]['chats']:

                    nao_visualizadas = []
                    visualizadas = []
                    escolha_enviar = ''
                    while escolha_enviar != '-1':
                        for user in leitores[usuario]['chats']:

                            if leitores[usuario]['chats'][user][0] != 0:
                                nao_visualizadas.append([f'{bold}{user}{end}',
                                                         f' {bold}{red}{leitores[usuario]["chats"][user][0]} {end}{gray}Mensagen(s) nao lida(s){end}'])
                            else:
                                visualizadas.append([f'{bold}{user}{end}', ''])

                        conversas = nao_visualizadas + visualizadas

                        print(f'{orange}------------------{end}')

                        count_chat = 0
                        for user in conversas:
                            count_chat += 1
                            print(f'{blue}{count_chat}{end} - {user[0]}{user[1]}')
                            print(f'{orange}------------------{end}')
                        try:
                            escolha_chat = int(input(f'{gray}Selecione uma conversa para abrir: {end}'))
                        except:
                            print(f"{red}Opção inválida!{end}\n")
                            break
                        if escolha_chat > len(conversas) or escolha_chat < 1:
                            print(f"{red}Opção inválida!{end}\n")
                            break

                        user = conversas[escolha_chat - 1][0][4:-4]

                        print(f'\n{orange}------{green} {user} {orange}------{end}')

                        for mensagem in leitores[usuario]['chats'][user][1:]:
                            print(mensagem)

                        print(f'{orange}------------------{end}')

                        leitores[usuario]['chats'][user][0] = 0

                        escolha_enviar = input(f"\n{bold}{blue}1{end} - Enviar mensagem\n"
                                               f"{bold}{blue}-1{end} - Voltar\n"
                                               f"{gray}Selecione uma opcao: {end}")
                        if escolha_enviar == '1':
                            enviar_chat(usuario, user, leitores)
                            print(f"{green}Mensagem enviada!{end}\n")
                            break
                        elif escolha_enviar != '-1':
                            print(f"{red}Opção inválida!{end}\n")
                            break
                    save_dict(leitores, 'leitores')
                else:

                    print(f"{gray}Nenhum chat iniciado.{end}")
            # ====================== CRUD LIVROS ===========================#
            elif opcao == '5':
                while True:
                    print(f"\n{bold}{orange}---------LIVROS---------{end}")
                    op = input(f"{bold}{blue}1{end} - Adicionar Livro"
                               f"\n{bold}{blue}2{end} - Buscar Livro"
                               f"\n{bold}{blue}3{end} - Editar Livro"
                               f"\n{bold}{blue}4{end} - Deletar Livro"
                               f"\n{bold}{blue}5{end} - Finalizar"
                               f"\n{gray}Selecione uma das opções:{end} ")

                    # ========================= CADASTRAR LIVROS ============================== #

                    if op == '1':
                        livro = {}

                        print(f"\n{bold}{orange}---------ADICIONAR LIVRO---------{end}")

                        titulo = (input(f"{gray}Digite o título do livro: {end}"))
                        editora = (input(f"{gray}Digite a editora:  {end}"))
                        autor = (input(f"{gray}Digite o autor: {end}"))
                        ano = int(input(f"{gray}Digite o ano: {end}"))
                        genero = escolha_genero()
                        pontos = input('Selecione a categoria do seu livro:'
                                       f"\n{bold}{blue}1{end} - Capa Dura"
                                       f"\n{bold}{blue}2{end} - Capa Mole"
                                       f"\n{bold}{blue}3{end} - Técnico"
                                       f"\n{gray}Selecione uma das opções: {end}")
                        if pontos == '1':
                            pontos = 20
                        elif pontos == '2':
                            pontos = 15
                        elif pontos == '3':
                            pontos = 30
                        else:
                            print("Categoria inválida!")
                            continue
                        livro['editora'] = editora
                        livro['autor'] = autor
                        livro['ano'] = ano
                        livro['genero'] = genero
                        livro['pontos'] = pontos

                        leitores[usuario]['livros'][titulo] = livro
                        save_dict(leitores, 'leitores')

                    # ========================= BUSCAR LIVRO ============================= #

                    elif op == '2':

                        nome_consulta = input(
                            f"{gray}Digite o nome do livro para buscar: {end}")

                        semelhantes = []
                        i_livro = 0
                        for i in leitores:
                            if i == 'posts':
                                continue
                            semelhantes += difflib.get_close_matches(nome_consulta,
                                                                     leitores[i]['livros'].keys(),
                                                                     cutoff=0.5)

                            for livro in semelhantes:
                                if livro in leitores[i]['livros']:
                                    ponto_print = leitores[i]['livros'][semelhantes[i_livro]]['pontos']
                                    semelhantes[
                                        i_livro] = f'{bold}{semelhantes[i_livro]}{end} {gray}{i}{end}\n{bold}{green}{ponto_print} Pontos{end}'

                                    i_livro += 1

                        if not semelhantes:
                            print(f"{red}Nenhum livro encontrado!{end}\n")

                        else:

                            print(f"{orange}- LIVROS ENCONTRADOS -{end}\n")
                            for livro in sorted(semelhantes):
                                print(livro, '\n')
                            print(f"{orange}---------------------{end}")

                    # ========================= EDITAR LIVRO ============================== #

                    elif op == '3':
                        nome_consulta = input(
                            f"{gray}Digite o nome do livro para editar: {end}")

                        semelhantes = difflib.get_close_matches(nome_consulta,
                                                                leitores[usuario]['livros'].keys(),
                                                                cutoff=0.5)
                        consulta = listar_opcoes(semelhantes)

                        if not semelhantes:
                            print(f"{red}Livro não encontrado{end}\n")

                        while True:
                            print(f"{bold}{blue}1{end} - Nome"
                                  f"\n{bold}{blue}2{end} - Editora"
                                  f"\n{bold}{blue}3{end} - Autor"
                                  f"\n{bold}{blue}4{end} - Ano"
                                  f"\n{bold}{blue}5{end} - Gênero"
                                  f"\n{bold}{blue}6{end} - Sair")

                            op_editar = input(

                                f"{gray}Escolha uma opção para editar ou '6' para sair:{end}")

                            if op_editar == '1':

                                novo_titulo = input(f"{gray}Digite um novo nome: {end}")

                                leitores[usuario]['livros'][novo_titulo] = leitores[usuario]['livros'].pop(
                                    consulta)
                                consulta = novo_titulo
                                save_dict(leitores, 'leitores')

                            elif op_editar == '2':

                                nova_editora = input(f"{gray}Digite uma nova editora: {end}")
                                leitores[usuario]['livros'][consulta]['editora'] = nova_editora
                                save_dict(leitores, 'leitores')

                            elif op_editar == '3':

                                novo_autor = input(f"{gray}Digite um novo autor: {end}")
                                leitores[usuario]['livros'][consulta]['autor'] = novo_autor
                                save_dict(leitores, 'leitores')

                            elif op_editar == '4':
                                while True:
                                    ano = int(input(f"{gray}Digite o ano: {end}"))
                                    if ano <= int(str(date.today())[0:4]):
                                        break
                                    else:
                                        print(f"{red}Ano inválido{end}\n")
                                        continue
                                leitores[usuario]['livros'][consulta]['ano'] = ano
                                save_dict(leitores, 'leitores')

                            elif op_editar == '5':
                                leitores[usuario]['livros'][consulta]['genero'] = escolha_genero()
                                save_dict(leitores, 'leitores')

                            elif op_editar == '6':
                                print(f"{green}Alterações Salvas!{end}")
                                break

                    # ========================= DELETAR LIVRO ============================== #

                    elif op == '4':
                        if leitores[usuario]['livros']:

                            nome_consulta = input(f"\n{gray}Qual o livro que deseja deletar? {end}")

                            semelhantes = difflib.get_close_matches(nome_consulta,
                                                                    leitores[usuario]['livros'].keys(),
                                                                    cutoff=0.5)
                            livros_usuario = listar_opcoes(semelhantes)

                            print(f"{gray}Tem certeza que deseja deletar esta informação? {end}")

                            op_cofirmacao = input(
                                f"{bold}{blue}S{end}{bold}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}").upper()

                            if op_cofirmacao.upper() == 'S':
                                leitores[usuario]['livros'].pop(livros_usuario)
                                save_dict(leitores, 'leitores')
                            else:
                                print(f"\n{red}O livro não foi deletado.{end}")
                        else:
                            print(f"\n{red}Nenhum livro cadastrado.{end}")
                    # ========================= SAIR DO CRUD DE LIVROS ============================== #

                    elif op == '5':
                        break

                    else:
                        print(f"{red}Opção inválida!{end}\n")

            # ========================= INICIO GAMIFICAÇÃO ============================== #

            elif opcao == '6':
                while True:
                    op_game = input(f"\nDigite qual missão você deseja realizar:"
                                    f"\n{bold}{blue}1{end} - Doe 5 Livros"
                                    f"\n{bold}{blue}2{end} - Doe R$30"
                                    f"\n{bold}{blue}3{end} - Doe 10 Livros"
                                    f"\n{bold}{blue}4{end} - Doe R$50"
                                    f"\n{bold}{blue}5{end} - Voltar"
                                    f"\n{gray}Selecione uma das opções: {end}")

                    if op_game == '1':
                        print(f"{green}Parabéns, você doou 5 livros. Você ganhou +7 pontos!{end}\n")
                        leitores[usuario]['pontos'] += 7
                        save_dict(leitores, 'leitores')
                        continue

                    elif op_game == '2':
                        print(f"{green}Parabéns, você doou R$30. Você ganhou +7 pontos pela boa ação!{end}\n")
                        leitores[usuario]['pontos'] += 7
                        save_dict(leitores, 'leitores')
                        continue

                    elif op_game == '3':
                        print(f"{green}Parabéns, você doou 5 livros. Você ganhou +7 pontos!{end}\n")
                        leitores[usuario]['pontos'] += 7
                        save_dict(leitores, 'leitores')
                        continue

                    elif op_game == '4':
                        print(f"{green}Parabéns, você doou R$50. Você ganhou +7 pontos pela boa ação!{end}\n")
                        leitores[usuario]['pontos'] += 7
                        save_dict(leitores, 'leitores')
                        continue

                    elif op_game == '5':
                        break

                    else:
                        print(f"{red}Missão inválida!{end}\n")
                        continue


            # ========================= SAIR DA CONTA LOGADA =============================== #

            elif opcao == '-1':
                logado = False
                print(f"{red}Conta desconectada{end}\n")
            else:
                print(f"{red}Opção inválida!{end}\n")
    elif opcao_log == '-1':
        break
    else:
        print(f"{red}Código inválido{end}\n")

print(f"{red}Programa encerrado pelo usuário{end}")
