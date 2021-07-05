import ntpath
from pathlib import Path
from pathlib import PureWindowsPath
from pprint import pprint
import requests

URL = 'https://cloud-api.yandex.net'
API_KEY = ''

class YandexDisk:
    def __init__(self, local_path):
        self.local_path = local_path

    def get_header(self, api_key=API_KEY):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {api_key}'
        }

    def path_cut(self):
        main_path = ((ntpath.splitdrive(self.local_path))[1]).replace('\\', '/')
        main_path = Path(main_path).parts

        dir_path = '/'.join(main_path[:-1]).replace('\\/','')
        full_path = '/'.join(main_path).replace('\\/','')
        file_name = main_path[-1]

        return full_path, file_name, dir_path

    # def get_files(self):
    #     files_url = f'{URL}/v1/disk/resources/files'
    #     headers = self.get_header()
    #     response = requests.get(files_url, headers=headers)
    #     response.raise_for_status()
    #     return pprint(response.json())

    def mk_dir(self):
        # ya_path = input('Такой папки нет. Введите название новой папки: ')
        # ya_path = Path(self.local_path).parts
        # print(ya_path)
        dir_url = f'{URL}/v1/disk/resources'
        headers = self.get_header()
        params = {'path': self.path_cut()[2], 'overwrite': 'true'}
        response = requests.put(dir_url, headers=headers, params=params)
        # response.raise_for_status()
        if response.status_code == 409:
            print(f'Путь {self.path_cut()[2]} уже существует.')
            self.ya_file_upload()
        elif response.status_code == 201:
            print(f'Директория {self.path_cut()[2]} успешно создана')
            self.ya_file_upload()
        elif response.status_code == 400:
            self.ya_file_upload()
        return response

    def get_upload_url(self, ya_path):
        ya_url = f'{URL}/v1/disk/resources/upload'
        headers = self.get_header()
        params = {'path': ya_path, 'overwrite': 'true'}
        response = requests.get(ya_url, headers=headers, params=params)
        return response.json()

    def ya_file_upload(self):
        # local_path_file = Path(self.local_path).parts
        # print(local_path_file)
        # upload_url = self.get_upload_url(ya_path=local_path_file[-1]).get('href')
        upload_url = self.get_upload_url(ya_path=self.path_cut()[0]).get('href')
        response = requests.put(upload_url, data=open(self.local_path, 'rb'))
        # response.raise_for_status()
        if response.status_code == 201:
            print(f'Файл записан на Яндекс Диск по пути {self.path_cut()[0]}')
        else: print('Что-то пошло не так')