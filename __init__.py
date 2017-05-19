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

    import config
    config.DEFAULT_PATH = os.path.join(main_path, 'out')
    print(config.DEFAULT_PATH)

    # Token url forming
    import urlretriever
    print('Your url to get token string:')
    print()
    print(urlretriever.UrlRetriever().token_string())
    print()
    print('''Please copy this url to your browser, get token, write it in config.py and then restart script!''')
    print()
    answer = input('Do you retrieve token ? Y/N\n')
    if (answer == 'Y'):
        import photodownloader
        print(photodownloader.PhotoDownloader().photo_downloading())
