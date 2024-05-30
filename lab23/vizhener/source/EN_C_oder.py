
from source.IOFILESTREEM import FileInstance
DEBUG = False


def coder(key : str, alpha : dict, resource_file : str, tocode_file : str):
    key = key.lower()
    file = FileInstance(
        path=resource_file
    )
    text = file.data()[0].lower() # take first string
    print(text)

    matrix = FileInstance(
            path='vizhener/files/code_matrix.txt'
        ).data()
    
    new_text = ''
    ind = 0
    for word in range(0, len(text)):
        if ind >= len(key): # move to begin
            ind = 0
        if text[word] != ' ':
            # append word from shiftmatrix
            new_text = new_text + matrix[
                                        alpha.get(key[ind]) # get shiftline
                                    ].split(' ')[ # clear spaces
                                            alpha.get(text[word]) # get shiftword
                                        ]
        else:
            new_text = new_text + ' '
        ind += 1

    FileInstance(path=tocode_file).write(new_text, endstr='', mode='w') # save to file

    print(new_text)
    

def encoder(key : str, lat : str, alpha : dict, resource_file : str, tocode_file):
    
    def origin(keyline : str, shiftwd : str):
        for wd in range(0, len(keyline)):
            if keyline[wd] == shiftwd:
                return lat[wd]
    
    key = key.lower()
    file = FileInstance(
        path=resource_file
    )
    text = file.data()[0].lower() # take first string
    print(text)

    matrix = FileInstance(
            path='vizhener/files/code_matrix.txt'
        ).data()
    
    new_text = ''
    ind = 0
    for word in range(0, len(text)):
        if ind >= len(key): # move to begin
            ind = 0
        if text[word] != ' ':
            # append word from shiftmatrix
            new_text = new_text + origin(
                keyline=matrix[alpha.get(key[ind])].split(' '), # get shiftline
                shiftwd=text[word]
            )
        else:
            new_text = new_text + ' '
        ind += 1

    FileInstance(path=tocode_file).write(new_text, endstr='', mode='w') # save to file

    print(new_text)
    
