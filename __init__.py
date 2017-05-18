import sys
import os
import logging


def path_to(main_path, *args):
    for name in args:
        sys.path.append(os.path.join(name))
    return True


if __name__ == '__main__':
    logging.basicConfig(filename="vksaver.log",
                        format="%(asctime)-15s %(msg)s")
    logging.info("App started")
    main_path = (str(os.path.realpath(os.path.dirname(sys.argv[0]))))
    logging.info("App path:\n {}".format(main_path))
    path_to(main_path,
            'src',
            'out',
            )
    
    
    import photodownloader
    print(photodownloader.PhotoDownloader().photo_downloading())
    