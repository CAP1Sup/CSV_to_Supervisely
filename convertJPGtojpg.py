from PIL import Image  # Python Image Library - Image Processing
import glob
import os

all_train_file_names = glob.glob("../SuperviselyTransformation/Input_structure/test/*.jpg")
counter = 1

for file in all_train_file_names:

    if file[len(file) - 4 : len(file)] == ".JPG":
        image = Image.open(file)
        new_file_name = file[0 : len(file) - 4] + "##.jpg"
        image.save(new_file_name)
        os.remove(file)
        print("Original: " + file)
        print("Saved: ", new_file_name)

    elif file[len(file) - 5 : len(file)] == "#.jpg":
        new_file_name = file[0 : len(file) - 5] + "#.jpg"
        print(new_file_name)
        new_image = Image.open(new_file_name)
        final_file_name = new_file_name[0 : len(new_file_name) - 6] + ".jpg"
        new_image.save(final_file_name)
        os.remove(new_file_name)
        print("Original: " + new_file_name)
        print("Saved: ", new_image)

    print("On file " + str(counter) + " of " + str(len(all_file_names)))
    counter = counter + 1

print("Files Converted!")