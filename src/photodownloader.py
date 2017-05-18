import urlretriever
import urllib
import logging
import os
import config

class PhotoDownloader:
    
    
    def __init__(self):
        self.PHOTO_DICT = urlretriever.UrlRetriever().photo_list()
        self.DEFAULT_PATH = config.DEFAULT_PATH
        self.DEFAULT_FORMAT = config.DEFAULT_FORMAT


    def photo_downloading(self):
        print('Path to photo downloading:')
        print(self.DEFAULT_PATH)
        print('Start downloading')
        try:
            print('Downloading albums:')
            for key in self.PHOTO_DICT:
                counter = 0 
                print(key)
                for item in self.PHOTO_DICT[key]:
                    photo = urllib.request.urlopen(item).read()
                    output_file = open(os.path.join(self.DEFAULT_PATH, str(key) +
                                                    str(counter) + self.DEFAULT_FORMAT),
                                       "wb")
                    output_file.write(photo)
                    output_file.close()
                    counter += 1
                    logging.info("Photo saved: {}".format(item))
            print('Downoading succesfully complete!')
            return True
        except Exception as e:
            logging.exception("Error occured: {}".format(e))
            return False


    def __folder_forming(self, key):
        path = self.DEFAULT_PATH.join('join')
        
        return(path)