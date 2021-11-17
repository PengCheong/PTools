import os.path
import sys
from utils import config
from utils import files
from utils import zips as z


if __name__ == '__main__':
    path = None

    config = config.Config()

    try:
        path = sys.argv[1]

        if (not os.path.isdir(path)) or (not os.path.exists(path)):
            print('[!] Path is invalid')
            exit(-1)

        if len(sys.argv) > 2:
            print(f"[-] Arguments error, more that 1 path given")
            exit(-1)
        else:
            print("*" * 50)
            if path in ["dl", "download"]:
                path = config.usr_downloads

    except IndexError:
        print(f"[-] No path given, use /download as default, continue? (y/n)")
        _input = input()
        if _input in ["y", "Y", "yes", "Yes", "YES"]:
            path = config.usr_downloads
        else:
            exit(-1)

    finally:
        zip_list = files.Files().get_zips(path)
        z.ZIPS().zips(zip_list)
