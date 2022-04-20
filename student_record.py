from ast import While
from asyncio.windows_events import NULL
import json
import sys
from os import path
from datetime import datetime

# initialize/declaration part
filename = 'Student.json'
empty = {"Students": [], "Semester-1": [], "Semester-2": [], "Semester-3": [],
         "Semester-4": [], "Semester-V": [], "Semester-6": []}
listObj = []
new_stu = []
subjectArray = ["English", "Science", "Mathematics"]
sem1 = ["Digital Electronics",
        "Basics Computer Science", "Environmental Sciences"]
sem2 = ["Front Office Managementh",
        "Discrete Mathematics", "Computer Organization"]
sem3 = ["C++", "Functional English", "Technical Writing"]
sem4 = ["Database", "Value and Ethics", "System Design"]
sem5 = ["Operating System", "Python", "System Software"]
sem6 = ["Numerical Analysis", "System Programming", "Project Work"]

# Check if file exists
if path.isfile(filename) is False:
    with open("Student.json", "w") as outfile:
        json.dump(empty, outfile)
else:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            len(data['Students'])
    except:
        with open(filename, "w") as outfile:
            json.dump(empty, outfile)


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
        'S.No', 'Student name', 'Student number'))
    print("{:<8} {:<25} {:<10}".format(
        '====', '============', '=============='))
    for i in range(len(data['Students'])):
        print("{:<8} {:<25} {:<10}".format(
            i+1, data['Students'][i]['Name'], data['Students'][i]['Number']))
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
    print("{:<8} {:<25} {:<10} {:<10}".format(
        'S.No', 'Subject', 'Mark', 'Status'))
    print("{:<8} {:<25} {:<10} {:<10}".format(
        '====', '=======', '====', '======'))

    for j in range(len(data['Marks'])):
        if data['Students'][n_val-1]['Number'] == data['Marks'][j]['Number']:
            for key in data['Marks'][j]:
                if key == 'Number':
                    continue
                tot += int(data['Marks'][j][key])
                if int(data['Marks'][j][key]) < 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    list(data['Marks'][j]).index(key), key, data['Marks'][j][key], sts))
                # print(list(data['Marks'][j]).index(key), "\t\t", key, "\t",
                #       data['Marks'][j][key], "\t", sts)

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
        if data['Students'][i]['Number'] == roll_number:
            return True
    return False


def valid_dob():
    format = "%d-%m-%Y"
    maxYear = 2017
    minYear = 1990
    while True:
        dob = str(input("Enter DOB(dd-mm-yyyy) year[1990-2017]: "))

        try:
            fDate = datetime.strptime(dob, format)
            if fDate.year < minYear or fDate.year > maxYear:
                None
            else:
                return dob
        except:
            None


def valid_mark(str):
    while True:
        print("Enter ", str, " Mark (Max *100) : ")
        num = input()
        try:
            num = int(num)
            if num >= 0 and num <= 100:
                return num
        except ValueError:
            None


def new_student():

    while True:
        try:
            roll_number = input("Enter roll number: ")
            int(roll_number)

            chk_roll = chk_student_byID(roll_number)
            if chk_roll == False:
                stu_details = [{
                    "Name": str(input("Enter name: ")),
                    "DateOfBirth": valid_dob(),
                    "PlaceOfBirth":  str(input("Enter PlaceOfBirth: ")),
                    "Number":  roll_number
                }, {
                    "Number": roll_number,
                    subjectArray[0]: valid_mark(subjectArray[0]),
                    subjectArray[1]: valid_mark(subjectArray[1]),
                    subjectArray[2]: valid_mark(subjectArray[2])
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
    resp = False
    for i in range(len(data['Students'])):
        if data['Students'][i]['Number'] == roll_num:
            resp = True
            break
    return resp


def edit_student(roll_num):
    while True:
        try:
            stu_details = [{
                "Name": str(input("Enter name: ")),
                "DateOfBirth": valid_dob(),
                "PlaceOfBirth":  str(input("Enter PlaceOfBirth: ")),
                "Number":  roll_num
            }, {
                "Number": roll_num,
                "English": int(input("Enter English mark: ")),
                "Science": int(input("Enter Science mark: ")),
                "Mathematics": int(input("Enter Mathematics mark: "))
            }]
            return stu_details
        except ValueError:
            print('***ENTER VALID DETAILS***')
            print('_________________________________________________')
            None


def delete_student(roll_num):
    for i in range(len(data['Students'])):
        if data['Students'][i]['Number'] == roll_num:
            del data['Students'][i]
            break
    for j in range(len(data['Marks'])):
        if data['Marks'][j]['Number'] == roll_num:
            del data['Marks'][j]
            write_json(filename, data)
            return True
    return False


def index_main():
    while True:
        print('\t\tINDEX\t\n=============================')
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


# FUNCTION CALL
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
            data['Marks'].append(new_stu[1])
            write_json(filename, data)
            print('_________________________________________________')
            print('*******STUDENT RECORD ADDED SUCCESSFULLY.')

            None
        elif val == 3:
            while True:
                try:
                    roll_num = input("Roll Num : ")
                    int(roll_num)
                    if chk_student(roll_num):
                        edit_stu = edit_student(roll_num)
                        if delete_student(roll_num):
                            data['Students'].append(edit_stu[0])
                            data['Marks'].append(edit_stu[1])
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
