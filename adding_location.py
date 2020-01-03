

import mysql.connector
import csv

'''
Augustine Valdez & Hannah Freudenberger
Database Final Project

'''

# To open Workbook and print all data
with open('student_responses.csv') as data:
    reader = csv.reader(data)

    current_students = []        

    for row in reader:
        current_students.append(row)


# for student in current_students:
#     print(student)

us = 'token_5507'
pw = 'D3qLSoNHmvkCB9c_'
try:
    cnx = mysql.connector.connect(

        user=us,
        password=pw,
        host='127.0.0.1',
        database='amv0830_finalProjecct'
    )

    cursor  = cnx.cursor()

    for student_number in range(len(current_students)):
        '''
        INSERT INTO Location
        (countryFK, state, city)
        VALUES
        ('United States of America', 'Utah', 'Salt Lake City');
        '''





    print('\nLOCATION TABLE')
    queryDegree = f'''SELECT * FROM Location'''
    cursor.execute(queryDegree)
    for item in cursor:
        print(item)
            




except mysql.connector.Error as err:
    print(err)
else: 
    #Invoked in no exception was thrown
    cnx.close()
