from datetime import date, datetime  # Para calculo de idade e momento de realizacao dos posts

end, bold = '\033[0m', '\033[1m'
red, green, blue, orange, gray = '\033[91m', '\033[32m', '\033[34m', '\033[33m', '\033[1m\033[90m'
semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]


# ================================== DEFINICOES DE FUNCOES ====================================== #


def read_dict(nome_arquivo):
    txt = open(f'{nome_arquivo}.txt', 'r', encoding='utf8')
    dicionario = txt.read()
    txt.close()
    if dicionario == '':
        return {}
    return eval(dicionario)


def save_dict(dic, file):
    txt = open(f'{file}.txt', 'w', encoding='utf8')
    txt.write(str(dic))
    txt.close()


# ================================ LISTAR E SELECIONAR =================================== #

def listar_opcoes(lista):
    if not lista:
        return ''
    while True:
        for i in range(len(lista)):
            print(f"{bold}{blue}{i + 1}{end} - {lista[i]}")

        escolha = int(input(f"{gray}Selecione uma das opções:{end} \n"))

        if len(lista) >= escolha > 0:
            break
        else:
            print(f"{red}Código inválido.{end}\n")

    return lista[escolha - 1]


# ================================ VERIFICAR FORMATO DA SENHA =================================== #

def check_senha():
    print("Digite sua senha, ela deve ter de 6 a 16 Caracteres")
    while True:
        sen = input(f"{gray}Senha: {end}")
        if len(sen) < 6:
            print(f"{red}Sua senha deve ter mais de 6 dígitos{end}\n")
            continue
        elif len(sen) > 16:
            print(f"{red}Sua senha deve ter menos de 16 caracteres{end}\n")
            continue

        check = input(f"{gray}Confirme sua senha: {end}")
        if sen != check:
            print(f"{red}As senhas não são iguais{end}\n")
            continue
        else:
            break
    return sen


# =========================== VERIFICAR EXISTENCIA DO NOME DE USUARIO ============================ #

def check_username(leitores):
    print("Digite um Username, ele deve ter de 4 a 16 caracteres: "),
    while True:
        username = input(f"{gray}Username: {end}")
        if username.__len__() <= 4:
            print(f"{red}Seu username deve ter mais de 4 dígitos{end}\n")
            continue
        elif username.__len__() >= 16:
            print(f"{red}Seu username deve ter menos de 16 caracteres{end}\n")
            continue
        if username in leitores:
            print(f"{red}Username não disponível{end}\n")
            continue
        else:
            break
    return username


# ================================ VERIFICAR INPUT DE NOME ====================================== #

def nome_completo():
    return input(f"{gray}Nome completo: {end}")


# ========================= VERIFICAR FORMATO E EXISTENCIA DO EMAIL ============================== #

def check_email(leitores):
    while True:
        email = input(f"{gray}E-mail: {end}")
        if email in leitores:
            print(f"{red}E-mail já cadastrado{end}\n")
            continue
        if '.' not in email and '@' not in email:  # verificar ':'?
            print(f"{red}E-mail inválido{end}\n")
        else:
            break
    return email


# ========================= VERIFICAR FORMATO DA DATA E IDADE(+18) ============================== #

def idade(nascimento):
    hoje = date.today()
    return hoje.year - nascimento[2] - ((hoje.month, hoje.day) < (nascimento[1], nascimento[0]))


def check_formato(data):
    if len(data) == 10 and data[2] == '/' and data[5] == '/' and \
            data[:2].isdigit() and data[3:5].isdigit() and data[6:].isdigit():
        return True
    return False


def check_data():
    while True:
        data = input(f"{gray}Data de nascimento (dd/mm/aaaa): {end}")
        dia_mes_ano = []
        if check_formato(data):
            dia_mes_ano = data.split('/')
            dia_mes_ano[0] = int(dia_mes_ano[0])
            dia_mes_ano[1] = int(dia_mes_ano[1])
            dia_mes_ano[2] = int(dia_mes_ano[2])
            if idade(dia_mes_ano) >= 18:
                break
            else:
                print(
                    f"{red}Idade inválida, só é permitido maiores de 18{end}\n"
                )
                continue
        else:
            print(f"{red}Formato inválido{end}\n")
            continue
    return dia_mes_ano


