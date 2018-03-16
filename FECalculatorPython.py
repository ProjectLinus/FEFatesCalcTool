from Character import Character
from operator import itemgetter
from Stats import Stats
from GameBools import GameBools
from UnitClass import UnitClass
from tabulate import tabulate



def initData(strfile):

    populatefile = open(strfile,"r");
    populatefileLines = list(populatefile);
    populatefile.close();

    classDict = {}
    characterDict = {}

    for i in populatefileLines:
        if("insert into class_growths values" in i):
            classGrowthLine = i[34:]
            classGrowthLine = classGrowthLine[:-3]
            classGrowthValueList = classGrowthLine.split(",")
            className = classGrowthValueList[0]
            classHp = classGrowthValueList[1]
            classStr = classGrowthValueList[2]
            classMag = classGrowthValueList[3]
            classSkl = classGrowthValueList[4]
            classSpd = classGrowthValueList[5]
            classLck = classGrowthValueList[6]
            classDef = classGrowthValueList[7]
            classRes = classGrowthValueList[8]
            classAdvClass = classGrowthValueList[9]
            classStats = Stats(classHp,classStr,classMag,classSkl,classSpd,classLck,classDef,classRes)
            classDict[className] = UnitClass(classStats,className,classAdvClass);

        elif("insert into character_growths values" in i):
            characterGrowthLine = i[38:]
            characterGrowthLine = characterGrowthLine[:-3]
            characterGrowthValueList = characterGrowthLine.split(",");
            characterName = characterGrowthValueList[0]
            characterHp = characterGrowthValueList[1]
            characterStr = characterGrowthValueList[2]
            characterMag = characterGrowthValueList[3]
            characterSkl = characterGrowthValueList[4]
            characterSpd = characterGrowthValueList[5]
            characterLck = characterGrowthValueList[6]
            characterDef = characterGrowthValueList[7]
            characterRes = characterGrowthValueList[8]
            characterStats = Stats(characterHp,characterStr,characterMag,characterSkl,characterSpd,characterLck,characterDef,characterRes)
            characterDict[characterName] = Character(characterStats,characterName)

        elif("insert into character_base_stats values" in i):
            line = i[41:]
            line = line[:-2]
            lineList = line.split(",");
            characterName = lineList[0]
            gameBool = lineList[-1]
            if(characterName in characterDict):
                character = characterDict[characterName]
                if(gameBool == "B"):
                    character.setBirthright(True)
                elif(gameBool == "C"):
                    character.setConquest(True)
                elif(gameBool == "R"):
                    character.setRevelations(True)
                characterDict[characterName] = character

    return (classDict,characterDict)



def stat_menu(tableArray):

    statMenu = {}
    statMenu["0"] = "Return"
    statMenu["1"] = "Sort by HP"
    statMenu["2"] = "Sort by STR"
    statMenu["3"] = "Sort by MAG"
    statMenu["4"] = "Sort by SKL"
    statMenu["5"] = "Sort by SPD"
    statMenu["6"] = "Sort by LCK"
    statMenu["7"] = "Sort by DEF"
    statMenu["8"] = "Sort by RES"

    sortedTableArray = tableArray;
    sortOptions = statMenu.keys();
    for sta1 in sortOptions:
        print(sta1 + ":" + statMenu[sta1]);
    select2 = input("Choose an option: ");
    if(select2 == "0"):
        print("Returning...");
        return sortedTableArray;
    elif((int(select2) > 0) and (int(select2) < 9)):
        sortedTableArray = sorted(tableArray,key=itemgetter(int(select2)+1), reverse=True);
        return sortedTableArray
    else:
        print("Error: Invalid option entered.");
        return sortedTableArray

