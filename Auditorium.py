

#c.execute("CREATE TABLE aud(RollNO text, date integer, starttime integer,endtime integer)")
def check(roll,date,starttime,endtime):
    import sqlite3
    message=""
    conn=sqlite3.connect('aud.db')

    c=conn.cursor()
    tup=tuple([roll,date,starttime,endtime])

    audopen=9
    audclose=24
    if int(starttime)<int(audopen) or int(endtime)<int(audopen) or int(starttime)>int(audclose) or int(endtime)>int(audclose):
        message= "enter a valid time frame, Auditorium functions from 9AM to 12AM"
 
    elif int(starttime)>int(endtime):
        message= "start time should be greater than endtime, Please try again"

    else:
        c.execute("SELECT * FROM aud")
        items=c.fetchall()
        booked=[]
        for i in items:
            if i[1]==date:
                for j in range(i[2],i[3]):
                    booked.append(int(j))

        t=0
        for i in range(int(starttime),int(endtime)):
            if i in booked:
                t=1
                break


        if t==1:
            message= "That slot is already booked please try another one"

        else:
            c.execute("INSERT INTO aud VALUES(?,?,?,?)",tup)
            message="You have booked the slot sucessfully"
    conn.commit()
    conn.close()
    return message
