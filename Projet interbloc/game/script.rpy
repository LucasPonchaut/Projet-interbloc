# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Narrateur', color="#c8ffc8")


# Le jeu commence ici
label start:

    n "Nos amies les cellules sont emportées par un courant marin. Une fois le courant passé, elles s’arrêtent dans un environnement fort ensoillé ! Certains de nos amis aiment cela tandis que d’autres non. En plus, une dispute a lieu entre ces cellules. "

    n "En effet, là où nos amis multicellulaires se sont arrêtés est un endroit où il n’y a pas assez à manger pour tout le monde, ce qui a pour conséquence d’envoyer les individus les moins adaptés (ceux qui aiment moins le soleil) au fond de la mer car elles n’ont plus les ressources nécessaires en surface."
    menu:
        n "A toi de choisir jeune scientifique, avec quelles cellules veux-tu rester ?"
        "Veux-tu rester avec les autres en surface ?":
            jump surface
        "Veux-tu découvrir avec eux ce qu’il se trouve en dessous ?":
            n "Elles découvrent un endroit sombre et froid. Au fur et à mesure de leur périple, elles trouvent de quoi se nourrir et donc décident de coloniser cet endroit. Etant donné que la nourriture est proche, ces dernières ont peu de déplacement à effectuer."
    n "Cependant, une variété parmi tous ces organismes multicellulaires va commencer à se rejoindre pour ainsi former un organisme complètement rond."
    n "Félicitation nous te présentons le Rondulus magnificient !"

    menu:
        n "Selon toi jeune scientifique, est-ce qu’un squelette serait-il nécessaire pour son déplacement ?"
        "oui":
        # Voir fin du code
            jump vertébré_profondeur 
        "non":
            return
# Ici on arrive dans le groupe de cellule en surface de l'eau
label surface:
    n "Les cellules de ces premiers organismes sont plus à l’aise au soleil car elles possèdent une fine peau qui leur permettra de résister à la chaleur et à la lumière du soleil. "
    n "Elles commencent à se multiplier de plus en plus jusqu’à arriver à un moment où le nombre de cellules exposé au soleil est trop important !"
    n "Certains de ces premiers organismes vont alors au cours du temps réussir à se développer de sorte que la partie qui est au soleil diminue et ainsi demande moins d’énergie à protéger !"
    n "On obtient ainsi le tout premier animal de ta lignée ! Félicitation, nous te présentons le Tubulus magnificient."
    n "Quelques millions d’années plus tard, on se trouve dans un milieu aquatique dans lequel la population a augmenté de façon importante et dans laquelle plusieurs espèces sont apparues."
    n "Par le hasard des choses, dans une de ces espèces, au fil des générations, une structure ressemblant à un squelette a commencé à apparaître, cette espèce s’appelle Durus Chordus . Dans d’autres en revanche, elles ont conservé un aspect mou, sans squelette comme par exemple les Nouillus Asichinus."
 
    menu:
        n "Pour toi jeune scientifique, lequel des deux serait le plus intéressant à suivre ?"
        "Descendance des Durus Chordus":
            jump vertébré_surface
        "Descendance des Nouillus Asichinus": 
            return
# Ici on rentre dans la branche des vertébrés
label vertébré_surface:
    n "Quelques millions d’années après l’apparition de début de squelette, ces petites populations se sont multipliés et ont donné naissance à une nouvelle catégorie d’espèces : les vertébrés. Ils disposent donc d’un vrai squelette !"
    n "Grâce à ce squelette, les organes internes sont mieux protégés. Il a aussi provoqué des excroissances dans une partie des vertèbres."
    n "Dans les populations ayant subi le développement de ces excroissances, une structure osseuse est alors apparue au cours du temps pour former des nageoires,... Comme on peut le voir chez un des descendants de ta lignée, les Squeletus Chordus"
    n "Au cours des millions d’années qui ont suivi l’apparition des premiers vertébrés, la vie aquatique a proliférée, donnant ainsi des animaux complètement différents, donnant ainsi de nouvelles espèces."
    n "La nourriture y étant abondante tous les animaux sont amis et se nourrissent de plantes ou de cailloux, de sable… "
    n "Cependant un grand cataclysme va toucher notre chère planète. Ces catastrophes vont provoquer un refroidissement de la planète tellement fort que des tempêtes et de nombreux tsunamis vont avoir lieu. "
    n "Dans cette horrible tempête les animaux une partie des espèces d’animaux se trouvant au plus proche de la surface de l’eau vont être dispersé parmi les terres. D’autres en revanche vont pouvoir continuer à vivre paisiblement dans l’eau bien à l’abri de toute cette agitation en vivant assez profond pour ne pas être impacter."
    
    menu:
        n "Pour la suite de ton aventure évolutive, avec quels animaux souhaites-tu poursuivre ? Veux-tu suivre les aventures dans les profondeurs ou plus en surface de nos amis ?"
        "Terrestre":
            jump terrestre
        "Marin":
            return