def low_constraint_menu():

    constraintMinMenu = {}
    constraintMinMenu["0"] = "Return"
    constraintMinMenu["1"] = "Set HP Lower Constraint"
    constraintMinMenu["2"] = "Set STR Lower Constraint"
    constraintMinMenu["3"] = "Set MAG Lower Constraint"
    constraintMinMenu["4"] = "Set SKL Lower Constraint"
    constraintMinMenu["5"] = "Set SPD Lower Constraint"
    constraintMinMenu["6"] = "Set LCK Lower Constraint"
    constraintMinMenu["7"] = "Set DEF Lower Constraint"
    constraintMinMenu["8"] = "Set RES Lower Constraint"

    options = constraintMinMenu.keys();
    for option in options:
        print(option + ":" + constraintMinMenu[option]);
    select = input("Choose an option: ")
    if(select == "0"):
        print("Returning...");
        return (-1,-1)
    elif((int(select) > 0) and (int(select) < 9)):
        constraintValue = constraint_prompt()
        if(constraintValue != -1):
            return (int(select)-1, constraintValue)
    else:
        print("Error: Invalid option entered.");
        return (-1,-1)



def high_constraint_menu():

    constraintMaxMenu = {}
    constraintMaxMenu["0"] = "Return"
    constraintMaxMenu["1"] = "Set HP Higher Constraint"
    constraintMaxMenu["2"] = "Set STR Higher Constraint"
    constraintMaxMenu["3"] = "Set MAG Higher Constraint"
    constraintMaxMenu["4"] = "Set SKL Higher Constraint"
    constraintMaxMenu["5"] = "Set SPD Higher Constraint"
    constraintMaxMenu["6"] = "Set LCK Higher Constraint"
    constraintMaxMenu["7"] = "Set DEF Higher Constraint"
    constraintMaxMenu["8"] = "Set RES Higher Constraint"

    options = constraintMaxMenu.keys();
    for option in options:
        print(option + ":" + constraintMaxMenu[option]);
    select = input("Choose an option: ")
    if(select == "0"):
        print("Returning...");
        return (-1,-1)
    elif((int(select) > 0) and (int(select) < 9)):
        constraintValue = constraint_prompt()
        if(constraintValue != -1):
            return (int(select)-1, constraintValue)
    else:
        print("Error: Invalid option entered.");
        return (-1,-1)



def constraint_prompt():
    value = input("Please enter the % of the stat to filter (between 0 and 100): ")
    if(int(value) >= 0 and int(value) <= 100):
        return int(value);
    else:
        print("Error: Invalid value entered.");
        return -1;
        


def display_constraints(minConstraints,maxConstraints):
    print("\n")
    print("Current constraints are as follows:");
    print(tabulate([minConstraints,maxConstraints],headers=['HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']))
    print("\n")

def createUnitValueArray(inputName,dictValue,searchresultStats):
    unitValues = []
    unitValues.append(inputName)
    unitValues.append(dictValue.getName())
    unitValues.append(int(dictValue.getGrowthRates().getHp()) + searchresultStats[0])
    unitValues.append(int(dictValue.getGrowthRates().getStr()) + searchresultStats[1])
    unitValues.append(int(dictValue.getGrowthRates().getMag()) + searchresultStats[2])
    unitValues.append(int(dictValue.getGrowthRates().getSkl()) + searchresultStats[3])
    unitValues.append(int(dictValue.getGrowthRates().getSpd()) + searchresultStats[4])
    unitValues.append(int(dictValue.getGrowthRates().getLck()) + searchresultStats[5])
    unitValues.append(int(dictValue.getGrowthRates().getDefe()) + searchresultStats[6])
    unitValues.append(int(dictValue.getGrowthRates().getRes()) + searchresultStats[7])
    return unitValues;

def checkConstraints(unitValues,minConstraints,maxConstraints):
    for i in range(0,len(unitValues)):
        if((unitValues[i] < minConstraints[i]) or (unitValues[i] > maxConstraints[i])):
            return False
    return True


def updateTableArray(unitDict, inputName, searchDict, minConstraints, maxConstraints):

    tableArray = []
    searchresult = searchDict[inputName];
    searchresultStats = [int(searchresult.getGrowthRates().getHp()),int(searchresult.getGrowthRates().getStr()),int(searchresult.getGrowthRates().getMag()),int(searchresult.getGrowthRates().getSkl()),int(searchresult.getGrowthRates().getSpd()),int(searchresult.getGrowthRates().getLck()),int(searchresult.getGrowthRates().getDefe()),int(searchresult.getGrowthRates().getRes())]    
                
    for unit in unitDict.keys():
        unitDictValue = unitDict[unit]
        unitValues = createUnitValueArray(inputName,unitDictValue,searchresultStats)
        if(checkConstraints(unitValues[2:],minConstraints,maxConstraints)):
            tableArray.append(unitValues)
    return tableArray


