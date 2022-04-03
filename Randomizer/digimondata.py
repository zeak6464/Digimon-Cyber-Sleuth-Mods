import pandas
import random
import shutil
import os.path

def digimondata_func():
    # File name of where mod is made
    dir_name = "./digimondata"

    # Output File name for mod .zip
    output_filename = "Random DigimonData"

    # File name for Digimon digivolve & Backup
    file_name = "./digimondata/modfiles/data/digimon_farm_para.mbe/digimon.csv"
    back_up = "./backup/digimondata_backup.csv"


    # List of all Atk Skills in Game
    digimon = "./infolist/skills.csv"

    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/digimondata_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    # Open the csv file (Digimon)
    # n= Number of Skills Listed
    sMove1 = pandas.read_csv(digimon).sample(n=375,replace=True)
    sMove2 = pandas.read_csv(digimon).sample(n=375,replace=True)
    
    move1 = pandas.read_csv(digimon).sample(n=375,replace=True)
    move2 = pandas.read_csv(digimon).sample(n=375,replace=True)
    move3 = pandas.read_csv(digimon).sample(n=375,replace=True)
    move4 = pandas.read_csv(digimon).sample(n=375,replace=True)
    move5 = pandas.read_csv(digimon).sample(n=375,replace=True)
    move6 = pandas.read_csv(digimon).sample(n=375,replace=True)


    # Open the csv file (File_Name)
    df = pandas.read_csv(file_name,index_col=["id","memoryUse","growthType","unk3","baseHP","baseSP","baseATK","baseDEF","baseINT","baseSPD","maxLevel","equipSlots","supportSkill","sMove1","sMove1Level","sMove2","sMove2Level","move1","move1Level","move2","move2Level","move3","move3Level","move4","move4Level","move5","move5Level","move6","move6Level","expValue","levelCurve","profile","unk32","unk33"]).sample(frac=1, ignore_index=True)


    # Inserts Colums
    df.insert(loc=0,column="id",value= pandas.read_csv(file_name)["id"])
    
    df.insert(loc=1,column="memoryUse",value= 0)
    df.insert(loc=2,column="growthType",value= pandas.read_csv(file_name)["growthType"])
    df.insert(loc=3,column="unk3",value= pandas.read_csv(file_name)["unk3"])
    df.insert(loc=4,column="baseHP",value= pandas.read_csv(file_name)["baseHP"])
    df.insert(loc=5,column="baseSP",value= pandas.read_csv(file_name)["baseSP"])
    df.insert(loc=6,column="baseATK",value= pandas.read_csv(file_name)["baseATK"])
    df.insert(loc=7,column="baseDEF",value= pandas.read_csv(file_name)["baseDEF"])
    df.insert(loc=8,column="baseINT",value= pandas.read_csv(file_name)["baseINT"])
    df.insert(loc=9,column="baseSPD",value= pandas.read_csv(file_name)["baseSPD"])
    
    df.insert(loc=10,column="maxLevel",value= 100)
    
    df.insert(loc=11,column="equipSlots",value= pandas.read_csv(file_name)["equipSlots"])
    df.insert(loc=12,column="supportSkill",value= pandas.read_csv(file_name)["supportSkill"])
    
    df.insert(loc=13,column="sMove1",value= sMove1)
    df.insert(loc=14,column="sMove1Level",value= pandas.read_csv(file_name)["sMove1Level"])
    df.insert(loc=15,column="sMove2",value= sMove2)
    df.insert(loc=16,column="sMove2Level",value= pandas.read_csv(file_name)["sMove2Level"])
    df.insert(loc=17,column="move1",value= move1)
    df.insert(loc=18,column="move1Level",value= pandas.read_csv(file_name)["move1Level"])
    df.insert(loc=19,column="move2",value= move2)
    df.insert(loc=20,column="move2Level",value= pandas.read_csv(file_name)["move2Level"])
    df.insert(loc=21,column="move3",value= move3)
    df.insert(loc=22,column="move3Level",value= pandas.read_csv(file_name)["move3Level"])
    df.insert(loc=23,column="move4",value= move4)
    df.insert(loc=24,column="move4Level",value= pandas.read_csv(file_name)["move4Level"])
    df.insert(loc=25,column="move5",value= move5)
    df.insert(loc=26,column="move5Level",value= pandas.read_csv(file_name)["move5Level"])
    df.insert(loc=27,column="move6",value= move6)
    df.insert(loc=28,column="move6Level",value= pandas.read_csv(file_name)["move6Level"])
    
    df.insert(loc=29,column="expValue",value= pandas.read_csv(file_name)["expValue"])
    df.insert(loc=30,column="levelCurve",value= pandas.read_csv(file_name)["levelCurve"])
    df.insert(loc=31,column="profile",value= pandas.read_csv(file_name)["profile"])
    df.insert(loc=32,column="unk32",value= pandas.read_csv(file_name)["unk32"])
    df.insert(loc=33,column="unk33",value= pandas.read_csv(file_name)["unk33"])


    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)
