playlist = [
    "S-Class",
    "Maniac",
    "God's Menu",
    "Thunderous",
    "Back Door"
]

while True:
    print("\n===== PLAYLIST =====")
    print("1 - Adicionar música")
    print("2 - Remover música")
    print("3 - Trocar posição de músicas")
    print("4 - Exibir playlist")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        musica = input("Nome da música: ")
        playlist.append(musica)
        print("Música adicionada!")

    elif opcao == 2:
        musica = input("Nome da música que deseja remover: ")

        if musica in playlist:
            playlist.remove(musica)
            print("Música removida!")
        else:
            print("Música não encontrada.")

    elif opcao == 3:
        for i, musica in enumerate(playlist, start=1):
            print(i, "-", musica)

        p1 = int(input("Primeira posição: "))
        p2 = int(input("Segunda posição: "))

        if 1 <= p1 <= len(playlist) and 1 <= p2 <= len(playlist):
            playlist[p1 - 1], playlist[p2 - 1] = playlist[p2 - 1], playlist[p1 - 1]
            print("Posições trocadas!")
        else:
            print("Posição inválida!")

    elif opcao == 4:
        print("\nSua playlist:")

        for i, musica in enumerate(playlist, start=1):
            print(i, "-", musica)

    elif opcao == 5:
        print("Encerrando playlist...")
        break

    else:
        print("Opção inválida!")