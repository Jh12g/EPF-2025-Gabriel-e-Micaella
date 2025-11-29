% rebase('layout.tpl', title='Formulário Usuário')

<section class="form-section">
    <h1>{{'Editar Usuário' if user else 'Adicionar Usuário'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container">
        
        <div class="form-group">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" required 
                   value="{{user['nome'] if user else ''}}">
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required 
                   value="{{user['email'] if user else ''}}">
        </div>
        
        <div class="form-group">
            <label for="senha">Senha:</label>
            <input type="password" id="senha" name="senha" 
                   placeholder="{{'Deixe em branco para manter a atual' if user else 'Obrigatória no cadastro'}}">
        </div>

        <div class="form-group" style="margin-top: 10px;">
            <label>
                <input type="checkbox" name="admin" 
                       {{'checked' if user and user.get('admin') else ''}}>
                Usuário Administrador?
            </label>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <a href="/users" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>