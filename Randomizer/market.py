import pandas
import random
import shutil
import os.path

def market_func():
    # File name of where mod is made
    dir_name = "./market"

    # Output File name for mod .zip
    output_filename = "Random DigiMarket"

    # File name for Digimon Market & Backup
    file_name = "./market/modfiles/data/digimon_market_para.mbe/table.csv"
    back_up = "./backup/market_backup.csv"


    # List of all Digimon in Game
    digimon = "./infolist/digimon.csv"

    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/market_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    # Open the csv file (Digimon)
    # n= Number of Digimon in market
    dfc = pandas.read_csv(digimon).sample(n=50) 

    # Open the csv file (File_Name) & Removes Colum "ID" & "Unknown1"
    df = pandas.read_csv(file_name, index_col=["id","unknown1"]).sample(frac=1, ignore_index=True)

    # Replaces Digimon ID Data with Random ID from (Digimon)
    df.loc[:,'digimonId'] = dfc

    # Replaces Prices
    df.loc[:,'price'] = 1

    # Replaces Level
    df.loc[:,'level'] = 1

    # Reinserts Colum "ID" & "Unknown1"
    df.insert(loc=0, column="id", value=pandas.read_csv(file_name)["id"])
    df.insert(loc=2, column="unknown1", value=pandas.read_csv(file_name)["unknown1"])

    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)