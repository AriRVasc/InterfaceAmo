from PyQt5 import uic, QtWidgets
import requests
import time
import threading

def atualiza_dados():
    while True:
        time.sleep(2)
        resposta = requests.get('http://192.168.0.***') #atualizar o ip de acordo com o codigo arduino  
        dados = resposta.text
        # Divida os dados em linhas
        linhas = dados.split('\n')
        
        umidade1 = None
        temperatura1 = None
        umidade2 = None
        temperatura2 = None
        
        # Percorra as linhas e encontre os valores de umidade e temperatura para ambos os sensores
        for linha in linhas:
            if "Sensor 1 - Umidade" in linha:
                umidade1 = linha.split(":")[1].strip()
            if "Sensor 1 - Temperatura" in linha:
                temperatura1 = linha.split(":")[1].strip()
            if "Sensor 2 - Umidade" in linha:
                umidade2 = linha.split(":")[1].strip()
            if "Sensor 2 - Temperatura" in linha:
                temperatura2 = linha.split(":")[1].strip()
        
        # Atualize as etiquetas na interface gráfica
        if umidade1 is not None:
            tela.label_7.setText(umidade1)
        if temperatura1 is not None:
            tela.label_6.setText(temperatura1)
        if umidade2 is not None:
            tela.label_9.setText(umidade2)  # Atualiza o QLabel para Sensor 2
        if temperatura2 is not None:
            tela.label_8.setText(temperatura2)  # Atualiza o QLabel para Sensor 1

app = QtWidgets.QApplication([])
tela = uic.loadUi("tela_monitor.ui")
threading.Thread(target=atualiza_dados).start()
tela.show()
app.exec()
