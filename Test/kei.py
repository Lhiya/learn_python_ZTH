
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) #instance app
db = SQLAlchemy()
app.config['SECRET_KEY'] = 'KUNCI_RAHASIA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mahasiswa.db')

db.init_app(app)

class Pelanggan(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    tgl_masuk = db.Column(db.String(25))
    name = db.Column(db.String(50))
    wa = db.Column(db.String(15))
    jenis_laundry = db.Column(db.String(25))
    berat = db.Column(db.Int(50))
    total_harga =db.Column(db.Int(50))
    tgl_ambil =db.Column(db.String(25))

    def __repr__(self) -> str:
        return (self).name



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rekap')
def rekap_pelanggan():
    rekap= Pelanggan.query.all() #mengambil data data
    print (rekap)
    return render_template('home.html', pelanggan_all=rekap)

@app.route('/daftar_harga')
def daftar_harga():
    harga= Pelanggan.query.all() #mengambil data data
    print(harga)
    return render_template('daftar_harga.html')

@app.route('/login') #nama url
def login():
    return render_template('login.html')

@app.route('/input')
def input_pelanggan():
    return render_template('input.html')

@app.route('/data-pelanggan', methods=['POST']) #halaman untuk melihat data yang dikirim dari form registrasi
def data():
    print(request)
    print(request.form)
    print('Data Pelanggan', request.files)
    return 'success'


@app.route('/tambah', methods = ['POST'])
def tambah():

    p1 = Pelanggan()
    p1.tgl_masuk = request.form['tgl_masuk']
    p1.nama = request.form['nama_pelanggan']
    p1.wa = request.form['wa']
    p1.jenis_laundry = request.form['jenis_laundry']
    p1.berat = request.form['berat']
    p1.total_harga =request.form['total_harga']
    p1.tgl_ambil = request.form['tgl_ambil']

    db.session.add(p1)
    db.session.commit()
    return redirect('/home')

@app.route('/edit/<int:id>')
def edit(id):
    pelanggan = Pelanggan.query.filter(Pelanggan.id==id).first()
    return render_template('edit_pelanggan.html',Pelanggan=Pelanggan)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    pelanggan = Pelanggan.query.filter(Pelanggan.id==id).first()
    p1 = Pelanggan()
    p1.tgl_masuk = request.form['tgl_masuk']
    p1.nama = request.form['nama_pelanggan']
    p1.wa = request.form['wa']
    p1.jenis_laundry = request.form['jenis_laundry']
    p1.berat = request.form['berat']
    p1.total_harga =request.form['total_harga']
    p1.tgl_ambil = request.form['tgl_ambil']

    db.session.add(Pelanggan)
    db.session.commit()
    return redirect('/rekap')    







