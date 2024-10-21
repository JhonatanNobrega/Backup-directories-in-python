from dotenv import load_dotenv
from helpers.subtractDaysFromCurrentDate import subtractDaysFromCurrentDate
from helpers.searchFiles import searchFiles
from helpers.createZip import createZip
import os
from colorama import Fore, Style

load_dotenv(override=True)

path_directories = os.getenv('PATH_DIRECTORIES')
days = os.getenv('LAST_DAYS')
pwd = os.getcwd()
path_zip = f"{pwd}/backups"
search_by_date = subtractDaysFromCurrentDate(int(days))
array_directories = path_directories.split(",")

try:
    backup_folder = f"{path_zip}/{search_by_date}"
    os.mkdir(backup_folder)
except FileExistsError:
    print(Fore.YELLOW + f'O diretório do backup já existe, atente que arquivos existentes serão substituidos!' + Style.RESET_ALL)

print(f"Procurando novos arquivos aparti de {search_by_date}")

for base_path in array_directories:
    path_files_found = searchFiles(base_path, search_by_date)
    folder = os.path.basename(base_path)
    if len(path_files_found) == 0:
        print(Fore.YELLOW + f"{folder} -> Não encontrado novos arquivos" + Style.RESET_ALL)
        continue
    path_zip_save = f"{path_zip}/{search_by_date}/{folder}.zip"
    createZip(path_files_found, base_path, path_zip_save)
    print(f"{folder} -> Realizado backup dos arquivos encontrados")