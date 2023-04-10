define profe = Character("Monika")

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
    profe "Vamos bien, sigamos aprendiendo"
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
    profe "A las ovejas se les dice {b} Sheep {/b} o {b} lamb {/b}"
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
    profe "¿Como se le dice a los perros?"

label pregunta1:
    show profe1 at left
    menu:
        "Dog":
            profe "Fine, (muy bien), siguiente pregunta:"
        "Cat":
            hide profe1
            show profe5 at left
            profe "Oh no!, recuerda, Cat es gato."
            hide profe5
            jump pregunta1
        "Bird":
            hide profe1
            show profe5 at left
            profe "a little wrong, recuerda, Bird es ave."
            hide profe5
            jump pregunta1
        "Lizard":
            hide porfe5
            profe "Incorrecto, aunque seguro fué la curiosidad"
            show lizard 
            profe "Lizard se les dice a las lagartijas"
            hide lizard
            jump pregunta1

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