# Gestionnaire de Dépenses Simple

depenses = []

while True:
    print("MENU")
    print("1. Ajouter une depense")
    print("2. Afficher les depenses")
    print("3. Total des depenses")
    print("4. Depenses par categorie")
    print("5. Quitter")
    
    choix = input("Choix : ")
    
    if choix == "1":
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
    
   
    elif choix == "2":

        print("tous les depence ")
        for i in range(len(depenses)):
            d = depenses[i]
            print(f"{i+1}. {d['montant']} FCFA - {d['categorie']} - {d['description']}")
    
   
    elif choix == "3":
        total = 0
        for depense in depenses:
            total += depense["montant"]
        print(f"Total : {total} FCFA")
    
    
    elif choix == "4":
      print("Affichage par categorie ")
      
      categorie = {}

      for depense in depenses :  
          total_cat = depense['categorie']
          if total_cat  in categorie:
              categorie[total_cat ] =  depense['montant'] + categorie[total_cat ]                 
          else :
              categorie[total_cat ] =  depense['montant']
      print (categorie)
      
    

    elif choix == "5":
        print("Au revoir!")
        break
    else :
        print('Choisir une option entre 1 et 5')
