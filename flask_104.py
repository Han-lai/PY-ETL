from flask import Flask, request, jsonify
# jsonify 在網頁上秀出json 單純回喘給使用者
import homework as h #取別名p
#調用別人的程式，可以這樣子做
app = Flask(__name__)

@app.route('/searchjob', methods=['GET', 'POST'])
def searchjob():
    if request.method == 'GET':
        outStr = """
          <html>
              <head>
                  <title> searchjob</title>
              </head>
              <body>
                  <h1>Search job now !</h1> 
                  <form action="/searchjob" method="post">  
                      <input type="textbox" name="jobsearch"> 
                      <button type="submit">Submit</button>
                  </form>
              </body>
          </html>
          """
        return  outStr
    elif request.method == 'POST':
        jobsearch = request.form.get('jobsearch')
        result = h.job





if __name__=='__main__':
    app.run(debug =True, host='0.0.0.0', port=5000)