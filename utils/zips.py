import shutil
import zipfile
import os

from utils import config


class ZIPS:
    def __init__(self):
        pass

    @staticmethod
    def _check_is_pixiv_zip(zip_name):
        try:
            if len(zip_name.split(' - ')) == 3:
                return True
        except IndexError:
            return False

    def zips(self, zip_list):
        zip_list = zip_list if not isinstance(zip_list, str) else [zip_list]
        print(zip_list)
        for _zip in zip_list:
            # print(_zip)
            # Check if zip is pixiv
            if not self._check_is_pixiv_zip(_zip):
                print(f'[-] {_zip} is not a pixiv zip file, skipped')
                continue
            print(f'[+] {_zip} is a pixiv zip file, extracting...')
            # Get pid
            pid = _zip.split(' - ')[1]
            # Extract zip
            try:
                zip_ref = zipfile.ZipFile(_zip, 'r')
                for names in zip_ref.namelist():
                    img_format = names.split('.')[-1]
                    img_index = self.get_true_image_index(names)
                    if img_index == -1:
                        print(f'[-] Something seems wrong. error 0x01')
                        break
                    # Compact new file name
                    new_img_name = f"{_zip.replace(pid, f'{pid} #{img_index}')[0:-4]}" + f".{img_format}"
                    # Create new file
                    """
                    use shutil create a new file, and copy the content from new_img_name to it
                    """
                    try:
                        if not os.path.exists(new_img_name):
                            with open(new_img_name, 'wb') as new_file:
                                shutil.copyfileobj(zip_ref.open(names), new_file)
                                # Success to unzip the zip, img_index is the index of the image
                            print(f'   [+] {os.path.basename(new_img_name)} is extracted successfully')
                        else:
                            print(f'   [-] {os.path.basename(new_img_name)} already exists, skipped')
                            break
                    except shutil.Error as error:
                        print(error)
                        continue
                # Close the zip
                zip_ref.close()
                # Try to delete the zip
                if config.DELETE_ORIGINAL_FILES is True:
                    # delete the zip
                    try:
                        zip_ref.close()
                        os.remove(_zip)
                        print(f'[+] {os.path.basename(_zip)} is deleted successfully')
                    except zipfile.error:
                        raise
                    except os.error:
                        raise
            except zipfile.BadZipFile:
                print(f'[-] {_zip} is not a zip file, skipped')
                continue

    @staticmethod
    def get_true_image_index(img):
        if img.endswith('jpg') or img.endswith('png'):
            img = img[0:-4]
        try:
            return int(img)
        except ValueError:
            return -1


if __name__ == '__main__':
    print(ZIPS.get_true_image_index('012.jpg'))
