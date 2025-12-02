% rebase('layout.tpl', title='Criar Conta')

<div style="max-width: 400px; margin: 50px auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background: white;">
    <h2 style="text-align: center;">Criar Nova Conta</h2>

    <form action="/cadastro" method="POST">
    
    <input type="text" name="nome" placeholder="Nome" required>
    <input type="text" name="email" placeholder="Email" required>
    <input type="password" name="senha" placeholder="Senha" required>
    
    <button type="submit">Cadastrar</button>
    </form>
    
    <p style="text-align: center; margin-top: 15px;">
        Já tem conta? <a href="/login">Faça Login</a>.
    </p>
</div>