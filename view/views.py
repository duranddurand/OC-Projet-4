
def print_view(preview) -> str:
    view_dict = {
        1: "######## Bienvenue ######## \n\n1: Tournois \n2: Joueurs \n3: Quitter",
        2: "######## Tournois ######## \n\n1: Nouveau \n2: Reprende \n3: Historique \n4: Retour",
        3: "######## Joueurs ######## \n\n1: Ajouter \n2: Modifier \n3: Classement \n4: Retour",
        4: "######## Classement ######## \n\n1: Afficher \n2: Modifier \n3: Retour"

    }
    print(view_dict[preview])
