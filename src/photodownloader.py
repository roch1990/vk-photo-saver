import urlretriever
import urllib
import logging

class PhotoDownloader:
    
    
    def __init__(self):
        self.PHOTO_DICT = urlretriever.UrlRetriever().photo_list()
        print(self.PHOTO_DICT)
        self.DEFAULT_PATH = ''
        
    
    def folder_forming(self):
        for key in self.PHOTO_DICT:
            self.DEFAULT_PATH = os.path.join(str(os.path.realpath(os.path.dirname(sys.argv[0]))),
                                                 'out', key)
            logging.info("Path created: {}".format(self.DEFAULT_PATH))
            yield self.DEFAULT_PATH


    def photo_downloading(self):
        try:
            for key in self.PHOTO_DICT:
                print(key)
                path = self.DEFAULT_PATH
                counter = 0
                for item in self.PHOTO_DICT[key]:
                    photo = urllib.request.urlopen(self.PHOTO_DICT[key][item]).read()
                    output_file = open(path.join(self.PHOTO_DICT[key]),
                                       "wb")
                    output_file.write(photo)
                    output_file.close()
                    counter += 1
                    logging.info("Photo saved: {}".format(self.PHOTO_DICT[key][item]))
                return True
        except Exception as e:
            logging.exception("Error occured: {}".format(e))
            return False
