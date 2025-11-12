import random
import time

# ok alors g trouvé ces symboles sur le site donné en consigne
# dictionnaire avec les choix et leurs symboles unicode
mes_choix = {
    "pierre": "✊",  # le poing fermé
    "papier": "✋",  # la main ouverte
    "ciseaux": "✂"   # les ciseaux (j'ai pris celui du site)
}

# liste de tuples comme demandé
# (gagnant, perdant) pour savoir qui bat qui
regles = [
    ("pierre", "ciseaux"),  # la pierre casse les ciseaux
    ("papier", "pierre"),   # le papier enveloppe la pierre
    ("ciseaux", "papier")   # les ciseaux coupent le papier
]

# dictionnaire pour compter les points
# je le mets global pcq plus simple
compteur_score = {
    "joueur": 0,
    "ordi": 0,
    "match_nul": 0
}

# Bonus demandé : fonction pour afficher lettre par lettre
def ecrire_doucement(texte, vitesse=0.02):
    """
    Cette fonction affiche le texte lettre par lettre comme demandé
    
    Paramètres:
        texte : le texte à afficher
        vitesse : le temps entre chaque lettre
    """
    for lettre in texte:
        print(lettre, end='', flush=True)  # le flush c'est pour forcer l'affichage (j'avoue m'être aidé de l'ia pr ca sorry)
        time.sleep(vitesse)
    print()  # retour à la ligne

def montrer_titre():
    """
    Affiche le titre du jeu avec des symboles
    """
    # j'ai trouvé ces symboles sur le site unicode
    print("\n")
    print("""
 ░█▀█░▀█▀░█▀▀░█▀▄░█▀▄░█▀▀░░░█▀█░█▀█░█▀█░▀█▀░█▀▀░█▀▄░░░█▀▀░▀█▀░█▀▀░█▀▀░█▀█░█░█░█░█
 ░█▀▀░░█░░█▀▀░█▀▄░█▀▄░█▀▀░░░█▀▀░█▀█░█▀▀░░█░░█▀▀░█▀▄░░░█░░░░█░░▀▀█░█▀▀░█▀█░█░█░▄▀▄
 ░▀░░░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀░░░▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀
    """)
    ecrire_doucement("    Bienvenue à toi JC", 0.03)
    print()

def afficher_les_scores():
    """
    Montre le score actuel de la partie
    """
    print("\n")
    print(f" ☺ JC     : {compteur_score['joueur']:2d} points")
    print(f" ☻ Ordinateur: {compteur_score['ordi']:2d} points")
    print(f" ⚖ Égalités : {compteur_score['match_nul']:2d}      ")
    

def demander_choix_joueur():
    """
    Demande au joueur ce qu'il veut jouer
    
    Returns:
        le choix du joueur ou 'stop' pour arrêter
    """
    # liste des choix possibles pour la validation
    choix_ok = ["pierre", "papier", "ciseaux", "p", "f", "c", "1", "2", "3", "stop", "quitter", "q"]
    
    while True:  # boucle jusqu'à avoir un bon choix
        print("\n➤ choisis ton arme ?")
        print("  ① Pierre " + mes_choix["pierre"])
        print("  ② Papier " + mes_choix["papier"])
        print("  ③ Ciseaux " + mes_choix["ciseaux"])
        print("  ✖ [Q]uitter")
        
        reponse = input("\n☞ ton choix : ").lower().strip()
        
        # bcl if pour tous les cas possibles
        if reponse in ["1", "p", "pierre"]:
            return "pierre"
        elif reponse in ["2", "f", "papier", "feuille"]:
            return "papier"
        elif reponse in ["3", "c", "ciseaux"]:
            return "ciseaux"
        elif reponse in ["q", "stop", "quitter", "exit", "fin"]:
            return "stop"
        else:
            # warning demandé dans la consigne
            print("\n⚠ WARNING : Ce n'est pas un choix valide !")
            print("   Essaie encore stp...")
            time.sleep(1)  # petite pause pour lire le message

def choix_ordinateur():
    """
    L'ordinateur choisit au hasard
    
    Returns:
        son choix (pierre, papier ou ciseaux)
    """
    # je convertis en liste pour utiliser random.choice
    liste_choix = list(mes_choix.keys())
    choix = random.choice(liste_choix)
    return choix

def qui_gagne(choix_joueur, choix_ordi):
    """
    Détermine qui gagne le tour
    
    Args:
        choix_joueur : ce que le joueur a choisi
        choix_ordi : ce que l'ordi a choisi
    
    Returns:
        'joueur', 'ordi' ou 'nul'
    """
    # cas d'égalité d'abord
    if choix_joueur == choix_ordi:
        return "nul"
    
    # je parcours ma liste de tuples pour voir si le joueur gagne
    for regle in regles:
        if regle[0] == choix_joueur and regle[1] == choix_ordi:
            return "joueur"
    
    # si c'est pas nul et le joueur gagne pas, c'est l'ordi
    return "ordi"

