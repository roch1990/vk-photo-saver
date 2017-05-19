# vk api config
API_TOKEN = ''
TOKEN_EP_IN = ''
CLIENT_ID = ''
REDIRECT_URI = 'https://oauth.vk.com/blank.html'
RESPONSE_TYPE = 'token'
REVOKE = '1'
SCOPE = 'photos'
V = '5.64'

USER_ID = ''
METHOD_GETALLPHOTOS = 'photos.getAll'
METHOD_GETALBUMS = 'photos.getAlbums'
METHOD_GETALBUMPHOTOS = 'photos.get'

# photo resolution configurating
PHOTO_RESOLUTION = ('photo_75',
                    'photo_130',
                    'photo_604')

OUTPUT_FOLDER = 'out'

DEFAULT_PATH = ''
DEFAULT_FORMAT = '.jpg'

# 0 - method name; 1 - parameters; 2 - token; 3 - version
method_name = 'https://api.vk.com/method/{0}?owner_id={1}{2}&access_token={3}&v={4}'
# 0 - application id; 1 - redirect uri; 2- scope; 3- response type; 4- revoke
token_string = 'https://oauth.vk.com/authorize?client_id={0}&redirect_uri={1}&scope={2}&response_type={3}&v={4}&revoke={5}'
