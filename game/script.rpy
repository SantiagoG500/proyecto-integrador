define profe = Character("Monika")
init:
    $ contador = 0
    
label start:
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
            profe "Fine, (muy bien), vamos con siguiente pregunta:"
            $ contador = contador + 1
            jump pregunta2
        "Cat":
            hide profe1
            show profe5 at left with vpunch
            profe "Oh no!, recuerda, Cat es gato, vamos con la siguiente pregunta."
            hide profe5
            jump pregunta2
        "Bird":
            hide profe1
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
            show profe5 at left with vpunch
            profe "Incorrecto, Sheep es oveja, vamos con la siguiente pregunta"
            hide profe5
            jump pregunta3
        "Horse":
            hide profe1
            show profe5 at left with vpunch
            profe "Casi... recuerda que Horse es caballo, vamos con la siguiente pregunta"
            jump pregunta3
        "Cow":
            hide profe1
            show profe2 at left
            profe "Correcto, facil ¿verdad?, vamos con la siguiente pregunta"
            hide profe2
            $ contador = contador +1
            jump pregunta3
        "Chicken":
            hide profe1
            show profe5 at left with vpunch
            profe "La proxima te irá bien, pero recuerda que Chicken es gallina"
            profe "Vamos a la siguiente pregunta"
            hide profe5
            jump pregunta3
label pregunta3:
    show profe1 at left
    profe "A partir de aquí encontrarás respuestas falsas, Be careful(Ten cuidado)"
    profe "como se les dice a las serpientes"
    menu:
        "Rabbit":
            hide profe1
            show profe4 at left with vpunch
            profe "Rabbit es conejo, mejor suerte para la proxima"
            hide profe4
            jump pregunta4
        "Shake":
            hide profe1
            show profe5 at left with vpunch
            profe "Oh, estuviste muy cerca, la palabra (Shake) significa sacudir o agitar aunque es muy similar a Snake su significado es muy diferente"
            hide profe5
            jump pregunta4
        "Snake":
            hide profe1
            show profe2 at left
            profe "Bien hecho, distingues muy bien las palabras"
            hide profe2
            $ contador = contador +1
            jump pregunta4
        "Snail":
            hide profe1
            show profe5 at left with vpunch
            profe "Wrong, Snail es caracol pero estuviste cerca"
            hide profe5
            jump pregunta4
        "Skane":
            hide profe1
            show profe5 at left with vpunch
            profe "Este es a proposito aunque estas casi en lo correcto, para la proxima revisa bien las letras"
            hide profe5
            jump pregunta4
label pregunta4:
    show profe1 at left
    profe "como se les dice al pez en plural(varios)"
    menu:
        "Fisherman":
            hide profe1
            show profe4 at left with vpunch
            profe "Incorrecto"
            profe "Por si te lo preguntas esto significa pescador"
            hide profe1
            jump pregunta5
        "Fish":
            hide profe1
            show profe4 at left with vpunch
            profe "Estuviste cerca... era el plural asi que era Fishes, pero vas bien"
            hide profe4
            jump pregunta5
        "Fishes":
            hide profe1
            show profe2 at left
            profe "Well done (Bien hecho) identificaste bien la respuesta correcta"
            hide profe2
            $ contador = contador +1
            jump pregunta5
        "Lamb":
            hide profe1
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
            show profe4 at left with vpunch
            profe "Wrong (incorrecto), fish es pez y fishes son peces"
            hide profe4
            jump resultadoTest1
        "Sheep":
            hide profe1
            show profe2 at left
            profe "muy bien, tienes buen ojo para la gramatica"
            $ contador = contador + 1
            hide profe2
            jump resultadoTest1
        "Shep":
            hide profe1
            show profe4 at left with vpunch
            profe "¡uy!, esta era un poco complicada, la respuesta es shEEp (sheP es incorrecto) recuerda la forma de escritura"
            hide profe4
            jump resultadoTest1
        "Goat":
            hide profe1
            show profe4 at left with vpunch
            profe "Goat es cabra."
            hide profe4
            jump resultadoTest1
    
label resultadoTest1:

    if contador == 5:
        hide profe5
        show profe2 at left
        profe "¡Excelente trabajo!"
        hide profe2
    if contador == 3 or contador == 4:
        hide profe5
        show profe1 at left
        profe "Bien hecho, cometiste unos erroes pero no te preocupes, si quiere puede volver a intentar el test"
        profe "¿Quieres intentarlo"
        menu:
            "SI":
                profe "De acuerdo hagamoslo de nuevo"
                $ contador = 0
                hide profe1
                jump pregunta1
            
            "NO":
                "De acuerdo, entonces continuemos"

    if contador == 0 or contador <= 2:
        show profe5 at left
        profe "Parece que no entendiste bien, intentalo de nuevo"
        $ contador = 0
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
    profe "¿Recuerdas como se les dice a las palabras que son iguales en el español e ingles?"
label fastquest:
    show profe6 at left
    menu:
        "Sinonimos":
            show profe5 at left with vpunch
            profe "!Ups¡"
            profe "Los sinonimos son palabras con igual {b}significado{/b}."
            hide profe5
        "Gognados":
            show profe2 at left
            profe "Very well (Muy bien), sigamos."
            hide profe1

        "Homonimos":
            show profe4 at left with vpunch
            profe "Incorrecto, los Homonimos son palbras iguales pero con diferente significado."
            hide profe4

        "Adgetivos":
            show profe5 at left with vpunch
            profe "Incorrecto"
            profe "Los adjetivos son las palabras que describen algo."
            hide profe5
    show profe1 at left
    profe "Continuamos con..."
    show mango 
    porfe "{b}Mangos{/b}, este tambien es un cognado"
    hide mango
    show strawberry
    profe "A las fresas se les dice {b}Strawberry{/b} ten cuidado de no escribir mal esta palabra."
    hide strawberry
    profe "Ahora veremos algunas verduras, o en ingles {b}Vegetables"
    




