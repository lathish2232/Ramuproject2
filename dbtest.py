
import sqlite3
#from guide.api.settings import DATABASES
import DATABASES
import pyodbc
import mysql.connector
import  psycopg2
Database =input("Databasename ")
if Database =="SQLserver":
    user_input =True
   # SQL server connections
    while user_input:
        conn= pyodbc.connect(host=input("host "),
        user = input("user name "),
        password=input("password "),
        Driver='ODBC Driver 13 for SQL Server',
        database=input("database "))
        if True:
            print("connection is successful")
            break
        else:
            print("not connected")

    mycursor =conn.cursor()
    mycursor.execute("select Table_Name from INFORMATION_SCHEMA.TABLES")

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
    else:
        print("Thank you")

#--------------------------------------- mysql connections------------------------------------------------
elif Database =="Mysql":
    user_input =True
   # SQL server connections
    while user_input:
        conn= mysql.connector.connect(host=input("host "),
        user = input("user name "),
        password=input("password "),
        database=input("database "))
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
            Tablename=input("Table name ")
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
