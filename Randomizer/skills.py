import pandas
import random
import shutil
import os.path

# File name of where mod is made
dir_name = "./skills"

# Output File name for mod .zip
output_filename = "Random Skills"

# File name for Digimon digivolve & Backup
file_name = "./infolist/skillslist.csv"
back_up = "./backup/skills_backup.csv"


# List of all Digimon in Game
skills = "./infolist/skillslist.csv"

# Open file & makes backup
df = pandas.read_csv(file_name)
file_exists = os.path.exists('./backup/skills_backup.csv')

if file_exists == True:
    print("backup is already made")
else:
    df.to_csv(back_up, index=False)
    print("backup has been made")

# Open the csv file (File_Name)
zf = pandas.read_csv(back_up,usecols=["ID"])

# Saves the Randomized File
zf.to_csv(file_name, index=False)

