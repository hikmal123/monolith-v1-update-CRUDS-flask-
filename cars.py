from peewee import *
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

global appType 
appType = 'Monolith'

database = SqliteDatabase('carsweb.db')

class BaseModel(Model):
     class Meta:
        database = database

class TBCars(BaseModel):
    carname = TextField()
    carbrand = TextField()
    carmodel = TextField()
    carprice = TextField()

def create_tables():
    with database:
        database.create_tables([TBCars])

@app.route('/')
def indeks():
    return render_template('index.html', appType=appType)

@app.route('/createcar')
def createcar():
    return render_template('createcar.html', appType=appType)

@app.route('/createcarsave',methods=['GET','POST'])
def createcarsave():
    fName = request.form['carName']
    fBrand = request.form['carBrand']
    fModel = request.form['carModel']
    fPrice = request.form['carPrice']

    viewData = {
        "name" : fName,
        "brand" : fBrand,
        "model" : fModel,
        "price" : fPrice 
    }

    #simpan di DB
    car_simpan = TBCars.create(
        carname = fName,
        carbrand = fBrand,
        carmodel = fModel,
        carprice = fPrice
        )
    return redirect(url_for('readcar'))

@app.route('/readcar')
def readcar():
    rows = TBCars.select()
    return render_template('readcar.html', rows=rows, appType=appType)

@app.route('/updatecar')
def updatecar():
    carname = request.args.get('carname')
    car = None
    if carname:
        try:
            car = TBCars.get(TBCars.carname == carname)
        except:
            pass
    return render_template('updatecar.html', appType=appType, car=car)

@app.route('/updatecarsave', methods=['POST'])
def updatecarsave():
    oldName = request.form.get('oldName')
    fName = request.form['carName']
    fBrand = request.form['carBrand']
    fModel = request.form['carModel']
    fPrice = request.form['carPrice']

    if oldName:
        car_update = TBCars.update(carname=fName, carbrand=fBrand, carmodel=fModel, carprice=fPrice).where(TBCars.carname == oldName)
    else:
        car_update = TBCars.update(carbrand=fBrand, carmodel=fModel, carprice=fPrice).where(TBCars.carname == fName)
    car_update.execute()
    return redirect(url_for('readcar'))

@app.route('/deletecar')
def deletecar():
    rows = TBCars.select()
    return render_template('deletecar.html', appType=appType, rows=rows)

@app.route('/deletecarsave', methods=['POST'])
def deletecarsave():
    fName = request.form['carName']
    car_delete = TBCars.delete().where(TBCars.carname==fName)
    car_delete.execute()
    return redirect(url_for('deletecar'))

@app.route('/searchcar')
def searchcar():
    return render_template('searchcar.html', appType=appType)

@app.route('/searchcarsave', methods=['POST'])
def searchcarsave():
    fName = request.form['carName']
    rows = list(TBCars.select().where(TBCars.carname.contains(fName)))
    return render_template('searchcar.html', appType=appType, rows=rows, searched=True)

@app.route('/help')
def help():
    return "ini halaman Helps"


if __name__ == '__main__':
    create_tables()
    app.run(
        port =5010,
        host='0.0.0.0',
        debug = True
        )


