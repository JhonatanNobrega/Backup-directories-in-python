import zipfile
import os

def createZip(path_files_found, base_path, path_zip_save):
  with zipfile.ZipFile(path_zip_save, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in path_files_found:
      path_relative = os.path.relpath(file, base_path)
      zipf.write(file, path_relative)
