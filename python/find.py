#!/bin/python3
import argparse
from argparse import ArgumentParser, FileType, Namespace
from collections.abc import Callable, Iterable, Sequence
from enum import Enum
from fileex.search import Searcher

class emFileType(Enum):
    file        = 1
    directory   = 2,
    all         = 3,

def ToFileType(fileType: str):
    mapper = {
        "f" : emFileType.file,
        "d" : emFileType.directory}

    if len(fileType) == 0:
        return emFileType.all
    
    if fileType in mapper.keys():
        raise -1

    return mapper.get(fileType)

def Process(searchPath: str, fileName: str, fileType: str):
    if len(searchPath) <= 0:
        raise ValueError(str.format("bad search path:{}", searchPath))
    if len(fileName) <= 0:
        raise ValueError(str.format("bad filename:{}", fileName))
    
    search = Searcher

    match ToFileType(fileType):
        case emFileType.file:
            search.FindFile(searchPath, fileName)
        case emFileType.directory:
            search.FindFolder(searchPath, fileName)
        case emFileType.all:
            search.Find(searchPath, fileName)
        case _:
            raise ValueError(str.format("bad filetype:{}", fileType))
    pass

## 单参数赋值action
class SingleValueSetAction(argparse.Action):
    def __init__(self, option_strings: Sequence[str], dest, nargs=1, **kwargs):
        super().__init__(option_strings, dest, nargs, kwargs)
    
    def __call__(self, parser, namespace, values=Sequence[str], option_string=None):
        setattr(namespace, self.dest, values[0])
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="find(bbtools script)",
        description="可以过滤、特征查找、限定范围查找文件")
    

    parser.add_argument('-v', '--version',  action='version', version='%(prog)s v1.0', dest="version string.")
    ## 搜索的目标文件（支持正则）
    parser.add_argument('--name',           action=SingleValueSetAction, type=str, dest="name",             help="target file name. support regex")
    ## 搜索路径
    parser.add_argument('-s', '--search',   action=SingleValueSetAction, type=str, dest="searchpath",       help="target search path.")
    ## 目标文件类型
    parser.add_argument('--type',           action=SingleValueSetAction, type=str, dest="targetfiletype",   help="target file type.")

    args = parser.parse_args()
    Process(args.searchpath, args.name, args.targetfiletype)
    exit(0)
    pass