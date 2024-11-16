import requests

# defining base url and api host and key

baseurl= "https://spotify23.p.rapidapi.com/"
headers= {
    'x-rapidapi-host': 'spotify23.p.rapidapi.com',
    'x-rapidapi-key': 'cc6ab9ac7fmshad9a4dc9a1cdd26p1355f0jsncb183ad94797'
}

# function 1 "Artist Overview"

def getartistid(artist_name):
    url_id= f"{baseurl}search/?q={artist_name}&type=artist&limit=1"
    response_id= requests.get(url_id, headers=headers)
    data= response_id.json()
    ids= data['artists']['items'][0]['data']['uri']
    idsclean = ids.split("spotify:artist:")[1]

    url_artist = f"{baseurl}artists/?ids={idsclean}"
    response_artist = requests.get(url_artist, headers=headers)

    url_artist2 = f"{baseurl}artist_overview/?id={idsclean}"
    response_artist2 = requests.get(url_artist2, headers=headers)
    
    if response_artist.status_code==200:
        data = response_artist.json()
        print("")
        print(f"Name: {data['artists'][0]['name']}")
        print("Genres: ", end="")
        for i in range(len(data['artists'][0]['genres'])):
            if (i+1)==len(data['artists'][0]['genres']):
                print(f"{data['artists'][0]['genres'][i]}")
            else:
                print(f"{data['artists'][0]['genres'][i]}, ", end="")
        print(f"Artist photo: {data['artists'][0]['images'][0]['url']}")
    else:
        print("error", response_artist.status_code)

    if response_artist2.status_code==200:
        data2 = response_artist2.json()
        print(f"Followers: {data2['data']['artist']['stats']['followers']}")
        print(f"Monthly Listeners: {data2['data']['artist']['stats']['monthlyListeners']}")
        print(f"Verified: {data2['data']['artist']['profile']['verified']}")
        print(f"Latest Release: {data2['data']['artist']['discography']['latest']['name']}, {data2['data']['artist']['discography']['latest']['type']}")
        print(f"Total Single: {data2['data']['artist']['discography']['singles']['totalCount']}")
        print(f"Total Albums: {data2['data']['artist']['discography']['albums']['totalCount']}")
        for i in range(len(data2['data']['artist']['profile']['externalLinks']['items'])):
            print(f"{data2['data']['artist']['profile']['externalLinks']['items'][i]['name']}: {data2['data']['artist']['profile']['externalLinks']['items'][i]['url']}")
    else:
        print("error", response_artist.status_code)

# function 2 "Album Overview"

def getalbumid(album_name):
    url_id2 = f"{baseurl}search/?q={album_name}&type=album&limit=1"
    response_id2 = requests.get(url_id2, headers=headers)
    data2= response_id2.json()
    ids2= data2['albums']['items'][0]['data']['uri']
    ids2cleaned = ids2.split("spotify:album:")[1]
    
    url_album = f"{baseurl}albums/?ids={ids2cleaned}"
    response_album = requests.get(url_album, headers=headers)

    if response_album.status_code == 200:
        data_album = response_album.json()
        print("")
        print(f"Album name: {data_album['albums'][0]['name']}")
        print(f"Artist name: {data_album['albums'][0]['artists'][0]['name']}")
        print(f"Label: {data_album['albums'][0]['label']}")
        print(f"Album cover: {data_album['albums'][0]['images'][0]['url']}")
        print(f"Release date: {data_album['albums'][0]['release_date']}")
        duration= []
        for i in range(len(data_album['albums'][0]['tracks']['items'])):
            duration += [data_album['albums'][0]['tracks']['items'][i]['duration_ms']]
        print(f"Duration: {int(sum(duration)/3600000)} h {int(((sum(duration)/3600000)%1)*60)} m {int(((((sum(duration)/3600000)%1)*60)%1)*60)} s")
        print("Tracks: ", end="")
        for i in range(len(data_album['albums'][0]['tracks']['items'])):
            if i == 0:
                print(f"{data_album['albums'][0]['tracks']['items'][i]['name']}")
            else:
                print(f"        {data_album['albums'][0]['tracks']['items'][i]['name']}")
    else:
        print("error", response_album.status_code)

# function 3 "Track Overview"

