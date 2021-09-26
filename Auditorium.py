import sqlite3

conn=sqlite3.connect('aud.db')

c=conn.cursor()

#c.execute("CREATE TABLE aud(RollNO text, date integer, starttime integer,endtime integer)")

roll=str(input("enter roll no"))
date=int(input("enter date in DDMMYYYY format"))
starttime=int(input("enter starting time in 24 hr format"))
endtime=int(input("enter ending time in 24 hr format"))
tup=tuple([roll,date,starttime,endtime])

audopen=9
audclose=24
if starttime<audopen or endtime<audopen or starttime>audclose or endtime>audclose:
    print("enter a valid time frame")
    print("Auditorium functions from 9AM to 12AM")

elif(starttime>endtime):
    print("start time should be greater than endtime")
    print("Please try again")

else:
    c.execute("SELECT * FROM aud")
    items=c.fetchall()
    booked=[]
    for i in items:
        if (i[1]==date):
            for j in range(i[2],i[3]):
                booked.append(j)

    t=0
    for i in range(starttime,endtime):
        if i in booked:
            t=1
            break


    if t==1:
        print("That slot is already booked please try another one")
        print("the available slots on",date,"are")
        for i in range(9,24):
            if i not in booked:
                print(i,"to",i+1)

    else:
        c.execute("INSERT INTO aud VALUES(?,?,?,?)",tup)
        print("You have booked the slot sucessfully")
conn.commit()
conn.close()