print(playlist)

playlist = ["maknae on top", "divine", "japao vs frança", "do it", "lana"]
add = input("Voce quer adicionar alguma musica? (S/N)")
remove = input("Deseja remover alguma musica? (S/N)")

if add == "S":
    musica_add = input("Nome da musica: ")
    playlist.append(musica_add)
    print("Musica adicionada com sucesso!")
    print(playlist)
elif add == "N":
    print("Nenhuma música foi adicionada.")
else:
    print("Resposta inválida!")

if remove == "S":
    remove_playlist = input("Qual musica voce quer remover? ")
    playlist.remove(remove_playlist)
    print("Musica removida com sucesso!")
    print(playlist)
elif remove == "N":
     print("Nenhuma música foi removida.")
else:
    print("Resposta inválida!")
