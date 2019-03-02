import pprint
from SPOTIFY_KEYS import KEYS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

pp = pprint.PrettyPrinter()

CLIENT_ID = KEYS['CLIENT_ID']
CLIENT_SECRET = KEYS['CLIENT_SECRET']

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_uri(artist_name):
    results = spotify.search(q=artist_name, type='artist')
    uri = results['artists']['items'][0]['uri']
    return uri

def get_artist_top_tracks(artist_name):
    artist_uri = get_artist_uri(artist_name)
    results = spotify.artist_top_tracks(artist_uri)
    tracks = results['tracks']
    top_tracks_list = []
    for track in tracks:
        curr_track_info = {}
        curr_track_info['name'] = track['name']
        curr_track_info['uri'] = track['uri']
        top_tracks_list.append(curr_track_info)
    return top_tracks_list

artist_name = 'Taylor Swift'
pp.pprint(get_artist_top_tracks(artist_name))