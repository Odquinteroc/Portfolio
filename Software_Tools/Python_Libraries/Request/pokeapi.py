import requests

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form/', offset = 0):
    args ={'offset': offset} if offset else{}

    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    response = requests.get(url, params=args)

    if response.status_code == 200: # the status of the server will be store in the argument status_code
        payload  =response.json()
        results = payload.get('results',[])
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
        next = input("continuar listando [Y/N]").lower()
        if next == 'y': 
            get_pokemons(offset= offset+20)

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemons()