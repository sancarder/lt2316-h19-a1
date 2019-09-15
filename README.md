# lt2316-h19-a1
Assignment 1 in Machine Learning course, Master program in Language Technology, Gothenburg University

## Part 0: GPU
My GPU is 0

## Part 1: Data preparation
Languages chosen (10):
+ Albanian,
+ Bokmål
+ Dutch
+ English
+ German
+ Latin
+ Portuguese
+ Somali
+ Swedish
+ Turkish

A script create either training and test data depending on the arguments. The file is run like this:
+ create_language_data.py [file with the 10 languages] [file with the labels] [x file] [y file] [output x file] [output y file]
+ Example: python create_language_data.py languages.txt data/labels.csv data/x_train.txt data/y_train.txt my-x-train.txt my-y-train.txt