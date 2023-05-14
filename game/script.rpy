define profe = Character("Monika")
define elena = Character("Elena")
init:
    $ contador1 = 0
    $ contador2 = 0
    $ contador3 = 0

    
label start:
    play music "audio/musica_game.mp3"
    scene fondo
    show profe1 at left with moveinleft
    profe "Hello there and welcome to your new english class (Hola y bienvenido a tu nueva clase de inglés)."
    profe "I´m Mokia, I'm here for teaching you the basics concepts for help you in your learning. (Yo soy Monika, estoy aqui para enseñarte los conceptos básicos del ingles que te ayudaran en tu aprendizaje.)"
    profe "Entonces, cuéntame, ¿ya tienes conocimiento previo del inglés?"
    menu:
        "SI":
            hide profe1
            show profe2 at left
            profe "¡Perfecto!, déjame decirte que no estaria mal un repaso asi que comenzaremos con el nivel que desees seleccionar"
            hide profe2
            show profe1 at left


        "NO":
            show profe1 at left
            profe "¡No hay problema!,te enseñaré lo mas básico y facil para empezar, entonces selecciona el nivel 1"

    menu:
        "Nivel 1":
            jump nivel1

label nivel1:
    hide profe2
    show profe1 at left with moveinleft
    profe "Este es el nivel 1 y adivina, iniciameros con... ¡ANIMALES!, a todos nos gustan los animales, asi que veremos como se les dice en el extranjero."
    profe "Primero, animales domésticos."
    show dog
    profe "Primero, considerada la mascota favorita, cuando solo es uno, el perro es llamado{b} (Dog) {/b}, pero cuando son 2 o mas agregamos una {b} S {/b} al final, entonces quedaria {b} (Dogs) {/b}."
    hide dog
    profe "vamos con otro"
    show cat
    profe "Felinos, el gato es llamado {b} (Cat) {/b},y si son más de 2 son {b} (Cats) {/b}."
    hide cat 
    show bird  
    profe "Algunas personas tienen aves como mascotas, en general pájaros, 1 solo es {b} (Bird) {/b} y varios son {b} (Birds) {/b}."
    hide bird 
    profe "Vamos bien, sigamos aprendiendo. Ahora veremos animales de granja (farm animals)"
    show cow  
    profe "A las vacas se les dice {b} Cow {/b}"
    hide cow 
    show horse  
    profe "A los caballos se les dice {b} Horse {/b}"
    hide horse 
    show goat  
    profe "A las cabras se les dice {b} Goat {/b}"
    hide goat 
    show sheep  
    profe "A las ovejas se les dice {b} Sheep {/b} o {b} Lamb {/b}"
    hide sheep 
    show rabbit  
    profe "A los conejos se les dice {b} Rabbit {/b} o {b} Bunny {/b}"
    hide rabbit 
    show pork  
    profe "A los cerdos se les dice {b} Pig {/b}"
    hide pork 
    show chicken  
    profe "A las gallinas se les dice {b} Chicken {/b} o {b} Hen {/b} a los gallos se les dice {b} rooster {/b}. "
    hide chicken 
    show fish  
    profe "A los peces se les dice {b} Fish, ¡CUIDADO! {/b} a las palabra que finalizan en {b} SH {/b} se les añade {b} ES {/b} al final para si quedar Fish{b}es{/b}."
    hide fish 
    profe "Ok, creo que estás listo para un pequeño Test"
    
label pregunta1:
    show profe1 at left
    profe "¿Como se le dice a los perros?"
    menu:
        "Dog":
            hide profe1
            show profe2 at left
            play sound "audio/correct-fx.mp3"
            profe "Fine, (muy bien), vamos con siguiente pregunta:"
            $ contador1 = contador1 + 1
            jump pregunta2
        "Cat":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Oh no!, recuerda, Cat es gato, vamos con la siguiente pregunta."
            hide profe5
            jump pregunta2
        "Bird":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "a little wrong, recuerda, Bird es ave, vamos con la siguiente pregunta."
            hide profe5
            jump pregunta2
        "Lizard":
            profe "Incorrecto, aunque seguro fué la curiosidad"
            show lizard 
            profe "Lizard se les dice a las lagartijas, intentalo nuevamente"
            hide lizard
            jump pregunta1
