% rebase('layout.tpl', title=get('titulo_pagina', 'Nova Receita'))

<div class="container" style="max-width: 800px; margin-top: 40px;">
    
    <div style="background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: left;">
        
        <h2 style="color: #1a2a6c; margin-bottom: 20px; text-align: center;">
            {{get('titulo_pagina', 'Cadastrar Nova Receita')}}
        </h2>

        % action_url = f"/receitas/editar/{receita['id']}" if defined('receita') and receita else "/nova_receita"
        
        <form action="{{action_url}}" method="POST" style="box-shadow: none; padding: 0;">
            
            <label>Título da Receita:</label>
            <input type="text" name="titulo" required 
                   value="{{receita['titulo'] if defined('receita') and receita else ''}}">
            
            <label>Ingredientes:</label>
            <textarea name="ingredientes" required style="height: 100px;">{{receita['ingredientes'] if defined('receita') and receita else ''}}</textarea>

            <label>Modo de Preparo:</label>
            <textarea name="preparo" required style="height: 100px;">{{receita['preparo'] if defined('receita') and receita else ''}}</textarea>

            <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                <div style="flex: 1;">
                    <label>Tempo (minutos):</label>
                    <input type="number" name="tempo" required
                           value="{{receita['tempo'] if defined('receita') and receita else ''}}">
                </div>
                
                <div style="flex: 1;">
                    <label>Categoria:</label>
                    <select name="categoria">
                        % cat = receita['categoria'] if defined('receita') and receita else ''
                        <option value="Cafe" {{'selected' if cat == 'Cafe' else ''}}>Café da Manhã</option>
                        <option value="Almoco" {{'selected' if cat == 'Almoco' else ''}}>Almoço</option>
                        <option value="Janta" {{'selected' if cat == 'Janta' else ''}}>Jantar</option>
                        <option value="Lanche" {{'selected' if cat == 'Lanche' else ''}}>Lanche</option>
                        <option value="Petisco" {{'selected' if cat == 'Petisco' else ''}}>Petisco</option>
                        <option value="Cachorro" {{'selected' if cat == 'Cachorro' else ''}}>Comida de Cachorro</option>
                        <option value="Gato" {{'selected' if cat == 'Gato' else ''}}>Comida de Gato</option>
                    </select>
                </div>
            </div>
            
            <hr style="margin: 20px 0; border: 0; border-top: 1px solid #eee;">

            <label>Tipo de Receita:</label>
            <select name="tipo" id="tipoSelect" onchange="mostrarPet()">
                % tipo = receita.get('tipo', 'padrao') if defined('receita') and receita else 'padrao'
                <option value="padrao" {{'selected' if tipo == 'padrao' else ''}}>Padrão (Humano)</option>
                <option value="pet" {{'selected' if tipo == 'pet' else ''}}>Pet (Animal)</option>
            </select>

            <div id="campoEspecie" style="display: {{'block' if tipo == 'pet' else 'none'}}; margin-top: 10px;">
                <label>Espécie do Animal:</label>
                <input type="text" name="especie" placeholder="Ex: Cachorro, Gato..."
                       value="{{receita.get('especie', '') if defined('receita') and receita else ''}}">
            </div>

            <br>
            <button type="submit" class="btn-success">Salvar Receita</button>
        </form>
    </div>
</div>

<script>
function mostrarPet() {
    var tipo = document.getElementById("tipoSelect").value;
    var divPet = document.getElementById("campoEspecie");
    divPet.style.display = (tipo === "pet") ? "block" : "none";
}
</script>