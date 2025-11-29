% rebase('layout.tpl', title='Painel Admin')

<h2>Painel de Controle - Receitas</h2>
<table border="1" width="100%">
    <tr>
        <th>ID</th>
        <th>Título</th>
        <th>Categoria</th>
        <th>Status</th>
    </tr>
    % for r in receitas:
    <tr>
        <td>{{r['id']}}</td>
        <td>{{r['titulo']}}</td>
        <td>{{r['categoria']}}</td>
        <td>{{r['status']}}</td>
    </tr>
    % end
</table>