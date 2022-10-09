from flask import Flask, render_template, request, redirect

from users import User

app = Flask(__name__)

@app.route('/')
def leer():
    users = User.muestra_usuarios()
    return render_template('leer.html', usuarios=users)

@app.route('/new')
def new():
    return render_template('crear.html')

@app.route('/create', methods=['POST'])
def create():
    User.guardar(request.form)
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)