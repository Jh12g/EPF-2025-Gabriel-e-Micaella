% rebase('layout.tpl', title='Fazer Login')

<link rel="stylesheet" href="/static/css/style.css?v=1002"> 

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

    <form action="/login" method="POST">
    
    <input type="text" name="email" placeholder="Email" required>
    <input type="password" name="senha" placeholder="Senha" required>
    
    <button type="submit">Entrar</button>
    </form>

        <p style="text-align: center; margin-top: 25px; font-size: 0.9rem; color: #666;">
            Não tem conta? <a href="/cadastro" style="color: #801313ff; font-weight: bold;">Cadastre-se aqui</a>
        </p>
    </div>
</div>