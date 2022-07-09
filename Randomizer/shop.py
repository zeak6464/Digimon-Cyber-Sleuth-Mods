import pandas
import random
import shutil
import os.path
import time


item_ids = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,79,80,90,91,92,100,101,102,103,104,105,106,107,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,501,502,503,504,505,506,507,508,509,510,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539]

def draw_number_of_items():
    # Replace with whatever distribution you want...
    return random.randint(99, 100)

def shop_func():
    # File name of where mod is made
    dir_name = "./shop"

    # Output File name for mod .zip
    output_filename = "Random Shop"

    # File name for Shop & Backup
    file_name = "./shop/modfiles/data/shop_para.mbe/lineup.csv"
    back_up = "./backup/shop_backup.csv"


    # List of all Items in Game
    item = "./infolist/item.csv"


    # Open file & makes backup
    df = pandas.read_csv(file_name)
    file_exists = os.path.exists('./backup/shop_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    # Open the csv file (Shop)
    # n= Number of Items
    for i, row in df.iterrows():
        drawn_items = random.sample(item_ids, draw_number_of_items())
        drawn_items += [0]*(100 - len(drawn_items))
        row[1:] = drawn_items

    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)