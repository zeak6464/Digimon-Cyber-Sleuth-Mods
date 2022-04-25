import pandas
import random
import shutil
import os.path
import time

def enskills_func():
    # File name of where mod is made
    dir_name = "./encounterskills"

    # Output File name for mod .zip
    output_filename = "Random Encounter Skills"

    # File name for Digimon digivolve & Backup
    file_name = "./encounterskills/modfiles/data/battle_ai.mbe/Ai.csv"
    back_up = "./backup/encounterskills_backup.csv"


    # List of all Atk Skills in Game
    skills = "./infolist/skills.csv"

    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/encounterskills_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    # Open the csv file (Digimon)
    # n= Number of Skills Listed
    move1 = pandas.read_csv(skills).sample(n=983,replace=True)
    move2 = pandas.read_csv(skills).sample(n=983,replace=True)
    move3 = pandas.read_csv(skills).sample(n=983,replace=True)
    move4 = pandas.read_csv(skills).sample(n=983,replace=True)
    move5 = pandas.read_csv(skills).sample(n=983,replace=True)
    move6 = pandas.read_csv(skills).sample(n=983,replace=True)
    move7 = pandas.read_csv(skills).sample(n=983,replace=True)
    move8 = pandas.read_csv(skills).sample(n=983,replace=True)
    move9 = pandas.read_csv(skills).sample(n=983,replace=True)
    move10 = pandas.read_csv(skills).sample(n=983,replace=True)


    # Open the csv file (File_Name)
    df = pandas.read_csv(file_name,index_col=["id","nameId?","Unk2_1","Unk2_2","Unk3_1","Unk3_2","Unk4_1","Unk4_2","Unk5","Unk6_1","Unk6_2","Unk7_1","Unk7_2","Unk8_1","Unk8_2","Unk9","Unk10_1","Unk10_2","Unk11_1","Unk11_2","Unk12_1","Unk12_2","Unk13","Unk14_1","Unk14_2","Unk15_1","Unk15_2","Unk16_1","Unk16_2","Unk17","Unk18_1","Unk18_2","Unk19_1","Unk19_2","Unk20_1","Unk20_2","Unk21","Unk22_1","Unk22_2","Unk23_1","Unk23_2","Unk24_1","Unk24_2","Unk25","Unk26_1","Unk26_2","Unk27_1","Unk27_2","Unk28_1","Unk28_2","Unk29","Unk30_1","Unk30_2","Unk31_1","Unk31_2","Unk32_1","Unk32_2","Unk33","Unk34_1","Unk34_2","Unk35_1","Unk35_2","Unk36_1","Unk36_2","Unk37","Unk38_1","Unk38_2","Unk39","Unk40"]).sample(frac=1, ignore_index=True)


    # Inserts Colums
    df.insert(loc=0,column="id",value= pandas.read_csv(file_name)["id"])
    
    df.insert(loc=1,column="nameId?",value= move1)
    df.insert(loc=2,column="Unk2_1",value= 0)
    df.insert(loc=3,column="Unk2_2",value= 0)
    df.insert(loc=4,column="Unk3_1",value= 10)
    df.insert(loc=5,column="Unk3_2",value= 0)
    df.insert(loc=6,column="Unk4_1",value= 0)
    df.insert(loc=7,column="Unk4_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=8,column="Unk5",value= move2)
    df.insert(loc=9,column="Unk6_1",value= 0)
    df.insert(loc=10,column="Unk6_2",value= 0)
    df.insert(loc=11,column="Unk7_1",value= 10)
    df.insert(loc=12,column="Unk7_2",value= 0)
    df.insert(loc=13,column="Unk8_1",value= 0)
    df.insert(loc=14,column="Unk8_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=15,column="Unk9",value= move3)
    df.insert(loc=16,column="Unk10_1",value= 0)
    df.insert(loc=17,column="Unk10_2",value= 0)
    df.insert(loc=18,column="Unk11_1",value= 10)
    df.insert(loc=19,column="Unk11_2",value= 0)
    df.insert(loc=20,column="Unk12_1",value= 0)
    df.insert(loc=21,column="Unk12_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=22,column="Unk13",value= move4)
    df.insert(loc=23,column="Unk14_1",value= 0)
    df.insert(loc=24,column="Unk14_2",value= 0)
    df.insert(loc=25,column="Unk15_1",value= 10)
    df.insert(loc=26,column="Unk15_2",value= 0)
    df.insert(loc=27,column="Unk16_1",value= 0)
    df.insert(loc=28,column="Unk16_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=29,column="Unk17",value= move5)
    df.insert(loc=30,column="Unk18_1",value= 0)
    df.insert(loc=31,column="Unk18_2",value= 0)
    df.insert(loc=32,column="Unk19_1",value= 10)
    df.insert(loc=33,column="Unk19_2",value= 0)
    df.insert(loc=34,column="Unk20_1",value= 0)
    df.insert(loc=35,column="Unk20_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=36,column="Unk21",value= move6)
    df.insert(loc=37,column="Unk22_1",value= 0)
    df.insert(loc=38,column="Unk22_2",value= 0)
    df.insert(loc=39,column="Unk23_1",value= 10)
    df.insert(loc=40,column="Unk23_2",value= 0)
    df.insert(loc=41,column="Unk24_1",value= 0)
    df.insert(loc=42,column="Unk24_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=43,column="Unk25",value= move7)
    df.insert(loc=44,column="Unk26_1",value= 0)
    df.insert(loc=45,column="Unk26_2",value= 0)
    df.insert(loc=46,column="Unk27_1",value= 10)
    df.insert(loc=47,column="Unk27_2",value= 0)
    df.insert(loc=48,column="Unk28_1",value= 0)
    df.insert(loc=49,column="Unk28_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=50,column="Unk29",value= move8)
    df.insert(loc=51,column="Unk30_1",value= 0)
    df.insert(loc=52,column="Unk30_2",value= 0)
    df.insert(loc=53,column="Unk31_1",value= 10)
    df.insert(loc=54,column="Unk31_2",value= 0)
    df.insert(loc=55,column="Unk32_1",value= 0)
    df.insert(loc=56,column="Unk32_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=57,column="Unk33",value= move9)
    df.insert(loc=58,column="Unk34_1",value= 0)
    df.insert(loc=59,column="Unk34_2",value= 0)
    df.insert(loc=60,column="Unk35_1",value= 10)
    df.insert(loc=61,column="Unk35_2",value= 0)
    df.insert(loc=62,column="Unk36_1",value= 0)
    df.insert(loc=63,column="Unk36_2",value= 0)
    time.sleep(0.2)
    
    df.insert(loc=64,column="Unk37",value= move10)
    df.insert(loc=65,column="Unk38_1",value= 0)
    df.insert(loc=66,column="Unk38_2",value= 0)
    df.insert(loc=67,column="Unk39",value= 10)
    df.insert(loc=68,column="Unk40",value= 0)
    time.sleep(0.2)


    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)
