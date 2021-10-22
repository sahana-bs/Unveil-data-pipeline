'''
inputs and other pointers:
https://docs.google.com/document/d/1KskoglMEV6W42ZVilPHjwY-cdPREtrF5Aocdd5AnAe4/edit?usp=sharing
'''
#importing facebook-sdk
#import facebook as fb
import json
import urllib.request
'''
user access token
TODO: needs to be generated for every user
class, functions,..

#https://developers.facebook.com/docs/facebook-login/access-tokens

This is a rough demo
'''
def get_fb_data(access_token):

    graph_url="https://graph.facebook.com/v12.0/me?fields=id%2Cname&access_token="+access_token

    try:
        response = urllib.request.urlopen(graph_url)
        response_py = json.loads(response.read())    #is read necessary??
        #print(response_py)
        '''
        furthur processing with response_py
        '''
        return response_py



    except URLError:
        print("Access token error##")
        print(error)

access_token="EAAFq61iIUZCQBAOZArfjWln9iTDiUkZAxLzsC2fhwVRMDHHvYcTOalADQF1C3IYGsL8plt7GN50VDAJVSaJpyxtPldedZAmvfRiMq610ks8j7RIj0EgoTmj8yT8jAbhIP1Q0SUparQoFZBhxjstm1umyadOlVeqkOXjKwDKqitez0obxf29G5"
print(get_fb_data(access_token))


'''
output:
{'id': '4547123585403120', 'name': 'Sahana Srinivas'}
'''
