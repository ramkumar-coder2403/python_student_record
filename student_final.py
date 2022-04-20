from ast import While
from asyncio.windows_events import NULL
import json
import sys
from os import path
from datetime import datetime


# initialize/declaration part
filename = 'Student.json'
empty = {"Students": [], "Semester_1": [], "Semester_2": [], "Semester_3": [],
         "Semester_4": [], "Semester_5": [], "Semester_6": []}
listObj = []
new_stu = []
markIndex = 0
semesters = ["Semester_1", "Semester_2", "Semester_3",
             "Semester_4", "Semester_5", "Semester_6"]
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


# VIEW ALL RECORD
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


def print_sem_wise(n_val, sem):
    global markIndex
    markIndex += markIndex

    for j in range(len(data[sem])):
        if data['Students'][n_val-1]['Number'] == data[sem][j]['Number']:
            for key in data[sem][j]:
                if key == 'Number':
                    continue
                tot += int(data[sem][j][key])
                if int(data[sem][j][key]) < 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    markIndex, key, data[sem][j][key], sts))
                print("===================================================")
                print("{:<10} {:>27}".format('TOTAL', tot))
                print("===================================================")


def view_rec_by_id(n_val):
    tot = 0
    print("Name of the Student : ",
          data['Students'][n_val-1]['Name'], '\n')
    print("{:<8} {:<25} {:<10} {:<10}".format(
        'S.No', 'Subject', 'Mark', 'Status'))
    print("{:<8} {:<25} {:<10} {:<10}".format(
        '====', '=======', '====', '======'))

    for i in range(5):
        print(semesters[i], ":")
        print_sem_wise(n_val, semesters[i])

    global markIndex
    markIndex = 0

    while True:
        choice = input(
            "Do you want see other details?: yes/no ")
        if choice.lower().replace(" ", "") == 'yes':
            view_all_rec()
        elif choice.lower().replace(" ", "") == 'no':
            break
    main()


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
        # elif val == 2:
        #     new_stu = new_student()
        #     data['Students'].append(new_stu[0])
        #     data['Marks'].append(new_stu[1])
        #     write_json(filename, data)
        #     print('_________________________________________________')
        #     print('*******STUDENT RECORD ADDED SUCCESSFULLY.')

        #     None
        # elif val == 3:
        #     while True:
        #         try:
        #             roll_num = input("Roll Num : ")
        #             int(roll_num)
        #             if chk_student(roll_num):
        #                 edit_stu = edit_student(roll_num)
        #                 if delete_student(roll_num):
        #                     data['Students'].append(edit_stu[0])
        #                     data['Marks'].append(edit_stu[1])
        #                     write_json(filename, data)
        #                     print(
        #                         '_______________________________________________')
        #                     print('*****STUDENT RECORD EDITED SUCCESSFULLY.')
        #                 else:
        #                     print("***Error in edit opt")
        #             else:
        #                 print('*******STUDENT RECORD NOT FOUND.')
        #             break
        #         except ValueError:
        #             print('***ENTER VALID ROLL NUMBER***')
        #             None
        # elif val == 4:
        #     while True:
        #         try:
        #             roll_num = input("Roll Num : ")
        #             int(roll_num)
        #             if delete_student(roll_num):
        #                 print('_________________________________________________')
        #                 print('STUDENT RECORD DELETED SUCCESSFULLY.')

        #             else:
        #                 print('STUDENT RECORD NOT FOUND.')
        #             break
        #         except ValueError:
        #             print('***ENTER VALID ROLL NUMBER***')
        #             None


main()
