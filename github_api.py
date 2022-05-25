import requests


def buscar_avatar(usuario):
    """
    busca o avatar de um usuario no GIthub

    :param usuario: str com o nome do usuario no github
    :return: str com o link do avatar
     """
    url = f'https://api.github.com/users/{usuario}'
    answer = requests.get(url)
    return answer.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('vagner'))

