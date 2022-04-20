import json
from datetime import datetime
import sys
from os import path
###============================================================================
### Local Variables
###============================================================================
filename = 'Mark_list.json'
empty = {"Students": [], "Semester-1": [], "Semester-2": [], "Semester-3": [],
         "Semester-4": [],"Semester-V": [], "Semester-6": []}
listObj = []
new_stu = []
tot = 0
# Check if file exists
if path.isfile(filename) is False:
    with open("College_Mark_list_new_file", "w") as outfile:
        json.dump(empty, outfile)
else:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            len(data['Students'])
    except:
        with open(filename, "w") as outfile:
            json.dump(empty, outfile)
###============================================================================
### Main function
###============================================================================  
def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Read JSON file
data = read_json(filename)

def view_all_rec():
    print("{:<8} {:<25} {:<10}".format(
        'S.No', 'Student name', 'Student Roll number'))
    print("{:<8} {:<25} {:<10}".format(
        '====', '============', '==================='))
    for i in range(len(data['Students'])):
        print("{:<8} {:<25} {:<10}".format(
            i+1, data['Students'][i]['Name'], 
            data['Students'][i]['Roll Number']))
    print('_________________________________________________')
    while True:
        val = input(
            "Enter the S.No for more details or type exit to Main menu: ")
        try:
            n_val = int(val)
            if n_val == 0 or n_val > len(data['Students']):
                None
            else:
                break
        except ValueError:
            if val.lower().replace(" ", "") == 'exit':
                main()
            else:
                None
    print('_________________________________________________')
    view_rec_by_id(n_val)

def view_rec_by_id(n_val):
    tot = 0
    print("Name of the Student : ",
          data['Students'][n_val-1]['Name'], '\n')
    # print("Semester Number: ",'\n')
    print("{:<8} {:<25} {:<10} {:<10}".format(
        'S.No', 'Subject', 'Mark', 'Status'))
    print("{:<8} {:<25} {:<10} {:<10}".format(
        '====', '=======', '====', '======'))
    # print('Seme')
    for j in range(len(data['Semester-1'])):
        if data['Students'][n_val-1]['Roll Number']== (data['Semester-1']
        [j]['Roll Number']):
            for key in data['Semester-1'][j]:
                if key == 'Roll Number':
                    continue
                tot += int(data['Semester-1'][j][key]) 
                if int(data['Semester-1'][j][key])< 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Semester-1'][j]).index(key),key,
                    data['Semester-1'][j][key], sts))
    for j in range(len(data['Semester-2'])):
        if data['Students'][n_val-1]['Roll Number']== (data['Semester-2']
        [j]['Roll Number']):
            for key in data['Semester-2'][j]:
                if key == 'Roll Number':
                    continue
                tot += int(data['Semester-2'][j][key]) 
                if int(data['Semester-2'][j][key])< 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Semester-2'][j]).index(key),key,
                    data['Semester-2'][j][key], sts))
    for j in range(len(data['Semester-3'])):
        if data['Students'][n_val-1]['Roll Number']== (data['Semester-3']
        [j]['Roll Number']):
            for key in data['Semester-3'][j]:
                if key == 'Roll Number':
                    continue
                tot += int(data['Semester-3'][j][key]) 
                if int(data['Semester-3'][j][key])< 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Semester-3'][j]).index(key),key,
                    data['Semester-3'][j][key], sts))
    for j in range(len(data['Semester-4'])):
        if data['Students'][n_val-1]['Roll Number']== (data['Semester-4']
        [j]['Roll Number']):
            for key in data['Semester-4'][j]:
                if key == 'Roll Number':
                    continue
                tot += int(data['Semester-4'][j][key]) 
                if int(data['Semester-4'][j][key])< 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Semester-4'][j]).index(key),key,
                    data['Semester-4'][j][key], sts))
    for j in range(len(data['Semester-5'])):
        if data['Students'][n_val-1]['Roll Number']== (data['Semester-5']
        [j]['Roll Number']):
            for key in data['Semester-5'][j]:
                if key == 'Roll Number':
                    continue
                tot += int(data['Semester-5'][j][key]) 
                if int(data['Semester-5'][j][key])< 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Semester-5'][j]).index(key),key,
                    data['Semester-5'][j][key], sts))
    for j in range(len(data['Semester-6'])):
        if data['Students'][n_val-1]['Roll Number']== (data['Semester-6']
        [j]['Roll Number']):
            for key in data['Semester-6'][j]:
                if key == 'Roll Number':
                    continue
                tot += int(data['Semester-6'][j][key]) 
                if int(data['Semester-6'][j][key])< 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Semester-6'][j]).index(key),key,
                    data['Semester-6'][j][key], sts))
    print("===================================================")
    print("{:<10} {:>27}".format('TOTAL', tot))
    print("===================================================")
    while True:
        choice = input(
            "Do you want see other details?: yes/no ")
        if choice.lower().replace(" ", "") == 'yes':
            view_all_rec()
        elif choice.lower().replace(" ", "") == 'no':
            break
    main()

