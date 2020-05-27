from Personal import *
from EquipoMaterial import *
from Operacion import *
from flask import Flask, render_template
personal=Personal()
numero=personal.numeroMusicos()
array=personal.compadreAfinemos()
InstrumentosA=[]
InstrumentosB=[]
for i in range (0,numero):
 InstrumentosA.append(array[i].prepararInstrumento())
for i in range (0,numero):
 InstrumentosB.append(array[i].tocarInstrumento())
# Creamos la instancia de Flask
app=Flask(__name__)

# Un segundo route con el nombre del parametro
@app.route('/')



def render(): 
 nombre='llegaron '+str(numero)+' musicos'
 return render_template('index.html',nombre='llegaron '+str(numero)+' musicos')
@app.route('/HTMLPage1')
def render2():
  return render_template('HTMLPage1.html',lista=InstrumentosA)
@app.route('/HTMLPage2')
def render1():
  return render_template('HTMLPage2.html',lista=InstrumentosB)
if __name__ == "_main_":
    app.run(debug=True)




   
