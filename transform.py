# Christian Piper
# 12/1/19
# This program will prompt the user for the beginning and end directories, then convert from a .csv format to a Supervisely format

import os
import shutil
import generateImageJson
import generateMeta

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

    input_names = input_train_names + input_test_names

    input_image_names = []
    input_xml_names = []

    for entry in input_names:
        unused_filename, file_extension = os.path.splitext(entry)
        # TODO: convert the files to the standarized format
        if file_extension == ".jpeg":
            input_image_names.append(entry)

        elif file_extension == "jpg":
            input_image_names.append(entry)

        elif file_extension == ".xml":
            input_xml_names.append(entry)
            
    notAvaiableCount = 0

    # Copy each image over to the output images folder
    for entry in input_train_names:
        filename, file_extension = os.path.splitext(entry)
        if file_extension == ".jpeg" or file_extension == ".JPG":
            shutil.copy(input_path + "\\train\\" + entry, output_path + "\\" + project_name + "\\main_dataset\\img")
            print("Copied: " + entry)
        elif file_extension == ".xml":
            transferXMLToJson(input_path + "\\train\\" + entry)
        else:
            notAvaiableCount =+ 1            

    # Copy each image over to the output images folder
    for entry in input_test_names:
        filename, file_extension = os.path.splitext(entry)
        if file_extension == ".jpeg" or file_extension == ".JPG":
            shutil.copy(input_path + "\\test\\" + entry, output_path + "\\" + project_name + "\\main_dataset\\img")
            print("Copied: " + entry)
        else:
            notAvaiableCount =+ 1

    # print(str(notAvaiableCount) + " files were skipped")

    #for 
    #generateImageJson.getInfoFromXML()

def transferXMLToJson(file_path):
    xml_file = open(file_path)
    info = generateImageJson.getInfoFromXML(xml_file.read())
    object_count = (len(info) - 3) % 5
    file_name = info[0]
    width = info[1]
    height = info[2]

    names = []
    xmins = []
    ymins = []
    xmaxes = []
    ymaxes = []

    for object_number in range(0, object_count):
        names.append(info[1 + (5 * object_number)])
        xmins.append(info[2 + (5 * object_number)])
        ymins.append(info[3 + (5 * object_number)])
        xmaxes.append(info[4 + (5 * object_number)])
        ymaxes.append(info[5 + (5 * object_number)])

    generateImageJson.generateJson(file_name, width, height, names, xmins, ymins, xmaxes, ymaxes)


main()