import os, re, shutil

src_path = r"C:\Users\jadta\Documents\Projects\file-sorter\test_images"
dest_path = r"C:\Users\jadta\Documents\Projects\file-sorter\dest_folder"
whatsapp_search_path = r"Dieser PC\S22 von Jad\Interner Speicher\Android\media\com.whatsapp\WhatsApp\Media"

def extract_year(file_name):
    whatsapp_regex = r"^(IMG)-[0-9]{8}-(WA)[0-9]{4}"
    if re.search(whatsapp_regex, file_name):
        return file_name[4:8]

def move_files(src_path, dest_path):
    for file in os.scandir(src_path):
        if file.is_file():
            file_name = os.path.basename(file)
            year_folder = dest_path + "\\" + extract_year(file_name)
            if not os.path.exists(year_folder):
                os.makedirs(year_folder)
            if not os.path.isfile(year_folder + "\\" + file_name):
                shutil.copy(file, year_folder)
            else:
                print(f"{file_name} exists in {year_folder}")

if __name__ == "__main__":
    move_files(src_path, dest_path)
    print(os.path.exists(whatsapp_search_path))