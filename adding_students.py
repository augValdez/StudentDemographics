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

    '''
    HOW WE ADDED AUGUSTINE TO TABLES:
    ---------------------------------
    INSERT INTO Person
    (name, email, ethnicity, gender, contact, needContact)
    VALUES
    ('Augustine Valdez', 'amv0830@westminstercollege.edu', 'Caucasian, Hispanic or Latino', 'Female', '801-837-2142', 'No thanks');

    INSERT INTO Degree
    (personId, majorId, minorId, yearr, fourYear, job)
    VALUES
    ((SELECT id FROM Person WHERE name = 'Augustine Valdez'), (SELECT id FROM MajorTable WHERE major = 'Computer Science'), 
        (SELECT id FROM MinorTable WHERE minor = 'No minor'), 'junior', 'yes', 'yes');

    INSERT INTO SocialLife
    (personId, living ,hangout, pals, meetPals, campusHobbies, offHobbies)
    VALUES
    ((SELECT id FROM Person WHERE name = 'Augustine Valdez'), '5+ miles away from campus', 'Shaw', 'on campus', 
        'friends IN YOUR MAJOR at Westminster', 'S-cubed', 'Golfing, Hiking, Camping');

    INSERT INTO Location
    (countryFK, state, city)
    VALUES
    ('United States of America', 'Utah', 'Salt Lake City');
    '''

    # for student in current_students:
    #     for item in student:
    #         print(item)
    

    for student_number in range(len(current_students)):
        
        # INSERTING INTO PERSON 
        '''
        INSERT INTO Person
        (name, email, ethnicity, gender, contact, needContact)
        VALUES
        ('Augustine Valdez', 'amv0830@westminstercollege.edu', 'Caucasian, Hispanic or Latino', 
            'Female', '801-837-2142', 'No thanks');
        '''
        print('in person:', current_students[student_number][1])
        query = f'''
                INSERT INTO Person
                (email, name, gender, ethnicity, contact, needContact)
                VALUES
                ( %s, %s, %s, %s, %s, %s) 
                '''

        email = (current_students[student_number][1])
        name = (current_students[student_number][2]) 
        gender = (current_students[student_number][3])
        ethnicity = (current_students[student_number][4]) 
        contact = (current_students[student_number][19])
        needContact = (current_students[student_number][20])
        cursor.execute(query, ((email), (name), (gender),(ethnicity), (contact), (needContact)))
        cnx.commit()
        
        
    # PRINTING OUT THE TABLES 
    print('\nPERSON TABLE')
    queryPerson = f'''SELECT * FROM Person'''
    cursor.execute(queryPerson)
    for item in cursor:
        print(item)
          




except mysql.connector.Error as err:
    print(err)
else: 
    #Invoked in no exception was thrown
    cnx.close()

