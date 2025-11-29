% rebase('layout.tpl', title='Login')

<div style="max-width: 400px; margin: 50px auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background: white;">
    <h2 style="text-align: center;">Fazer Login</h2>
    
    % if get('erro'):
        <div style="background: #f8d7da; color: #721c24; padding: 10px; margin-bottom: 15px; border-radius: 5px;">
            {{erro}}
        </div>
    % end

    <form action="/login" method="POST">
        <label>Email:</label><br>
        <input type="email" name="email" required style="width: 100%; padding: 8px; margin-bottom: 15px;"><br>
        
        <label>Senha:</label><br>
        <input type="password" name="senha" required style="width: 100%; padding: 8px; margin-bottom: 20px;"><br>
        
        <button type="submit" class="btn-success" style="width: 100%;">Entrar</button>
    </form>
    
    <p style="text-align: center; margin-top: 15px;">
        Ainda não tem conta? <a href="/cadastro">Cadastre-se aqui</a>.
    </p>
</div>