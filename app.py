# import flask

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
# stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') # creates home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')  # additional route
def about():
    name = '30 Days of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods= ['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, time = name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))
    
if __name__ == '__main__':
    # deploy using the environment 
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