def chk_student_byID(roll_number):
    for i in range(len(data['Students'])):
        if data['Students'][i]['Roll Number'] == roll_number:
            return True
    return False

def valid_dob():
    format = "%d-%m-%Y"
    maxYear = 2017
    minYear = 1995
    while True:
        dob = str(input("Enter DOB(dd-mm-yyyy) year[1995-2017]: "))

        try:
            fDate = datetime.strptime(dob, format)
            if fDate.year < minYear or fDate.year > maxYear:
                None
            else:
                return dob
        except:
            None

def new_student():
    while True:
        try:
            roll_number = input("Enter Roll number: ")
            int(roll_number)

            chk_roll = chk_student_byID(roll_number)
            if chk_roll == False:
                stu_details = [{
                    "Name": str(input("Enter name: ")),
                    "DateOfBirth": valid_dob(),
                    "PlaceOfBirth":  str(input("Enter PlaceOfBirth: ")),
                    "Roll Number":  roll_number
                }, 
                {
                    "Roll Number": roll_number,
                   "Digital Electronics": int(input("Enter Digital Electronics mark: ")),
                   "Basics Computer Science": int(input("Enter Basics of Computer Science mark: ")),
                   "Environmental Sciences": int(input("Enter Environmental Sciences mark: "))
                }, 
                {
                   "Roll Number": roll_number,
                   "Front Office Managementh": int(input("Enter Front Office Management mark: ")),
                   "Discrete Mathematics": int(input("Enter Discrete Mathematics mark: ")),
                   "Computer Organization": int(input("Enter Computer Organization mark: ")) 
                },
                {
                  "Roll Number": roll_number,
                  "C++": int(input("Enter C++ mark: ")),
                  "Functional English": int(input("Enter Functional English mark: ")),
                  "Technical Writing": int(input("Enter Technical Writing mark: "))
                }, 
                {
                  "Roll Number": roll_number,
                  "Database": int(input("Enter Database mark: ")),
                  "Value and Ethics": int(input("Enter Value and Ethics mark: ")),
                  "System Design": int(input("Enter System Design mark: "))
                }, 
                {
                  "Roll Number": roll_number,
                  "Operating System": int(input("Enter Operating System mark: ")),
                  "Python": int(input("Enter Python mark: ")),
                  "System Software": int(input("Enter System Software mark: "))
                }, 
                {
                  "Roll Number": roll_number,
                  "Numerical Analysis": int(input("Enter Numerical Analysis mark: ")),
                  "System Programming": int(input("Enter System Programming mark: ")),
                  "Project Work": int(input("Enter Project Work: ")) 
                }]
                return stu_details
            else:
                print('STUDENT RECORD ALREADY FOUND.')
                None
        except ValueError:
            print('***ENTER VALID DETAILS***')
            print('_________________________________________________')
            None

def chk_student(roll_num):

    for i in range(len(data['Students'])):
        if data['Students'][i]['Roll Number'] == roll_num:
            
            break
def edit_student(roll_num):
    while True:
        try:
            stu_details = [{
                "Name": str(input("Enter name: ")),
                "DateOfBirth": valid_dob(),
                "PlaceOfBirth":  str(input("Enter PlaceOfBirth: ")),
                "Number":  roll_num
            }, {
                "Roll Number": roll_num,
                "Digital Electronics": int(input("Enter Digital Electronics mark: ")),
                "Basics Computer Science": int(input("Enter Basics of Computer Science mark: ")),
                "Environmental Sciences": int(input("Enter Environmental Sciences mark: "))
            }, {
                "Roll Number": roll_num,
                "Front Office Managementh": int(input("Enter Front Office Management mark: ")),
                "Discrete Mathematics": int(input("Enter Discrete Mathematics mark: ")),
                "Computer Organization": int(input("Enter Computer Organization mark: "))
            }, {
                "Roll Number": roll_num,
                "C++": int(input("Enter C++ mark: ")),
                "Functional English": int(input("Enter Functional English mark: ")),
                "Technical Writing": int(input("Enter Technical Writing mark: "))
            }, {
                "Roll Number": roll_num,
                "Database": int(input("Enter Database mark: ")),
                "Value and Ethics": int(input("Enter Value and Ethics mark: ")),
                "System Design": int(input("Enter System Design mark: "))
            }, {
                "Roll Number": roll_num,
                "Operating System": int(input("Enter Operating System mark: ")),
                "Python": int(input("Enter Python mark: ")),
                "System Software": int(input("Enter System Software mark: "))
            }, {
                "Roll Number": roll_num,
                "Numerical Analysis": int(input("Enter Numerical Analysis mark: ")),
                "System Programming": int(input("Enter System Programming mark: ")),
                "Project Work": int(input("Enter Project Work: "))
            }]
            return stu_details
        except ValueError:
            print('***ENTER VALID DETAILS***')
            print('_________________________________________________')
            None

