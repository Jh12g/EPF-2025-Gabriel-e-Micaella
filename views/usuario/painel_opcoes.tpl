% rebase('layout.tpl', title='Opções')

<div class="hero-section" style="padding: 40px; margin-top: 0; text-align: center;">
    <h2 class="hero-title" style="color: #6c1a1aff; margin-bottom: 10px;">Menu Principal</h2>
    <p class="hero-subtitle" style="color: #555; margin-bottom: 30px;">Escolha uma categoria abaixo.</p>

    <div style="display: flex; flex-direction: column; gap: 15px; width: 100%; max-width: 500px; margin: 0 auto;">
        
        <style>
            .botao-menu {
                display: flex; align-items: center; justify-content: space-between;
                background-color: white; padding: 15px 20px;
                border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
                text-decoration: none; color: #444; font-weight: 700; font-size: 1.1rem;
                transition: all 0.2s; border: 2px solid transparent;
            }
        
            .botao-menu:hover {
                transform: translateY(-3px);
                
                border-color: #e53935; 
                color: #e53935;
                
                /* MUDE AQUI (A sombra também, se quiser) */
                box-shadow: 0 8px 20px rgba(229, 57, 53, 0.2);
            }
            
            /* Bolinha colorida atrás do ícone */
            .icon-box {
                width: 40px; height: 40px; border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-size: 1.4rem; margin-right: 15px;
            }
        </style>

        <a href="/cafe" class="botao-menu">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #fff3e0; color: #e65100;">☕</span>
                Café da Manhã
            </div>
            <span style="color: #ddd;">➔</span>
        </a>

        <a href="/almoco" class="botao-menu">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #ffebee; color: #c62828;">🍛</span>
                Almoço
            </div>
            <span style="color: #ddd;">➔</span>
        </a>

        <a href="/janta" class="botao-menu">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #f3e5f5; color: #6a1b9a;">🍲</span>
                Jantar
            </div>
            <span style="color: #ddd;">➔</span>
        </a>

        <a href="/lanche" class="botao-menu">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #fff8e1; color: #fbc02d;">🥪</span>
                Lanche
            </div>
            <span style="color: #ddd;">➔</span>
        </a>

        <a href="/petisco" class="botao-menu">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #efebe9; color: #5d4037;">🍟</span>
                Petisco
            </div>
            <span style="color: #ddd;">➔</span>
        </a>

        <div style="height: 1px; background: #e0e0e0; margin: 5px 0;"></div>

        <a href="/cachorro" class="botao-menu" style="border-left: 5px solid #81d4fa;">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #e1f5fe; color: #0277bd;">🐶</span>
                Receitas para Cães
            </div>
            <span style="color: #ddd;">➔</span>
        </a>

        <a href="/gato" class="botao-menu" style="border-left: 5px solid #b39ddb;">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #ede7f6; color: #512da8;">🐱</span>
                Receitas para Gatos
            </div>
            <span style="color: #ddd;">➔</span>
        </a>

        <a href="/sugerir" class="botao-menu" style="background-color: #f1f8e9; border: 1px solid #c5e1a5;">
            <div style="display: flex; align-items: center;">
                <span class="icon-box" style="background: #dcedc8; color: #33691e;">💡</span>
                Sugerir Nova
            </div>
            <span style="color: #33691e;">➔</span>
        </a>

    </div>
</div>