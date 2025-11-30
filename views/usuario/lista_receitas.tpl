% rebase('layout.tpl', title=titulo)

<h2 style="color: #1a2a6c; margin-bottom: 30px;">🍽️ {{titulo}}</h2>

% if not receitas:
    <div style="background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <p>Nenhuma receita encontrada nesta categoria.</p>
        <a href="/sugerir" class="btn-success" style="width: auto; display: inline-block; padding: 10px 20px;">+ Adicionar Primeira</a>
    </div>
% end

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 25px;">
    
    % for r in receitas:
    <a href="/receita/{{r['id']}}" style="text-decoration: none; color: inherit;">
        <div style="background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.2s; height: 100%;">
            
            <div style="height: 150px; overflow: hidden;">
                <img src="{{r.get('imagem', 'https://placehold.co/600x400')}}" alt="{{r['titulo']}}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>

            <div style="padding: 20px;">
                <h3 style="margin: 0 0 10px 0; color: #333; font-size: 1.2rem;">{{r['titulo']}}</h3>
                
                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #777;">
                    <span>⏱ {{r['tempo']}} min</span>
                    
                    % if r.get('dificuldade') == 'Fácil':
                        <span style="color: green; font-weight: bold;">🟢 Fácil</span>
                    % elif r.get('dificuldade') == 'Médio':
                        <span style="color: orange; font-weight: bold;">🟡 Médio</span>
                    % else:
                        <span style="color: red; font-weight: bold;">🔴 Difícil</span>
                    % end
                </div>
            </div>
        </div>
    </a>
    % end
</div>

<style>
    div[style*="transition"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.2) !important;
    }
</style>