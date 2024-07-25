'''
Copyright [2024] [Ryan Stanley Feinberg]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import os
import re

class ScraperUtil:
    def __init__(self) -> None:
        pass

    def read_files(self, directory: str, file_type: str = '.*') -> 'list[str]':
        """ Reads in the data line by line for each file name given in the given directory path. 
        ### Args
            - directory: The path to the directory to read in file data.
            - list_of_filenames: The list of files by name you want to read into the return list.
        ### Returns
            - data_list: A list of data (as string lines) from each line in each file read in.
        """
        list_of_filenames = self._get_filenames(directory, file_type)
        data_list = []
        for file_name in list_of_filenames:
            with open(directory+'/'+file_name, 'r') as file:
                data = file.readlines()
                data_list.extend(data)
        return data_list

    def _get_filenames(self, directory: str, file_type: str = '.*') -> 'list[str]':
        """ Gets name of each keywords file in keywords directory.
        ### Args:
            - directory: The path to the directory you would like the file names of.
            - file_type: Returns the names of file only with the given extension. (default = all files)  

        ### Returns:
            - List of file names from the directory specified.
        """
        pattern = re.compile(f'{file_type}$')
        return [file for file in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, file)) and pattern.search(file)]

