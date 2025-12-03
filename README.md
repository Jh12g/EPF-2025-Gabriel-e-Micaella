# Projeto Template: POO com Python + Bottle + JSON

Este é um projeto de template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.

--- ass

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
│
├── .vscode/
│   └── settings.json
│
├── controllers/
│   ├── __init__.py
│   ├── base_controller.py
│   ├── comentario_controller.py
│   ├── receita_controller.py
│   └── usuario_controller.py
│
├── data/
│   ├── comentarios.json
│   ├── receitas.json
│   ├── users.json
│   └── usuarios.json
│
├── models/
│   ├── base_model.py
│   ├── comentario_model.py
│   ├── entidades.py
│   ├── receita_model.py
│   └── usuario_model.py
│
├── services/
│   ├── comentario_service.py
│   ├── receita_service.py
│   └── usuario_service.py
│
├── static/
│   ├── css/
│   │   ├── helper.css
│   │   └── style.css
│   ├── img/
│   │   └── BottleLogo.png
│   └── js/
│       ├── helper.js
│       └── main.js
│
├── venv/
│   ├── Include/
│   ├── Lib/
│   └── Scripts/
│
├── views/
│   ├── admin/
│   │   ├── dashboard.tpl
│   │   ├── receita_form.tpl
│   │   ├── user_form.tpl
│   │   └── users.tpl
│   ├── usuario/
│   │   ├── lista_receitas.tpl
│   │   ├── painel_opcoes.tpl
│   │   ├── receita_form.tpl
│   │   └── ver_receita.tpl
│   ├── cadastro.tpl
│   ├── helper-final.tpl
│   ├── landing.tpl
│   ├── layout.tpl
│   └── login.tpl
│
├── .gitignore
├── .pylintrc
├── app.py
├── config.py
├── main.py
├── Makefile
├── README.md
├── requirements.txt
└── sessao.py
```


---

## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.

### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- `user.py`: classe `User`, com atributos como `id`, `name`, `email`, etc.

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON. Exemplo:
- `user_service.py`: contém métodos como `get_all`, `add_user`, `delete_user`.

### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
- `layout.tpl`: estrutura base com navegação e bloco `content`.
- `users.tpl`: lista os usuários.
- `user_form.tpl`: formulário para adicionar/editar usuário.

### `static/`
Arquivos estáticos como:
- `css/style.css`: estilos básicos.
- `js/main.js`: scripts JS opcionais.
- `img/BottleLogo.png`: exemplo de imagem.

### `data/`
Armazena os arquivos `.json` que simulam o banco de dados:
- `users.json`: onde os dados dos usuários são persistidos.

---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Personalização
Para adicionar novos modelos (ex: Atividades):

1. Crie a classe no diretório **models/**.

2. Crie o service correspondente para manipulação do JSON.

3. Crie o controller com as rotas.

4. Crie as views .tpl associadas.

---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
