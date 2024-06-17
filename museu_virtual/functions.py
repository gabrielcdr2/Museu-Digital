from os import system
from time import sleep
from datetime import datetime

def bubble_sort(lista):
    qtd = len(lista)
    for i in range(qtd):
        for indice in range(0, qtd-i-1):
            if lista[indice] > lista[indice+1]:
                lista[indice], lista[indice+1] = lista[indice+1], lista[indice]
    return lista

def login(users):
    while True:
        print('='*20)
        print('Museu Digital')
        print('='*20)

        login = input('Login: ')
        password = input('Senha: ')

        i = 0
        for user in users:
            if login == user["login"]:
                if password == user["password"]:
                    return user["acess_type"]
                else:
                    print('Senha incorreta!')
                    sleep(1.2)
                    system('cls')
                    continue
            else:
                i += 1
                if i >= len(users):
                    print('Usuário não encontrado!')
                    sleep(1.2)
                    system('cls')
                    continue

def explorar(artes, obras_alugadas):
    system('cls')
    print('Obras do museu: \n')

    titulos = []
    for obra in artes:
        titulos.append(obra["title"])
    titulos_ordenados = bubble_sort(titulos)
    for i, name in enumerate(titulos_ordenados):
        print(f'{i+1} - {name}' )

    selection = input('\nSelecione uma obra: ')
    try:
        int(selection)
        if int(selection) > len(titulos_ordenados):
            print('Selecione uma opção válida.')
            sleep(1.5)
            system('cls')

    except ValueError:
        print('Você digitou um caractere inválido')
        sleep(1.5)
        system('cls')
        
    obra_escolhida = titulos_ordenados[int(selection)-1]
        
    for obra in artes:
        if obra_escolhida == obra["title"]:
            while True:
                system('cls')
                print('Obra selecionada: \n')
                print(f'Título: {obra["title"]}')
                print(f'Autor(a): {obra["author"]}')
                print(f'Data de lançamento: {obra["date"]}')
                print(f'Estilo: {obra["style"]}')
                print(f'Técnica usada: {obra["tecnica"]}')
                print(f'\nDescrição: {obra["description"]}')
                alugar = input('\nDeseja alugar?[S/N]: ')

                if alugar.lower() == 's' or alugar.lower == 'sim':
                    system('cls')
                    nome = input('Responsável: ')
                    nome_evento = input('Nome do evento: ')
                    tema = input('Tema: ')
                    tempo = input('Período de empréstismo: ')
                    obras_alugadas.append(obra_escolhida)
                    log_registros(obra_escolhida)
                    print('\nObra alugada com sucesso!')
                    print('Retornando ao início...')
                    sleep(1.5)
                    system('cls')
                    break
                elif alugar.lower() == 'n' or alugar.lower == 'nao':
                    print('Retornando ao início...')
                    sleep(1.5)
                    system('cls')
                    break

def aba_artistas(lista):
    while True:
        system('cls')
        print("Conheça nossos artistas:\n ")
        for i, artista in enumerate(lista):
            print(f"{i+1} - {artista["nome"]}")
        
        selecao = input('\nSelecione um artista: ')

        try:
            int(selecao)
            if int(selecao) > len(lista):
                print('Selecione uma opção válida.')
                sleep(1.5)
                system('cls')

        except ValueError:
            print('Você digitou um caractere inválido')
            sleep(1.5)
            system('cls')

        system('cls')
        print(f'{lista[int(selecao)-1]["nome"]} \n')
        print(f'Data e local de nascimento: {lista[int(selecao)-1]["nascimento"]}, {lista[int(selecao)-1]["local_nascimento"]}')
        print(f'Estilo: {lista[int(selecao)-1]["estilo"]}')
        print(f'Biografia: {lista[int(selecao)-1]["biografia"]}')
        
        input('\nPressiona qualquer tecla para continuar...')
        system('cls')
        break
        
def agendar_visita(lista, roteiro):
    while True:
        system('cls')
        print('AGENDAMENTO DE VISITA GUIADA\n')
        responsavel = input('Organização/Pessoa responsavel pela visita: ')
        qtd = input('Quantidade de visitantes: ')
        data = input('Data e hora da visita: ')
        tema = input('Tema: ')
        descricao = input('Descrição detalhada da visita: ')

        pesquisa = input('\nDeseja selecionar obras para a visita guiada?[S/N]: ')
        
        if pesquisa.lower() == 's' or pesquisa.lower() == 'sim':
            pesquisar_obras(lista, roteiro)
            log_registros_visitas(responsavel, data)
            print('Visita agendada com sucesso!\n Retornando ao início...')
            sleep(2)
            system('cls')
            break

        elif pesquisa.lower() == 'n' or pesquisa.lower() == 'não':
            system('cls')
            print('Visita agendada:\n ')
            print(f'A visita ao museu foi marcada para o dia {data}\nTema: {tema}\nDescrição: {descricao}')
            input('\nPressione qualquer tecla para confirmar e voltar ao início.')
            break

def pesquisar_obras(lista, roteiro):
    while True:
        pesquisa = input('Digite o nome da obra: ')
        obra_encontrada = False  # Flag to check if the obra was found
        for item in lista:
            if pesquisa == item["title"]:
                obra = item["title"]
                roteiro.append(obra)
                obra_encontrada = True
                break  # Exit the loop if the obra is found
        if obra_encontrada:
            print(f'Obra "{pesquisa}" adicionada ao roteiro.')
        else:
            print('Obra não encontrada!')

        # Option to exit the loop
        continuar = input('Deseja continuar pesquisando? (s/n): ')
        if continuar.lower() != 's':
            break

def log_registros(name):
    with open('log', 'a') as registros_de_alugueis:
        registros_de_alugueis.write(f"\nA obra {name} foi alugada na data {datetime.now()} pelo usuario")

def log_registros_visitas(nome, data):
    with open('agenda', 'a') as registros_de_visitas:
        registros_de_visitas.write(f"\nUma visita foi agendada para {data}, no nome de {nome}. Visita agendadada na data {datetime.now()}")