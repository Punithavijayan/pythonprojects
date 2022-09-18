import pandas as pd
import mysql.connector
import warnings
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="sHj@6378#jw",
  database="railway" 
)
#print(mydb)
mycursor=mydb.cursor()
def menu():
    print()
    print("\t\t\tTRAIN RESERVATION\t\t\t")
    print("\t\t\t******************\t\t\t")
    print("1. add new passenger details")
    print("2. show all from train details")
    print("3. show all from passenger table")
    print("4. Reservation of ticket")
    print("5. Cancellation of Reservation")
menu() 

def add_passengers():
    warnings.filterwarnings('ignore')
    mycursor=mydb.cursor()
    list=[]
    passname=input("ENTER NAME:")
    list.append(passname)
    age=input("ENTER AGE:")
    list.append(age)
    trainno=input("ENTER TRAIN NO:")
    list.append(trainno)
    no_ofpassangers=input("ENTER NOO. OF PASENGERS:")
    list.append(no_ofpassangers)
    cls=input("ENTER CLASS:")
    list.append(cls)
    destination=input("ENTER DESTINATION:")
    list.append(destination)
    amount=input("ENTER FARE:")
    list.append(amount)
    status=input("ENTER STATUS:")
    list.append(status)
    pnrno=input("ENTER PNRNO:")
    list.append(pnrno)
    pas=(list)
    sql="insert into passangers(passname,age,trainno,no_ofpassangers,class,destination,amount,status,pnrno) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,pas)
    mydb.commit()
    print('passenger record inserted')
    df=pd.read_sql("select * from passangers",mydb)
    print(df)

def add_traindetail():
    warnings.filterwarnings('ignore')
    mycursor=mydb.cursor()
    mycursor.execute("select * from trainsdetail")
    list=[]
    trainname=input("ENTER TRAIN NAME:")
    list.append(trainname)
    trainno=input("ENTER NUMBER OF TRAIN:")
    list.append(trainno)
    source=input("ENTER  SOURCE OF TRAIN:")
    list.append(source)
    destination=input("ENTER DESTINATION  OF TRAIN:")
    list.append(destination)
    fare=input("ENTER FARE OF STATION:")
    list.append(fare)
    ac1=input("ENTER NO. OF SEATS FOR AC1:")
    list.append(ac1)
    ac2=input("ENTER NO. OF SEATS FOR AC2:")
    list.append(ac2)
    sleep=input("ENTER NO. OF SEATS FOR SLEEPER:")
    list.append(sleep)
    f=(list)
    sql="insert into trainsdetail(trainname,trainno,source,destination,fare,ac1,ac2,sleep) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,f)
    mydb.commit()
    print('train details inserted successfully')

def showtrainsdetails():
    warnings.filterwarnings('ignore')
    print("ALL TRAIN DETAILS")
    df=pd.read_sql("select * from trainsdetail",mydb)
    print(df)

def showpass():        
    warnings.filterwarnings('ignore')
    print("ALL PASSENGER DETAILS")
    df=pd.read_sql("select * from passangers",mydb)
    print(df)
def ticketreservation():
    warnings.filterwarnings('ignore')
    print("WE HAVE THE FOLLOWING SEAT TYPESMFOR YOU")
    print("TNAME IS 1 FOR BANAGALORE_EXPRESS FROM DELHI")
    print()
    print("1. FIRST CLASS AC RS/-1000 PER PERSON")
    print("2. SECOND CLASS AC RS/-800 PER PERSON")
    print("1. THIRD CLASS AC RS/-500 PER PERSON")
    print("1. FOR SLEEPER RS/-400 PER PERSON")
    print()
    print("TNAME IS 2 FOR CHENNAI_EXPRESS FROM DELHI")
    print()
    print("1. FIRST CLASS AC RS/-2000 PER PERSON")
    print("2. SECOND CLASS AC RS/-1500 PER PERSON")
    print("1. THIRD CLASS AC RS/-500 PER PERSON")
    print("1. FOR SLEEPER RS/-400 PER PERSON")
    print()

    trainname=input("*ENTER YOUR CHOICE OF TRAIN NAME PLEASE*:")
    print(trainname)
    x=int(input("ENTER YOUR CHOICE OF TICKET PLEASE:"))
    n=int(input("HOW MANY TICKET YOU NEED:"))
    if(x==1):
        print("you have chosen first class ac ticket")
        s=1000*n
    elif(x==2):
        print("you have to choosen second class ac ticket")
        s=800*n
    elif(x==3):
        print("you have to choosen third class ac ticket")
        s=500*n    
    else:
        print("Invalid option") 
        print("please choose a train")
    print("your total ticket price is =",s,"\n")

def cancel():
    warnings.filterwarnings('ignore')
    print('before any changes in the status')
    df=pd.read_sql("select * from passangers",mydb)
    print(df)
    mycursor=mydb.cursor()
    mycursor.execute("update passangers set status='cancelled' where pnrno='G1003'")
    df=pd.read_sql("select * from passangers",mydb)
    print(df)

opt=""
opt=int(input("enter your chioce:"))
if opt==1:
    add_passengers()
elif opt==2:
    showtrainsdetails()
elif opt==3:
    showpass()
elif opt==4:
    ticketreservation()
elif opt==5:
    cancel()    
else:
    print('invalid option')                                        
