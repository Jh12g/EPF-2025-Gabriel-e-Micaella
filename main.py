from app import App

if __name__ == '__main__':
    print("Iniciando Servidor de Receitas...")
    
    #cria a aplicação
    minha_app = App().get_app()
    
    # roda o servidor
    # debug=True e reloader=True ajudam muito pq mostram erros na tela mas dps apago quando finalizar a fase teste
    minha_app.run(host='localhost', port=8080, debug=True, reloader=True)