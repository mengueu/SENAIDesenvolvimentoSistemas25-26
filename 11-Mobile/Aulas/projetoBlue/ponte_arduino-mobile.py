import serial

porta_bluetooth = 'COM13'
porta_arduino = 'COM12'

bt = serial.Serial(porta_bluetooth, 9600) # Porta gerada pelo pareamento Bluetooth
arduino = serial.Serial(porta_arduino, 9600) # Porta onde o Arduino está conectado

print("Ponte ativa. Aguardando comandos...")

while True:
    if bt.in_waiting > 0:
        dados = bt.read()
        print(f"Recebido: (dados)")
        arduino.write(dados)
