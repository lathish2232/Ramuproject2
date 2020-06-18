import pyodbc
class Connections():
        def __init__(self):
                conn= pyodbc.connect(
                host= "DESKTOP-V5F828B\SQLEXPRESS",
                USER = "Testlogin",
                password ="1234",
                Driver='ODBC Driver 13 for SQL Server',
                # PORT='1433',
                database='master'
)

def createTable(self):
        try:
            with self.connection:
                self.connection.execute('''CREATE TABLE connection
                              (Connection_type text, 
                               Connection_name text, 
                               Connection_parameters text)''')
        except:
            print("connection failed")
            raise
def insert(self,Connection_type,Connection_name,Connection_parameters):
       try:
            with self.connection:
                insert_sql="""
                           insert into connection(Connection_type,Connection_name,Connection_parameters)
                           values(?,?,?)
                           """
                self.connection.execute(insert_sql,(Connection_type,Connection_name,Connection_parameters))
       except:
            self.operation_status=1
            print("insert failed")
            raise
def update(self,Connection_name,Connection_parameters):
       try:
            with self.connection:
                update_sql="""
                           update connection set Connection_parameters=:Connection_parameters
                           where Connection_name=:Connection_name
                           """
                self.connection.execute(update_sql,{'Connection_name':Connection_name,'Connection_parameters':Connection_parameters})
       except:
            self.operation_status=1
def delete(self,Connection_name):
       try:
            with self.connection:
                 delete_sql="""
                            delete from connection where Connection_name=:Connection_name
                            """
                 self.connection.execute(delete_sql,{'Connection_name':Connection_name})
       except:
            self.operation_status=1
def showConnections(self):
        try:
            cursor=self.connection.cursor()
            select_sql="""
                      select * from connection
                       """
            cursor.execute(select_sql)
            self.result=cursor.fetchall()
        except:
           self.operation_status=1
        finally:
            cursor.close()
def showConnectionData(self,Connection_name):
        try:
            cursor=self.connection.cursor()
            select_sql="""
                       select * from connection where Connection_name=:Connection_name
                       """
            cursor.execute(select_sql,{'Connection_name':Connection_name})
            self.result=cursor.fetchall()
        except:
            self.operation_status=1
        finally:
            cursor.close()
def __del__(self):
        self.connection.close()