label pregunta2:
    show profe1 at left
    profe "Como se les dice a las vacas"
    menu:
        "Sheep":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto, Sheep es oveja, vamos con la siguiente pregunta"
            hide profe5
            jump pregunta3
        "Horse":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Casi... recuerda que Horse es caballo, vamos con la siguiente pregunta"
            jump pregunta3
        "Cow":
            hide profe1
            show profe2 at left
            play sound "audio/correct-fx.mp3"
            profe "Correcto, facil ¿verdad?, vamos con la siguiente pregunta"
            hide profe2
            $ contador1 = contador1 +1
            jump pregunta3
        "Chicken":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "La proxima te irá bien, pero recuerda que Chicken es gallina"
            profe "Vamos a la siguiente pregunta"
            hide profe5
            jump pregunta3
label pregunta3:
    show profe1 at left
    profe "como se les dice a los conejos"
    menu:
        "Rabbit":
            hide profe1
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Muy bien, siguiente pregunta."
            hide profe2
            $ contador1 = contador1 + 1
            jump pregunta4
        "Rebbit":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Casi, no te dejes confundir, recuerda leer siemrpe bien las palabras."
            profe "Siguente pregunta."
            hide profe5
            jump pregunta4
        "Bouny":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Casi, pero no es."
            profe "Siguiente pregunta."
            hide profe4
            jump pregunta4
        "Banny":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Casi, no te dejes confundir, recuerda leer siemrpe bien las palabras."
            profe "siguiente pregunta"
            hide profe5
            jump pregunta4
label pregunta4:
    show profe1 at left
    profe "como se les dice al pez en plural(varios)"
    menu:
        "Fisherman":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Incorrecto"
            profe "Por si te lo preguntas esto significa pescador"
            hide profe1
            jump pregunta5
        "Fish":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Estuviste cerca... era el plural asi que era Fishes, pero vas bien"
            hide profe4
            jump pregunta5
        "Fishes":
            hide profe1
            show profe2 at left
            play sound "audio/correct-fx.mp3"
            profe "Well done (Bien hecho) identificaste bien la respuesta correcta"
            hide profe2
            $ contador1 = contador1 +1
            jump pregunta5
        "Lamb":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "recuerda que a la oveja se le puede decir sheep o lamb por lo cual estas equivocado"
            hide profe4
            jump pregunta5
label pregunta5:
    show profe1 at left
    profe "Como se les dice a las ovejas"
    menu:
        "Fishes":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Wrong (incorrecto), fish es pez y fishes son peces"
            hide profe4
            jump resultadoTest1
        "Sheep":
            hide profe1
            show profe2 at left
            play sound "audio/correct-fx.mp3"
            profe "muy bien, tienes buen ojo para la gramatica"
            $ contador1 = contador1 + 1
            hide profe2
            jump resultadoTest1
        "Shep":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "¡uy!, esta era un poco complicada, la respuesta es shEEp (sheP es incorrecto) recuerda la forma de escritura"
            hide profe4
            jump resultadoTest1
        "Goat":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Incorrecto, Goat es cabra."
            hide profe4
            jump resultadoTest1
    
