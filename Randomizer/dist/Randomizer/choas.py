import pandas
import random
import shutil
import os.path
import csv

baby = [629,387,437,317,320]
babytwo = [62,322,512,438,631,325,515,567,510,514,388,321]
child = [50,143,63,707,81,564,582,55,569,151,713,90,53,626,595,111,343,709,697,728,20,701,303,708,457,208,112,9,96,687,348,97,307,705,42,114,361,389,706,607,458,56,390,2,391,750,392,190,781,682,761,762,763,764,765]
adult = [102,730,758,15,676,64,711,344,377,680,393,11,365,87,394,341,760,68,304,455,710,12,714,395,78,630,326,712,398,367,399,729,218,209,113,5,452,30,58,347,130,54,313,14,91,16,698,755,621,759,363,92,93,349,396,375,70,308,115,13,397,22,752,43,314,702,10,369,370,548,25,590,72,3,77,454,191,783,716]
perfect = [305,65,731,342,756,627,85,210,679,400,311,148,401,309,681,402,44,727,211,403,26,4,719,723,379,720,79,404,6,345,116,405,129,84,23,374,406,699,376,33,407,718,576,408,409,41,596,410,82,584,753,177,411,21,101,59,31,74,412,132,134,302,327,364,413,61,721,71,73,722,359,39,107,140,715,726,192,751]
ultimate = [66,416,417,451,732,419,346,773,117,600,27,421,744,677,150,422,688,127,754,423,32,704,83,734,774,735,48,424,425,749,94,737,86,213,315,741,771,745,440,128,733,632,38,126,738,700,739,743,19,75,426,60,36,49,427,428,69,175,429,214,450,306,35,439,310,453,431,678,675,748,24,747,95,385,47,312,135,182,434,80,383,37,34,740,703,57,742,901,902,903,905,193,382,683,782,784]
ultimateplus = [106,67,766,420,215,88,757,772,118,104,105,40,435,328,776,775,777,778,779,904]

mon_lists_by_stage = [baby, babytwo, child,adult,perfect,ultimate,ultimateplus]
mon_list_lookups = [set(lst) for lst in mon_lists_by_stage] # O(1) lookup instead of O(n)

def get_stage(id_):
    for i, mon_ids in enumerate(mon_list_lookups):
        if id_ in mon_ids:
            return i
    return -1

roll_distribution = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
cumulative_distribution = [sum(roll_distribution[:i+1]) for i in range(len(roll_distribution))]
def draw_number_of_evos(max_evos):
    # Draw a biased random integer between 0 and 5
    rand_num = random.random()
    for num_evos, threshold in enumerate(cumulative_distribution):
        if rand_num < threshold:
            break
        
    # Truncate to maximum allowed evos
    return min(num_evos+1, max_evos)
    

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
    df = pandas.read_csv(back_up,index_col=["id","digi1","digi2","digi3","digi4","digi5","digi6","level1","level2","level3","level4","level5","level6","variation1","variation2","variation3","variation4","variation5","variation6","unk13","unk14","unk15","unk16","unk9","unk10"]).sample(frac=1, ignore_index=True)
    
    df.insert(loc=0,column="id",value= pandas.read_csv(back_up)["id"])
    df.insert(loc=1,column="digi1",value=  pandas.read_csv(back_up)["digi1"])
    df.insert(loc=2,column="digi2",value=  pandas.read_csv(back_up)["digi2"])
    df.insert(loc=3,column="digi3",value=  pandas.read_csv(back_up)["digi3"])
    df.insert(loc=4,column="digi4",value=  pandas.read_csv(back_up)["digi4"])
    df.insert(loc=5,column="digi5",value=  pandas.read_csv(back_up)["digi5"])
    df.insert(loc=6,column="digi6",value=  pandas.read_csv(back_up)["digi6"])
    
    file_exists = os.path.exists('./backup/encounters_backup.csv') 
    if file_exists == True:
        print("backup is already made")
    else:
        df.to_csv(back_up, index=False)
        print("backup has been made")

    for i, row in df.iterrows():
        mon_stage = get_stage(row[1])
        
        evolutions = [0,0,0,0,0,0]
        if mon_stage == -1:
            continue   
        elif mon_stage == 7:
            pass   
        else:
            mon_stage = random.randint(0, 6)
            potential_evos = mon_lists_by_stage[mon_stage]
            evolutions = random.sample(potential_evos, random.randint(1, min(6, len(potential_evos))))
            evolutions += [-1]*(6 - len(evolutions))
        
        row[1:7] = evolutions
        
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
    
    f = open(file_name)
    f.close()
    
    shutil.make_archive(output_filename, 'zip', dir_name)