def delete_student(roll_num):
    for i in range(len(data['Students'])):
        if data['Students'][i]['Roll Number'] == roll_num:
            del data['Students'][i]
            break
    for j in range(len(data['Semester-1'])):
        if (data['Semester-1'][j]['Roll Number']) == roll_num:
            del data['Semester-1'][j]
            break
    for k in range(len(data['Semester-2'])):
        if (data['Semester-2'][k]['Roll Number']) == roll_num:
            del data['Semester-2'][k]
            break
    for p in range(len(data['Semester-3'])):
        if (data['Semester-3'][p]['Roll Number']) == roll_num:
            del data['Semester-3'][p]
            break
    for q in range(len(data['Semester-4'])):
        if (data['Semester-4'][q]['Roll Number']) == roll_num:
            del data['Semester-4'][q]
            break
    for r in range(len(data['Semester-5'])):
        if (data['Semester-5'][r]['Roll Number']) == roll_num:
            del data['Semester-5'][r]
            break
    for s in range(len(data['Semester-6'])):
        if (data['Semester-6'][s]['Roll Number']) == roll_num:
            del data['Semester-6'][s]
            write_json(filename, data)
            return True
    return False

def index_main():
    while True:
        print('\tINDEX\t\n=============================')
        print(
            '1. View All Records\n2. Add new Student\n3. Edit Student\n4. Delete existing Student\n0. Exit')
        print('=============================')
        try:
            opt = int(input("Enter Valid Option : "))
            if opt == 1 or opt == 2 or opt == 3 or opt == 4:
                return opt
            elif opt == 0:
                sys.exit()
            else:
                None
        except ValueError:
            print('***ENTER VALID MENU OPTION***')
# function call
def main():
    while True:
        val = index_main()
        if val == 1:
            if len(data['Students']) == 0:
                print('_________________________________________________')
                print('*******STUDENT RECORDS NOT FOUND.')
            else:
                view_all_rec()
        elif val == 2:
            new_stu = new_student()
            data['Students'].append(new_stu[0])
            data['Semester-1'].append(new_stu[1])
            data['Semester-2'].append(new_stu[2])
            data['Semester-3'].append(new_stu[3])
            data['Semester-4'].append(new_stu[4])
            data['Semester-5'].append(new_stu[5])
            data['Semester-6'].append(new_stu[6])
            write_json(filename, data)
            print('_________________________________________________')
            print('*******STUDENT RECORD ADDED SUCCESSFULLY.')
            None
        elif val == 3:
            while True:
                try:
                    roll_num = input("Roll Number : ")
                    int(roll_num)
                    if chk_student(roll_num):
                        edit_stu = edit_student(roll_num)
                        if delete_student(roll_num):
                            data['Students'].append(edit_stu[0])
                            data['Semester-1'].append(edit_stu[1])
                            data['Semester-2'].append(edit_stu[2])
                            data['Semester-3'].append(edit_stu[3])
                            data['Semester-4'].append(edit_stu[4])
                            data['Semester-5'].append(edit_stu[5])
                            data['Semester-6'].append(edit_stu[6])
                            write_json(filename, data)
                            print(
                                '_______________________________________________')
                            print('*****STUDENT RECORD EDITED SUCCESSFULLY.')
                        else:
                            print("***Error in edit opt")
                    else:
                        print('*******STUDENT RECORD NOT FOUND.')
                    break
                except ValueError:
                    print('***ENTER VALID ROLL NUMBER***')
                    None
        elif val == 4:
            while True:
                try:
                    roll_num = input("Roll Num : ")
                    int(roll_num)
                    if delete_student(roll_num):
                        print('_________________________________________________')
                        print('STUDENT RECORD DELETED SUCCESSFULLY.')

                    else:
                        print('STUDENT RECORD NOT FOUND.')
                    break
                except ValueError:
                    print('***ENTER VALID ROLL NUMBER***')
                    None
main()
