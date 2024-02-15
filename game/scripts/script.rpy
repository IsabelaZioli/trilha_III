# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character ("José")
define e = Character ("Sr. Ednaldo")


# The game starts here.

label start:

    play music "TownTheme.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene portaria
    with fade

    "Todos os dias, no Condomínio Laranjeiras, chegam várias encomendas de moradores, desde as grandes até as pequenas."

    scene portaria com interfone
    with fade

    show joseecaixas
    with dissolve

    "Naquele dia, José estava na portaria quando uma grande remessa de várias caixas pequenas, identificadas com fita vermelha e a etiqueta ''frágil'', foi descarregada."

    scene portaria com interfone
    with fade


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    scene portaria com caixas

    show jose simpatico
    with dissolve

    j "Hoje chegaram mais encomendas do que o normal, e, além disso, são frágeis. Elas são do Sr. Ednaldo."

    play music "Ove Melaa I have just been eaten.mp3"

    scene portaria com caixas
    
    show jose pensativo
    with dissolve

    menu:

        "O que José deve fazer?"

        "Interfonar para Sr. Ednaldo.":

            jump rightaway

        "Deixar na portaria.":

            jump later
    

    return
    
label rightaway:
        
        play music "TownTheme.mp3"

        show jose simpatico
        with dissolve

        "Parabéns! Você deve sempre interfonar para o morador assim que a encomenda chegar."

        scene jose no interfone
        with dissolve

        j "Boa tarde, Sr. Ednaldo, acabaram de chegar encomendas suas. Acredito que sejam itens importantes, pois todas estão identificadas como frágeis"

        scene apartamentodoednaldo
        with fade

        e "Boa tarde, José! Vou agora mesmo."

        scene portaria com caixas
        with fade
       
        play music "Ove Melaa I have just been eaten.mp3"

        scene portaria com caixas

        show jose pensativo
        with dissolve

        menu:

            "O que José deve fazer?"

            "Registrar as encomendas e pedir o documento":

                jump rightaway2 

            "Esperar Sr. Ednaldo descer.":

                jump later2
        
        return

label rightaway2:

        play music "TownTheme.mp3"

        show jose simpatico
        with dissolve

        "Parabéns! Registrar as encomendas, solicitar identidade e obter a assinatura do morador é crucial para comprovar a retirada."

        scene jose no interfone
        with dissolve

        j "Certo! Já registrei suas encomendas no livro de registro. Por favor, traga sua identidade e assine o livro conforme as normas do condomínio."

        scene apartamentodoednaldo
        with fade

        
        e "Com certeza! Irei procurar minha identidade agora mesmo."

        scene ednaldo no elevador
        with fade

        "Ednaldo desce para a portaria..." 

        scene portaria com caixas

        show ednaldo simpatico
        with dissolve
        
        "...e segue o protocolo do condomínio."

        show ednaldo simpatico
        with dissolve

        play music "The Last Encounter (90s RPG Version) Full Loop.wav"

        e "Você é um exemplo, José. Vou fazer te elogiar para o síndico. Obrigado!"

    # This ends the game.

        return

label later:
    
    play music "Ove Melaa - Times.mp3"

    scene portaria com caixas

    show jose triste
    with dissolve

    "Oh não! Você acabou tropeçando e quebrou todas as encomendas do Sr. Ednaldo."

    scene portaria com caixas

    show jose triste
    with dissolve

    "Esse é um dos motivos para não deixar as encomendas na portaria, nunca se sabe quando um acidente pode acontecer no seu turno."

    scene portaria com caixas

    show jose pensativo
    with dissolve

    play music "Ove Melaa I have just been eaten.mp3"

    menu:

        "O que José deve fazer?"

        "Interfonar para o Sr. Ednaldo.":

            jump rightaway

        "Deixar na portaria.":

            jump later

    return

label later2:

    scene portaria com caixas
    play music "Ove Melaa - Psycho Behind The Keys.mp3"

    show morador ladrao
    with dissolve

    "Um morador diferente retirou as encomendas do Ednaldo sem registrar no livro, resultando na ausência de qualquer registro para o Ednaldo."

    scene portaria com caixas

    show jose com medo
    with dissolve

    "É crucial garantir que o morador em questão seja quem retira as encomendas, evitando incidentes como esse."

    scene portaria com caixas

    show jose pensativo
    with dissolve
    
    play music "Ove Melaa I have just been eaten.mp3"

    menu:

            "O que José deve fazer?"

            "Registrar as encomendas e pedir o documento.":

                jump rightaway2 

            "Esperar Sr. Ednaldo descer.":

                jump later2

    return






