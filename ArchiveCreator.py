import shutil

# Prompt user for archive format and output path
archive_format = input('[+] Enter the Format (zip, tar, gztar, bztar, xztar): ')
output_path = input(f'[+] Enter the Path where the {archive_format} Should be Created: ')

# Lists to store file names and paths
file_names = []
path_names = []

while True:
    try:
        # Prompt user for file name and path
        file_name = input(f'[+] Enter the {archive_format} Name: ')
        file_names.append(file_name)

        path = input('[+] Enter the Path of the File: ')
        path_names.append(path)

        # Check if the user wants to create another archive
        create_another = input(f'[-] Do you want to create another {archive_format} (y/n): ')

        if create_another == 'n':
            print()
            print('[+] Thank you for using me! Goodbye!')
            break
        else:
            continue
    except Exception as ex:
        print('[-] Oops! Something went wrong:', ex)

iFile = 0
print()

try:
    for i in range(len(file_names)):
        # Create the archive
        shutil.make_archive(file_names[iFile], archive_format, path_names[iFile], output_path)

        print(f'{iFile+1}. {archive_format} was created!')
        iFile += 1
except Exception as ex:
    print('[-] Oops! Something went wrong! :(', ex)
