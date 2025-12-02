% rebase('layout.tpl', title='Criar Conta')

<div class="login-container">
    <div class="card-login">
        
        <h2 class="login-title">Crie sua Conta</h2>
        <p class="login-subtitle">Junte-se à nossa comunidade!</p>

        % if get('erro'):
            <div class="alert-error">
                ⚠️ {{erro}}
            </div>
        % end

        <form action="/cadastro" method="POST">
            <div class="form-group">
                <label class="form-label">Seu Nome</label>
                <input type="text" name="nome" class="form-input" placeholder="Como quer ser chamado?" required>
            </div>

            <div class="form-group">
                <label class="form-label">Seu Email</label>
                <input type="text" name="email" class="form-input" placeholder="exemplo@email.com" required>
            </div>
            
            <div class="form-group">
                <label class="form-label">Sua Senha</label>
                <input type="password" name="senha" class="form-input" placeholder="Crie uma senha segura" required>
            </div>
            
            <button type="submit" class="btn-success">Criar Conta</button>
        </form>

        <p class="login-footer">
            Já tem conta? <a href="/login" class="login-link">Faça Login</a>
        </p>
    </div>
</div>