def montrer_resultat(choix_j, choix_o, gagnant):
    """
    Affiche le résultat du tour avec des jolis symboles
    
    Args:
        choix_j : choix du joueur
        choix_o : choix de l'ordinateur
        gagnant : qui a gagné
    """
    print("\n" + "◆" * 35)
    print(f"\n  ☺ Tu avais joué : {mes_choix[choix_j]} {choix_j.upper()}")
    time.sleep(0.5)
    print(f"  ☻ L'ordi a joué  : {mes_choix[choix_o]} {choix_o.upper()}")
    time.sleep(0.5)
    
    # selon qui gagne j'affiche un message différent
    if gagnant == "joueur":
        ecrire_doucement("\n  ✰ ✰ ✰ BRAVO ! t'es trop chaud ! ✰ ✰ ✰", 0.02)
        compteur_score["joueur"] += 1
    elif gagnant == "ordi":
        ecrire_doucement("\n  ☹ Dommage... L'ordinateur gagne...", 0.02)
        compteur_score["ordi"] += 1
    else:
        ecrire_doucement("\n  ⚖ Égalité ! Personne ne gagne.", 0.02)
        compteur_score["match_nul"] += 1
    
    print("◆" * 35)

def jouer_un_tour():
    """
    Fonction pour jouer un tour complet
    
    Returns:
        True pour continuer, False pour arrêter
    """
    # on demande au joueur
    choix_j = demander_choix_joueur()
    
    # si il veut arrêter on retourne False
    if choix_j == 'stop':
        return False
    
    # sinon l'ordi joue aussi
    choix_o = choix_ordinateur()
    
    # on regarde qui gagne
    resultat = qui_gagne(choix_j, choix_o)
    
    # on affiche tout ça
    montrer_resultat(choix_j, choix_o, resultat)
    
    return True  # on continue

def affichage_final():
    """
    Affiche le score final et qui a gagné la partie
    """
    print("\n" + "═" * 50)
    ecrire_doucement("       ☆ ★ FIN DE LA PARTIE ★ ☆", 0.04)
    print("═" * 50)
    
    # je montre les scores finaux
    print(f"\n  RÉSULTATS FINAUX :")
    print(f"  ──────────────────")
    print(f"  ☺ JC      : {compteur_score['joueur']} victoires")
    print(f"  ☻ Ordinateur : {compteur_score['ordi']} victoires")
    print(f"  ⚖ Égalités  : {compteur_score['match_nul']}")
    
    # on détermine le grand gagnant
    print()
    if compteur_score['joueur'] > compteur_score['ordi']:
        ecrire_doucement("  ♛ FÉLICITATIONS cher avenger ! ♛", 0.03)
        print("         ✰ ✰ ✰ ✰ ✰")
    elif compteur_score['ordi'] > compteur_score['joueur']:
        ecrire_doucement("  ☹ L'ordinateur remporte la partie...", 0.03)
        print("    Mais tu peux prendre ta revanche !")
    else:
        ecrire_doucement("  ⚖ Match nul ! te êtes de force égale !", 0.03)

def main():
    """
    Fonction principale qui fait tourner le jeu
    """
    # Message de bienvenue
    montrer_titre()
    ecrire_doucement("  L'ordinateur te défie ! ⚔", 0.03)
    time.sleep(1)
    
    # Variables pour la boucle principale
    continuer = True
    nb_tours = 0
    
    # Boucle principale du jeu (comme demandé dans la consigne)
    while continuer == True:
        afficher_les_scores()
        continuer = jouer_un_tour()
        nb_tours = nb_tours + 1
        
        # petite pause entre les tours pour bien voir
        if continuer:
            time.sleep(1.5)
    
    # Quand on sort de la boucle c'est fini
    print(f"\n  Nombre de tours joués : {nb_tours - 1}")  # -1 car le dernier c'est quitter
    affichage_final()
    
    # Message de fin
    print()
    ecrire_doucement("  ☺ Merci d'avoir joué ! À bientôt ! ☺", 0.03)
    print("  ♪ ♫ ♪")

# Le programme commence ici
if __name__ == "__main__":
    try:
        # j'appelle ma fonction principale
        main()
    except KeyboardInterrupt:
        # si l'utilisateur fait Ctrl+C
        print("\n\n✖ Jeu interrompu par l'utilisateur")
        affichage_final()
    except Exception as erreur:
        # au cas où il y a un bug
        print(f"\n✖ Oups, erreur : {erreur}")
        print("Désolé, le jeu a planté ☹")