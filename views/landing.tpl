<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Receitas - Bem-vindo</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Round" rel="stylesheet">
    
    <style>
        /* --- ESTILOS FORÇADOS (AGORA VERMELHOS) --- */
        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: white;
            background-image:
                linear-gradient(90deg, rgba(255, 0, 0, 0.3) 50%, transparent 50%),
                linear-gradient(rgba(255, 0, 0, 0.3) 50%, transparent 50%);
            background-size: 50px 50px;
            display: flex; flex-direction: column; min-height: 100vh;
            align-items: center; justify-content: center;
        }

        a { text-decoration: none; transition: 0.3s; }

        .hero-container {
            background-color: rgba(255, 255, 255, 0.95);
            max-width: 700px; width: 90%; padding: 50px;
            border-radius: 25px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
            text-align: center; display: flex; flex-direction: column; align-items: center;
        }

        .hero-icon-bg {
            background: #e53935; /* VERMELHO */
            width: 90px; height: 90px;
            border-radius: 50% 50% 50% 15px;
            display: flex; align-items: center; justify-content: center;
            margin-bottom: 25px; color: white;
            box-shadow: 0 10px 25px rgba(229, 57, 53, 0.3); /* Sombra Vermelha */
        }

        .hero-title {
            font-size: 3.5rem;
            
            /* MUDE ISTO: de #1a2a6c (Azul) para #b71c1c (Vermelho Escuro) */
            color: #5e0404ff; 
            
            margin: 0;
            font-weight: 800;
            letter-spacing: -1px;
        }

        .hero-underline {
            width: 150px; height: 6px;
            background: #ffcdd2; /* VERMELHO CLARO */
            margin-top: -10px; margin-bottom: 20px; z-index: 0; border-radius: 10px;
        }

        .hero-text {
            font-size: 1.1rem; color: #555; margin-bottom: 40px; line-height: 1.6;
        }

        .hero-buttons { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }

        .btn-hero-primary {
            background: linear-gradient(90deg, #e53935, #d32f2f); /* GRADIENTE VERMELHO */
            color: white; padding: 15px 40px; border-radius: 50px;
            font-size: 1.1rem; font-weight: bold; display: flex; align-items: center; gap: 10px;
            box-shadow: 0 10px 25px rgba(211, 47, 47, 0.4);
        }
        .btn-hero-primary:hover { transform: translateY(-3px); }

        .btn-hero-secondary {
            background: white; color: #1a2a6c; padding: 15px 40px;
            border-radius: 50px; font-size: 1.1rem; font-weight: bold;
            display: flex; align-items: center; gap: 10px;
            border: 1px solid #e2e8f0; box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        }
        .btn-hero-secondary:hover { transform: translateY(-3px); border-color: #e53935; color: #e53935; }
    </style>
</head>
<body>

    <div class="hero-container">
        
        <div class="hero-icon-bg">
            <span class="material-icons-round" style="font-size: 40px;">restaurant_menu</span>
        </div>

        <h1 class="hero-title">Livro de Receitas</h1>
        <div class="hero-underline"></div>

        <p class="hero-text">
            Com tecnologia, aqui você consegue encontrar os melhores sabores para você e seu PET. 
            Sugira novos pratos e organize sua alimentação com facilidade e segurança!
        </p>

        <div class="hero-buttons">
            <a href="/login" class="btn-hero-primary">
                <span class="material-icons-round">login</span> Acessar Conta
            </a>
            <a href="/cadastro" class="btn-hero-secondary">
                <span class="material-icons-round">person_add</span> Criar Conta
            </a>
        </div>

    </div>

</body>
</html>