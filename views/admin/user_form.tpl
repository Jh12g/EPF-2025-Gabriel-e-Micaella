% rebase('layout.tpl', title='Gerenciar Usuário')

<div class="container" style="max-width: 600px; margin-top: 40px;">
    
    <div style="text-align: center; margin-bottom: 30px;">
        <h2 style="color: #1a2a6c; margin: 0; font-weight: 800;">
            {{'✏️ Editar Usuário' if user else '➕ Novo Usuário'}}
        </h2>
        <p style="color: #666; margin-top: 5px;">Preencha os dados abaixo</p>
    </div>

    <form action="{{action}}" method="POST">
        
        <div style="margin-bottom: 20px;">
            <label>Nome Completo</label>
            <input type="text" name="nome" value="{{user['nome'] if user else ''}}" required placeholder="Ex: João da Silva">
        </div>

        <div style="margin-bottom: 20px;">
            <label>Email</label>
            <input type="email" name="email" value="{{user['email'] if user else ''}}" required placeholder="exemplo@email.com">
        </div>

        <div style="margin-bottom: 20px;">
            <label>Senha</label>
            <input type="password" name="senha" placeholder="{{'Deixe em branco para manter a atual' if user else 'Crie uma senha'}}">
            % if not user:
                <small style="color: #3b82f6; font-size: 0.8rem;">* Obrigatória para novos usuários</small>
            % end
        </div>

        <div style="margin-bottom: 30px; background: #f8fbff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; display: flex; align-items: center; gap: 10px;">
            <input type="checkbox" name="admin" id="adminCheck" {{'checked' if user and user.get('admin') else ''}} style="width: 20px; height: 20px; margin: 0;">
            <label for="adminCheck" style="margin: 0; cursor: pointer; color: #1a2a6c;">Conceder permissão de Administrador?</label>
        </div>

        <div style="display: flex; gap: 15px;">
            <a href="/users" style="flex: 1; text-align: center; padding: 15px; background: #e0e0e0; color: #555; border-radius: 30px; font-weight: bold; text-decoration: none;">
                Cancelar
            </a>
            
            <button type="submit" class="btn-success" style="flex: 2;">
                Salvar Dados
            </button>
        </div>

    </form>
</div>