import pandas as pd

#array in order: normal, fighting, flying, poison, ground, 
#rock, bug, ghost, steel, fire, water, grass, electric
#psychic, ice, dragon, dark, fairy

#----------types to be listed in terms of defensive capabilities----------
normal =   [1,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]
fighting = [1,1,2,1,1,0.5,0.5,1,1,1,1,1,1,2,1,1,0.5,2]
flying =   [1,0.5,1,1,0,2,0.5,1,1,1,1,0.5,2,1,2,1,1,1,1]
poison =   [1,0.5,1,0.5,2,1,0.5,1,1,1,1,0.5,1,2,1,1,1,0.5]
ground=    [1,1,1,0.5,1,0.5,1,1,1,1,2,2,0,1,2,1,1,1]
rock=      [0.5,2,0.5,0.5,2,1,1,1,2,0.5,2,2,1,1,1,1,1,1]
bug=       [1,0.5,2,1,0.5,2,1,1,1,2,1,0.5,1,1,1,1,1,1]
ghost=     [0,0,1,0.5,1,1,0.5,2,1,1,1,1,1,1,1,1,2,1]
steel =    [0.5,2,0.5,0,2,0.5,0.5,1,0.5,2,1,0.5,1,0.5,0.5,0.5,1,0.5]
fire=      [1,1,1,1,2,2,0.5,1,0.5,0.5,2,0.5,1,1,0.5,1,1,0.5]
water=     [1,1,1,1,1,1,1,1,0.5,0.5,0.5,2,2,1,0.5,1,1,1]
grass=     [1,1,2,2,0.5,1,2,1,1,2,0.5,0.5,0.5,1,2,1,1,1]
electric=  [1,1,0.5,1,2,1,1,1,0.5,1,1,1,0.5,1,1,1,1,1]
psychic=   [1,0.5,1,1,1,1,2,2,1,1,1,1,1,0.5,1,1,2,1]
ice=       [1,2,1,1,1,2,1,1,2,2,1,1,1,1,0.5,1,1,1]
dragon=    [1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,1,2,2,1,2]
dark =     [1,2,1,1,1,1,2,0.5,1,1,1,1,1,0,1,1,0.5,2]
fairy=     [1,0.5,1,2,1,1,0.5,1,2,1,1,1,1,1,1,0,0.5,1]
nil =      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


typesdict={'normal':normal,'fighting':fighting,'flying':flying,'poison':poison,'ground':ground,'rock':rock,'bug':bug,'ghost':ghost,
'steel':steel,'fire':fire,'water':water,'grass':grass,'electric':electric,'psychic':psychic,'ice':ice,'dragon':dragon,'dark':dark,
'fairy':fairy,'nil':nil}
#--------------------------------------------------------------------------
#empty lists to record down the specific pokemon's type effectiveness, used for pandas
pdnormal = []
pdfighting = []
pdflying = []
pdpoison = []
pdground = []
pdrock = []
pdbug = []
pdghost = []
pdsteel = []
pdfire = []
pdwater = []
pdgrass = []
pdelectric = []
pdpsychic = []
pdice = []
pddragon = []
pddark = []
pdfairy = []
totaltypelist = [pdnormal,pdfighting,pdflying,pdpoison,pdground,pdrock,pdbug,pdghost,pdsteel,pdfire,pdwater,pdgrass,pdelectric,pdpsychic,pdice,pddragon,pddark,pdfairy] #a list to hold the type vulnerability of each type of each pokemon
#--------------------------------------------------------------------------
#function for type effectiveness calculation
def typecalculation():
#function to determine what type it is based on user's input
    def typeinput():
        while True:
            typestring = input("Enter type "+typenostring+' (type "nil" if there is no type):')
            if(typestring.lower() in typesdict):
                pokemontype = typesdict[typestring.lower()]
            else:
                print("Invalid type. Enter again.")
                continue
            #repeat the loop until a valid condition is met
            break
        if(typeno == 0):
            type1list.append(typestring) #append to list of type 1
        elif(typeno == 1):
            type2list.append(typestring) #append to list of type 2
        return pokemontype
