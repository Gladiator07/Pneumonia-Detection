import os

data_dir = '/root/input/chest_xray'

print("The files in the data are: ")
print(os.listdir(data_dir))

classes = os.listdir(os.path.join(data_dir + "/train"))

print(f"The classes are: {classes}")

pneumonia_files_train = os.listdir(os.path.join(data_dir, "train/PNEUMONIA"))

# 3875
print(
    f"Number of images for Pneumonia class (train set) : {len(pneumonia_files_train)}")

normal_files_train = os.listdir(os.path.join(data_dir, "train/NORMAL"))
# 1341
print(
    f"Number of images for Normal class (train set) : {len(normal_files_train)}")


pneumonia_files_valid = os.listdir(os.path.join(data_dir, "val/PNEUMONIA"))

# 8
print(
    f"Number of images for Pneumonia class (val set) : {len(pneumonia_files_valid)}")

normal_files_valid = os.listdir(os.path.join(data_dir, "val/NORMAL"))
# 8
print(
    f"Number of images for Pneumonia class (val set) : {len(normal_files_valid)}")


pneumonia_files_test = os.listdir(os.path.join(data_dir, "test/PNEUMONIA"))

# 390
print(
    f"Number of images for Pneumonia class (test set) : {len(pneumonia_files_test)}")

normal_files_test = os.listdir(os.path.join(data_dir, "test/NORMAL"))
# 234
print(
    f"Number of images for Pneumonia class (test set) : {len(normal_files_test)}")
