import pandas
import random
import shutil
import os.path

def starters_func():
    # File name of where mod is made
    dir_name = "./starters"

    # Output File name for mod .zip
    output_filename = "Random Starters"

    # File name for Digimon Starters & Backup
    file_name = "./starters/modfiles/data/join_digimon_para_add.mbe/party.csv"
    file_nameCS = "./starters/modfiles/data/join_digimon_para.mbe/party.csv"
    back_up = "./backup/starters_backup.csv"

    # List of all Digimon in Game
    digimon = "./infolist/digimon.csv"

    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/starters_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    # Open the csv file (Digimon)
    # n= Number of Digimon
    dfc = pandas.read_csv(digimon).sample(n=8) 

    # Open the csv file (File_Name) & Removes Colums 
    df = pandas.read_csv(file_name, index_col=["id","unk1","unk2","unk3","unk4","unk5","unk6","unk7"]).sample(frac=1, ignore_index=True)

    # Replaces Digimon ID Data with Random ID from (Digimon)
    df.loc[:,'digimon_id'] = dfc

    # Reinserts Colum "ID" & "Unk1 -> Unk7"
    df.insert(loc=0, column="id", value=pandas.read_csv(file_name)["id"])
    df.insert(loc=2, column="unk1", value=pandas.read_csv(file_name)["unk1"])
    df.insert(loc=3, column="unk2", value=pandas.read_csv(file_name)["unk2"])
    df.insert(loc=4, column="unk3", value=pandas.read_csv(file_name)["unk3"])
    df.insert(loc=5, column="unk4", value=pandas.read_csv(file_name)["unk4"])
    df.insert(loc=6, column="unk5", value=pandas.read_csv(file_name)["unk5"])
    df.insert(loc=7, column="unk6", value=pandas.read_csv(file_name)["unk6"])
    df.insert(loc=8, column="unk7", value=pandas.read_csv(file_name)["unk7"])

    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    df.to_csv(file_nameCS, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)