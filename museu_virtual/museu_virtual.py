import functions, os, time

users = [
    {"login": "admin", "password": "admin", "acess_type": "admin"},
    {"login": "usuario", "password": "usuario123", "acess_type": "comum"}
]

artistas_cadastrados = [
     {
        "nome": "Van Gogh",
        "nascimento": "00/06/0000",
        "estilo": "Pós impressionismo",
        "local_nascimento": "Brasil",
        "biografia": "Vincent Willem van Gogh foi um pintor pós-impressionista neerlandês. Considerado uma das figuras mais famosas e influentes da história da arte ocidental, criou mais de dois mil trabalhos ao longo ..."
      }
]

artes = [
     {
        "title": "A NOITE ESTRELADA",
        "date": "10/06/1889",
        "theme": "PINTURA",
        "style": "EXPRESSIVO",
        "author": "VAN GOGH",
        "tecnica": "PICELADA FIRME",
        "description": "A Noite Estrelada é uma pintura de Vincent van Gogh de 1889. A obra retrata a vista da janela de um quarto do hospício de Saint-Rémy-de-Provence, pouco antes do nascer do sol, com a adição de um vilarejo idealizado pelo artista."
      },
      {
        "title": "MONA LISA",
        "date": "10/06/1889",
        "theme": "PINTURA",
        "style": "EXPRESSIVO",
        "author": "VAN GOGH",
        "tecnica": "PICELADA FIRME",
        "description": "A Noite Estrelada é uma pintura de Vincent van Gogh de 1889. A obra retrata a vista da janela de um quarto do hospício de Saint-Rémy-de-Provence, pouco antes do nascer do sol, com a adição de um vilarejo idealizado pelo artista."
      },
      {
        "title": "ABAPORU",
        "date": "10/06/1889",
        "theme": "PINTURA",
        "style": "EXPRESSIVO",
        "author": "VAN GOGH",
        "tecnica": "PICELADA FIRME",
        "description": "A Noite Estrelada é uma pintura de Vincent van Gogh de 1889. A obra retrata a vista da janela de um quarto do hospício de Saint-Rémy-de-Provence, pouco antes do nascer do sol, com a adição de um vilarejo idealizado pelo artista."
      } 
]

obras_alugadas = []
obras_roteiro = []

def main():
    acess = functions.login(users)
    os.system('cls')
    
    while True:
        if acess == "comum":
                print("-"*24)
                print(f'{"Museu Virtual":^25} ')
                print("-"*24)
                print("1 - Explorar obras")
                print("2 - Conheça os artistas")
                print("3 - Agendar visita")
                print("4 - Sair\n")

                selection = input('Selecione uma das opções acima: ')

                try:
                     int(selection)
                     if int(selection) > 4:
                          print('Selecione uma opção válida.')
                          time.sleep(1.5)
                          os.system('cls')
                          continue

                except ValueError:
                    print('Você digitou um caractere inválido')
                    time.sleep(1.5)
                    os.system('cls')
                    continue

                if selection == '1':
                    functions.explorar(artes, obras_alugadas)
                elif selection == '2':
                    functions.aba_artistas(artistas_cadastrados)
                elif selection == '3':
                    functions.agendar_visita(artes, obras_roteiro)
                else:
                     break

if __name__ == "__main__":
    main()
