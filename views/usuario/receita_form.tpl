% rebase('layout.tpl', title='Nova Receita')

<h2>{{get('titulo_pagina', 'Cadastrar Nova Receita')}}</h2>
<form action="/nova_receita" method="POST">
    <label>Título:</label><br>
    <input type="text" name="titulo" required><br><br>
    
    <label>Ingredientes:</label><br>
    <textarea name="ingredientes" required></textarea><br><br>

    <label>Preparo:</label><br>
    <textarea name="preparo" required></textarea><br><br>

    <label>Tempo (minutos):</label><br>
    <input type="number" name="tempo" required><br><br>

    <label>Categoria:</label>
    <select name="categoria">
        <option value="Cafe">Café da Manhã</option>
        <option value="Almoco">Almoço</option>
        <option value="Janta">Jantar</option>
        <option value="Lanche">Lanche</option>
        <option value="Petisco">Petisco</option>
        <option value="Cachorro">Comida de Cachorro</option>
        <option value="Gato">Comida de Gato</option>
    </select><br><br>
    
    <label>Tipo:</label>
    <select name="tipo">
        <option value="padrao">Humano</option>
        <option value="pet">Animal</option>
    </select><br><br>
    
    <label>Espécie (se for pet):</label>
    <input type="text" name="especie"><br><br>

    <button type="submit">Salvar Receita</button>
</form>