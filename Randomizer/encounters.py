import pandas
import random
import shutil
import os.path

def encounters_func():
    # File name of where mod is made
    dir_name = "./encounters"

    # Output File name for mod .zip
    output_filename = "Random Encounters"

    # File name for Digimon digivolve & Backup
    file_name = "./encounters/modfiles/data/mon_cpl.mbe/Coupling.csv"
    back_up = "./backup/encounters_backup.csv"


    # List of all Digimon in Game
    digimon = "./infolist/digimon.csv"

    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/encounters_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    # Open the csv file (Digimon)
    # n= Number of Digimon
    digi1 = pandas.read_csv(digimon).sample(n=1947,replace=True) 
    digi2 = pandas.read_csv(digimon).sample(n=1947,replace=True) 
    digi3 = pandas.read_csv(digimon).sample(n=1947,replace=True) 
    digi4 = pandas.read_csv(digimon).sample(n=1947,replace=True) 
    digi5 = pandas.read_csv(digimon).sample(n=1947,replace=True) 
    digi6 = pandas.read_csv(digimon).sample(n=1947,replace=True) 


    # Open the csv file (File_Name)
    df = pandas.read_csv(file_name,index_col=["id","digi1","digi2","digi3","digi4","digi5","digi6","level1","level2","level3","level4","level5","level6","variation1","variation2","variation3","variation4","variation5","variation6","unk13","unk14","unk15","unk16","unk9","unk10"]).sample(frac=1, ignore_index=True)


    # Inserts Colums
    df.insert(loc=0,column="id",value= pandas.read_csv(file_name)["id"])

    df.insert(loc=1,column="digi1",value=  pandas.read_csv(file_name)["digi1"])
    df.insert(loc=2,column="digi2",value=  pandas.read_csv(file_name)["digi2"])
    df.insert(loc=3,column="digi3",value=  pandas.read_csv(file_name)["digi3"])
    df.insert(loc=4,column="digi4",value=  pandas.read_csv(file_name)["digi4"])
    df.insert(loc=5,column="digi5",value=  pandas.read_csv(file_name)["digi5"])
    df.insert(loc=6,column="digi6",value=  pandas.read_csv(file_name)["digi6"])

    df.insert(loc=7,column="level1",value= pandas.read_csv(file_name)["level1"])
    df.insert(loc=8,column="level2",value= pandas.read_csv(file_name)["level2"])
    df.insert(loc=9,column="level3",value= pandas.read_csv(file_name)["level3"])
    df.insert(loc=10,column="level4",value= pandas.read_csv(file_name)["level4"])
    df.insert(loc=11,column="level5",value= pandas.read_csv(file_name)["level5"])
    df.insert(loc=12,column="level6",value= pandas.read_csv(file_name)["level6"])

    df.insert(loc=13,column="variation1",value= pandas.read_csv(file_name)["variation1"])
    df.insert(loc=14,column="variation2",value= pandas.read_csv(file_name)["variation2"])
    df.insert(loc=15,column="variation3",value= pandas.read_csv(file_name)["variation3"])
    df.insert(loc=16,column="variation4",value= pandas.read_csv(file_name)["variation4"])
    df.insert(loc=17,column="variation5",value= pandas.read_csv(file_name)["variation5"])
    df.insert(loc=18,column="variation6",value= pandas.read_csv(file_name)["variation6"])

    df.insert(loc=19,column="unk13",value= pandas.read_csv(file_name)["unk13"])
    df.insert(loc=20,column="unk14",value= pandas.read_csv(file_name)["unk14"])
    df.insert(loc=21,column="unk15",value= pandas.read_csv(file_name)["unk15"])
    df.insert(loc=22,column="unk16",value= pandas.read_csv(file_name)["unk16"])
    df.insert(loc=23,column="unk9",value= pandas.read_csv(file_name)["unk9"])
    df.insert(loc=24,column="unk10",value= pandas.read_csv(file_name)["unk10"])


    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)