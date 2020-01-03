

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

        # INSERTING INTO DEGREE
        '''
        INSERT INTO Degree
            (personId, majorId, minorId, yearr, fourYear, job)
            VALUES
            ((SELECT id FROM Person WHERE name = 'Augustine Valdez'), (SELECT id FROM MajorTable WHERE major = 'Computer Science'), 
                (SELECT id FROM MinorTable WHERE minor = 'No minor'), 'junior', 'yes', 'yes');
        '''
        # print(current_students[student_number])

        
        name = (current_students[student_number][2])
        nameQ = f'''SELECT id FROM Person WHERE name = %s'''
        cursor.execute(nameQ, (name,))
        for id in cursor:
            # print(id[0])
            id = id[0]
          
        temp_major = (current_students[student_number][8])
        majorQ = f'''SELECT id FROM MajorTable WHERE major = %s'''
        cursor.execute(majorQ, (temp_major,))
        for major in cursor:
            # print(major[0])
            major = major[0]

        temp_minor = (current_students[student_number][9])
        minorQ = f'''SELECT id FROM MinorTable WHERE minor = %s'''
        cursor.execute(minorQ, (temp_minor,))
        for minor in cursor:
            # print(minor[0])
            minor = minor[0]

        query = f''' INSERT INTO Degree
                (personId, majorId, minorId, yearr, fourYear, job)
                VALUES
                (%s, %s, %s, %s, %s, %s);
                '''
                
        yearr = (current_students[student_number][10])
        yearr = yearr.lower()
        fourYear = (current_students[student_number][11])
        fourYear = fourYear.lower()
        job = (current_students[student_number][12])
        job = job.lower()
        
        print(id, '\n', major, '\n', minor, '\n', yearr, '\n', fourYear, '\n', job)
        cursor.execute(query, ((id), (major), (minor), (yearr), (fourYear), (job)))
        cnx.commit()
            


    print('\nDEGREE TABLE')
    queryDegree = f'''SELECT * FROM Degree'''
    cursor.execute(queryDegree)
    for item in cursor:
        print(item)
            




except mysql.connector.Error as err:
    print(err)
else: 
    #Invoked in no exception was thrown
    cnx.close()