label resultadoTest1:
    show profe1 at left
    profe "Bueno revisemos tus resultados..."

    if contador1 == 5:
        hide profe5
        show profe2 at left
        profe "¡Excelente trabajo!"
        hide profe2

    if contador1 == 3 or contador1 == 4:
        hide profe5
        show profe1 at left
        profe "Bien hecho, cometiste unos erroes pero no te preocupes, si quiere puede volver a intentar el test"
        profe "¿Quieres intentarlo"
        menu:
            "SI":
                profe "De acuerdo hagamoslo de nuevo"
                $ contador1 = 0
                hide profe1
                jump pregunta1
            
            "NO":
                "De acuerdo, entonces continuemos"

    if contador1 == 0 or contador1 <= 2:
        show profe5 at left
        profe "Parece que no entendiste bien, intentalo de nuevo"
        $ contador1 = 0
        hide profe5
        jump pregunta1


    
    show profe1 at left
    profe "Ahora veremos algunos animales salvajes"
    show lion  
    profe "Al los leones se le dice {b} Lion {/b}"
    hide lion 
    show tiger  
    profe "A los tigres se les dice {b} Tiger {/b}"
    hide tiger 
    profe "Debemos tener en cuenta que algunos palabras cambian dependiendo si es singular o plural"
    show wolf  
    profe "La forma singular del lobo es {b} Wolf {/b} mientras que en su forma plural se escribe {b} Wolves {/b}."
    hide wolf 
    show bear  
    profe "Al oso se le dice {b} Bear {/b} y osos {b} Bears {/b}."
    hide bear 
    profe "En ocasiones, hay palabras que se escriben igual en español y en ingles, lo único que cambia es su pronunciación, por ejemplo, los nombres de personas, algunos animales, cosas o lugares. A estas palabras se les coonoce como {b} Cognados {/b}."
    show jaguar  
    profe "A los jaguares se les dice {b} Jaguar {/b} o {b} Jaguars {/b}, como se mencionó anteriormente, su pronunciacion cambia."
    hide jaguar 
    show cougar  
    profe "A los pumas se les dice {b} Cougar {/b} o {b} Cougars {/b}."
    hide cougar 
    show frog  
    profe "A las ranas o sapos se les dice {b} Frog {/b} o {b} Frogs {/b}."
    hide frog 
    show snake  
    profe "A las serpientes se les dice {b} Snake {/b}."
    hide snake 
    show rhinos  
    profe "A los rinocerontes se le dice {b} Rhinoceros o Rhino{/b}, su plural es {b} Rhinos {/b}."
    hide rhinos 
    show monkey  
    profe "A los monos se les dice {b} Monkey {/b}."
    hide monkey 
    show elephant  
    profe "A los elefantes se les dice {b} Elephant {/b}."
    hide elephant 
    show giraffe  
    profe "A las jirafas se les dice {b} Giraffe {/b}."
    hide giraffe 
    show canguro  
    profe "A los canguros se les dice {b} Kangaroo {/b}."
    hide canguro 
    show crocodile  
    profe "Finalmente a los cocodrilos se les dice {b} Crocodile {/b}. Como dato, a los caimanes los podemos llamar {b} Caiman {/b}, pero tambien los podemos llamar {b} Alligator {/b} o {b} Alligators {/b}."
    hide crocodile
    profe "Perfecto, ahora hagamos otra ronda de preguntas"


label pregunta6:
    show profe1 at left
    profe "¿Como se les dice a los lobos?, en plural"
    menu:
        "Wolfs":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left
            profe "Incorrecto."
            porfe "Siguiente pregunta."
            jump pregunta7
        "Wolfes":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left
            profe "Incorrecto."
            profe "Siguiente pregunta."
            jump pregunta7
        "Wolves":
            hide profe1
            show profe2 at left 
            play sound "audio/correct-fx.mp3"
            profe "Correcto, muy bien."
            profe "sigamos con la siguiente pregunta."
            $contador2 = contador2 +1
            jump pregunta7
        "Wloves":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left
            profe "Incorrecto, fijate bien, estaba mal escrito."
            porfe "Siguiente pregunta."
            jump pregunta7

label pregunta7:
    show profe1 at left
    profe "¿Como se les dice a los osos?"
    menu: 
        "Beard":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto, Bread significa {b}Barba{/b}."
            profe "Hay algunas palabras que parecen pronunciarse igual, sin embargo son diferentes, be careful with it (Ten cuidado con eso)"
            profe "Siguiente pregunta."

        "Bear":
            hide profe1
            show profe2 at left 
            play sound "audio/correct-fx.mp3"
            profe "Correcto, muy bien."
            profe "sigamos con la siguiente pregunta."
            $contador2 = contador2 +1

        "Bread":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto, Bread significa {b}Pan{/b}."
            profe "Hay algunas palabras que parecen pronunciarse igual, sin embargo son diferentes, be careful with it (Ten cuidado con eso)"
            profe "Siguiente pregunta."

        "Brear":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto."
            profe "Siguiente pregunta."

label pregunta8:
    show profe1 at left
    profe "¿Como se le dice a los jaguares?"
    menu:
        "Juagar":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto."
            profe "Siguiente pregunta."

        "Cougar":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto, cougar es {b}puma{/b}"
            profe "Siguiente pregunta."

        "Jaguar":
            hide profe1
            show profe2 at left 
            play sound "audio/correct-fx.mp3"
            profe "Correcto, muy bien, facil verdad."
            profe "sigamos con la siguiente pregunta."
            $contador2 = contador2 +1

        "Jagaur":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto."
            profe "Siguiente pregunta."

