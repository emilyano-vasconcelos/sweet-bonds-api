init python:
    import json
    import urllib.request
    import urllib.error

    API_BASE_URL = "http://127.0.0.1:8000/api"

    def _api_message(data, fallback):
        if isinstance(data, dict):
            return data.get("message") or data.get("error") or fallback
        return fallback

    def _decode_json(raw):
        try:
            if not raw:
                return {}
            return json.loads(raw.decode("utf-8"))
        except Exception:
            return {}

    def _post_json(path, payload):
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            API_BASE_URL + path,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.status, _decode_json(response.read())
        except urllib.error.HTTPError as e:
            return e.code, _decode_json(e.read())

    def _get_json(path):
        try:
            with urllib.request.urlopen(API_BASE_URL + path, timeout=5) as response:
                return response.status, _decode_json(response.read())
        except urllib.error.HTTPError as e:
            return e.code, _decode_json(e.read())

    ########################
    # LOGIN
    ########################
    def login_api():

        store.login_error = ""
        store.password_error = ""

        if not store.user_password:
            store.password_error = "Digite a senha."
            renpy.restart_interaction()
            return

        try:
            status, data = _post_json(
                "/login/",
                {
                    "username": store.username.strip(),
                    "password": store.user_password,
                },
            )

            if 200 <= status < 300 and data.get("success"):
                store.logado = True
                store.login_error = ""

                renpy.hide_screen("login_user_screen")
                renpy.hide_screen("login_password_screen")

                renpy.notify("Login OK")

                renpy.show_screen("main_menu")

            else:
                store.login_error = _api_message(data, "Login inválido.")
                renpy.restart_interaction()

        except Exception:
            store.login_error = "Erro ao conectar com o backend."
            renpy.restart_interaction()
    
    # Verifica se o campo de usuário não está vazio.
    # Se estiver vazio, exibe erro na tela.
    # Caso contrário, avança para a tela de senha.

    def next_login_step():
        if not store.username.strip():
            store.login_error = "Digite o usuário."
            renpy.restart_interaction()
        else:
            store.login_error = ""
            renpy.hide_screen("login_user_screen")
            renpy.show_screen("login_password_screen")


    ########################
    # REGISTER
    ########################
    def register_api():
        store.login_error = ""
        store.reg_password_error = ""

        if not store.reg_password:
            store.reg_password_error = "Digite a senha."
            renpy.restart_interaction()
            return

        try:
            status, data = _post_json(
                "/register/",
                {
                    "username": store.reg_username.strip(),
                    "password": store.reg_password,
                },
            )

            if 200 <= status < 300 and data.get("success"):
                # AUTO LOGIN
                store.username = store.reg_username.strip()
                store.user_password = store.reg_password
                store.reg_username = ""
                store.reg_password = ""
                store.login_error = ""

                store.logado = True

                renpy.notify("Conta criada e logado!")

                renpy.hide_screen("register_user_screen")
                renpy.hide_screen("register_password_screen")

                renpy.show_screen("main_menu")

            else:
                store.login_error = _api_message(data, "Erro ao registrar.")
                renpy.restart_interaction()

        except Exception:
            store.login_error = "Erro ao conectar com o backend."
            renpy.restart_interaction()

    def next_register_step():
        if not store.reg_username.strip():
            store.login_error = "Digite o usuário."
            renpy.restart_interaction()
        else:
            store.login_error = ""
            store.reg_password_error = ""
            renpy.hide_screen("register_user_screen")
            renpy.show_screen("register_password_screen")

    ########################
    # RANKING
    ########################
    def load_ranking():
        try:
            status, data = _get_json("/ranking/")

            if 200 <= status < 300:
                store.ranking_list = data
                renpy.show_screen("ranking")
            else:
                renpy.notify("Erro ao carregar ranking")

        except Exception:
            renpy.notify("Erro ao carregar ranking")

    ########################
    # SCORE
    ########################
    def send_score():
        if not store.username.strip():
            return

        try:
            _post_json(
                "/update-score/",
                {
                    "username": store.username.strip(),
                    "score": store.score,
                },
            )
        except Exception:
            renpy.notify("Erro ao enviar score")
        