from msilib.schema import ODBCAttribute
from select import select
import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="sHj@6378#jw",
  database="hotel1" 
)
#print(mydb)
mycursor=mydb.cursor()
#hotel management
print("\t\t^...HOTEL MANAGEMENT...^\t\t")
print("\t\t************************\t\t")
print("WELCOME TO RAKSHAN HOTEL")
print(".....................")
#introduce our hotel 
print("since:2000-2022")
print("our management is 22 years old to running successfully with our love and support")
print("our management is too good for quality")
print("And  amount quantity will be variable for you")
print("**Take your seat sir/mam**")
print("**what do you want sir/mam**")
#menu card#BUY ONE GET ONE 
    #OFFERS:
print(".*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
print("***..GRAND OPENING OFFER..***")
print("***only for/- 19,20,21.9.22")
fr=["1.chicken_biriyani+chicken_biriyani","2.mutton_biriyani+chicken_rice","3.chicken_biriyani+chicken_noodles+egg_rice"]
print(fr)
user=int(input("enter your offer 1,2,or 3:"))
if user==1:
  print("enjoy your buy one get one offer")
elif user==2:
  print("receive your food and enjoy")
elif user==3:
  print("your combo offer")
  print("enjoy :)")  
else:
  print("not in offer")   
print("_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#")              
print("*..MENU CARD..*")
print("_______________")  
mycursor.execute("select * from menu")
result=mycursor.fetchall()
for i in result:
    print(i)
    #choose the order
avaliables=["online_order","home_parcel","seat&eat"]
print(avaliables)
user=input("it is available:")
     #ONLINE ORDER
if user=="online_order":
  print("you can order this number:9876543267")
  op=input("enter your address:")
  print("**you can choose your order please**")
  print("**With in one hour your order will delivered")
  list=["1.Chicken_Biriyani","2.Chicken_Noodles","3.Egg_Noodles","4.Chicken_Rice","5.Egg_Rice","6.Veg_Biriyani","7.Mutton_Biriyani","8.Gobi_Manchuiran","9.South_Indian Veg Meals"]
  print(list)
  order=(input("your order pls:"))
  if order=="Chicken_Biriyani":
    print(f"your order {order} in menu")
  elif order=="Chicken_Noodles":
    print(f"your order {order} in menu")
  elif order=="Egg_Noodles":
    print(f"your order {order} in menu")
  elif order=="Chicken_Rice":
    print(f"your order {order} in menu")
  elif order=="Egg_Rice":
    print(f"your order {order} in menu")
  elif order=="Veg_Biriyani":
    print(f"your order {order} in menu")
  elif order=="Mutton_Biriyani":
        print(f"your order {order} in menu")
  elif order=="Gobi_Manchuiran":
        print(f"your order {order} in menu")
  else:
    print(f"your order{order} not in a menu")
#home parcel
elif user=="home_parcel":
  list=["1.Chicken_Biriyani","2.Chicken_Noodles","3.Egg_Noodles","4.Chicken_Rice","5.Egg_Rice","6.Veg_Biriyani","7.Mutton_Biriyani","8.Gobi_Manchuiran","9.South_Indian Veg Meals"]   
  print(list)
  ab=input("choose menu list:")
  if ab=="Chicken_Biriyani":
    print(f"your order {ab} in menu")
  elif ab=="Chicken_Noodles":
    print(f"your order {ab} in menu")
  elif ab=="Egg_Noodles":
    print(f"your order {ab} in menu")
  elif ab=="Chicken_Rice":
    print(f"your order {ab} in menu")
  elif ab=="Egg_Rice":
    print(f"your order {ab} in menu")
  elif ab=="Veg_Biriyani":
    print(f"your order {ab} in menu")
  elif ab=="Mutton_Biriyani":
    print(f"your order {ab} in menu")
  elif ab=="Gobi_Manchuiran":
    print(f"your order {ab} in menu")
  elif ab=="South_Indian Veg Meals":
    print(f"your order {ab} in menu")
  else:
    print("not in menu")  
    sd=input("how many parsel you want:")
    print("receive your parsel")
     #SEATANDEAT  
elif user=="seat&eat":
  list=["1.Chicken_Biriyani","2.Chicken_Noodles","3.Egg_Noodles","4.Chicken_Rice","5.Egg_Rice","6.Veg_Biriyani","7.Mutton_Biriyani","8.Gobi_Manchuiran","9.South_Indian Veg Meals"]
  print(list)
  order=(input("your order pls:"))
  if order=="Chicken_Biriyani":
    print(f"your order {order} in menu")
  elif order=="Chicken_Noodles":
    print(f"your order {order} in menu")
  elif order=="Egg_Noodles":
    print(f"your order {order} in menu")
  elif order=="Chicken_Rice":
    print(f"your order {order} in menu")
  elif order=="Egg_Rice":
    print(f"your order {order} in menu")
  elif order=="Veg_Biriyani":
    print(f"your order {order} in menu")
  elif order=="Mutton_Biriyani":
        print(f"your order {order} in menu")
  elif order=="Gpobi_Manchuiran":
        print(f"your order {order} in menu")
  else:
      print(f"your order {order} is not in menu")
      print("if you want any other item mam/sir")
      de=input("enter your ans:")        
      if de=="yes":
          print("sure sir/mam you can order again")
      else:
          print("thank you for visiting mam/sir")                            
print("****************************************************************")
    #customer feed back
print("\tyou can give the feed back \t")
print("\t***************************\t")
fb=input(" ENTER YOUR FEED BACK:")
print("#..Thank you for your feed back..#")
print("*******Thank You Sir/Madam********")