label pregunta9:
    profe "¿Como se les dice a las ranas?"
    menu:
        "Flogs":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Incorrecto."
            profe "Sigamos con la ultima pregunta pregunta."

        "Frogs":
            hide profe1
            show profe2 at left 
            play sound "audio/correct-fx.mp3"
            profe "Correcto, muy bien."
            profe "Sigamos con la ultima pregunta."
            $contador2 = contador2 +1

        "Frugs":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Incorrecto."
            profe "Vamos con la ultima pregunta."
        
        "Frosg":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Incorrecto, recuerda revisar bien las palabras."
            profe "Vamos con la ultima pregunta."

label pregunta10:
    show profe1 at left
    profe "Esta pregunta es un poco diferente"
    profe "¿Elephant es un congnado?"
    menu:
        "Si":
            hide profe1
            show profe2 at left
            play sound "audio/correct-fx.mp3"
            profe "muy bien"
            hide profe2
            show profe1 at left
            profe "Elephant si es un cognado, no necesariamente deben escribirse igual, pero son muy similares y si comparten el mismo significado"
            $ contador2 = contador2 + 1
            hide profe1
            jump resultadoTest2

        "No":
            hide profe 
            show profe4 at left
            profe "Elephant si es un cognado"
            hide profe4 
            show profe1 at left
            profe "Los cognados no necesariamente deben escribirse igual, por lo tanto Elephant si es un cognado" 
            hide profe1
            jump resultadoTest2

label resultadoTest2:
    show profe1 at left
    profe "Bueno revisemos tus resultados..."

    if contador2 == 5:
        hide profe5
        show profe2 at left
        profe "¡Excelente trabajo!"
        hide profe2

    if contador2 == 3 or contador2 == 4:
        hide profe5
        show profe1 at left
        profe "Bien hecho, cometiste unos erroes pero no te preocupes, si quiere puede volver a intentar el test"
        profe "¿Quieres intentarlo"
        menu:
            "SI":
                profe "De acuerdo hagamoslo de nuevo"
                $ contador2 = 0
                hide profe1
                jump pregunta1
            
            "NO":
                "De acuerdo, entonces continuemos"
                

    if contador2 == 0 or contador2 <= 2:
        show profe5 at left
        profe "Parece que no entendiste bien, intentalo de nuevo"
        $ contador2 = 0
        hide profe5
        jump pregunta6


    profe "Ahora veamos rapidamente como se le dice a algunos alimentos, a la comida en ingles se le dice {b}Food{/b}."
    profe "Vamos a comenzar con algunas frutas, en ingles {b}Fruits{/b}."
    show apple
    profe "A las manzanas se les dice {b}Apple{/b}."
    hide apple
    show orange
    profe "A las naranjas se les dice Orange, además del color naranja, tambien se le dice {b}Orange{/b}."
    hide orange
    show grapes
    profe "A las uvas se les dice {b}Grapes{/b}."
    hide grapes
    show pineapple
    profe "A las piñas se les dice {b}Pineapple{/b}."
    hide pineapple
    show pear
    profe "A las peras se les dice {b}Pear{/b}."
    hide pear
    show lemon
    profe "A los limones se les dice {b}Lemon{/b}"
    hide lemon
    show tangerines
    profe "A las mandarinas se les dice {b}Tangerines{/b}."
    hide tangerines
    show banana
    profe "A los platanos se les dice {b}Bananas{/b}."
    profe "Esta palabra tambien la usamos en el español."
    profe "ATTENTION!(Atención), ¿Recuerdas como se les dice a las palabras que se escriben igual en el español e ingles y tienen el mismo significado?"
    hide banana
