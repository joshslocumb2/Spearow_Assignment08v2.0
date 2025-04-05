# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import csv
from CSVUtilitiesPackage.CSVUtilities import CSVUtilities
try:
    from dataProcessingPackage.teamMember01 import teamMember01
except:
    pass
try:
    from dataProcessingPackage.teamMember02 import teamMember02
except:
    pass
try:
    from dataProcessingPackage.teamMember03 import teamMember03
except:
    pass


if __name__ == "__main__":
    myCSVUtilities = CSVUtilities()
    fileName = "data/fake people.csv"
    data = myCSVUtilities.load_csv_to_dict_list(fileName)
    print(len(data), "records read from", fileName)
    print(data[1])
    teamMembers = []
    for idx in range(1,4):
        try:
            class_name_string = "teamMember0" + str(idx)
            myTeamMember = globals()[class_name_string]()
            teamMembers.append(myTeamMember)
        except:
            print("Unable to instantiate the class " + class_name_string + "... (has that code been written?)")

    for teamMember in teamMembers:
        try:
            teamMember.print_something_interesting(data)
        except:
            print("Unable to invoke print_something_interesting method for class " + type(teamMember).__name__ , "... (has that method been written?)")