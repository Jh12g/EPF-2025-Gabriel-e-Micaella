% rebase('layout.tpl', title='Criar Conta')

<div style="max-width: 400px; margin: 50px auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background: white;">
    <h2 style="text-align: center;">Criar Nova Conta</h2>

    <form action="/cadastro" method="POST">
        <label>Nome Completo:</label><br>
        <input type="text" name="nome" required style="width: 100%; padding: 8px; margin-bottom: 15px;"><br>

        <label>Email:</label><br>
        <input type="email" name="email" required style="width: 100%; padding: 8px; margin-bottom: 15px;"><br>
        
        <label>Senha:</label><br>
        <input type="password" name="senha" required style="width: 100%; padding: 8px; margin-bottom: 20px;"><br>
        
        <button type="submit" class="btn-success" style="width: 100%;">Cadastrar</button>
    </form>
    
    <p style="text-align: center; margin-top: 15px;">
        Já tem conta? <a href="/login">Faça Login</a>.
    </p>
</div>