label fastquest:
    show profe6 at left
    menu:
        "Sinonimos":
            hide profe6
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "!Ups¡"
            profe "Los sinonimos son palabras con igual {b}significado{/b}."
            hide profe5

        "Cognados":
            hide profe6
            show profe2 at left
            play sound "audio/correct-fx.mp3"
            profe "Very well (Muy bien), sigamos."
            hide profe2

        "Homonimos":
            hide profe6
            play sound "audio/incorrect-fx.mp3"
            show profe4 at left with vpunch
            profe "Incorrecto, los Homonimos son palabras iguales pero con diferente significado."
            hide profe4

        "Adgetivos":
            hide profe6
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Incorrecto"
            profe "Los adjetivos son las palabras que describen algo."
            hide profe5

    show profe1 at left
    profe "Continuamos con..."
    show mango 
    profe "{b}Mangos{/b}, este tambien es un cognado"
    hide mango
    show strawberry
    profe "A las fresas se les dice {b}Strawberry{/b} ten cuidado de no escribir mal esta palabra."
    hide strawberry
    profe "Ahora veremos algunas verduras, o en ingles {b}Vegetables{/b}."
    show carrots
    profe "A las zanahorias se les dice {b}Carrot{/b} o {b}Carrots{/b} en plural."
    hide carrots
    show lechuga
    profe "A la lechuga se le dice {b}Lettuce{/b}."
    hide lechuga
    show onions
    profe "A la cebolla se le dice {b}Onion{/b}."
    hide onions
    show tomatoes
    profe "A los tomates se les dice tomato, ojo aqui, al igual que a las palabra que terminan en 'SH', para las palabras que finalizan en 'O', se les agrega 'ES' para su forma plural."
    profe "Es decir, el plural de tomato es {b}Tomatoes{/b}."
    hide tomatoes
    show potatoes
    profe "A las papas se les dice potato, y al igual que con tomato, su forma plural es agregando 'ES' al final."
    hide potatoes
    show calabaza
    profe "A las calabazas se les dice {b}Pumpkin{/b}."
    hide calabaza
    show rice
    profe "Al arroz se le dice {b}Rice{/b}."
    hide rice
    profe "Ojo, el arroz no es un {b}Vegetable{/b} es un cereal."
    profe "Esta palabra es un cognado, asi que en ingles tambien se dice {b}Cereal{b}."
    show lentils
    profe "A las lentejas se les dice {b}Lentils{/b}."
    profe "Esta tampoco es un vegetable, es una Legumbre, en ingles {b}Legume{/b}."
    hide lentils
    show peas
    profe "A las arvejas o guisantes se les dice {b}Pea{/b} y {b}Peas{/b}."
    profe "Esta tambien es una {b}Legume{/b}."
    hide peas
    profe "Estas a un paso de lograrlo, este es el ultimo test, con esto verás los frutos de tu aprendizaje y completar el primer nivel."
    hide profe1
    show profe6 at left
    profe "Este test será de PRONUNCIACION con un buen resultado podrás pasar al nivel 2. Y si fallas no te preocupes que podrás reintentarlo"
    hide profe6

label pregunta11:
    show profe1 at left
    profe "Are you ready? (Estás listo?) las proguntas seran sobre PRONUNCIATION (pronuncieishion) pronunciación asi que Good Luck and GO! (¡Buena suerte y vamos!)"
    profe "Como se pronuncia caballo en inglés (recuerda la forma en la que se escribe)"
    menu:
        "Horss":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "OH NO, it's wrong (es incorrecto) la siguiente es la buena"
            hide profe5
            jump pregunta12
        "Jurss":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) suerte en la próxima"
            hide profe5
            jump pregunta12
        "Jorse":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) recuerda que la E es muda"
            hide profe5
            jump pregunta12
        "Jorss":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) esta fué trampa ya que cuando una palabra tiene doble ss el sonido se prolonga"
            hide profe5
            jump pregunta12
        "Jors":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Well done (Bien hecho), sigue así"
            hide profe2
            $ contador3 = contador3 + 1
            jump pregunta12
label pregunta12:
    
    profe "Como se pronuncia león (lion)"
    menu:
        "Leion":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) casi, te equivocaste por la E"
            hide profe5
            jump pregunta13
        "Layon":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) cerca... pero recuerda tiene Y, se diria yon cuando debe ser ion"
            hide profe5
            jump pregunta13
        "Laion":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Perfect (perfecto) vas muy bien"
            hide profe2
            $ contador3 = contador3 + 1
            jump pregunta13
        "Leon":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) esa seria en español"
            hide profe5
            jump pregunta13
