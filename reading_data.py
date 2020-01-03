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


# workbook = xlrd.open_workbook("student_responses.xls")
# sheet = workbook.sheet_by_index(0) 
# DO NOT TOUCH ^^^^^^^^^^^^^^^^^^

# for i in range(sheet.ncols): 
#     for j in range(sheet.nrows):
#         print(sheet.cell_value(j, i))
#     print() 
# NOTES ABOVE

for student in current_students:
    print(student)
'''
what to do:
1 - get each row as a current student
2 - split it into individual data based off of columns
3 = add into tables
'''


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

    still_students = True
    
    while still_students:

        # this is iterating through students
        for i in range(len(current_students)-1):

            if i is len(current_students)-1:
                still_students = False

            # this is iterating through items in students
            for j in range(len(current_students[0])):

                if j is 1: 
                    '''
                        email = 1
                    '''
                    emailInput = str(current_students[i][j])
                    print('new email:',emailInput, 'i and j', i , j)

                    emaillist = []
                    query = f'''
                            SELECT email FROM Person;
                            '''
                    cursor.execute(query)
                    for (email) in cursor:
                        # print('in cursor:', email)
                        emaillist.append(email)

                    for tempe in emaillist:
                        if email is tempe:
                            i += 1
        
                    query = f'''
                    INSERT INTO Person (email) VALUES (%s)
                    '''
                    cursor.execute(query,(emailInput,))
                    
                j += 1


                # person info
                if j in (2, 3, 4, 19, 20):
                    
                    '''
                        if current_students[1][i] = "2, 3, 4, 19, 20":
                        (name,gender,ethnicty, contact, needContact)
                    '''
                    personInfo = str(current_students[i][j])
                    print(personInfo)

                    if j is 2:
                        query = f'''
                        INSERT INTO Person (name) VALUES (%s)
                        '''
                        cursor.execute(query,(personInfo,))

                    elif j is 3:
                        query = f'''
                        INSERT INTO Person (gender) VALUES (%s)
                        '''
                        cursor.execute(query,(personInfo,))
                        
                    elif j is 4:
                        query = f'''
                        INSERT INTO Person (ethnicity) VALUES (%s)
                        '''
                        cursor.execute(query,(personInfo,))

                        
                    elif j is 19:
                        query = f'''
                        INSERT INTO Person (contact) VALUES (%s)
                        '''
                        cursor.execute(query,(personInfo,))
                        
                    elif j is 20:    
                        query = f'''
                        INSERT INTO Person (needContact) VALUES (%s)
                        '''
                        cursor.execute(query,(personInfo,))
                            
                j += 1
                    
                
                # location info
                if j in (5, 6, 7):
            
                    '''
                        if current_students[1][i] = "5, 6, 7":
                        (country, state, city)
                            state and city only if country is usa
                            sql query = insert into Location table
                    '''
                    locationInfo = str(current_students[i][j])
                    print(locationInfo)
                    
                    if j is 5:
                        query = f'''
                        INSERT INTO Location (countryFK) VALUES (%s)
                        '''
                        cursor.execute(query,(locationInfo,))
                        
                    elif j is 6:
                        query = f'''
                        INSERT INTO Location (state) VALUES (%s)
                        '''
                        cursor.execute(query,(locationInfo,))

                    elif j is 7:
                        query = f'''
                        INSERT INTO Location (city) VALUES (%s)
                        '''
                        cursor.execute(query,(locationInfo,))

                j += 1
                    

                # degree info
                if j in (8, 9, 10, 11, 12):
                    
                    '''
                        if current_students[1][i] = "8, 9, 10, 11, 12":
                            (major, minor, yearstanding, 4year, job)
                    '''
                    degreeInfo = str(current_students[i][j])
                    degreeInfo = degreeInfo.islower()
                    print(degreeInfo)
                    
                    if j is 8:
                        query = f'''
                        INSERT INTO Degree (major) VALUES (%s)
                        '''
                        cursor.execute(query,(degreeInfo,))
                        
                    elif j is 9:
                        query = f'''
                        INSERT INTO Degree (minor) VALUES (%s)
                        '''
                        cursor.execute(query,(degreeInfo,))

                    elif j is 10:
                        query = f'''
                        INSERT INTO Degree (yearr) VALUES (%s)
                        '''
                        cursor.execute(query,(degreeInfo,))

                    elif j is 11:
                        query = f'''
                        INSERT INTO Degree (fourYear) VALUES (%s)
                        '''
                        cursor.execute(query,(degreeInfo,))

                    elif j is 12:
                        query = f'''
                        INSERT INTO Degree (job) VALUES (%s)
                        '''
                        cursor.execute(query,(degreeInfo,))

                j += 1

                #social life
                if j in (13, 14, 15, 16, 17, 18):   
                    print(j)                    

                    '''
                        if current_students[1][i] = "13, 14, 15, 16, 17, 18":
                            (where do you live, meetpals, hangoutwithpals, timeoncampus, campushobbies, off campus hobbies,)
                            sql query = insert into SocialLife
                    '''

                    socialInfo = str(current_students[i][j])
                    socialInfo = socialInfo.islower()
                    print(socialInfo)

                    if j is 13:
                        query = f'''
                        INSERT INTO SocialLife (living) VALUES (%s)'''
                        cursor.execute(query,(socialInfo,))

                    elif j is 14:
                        query = f'''
                        INSERT INTO SocialLife (meetPals) VALUES (%s)'''
                        cursor.execute(query,(socialInfo,))

                    elif j is 15:
                        query = f'''
                        INSERT INTO SocialLife (pals) VALUES (%s)'''
                        cursor.execute(query,(socialInfo,))

                    elif j is 16:
                        query = f'''
                        INSERT INTO SocialLife (hangout) VALUES (%s)'''
                        cursor.execute(query,(socialInfo,))

                    elif j is 17:
                        query = f'''
                        INSERT INTO SocialLife (campusHobbies) VALUES (%s)'''
                        cursor.execute(query,(socialInfo,))

                    elif j is 18:
                        query = f'''
                        INSERT INTO SocialLife (offHobbies) VALUES (%s)'''
                        cursor.execute(query,(socialInfo,))

                j += 1


    query = f'''
        SELECT * FROM Person
        '''
    cursor.execute(query)
    for item in cursor:
        print(item)


except mysql.connector.Error as err:
    print(err)
else: 
    #Invoked in no exception was thrown
    cnx.close()

