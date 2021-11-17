import os


class Files:

    @staticmethod
    def _find_all_files(path):
        _files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                fn = os.path.join(root, file)
                if fn.endswith('.ini'):
                    continue
                _files.append(fn)
        return _files

    def _find_all_zips(self, path):
        files = self._find_all_files(path)
        zips = []
        for file in files:
            if file.endswith('.zip'):
                zips.append(file)
        return zips

    def get_files(self, path):
        return self._find_all_files(path)

    def get_zips(self, path):
        return self._find_all_zips(path)



