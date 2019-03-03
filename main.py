from flask import Flask, redirect, jsonify
from spotify import app_Auth, user_Auth, Profile_Data, Playlists_Data, Playlist_Data
app = Flask(__name__)


@app.route('/')
def hello_world():
    print('hello world')
    auth_url = app_Auth()
    print(auth_url)
    return redirect(auth_url)


@app.route("/callback/q")
def callback():
    print("Authorized")
    auth_header = user_Auth()
    print(auth_header)
    profile_data = get_profile(auth_header)
    #print(profile_data)
    playlists= get_playlists(auth_header)
    #print(playlist)

    #return str(profile_data)
    good_list = []
    for playlist in playlists:
        good_list.append([playlist["id"], playlist["name"], playlist["external_urls"]])
    id = good_list[0][0]
    #return jsonify(id)
    playlist = get_playlist(auth_header, id)
    return jsonify(playlist)

def get_profile(auth_header):
    profile_data = Profile_Data(auth_header)
    return profile_data

def get_playlists(auth_header):
    playlists_data = Playlists_Data(auth_header)
    return playlists_data

def get_playlist(auth_header, id):
    playlist_data = Playlist_Data(auth_header, id)
    return playlist_data

if __name__ == '__main__':
    app.run()
