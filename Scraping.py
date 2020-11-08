def Heads():
    import requests, json, shutil
    from PIL import Image
    from io import BytesIO

    r = requests.get('https://api.minetools.eu/ping/breadmc.com/25565')

    players = json.loads(r.text)['players']['sample']

    player_list = []
    for player in players:
            name = player["name"]
            uuid = player["id"]
            player_list.append(name)
    return player_list