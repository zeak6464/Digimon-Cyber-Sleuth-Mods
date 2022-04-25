import csv
from tkinter import *
from PIL import Image, ImageTk

filepath = "./digimondata.csv"

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])

list_of_entries = []
for x in list(range(0,len(Data))):
	list_of_entries.append(Data[x][0])

root = Tk()
root.title('Digimon Data Reader')
root.geometry('475x800')
var = StringVar(value = list_of_entries)
listbox1 = Listbox(root, listvariable = var)
listbox1.grid(row=0 , column=0)
canvas = Canvas(root, width = 300, height = 300)  
canvas.grid(row=0,column=1, columnspan=2)
img=PhotoImage(file='images/'+Data[index][0]+'.png')
image_container = canvas.create_image(0,0, anchor=NW, image=img)

def update():
    index = listbox1.curselection()[0]
    idlabel2.config(text = Data[index][0])
    canvas.itemconfig(image_container,image=img)
    memoryuselabel2.config(text = Data[index][1])
    growthTypelabel2.config(text = Data[index][2])
    unk3label2.config(text = Data[index][3])
    baseHPlabel2.config(text = Data[index][4])
    baseSPlabel2.config(text = Data[index][5])
    baseATKlabel2.config(text = Data[index][6])
    baseDEFlabel2.config(text = Data[index][7])
    baseINTlabel2.config(text = Data[index][8])
    baseSPDlabel2.config(text = Data[index][9])
    maxLevellabel2.config(text = Data[index][10])
    equipSlotslabel2.config(text = Data[index][11])
    supportSkilllabel2.config(text = Data[index][12])
    sMove1label2.config(text = Data[index][13])
    sMove1Levellabel2.config(text = Data[index][14])
    sMove2label2.config(text = Data[index][15])
    sMove2Levellabel2.config(text = Data[index][16])
    move1label2.config(text = Data[index][17])
    move1Levellabel2.config(text = Data[index][18])
    move2label2.config(text = Data[index][19])
    move2Levellabel2.config(text = Data[index][20])
    move3label2.config(text = Data[index][21])
    move3Levellabel2.config(text = Data[index][22])
    move4label2.config(text = Data[index][23])
    move4Levellabel2.config(text = Data[index][24])
    move5label2.config(text = Data[index][25])
    move5Levellabel2.config(text = Data[index][26])
    move6label2.config(text = Data[index][27])
    move6Levellabel2.config(text = Data[index][28])
    expValuelabel2.config(text = Data[index][29])
    levelCurvelabel2.config(text = Data[index][30])
    profilelabel2.config(text = Data[index][31])
    unk32label2.config(text = Data[index][32])
    unk33label2.config(text = Data[index][33])
    return None




button1 = Button(root, text="Update", command=update)
button1.grid(row=35, column=1)

idlabel = Label(root, text="Id").grid(row=1, column=0,sticky="w")
memoryuselabel = Label(root, text="memoryUse").grid(row=2, column=0,sticky="w")
growthTypelabel = Label(root, text="growthType").grid(row=3, column=0,sticky="w")
unk3label = Label(root, text="unknown").grid(row=4, column=0,sticky="w")
baseHPlabel = Label(root, text="baseHP").grid(row=5, column=0,sticky="w")
baseSPlabel = Label(root, text="baseSP").grid(row=6, column=0,sticky="w")
baseATKlabel = Label(root, text="baseATK").grid(row=7, column=0,sticky="w")
baseDEFlabel = Label(root, text="baseDEF").grid(row=8, column=0,sticky="w")
baseINTlabel = Label(root, text="baseINT").grid(row=9, column=0,sticky="w")
baseSPDlabel = Label(root, text="baseSPD").grid(row=10, column=0,sticky="w")
maxLevellabel = Label(root, text="maxLevel").grid(row=11, column=0,sticky="w")
equipSlotslabel = Label(root, text="equipSlots").grid(row=12, column=0,sticky="w")
supportSkilllabel = Label(root, text="supportSkilll").grid(row=13, column=0,sticky="w")
sMove1label = Label(root, text="sMove1").grid(row=14, column=0,sticky="w")
sMove1Levellabel = Label(root, text="sMove1Level").grid(row=15, column=0,sticky="w")
sMove2label = Label(root, text="sMove2").grid(row=16, column=0,sticky="w")
sMove2Levellabel = Label(root, text="sMove2Level").grid(row=17, column=0,sticky="w")
move1label = Label(root, text="move1").grid(row=18, column=0,sticky="w")
move1Levellabel = Label(root, text="move1Level").grid(row=19, column=0,sticky="w")
move2label = Label(root, text="move2").grid(row=20, column=0,sticky="w")
move2Levellabel = Label(root, text="move2Level").grid(row=21, column=0,sticky="w")

