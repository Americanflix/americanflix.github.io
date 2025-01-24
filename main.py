import os
import json
import requests
import xbmc

GITHUB_REPO_API = "https://api.github.com/repos/americanflix/americanflix.github.io/contents/movies"

def download_movies():
    local_movies_dir = os.path.join(os.path.dirname(__file__), 'movies')
    
    # Certifique-se de que o diretório local existe
    if not os.path.exists(local_movies_dir):
        os.makedirs(local_movies_dir)

    # Obter a lista de arquivos do repositório remoto
    response = requests.get(GITHUB_REPO_API)
    
    if response.status_code == 200:
        files = response.json()
        for file in files:
            # Verifique se o arquivo é do tipo JSON
            if file['name'].endswith('.json'):
                file_url = file['download_url']  # URL para baixar o arquivo diretamente
                filename = file['name']
                download_file(file_url, os.path.join(local_movies_dir, filename))
    else:
        xbmc.log(f"Erro ao acessar a API do GitHub: {response.status_code}", level=xbmc.LOGERROR)

def download_file(url, local_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'w') as f:
            f.write(response.text)
    else:
        xbmc.log(f"Erro ao baixar {local_path}: {response.status_code}", level=xbmc.LOGERROR)

def load_movies():
    download_movies()  # Certifique-se que os arquivos estão baixados
    local_movies_dir = os.path.join(os.path.dirname(__file__), 'movies')
    all_movies = []

    # Verifica se o diretório existe
    if not os.path.exists(local_movies_dir):
        xbmc.log("Diretório de movies não encontrado!", level=xbmc.LOGERROR)
        return all_movies

    # Percorre os arquivos na pasta de filmes
    for filename in os.listdir(local_movies_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(local_movies_dir, filename)
            with open(file_path, 'r') as f:
                try:
                    movie_data = json.load(f)
                    all_movies.extend(movie_data.get('movies', []))  # Adiciona filmes da chave 'movies'
                except json.JSONDecodeError:
                    xbmc.log(f"Erro ao decodificar o arquivo {filename}", level=xbmc.LOGERROR)

    return all_movies

# Exemplo de uso
movies = load_movies()
for movie in movies:
    xbmc.log(f"Filme: {movie.get('title', 'Título não disponível')}, URL: {movie.get('url', 'URL não disponível')}", level=xbmc.LOGINFO)
