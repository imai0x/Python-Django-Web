from flask import Flask, render_template,session
app = Flask(__name__)
<<<<<<< HEAD
app.secret_key = 'Abba'
=======
app.secret_key = '123'
>>>>>>> a5fbb0e4be104f4c2c8687849049cb538113c192

@app.route('/')
def myfirstfunction():
    if not 'title' in session:
        session['title'] = 'hello world'
    return render_template('index.html', name="Mike")

if __name__ == '__main__':
  app.run(debug = True)