#--------------------------------------------------------------------------
    #ability calculation
    def typeability():
        if (ability == "levitate"):
            typetotal[4] = 0
            #ground is 0
        if (ability == "volt absorb" or ability == "lightning rod" or ability == "motor drive"):
            typetotal[12] = 0
            #electric is 0
        if (ability == "flash fire"):
            typetotal[9] = 0
            #fire is 0
        if (ability == "storm drain" or ability == "water absorb"):
            typetotal[10] = 0
            #water is 0
        if (ability == "sap sipper"):
            typetotal[11] = 0
            #grass is 0
        if (ability == "heatproof"):
            typetotal[9] = typetotal[9]*0.5
            #fire is halved
        if (ability == "thick fat"):
            typetotal[9] = typetotal[9]*0.5
            typetotal[14] = typetotal[14]*0.5
            #fire and ice are halved
        if (ability == "dry skin"):
            typetotal[9] = typetotal[9]*1.25
            typetotal[10] = 0
            #fire is 1.25x, water is 0
    
#--------------------------------------------------------------------------
    typelist =[]#raw data for collecting the 2 types

    #collect 2 types
    for typeno in range(2):
        typenostring = str(typeno+1)
        pokemontype = typeinput()
        typelist.append(pokemontype)

    #assign the list to their respective types
    type1 = typelist[0]
    type2 = typelist[1]
    
    #total type effectiveness of the pokemon
    typetotal = []
    for num1,num2 in zip(type1,type2):
        typetotal.append(num1*num2)
    ability = input("Enter ability: ")
    pokemonability = typeability()
    abilitylist.append(ability) #append to list of abilities
    return(typetotal)
#--------------------------------------------------------------------------

#empty lists for append
pokemonnames = []
pokemontypetotal = []
type1list = []
type2list = []
abilitylist = []
pokemondata = {'Normal':pdnormal,'Fighting':pdfighting,'Flying':pdflying,'Poison':pdpoison,'Ground':pdground,'Rock':pdrock,
'Bug':pdbug,'Ghost':pdghost,'Steel':pdsteel,'Fire':pdfire,'Water':pdwater,'Grass':pdgrass,'Electric':pdelectric,'Psychic':pdpsychic,
'Ice':pdice,'Dragon':pddragon,'Dark':pddark,'Fairy':pdfairy}
typenamelist = ['Normal','Fighting','Flying','Poison','Ground','Rock','Bug','Ghost','Steel','Fire','Water','Grass','Electric','Psychic','Ice','Dragon','Dark','Fairy']

pokemoncounterstr = input("Number of Pokemon: ") #how many pokemon in the team
pokemoncounter = int(pokemoncounterstr)

#declaring each of the pokemon
for pokemonno in range(pokemoncounter):
    pokemonnostring = str(pokemonno+1)
    pokemonname = input("Pokemon " + pokemonnostring + " name:")
    typetotal = typecalculation()
    pokemonnames.append(pokemonname)
    pokemontypetotal.append(typetotal) #list of total type effectiveness per pokemon
    for i in range(len(typetotal)):
        listplaceholder = totaltypelist[i]
        listplaceholder.append(typetotal[i])

#adding total type effectiveness of whole team
typetotalfinal = []
for items in zip(*pokemontypetotal):
    sumitems = sum(items)
    typetotalfinal.append(sumitems)
for i in range(len(typetotalfinal)):
    listplaceholder = totaltypelist[i]
    listplaceholder.append(typetotalfinal[i])
pokemonnames.append('Total')


df = pd.DataFrame(pokemondata,columns = typenamelist,index = pokemonnames)

csvname = input("Save spreadsheetname: ")
df.to_csv(csvname+".csv")
print("csv printed.")
