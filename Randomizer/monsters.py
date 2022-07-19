import pandas
import random
import shutil
import os.path
import time


def monsters_func():
    # File name of where mod is made
    dir_name = "./monsters"

    # Output File name for mod .zip
    output_filename = "Random Monster Easy"

    # File name for monsters & Backup
    file_name = "./monsters/modfiles/data/mon_para.mbe/Monster.csv"
    back_up = "./backup/mon_para_backup.csv"

    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/mon_para_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")
 
    df['EXP'] = df['EXP'].apply(lambda x: x + 1000)
    df['EXPx2'] = df['EXPx2'].apply(lambda x: x + 10000)
    df['YEN'] = df['YEN'].apply(lambda x: x + 1000)
    df['YENx2'] = df['YENx2'].apply(lambda x: x + 10000)
    df['itemChance1'] = 100
    df['itemChance2'] = 100
    df['scanRate'] = 100


    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)