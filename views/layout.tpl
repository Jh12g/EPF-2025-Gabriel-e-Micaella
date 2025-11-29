<!DOCTYPE html>

<html lang="pt-br">

 /*pra que esse laout: ele contém a header do site, o menu de navegaçao, o rodapé (Footer) e O link p o CSS*/

<head>
    <meta charset="UTF-8" />
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Sistema Bottle - {{get('title', 'Sistema de Receitas')}}</title>
    
    <link rel="stylesheet" href="/static/css/style.css" />

    <style>
        /* define a fonte padrão e remove margens brancas do navegador */
        body { margin: 0; font-family: sans-serif; background-color: #f4f4f4; }
        
        /* estilo da faixa de qualquer cor do topo do cabeçalho */
        header { background: #ff6600; padding: 10px; text-align: center; color: white; }
        
        /* estilo da barra de menu */
        nav { background: #333; overflow: hidden; }
        
        /* estilo dos botões do menu */
        nav a { float: left; display: block; color: white; padding: 14px 16px; text-decoration: none; }
        
        /* efeito quando passa o mouse em cima do link (fica cinza) */
        nav a:hover { background: #ddd; color: black; }
        
        /* caixa branca central onde vai o conteúdo principal */
        .container { padding: 20px; background: white; margin: 20px auto; max-width: 900px; border-radius: 8px; }
        
        /* estilo do rodapé cinza lá embaixo */
        footer { text-align: center; padding: 20px; background: #ddd; margin-top: 20px; }
    </style>
</head>

<body>

    <header>
        <h1>🍳 Livro de Receitas & Pets</h1>
    </header>

    <nav>
        <a href="/cafe">Café</a>
        <a href="/almoco">Almoço</a>
        <a href="/janta">Janta</a>
        <a href="/petisco">Petisco</a>
        <a href="/cachorro">Pets</a>
        
        <div style="float: right;">
            <a href="/sugerir">Sugerir</a>
            <a href="/admin"> Admin</a>
            <a href="/users">Usuários</a>
        </div>
    </nav>

    <div class="container">
        {{!base}}  
    </div>

    <footer>
        <p>&copy; 2025, Projeto OO Python + Bottle. Todos os direitos reservados.</p>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>