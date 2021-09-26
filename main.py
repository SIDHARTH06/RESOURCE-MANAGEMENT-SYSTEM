from Auditorium import *
from flask import Flask, request, render_template 
# Flask constructor
app = Flask(__name__)
@app.route('/')
def show():
   return render_template('index.html')
@app.route('/result',methods =["GET", "POST"])
def result():
      if(request.method=="POST"):
         roll = request.form.get('roll')
         date = request.form.get('date')
         starttime = request.form.get('start')
         endtime = request.form.get('end')
         msg=check(roll,date,starttime,endtime)
      return render_template("index.html",msg=msg)
if __name__ == '__main__':
   app.run(debug = True)