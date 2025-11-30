% rebase('layout.tpl', title=receita['titulo'])

<div class="container" style="max-width: 800px; margin-top: 30px;">
    
    <a href="javascript:history.back()" style="display: inline-block; margin-bottom: 20px; color: #555; font-weight: bold;">
        ⬅ Voltar
    </a>

    <div style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
        
        <div style="width: 100%; height: 300px; overflow: hidden;">
            <img src="{{receita.get('imagem')}}" alt="{{receita['titulo']}}" style="width: 100%; height: 100%; object-fit: cover;">
        </div>

        <div style="padding: 40px; text-align: left;">
            <h1 style="color: #1a2a6c; margin-top: 0;">{{receita['titulo']}}</h1>
            
            <div style="display: flex; gap: 10px; margin-bottom: 30px;">
                <span style="background: #e3f2fd; color: #1976d2; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; font-weight: bold;">
                    ⏱ {{receita['tempo']}} min
                </span>
                <span style="background: #fff3e0; color: #f57c00; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; font-weight: bold;">
                    📊 {{receita.get('dificuldade', 'Normal')}}
                </span>
                % if receita.get('tipo') == 'pet':
                    <span style="background: #f3e5f5; color: #7b1fa2; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; font-weight: bold;">
                        🐶 Pet
                    </span>
                % end
            </div>

            <h3 style="color: #3b82f6; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px;">🥕 Ingredientes</h3>
            <p style="white-space: pre-wrap; line-height: 1.8; color: #555;">{{receita['ingredientes']}}</p>

            <br>

            <h3 style="color: #3b82f6; border-bottom: 2px solid #f0f0f0; padding-bottom: 10px;">🔥 Modo de Preparo</h3>
            <p style="white-space: pre-wrap; line-height: 1.8; color: #555;">{{receita['preparo']}}</p>

            % if receita.get('tipo') == 'pet':
                <div style="margin-top: 30px; background: #ffebee; color: #c62828; padding: 15px; border-radius: 10px;">
                    ⚠️ <strong>Atenção:</strong> {{receita.get('aviso')}}
                </div>
            % end
        </div>
    </div>
</div>