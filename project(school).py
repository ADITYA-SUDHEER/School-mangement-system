import mysql.connector print("\t\t\tSchool Management Software")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin") cur=mydb.cursor()
cur.execute("use schooldatabase;")

def admn():
    cur.execute('select max(adm_no) from student1;') rec=cur.fetchone()
    adm=rec[0]+1 return adm


def newadmission():
    Adm_no=admn()
    print('Admission Number :',Adm_no)
    Name=input("Enter your name")
    Age=int(input("Enter your Age"))
    Place=input("Enter your place")
    Father=input("Enter Father's Name")
    Mother=input("Enter mother's Name")
    Phone=int(input("Enter mobile number"))
    Aadhar=int(input("Enter Aadhar number"))
    Class=input("Enter your class")
    query="insert into Student1 values({},'{}',{},'{}','{}','{}','{}',{},{});".format(Adm_no,Name,Age,Place,Father,M other,Phone,Aadhar,Class)
    cur.execute(query) mydb.commit()
    mydb.commit()
def menu():
    while True:
        print('1:New Admission')
        print('2:Display Student Details')
        print('3:Edit Details')
        print('4:Delete Details')
        print('5:Academic Details')
        ch = input('enter choice: ')
        if ch == '1':
            newadmission()
        elif ch == '2':
            x=int(input("Enter your admission number"))
            cur.execute('select * from student1 where Adm_no = {};'.format(x)) records = cur.fetchall()
            if records:
                for i in records: print(i)
            else:
                print('not found')
        elif ch=='3':
            x=int(input("Enter your admission number"))
            cur.execute('select * from student1 where Adm_no = {};'.format(x)) records = cur.fetchall()
            for i in records:
                print(i)
            while True:
                print("1:Edit Name")
                print("2:Edit Age")
                print("3:Edit Place")
                print("4:Edit Father's Name")
                print("5:Edit Mother's Name")
                print("6:Edit Phone")
                print("7:Edit Aadhar Number")
                print("8:Edit Class")
                print('9: exit')
                ch=input('enter choice:')
                if ch=='1':
                    y=input("Enter your name")
                    cur.execute('update student1 set name = "{}" where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                elif ch=='2':
                    y=input("Enter your Age")
                    cur.execute('update student1 set Age = {} where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                elif ch=='3':
                    y=input("Enter your Place")
                    cur.execute('update student1 set Place = "{}" where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                elif ch=='4':
                    y=input("Enter your Father's Name")
                    cur.execute('update student1 set Father = "{}" where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                elif ch=='5':
                    y=input("Enter your Mothers Name")
                    cur.execute('update student1 set mother = "{}" where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                elif ch=='6':
                    y=input("Enter your Phone number")cur.execute('update student1 set Phone = {} where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                elif ch=='7':
                    y=input("Enter your Aadhar number")
                    cur.execute('update student1 set Aadhar = {} where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                elif ch=='8':
                    y=input("Enter your Class")
                    cur.execute('update student1 set Class = "{}" where Adm_no= {};'.format(y,x))
                    mydb.commit()
                    print("Successfully updated")
                else:
                    break
        elif ch=='4':
            x=int(input("Enter your admisssion number"))
            cur.execute('Delete from student1 where Adm_no={};'.format(x)) mydb.commit()
            print("Successfully deleted")
        elif ch == '5':
            adm_no = input('Enter Admission Number: ')
            cur.execute('select name from student1 where adm_no={};'.format(adm_no)) name = cur.fetchone()[0]
            print('Student is {}'.format(name))
            while True:
                print('''1: Enter marks 2: Edit marks 3: Display mark 4: Exit''')
                ch = input('enter choice: ')
                if ch=='1':
                    sub=input("Enter the subject")
                    mark=input("Enter the mark")
                    exam=input("Enter Exam name")
                    cur.execute("select * from academics where adm_no = {} and subject = '{}' and exam='{}';".format(adm_no,sub,exam))
                    exists = cur.fetchall()
                    if exists:
                        print('subject already exists')
                    else:
                        cur.execute("insert into academics values({},'{}','{}',{},'{}');".format(adm_no,name,sub,mark,exam))
                        mydb.commit()
                elif ch=='2':
                    sub=input("Enter the subject")
                    mark=input("Enter the mark")
                    exam=input("enter exam name")
                    cur.execute("update academics set mark={} where adm_no ={} and subject = '{}' and exam='{}';".format(mark,adm_no,sub,exam))
                    mydb.commit()
                elif ch=='3':
                    cur.execute("select * from academics where adm_no={};".format(adm_no))
                    z=cur.fetchall() for i in z:
                    print(i)
                elif ch=='4':
                    break
        else:
            break
menu()


                    



