########################
# LOGIN - USUÁRIO
########################
screen login_user_screen():
    tag menu
    modal True

    add "gui/main_menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 520
        padding (35, 30)

        vbox:
            spacing 18
            xalign 0.5

            text "Login" size 42 xalign 0.5
            text "Entre para salvar sua pontuação e aparecer no ranking." xalign 0.5 text_align 0.5

            if login_error:
                text "[login_error]" color "#ff6666" xalign 0.5 text_align 0.5

            text "Usuário"
            input value VariableInputValue("username") xsize 430 length 32 changed SetVariable("login_error", "")

            hbox:
                spacing 15
                xalign 0.5

                textbutton "Próximo":
                    action  Function(next_login_step)
                textbutton "Registrar":
                    action [Hide("login_user_screen"), Show("register_user_screen")]

            textbutton "Jogar sem login":
                xalign 0.5
                action Jump("historia")
            textbutton "Voltar ao menu":
                xalign 0.5
                action [Hide("login_user_screen"), Show("main_menu")]


########################
# LOGIN - SENHA
########################
screen login_password_screen():
    modal True

    add "gui/main_menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 520
        padding (35, 30)

        vbox:
            spacing 18
            xalign 0.5

            text "Senha" size 42 xalign 0.5

            if password_error:
                text "[password_error]" color "#ff6666" xalign 0.5 text_align 0.5


            text "Senha"
            input value VariableInputValue("user_password") xsize 430 length 64 mask "*" changed SetVariable("password_error", "")

            hbox:
                spacing 15
                xalign 0.5

                textbutton "Entrar":
                    action Function(login_api)

                textbutton "Voltar":
                    action [Hide("login_password_screen"), Show("login_user_screen")]


########################
# REGISTER - USUÁRIO
########################
screen register_user_screen():
    modal True

    add "gui/main_menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 520
        padding (35, 30)

        vbox:
            spacing 18
            xalign 0.5

            text "Criar conta" size 38 xalign 0.5

            if login_error:
                text "[login_error]" color "#ff6666" xalign 0.5 text_align 0.5

            text "Novo usuário"
            input value VariableInputValue("reg_username") xsize 430 length 32 changed SetVariable("login_error", "")

            hbox:
                spacing 15
                xalign 0.5

                textbutton "Próximo":
                    action Function(next_register_step)

                textbutton "Voltar":
                    action [Hide("register_user_screen"), Show("login_user_screen")]


########################
# REGISTER - SENHA
########################
screen register_password_screen():
    modal True

    add "gui/main_menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 520
        padding (35, 30)

        vbox:
            spacing 18
            xalign 0.5

            text "Senha" size 38 xalign 0.5

            if reg_password_error:
                text "[reg_password_error]" color "#ff6666" xalign 0.5 text_align 0.5

            text "Senha"
            input value VariableInputValue("reg_password") xsize 430 length 64 mask "*" changed SetVariable("reg_password_error", "")   

            hbox:
                spacing 15
                xalign 0.5

                textbutton "Registrar":
                    action Function(register_api)

                textbutton "Voltar":
                    action [Hide("register_password_screen"), Show("register_user_screen")]


########################
# RANKING (igual ao seu)
########################
screen ranking():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 480
        padding (30, 25)

        vbox:
            spacing 12

            text "Ranking" size 36 xalign 0.5

            if ranking_list:
                for player in ranking_list:
                    text "[player['username']] - [player['score']] pontos"
            else:
                text "Nenhuma pontuação registrada ainda." xalign 0.5

            textbutton "Fechar":
                xalign 0.5
                action Hide("ranking")