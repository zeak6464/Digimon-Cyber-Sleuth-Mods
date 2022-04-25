import pandas
import random
import shutil
import os.path

def digivolve_func():
    # File name of where mod is made
    dir_name = "./digivolve"

    # Output File name for mod .zip
    output_filename = "Random Digivolve"

    # File name for Digimon digivolve & Backup
    file_name = "./digivolve/modfiles/data/evolution_next_para.mbe/digimon.csv"
    back_up = "./backup/digivolve_backup.csv"


    # List of all Digimon in Game
    digimon = "./infolist/digimon.csv"

    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/digivolve_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    # Open the csv file (Digimon)
    # n= Number of Digimon in market
    digi1 = pandas.read_csv(digimon).sample(n=332) 
    digi2 = pandas.read_csv(digimon).sample(n=332) 
    digi3 = pandas.read_csv(digimon).sample(n=332) 
    digi4 = pandas.read_csv(digimon).sample(n=332) 
    digi5 = pandas.read_csv(digimon).sample(n=332) 
    digi6 = pandas.read_csv(digimon).sample(n=332) 

    # Open the csv file (File_Name)
    df = pandas.read_csv(file_name,index_col=["id","digi1","digi2","digi3","digi4","digi5","digi6"])

    # Inserts Colums
    df.insert(loc=0, column="id", value= pandas.read_csv(digimon))
    df.insert(loc=1, column="digi1", value= digi1 )
    df.insert(loc=2, column="digi2", value= digi2 )
    df.insert(loc=3, column="digi3", value= digi3 )
    df.insert(loc=4, column="digi4", value= digi4 )
    df.insert(loc=5, column="digi5", value= digi5 )
    df.insert(loc=6, column="digi6", value= digi6 )

    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)