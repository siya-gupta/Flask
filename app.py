#import Flask 
from flask import Flask,redirect,url_for,render_template,request

#WSGI (Web server Gateway interface)
app = Flask(__name__)

#Decorator
@app.route('/')
def welcome():
   return render_template('index.html')

#Success Page
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>50:
        res = "Well Done !!! you are PASS"
    else:
        res = "Oopps!!! you are FAIL"
    return render_template('result.html',result=score ) 


##Fail Page
@app.route('/fail/<int:score>')
def fail(score):
    return "Oopps!!! you are Fail and your mark is= " +str(score)

'''@app.route('/Result/<int:marks>')
def Result(marks):
    results=" "
    if marks<50:
        #return "better luck Next time "
        results = 'fail'
    else: 
        results = 'success'
        #return "Yeahh!! you are success "
    return redirect(url_for(results , score = marks)) 
'''
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        Science =float(request.form['Science'])
        Math =float(request.form['Math'])
        statistic =float(request.form['statistic'])        
        Data_Science =float(request.form['Data_Science'])
        
        total_score = (Science+Math+statistic+Data_Science)/4
    
    return redirect(url_for('success',score=total_score ))    



#to check script being run inside main funtion 
if __name__ == '__main__':
    app.run(debug=True)
