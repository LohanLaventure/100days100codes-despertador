import datetime
import time
import os

from datetime import datetime

#define hora
agora = datetime.now().strftime("%H:%M")

#relogio global
print(f"\r {agora}")

#som do alarme
def som():
    os.system(r'start "" ""') #SALVE O CAMINHO DO AUDIO AQUI
    
#programação do alarme
alarme = input("Digite a Hora do Alarme (HH:MM) em formato 24h: ")

#define loop de verificação
while True:
    agora = datetime.now().strftime("%H:%M")
    time.sleep(0.1)

#verifica se ta na hora do alarme tocar
    if agora == alarme: 
     som()
     break