#Ici on rentre dans la branche des animaux terrestres
label terrestre:
    n "Parmi ceux-ci les animaux qui sont envoyés sur la Terre par la force des marées ou par les tornades, certaines sont dispersés sur les plages donc près de la mer et sont donc plus apte à survivre."
    n "Car certains vertébrés vivaient déjà à l’origine près des récifs, ce qui a permis de développer, au fur et à mesure des générations, des structures respiratoires qui leur permettait de vivre un certain temps hors de l’eau. Ainsi ces accès à la plage les amènent en contact direct avec la terre tout en gardant un accès facile à l’eau."
    n "Parmi ces organismes se trouvent heureusement des représentant de la lignée dont on suit l’histoire. En effet, certaines espèces vivant proches des récifs qui se trouveront envoyés trop loin sur la terre se verront disparaître. On appelle ça une extinction."
    n "Parmi les individus de notre lignée, certains d’entre eux préfèrent retourner dans l’eau, qui était leur habitat de base, et d’autres veulent aller explorer le nouvel environnement."
    #Vidéo à ce moment là
    n "Les animaux originellement herbivores vont commencer à se nourrir des carcasses des autres animaux en commençant à dévorer leurs entrailles en y cherchant des plantes mais au fur et à mesure du temps, des lignées vont se spécialiser comme source principale de nourriture la viande des carcasses."
    n "Ainsi de nombreuses des espèces qui vivent sur notre monde sont devenus carnivores. Ou bien sont restés herbivores."
    n "Au fur et à mesure du temps, les individus carnivores sont restés charognards et en même temps se sont spécialisés dans la chasse. Certains individus se sont particulièrement démarqués en développant des membres qui à l’origine leurs servaient de nageoire et ont ainsi au fur et à mesure du temps créé des pattes."
    
    menu:
        n "Avec quelle lignée souhaite tu poursuivre ton aventure ?"
        "Carnivore":
            jump carnivore
        "Herbivore":
            return
#Ici on rentre dans la branche des carnivores
label carnivore:
    n "Avec ceux qui vont survivre, dû à l’ère à glacière. Au début, ils mangent les restes de plantes présents dans l’estomac des animaux morts mais au fur et à mesure du temps, les espèces les plus adaptées se nourrissent de + en plus de la chaire de ses animaux décédés."
    n "Ceci donnera donc lieu à une nouvelle caractéristique pour la lignée de l’animal : elle devient carnivore !"
    n "Après quelques milliers d’années, l’ère glaciaire prend fin. Le temps se réchauffe de plus en plus. Certains animaux restent dans les environs des plages alors que d’autres partent à l’aventure dans le centre des terres."
    n "De plus en plus de variétés de plantes et de fleurs apparaissent ce qui permet à plus d’animaux herbivores de survivre ! Cela implique donc que de moins en moins de carcasses soient trouvées par les espèces carnivores."
    n "Celles-ci commencent à manquer de nourriture et doivent donc trouver un moyen d’y remédier.  Plusieurs espèces commencent à attaquer directement les animaux vivants, la chasse est née !!"
    n "Au fur et à mesure du temps, certaines espèces développent plus leurs pattes pour aller plus vite alors que d’autres ont bcp plus de chance de survie en l’absence de pattes."
    menu:
        n "Pour chasser, faut-il, petit biologiste, conserver les pattes ou non ?"
        "Oui, conserver les pattes":
            jump pattes_oui
        "Non, perdre les pattes":
            jump pattes_non  
    return
# Ici on rentre dans la branche des vertébrés issus des profondeurs
label vertébré_profondeur:
    "WIP"
    return
   
