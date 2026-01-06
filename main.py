# Gestionnaire de Dépenses Simple
#lien Git: https://github.com/moussacode/GestionnaireDeDepense.git
depenses = []

def affiche_menu() :
    print("MENU")
    print("1. Ajouter une depense")
    print("2. Afficher les depenses")
    print("3. Total des depenses")
    print("4. Depenses par categorie")
    print("5. Quitter")


def ajouter_depense ():
    montant = float(input("Montant : "))
    categorie = input("Categorie : ")
    description = input("Description : ")
        
    depense = {
            "montant": montant,
            "categorie": categorie,
            "description": description
        }
    depenses.append(depense)
    print("Votre depeencse est ajouter")

def toute_depense ():
    print("tous les depence ")
    for i in range(len(depenses)):
        d = depenses[i]
        print(f"{i+1}. {d['montant']} FCFA - {d['categorie']} - {d['description']}")

def total_depence():
    total = 0
    for depense in depenses:
        total += depense["montant"]
    print(f"Total : {total} FCFA")

def par_categorie():
    print("=== PAR CATÉGORIE ===")
    categories = {}
        
    for depense in depenses:
            cat = depense["categorie"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(depense)
        
    for cat in categories:
            print(f"{cat}:")
            for d in categories[cat]:
                print(f"  - {d['montant']} FCFA: {d['description']}")
    

while True:

    affiche_menu()
    
    
    choix = input("Choix : ")
    
    if choix == "1":
        
        ajouter_depense ()
   
    elif choix == "2":

        toute_depense ()
    
    elif choix == "3":
        
        total_depence()
    
    elif choix == "4":
    
        par_categorie()
      
    

    elif choix == "5":
        print("Au revoir!")
        break
    else :
        print('Choisir une option entre 1 et 5')
