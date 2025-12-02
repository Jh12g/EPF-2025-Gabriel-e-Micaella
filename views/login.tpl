% rebase('layout.tpl', title='Login')

<div class="login-container">
    <div class="card-login">
        
        <h2 class="login-title">Bem-vindo!</h2>
        <p class="login-subtitle">Acesse sua conta para continuar</p>

        % if get('erro'):
            <div class="alert-error">
                ⚠️ {{erro}}
            </div>
        % end

        <form action="/login" method="POST">
            <div class="form-group">
                <label class="form-label">Seu E-mail</label>
                <input type="text" name="email" class="form-input" placeholder="exemplo@email.com" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Sua Senha</label>
                <input type="password" name="senha" class="form-input" placeholder="senha" required>
            </div>
            
            <button type="submit" class="btn-success">Entrar</button>
        </form>

        <p class="login-footer">
            Não tem conta? <a href="/cadastro" class="login-link">Cadastre-se aqui</a>
        </p>
    </div>
</div>