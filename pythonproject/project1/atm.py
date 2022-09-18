#import datetime                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           import random     
import random
from re import A
import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="sHj@6378#jw",
  database="sample" 
)
# print(mydb)
mycursor=mydb.cursor()
class cla:
  try:
    #withdrawal fn
    def withdrawal(self):
      try:
        all="select * from tab1"
        mycursor.execute(all)
        fetch=mycursor.fetchall()
        for widt in fetch:
          self.amount=int(input("enter your withdrawal amount:"))
          self.name="punitha"
          if self.amount==0:
            print("oops!!!")
          elif self.amount<=widt[3]:
              self.balance=widt[3]-self.amount
              a="update user set currrent_bal=%s where user_name=%s"
              b=(self.balance,self.name)
              mycursor.execute(a,b)
              mydb.commit()
              print(" your transaction is being processed...")
              print("\tplease wait....\t")
              print(f"successfully withdrawal {self.amount}")
              print(f"currrent_bal is {self.balance}") 
          else:
            print("invalid amount")
          break      
      except Exception as e:
        print(e)
    def deposite(self):
      try:
        all="select * from tab1"
        mycursor.execute(all)
        fetch=mycursor.fetchall()
        for des in fetch:
          self.amount=int(input("enter your deposite amount:"))
          self.name="punitha"
          self.balance=des[3]+self.amount
          a="update user set currrent_bal=%s where user_name=%s"
          b=(self.balance,self.name)
          mycursor.execute(a,b)
          mydb.commit()
          print("please wait sometimes....")
          print(f"successfully deposite {self.amount}")
          print(f"currrent_bal is {self.balance}") 
          break    
      except Exception as e:
        print(e)
  except Exception as e:
    print(e) 
object=cla()
print("\t\t...ATM MACHINE...\t\t")
print("\t\t_________________\t\t")
#x=datetime.datetime.now()
#print(x)
print("\tWelcome\t")
print("\t*******\t")
print("Please Insert your card")
print("PROCESSING.......")
print("Hi, Please do not remove your chip card ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
def pin_change():
  print(f" you can {select} now")
  pin=int(input("enter your new pin:"))
  ph_no=int(input("enteryour phone no:"))
  print("--enter OTP--")
  print(random.randint(1000,9999))
  otp=int(input("Enter your OTP NUMBER:"))
  print(f"{otp} otp number is valid")
  print("Please wait your process is almost finished")
def Balancy_Enquire():
  print(f"{select} loading")
#language selected
print("\t*#LANGUAGE SELECTING#\t")
print("\t******************\t")
Language=input("select your language:").upper().lower()
if Language=="english" or Language=="tamil" or Language=="hindi":
  print(f"your {Language}  language is selected")
  #enter any number
  print("\tENTERING ANY TWO DIGIT NUMBER\t")
  print("\t******************************\t")
  Number=int(input("Enter any Number Between 10 and 99: "))
  if Number<=99 and Number>=10:
    print(" your number will be selected ")
    Numbers=(input(">>Enter(yes or no) :"))
    if Numbers=="yes":  
      print(f"{Numbers} it will go to next page ")
      #pin number
      print("\tYOUR PIN_NO\t")
      print("\t***********\t")
      pin_no=int(input("Enter your secret pin:"))
      if pin_no==1308:
        print(f"your {pin_no} pin is valid")
        #Transaction choice
        print("\t***Please choose 'BANKING' for cash widthdrwal***\t")
        print("\t**************************************************\t")
        transaction=["Registration","mini statement","Banking","services","Transaction"]
        print(transaction)
        choose=input("Choose your withdrawal:").upper().lower()
        if choose=="registration":
          print(f"your {choose} is selected")
        elif choose=="Mini statement":
            print(f"your {choose} is selected")
        elif choose=="banking":
            print("banking will selected")
            #select transaction 
            print("\t***please select tranaction***\t")
            print("\t*******************************\t")
            tran=["Deposite","pin_change","Cash_withdrawal","Balancy Enquire"]
            for i in tran:
             print(i)     
            select=input("Enter your transaction:").lower()
            if select=="deposite":
              object.deposite()
              print(" your amount is deposited ")
              print("your successfully deposited amount in your bank:)")
              print("****************Thank you************************")
              print("***************visit Again*****************")
            elif select=="pin_change":
              pin_change()
              print("your new pin will changed successfully")
              print("***************visit Again*****************")
            elif select=="Balancy_Enquire":
              Balancy_Enquire() 
              print("your Balancy_Enquire has been successfully")
              print("***************visit Again*****************") 
            elif select=="cash_withdrawal":
              print("you can select amount now")  
              #account type 
              print("\t***Please select account type***\t")
              print("\t********************************\t")
              acc=["current","saving","kcc"]
              for i in acc:
               print(i)
              account=input("enter your type:")
              if account=="current" or account=="saving" or account=="kcc":
                print(f"if you selected {account} account")
                #enter amount
                print("\t*** Please enter your amount Rs/-***\t")
                print("\t************************************\t")
                print("your amount limitation is 100 to 10,000")
                object.withdrawal() 
                print("Please collect cash")
                print("Transaction complete")
                print("successfully withdrawal amount in your bank:)")
                print("****************Thank you************************")
                print("***************visit Again*****************")    
              else:
                print("please select any one")
        else:
          print("sorry your transaction  is wrong!!!")  
      else:
        print("your is not valid try again!!!")  
    if Numbers=="No": 
      print("getting back")  
  else :
     print("put between 10 to 99 number otherwise is not taken")
else:
  print("your language not received please select any one in this option")  
  print("english,tamil,hindi")