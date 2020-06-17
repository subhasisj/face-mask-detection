# import sys
# sys.path.append('../')
import os
import shutil

class FileUtils:
    def __init__(self,base_path_for_files):
        # self._logger = logger
        self._base_path_for_files = base_path_for_files

    def create(self,sub_directory_to_create,delete_before_creation=None):
        try:
            if delete_before_creation:
                self.delete_directory(sub_directory_to_create)
            path = os.path.join(self._base_path_for_files,sub_directory_to_create)
            if not os.path.isdir(path):
                os.makedirs(path)
                print(f'New Path Created {path}')
            else:
                print(f'Requested Path {path} already exists!')
            return path
        except OSError as ex:
            print(f'File Error while trying to create {sub_directory_to_create} under {self._base_path_for_files}','critical')

    def move_file(self,filename, destination_directory):
        try:
            if filename != '.gitignore':
                source_file_path = filename #os.path.join(self._base_path_for_files,filename)
                destination_file_path = destination_directory#os.path.join(destination_directory,filename)
                if os.path.isfile(source_file_path):
                    shutil.copy(source_file_path, destination_file_path)
                    print(f'File {filename} successfully moved from {source_file_path} to {destination_file_path}')
                else:
                    print(f'{filename} is not a file. Move operation failed from {source_file_path} to {destination_file_path}','warning')

        except :
            print(f'File {filename} move from {source_file_path} to {destination_file_path} Failed','critical')
            raise OSError

    def move_all_files(self,source_directory,destination_directory):
        for file in os.listdir(source_directory):
            self.move_file(file,destination_directory)
    