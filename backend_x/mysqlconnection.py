#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 23:10:53 2017

@author: jcuartas
"""

import pymysql.cursors

class MySQL_Connection():
      
    def __init__(self, host, port, user, password, db):
        '''
        Initializes a MySQL_Connection object
                
        host (String): Host address
        port (Integer): Port number
        user (String): Username for the database
        password (String): Password for the database
        db (String): Database name
        charset (String): Charset by default utf-8
        cursorclass (DictCursor) : Custom cursor class to use by default DictCursor.
        connection (pymysql.connect Object) = Connection management
        
        a MySQL_Connection object has eight attributes:
            self.host (LatLng, determined by input host)
            self.port (Integer, determined by input port)
            self.user (String, determined by input user)
            self.password (String, determined by input password)
            self.db (String, determined by input db)
            self.charset (String, by default utf-8)
            self.cursorclass (DictCursor, by default DictCursor) : Custom cursor class to use by default DictCursor.
            self.connection (pymysql.connect Object, connection management according to inputs)
        '''

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = 'utf8mb4'
        self.cursorclass = pymysql.cursors.DictCursor
        self.connection = None
    
    def connect(self):
        '''
        connect()
        
        Return Value:  None
        Connects to the database, the object is stored in self.connection.
        '''
        print(self.host)
        self.connection = pymysql.connect(host = self.host,
                                   user = self.user,
                                   port = self.port,
                                   password = self.password, 
                                   db = self.db,
                                   charset = self.charset,
                                   cursorclass = self.cursorclass)
    
    def close(self):
        '''
        close()
        
        Return Value: None
        Closes connection to the database.
        '''
        self.connection.close()

    def select(self, sql):
        '''
        select(sql:String)
        
        Return Value:  Dict
        Returns result of a query to the database.
        '''
        self.connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
        except:
            return {}
        finally:
            self.close()
        
        return result

    def select_all(self, sql):
        '''
         select(sql:String)

         Return Value:  List
         Returns result of a query to the database.
         '''
        self.connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
        except:
            return []
        finally:
            self.close()

        return result
    
    def execute(self, sql):
        '''
        execute(sql:String)
        
        Return Value:  Integer
        Returns the number of rows affected after executing sql
        (Insert, Update, Delete) command.
        '''
        self.connect()
        
        try:
            with self.connection.cursor() as cursor:
                result = cursor.execute(sql)
                
            self.connection.commit()
        except:
            self.connection.rollback()
            return 0
        
        finally:
            self.connection.close()
        
        return result
            
    def delete(self, table, condition):
        '''
        delete(table:String, condition:Dict)
        
        Return Value:  Integer
        Returns the number of rows deleted.
        '''
        # table is a string
        # condition is a dictionary key (column) value (value)
        counter = 0
        sql = "DELETE FROM `" + table + "` WHERE "
        for key, value in condition.items():
            sql += "`" + key + "` = '" + value + "'"
            if counter < len(condition) - 1:
                sql += " AND "
            counter += 1
        
        result = self.execute(sql)
        
        return result
    
    def insert(self, table, columns, values):
        '''
        insert(table:String, columns:List, values:List)
        
        Return Value:  Integer
        Returns the number of rows inserted.
        '''
        sql = "INSERT INTO `" + table + "` "
        if len(columns) > 0:
            sql += "("
            counter = 0
            for i in columns:
                sql += "`"+i+"`"
                if counter < len(columns) - 1:
                    sql += ", "
                counter += 1
            sql += ")"
        sql += " VALUES ("
        counter = 0
        for j in values:
            sql += "'" + j + "'"
            if counter < len(values) - 1:
                sql += ", "
            else:
                sql += ")"
            counter += 1
        
        result = self.execute(sql)
        
        return result
    
    def update(self, table, colvalues, conditions):
        '''
        update(table:String, colvalues:Dict, conditions:Dict)
        
        Return Value:  Integer
        Returns the number of rows updated.
        '''
        
        sql = "UPDATE `" + table + "` SET "
        counter = 0
        for key, value in colvalues.items():
            sql += "`" + key + "` = '" + value + "'"
            if counter < len(colvalues) - 1:
                sql += ", "
            counter += 1
        
        if len(conditions) > 0:
            sql += " WHERE "
            counter = 0
            for key, value in conditions.items():
                sql += "`" + key + "` = '" + value + "'"
                if counter < len(conditions) - 1:
                    sql += " AND "
                counter += 1
        
        print(sql)
        result = self.execute(sql)
        
        return result


"""
Examples:
--------------------------------------    
    
table: hackathon

columns:
    id: Integer Primary Key Autoincrement
    email: String Not Null
    password: String Not Null.

"""

"""    
# Object creation
SQLConn = MySQL_Connection('localhost', 8889, 'root', 'root', 'admin_facilito')

# Select example
sql = "SELECT `id`, `password`, `email` FROM `hackathon` WHERE `email` = 'webmaster@python.org'"
r = SQLConn.select(sql)

print(r)


r2 = SQLConn.delete("hackathon", {"email":"webmaster@python.org", 'password': 'very-secret-pass'})

print("r2, delete", r2)

print("Execute query again")

r = SQLConn.select(sql)
print("Query again", r)

r3 = SQLConn.insert("hackathon", ["email", "password"], ["juan.cuartas@python.dev", "123455"])

print("Data inserted ", r3)

r4 = SQLConn.update("hackathon", {"email":"changed"}, {"id":"5"})
print(r4)

r5 = SQLConn.select("SELECT `id`, `password`, `email` FROM `hackathon`")
print(r5)

"""