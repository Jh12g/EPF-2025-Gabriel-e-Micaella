% rebase('layout.tpl', title='Gerenciar Usuários')

<h2>Usuários Cadastrados</h2>
<a href="/users/add" style="background:green; color:white; padding:5px;">+ Novo Usuário</a>
<br><br>

<table border="1" width="100%">
    <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Email</th>
        <th>Admin?</th>
        <th>Ações</th>
    </tr>
    % for u in users:
    <tr>
        <td>{{u['id']}}</td>
        <td>{{u['nome']}}</td>
        <td>{{u['email']}}</td>
        <td>{{'Sim' if u.get('admin') else 'Não'}}</td>
        <td>
            <a href="/users/edit/{{u['id']}}">Editar</a>
            <form action="/users/delete/{{u['id']}}" method="POST" style="display:inline;">
                <button type="submit" onclick="return confirm('Tem certeza?')">X</button>
            </form>
        </td>
    </tr>
    % end
</table>