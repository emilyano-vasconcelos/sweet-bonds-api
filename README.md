# 🍬 Sweet Bonds

Visual Novel desenvolvida com **Ren'Py** e backend em **Django**, com sistema de login, registro e ranking online.

---

## 🎮 Sobre o projeto

Sweet Bonds é um jogo estilo visual novel onde o jogador acompanha a história enquanto acumula pontos.  
O sistema conta com autenticação de usuário e ranking online integrado via API.

---

## 🚀 Tecnologias utilizadas

- 🎮 Ren'Py (frontend do jogo)
- 🐍 Django (backend / API)
- 🌐 API REST

---

## 📁 Estrutura do projeto

sweet-bonds/
├── backend-django/   # API em Django  
├── frontend-renpy/   # Jogo em Ren'Py  

---

## ⚙️ Como rodar o projeto

### 🔹 1. Rodar o backend (Django)

Abra o terminal:

cd backend-django

### Criar ambiente virtual (venv)

Windows:

python -m venv venv
venv\Scripts\activate

Linux / Mac:

python3 -m venv venv
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

Inicie o servidor:

python manage.py runserver

O backend estará disponível em:
http://127.0.0.1:8000/api

---

### 🔹 2. Rodar o frontend (Ren'Py)

1. Abra o Ren'Py Launcher  
2. Clique em "Open Project"  
3. Selecione a pasta:

frontend-renpy

4. Clique em "Launch Project"

---

## 🔐 Funcionalidades

- Registro de usuário  
- Login  
- Sistema de pontuação  
- Ranking online  
- Jogar sem login  

---

## 📡 Endpoints da API

POST /api/register/ → criar conta  
POST /api/login/ → autenticação  
GET /api/ranking/ → ranking  
POST /api/update-score/ → enviar pontuação  

---

## ⚠️ Observações importantes

- O backend precisa estar rodando antes de abrir o jogo  
- O jogo se conecta via http://127.0.0.1:8000/api  

---

## 👨‍💻 Autor

Emilyano Vasconcelos  

---

## 📌 Próximas melhorias

- Deploy do backend  
- Sistema de perfil  
- Melhorias visuais  
- Adicionar imagens no README  