move3label = Label(root, text="move3").grid(row=1, column=2,sticky="w")
move3Levellabel = Label(root, text="move3Level").grid(row=2, column=2,sticky="w")
move4label = Label(root, text="move4").grid(row=3, column=2,sticky="w")
move4Levellabel = Label(root, text="move4Level").grid(row=4, column=2,sticky="w")
move5label = Label(root, text="move5").grid(row=5, column=2,sticky="w")
move5Levellabel = Label(root, text="move5Level").grid(row=6, column=2,sticky="w")
move6label = Label(root, text="move6").grid(row=7, column=2,sticky="w")
move6Levellabel = Label(root, text="move6Level").grid(row=8, column=2,sticky="w")
expValuelabel = Label(root, text="expValue").grid(row=9, column=2,sticky="w")
levelCurvelabel = Label(root, text="levelCurve").grid(row=10, column=2,sticky="w")
profilelabel = Label(root, text="profile").grid(row=11, column=2,sticky="w")
unk32label = Label(root, text="unknown").grid(row=12, column=2,sticky="w")
unk33label = Label(root, text="unknown").grid(row=13, column=2,sticky="w")


idlabel2 = Label(root, text="")
idlabel2.grid(row=1, column=1,sticky="w")


memoryuselabel2 = Label(root, text="")
memoryuselabel2.grid(row=2, column=1,sticky="w")

growthTypelabel2 = Label(root, text="")
growthTypelabel2.grid(row=3, column=1,sticky="w")

unk3label2 = Label(root, text="")
unk3label2.grid(row=4, column=1,sticky="w")

baseHPlabel2 = Label(root, text="")
baseHPlabel2.grid(row=5, column=1,sticky="w")

baseSPlabel2 = Label(root, text="")
baseSPlabel2.grid(row=6, column=1,sticky="w")

baseATKlabel2 = Label(root, text="")
baseATKlabel2.grid(row=7, column=1,sticky="w")

baseDEFlabel2 = Label(root, text="")
baseDEFlabel2.grid(row=8, column=1,sticky="w")

baseINTlabel2 = Label(root, text="")
baseINTlabel2.grid(row=9, column=1,sticky="w")

baseSPDlabel2 = Label(root, text="")
baseSPDlabel2.grid(row=10, column=1,sticky="w")

maxLevellabel2 = Label(root, text="")
maxLevellabel2.grid(row=11, column=1,sticky="w")

equipSlotslabel2 = Label(root, text="")
equipSlotslabel2.grid(row=12, column=1,sticky="w")

supportSkilllabel2 = Label(root, text="")
supportSkilllabel2.grid(row=13, column=1,sticky="w")

sMove1label2 = Label(root, text="")
sMove1label2.grid(row=14, column=1,sticky="w")

sMove1Levellabel2 = Label(root, text="")
sMove1Levellabel2.grid(row=15, column=1,sticky="w")

sMove2label2 = Label(root, text="")
sMove2label2.grid(row=16, column=1,sticky="w")

sMove2Levellabel2 = Label(root, text="")
sMove2Levellabel2.grid(row=17, column=1,sticky="w")

move1label2 = Label(root, text="")
move1label2.grid(row=18, column=1,sticky="w")

move1Levellabel2 = Label(root, text="")
move1Levellabel2.grid(row=19, column=1,sticky="w")

move2label2 = Label(root, text="")
move2label2.grid(row=20, column=1,sticky="w")

move2Levellabel2 = Label(root, text="")
move2Levellabel2.grid(row=21, column=1,sticky="w")

move3label2 = Label(root, text="")
move3label2.grid(row=1, column=4,sticky="w")

move3Levellabel2 = Label(root, text="")
move3Levellabel2.grid(row=2, column=4,sticky="w")

move4label2 = Label(root, text="")
move4label2.grid(row=3, column=4,sticky="w")

move4Levellabel2 = Label(root, text="")
move4Levellabel2.grid(row=4, column=4,sticky="w")

move5label2 = Label(root, text="")
move5label2.grid(row=5, column=4,sticky="w")

move5Levellabel2 = Label(root, text="")
move5Levellabel2.grid(row=6, column=4,sticky="w")

move6label2 = Label(root, text="")
move6label2.grid(row=7, column=4,sticky="w")

move6Levellabel2 = Label(root, text="")
move6Levellabel2.grid(row=8, column=4,sticky="w")

expValuelabel2 = Label(root, text="")
expValuelabel2.grid(row=9, column=4,sticky="w")

levelCurvelabel2 = Label(root, text="")
levelCurvelabel2.grid(row=10, column=4,sticky="w")

profilelabel2 = Label(root, text="")
profilelabel2.grid(row=11, column=4,sticky="w")

unk32label2 = Label(root, text="")
unk32label2.grid(row=12, column=4,sticky="w")

unk33label2 = Label(root, text="")
unk33label2.grid(row=13, column=4,sticky="w")



root.mainloop()
