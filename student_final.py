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
stu_detail = ["Name", "DateOfBirth", "PlaceOfBirth", "Roll Number"]
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
            len(data[semesters[0]])
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
            i+1, data['Students'][i]['Name'], data['Students'][i]['Roll Number']))
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


# APPLY LOOP FOR EACH SEMESTER MARKS
def print_sem_wise(n_val, sem):
    tot = 0
    global markIndex

    for j in range(len(data[sem])):

        if data['Students'][n_val-1]['Roll Number'] == data[sem][j]['Roll Number']:
            for key in data[sem][j]:
                markIndex += 1
                if key == 'Roll Number':
                    markIndex -= 1
                    continue
                tot += int(data[sem][j][key])
                if int(data[sem][j][key]) < 35:
                    sts = 'fail'
                else:
                    sts = 'pass'

                print("{:<8} {:<25} {:<10} {:<10}".format(
                    markIndex, key, data[sem][j][key], sts))
            print("===================================================")
            print("{:<10} {:>26}".format('TOTAL', tot))
            print("===================================================")


# VIEW RECORD BY ID
def view_rec_by_id(n_val):

    print("Name of the Student : ",
          data['Students'][n_val-1]['Name'], '\n')
    print("{:<8} {:<25} {:<10} {:<10}".format(
        'S.No', 'Subject', 'Mark', 'Status'))
    print("{:<8} {:<25} {:<10} {:<10}".format(
        '====', '=======', '====', '======'))

    for i in range(6):
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


def common_student_data(roll_number):
    list_data = []
    student_details = {
        "Name": str(input("Enter name: ")),
        "DateOfBirth": valid_dob(),
        "PlaceOfBirth":  str(input("Enter PlaceOfBirth: ")),
        "Roll Number":  roll_number
    }
    list_data.append(student_details)
    print("SEMESTER-1 MARKS----------")
    semester1 = {
        "Roll Number": roll_number,
        sem1[0]: valid_mark(sem1[0]),
        sem1[1]: valid_mark(sem1[1]),
        sem1[2]: valid_mark(sem1[2])
    }
    list_data.append(semester1)
    print("SEMESTER-2 MARKS----------")
    semester2 = {
        "Roll Number": roll_number,
        sem2[0]: valid_mark(sem2[0]),
        sem2[1]: valid_mark(sem2[1]),
        sem2[2]: valid_mark(sem2[2])
    }
    list_data.append(semester2)
    print("SEMESTER-3 MARKS----------")
    semester3 = {
        "Roll Number": roll_number,
        sem3[0]: valid_mark(sem3[0]),
        sem3[1]: valid_mark(sem3[1]),
        sem3[2]: valid_mark(sem3[2])
    }
    list_data.append(semester3)
    print("SEMESTER-4 MARKS----------")
    semester4 = {
        "Roll Number": roll_number,
        sem4[0]: valid_mark(sem4[0]),
        sem4[1]: valid_mark(sem4[1]),
        sem4[2]: valid_mark(sem4[2])
    }
    list_data.append(semester4)
    print("SEMESTER-5 MARKS----------")
    semester5 = {
        "Roll Number": roll_number,
        sem5[0]: valid_mark(sem5[0]),
        sem5[1]: valid_mark(sem5[1]),
        sem5[2]: valid_mark(sem5[2])
    }
    list_data.append(semester5)
    print("SEMESTER-6 MARKS----------")
    semester6 = {
        "Roll Number": roll_number,
        sem6[0]: valid_mark(sem6[0]),
        sem6[1]: valid_mark(sem6[1]),
        sem6[2]: valid_mark(sem6[2])
    }
    list_data.append(semester6)
    return list_data

# CHECK STUDENT BY ID FOR CREATE STU


def chk_student_byID(roll_number):
    for i in range(len(data['Students'])):
        if data['Students'][i]['Roll Number'] == roll_number:
            return True
    return False


# VALIDATE DOB FOR CREATE NEW STUDENT
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

# VALIDATE MARKS FOR CREATE NEW STUDENT


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

# CREATE NEW STUDENT


def new_student():
    while True:
        try:
            roll_number = input("Enter roll number: ")
            int(roll_number)
            chk_roll = chk_student_byID(roll_number)
            if chk_roll == False:

                list_data = common_student_data(roll_number)
                return list_data
            else:
                print('STUDENT RECORD ALREADY FOUND.')
                None
        except ValueError:
            print('***ENTER VALID DETAILS***')
            print('_________________________________________________')
            None


def edit_student(roll_num):
    while True:
        try:
            stu_details = common_student_data(roll_num)
            return stu_details
        except ValueError:
            print('***ENTER VALID DETAILS***')
            print('_________________________________________________')
            None


def delete_stu_sem_mark(roll_num, k):
    for j in range(len(data[semesters[k]])):
        if data[semesters[k]][j]['Roll Number'] == roll_num:
            del data[semesters[k]][j]


def delete_student(roll_num):
    for i in range(len(data['Students'])):
        if data['Students'][i]['Roll Number'] == roll_num:
            del data['Students'][i]
            break

    for k in range(6):
        delete_stu_sem_mark(roll_num, k)

    write_json(filename, data)
    return True


# MAIN INDEX OPTION
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
            data[semesters[0]].append(new_stu[1])
            data[semesters[1]].append(new_stu[2])
            data[semesters[2]].append(new_stu[3])
            data[semesters[3]].append(new_stu[4])
            data[semesters[4]].append(new_stu[5])
            data[semesters[5]].append(new_stu[6])
            write_json(filename, data)
            print('_________________________________________________')
            print('*******STUDENT RECORD ADDED SUCCESSFULLY.')
            None
        elif val == 3:
            while True:
                try:
                    roll_num = input("Roll Num : ")
                    int(roll_num)
                    if chk_student_byID(roll_num):
                        edit_stu = edit_student(roll_num)
                        if delete_student(roll_num):
                            data['Students'].append(edit_stu[0])
                            data[semesters[0]].append(edit_stu[1])
                            data[semesters[1]].append(edit_stu[2])
                            data[semesters[2]].append(edit_stu[3])
                            data[semesters[3]].append(edit_stu[4])
                            data[semesters[4]].append(edit_stu[5])
                            data[semesters[5]].append(edit_stu[6])
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
                    if chk_student_byID(roll_num):
                        if delete_student(roll_num):
                            print(
                                '_________________________________________________')
                            print('STUDENT RECORD DELETED SUCCESSFULLY.')
                        else:
                            print('STUDENT RECORD NOT DELETED.')
                    else:
                        print('STUDENT RECORD NOT FOUND.')
                    break
                except ValueError:
                    print('***ENTER VALID ROLL NUMBER***')
                    None


main()
