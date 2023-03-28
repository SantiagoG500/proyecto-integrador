define profe = Character("Monika")

label start:
    scene fondo
    show profe at left with moveinleft
    profe "Welcome, bienvenido."
    profe "Soy Monika, bienvenido a tu clase de ingles, donde aprenderas coasas basicas que te ayudaran en tu aprendizaje."
    profe "Esto esta enfocado a todo publico, asi que si ya tienes conociemiento en ingles tambien puedes complementarlo."
    profe "¿Tienes conocimiento en ingles?"
    menu:
        "SI":
            profe "¡Genial!, podras complementar lo que ya haz aprendido, selecciona un nivel para comenzar."


        "NO":
            profe "No te preocupes, aqui parenderas lo basico, comenzaremos con el nivel 1"

    menu:
        "Nivel 1":
            jump nivel1

label nivel1:
    show profe at left with moveinleft
    profe "Comenzaremos con lo basico, ¡ANIMALES!, a todos nos gustan los animales, asi que veamos como es su nombre en ingles."
    profe "Primero algunos animales domesticos."
    show dog 
    profe "a los perros se les llama {b} Dog {/b}, cuando se habla de uno solo, cuando hablamos de 2 o mas agregamos una {b} S {/b} al final, {b} Dogs {/b}."
    hide dog 
    show cat  
    profe "Y a los gatos les decimos {b} cat {/b}, o {b} cats {/b}."
    hide cat 
    show bird  
    profe "Algunas personas tienen de mascotas pajaritos, en general a los pajaros se les llama {b} Bird {/b} o {b} Birds {/b}."
    hide bird 
    profe "Creo que ya lo tienes, hagamos esto mas rapido"
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
    profe "A las ovejas se les dice {b} Sheep o lamb {/b}"
    hide sheep 
    show rabbit  
    profe "A los conejos se les dice {b} Rabbit o Bunny {/b}"
    hide rabbit 
    show pork  
    profe "A los cerdos se les dice {b} Pig {/b}"
    hide pork 
    show chicken  
    profe "A las gallinas se les dice {b} Chicken o Hen {/b} a los gallos se les dice {b} rooster {/b}. "
    hide chicken 
    show fish  
    profe "A los peces se les dice {b} Fish, OJO {/b} a las palabra que finalizan en {b} SH {/b} se le escribe {b} ES {/b} Fish{b}es{/b}."
    hide fish 
    profe "Haremos una ronda de 5 preguntas"
    profe "¿Como se le dice a los perros?"
label pregunta1:
    menu:
        "Dog":
            profe "Correcto"

        "Cat":
            profe "Incorrecto, recuerda, Cat es gato."
            jump pregunta1

        "Bird":
            profe "Incorrecto, recuerda, Bird es ave."
            jump pregunta1

        "Lizard":
            profe "Incorrecto, aunque seguro lo hicicste por curiosidad"
            show lizard 
            profe "Lizard se les dice a las lagartijas"
            hide lizard
            jump pregunta1

    profe "Ahora veamos algunos animales salvajes"
    show lion  
    profe "Al los leones se le dice {b} Lion {/b}"
    hide lion 
    show tiger  
    profe "A los tigres se les dice {b} Tiger {/b}"
    hide tiger 
    profe "En algunos casos, la froma {b} singular {/b}, es decir, uno solo, varia de la forma {b} prural {/b} mas de 2."
    show wolf  
    profe "La forma singular de lobo se escribe {b} Wolf {/b} mientras su forma prural se escribe {b} Wolves {/b}."
    hide wolf 
    show bear  
    profe "A los osos se les dice {b} Bear {/b}."
    hide bear 
    profe "En ocasiones, hay palabras que se escriben igual en español e ingles, lo que cambia es su pronunciacion, por ejemplo, los nombres de personas, animales, cosas o lugares. A estas palabras se les coonoce como {b} Cognados {/b}."
    show jaguar  
    profe "A los jaguares se les dice {b} Jaguar {/b} o {b} Jaguars {/b}, como se mencionó anteriormente, su pronunciacion cambia."
    hide jaguar 
    show cougar  
    profe "A los pumas se les dice {b} Cougar {/b}."
    hide cougar 
    show frog  
    profe "A las ranas o sapos se les dice {b} Frog {/b}."
    hide frog 
    show snake  
    profe "A las serpientes se les dice {b} Snake {/b}."
    hide snake 
    show rhinos  
    profe "A los rinocerontes se le dice {b} Rhinoceros o Rhino{/b}, su prural es {b} Rhinos {/b}."
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
    profe "A los cocodrilos se les dice {b} Crocodile {/b}. Como dato, a los caimanes los podemos llamar {b} Caiman {/b}, pero tambien los podemos llamar {b} Alligator {/b} o {b} Alligators {/b}."