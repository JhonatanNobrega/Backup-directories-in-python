import os
from datetime import datetime
from colorama import Fore, Style

def searchFiles(base_path, search_by_date):
  search_by_date = datetime.strptime(search_by_date, '%Y-%m-%d').date()
  path_files_found = []
  if not os.path.isdir(base_path):
    print(Fore.RED + f"O diretório não existe: {base_path}" + Style.RESET_ALL)
    return path_files_found
  for dirpath, dirnames, filenames in os.walk(base_path):
    for filename in filenames:
      path_file = os.path.join(dirpath, filename)
      data_modification_timestamp = os.path.getmtime(path_file)
      data_modification = datetime.fromtimestamp(data_modification_timestamp).date()
      if data_modification >= search_by_date:
        path_files_found.append(path_file)
  return path_files_found
