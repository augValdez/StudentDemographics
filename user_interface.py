'''
USER INTERFACE FINAL - Databases
Augustine Valdez
Hannah Freudenberger
'''
import mysql.connector
import csv


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

    print()
    print("Welcome to Augustine and Hannah's Final Database Final")
    print('''Our database is on the Student Demographics of Westminster.''')
    
    
    # todo = ['do laundry', 'clean bathroom', 'make dinner']
    completed = []
    within_database = False
    while within_database == False:
        
    
        print()
        print(' Here are your options: ')
        print('*enter a response by the number!*')
        print(''' 
        1. See all the students in the database. 
        2. See the students with the same OFF campus hobbies as you.
        3. See the students with the same ON campus as you. 
        4. See all the students in the same major as you.  
        5. See all the students in the same minor as you.
        6. See all the students in your same year. 
        7. Exit Database.
        ''')
        user_input = input ("enter response here: \n") 
        print('user : ', user_input)

        if user_input == '1':
            query = f'''SELECT name FROM Person'''
            cursor.execute(query)
            print('in 1')
            for person in cursor:
                person = person[0]
                print(person)


        if user_input == '2' or user_input == '3':
            user_name = input ('Enter your name! ')
            if user_input == '2':
                print('Students that have similar OFF campus hobbies.')
                #print out users off campus hobbies
                users_id = f''' SELECT id FROM Person WHERE name LIKE %s'''
                user_name += '%'
                cursor.execute(users_id, (user_name,))
                for id in cursor:
                    continue
                    # print(id)

                users_hobby = f''' SELECT offHobbies FROM SocialLife WHERE personId = %s'''
                id = id[0]
                cursor.execute(users_hobby, (id,))
                for hobby in cursor:
                    continue
                    # print(hobby)

                all_offhobbies = f''' SELECT Person.name, SocialLife.offHobbies 
                                        FROM Person
                                            INNER JOIN SocialLife ON Person.id = SocialLife.personId
                                        WHERE SocialLife.offHobbies LIKE %s;'''

                hobby = hobby[0]
                hobby = (''.join(('%',hobby,'%')))
                cursor.execute(all_offhobbies, (hobby,))
                for (name),(hobbies) in cursor:
                    print(name, ': ',hobbies)

            elif user_input == '3':
                print('Students that have the same ON campus hobbies as you. ')
                #print out users off hobbies
                users_id = f''' SELECT id FROM Person WHERE name LIKE %s'''
                user_name += '%'
                cursor.execute(users_id, (user_name,))
                for id in cursor:
                    continue
                    # print(id)
                    
                users_hobby = f''' SELECT campusHobbies FROM SocialLife WHERE personId = %s'''
                id = id[0]
                cursor.execute(users_hobby, (id,))
                for hobby in cursor:
                    continue
                    # print(hobby)

                all_campusHobbies = f''' SELECT Person.name, SocialLife.campusHobbies 
                                        FROM Person
                                            INNER JOIN SocialLife ON Person.id = SocialLife.personId
                                        WHERE SocialLife.campusHobbies LIKE %s;'''

                hobby = hobby[0]
                hobby = (''.join(('%',hobby,'%')))
                cursor.execute(all_campusHobbies, (hobby,))
                for (name),(hobbies) in cursor:
                    print(name, ': ',hobbies)
        
        elif user_input == '4':
            print('Students that have your same major.')
            #print out users major
            users_input_major = input ('Please enter your major: ')
            users_major = f''' SELECT id FROM MajorTable WHERE major LIKE %s'''

            users_input_major = (''.join(('%',users_input_major,'%')))
            cursor.execute(users_major, (users_input_major,))
            for major_id in cursor:
                continue
                # print(major_id)
            major_id = major_id[0]

            all_majors = f''' SELECT Person.name 
                                    FROM Person
                                        INNER JOIN Degree ON Person.id = Degree.personId
                                    WHERE Degree.majorId = %s'''

            cursor.execute(all_majors, (major_id,))
            for (name)in cursor:
                name = name[0]
                print(name)


        elif user_input == '5':
            print('Students that have the same minor as you.')
            #print out users minor
            users_input_minor = input ('Please enter your minor: ')
            users_minor = f''' SELECT id FROM MinorTable WHERE minor LIKE %s'''

            users_input_minor = (''.join(('%',users_input_minor,'%')))
            cursor.execute(users_minor, (users_input_minor,))
            for minor_id in cursor:
                continue
                # print(major_id)
            minor_id = minor_id[0]
            
            all_minors = f''' SELECT Person.name 
                                    FROM Person
                                        INNER JOIN Degree ON Person.id = Degree.personId
                                    WHERE Degree.minorId = %s'''

            cursor.execute(all_minors, (minor_id,))
            for (name)in cursor:
                name = name[0]
                print(name)
            
        elif user_input == '6':
            print('All students within your year.')
            #show all students wihtin the same year 
            users_name = input ('Please enter your name: ')
            users_year= f''' SELECT Degree.yearr
                            FROM Person 
                                INNER JOIN Degree ON Person.id = Degree.personId
                            WHERE name like %s;'''
            users_name += '%'
            cursor.execute(users_year, (users_name,))
            for year_standing in cursor:
                continue
                # print(year_standing)
            year_standing = year_standing[0]
            year_standing = year_standing.pop()
        
            all_users_year = f'''
                                SELECT Person.name
                                FROM Person
                                    INNER JOIN Degree ON Person.id = Degree.personId
                                WHERE yearr = %s'''

            cursor.execute(all_users_year, (year_standing,))
            for names in cursor:
                # continue
                names = names[0]
                print(names)

        elif user_input == '7':
            print('Thank you for viewing our database!')
            within_database = True

        else:
            print('\nplease enter a valid number')

    




except mysql.connector.Error as err:
    print(err)
else: 
    #Invoked in no exception was thrown
    cnx.close()