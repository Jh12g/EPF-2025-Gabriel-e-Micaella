% rebase('layout.tpl', title='Fazer Login')

<link rel="stylesheet" href="/static/css/style.css?v=1002"> 

<div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000; background: rgba(255, 255, 255, 0.9); padding: 10px; border-radius: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
    <button onclick="alterarFonte('diminuir')" aria-label="Diminuir letra" style="cursor: pointer; width: 40px; height: 40px; border: 1px solid #ccc; background: white; border-radius: 50%; font-weight: bold; color: #333; margin-right: 5px;">A-</button>
    <button onclick="alterarFonte('aumentar')" aria-label="Aumentar letra" style="cursor: pointer; width: 40px; height: 40px; border: 1px solid #ccc; background: white; border-radius: 50%; font-weight: bold; color: #333;">A+</button>
</div>
<div class="login-container"> 
    
    <div class="card-login" style="background: white;"> 
        
        <div style="text-align: center; margin-bottom: 30px;">
            <h2 style="color: #620202ff; margin: 0; font-size: 1.8rem; font-weight: 800;">Fazer Login</h2>
            <p style="color: #666; font-size: 0.95rem; margin-top: 5px;">Acesse sua conta para continuar</p>
        </div>

        % if get('erro'):
            <div class="alerta-erro" style="background: #fee2e2; color: #b91c1c; padding: 12px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
                ⚠️ {{erro}}
            </div>
        % end

        <form action="/login" method="POST" style="box-shadow: none; padding: 0;">
            
            <div style="margin-bottom: 20px; text-align: left;">
                <label style="font-size: 1rem;">Email</label>
                <input type="email" name="email" placeholder="seu@email.com" required style="font-size: 1rem;">
            </div>
            
            <div style="margin-bottom: 30px; text-align: left;">
                <label style="font-size: 1rem;">Senha</label>
                <input type="password" name="senha" placeholder="Sua senha" required style="font-size: 1rem;">
            </div>
            
            <button type="submit" class="btn-success" style="width: 100%; padding: 15px; font-size: 1rem; border-radius: 30px;">
                Entrar
            </button>
        </form>

        <p style="text-align: center; margin-top: 25px; font-size: 0.9rem; color: #666;">
            Não tem conta? <a href="/cadastro" style="color: #801313ff; font-weight: bold;">Cadastre-se aqui</a>
        </p>
    </div>
</div>

<script>
    function alterarFonte(acao) {
        const elementoHtml = document.documentElement;
        const estiloAtual = window.getComputedStyle(elementoHtml, null).getPropertyValue('font-size');
        let tamanhoAtual = parseFloat(estiloAtual);
        const tamanhoMinimo = 12; 
        const tamanhoMaximo = 24; 

        if (acao === 'aumentar' && tamanhoAtual < tamanhoMaximo) {
            elementoHtml.style.fontSize = (tamanhoAtual + 2) + 'px';
        } else if (acao === 'diminuir' && tamanhoAtual > tamanhoMinimo) {
            elementoHtml.style.fontSize = (tamanhoAtual - 2) + 'px';
        }
    }
</script>