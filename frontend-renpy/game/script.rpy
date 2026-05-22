# Declare characters used by this game.
define n = Character(_("Natsuki"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")
define s = Character(_("Sylvie"), color="#ffc8c8")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.

default username = ""
default user_password = ""
default logado = False
default login_error = ""
default password_error = ""
default reg_password_error = ""
default reg_username = ""
default reg_password = ""
default score = 0
default book = False
default ranking_list = []

#init python:
#
#    def check_login():
#
#        if store.username == "admin" and store.password == "123":
#
#            renpy.hide_screen("login_screen")
#            renpy.jump("historia")
#
#        else:
#
#            store.login_error = "Usuário ou senha incorretos"

# The game starts here.
label start:

    "Bem-vindo ao jogo!"

    jump historia

label historia:

    # Start by playing some music.
    play music "illurock.opus"

    scene backgroundsescolasaladeaula
    with fade

    "Faz apenas algumas semanas que eu me mudei para esta escola desde um incidente que levou meus pais a se mudarem repentinamente"

    "Fui diagnosticado com câncer no fígado alguns meses atrás. Então eles buscaram fazer a mudança o mais rápido possível."

    "Desde minha chegada, eu ainda não tive tempo de fazer nenhum amigo ou colega... talvez isso não seja algo completamente ruim, já que eu precisava tomar um tempo para processar tudo"

    "Eu costumo frequentar as aulas, ler um pouco na biblioteca e nos dias que não tenho tratamento, vou direto pro dormitório."

    scene bg uni
    with fade

    "Essa hora eu geralmente costumo vir aqui para comer depois das aulas da manhã. É tranquilo e eu posso observar os pássaros comerem os farelos que eu ocasionalmente deixo cair no chão"

    "Ao me aproximar do banco que eu geralmente ocupo, eu vejo uma figura de uma garota sentada. Especificamente uma de cabelos castanhos e postura serena. Ela é um pouco familiar..."
    
    scene bg uni
    show natsukiseria:

        zoom 1.8
        xalign 0.5
        yalign 1.0

    
    n "Ah... oi, você é o garoto novo da turma né? É um prazer, meu nome é Natsuki"

    m "Ah, sim, isso mesmo. Meu nome é Nanami, o prazer é meu."

    " É estranho... a garota parecia ter um ar muito mais sério do que simpático, mas ela estranhamente transmite uma sensação total diferente de apatia."
 

    scene bg uni
    show natsukifeliz:

        zoom 1.8
        xalign 0.5
        yalign 1.0

    
    n "Então... você já conheceu a cantina da escola? Ou já ingressou em algum clube?"

    m "Na verdade não... os únicos lugares que realmente frequentei foram a sala de aula e meu dormitório. Ah... e a biblioteca também. É um lugar agradável e silencioso."

    n "Então que tal irmos juntos? Eu não tenho nada pra fazer e preciso entregar alguns livros emprestados que estão na minha mochila."
    
    m "Claro, seria ótimo. Também quero pegar algumas obras de lá... vi que tinha algumas HQ's legais."

    scene corredorbiblio
    with fade

    "O caminho até a biblioteca é tranquilo, apesar do leve nervosismo por estar perto de alguém que eu literalmente acabei de conhecer..."

    "É estranho pensar que minutos atrás eu só conhecia as pessoas de cara, e agora estou indo para a biblioteca com uma garota aleatória..."

    "Bem... na verdade acho que é mais comum que penso, aliás, estou em uma escola"

    "Antes que eu pudesse pensar mais, chegamos na biblioteca."

    scene bibliotecainterior

    "Posso observar várias figuras... algumas concentradas em livros, outras conversando baixinho e outras apenas descansando."

    "Em geral, a biblioteca continua com a mesma sensação aconchegante e calma que eu venho presenciando na minha primeira semana"

    
    scene bibliotecainterior
    show natsukifeliz: 

        zoom 1.8
        yalign 0.5 
        xalign 1.0



    n "Eu vou entregar os livros para a bibliotecária... pode ir procurando sua HQ, eu volto já."

    scene bibliotecainterior

    "Eu me ocupo em procurar pelas prateleiras levemente empoeiradas da biblioteca por algo que me lembre uma HQ."

    "Quem sabe algo como Superman ou Flash... ou talvez isso seja exigir demais de uma biblioteca escolar."

    "Mesmo a escola sendo particular e especialmente cara, isso não significa que eu posso achar esse tipo de livro aqui, né?"

    "Depois de alguns minutos, eu pego uma HQ que parecia legal. O título era O Eternauta e o interior era completamente preto e branco."

    "Eu me sento em um banco para ler, e antes mesmo que eu pudesse terminar a primeira página, eu sinto alguém se aproximar rapidamente e levanto o olhar."

    "É Natsuki."


    scene bibliotecainterior
    show natsukipreocupada:

        zoom 1.8
        xalign 0.5
        yalign 1.0


    with dissolve

    n "Parece que houve um incidente com o professor de matemática..."

    n "Ele não vai poder nos dar as próximas aulas então... ficaremos livres até o final do dia."

    m "Caramba... e como você soube disso tão rápido?"

    n "A bibliotecária é minha amiga... eu costumo vir muito pra cá então eventualmente eu acho que isso iria acontecer."


    "Já que temos o resto do dia livre, eu poderia aproveitar para comer algo no centro... Não fica tão longe daqui de qualquer forma..."

    menu:

        "Antes que eu possa sugerir a ideia, Natsuki dá um leve tapa no meu ombro, e sorrindo me pergunta:"

        "Então... Já que temos o dia livre, o que acha de experimentar o melhor doce daqui do centro?"

        "Eu e minha barriga parecemos concordar.":

            jump rightaway

        "Acho que eu prefiro ficar pela escola...":

            jump later


label rightaway:

    scene bibliotecainterior
    show natsukifeliz:

        zoom 1.8
        xalign 0.5
        yalign 1.0


    n "Tem uma loja de doces simplesmente incrível... eles vendem a melhor torta de limão que já comi."

    m "Torta de limão, é?... Ainda prefiro as tortinhas de maracujá! São deliciosas e difícil de errar a receita."

    "Não consigo evitar sorrir com a conversa agradável e seu aparente entusiasmo com a lojinha de doces."

    scene bg meadow

    "Nós andamos pela avenida por alguns minutos antes de chegarmos finalmente até a lojinha. Poucos carros passaram e o comércio parecia mais calmo que deveria... pelo menos é a impressão que tenho."

    "Natsuki me levou diretamente até o interior da loja. O cheiro de chantilly e açúcar pairavam no ar, e eu precisei me conter para não lamber os lábios com aquela sensação."
    
    
    scene lojadedoce
    with fade

    "Nos sentamos em uma pequena mesa e pedimos o que queriamos. Nós comemos com calma e "

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show sylvie green surprised

    "Silence."

    "She looks so shocked that I begin to fear the worst. But then..."

    show sylvie green smile

    menu:

        s "Sure, but what's a \"visual novel?\""

        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book


label game:

    m "It's a kind of videogame you can play on your computer or a console."

    m "Visual novels tell a story with pictures and music."

    m "Sometimes, you also get to make choices that affect the outcome of the story."

    s "So it's like those choose-your-adventure books?"

    m "Exactly! I've got lots of different ideas that I think would work."

    m "And I thought maybe you could help me...since I know how you like to draw."

    m "It'd be hard for me to make a visual novel alone."

    show sylvie green normal

    s "Well, sure! I can try. I just hope I don't disappoint you."

    m "You know you could never disappoint me, Sylvie."

    jump marry


label book:

    $ book = True

    m "It's like an interactive book that you can read on a computer or a console."

    show sylvie green surprised

    s "Interactive?"

    m "You can make choices that lead to different events and endings in the story."

    s "So where does the \"visual\" part come in?"

    m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    show sylvie green smile

    s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

    m "That's great! So...would you be interested in working with me as an artist?"

    s "I'd love to!"

    jump marry

label marry:

    scene black
    with dissolve

    "And so, we become a visual novel creating duo."

    scene bg club
    with dissolve

    "Over the years, we make lots of games and have a lot of fun making them."

    if book:

        "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

    "We take turns coming up with stories and characters and support each other to make some great games!"

    "And one day..."

    show sylvie blue normal
    with dissolve

    s "Hey..."

    m "Yes?"

    show sylvie blue giggle

    s "Will you marry me?"

    m "What? Where did this come from?"

    show sylvie blue surprised

    s "Come on, how long have we been dating?"

    m "A while..."

    show sylvie blue smile

    s "These last few years we've been making visual novels together, spending time together, helping each other..."

    s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"

    m "Sylvie..."

    show sylvie blue giggle

    s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"

    show sylvie blue normal

    s "So will you marry me?"

    m "Of course I will! I've actually been meaning to propose, honest!"

    s "I know, I know."

    m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."

    show sylvie blue giggle

    s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"

    scene black
    with dissolve

    "We get married shortly after that."

    "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."

    "Together, we live happily ever after even now."

    "{b}Good Ending{/b}."

    return

label later:

    "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

    scene black
    with dissolve

    "But I'm an indecisive person."

    "I couldn't ask her that day and I end up never being able to ask her."

    "I guess I'll never know the answer to my question now..."

    "{b}Bad Ending{/b}."

    return