# ================================ VERIFICAR CIDADE =================================== #

def cidade():
    while True:
        sn = input(
            "Você mora em Recife?"
            f"\n{blue}{bold}S{end}{gray} - Sim / {blue}{bold}N{end}{gray} - Não: {end}").upper()
        if sn == 'S':
            cid = "Recife"
            break
        elif sn == 'N':
            cid = input(f"{gray}Digite o nome da sua cidade: {end}")
            print(
                f"{red}Você pode entrar na plataforma, mas não pode realizar trocas.\n{end}"
            )
            break
    return cid


# ================================ ESCOLHA GÊNERO =================================== #
# Pretendemos utilizar a funcao listar e selecionar para nao precisarmos mais desta

def escolha_genero():
    print(f"\nEscolha o Gênero: "
          f"\n{bold}{blue}1{end} - Autoajuda"
          f"\n{bold}{blue}2{end} - Científico"
          f"\n{bold}{blue}3{end} - Comédia"
          f"\n{bold}{blue}4{end} - Drama"
          f"\n{bold}{blue}5{end} - Fantasia"
          f"\n{bold}{blue}6{end} - Ficção"
          f"\n{bold}{blue}7{end} - Poesia"
          f"\n{bold}{blue}8{end} - Religião"
          f"\n{bold}{blue}9{end} - Romance"
          f"\n{bold}{blue}10{end} - Suspense"
          f"\n{bold}{blue}11{end} - Terror"
          f"\n{bold}{blue}12{end} - Outro")

    genero = input(f"\n{gray}Selecione uma das opções: {end}")

    if genero == '1':
        gen = "Autoajuda"
    elif genero == '2':
        gen = "Científico"
    elif genero == '3':
        gen = "Comédia"
    elif genero == '4':
        gen = "Drama"
    elif genero == '5':
        gen = "Fantasia"
    elif genero == '6':
        gen = "Ficção"
    elif genero == '7':
        gen = "Poesia"
    elif genero == '8':
        gen = "Religião"
    elif genero == '9':
        gen = "Romance"
    elif genero == '10':
        gen = "Suspense"
    elif genero == '11':
        gen = "Terror"
    elif genero == '12':
        gen = "Outro"
    else:
        print(f"{red}Opção inválida!{end}\n")
        gen = ''
    return gen


def pergunta_secreta():
    print(f"{gray}Escolha uma das perguntas que será a sua pergunta de segurança: {end}")
    perguntas = [f'{gray}Qual seu livro infantil favorito? {end}',
                 f'{gray}Qual o nome do seu primeiro pet? {end}',
                 f'{gray}Qual o nome da sua primeira escola? {end}',
                 f'{gray}Qual cidade os seus pais se conheceram? {end}',
                 f'{gray}Qual era o nome do seu melhor amigo na adolescência? {end}']

    return listar_opcoes(perguntas)


def enviar_chat(envia, recebe, leitores):
    chat = input("Escreva: ")
    chat_verde = f"{bold}{green}{envia}{end} {gray}{datetime.today().hour}:{datetime.today().minute:02d}:{end} {chat}"
    chat_laranja = f"{bold}{orange}Você{end} {gray}{datetime.today().hour}:{datetime.today().minute:02d}:{end} {chat}"
    if recebe in leitores[envia]['chats']:
        leitores[envia]['chats'][recebe].append(chat_laranja)
    else:
        leitores[envia]['chats'][recebe] = [0]
        leitores[envia]['chats'][recebe].append(chat_laranja)

    if envia in leitores[recebe]['chats']:
        leitores[recebe]['chats'][envia][0] += 1
        leitores[recebe]['chats'][envia].append(chat_verde)
    else:
        leitores[recebe]['chats'][envia] = [1]
        leitores[recebe]['chats'][envia].append(chat_verde)

    save_dict(leitores, 'leitores')
