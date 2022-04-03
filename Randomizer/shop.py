import pandas
import random
import shutil
import os.path
import time

def shop_func():
    # File name of where mod is made
    dir_name = "./shop"

    # Output File name for mod .zip
    output_filename = "Random Shop"

    # File name for Shop & Backup
    file_name = "./shop/modfiles/data/shop_para.mbe/lineup.csv"
    back_up = "./backup/shop_backup.csv"


    # List of all Items in Game
    item = "./shop/modfiles/data/item_para.mbe/table.csv"

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
    item1  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item1['buyPrice'].ge(1)
    item1  = item1[item1.buyPrice >= 1]
    item1  = item1.drop(columns=['buyPrice'])
    item1  = item1.sample(n=44)
    
    
    item2  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item2['buyPrice'].ge(1)
    item2  = item2[item2.buyPrice >= 1]
    item2  = item2.drop(columns=['buyPrice'])
    item2  = item2.sample(n=44)
    
    item3  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item3['buyPrice'].ge(1)
    item3  = item3[item3.buyPrice >= 1]
    item3  = item3.drop(columns=['buyPrice'])
    item3  = item3.sample(n=44)
    
    item4  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item4['buyPrice'].ge(1)
    item4  = item4[item4.buyPrice >= 1]
    item4  = item4.drop(columns=['buyPrice'])
    item4  = item4.sample(n=44)
    
    item5  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item5['buyPrice'].ge(1)
    item5  = item5[item5.buyPrice >= 1]
    item5  = item5.drop(columns=['buyPrice'])
    item5  = item5.sample(n=44)
    
    item6  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item6['buyPrice'].ge(1)
    item6  = item6[item6.buyPrice >= 1]
    item6  = item6.drop(columns=['buyPrice'])
    item6  = item6.sample(n=44)
    
    item7  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item7['buyPrice'].ge(1)
    item7  = item7[item7.buyPrice >= 1]
    item7  = item7.drop(columns=['buyPrice'])
    item7  = item7.sample(n=44)
    
    item8  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item8['buyPrice'].ge(1)
    item8  = item8[item8.buyPrice >= 1]
    item8  = item8.drop(columns=['buyPrice'])
    item8  = item8.sample(n=44)
    
    item9  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item9['buyPrice'].ge(1)
    item9  = item9[item9.buyPrice >= 1]
    item9  = item9.drop(columns=['buyPrice'])
    item9  = item9.sample(n=44)
    
    item10  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item10['buyPrice'].ge(1)
    item10  = item10[item10.buyPrice >= 1]
    item10  = item10.drop(columns=['buyPrice'])
    item10  = item10.sample(n=44)
    
    item11  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item11['buyPrice'].ge(1)
    item11  = item11[item11.buyPrice >= 1]
    item11  = item11.drop(columns=['buyPrice'])
    item11  = item11.sample(n=44)
    
    item12  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item12['buyPrice'].ge(1)
    item12  = item12[item12.buyPrice >= 1]
    item12  = item12.drop(columns=['buyPrice'])
    item12  = item12.sample(n=44)
    
    item13  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item13['buyPrice'].ge(1)
    item13  = item13[item13.buyPrice >= 1]
    item13  = item13.drop(columns=['buyPrice'])
    item13  = item13.sample(n=44)
    
    item14  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item14['buyPrice'].ge(1)
    item14  = item14[item14.buyPrice >= 1]
    item14  = item14.drop(columns=['buyPrice'])
    item14  = item14.sample(n=44)
    
    item15  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item15['buyPrice'].ge(1)
    item15  = item15[item15.buyPrice >= 1]
    item15  = item15.drop(columns=['buyPrice'])
    item15  = item15.sample(n=44)
    
    item16  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item16['buyPrice'].ge(1)
    item16  = item16[item16.buyPrice >= 1]
    item16  = item16.drop(columns=['buyPrice'])
    item16  = item16.sample(n=44)
    
    item17  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item17['buyPrice'].ge(1)
    item17  = item17[item17.buyPrice >= 1]
    item17  = item17.drop(columns=['buyPrice'])
    item17  = item17.sample(n=44)
    
    item18  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item18['buyPrice'].ge(1)
    item18  = item18[item18.buyPrice >= 1]
    item18  = item18.drop(columns=['buyPrice'])
    item18  = item18.sample(n=44)
    
    item19  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item19['buyPrice'].ge(1)
    item19  = item19[item19.buyPrice >= 1]
    item19  = item19.drop(columns=['buyPrice'])
    item19  = item19.sample(n=44)
    
    item20  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item20['buyPrice'].ge(1)
    item20  = item20[item20.buyPrice >= 1]
    item20  = item20.drop(columns=['buyPrice'])
    item20  = item20.sample(n=44)
    
    item21  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item21['buyPrice'].ge(1)
    item21  = item21[item21.buyPrice >= 1]
    item21  = item21.drop(columns=['buyPrice'])
    item21  = item21.sample(n=44)
    
    item22  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item22['buyPrice'].ge(1)
    item22  = item22[item22.buyPrice >= 1]
    item22  = item22.drop(columns=['buyPrice'])
    item22  = item22.sample(n=44)
    
    item23  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item23['buyPrice'].ge(1)
    item23  = item23[item23.buyPrice >= 1]
    item23  = item23.drop(columns=['buyPrice'])
    item23  = item23.sample(n=44)
    
    item24  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item24['buyPrice'].ge(1)
    item24  = item24[item24.buyPrice >= 1]
    item24  = item24.drop(columns=['buyPrice'])
    item24  = item24.sample(n=44)
    
    item25  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item25['buyPrice'].ge(1)
    item25  = item25[item25.buyPrice >= 1]
    item25  = item25.drop(columns=['buyPrice'])
    item25  = item25.sample(n=44)
    
    item26  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item26['buyPrice'].ge(1)
    item26  = item26[item26.buyPrice >= 1]
    item26  = item26.drop(columns=['buyPrice'])
    item26  = item26.sample(n=44)
    
    item27  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item27['buyPrice'].ge(1)
    item27  = item27[item27.buyPrice >= 1]
    item27  = item27.drop(columns=['buyPrice'])
    item27  = item27.sample(n=44)
    
    item28  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item28['buyPrice'].ge(1)
    item28  = item28[item28.buyPrice >= 1]
    item28  = item28.drop(columns=['buyPrice'])
    item28  = item28.sample(n=44)
    
    item29  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item29['buyPrice'].ge(1)
    item29  = item29[item29.buyPrice >= 1]
    item29  = item29.drop(columns=['buyPrice'])
    item29  = item29.sample(n=44)

    item30  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item30['buyPrice'].ge(1)
    item30  = item30[item30.buyPrice >= 1]
    item30  = item30.drop(columns=['buyPrice'])
    item30  = item30.sample(n=44)
    
    item31  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item31['buyPrice'].ge(1)
    item31  = item31[item31.buyPrice >= 1]
    item31  = item31.drop(columns=['buyPrice'])
    item31  = item31.sample(n=44)
    
    item32  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item32['buyPrice'].ge(1)
    item32  = item32[item32.buyPrice >= 1]
    item32  = item32.drop(columns=['buyPrice'])
    item32  = item32.sample(n=44)
    
    item33  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item33['buyPrice'].ge(1)
    item33  = item33[item33.buyPrice >= 1]
    item33  = item33.drop(columns=['buyPrice'])
    item33  = item33.sample(n=44)
    
    item34  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item34['buyPrice'].ge(1)
    item34  = item34[item34.buyPrice >= 1]
    item34  = item34.drop(columns=['buyPrice'])
    item34  = item34.sample(n=44)
    
    item35  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item35['buyPrice'].ge(1)
    item35  = item35[item35.buyPrice >= 1]
    item35  = item35.drop(columns=['buyPrice'])
    item35  = item35.sample(n=44)
    
    item36  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item36['buyPrice'].ge(1)
    item36  = item36[item36.buyPrice >= 1]
    item36  = item36.drop(columns=['buyPrice'])
    item36  = item36.sample(n=44)
    
    item37  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item37['buyPrice'].ge(1)
    item37  = item37[item37.buyPrice >= 1]
    item37  = item37.drop(columns=['buyPrice'])
    item37  = item37.sample(n=44)
    
    item38  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item38['buyPrice'].ge(1)
    item38  = item38[item38.buyPrice >= 1]
    item38  = item38.drop(columns=['buyPrice'])
    item38  = item38.sample(n=44)
    
    item39  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item39['buyPrice'].ge(1)
    item39  = item39[item39.buyPrice >= 1]
    item39  = item39.drop(columns=['buyPrice'])
    item39  = item39.sample(n=44)
    
    item40  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item40['buyPrice'].ge(1)
    item40  = item40[item40.buyPrice >= 1]
    item40  = item40.drop(columns=['buyPrice'])
    item40  = item40.sample(n=44)
    
    item41  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item41['buyPrice'].ge(1)
    item41  = item41[item41.buyPrice >= 1]
    item41  = item41.drop(columns=['buyPrice'])
    item41  = item41.sample(n=44)
    
    item42  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item42['buyPrice'].ge(1)
    item42  = item42[item42.buyPrice >= 1]
    item42  = item42.drop(columns=['buyPrice'])
    item42  = item42.sample(n=44)
    
    item43  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item43['buyPrice'].ge(1)
    item43  = item43[item43.buyPrice >= 1]
    item43  = item43.drop(columns=['buyPrice'])
    item43  = item43.sample(n=44)
    
    item44  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item44['buyPrice'].ge(1)
    item44  = item44[item44.buyPrice >= 1]
    item44  = item44.drop(columns=['buyPrice'])
    item44  = item44.sample(n=44)
    
    item45  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item45['buyPrice'].ge(1)
    item45  = item45[item45.buyPrice >= 1]
    item45  = item45.drop(columns=['buyPrice'])
    item45  = item45.sample(n=44)
    
    item46  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item46['buyPrice'].ge(1)
    item46  = item46[item46.buyPrice >= 1]
    item46  = item46.drop(columns=['buyPrice'])
    item46  = item46.sample(n=44)
    
    item47  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item47['buyPrice'].ge(1)
    item47  = item47[item47.buyPrice >= 1]
    item47  = item47.drop(columns=['buyPrice'])
    item47  = item47.sample(n=44)
    
    item48  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item48['buyPrice'].ge(1)
    item48  = item48[item48.buyPrice >= 1]
    item48  = item48.drop(columns=['buyPrice'])
    item48  = item48.sample(n=44)
    
    item49  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item49['buyPrice'].ge(1)
    item49  = item49[item49.buyPrice >= 1]
    item49  = item49.drop(columns=['buyPrice'])
    item49  = item49.sample(n=44)
    
    item50  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item50['buyPrice'].ge(1)
    item50  = item50[item50.buyPrice >= 1]
    item50  = item50.drop(columns=['buyPrice'])
    item50  = item50.sample(n=44)
    
    item51  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item51['buyPrice'].ge(1)
    item51  = item51[item51.buyPrice >= 1]
    item51  = item51.drop(columns=['buyPrice'])
    item51  = item51.sample(n=44)
    
    item52  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item52['buyPrice'].ge(1)
    item52  = item52[item52.buyPrice >= 1]
    item52  = item52.drop(columns=['buyPrice'])
    item52  = item52.sample(n=44)
    
    item53  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item53['buyPrice'].ge(1)
    item53  = item53[item53.buyPrice >= 1]
    item53  = item53.drop(columns=['buyPrice'])
    item53  = item53.sample(n=44)
    
    item54  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item54['buyPrice'].ge(1)
    item54  = item54[item54.buyPrice >= 1]
    item54  = item54.drop(columns=['buyPrice'])
    item54  = item54.sample(n=44)
    
    item55  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item55['buyPrice'].ge(1)
    item55  = item55[item55.buyPrice >= 1]
    item55  = item55.drop(columns=['buyPrice'])
    item55  = item55.sample(n=44)
    
    item56  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item56['buyPrice'].ge(1)
    item56  = item56[item56.buyPrice >= 1]
    item56  = item56.drop(columns=['buyPrice'])
    item56  = item56.sample(n=44)
    
    item57  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item57['buyPrice'].ge(1)
    item57  = item57[item57.buyPrice >= 1]
    item57  = item57.drop(columns=['buyPrice'])
    item57  = item57.sample(n=44)
    
    item58  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item58['buyPrice'].ge(1)
    item58  = item58[item58.buyPrice >= 1]
    item58  = item58.drop(columns=['buyPrice'])
    item58  = item58.sample(n=44)
    
    item59  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item59['buyPrice'].ge(1)
    item59  = item59[item59.buyPrice >= 1]
    item59  = item59.drop(columns=['buyPrice'])
    item59  = item59.sample(n=44)
    
    item60  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item60['buyPrice'].ge(1)
    item60  = item60[item60.buyPrice >= 1]
    item60  = item60.drop(columns=['buyPrice'])
    item60  = item60.sample(n=44)
    
    item61  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item61['buyPrice'].ge(1)
    item61  = item61[item61.buyPrice >= 1]
    item61  = item61.drop(columns=['buyPrice'])
    item61  = item61.sample(n=44)
    
    item62  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item62['buyPrice'].ge(1)
    item62  = item62[item62.buyPrice >= 1]
    item62  = item62.drop(columns=['buyPrice'])
    item62  = item62.sample(n=44)
    
    item63  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item63['buyPrice'].ge(1)
    item63  = item63[item63.buyPrice >= 1]
    item63  = item63.drop(columns=['buyPrice'])
    item63  = item63.sample(n=44)
    
    item64  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item64['buyPrice'].ge(1)
    item64  = item64[item64.buyPrice >= 1]
    item64  = item64.drop(columns=['buyPrice'])
    item64  = item64.sample(n=44)
    
    item65  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item65['buyPrice'].ge(1)
    item65  = item65[item65.buyPrice >= 1]
    item65  = item65.drop(columns=['buyPrice'])
    item65  = item65.sample(n=44)
    
    item66  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item66['buyPrice'].ge(1)
    item66  = item66[item66.buyPrice >= 1]
    item66  = item66.drop(columns=['buyPrice'])
    item66  = item66.sample(n=44)
    
    item67  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item67['buyPrice'].ge(1)
    item67  = item67[item67.buyPrice >= 1]
    item67  = item67.drop(columns=['buyPrice'])
    item67  = item67.sample(n=44)
    
    item68  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item68['buyPrice'].ge(1)
    item68  = item68[item68.buyPrice >= 1]
    item68  = item68.drop(columns=['buyPrice'])
    item68  = item68.sample(n=44)
    
    item69  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item69['buyPrice'].ge(1)
    item69  = item69[item69.buyPrice >= 1]
    item69  = item69.drop(columns=['buyPrice'])
    item69  = item69.sample(n=44)
    
    item70  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item70['buyPrice'].ge(1)
    item70  = item70[item70.buyPrice >= 1]
    item70  = item70.drop(columns=['buyPrice'])
    item70  = item70.sample(n=44)
    
    item71  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item71['buyPrice'].ge(1)
    item71  = item71[item71.buyPrice >= 1]
    item71  = item71.drop(columns=['buyPrice'])
    item71  = item71.sample(n=44)
    
    item72  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item72['buyPrice'].ge(1)
    item72  = item72[item72.buyPrice >= 1]
    item72  = item72.drop(columns=['buyPrice'])
    item72  = item72.sample(n=44)
    
    item73  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item73['buyPrice'].ge(1)
    item73  = item73[item73.buyPrice >= 1]
    item73  = item73.drop(columns=['buyPrice'])
    item73  = item73.sample(n=44)
    
    item74  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item74['buyPrice'].ge(1)
    item74  = item74[item74.buyPrice >= 1]
    item74  = item74.drop(columns=['buyPrice'])
    item74  = item74.sample(n=44)
    
    item75  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item75['buyPrice'].ge(1)
    item75  = item75[item75.buyPrice >= 1]
    item75  = item75.drop(columns=['buyPrice'])
    item75  = item75.sample(n=44)
    
    item76  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item76['buyPrice'].ge(1)
    item76  = item76[item76.buyPrice >= 1]
    item76  = item76.drop(columns=['buyPrice'])
    item76  = item76.sample(n=44)
    
    item77  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item77['buyPrice'].ge(1)
    item77  = item77[item77.buyPrice >= 1]
    item77  = item77.drop(columns=['buyPrice'])
    item77  = item77.sample(n=44)
    
    item78  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item78['buyPrice'].ge(1)
    item78  = item78[item78.buyPrice >= 1]
    item78  = item78.drop(columns=['buyPrice'])
    item78  = item78.sample(n=44)
    
    item79  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item79['buyPrice'].ge(1)
    item79  = item79[item79.buyPrice >= 1]
    item79  = item79.drop(columns=['buyPrice'])
    item79  = item79.sample(n=44)
    
    item80  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item80['buyPrice'].ge(1)
    item80  = item80[item80.buyPrice >= 1]
    item80  = item80.drop(columns=['buyPrice'])
    item80  = item80.sample(n=44)
    
    item81  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item81['buyPrice'].ge(1)
    item81  = item81[item81.buyPrice >= 1]
    item81  = item81.drop(columns=['buyPrice'])
    item81  = item81.sample(n=44)
    
    item82  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item82['buyPrice'].ge(1)
    item82  = item82[item82.buyPrice >= 1]
    item82  = item82.drop(columns=['buyPrice'])
    item82  = item82.sample(n=44)
    
    item83  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item83['buyPrice'].ge(1)
    item83  = item83[item83.buyPrice >= 1]
    item83  = item83.drop(columns=['buyPrice'])
    item83  = item83.sample(n=44)
    
    item84  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item84['buyPrice'].ge(1)
    item84  = item84[item84.buyPrice >= 1]
    item84  = item84.drop(columns=['buyPrice'])
    item84  = item84.sample(n=44)
    
    item85  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item85['buyPrice'].ge(1)
    item85  = item85[item85.buyPrice >= 1]
    item85  = item85.drop(columns=['buyPrice'])
    item85  = item85.sample(n=44)
    
    item86  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item86['buyPrice'].ge(1)
    item86  = item86[item86.buyPrice >= 1]
    item86  = item86.drop(columns=['buyPrice'])
    item86  = item86.sample(n=44)
    
    item87  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item87['buyPrice'].ge(1)
    item87  = item87[item87.buyPrice >= 1]
    item87  = item87.drop(columns=['buyPrice'])
    item87  = item87.sample(n=44)
    
    item88  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item88['buyPrice'].ge(1)
    item88  = item88[item88.buyPrice >= 1]
    item88  = item88.drop(columns=['buyPrice'])
    item88  = item88.sample(n=44)
    
    item89  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item89['buyPrice'].ge(1)
    item89  = item89[item89.buyPrice >= 1]
    item89  = item89.drop(columns=['buyPrice'])
    item89  = item89.sample(n=44)
    
    item90  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item90['buyPrice'].ge(1)
    item90  = item90[item90.buyPrice >= 1]
    item90  = item90.drop(columns=['buyPrice'])
    item90  = item90.sample(n=44)
    
    item91  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item91['buyPrice'].ge(1)
    item91  = item91[item91.buyPrice >= 1]
    item91  = item91.drop(columns=['buyPrice'])
    item91  = item91.sample(n=44)
    
    item92  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item92['buyPrice'].ge(1)
    item92  = item92[item92.buyPrice >= 1]
    item92  = item92.drop(columns=['buyPrice'])
    item92  = item92.sample(n=44)
    
    item93  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item93['buyPrice'].ge(1)
    item93  = item93[item93.buyPrice >= 1]
    item93  = item93.drop(columns=['buyPrice'])
    item93  = item93.sample(n=44)
    
    item94  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item94['buyPrice'].ge(1)
    item94  = item94[item94.buyPrice >= 1]
    item94  = item94.drop(columns=['buyPrice'])
    item94  = item94.sample(n=44)
    
    item95  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item95['buyPrice'].ge(1)
    item95  = item95[item95.buyPrice >= 1]
    item95  = item95.drop(columns=['buyPrice'])
    item95  = item95.sample(n=44)
    
    item96  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item96['buyPrice'].ge(1)
    item96  = item96[item96.buyPrice >= 1]
    item96  = item96.drop(columns=['buyPrice'])
    item96  = item96.sample(n=44)
    
    item97  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item97['buyPrice'].ge(1)
    item97  = item97[item97.buyPrice >= 1]
    item97  = item97.drop(columns=['buyPrice'])
    item97  = item97.sample(n=44)
    
    item98  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item98['buyPrice'].ge(1)
    item98  = item98[item98.buyPrice >= 1]
    item98  = item98.drop(columns=['buyPrice'])
    item98  = item98.sample(n=44)
    
    item99  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item99['buyPrice'].ge(1)
    item99  = item99[item99.buyPrice >= 1]
    item99  = item99.drop(columns=['buyPrice'])
    item99  = item99.sample(n=44)
    
    
    item100  = pandas.read_csv(item,usecols=["id","buyPrice"])
    item100['buyPrice'].ge(1)
    item100  = item100[item100.buyPrice >= 1]
    item100  = item100.drop(columns=['buyPrice'])
    item100  = item100.sample(n=44)
    

    # Open the csv file (File_Name)
    df = pandas.read_csv(file_name,index_col=["id","item1","item2","item3","item4","item5","item6","item7","item8","item9","item10","item11","item12","item13","item14","item15","item16","item17","item18","item19","item20","item21","item22","item23","item24","item25","item26","item27","item28","item29","item30","item31","item32","item33","item34","item35","item36","item37","item38","item39","item40","item41","item42","item43","item44","item45","item46","item47","item48","item49","item50","item51","item52","item53","item54","item55","item56","item57","item58","item59","item60","item61","item62","item63","item64","item65","item66","item67","item68","item69","item70","item71","item72","item73","item74","item75","item76","item77","item78","item79","item80","item81","item82","item83","item84","item85","item86","item87","item88","item89","item90","item91","item92","item93","item94","item95","item96","item97","item98","item99","item100"]).sample(frac=1, ignore_index=True)

    # Inserts Colums
    df.insert(loc=0, column="id", value=pandas.read_csv(file_name)["id"])
    df.insert(loc=1, column="item1", value= item1)
    df.insert(loc=2, column="item2", value= item2)
    df.insert(loc=3, column="item3", value= item3)
    df.insert(loc=4, column="item4", value= item4)
    df.insert(loc=5, column="item5", value= item5)
    df.insert(loc=6, column="item6", value= item6)
    df.insert(loc=7, column="item7", value= item7)
    df.insert(loc=8, column="item8", value= item8)
    df.insert(loc=9, column="item9", value= item9)
    df.insert(loc=10, column="item10", value= item10)
    time.sleep(0.2)

    df.insert(loc=11, column="item11", value= item11)
    df.insert(loc=12, column="item12", value= item12)
    df.insert(loc=13, column="item13", value= item13)
    df.insert(loc=14, column="item14", value= item14)
    df.insert(loc=15, column="item15", value= item15)
    df.insert(loc=16, column="item16", value= item16)
    df.insert(loc=17, column="item17", value= item17)
    df.insert(loc=18, column="item18", value= item18)
    df.insert(loc=19, column="item19", value= item19)
    df.insert(loc=20, column="item20", value= item20)
    time.sleep(0.2)

    df.insert(loc=21, column="item21", value= item21)
    df.insert(loc=22, column="item22", value= item22)
    df.insert(loc=23, column="item23", value= item23)
    df.insert(loc=24, column="item24", value= item24)
    df.insert(loc=25, column="item25", value= item25)
    df.insert(loc=26, column="item26", value= item26)
    df.insert(loc=27, column="item27", value= item27)
    df.insert(loc=28, column="item28", value= item28)
    df.insert(loc=29, column="item29", value= item29)
    df.insert(loc=30, column="item30", value= item30)
    time.sleep(0.2)

    df.insert(loc=31, column="item31", value= item31)
    df.insert(loc=32, column="item32", value= item32)
    df.insert(loc=33, column="item33", value= item33)
    df.insert(loc=34, column="item34", value= item34)
    df.insert(loc=35, column="item35", value= item35)
    df.insert(loc=36, column="item36", value= item36)
    df.insert(loc=37, column="item37", value= item37)
    df.insert(loc=38, column="item38", value= item38)
    df.insert(loc=39, column="item39", value= item39)
    df.insert(loc=40, column="item40", value= item40)
    time.sleep(0.2)

    df.insert(loc=41, column="item41", value= item41)
    df.insert(loc=42, column="item42", value= item42)
    df.insert(loc=43, column="item43", value= item43)
    df.insert(loc=44, column="item44", value= item44)
    df.insert(loc=45, column="item45", value= item45)
    df.insert(loc=46, column="item46", value= item46)
    df.insert(loc=47, column="item47", value= item47)
    df.insert(loc=48, column="item48", value= item48)
    df.insert(loc=49, column="item49", value= item49)
    df.insert(loc=50, column="item50", value= item50)
    time.sleep(0.2)

    df.insert(loc=51, column="item51", value= item51)
    df.insert(loc=52, column="item52", value= item52)
    df.insert(loc=53, column="item53", value= item53)
    df.insert(loc=54, column="item54", value= item54)
    df.insert(loc=55, column="item55", value= item55)
    df.insert(loc=56, column="item56", value= item56)
    df.insert(loc=57, column="item57", value= item57)
    df.insert(loc=58, column="item58", value= item58)
    df.insert(loc=59, column="item59", value= item59)
    df.insert(loc=60, column="item60", value= item60)
    time.sleep(0.2)

    df.insert(loc=61, column="item61", value= item61)
    df.insert(loc=62, column="item62", value= item62)
    df.insert(loc=63, column="item63", value= item63)
    df.insert(loc=64, column="item64", value= item64)
    df.insert(loc=65, column="item65", value= item65)
    df.insert(loc=66, column="item66", value= item66)
    df.insert(loc=67, column="item67", value= item67)
    df.insert(loc=68, column="item68", value= item68)
    df.insert(loc=69, column="item69", value= item69)
    df.insert(loc=70, column="item70", value= item70)
    time.sleep(0.2)

    df.insert(loc=71, column="item71", value= item71)
    df.insert(loc=72, column="item72", value= item72)
    df.insert(loc=73, column="item73", value= item73)
    df.insert(loc=74, column="item74", value= item74)
    df.insert(loc=75, column="item75", value= item75)
    df.insert(loc=76, column="item76", value= item76)
    df.insert(loc=77, column="item77", value= item77)
    df.insert(loc=78, column="item78", value= item78)
    df.insert(loc=79, column="item79", value= item79)
    df.insert(loc=80, column="item80", value= item80)
    time.sleep(0.2)

    df.insert(loc=81, column="item81", value= item81)
    df.insert(loc=82, column="item82", value= item82)
    df.insert(loc=83, column="item83", value= item83)
    df.insert(loc=84, column="item84", value= item84)
    df.insert(loc=85, column="item85", value= item85)
    df.insert(loc=86, column="item86", value= item86)
    df.insert(loc=87, column="item87", value= item87)
    df.insert(loc=88, column="item88", value= item88)
    df.insert(loc=89, column="item89", value= item89)
    df.insert(loc=90, column="item90", value= item90)
    time.sleep(0.2)

    df.insert(loc=91, column="item91", value= item91)
    df.insert(loc=92, column="item92", value= item92)
    df.insert(loc=93, column="item93", value= item93)
    df.insert(loc=94, column="item94", value= item94)
    df.insert(loc=95, column="item95", value= item95)
    df.insert(loc=96, column="item96", value= item96)
    df.insert(loc=97, column="item97", value= item97)
    df.insert(loc=98, column="item98", value= item98)
    df.insert(loc=99, column="item99", value= item99)
    df.insert(loc=100, column="item100", value= item100)
    time.sleep(0.2)


    # Saves the Randomized File
    df.to_csv(file_name, index=False)
    shutil.make_archive(output_filename, 'zip', dir_name)