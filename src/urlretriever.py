# external python library
import requests
import json
import logging
# internal application library
import config


class UrlRetriever:

    def __init__(self):
        '''Class constructor. No comments.'''
        self.API_TOKEN = config.API_TOKEN
        self.CLIENT_ID = config.CLIENT_ID
        self.REDIRECT_URI = config.REDIRECT_URI
        self.RESPONSE_TYPE = config.RESPONSE_TYPE
        self.REVOKE = config.REVOKE
        self.SCOPE = config.SCOPE
        self.V = config.V
        self.USER_ID = config.USER_ID
        self.METHOD_GET = config.METHOD_GETALBUMS
        self.PHOTO_RESOLUTION = config.PHOTO_RESOLUTION
        self.METHOD_NAME = config.method_name
        self.PARAMS = ''
        self.ALBUM_DICT = {}
        self.PHOTO_DICT = {}
        self.TOKEN_STRING = config.token_string

    def token_string(self):
        self.TOKEN_STRING = self.TOKEN_STRING.format(self.CLIENT_ID,
                                                     self.REDIRECT_URI,
                                                     self.SCOPE,
                                                     self.RESPONSE_TYPE,
                                                     self.V,
                                                     self.REVOKE)
        return self.TOKEN_STRING

    def albums_list(self):
        '''Bad code :('''
        try:
            json_data = self.__get_album_request()
            counter = 0
            self.METHOD_GET = config.METHOD_GETALBUMS
            while counter < int(json_data['response']['count']):
                self.ALBUM_DICT[
                    json_data['response']['items'][counter]['id']] =
                json_data['response']['items'][counter]['title']
                counter += 1
            logging.info("Album formed: {}".format(self.ALBUM_DICT))
            print('Album list retrieving - done')
            return self.ALBUM_DICT
        except Exception as e:
            logging.critical("Error occured: {}".format(e))
            return self.ALBUM_DICT

    def photo_list(self):
        '''Don't do like this'''
        counter = 0
        number = 0
        number_of_photos = 0
        key = ''
        photo_json = {}
        photo_list = []
        self.ALBUM_DICT = self.albums_list()
        print('Retrieving of photo list in progress')
        try:
            for item in (self.ALBUM_DICT):
                # filling photo_json list from album
                photo_list = []
                number = 0
                photo_json = self.__vk_api_photo_json(item)
                try:
                    number_of_photos = int(photo_json['response']['count'])
                except Exception as e:
                    print(photo_json['error'])
                    print('\n\nPlease try again later!')
                while number < number_of_photos:
                    for key in photo_json['response']['items'][number]:
                        if key in self.PHOTO_RESOLUTION:
                            photo_list.append(
                                photo_json['response']['items'][number][key])
                    number += 1
                self.PHOTO_DICT[self.ALBUM_DICT[item]] = photo_list
                logging.info("Item:".format(
                    self.PHOTO_DICT[self.ALBUM_DICT[item]]))
            print('Photo list retrieving - done')
            return self.PHOTO_DICT
        except Exception as e:
            logging.critical("Error occured: {}".format(e))
            return self.PHOTO_DICT

    # private methods
    def __request_get(func):
        '''requests.get - no comments'''
        def wrapped(*args):
            get_querry = requests.get(func(*args))
            if get_querry.status_code != 200:
                logging.waarning(
                    "Error, status code: {}".format(get_querry.status_code))
                return False
            return requests.get(func(*args))
        return wrapped

    def __request_text(func):
        '''Returning text from requests.get'''
        def wrapped(*args):
            return func(*args).json()
        return wrapped

    def __json_pretty(func):
        '''Pretty JSON formating'''
        def wrapped(*args):
            return json.dumps(func(*args), indent=4, sort_keys=True)
        return wrapped

    # @__json_pretty
    @__request_text
    @__request_get
    def __get_album_request(self):
        '''Forming api request'''
        method_to_call = ((self.METHOD_NAME).format(self.METHOD_GET,
                                                    self.USER_ID,
                                                    self.PARAMS,
                                                    self.API_TOKEN,
                                                    self.V))
        return method_to_call

    def __vk_api_photo_json(self, album_id):
        '''Forming pretty JSON with photo list'''
        self.PARAMS = '&album_id='+str(album_id)
        self.METHOD_GET = config.METHOD_GETALBUMPHOTOS
        photo_json = self.__get_album_request()
        return photo_json
