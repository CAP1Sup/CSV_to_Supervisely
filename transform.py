# Christian Piper
# 12/1/19
# This program will prompt the user for the beginning and end directories, then convert from a .csv format to a Supervisely format

import os
import shutil

def main():
    print("")
    input_path = getPath("Enter the full path to the directory of your input data: ")
    output_path = getPath("Enter the full path to the directory of your output data: ")
    name = "test_export"


    createFolderStructure(input_path, output_path, name)

def getPath(prompt):
    input_path = input(prompt)
    
    if os.path.exists(input_path):
        return input_path
    
    else:
        AttributeError

def createFolderStructure(input_path, output_path, project_name):

    # Check to see if output directory exists, otherwise error
    if os.path.exists(output_path):
        os.chdir(output_path)

    else:
        AttributeError
    
    # Create the project name folder and move into it
    try:
        os.mkdir(project_name)
        os.chdir(project_name)
    except:
        print("Project directory already exists!")
    

    # Create the dataset folder and move into it
    os.mkdir('main_dataset')
    os.chdir('main_dataset')

    # Create the folders for annotations and images
    os.mkdir('ann')
    os.mkdir('img')

    # Get all the image names in the input images directory
    input_train_names = [f for f in os.listdir(input_path + '\\train') if os.path.isfile(os.path.join(input_path + '\\train', f))]

    input_test_names = [f for f in os.listdir(input_path + '\\test') if os.path.isfile(os.path.join(input_path + '\\test', f))]

    input_image_names = input_train_names + input_test_names

    for entry in input_image_names:
        filename, file_extension = os.path.splitext(entry)
        # TODO: convert the files to the standarized format
        if file_extension == ".jpeg":
            input_image_names.append(entry)

        elif file_extension == "jpg":
            input_image_names.append(entry)
            
    notAvaiableCount = 0

    # Copy each image over to the output images folder
    for entry in input_train_names:
        filename, file_extension = os.path.splitext(entry)
        if file_extension == ".jpeg" or file_extension == ".JPG" or file_extension == ".png":
            shutil.copy(input_path + "\\train\\" + entry, output_path + "\\" + project_name + "\\main_dataset\\img")
            print("Copied: " + entry)
        else:
            notAvaiableCount =+ 1            

    # Copy each image over to the output images folder
    for entry in input_test_names:
        filename, file_extension = os.path.splitext(entry)
        if file_extension == ".jpeg" or file_extension == ".JPG" or file_extension == ".png":
            shutil.copy(input_path + "\\test\\" + entry, output_path + "\\" + project_name + "\\main_dataset\\img")
            print("Copied: " + entry)
        else:
            notAvaiableCount =+ 1

    # print(str(notAvaiableCount) + " files were skipped")

main()