def generateTableArrayAllCombos(characterDict,classDict,minConstraints,maxConstraints):
    tableArray = [];
    for characterInDict in characterDict.keys():
        searchresult = characterDict[characterInDict];
        searchresultStats = [int(searchresult.getGrowthRates().getHp()),int(searchresult.getGrowthRates().getStr()),int(searchresult.getGrowthRates().getMag()),int(searchresult.getGrowthRates().getSkl()),int(searchresult.getGrowthRates().getSpd()),int(searchresult.getGrowthRates().getLck()),int(searchresult.getGrowthRates().getDefe()),int(searchresult.getGrowthRates().getRes())]
        for unit in classDict.keys():
            unitDictValue = classDict[unit]
            unitValues = createUnitValueArray(characterInDict,unitDictValue,searchresultStats)
            if(checkConstraints(unitValues[2:],minConstraints,maxConstraints)):
                tableArray.append(unitValues)
    return tableArray



def main():
    dictTuple = initData("populate.txt");
    classDict = dictTuple[0];
    characterDict = dictTuple[1];

    minConstraints = [0,0,0,0,0,0,0,0]
    maxConstraints = [100,100,100,100,100,100,100,100]

    menu = {};
    menu["0"] = "Exit";
    menu["1"] = "Search by Class"
    menu["2"] = "Search by Character"
    menu["3"] = "Show Every Combi"
    menu["4"] = "Set Lower Constraints"
    menu["5"] = "Set Higher Constraints"
    menu["6"] = "Reset Constraints"
    #menu["3"] = "Set Games"
    #menu["4"] = "Exclude Basic Classes"

    classMenu = {}
    classMenu["0"] = "Return"
    classMenu["1"] = "Sort by Stat"
    classMenu["2"] = "Set Lower Constraints"
    classMenu["3"] = "Set Higher Constraints"

    characterMenu = {}
    characterMenu["0"] = "Return"
    characterMenu["1"] = "Sort by Stat"
    characterMenu["2"] = "Set Lower Constraints"
    characterMenu["3"] = "Set Higher Constraints"



    while(1):
        display_constraints(minConstraints,maxConstraints);
        menuOptions = menu.keys();
        for i in menuOptions:
            print(i + ":" + menu[i]);
        select = input("Choose an option: ");

        if(select == "0"):
            print("Exiting...");
            break;

        elif(select == "1"):
            unitClass = input("Class to search for: ");
            if(unitClass in classDict.keys()):
                tableArray = updateTableArray(characterDict,unitClass,classDict,minConstraints,maxConstraints);
                print(tabulate(tableArray, headers=['Class Name', 'Character', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                while(1):
                    display_constraints(minConstraints,maxConstraints);
                    classOptions = classMenu.keys();
                    for cla1 in classOptions:
                        print(cla1 + ":" + classMenu[cla1]);
                    select1 = input("Choose an option: ");
                    if(select1 == "0"):
                        print("Returning...");
                        break;
                    elif(select1 == "1"):
                        tableArray = updateTableArray(characterDict,unitClass,classDict,minConstraints,maxConstraints);
                        sortedTableArray = stat_menu(tableArray)
                        print(tabulate(sortedTableArray, headers=['Class Name', 'Character', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                    elif(select1 == "2"):
                        constraintMinResults = low_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
                        if((constraintMinResults[0] != -1) and (constraintMinResults[1] != -1)):
                            minConstraints[constraintMinResults[0]] = constraintMinResults[1];
                            tableArray = updateTableArray(characterDict,unitClass,classDict,minConstraints,maxConstraints);
                            print(tabulate(tableArray, headers=['Class Name', 'Character', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                    elif(select1 == "3"):
                        constraintMaxResults = high_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
                        if((constraintMaxResults[0] != -1) and (constraintMaxResults[1] != -1)):
                            maxConstraints[constraintMaxResults[0]] = constraintMaxResults[1];
                            tableArray = updateTableArray(characterDict,unitClass,classDict,minConstraints,maxConstraints);
                            print(tabulate(tableArray, headers=['Class Name', 'Character', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));

            else:
                print("Class not found. Please try again.");


        elif(select == "2"):
            characterSelected = input("Character to search for: ");
            if(characterSelected in characterDict.keys()):   
                tableArray = updateTableArray(classDict,characterSelected,characterDict,minConstraints,maxConstraints);
                print(tabulate(tableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                while(1):
                    display_constraints(minConstraints,maxConstraints);
                    charOptions = characterMenu.keys();
                    for char1 in charOptions:
                        print(char1 + ":" + characterMenu[char1]);
                    select4 = input("Choose an option: ");
                    if(select4 == "0"):
                        print("Returning...");
                        break;
                    elif(select4 == "1"):
                        tableArray = updateTableArray(classDict,characterSelected,characterDict,minConstraints,maxConstraints);
                        sortedTableArray = stat_menu(tableArray)
                        print(tabulate(sortedTableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                    elif(select4 == "2"):
                        constraintMinResults = low_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
                        if((constraintMinResults[0] != -1) and (constraintMinResults[1] != -1)):
                            minConstraints[constraintMinResults[0]] = constraintMinResults[1];
                            tableArray = updateTableArray(classDict,characterSelected,characterDict,minConstraints,maxConstraints);
                            print(tabulate(tableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                    elif(select4 == "3"):
                        constraintMaxResults = high_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
                        if((constraintMaxResults[0] != -1) and (constraintMaxResults[1] != -1)):
                            maxConstraints[constraintMaxResults[0]] = constraintMaxResults[1];
                            tableArray = updateTableArray(classDict,characterSelected,characterDict,minConstraints,maxConstraints);
                            print(tabulate(tableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
            else:
                print("Character not found. Please try again.");


        elif(select == "3"):
            tableArray = generateTableArrayAllCombos(characterDict,classDict,minConstraints,maxConstraints);
            print(tabulate(tableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
            while(1):
                display_constraints(minConstraints,maxConstraints);
                charOptions = characterMenu.keys();
                for char1 in charOptions:
                    print(char1 + ":" + characterMenu[char1]);
                select4 = input("Choose an option: ");
                if(select4 == "0"):
                    print("Returning...");
                    break;
                elif(select4 == "1"):
                    tableArray = generateTableArrayAllCombos(characterDict,classDict,minConstraints,maxConstraints);
                    sortedTableArray = stat_menu(tableArray);
                    print(tabulate(sortedTableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                elif(select4 == "2"):
                    constraintMinResults = low_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
                    if((constraintMinResults[0] != -1) and (constraintMinResults[1] != -1)):
                        minConstraints[constraintMinResults[0]] = constraintMinResults[1];
                        tableArray = generateTableArrayAllCombos(characterDict,classDict,minConstraints,maxConstraints);
                        print(tabulate(tableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
                elif(select4 == "3"):
                    constraintMaxResults = high_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
                    if((constraintMaxResults[0] != -1) and (constraintMaxResults[1] != -1)):
                        maxConstraints[constraintMaxResults[0]] = constraintMaxResults[1];
                        tableArray = generateTableArrayAllCombos(characterDict,classDict,minConstraints,maxConstraints);
                        print(tabulate(tableArray, headers=['Character', 'Class Name', 'HP', 'STR', 'MAG', 'SKL', 'SPD', 'LCK', 'DEF', 'RES']));
            else:
                print("Character not found. Please try again.");


        elif(select == "4"):
            constraintMinResults = low_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
            if((constraintMinResults[0] != -1) and (constraintMinResults[1] != -1)):
                minConstraints[constraintMinResults[0]] = constraintMinResults[1];
        elif(select == "5"):
            constraintMaxResults = high_constraint_menu();           #[0] is index in the constraints array, [1] is constraint percentage
            if((constraintMaxResults[0] != -1) and (constraintMaxResults[1] != -1)):
                maxConstraints[constraintMaxResults[0]] = constraintMaxResults[1];
        elif(select == "6"):
            minConstraints = [0,0,0,0,0,0,0,0]
            maxConstraints = [100,100,100,100,100,100,100,100]


main();