def gettrackid(track_name):
    url_id3 = f"{baseurl}search/?q={track_name}&type=track&limit=1"
    response3 = requests.get(url_id3, headers=headers)
    data3= response3.json()
    ids3= data3['topResults']['items'][0]['data']['uri']
    ids3cleaned = ids3.split("spotify:track:")[1]

    url_track = f"{baseurl}tracks/?ids={ids3cleaned}"
    response_track = requests.get(url_track, headers=headers)

    if response_track.status_code ==200:
        data_track = response_track.json()
        print("")
        print(f"Track name: {data_track['tracks'][0]['name']}")
        print("Artists: ", end="")
        for i in range(len(data_track['tracks'][0]['artists'])):
            if (i+1)==len(data_track['tracks'][0]['artists']):
                print(f"{data_track['tracks'][0]['artists'][i]['name']}")
            else:
                print(f"{data_track['tracks'][0]['artists'][i]['name']}, ", end="")
        print(f"Album name: {data_track['tracks'][0]['album']['name']}")
        print(f"Track cover: {data3['topResults']['items'][0]['data']['albumOfTrack']['coverArt']['sources'][0]['url']}")
        print(f"Duration: {int(data_track['tracks'][0]['duration_ms'])//60000} m {int(((float(data_track['tracks'][0]['duration_ms'])/60000)%1)*60)} s")
        print(f"Explicitness: {data_track['tracks'][0]['explicit']}")

# function 4 "Track Lyrics"

def getlyricsid(track_name2):
    url_id4 = f"{baseurl}search/?q={track_name2}&type=track&limit=1"
    response4 = requests.get(url_id4, headers=headers)
    data4= response4.json()
    ids4= data4['topResults']['items'][0]['data']['uri']
    ids4cleaned = ids4.split("spotify:track:")[1]

    url_track_lyric = f"{baseurl}track_lyrics/?id={ids4cleaned}"
    response_track_lyric = requests.get(url_track_lyric, headers=headers)

    if response_track_lyric.status_code==200:
        data_lyric= response_track_lyric.json()
        print("")
        print('LYRICS')
        for i in range(len(data_lyric['lyrics']['lines'])):
            print(data_lyric['lyrics']['lines'][i]['words'])
    else:
        print("error", response_track_lyric.status_code)

# function 5 "Track Recommendation"

def getrecommendation(track_name3):
    url_id5 = f"{baseurl}search/?q={track_name3}&type=track&limit=1"
    response5 = requests.get(url_id5, headers=headers)
    data5= response5.json()
    ids5= data5['topResults']['items'][0]['data']['uri']
    ids5cleaned = ids5.split("spotify:track:")[1]
    
    url_recommendation = f"{baseurl}recommendations/?limit=20&seed_tracks={ids5cleaned}"
    response_recommendation = requests.get(url_recommendation, headers=headers)

    if response_recommendation.status_code==200:
        datarecommendation= response_recommendation.json()
        print("")
        print("TRACK RECOMMENDATION")
        for i in range(len(datarecommendation['tracks'])):
            print(f"{datarecommendation['tracks'][i]['name']} by ", end="")
            for y in range(len(datarecommendation['tracks'][i]['artists'])):
                if (y+1)==len(datarecommendation['tracks'][i]['artists']):
                    print(f"{datarecommendation['tracks'][i]['artists'][y]['name']}")
                else:
                    print(f"{datarecommendation['tracks'][i]['artists'][y]['name']}, ", end="")

# choose menu

while True:
    print("")
    print("1. Artist Overview")
    print("2. Album Overview")
    print("3. Track Overview")
    print("4. Track Lyrics")
    print("5. Track Recommendation")

    user_input= input("Choose 1-5: ")
    if user_input=='1':
        artist= input("input artist name: ")
        getartistid(artist)
    elif user_input=='2':
        album= input("input album name: ")
        getalbumid(album)
    elif user_input=='3':
        track= input("input track name: ")
        gettrackid(track)
    elif user_input=='4':
        lyric= input("input track name: ")
        getlyricsid(lyric)
    elif user_input=='5':
        recommendation= input("input track name: ")
        getrecommendation(recommendation)
    else:
        print("enter 1-5")
