import pathlib

class Searcher:
    def _FindFileByNameEx(self, searchPath: str, fileName: str) -> list[pathlib.Path]:
        fileList = []
        path = pathlib.Path(searchPath)
        if not path.exists():
            raise ValueError(str.format("searchPath:{} not exists.", searchPath))
        
        files = path.glob(str.format("**/{}", fileName))
        for file in files:
            if file.exists():
                fileList.append(file)

        return fileList

    def FindFolder(self, searchPath: str, folderName: str) -> list[pathlib.Path]:
        folderList = []
        files = self._FindFileByNameEx(searchPath, folderName)
        for file in files:
            if file.is_dir():
                folderList.append(file.absolute())

        return folderList

    def FindFile(self, searchPath: str, fileName: str) -> list[pathlib.Path]:
        fileList = []
        files = self._FindFileByNameEx(searchPath, fileName)
        for file in files:
            if file.is_file():
                fileList.append(file.ab)

        return fileList
    
    def Find(self, searchPath: str, fileName: str) -> list[pathlib.Path]:
        return self._FindFileByNameEx(searchPath, fileName)
