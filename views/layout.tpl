<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{get('title', 'Sistema de Receitas')}}</title>
    <link rel="stylesheet" href="/static/css/style.css?v=2000">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Round" rel="stylesheet">
</head>
<body>

    <header>
        <nav>
            <h1> 📕 Livro de Receitas </h1>
            <h2> Aprenda e Ensine <h2>
            <div class="nav-links">
                <a href="/" style="margin-right: 20px;">Tela de Início</a>
                
               % if logado:
                    <a href="/opcoes">Painel</a>
                    
                    % if get('is_admin'):
                        <a href="/admin">Admin</a>
                    % end
                    
                    <a href="/logout" class="btn-danger" onclick="return confirm('Tem certeza que deseja sair?');">Sair</a>
                % else:
                    <a href="/login" class="btn-success" style="display:inline-block; width:auto; padding: 8px 20px;">Login</a>
                % end
            </div>
        </nav>
    </header>

    <div style="flex: 1; display: flex; flex-direction: column; width: 100%; max-width: 1000px; margin: 0 auto; padding: 20px;">
        {{!base}}
    </div>

    <footer>
        <p>&copy; 2025, Projeto OO Python + Bottle. Todos os direitos reservados.</p>
    </footer>

</body>
</html>