% rebase('layout.tpl', title=titulo)

<h2>🍽️ {{titulo}}</h2>

% if not receitas:
    <p>Nenhuma receita encontrada.</p>
% end

<ul>
% for r in receitas:
    <li style="border-bottom: 1px solid #ccc; padding: 10px;">
        <h3>{{r['titulo']}}</h3>
        <p>Tempo: {{r['tempo']}} min | 
           Dificuldade: 
           % if r.get('dificuldade') == 'Fácil':
               <span style="color:green">🟢 Fácil</span>
           % elif r.get('dificuldade') == 'Médio':
               <span style="color:orange">🟡 Médio</span>
           % else:
               <span style="color:red">🔴 Difícil</span>
           % end
        </p>
        % if r.get('tipo') == 'pet':
            <p style="background: #ffe6e6; padding: 5px;">⚠️ {{r.get('aviso')}}</p>
        % end
    </li>
% end
</ul>