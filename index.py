import requests
import streamlit as st

BASE_URL = 'https://api.github.com'

def selecionar_usuario(username):
    """
    Concatenando a constante com o nome do usuário, o parâmetro username será responsável pelo usuário.
    """
    url = f'{BASE_URL}/users/{username}'
    
    # Realizando a requisição com o HTTP GET
    response = requests.get(url)
    
    # Verificando se o retorno foi realizado com sucesso
    if response.status_code == 200:
        return response.json()
    else:
        return None

def ui():
    """
    Função responsável por exibir a interface do usuário.
    """
    # Utilizando o bootstrap
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)
    
    # Título
    st.title("Consulta Github")
    
    # Texto
    username = st.text_input("Insira o nome do Usuário:")
    
    # Verificando se o botão foi clicado
    if st.button("Buscar Usuário"):
        info_usuario = selecionar_usuario(username)
        # Verificando se o retorno não é nulo e exibindo as informações
        if info_usuario is not None:
            st.markdown(f'''
                        <div class="card" style="width: 18rem;">
                        <img class="card-img-top" src="{info_usuario['avatar_url']}" alt="Card Image cap">
                        <div class="card-body">
                        <h5 class="card-title">{info_usuario['name']}</h5>
                        <p class="card-text">{info_usuario['bio']}</p>
                        <a href="{info_usuario['html_url']}" style="color: white; text-decoration: none;" class="btn btn-primary"> Ver Perfil</a>
                        </div>
                        </div>
                        ''', unsafe_allow_html=True)

# Executando a função principal
ui()
