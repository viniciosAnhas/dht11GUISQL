from tkinter import *
import mysql.connector
import Adafruit_DHT as dht
import time

banco = mysql.connector.connect(

    host = 'IP',
    user = 'UserBD',
    passwd = 'Senha',
    database = 'BD'

)

janela = Tk()

janela.title("DHT11")
janela.geometry("230x120+500+250")
janela.resizable(0,0)

lbl_temp = Label(janela, text = "Temp:")
lbl_temp.grid(row=0, column = 0)

lbl_umi = Label(janela, text = "Umi:")
lbl_umi.grid(row=1, column=0)

lbl_resp_temp = Label (janela, text= "")
lbl_resp_temp.grid(row=0, column=1)

lbl_resp_umi = Label (janela, text = "")
lbl_resp_umi.grid(row=1, column=1)

lbl_C = Label(janela, text = "°C")
lbl_C.grid(row=0, column=2)

lbl_porcentagem = Label(janela, text = "%")
lbl_porcentagem.grid(row=1, column=2)

def leitura():

    time.sleep(0.5)
    
    umi, temp = dht.read_retry(dht.DHT11, 21)
       
    dados = (temp, umi)
    
    cursor = banco.cursor()
    
    query = "insert into sensor (temperatura, umidade) values (%s, %s)"

    cursor.execute(query, dados)
    
    lbl_resp_temp.configure(text=str(temp))
    lbl_resp_umi.configure(text=str(umi))
    
    banco.commit()
    
    janela.after(3000, leitura)

leitura()
janela.mainloop()