from flask import Flask, render_template, Response, request
import serial
import time

serialcom = serial.Serial('COM6', 9600)
serialcom.timeout = 1

app = Flask(__name__)


def GarageOn():
    serialcom.write(str('Gon').encode())
    
def GarageOff():
	serialcom.write(str('Goff').encode())

def SalaOn():
    serialcom.write(str('Son').encode())
    
def SalaOff():
	serialcom.write(str('Soff').encode())

def BanheiroOn():
    serialcom.write(str('Bon').encode())
    
def BanheiroOff():
	serialcom.write(str('Boff').encode())

def CosinhaOn():
    serialcom.write(str('Con').encode())
    
def CosinhaOff():
	serialcom.write(str('Coff').encode())

def Quarto1On():
    serialcom.write(str('Q1on').encode())
    
def Quarto1Off():
	serialcom.write(str('Q1off').encode())

def Quarto2On():
    serialcom.write(str('Q2on').encode())
    
def Quarto2Off():
	serialcom.write(str('Q2off').encode())

def Quarto3On():
    serialcom.write(str('Q3on').encode())
    
def Quarto3Off():
	serialcom.write(str('Q3off').encode())


def disconnect():
	serialcom.close()

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if 'Gon' in request.form.to_dict():
			GarageOn()
		if 'Goff' in request.form.to_dict():
			GarageOff()
		if 'Son' in request.form.to_dict():
			SalaOn()
		if 'Soff' in request.form.to_dict():
			SalaOff()
		if 'Bon' in request.form.to_dict():
			BanheiroOn()
		if 'Boff' in request.form.to_dict():
			BanheiroOff()
		if 'Con' in request.form.to_dict():
			CosinhaOn()
		if 'Coff' in request.form.to_dict():
			CosinhaOff()
		if 'Q1on' in request.form.to_dict():
			Quarto1On()
		if 'Q1off' in request.form.to_dict():
			Quarto1Off()
		if 'Q2on' in request.form.to_dict():
			Quarto2On()
		if 'Q2off' in request.form.to_dict():
			Quarto2Off()
		if 'Q3on' in request.form.to_dict():
			Quarto3On()
		if 'Q3off' in request.form.to_dict():
			Quarto3Off()

		if 'dis' in request.form.to_dict():
			disconnect()
			
	return render_template('index.html')

if __name__ == "__main__":
    app.run()