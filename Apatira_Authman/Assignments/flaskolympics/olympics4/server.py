from flask import Flask, render_template,session, request
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def myfirstfunction():
    if not 'title' in session:
        session['title'] = 'hello world'
    return render_template('index.html', name="Mike")

<<<<<<< HEAD
@app.route('/do_something', methods=['POST'])
=======
@app.route('/do_something', methods=["post"])
>>>>>>> a5fbb0e4be104f4c2c8687849049cb538113c192
def mysecondfunction():
    print request.form
    session['title'] = request.form['title']
    name = "Fred"
    return render_template('index.html',name=name)

if __name__ == '__main__':
  app.run(debug = True)
