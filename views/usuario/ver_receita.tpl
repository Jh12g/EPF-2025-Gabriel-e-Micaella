% rebase('layout.tpl', title=receita['titulo'])

<div class="recipe-container">
    
    <a href="javascript:history.back()" class="btn-voltar">
        ⬅ Voltar ao cardápio
    </a>

    <div class="recipe-layout">
        
        <div class="recipe-image-col">
            <img src="{{receita.get('imagem')}}" alt="{{receita['titulo']}}">
        </div>

        <div class="recipe-content-col">
            
            <div class="recipe-meta-block" style="border-bottom: none; margin-bottom: 0; padding-bottom: 0;">
                <h1 class="recipe-title">{{receita['titulo']}}</h1>
                
                <div class="badge-group">
                    <span class="badge badge-blue">⏱ {{receita['tempo']}} min</span>
                    <span class="badge badge-orange">📊 {{receita.get('dificuldade', 'Normal')}}</span>
                    
                    % if receita.get('tipo') == 'pet':
                        <span class="badge badge-purple">🐶 Receita Pet</span>
                    % end
                </div>

                % if receita.get('tipo') == 'pet':
                    <div class="alert-pet">
                        ⚠️ <strong>Atenção:</strong> {{receita.get('aviso')}}
                    </div>
                % end
            </div>
            
        </div>
    </div> 
    <div class="recipe-section-card">
        <h3>🥕 Ingredientes</h3>
        <p class="recipe-text">{{receita['ingredientes']}}</p>
    </div>


    <div class="recipe-section-card">
        <h3>🔥 Modo de Preparo</h3>
        <p class="recipe-text">{{receita['preparo']}}</p>
    </div>


    <div class="comments-card">
        <h3 style="color: #b71c1c; margin-top: 0; margin-bottom: 25px;">💬 Avaliações da Comunidade</h3>

        <div>
            % if not comentarios:
                <div style="text-align: center; padding: 30px; background: #f9f9f9; border-radius: 10px; color: #777;">
                    <span style="font-size: 2rem;">📝</span><br>
                    Esta receita ainda não tem avaliações.<br>Seja o primeiro a comentar!
                </div>
            % else:
                % for c in comentarios:
                    <div class="comment-item">
                        <div class="comment-header">
                            <div style="display: flex; align-items: center; gap: 10px;">
                                <strong style="font-size: 1.1rem; color: #333;">{{c.get('nome_autor', 'Usuário')}}</strong>
                                
                                % if is_admin:
                                    <form action="/comentarios/delete/{{c['id']}}" method="POST" style="margin: 0; display: inline;">
                                        <button type="submit" class="btn-delete-comment" title="Apagar comentário" onclick="return confirm('Tem certeza que quer apagar este comentário?')">
                                            🗑️
                                        </button>
                                    </form>
                                % end
                            </div>

                            <div class="stars-active">
                                % nota = int(c.get('nota', 0))
                                % for i in range(nota):
                                    ★
                                % end
                                % for i in range(5 - nota):
                                    <span class="stars-inactive">★</span>
                                % end
                            </div>
                        </div>
                        <p style="margin: 0; color: #555; line-height: 1.5;">{{c['texto']}}</p>
                    </div>
                % end
            % end
        </div>

        <div class="comment-form-box">
            <h4 style="margin-top: 0; color: #b71c1c;">Gostou? Deixe sua opinião!</h4>
            
            <form action="/comentar" method="POST">
                <input type="hidden" name="receita_id" value="{{receita['id']}}">

                <div class="form-row">
                    <div class="form-col-small">
                        <label class="label-styled">Sua Nota:</label>
                        <select name="nota" required class="input-styled">
                            <option value="5">★★★★★ (Excelente)</option>
                            <option value="4">★★★★ (Muito bom)</option>
                            <option value="3">★★★ (Bom)</option>
                            <option value="2">★★ (Regular)</option>
                            <option value="1">★ (Ruim)</option>
                        </select>
                    </div>
                    
                    <div class="form-col-large">
                        <label class="label-styled">Seu Comentário:</label>
                        <textarea name="texto" required rows="1" class="input-styled" placeholder="O que você achou do sabor? Foi fácil fazer?"></textarea>
                    </div>
                </div>

                <button type="submit" class="btn-success" style="margin-top: 15px; width: auto; padding: 10px 30px;">Enviar Avaliação</button>
            </form>
        </div>
    </div>

</div>