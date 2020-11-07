def Heads():
    import requests, base64, json, shutil
    from PIL import Image
    from io import BytesIO

    r = requests.get('https://api.minetools.eu/ping/breadmc.com/25565')

    #bread = json.loads(r.text)['favicon']
    players = json.loads(r.text)['players']['sample']

    #img = bread.split(',')[1]

    player_list = []
    for player in players:
            name = player["name"]
            uuid = player["id"]
            player_list.append(name)
    return player_list