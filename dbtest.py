import sqlite3
#from guide.api.settings import DATABASES
#import DATABASES
import pyodbc
import mysql.connector
import  psycopg2
import json
Database =input("Databasename ")
d= Database.upper()
if Database=='sqlserver':
    user_input =True
   # SQL server connections
    while user_input:
        try:
            conn= pyodbc.connect(host=input("host "),
            user = input("user name "),
            password=input("password "),
            Driver='ODBC Driver 13 for SQL Server')
            #database=input("database "))
            if True:
                print("connection is successful")
                break
        except Exception:
            print(" connection failed please check the username and password")

    mycursor =conn.cursor()
    mycursor.execute("""select  
                            TABLE_CATALOG as [Database],
                            [TABLE_SCHEMA],TABLE_NAME,
                            count(COLUMN_NAME)as column_count from INFORMATION_SCHEMA.COLUMNS
                            Group by TABLE_CATALOG,[TABLE_SCHEMA],TABLE_NAME 
                            order by TABLE_NAME""")

    for i in mycursor:
        print(json.loads(i))

    Table = input("you want to select Table-y/n:")
    if Table=="y":
        try:
            Tablename=input("Table name ")
            mycursor.execute(f"select * from {Tablename}")
            for i in mycursor:
                print(i)
        except Exception:
            print("selected table not present in a database")
    elif Table=="n":
        print("Thank you")
    else:
        print("Wrong input please select y/n")

#--------------------------------------- mysql connections------------------------------------------------
elif Database =="Mysql":
    user_input =True
   # SQL server connections
    while user_input:
        conn= mysql.connector.connect(host=input("host "),
        user = input("user name "),
        password=input("password "))
        #database=input("database "))
        if True:
            print("connection is successful")
            break
        else:
            print("not connected")

    mycursor =conn.cursor()
    mycursor.execute("Show tables")

    for i in mycursor:
        print(i)

    Table = input("you want to select Table-y/n:")
    if Table=="y":
        try:
            Tablename=input("Table name ")
            mycursor.execute(f"select * from {Tablename}")
            for i in mycursor:
                print(i)
        except Exception:
            print("selected table not present in a database")

elif  Database =="Postgresql":
    user_input =True
    while user_input:
        conn = psycopg2.connect(host="ec2-35-162-194-10.us-west-2.compute.amazonaws.com",
        user = input("user name "),
        password=input("password "),
        database=input("database "))
        if True:
            print("connection is successful")
            break
        else:
            print("not connected")

    mycursor =conn.cursor()
    mycursor.execute("Show databases")

    for i in mycursor:
        print(i)

    Table = input("you want to select Table-y/n:")
    if Table=="y":
        try:
            Tablename=input("Table name ")
            mycursor.execute(f"select * from {Tablename}")
            for i in mycursor:
                print(i)
        except Exception:
            print("selected table not present in a database")
    #---------------------------------------SQL lite-----------------------------
elif  Database =="SQLlite":
    user_input =True
    while user_input:
        conn= connection = sqlite3.connect(DATABASES['sqlite'])	
        if True:
            print("connection is successful")
            break
        else:
            print("not connected")

    mycursor =conn.cursor()
    mycursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

    for i in mycursor:
        print(i)

    Table = input("you want to select Table-y/n:")
    if Table=="y":
        try:
            Tablename=input(" nameTable ")
            mycursor.execute(f"select * from {Tablename}")
            for i in mycursor:
                print(i)
        except Exception:
            print("selected table not present in a database")

else:
    print("Server is not listed")






"""
userinput={'host':input("host "),'USER':input("User Name "),'password':input("password "),'Driver':'ODBC Driver 13 for SQL Server','database':input("database ")}

for key,value in dbconnection.items():
    con={(key,value)}

print(con)




import mysql.connector
conn = mysql.connector.connect(host = "localhost",user = "root",password = "root")
mycursor =conn.cursor()
mycursor.execute("Show Databases")

for i in mycursor:
    print(i)
"""
