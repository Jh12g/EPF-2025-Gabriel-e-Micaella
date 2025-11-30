% rebase('layout.tpl', title='Gerenciar Usuários')

<div style="text-align: left; max-width: 900px; margin: 0 auto;">
    
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
        <h2 style="margin: 0; color: #1a2a6c;">👥 Usuários Cadastrados</h2>
        
        <a href="/users/add" class="btn-success" style="width: auto; padding: 10px 20px; font-size: 0.9rem;">
            + Novo Usuário
        </a>
    </div>

    <div style="background: white; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background: #f8f9fa; color: #444;">
                    <th style="padding: 15px; text-align: left;">ID</th>
                    <th style="padding: 15px; text-align: left;">Nome</th>
                    <th style="padding: 15px; text-align: left;">Email</th>
                    <th style="padding: 15px; text-align: left;">Admin?</th>
                    <th style="padding: 15px; text-align: left;">Ações</th>
                </tr>
            </thead>
            <tbody>
                % for u in users:
                <tr style="border-bottom: 1px solid #eee;">
                    <td style="padding: 15px;">#{{u['id']}}</td>
                    <td style="padding: 15px; font-weight: bold;">{{u['nome']}}</td>
                    <td style="padding: 15px;">{{u['email']}}</td>
                    <td style="padding: 15px;">
                        % if u.get('admin'):
                            <span style="color: #3b82f6; font-weight: bold;">Sim</span>
                        % else:
                            <span style="color: #777;">Não</span>
                        % end
                    </td>
                    <td style="padding: 15px;">
                        <a href="/users/edit/{{u['id']}}" style="color: #3b82f6; font-weight: bold; margin-right: 10px;">Editar</a>
                        
                        <form action="/users/delete/{{u['id']}}" method="POST" style="display:inline;" onsubmit="return confirm('Tem certeza?');">
                            <button type="submit" style="background: none; border: none; color: #ef4444; font-weight: bold; cursor: pointer;">Excluir</button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>