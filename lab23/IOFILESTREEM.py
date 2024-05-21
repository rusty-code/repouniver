
class File:
    def __init__(
            self, 
            # directory : str, # not use, append in
            path : str, 
            mode = 'r'
        ):

        self._PATH = path
        self._mode = mode

        self._file_data = [] # ['strings']
        self.read_file()

        # for genenrator interface
        self._curr_ = 0


    def __str__(self) -> str:
        return ''.join(str(ind) for ind in self.read_buffer())

    # setters 
    def set_mode(self, new_mode : str):
        self._mode = new_mode

    # getters
    def get_path(self):
        return self._PATH
    
    def get_mode(self):
        return self._mode

    def get_buffer(self):
        return self._file_data

    def write_file(self, data : list):
        try:
            with open(self._PATH, 'a') as file:
                    file.write(f'{data}')
            for string in data:
                self._file_data.append(string)

        except FileNotFoundError:
            print(f"(ERROR) no such of file: '{self._PATH}'")

    def read_file(self, mode = 'r'):
        try:
            with open(self._PATH, 'r') as file:
                for string in file:
                    self._file_data.append(string)
        except FileNotFoundError:
            print(f"(ERROR) no such of file: '{self._PATH}'")

    def read_buffer(self):
        for string in self._file_data:
            yield string

    def delete(self):
        pass    


class FileBuffer:
    """Worker with many files
        Accepts a collection relative file paths"""

    def __init__(
            self, 
            directory : str, # not use, append in
            paths : list | None = [], 
            mode : str | None = 'r'
        ):

        self._paths = paths
        self._mode = mode

        self._files_data = {} # dict {'path' : ['strings']}
        if paths != []:
            self.set_paths(paths)

    # system
    def __is_path_in_paths(self, path : str) -> bool:
        if path in self._paths:
            return True
        return False

    # setters 
    def set_mode(self, new_mode : str):
        self._mode = new_mode

    def set_paths(self, paths : list):
        for path in paths:
            self._paths.append(path)

        for filepath in paths: 
            with open(filepath, 'r') as file:
                strings = [] # file data

                for string in file:
                    strings.append(string)

                self._files_data[filepath] = strings # make pair

    # getters
    def get_paths(self):
        return self._paths
    
    def get_mode(self):
        return self._mode

    def write_file(self, data, path : str):
        try:
            self._paths.append(path)
            with open(path, 'a') as file:
                    file.write(f'{data}')
            self._files_data[path].append(f"{data}")

        except FileNotFoundError:
            print(f"(ERROR) no such of file: '{path}'")

    """generator"""
    def read_files_generator(self, paths : str):
        if paths == '*': # write all files from buffer
            for path in self._paths:
                for string in self._files_data[path]:
                    yield string
        else:
            for path in paths:
                if self.__is_path_in_paths():
                    for string in self._files_data[path]:
                        yield string
                else:
                    print(f"(ERROR) no such of file: '{path}'")
        
    