label pregunta13:
    profe "Como se pronuncia vaca (cow)"
    menu:
        "Cauw":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) fallaste por la U"
            hide profe5
            jump pregunta14
        "Moo":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) jeje ese es el sonido que realizan cuando enseñan en inglés"
            hide profe5
            jump pregunta14
        "Caow":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Fantastic (fantastico) buen acierto"
            hide profe2
            $ contador3 = contador3 + 1
            jump pregunta14
        "Muu":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) jeje ese es el sonido que realizan con la diferencia que asi lo explican en español"
            hide profe5
            jump pregunta14
label pregunta14:
    profe "Vamos con una dificil, como se pronuncia calabaza (pumpkin) recuerda decirlo en voz alta y asi lo recordarás en un futuro"
    menu:
        "pupkim":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) es pupmkin y su pronunciacion pompken"
            hide profe5
            jump pregunta15
        "punpkem":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) es pupmkin y su pronunciacion pompken, recuerda no confundir letras mientras pronuncias"
            hide profe5
            jump pregunta15
        "pumpken":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) Ohhh estuviste cerca... era con O pomp y elegiste pump pero casi lo lográs"
            hide profe5
            jump pregunta15
        "pompken":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Wonderful (maravilloso) complicada pero lo hiciste"
            hide profe2
            $ contador3 = contador3 + 1
            jump pregunta15
        "pikmin":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Easter Egg (huevo de pascua) ¿sabias que a esta palabra suele confundirsele con zanahoria en los videojuegos de origen japonés?"
            hide profe5
            jump pregunta15
label pregunta15:
    profe "finalmente como se pronuncia vegetales (vegetables)"
    menu:
        "vegetaibol":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) pequeño fail (fallo)"
            hide profe5
            jump pregunta16
        "vejetabol":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) pequeño fail (fallo) pero cerca"
            hide profe5
            jump pregunta16
        "vejstebols":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Amazing (increible) ahora preparate para la pregunta final más dificil"
            hide profe2
            $ contador3 = contador3 + 1
            jump pregunta16
        "aguacate":
            hide profe1
            play sound "audio/incorrect-fx.mp3"
            show profe5 at left with vpunch
            profe "Wrong (incorrecto) en ingles es avocado(avecadou)"
            hide profe5
            jump pregunta16
label pregunta16:
    profe "Como se DICE mango en inglés"
    menu:
        "mango":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Wow(guau) estuvo dificil ¿verdad? bien hecho"
            hide profe2
            $ contador3 = contador3 + 1
            jump resultadoTest4
        "mango":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Wow(guau) estuvo dificil ¿verdad? bien hecho"
            hide profe2
            $ contador3 = contador3 + 1
            jump resultadoTest4
        "mango":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Wow(guau) estuvo dificil ¿verdad? bien hecho"
            hide profe2
            $ contador3 = contador3 + 1
            jump resultadoTest4
        "mango":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Wow(guau) estuvo dificil ¿verdad? bien hecho"
            hide profe2
            $ contador3 = contador3 + 1
            jump resultadoTest4
        "Mango":
            play sound "audio/correct-fx.mp3"
            show profe2 at left
            profe "Wow(guau) estuvo dificil ¿verdad? bien hecho"
            hide profe2
            $ contador3 = contador3 + 1
            jump resultadoTest4

label resultadoTest4:
    show profe1 at left
    profe "Bueno revisemos tus resultados..."

    if contador3 == 5:
        hide profe5
        show profe2 at left
        profe "¡Excelente trabajo!"
        hide profe2

    if contador3 == 3 or contador3 == 4:
        hide profe5
        show profe1 at left
        profe "Bien hecho, cometiste unos errores pero no te preocupes, intentalo nuevamente si lo deseas"
        profe "¿Quieres reintentar?"
        menu:
            "SI":
                profe "Esa es la actitud, (Here we go again) vamos otra vez"
                $ contador3 = 0
                hide profe1
                jump pregunta11
            
            "NO":
                "De acuerdo, de todos modos lo hiciste muy bien"
                

    if contador3 == 0 or contador3 <= 2:
        show profe5 at left
        profe "No te preocupes, recuerda que tienes vidas infinitas :D"
        $ contador3 = 0
        hide profe5
        jump pregunta11

show profe1 at left 
profe "Congratulations (felicitaciones) haz finalizado exitosamente el nivel 1 espero que hayas aprendido y lo más importante... que te hayas divertido mucho con nuestro programa nos veremos en el nivel 2, hasta pronto"
    

    




