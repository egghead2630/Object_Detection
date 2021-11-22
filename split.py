import os
import random
import shutil

from sklearn.model_selection import train_test_split

path = './train/'
path_L = './labels/'
if os.path.isdir('train/images/') is not True:
    os.makedirs('train/images/')
if os.path.isdir('val/') is not True:
    os.makedirs('val/')
if os.path.isdir('val/images/') is not True:
    os.makedirs('val/images/')

if os.path.isdir('train/labels/') is not True:
    os.makedirs('train/labels/')

if os.path.isdir('val/labels/') is not True:
    os.makedirs('val/labels/')
val_P = 'val/images/'
train_P = 'train/images/'
val_LP = 'val/labels/'
train_LP = 'train/labels/'

file_list = os.listdir(path)
pngs = []
txts = []
for file in file_list:
    if file[-4:] == ".png":
        pngs.append(file)
        txts.append(file[0:-4] + '.txt')
png_train, png_test, txts_train, txts_test = train_test_split(pngs,
                                                              txts,
                                                              test_size=0.1)
print(len(png_test))
print(len(txts_test))


for png in png_train:
    shutil.copyfile(path+png, train_P + png)
for png in png_test:
    shutil.copyfile(path+png, val_P + png)
for label in txts_train:
    shutil.copyfile(path_L+label, train_LP + label)
for label in txts_test:
    shutil.copyfile(path_L+label, val_LP + label)
