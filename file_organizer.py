#This script copies all file in a directory, sorts them by Month_Year of creation
#and stores them in the correspondig folder with the name Month_Year
import os
import shutil
import datetime
import time

def get_path():
    """Gets a path from the user"""
    while True:
        print('Please, enter the link down below.')
        location = input('Link -- ')
        if os.path.isdir(location):
            print('Location accepted!\n')
            return location
        else:
            print('Incorrect location. Please, recheck your link. Try again.')

def get_file_path(file, destination):
    """Gets the month and year when a file was created and returns a path
    in the form Month_Year, where the files should be stored"""
    os.chdir(destination)
    timestamp = os.path.getmtime(file)
    file_creation_date = time.ctime(timestamp).split() # Converts the timestamp(s) into a string with the full date
    folder_name = file_creation_date[1] + '_' + file_creation_date[4] # file_creation_date[1] -> corresponds to the Month; file_creation_date[4] -> corresponds to the year
    new_folder_name = os.path.join(destination,folder_name)
    return new_folder_name

def copy_file(file, new_folder_name):
    """Copies a file to a new location"""
    try:
        new_file_path = shutil.copy2(file, new_folder_name)
        return new_file_path
    except FileNotFoundError:
        return
    
def main():
    print('I will organize your files by Month_Year')

    print('Where are your files located?')
    location = get_path() # Path where the files are located

    print('Where would you like your new sorted files be placed?')
    destination = get_path() # Path where the files are to be stored

    #Go to the location of the files
    os.chdir(location)
    list_files = os.listdir(location)
    count = 0
    print('You have {} files in the folder {}'.format(len(list_files), location))
    print('Copying...')
    for directory, subdir, files in os.walk(location):
        for file_ in files:
            if file_.startswith('._'):
                continue
            file_full_path = os.path.join(directory, file_)
            #file_full_path is the complete path of the location to the file itself
            new_folder_name = get_file_path(file_full_path, destination) # The function returns the new path to the copy of file

            # Check if the Month_Year directory already exists, if it does skip over to the next step
            directory_exists = os.path.isdir(new_folder_name)
            if not directory_exists:
                os.mkdir(new_folder_name)
                print('Folder created: {}'.format(new_folder_name))        
            
            # Copy the file to the new Month_Year folder
            new_file_location = copy_file(file_full_path, new_folder_name)
            if new_file_location is None:
                print('File {} not found'.format(file_))
                continue
            else:
                count += 1
    
    print('Finished!')
    print('{} of {} files copied.'.format(count, len(list_files)))

if __name__ == '__main__':
    main()
