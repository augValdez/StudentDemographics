
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
       
        # INSERTING INTO SOCIAL LIFE
        '''
        INSERT INTO SocialLife
            (personId, living ,hangout, pals, meetPals, campusHobbies, offHobbies)
            VALUES
            ((SELECT id FROM Person WHERE name = 'Augustine Valdez'), '5+ miles away from campus', 
                'Shaw', 'on campus', 'friends IN YOUR MAJOR at Westminster', 'S-cubed', 'Golfing, Hiking, Camping');

        # '''

         # print(current_students[student_number][2])
        name = current_students[student_number][2]
        # print(name)
        nameQ = f'''SELECT id FROM Person WHERE name = %s'''
        cursor.execute(nameQ, (name,))
        for id in cursor:
            print(id[0])
            id = id[0]
            
            query = f'''INSERT INTO SocialLife
                    (personId, living ,hangout, pals, meetPals, campusHobbies, offHobbies)
                    VALUES
                    (%s, %s, %s, %s, %s, %s, %s);
                    '''

            living = (current_students[student_number][13])
            hangout = (current_students[student_number][16])
            pals = (current_students[student_number][15])
            meetPals = (current_students[student_number][14])
            campusHobbies = (current_students[student_number][17])
            offHobbies = (current_students[student_number][18])

            cursor.execute(query, ((id), (living), (hangout), (pals), (meetPals), (campusHobbies), (offHobbies)))
            cnx.commit()
        
        
        
        print('living:',living, '\n','hangout:', hangout,'\n','pals:', pals, '\n', 'meetpals:', meetPals, 
        '\n', 'campushobbies:', campusHobbies, '\n', 'offhobbies:', offHobbies)


    # PRINTING OUT THE TABLES 
    print('\nSOCIAL TABLE')
    querySocial = f'''SELECT * FROM SocialLife'''
    cursor.execute(querySocial)
    for item in cursor:
        print(item)

        

except mysql.connector.Error as err:
    print(err)
else: 
    #Invoked in no exception was thrown
    cnx.close()
