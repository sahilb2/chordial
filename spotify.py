import requests
import urllib
import base64
import json
from flask import request
from auth import CLIENT_ID, CLIENT_SECRET


PORT = 5000
SCOPE = "user-library-read"
CLIENT_SIDE_URI = "http://127.0.0.1"
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URI, PORT)

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)



def app_Auth():
    auth_query_params = {
        "response_type" : "code",
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "scope" : SCOPE
    }
    url_args = "&".join(["{}={}".format(key,urllib.quote(val)) for key,val in auth_query_params.iteritems()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return auth_url

def user_Auth():
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))


    hard_code = "ZTM5NDk0NzQxOGUxNDFkNGIwNTM2MDgzZDc4ZjhlZDY6MzI3NTNiMzNhNzY4NDgyMDkzNzA4YjYwMjQ3ZGM1YWY"
    headers = {"Authorization": "Basic {}".format(base64encoded)}

    print(headers)
    # print("000000000000000000000000000000000000000000000000000000000000000000000000")
    #
    # print(code_payload)
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    response_data = json.loads(post_request.text)
    print(response_data)
    access_token = response_data["access_token"]
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}
    return authorization_header

def Profile_Data(header):
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=header)
    profile_data = json.loads(profile_response.text)
    return profile_data
