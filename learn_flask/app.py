
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) #instance app
db = SQLAlchemy()
app.config['SECRET_KEY'] = 'KUNCI_RAHASIA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mahasiswa.db')

db.init_app(app)

class Mahasiswa(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    ttl = db.Column(db.String(15))
    fakultas = db.Column(db.String(25))
    jurusan = db.Column(db.String(25))

    def __repr__(self) -> str:
        return (self).name



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    data = Mahasiswa.query.all() #mengambil data data
    print (data)
    return render_template('home.html', mahasiswa_all=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login') #nama url
def login():
    return render_template('login.html')

@app.route('/resto')
def resto():
    return render_template('resto.html')

@app.route('/form-registrasi')
def form_regis():
    return render_template('form_registrasi.html')

@app.route('/data-from-regis', methods=['POST']) #halaman untuk melihat data yang dikirim dari form registrasi
def data():
    print(request)
    print(request.form)
    print('ini file', request.files)
    return 'success'


@app.route('/tambah', methods = ['POST'])
def tambah():

    m1 = Mahasiswa()
    m1.name = request.form['nama_lengkap']
    m1.ttl = request.form['ttl']
    m1.fakultas = request.form['fakultas']
    m1.jurusan = request.form['jurusan']

    db.session.add(m1)
    db.session.commit()
    return redirect('/home')

@app.route('/edit/<int:id>')
def edit(id):
    mahasiswa = Mahasiswa.query.filter(Mahasiswa.id==id).first()
    return render_template('edit_mahasiswa.html',mahasiswa=mahasiswa)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    mahasiswa = Mahasiswa.query.filter(Mahasiswa.id==id).first()
    mahasiswa.name = request.form['nama_lengkap']
    mahasiswa.ttl = request.form['ttl']
    mahasiswa.fakultas = request.form['fakultas']
    mahasiswa.jurusan = request.form['jurusan']

    db.session.add(mahasiswa)
    db.session.commit()
    return redirect('/home')    







