
from IOFILESTREEM import FilesBuffer

def IOFILE(file : str, action : str, data = [], dir = './'):
    buff = FilesBuffer(dir) # init

    if action == 'w':
        buff.file(file).write(data=data, mode='w')
        return None 
    elif action == 'r':
        return buff.file(file).data()

