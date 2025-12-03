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

    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 9999; background: rgba(255, 255, 255, 0.95); padding: 8px; border-radius: 50px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: 1px solid #e0e0e0; display: flex; gap: 5px;">
        <button onclick="alterarFonte('diminuir')" aria-label="Diminuir letra" style="cursor: pointer; width: 35px; height: 35px; border: 1px solid #ccc; background: white; border-radius: 50%; font-weight: bold; color: #333; display: flex; align-items: center; justify-content: center; font-size: 14px;">A-</button>
        <button onclick="alterarFonte('aumentar')" aria-label="Aumentar letra" style="cursor: pointer; width: 35px; height: 35px; border: 1px solid #ccc; background: white; border-radius: 50%; font-weight: bold; color: #333; display: flex; align-items: center; justify-content: center; font-size: 14px;">A+</button>
    </div>

    <script>
        function alterarFonte(acao) {
            const elementoHtml = document.documentElement;
            const estiloAtual = window.getComputedStyle(elementoHtml, null).getPropertyValue('font-size');
            let tamanhoAtual = parseFloat(estiloAtual);
            
            // Limites (Mínimo 12px, Máximo 24px)
            const tamanhoMinimo = 12; 
            const tamanhoMaximo = 24; 

            if (acao === 'aumentar' && tamanhoAtual < tamanhoMaximo) {
                elementoHtml.style.fontSize = (tamanhoAtual + 2) + 'px';
            } else if (acao === 'diminuir' && tamanhoAtual > tamanhoMinimo) {
                elementoHtml.style.fontSize = (tamanhoAtual - 2) + 'px';
            }
        }
    </script>
    </body>
</html>