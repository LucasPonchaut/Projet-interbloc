
label pattes_oui:
    n "Au fil des générations, la lignée de ton animal conserve le nombre de pattes qu’il avait lors de sa sortie de l’eau. {w}Cependant, les proies aussi !"
    n "Certaines populations de ces dernières auront plus de chance de survie grâce au développement de leurs pattes qui leur permettent de courir plus vite et d’échapper aux prédateurs. {w}Ta lignée est donc perturbée."
    n "Les animaux qui vivent dans des forêts tropicales s’attachent aux arbres pour savoir chasser." 
    n "Certaines populations développent donc des pattes avants (bras) leur permettant de monter aux arbres plus facilement pour mieux voir leurs proies et leur tomber dessus par surprise. "
    n "D’autres, qui restent au sol, développent des structures qui rendront leurs pattes plus fortes et donc qui amélioreront la vitesse de l’individu."
    
    # ici choix des pattes
    menu:
        n "Pour toi, quel est le plus intéressant moteur de chasse à suivre ?"
        "4 pattes":
            jump quadrupede
        "2 pattes":
            "WIP"
    return

            
# ici partie quadrupede    
label quadrupede:
    n "Une population de la lignée de ton animal va suivre le modèle de ses proies en développant des pattes de plus en plus musclées. {w}Cela les rendra très rapide !"
    n "De plus en plus de créatures peuplent la planète et colonisent tous les types d’environnement. Ces environnements sont très semblables et le climat est toujours très très chaud."
    n "Les prédateurs et les proies vivent maintenant tout le temps ensemble dans le même milieu. Les animaux qu’on y retrouve sont de toutes les tailles."
    n "Les animaux de la lignée avec laquelle tu avances sont de taille moyenne et arrivent à chasser des proies de tailles plus ou moins égales à la leur."

    menu:
        n "Penses-tu, jeune scientifique, que pour chasser plus efficacement, les animaux devraient vivre en groupe ou rester seul ?"
        "rester en groupe":
            jump en_groupe
        "rester seul":
            jump seul

    return

