import sqlite3
import oldmodel

connection = sqlite3.connect('../data/coachdata.sqlite')
cursor = connection.cursor()

import glob
import athletemodel
datafile = glob.glob('../data/*.txt')
athletes = oldmodel.put_to_store(datafile)

for each_athlete in athletes:
    name = athletes[each_athlete].name
    dob  = athletes[each_athlete].dob
    cursor.execute("INSERT INTO athletes (name,dob) VALUES(?,?)",(name, dob))
    connection.commit()

    cursor.execute("SELECT id from athletes WHERE name=? and dob=?",(name,dob))
    the_current_id = cursor.fetchone()[0]
    for each_time in set(athletes[each_athlete]):
        cursor.execute("INSERT INTO timing_data (athlete_id,value) VALUES (?,?)",(the_current_id,each_time))
    connection.commit()
connection.close()
