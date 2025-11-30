% rebase('layout.tpl', title='Painel Admin')

<div style="text-align: left; max-width: 1000px; margin: 0 auto;">
    
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
        <h2 style="margin: 0; color: #1a2a6c;">⚙️ Gestão de Receitas</h2>
        
        <div style="display: flex; gap: 10px;">
            <a href="/opcoes" style="padding: 10px 20px; background: #e0e0e0; color: #555; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 0.9rem;">⬅ Voltar</a>
            <a href="/users" class="btn-success" style="width: auto; padding: 10px 20px; background: #6c757d; font-size: 0.9rem;">👥 Usuários</a>
            <a href="/nova_receita" class="btn-success" style="width: auto; padding: 10px 20px; font-size: 0.9rem;">+ Nova Receita</a>
        </div>
    </div>

    <div style="background: white; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background: #f8f9fa; color: #444;">
                    <th style="padding: 15px;">ID</th>
                    <th style="padding: 15px;">Título</th>
                    <th style="padding: 15px;">Categoria</th>
                    <th style="padding: 15px;">Status</th>
                    <th style="padding: 15px;">Ações</th>
                </tr>
            </thead>
            <tbody>
                % if not receitas:
                    <tr><td colspan="5" style="padding: 20px; text-align: center;">Nenhuma receita cadastrada.</td></tr>
                % end

                % for r in receitas:
                <tr style="border-bottom: 1px solid #eee;">
                    <td style="padding: 15px;">#{{r['id']}}</td>
                    <td style="padding: 15px; font-weight: bold;">{{r['titulo']}}</td>
                    <td style="padding: 15px;">{{r['categoria']}}</td>
                    <td style="padding: 15px;">
                        % if r.get('status') == 'Pendente':
                            <span style="background: #fff3cd; color: #856404; padding: 5px 10px; border-radius: 20px; font-size: 0.8rem;">Pendente</span>
                        % else:
                            <span style="background: #d4edda; color: #155724; padding: 5px 10px; border-radius: 20px; font-size: 0.8rem;">Ativo</span>
                        % end
                    </td>
                    <td style="padding: 15px; display: flex; align-items: center; gap: 10px;">
                        
                        % if r.get('status') == 'Pendente':
                            <form action="/receitas/aprovar/{{r['id']}}" method="POST" style="margin:0; padding:0; background:none; box-shadow:none;">
                                <button type="submit" style="background: #28a745; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer; font-size: 0.8rem;">✔ Aprovar</button>
                            </form>
                        % end

                        <a href="/receitas/editar/{{r['id']}}" style="color: #3b82f6; font-weight: bold;">Editar</a>

                        <form action="/receitas/delete/{{r['id']}}" method="POST" style="margin:0; padding:0; background:none; box-shadow:none;" onsubmit="return confirm('Apagar receita?');">
                            <button type="submit" style="background: none; border: none; color: #ef4444; font-weight: bold; cursor: pointer;">X</button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>