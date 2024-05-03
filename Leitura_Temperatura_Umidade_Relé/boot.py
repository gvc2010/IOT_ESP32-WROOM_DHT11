import dht
import machine
import time
import urequests
import network

# Configuração das credenciais da rede Wi-Fi
SSID = "nome_da_rede_wifi"
PASSWORD = "senha_da_rede_wifi"

# Inicialização do objeto WiFi
station = network.WLAN(network.STA_IF)

# Configuração do sensor DHT11
pin_dht = 4  # Pino D4 do ESP32
dht_sensor = dht.DHT11(machine.Pin(pin_dht))

# Configuração do relé
pin_relay = 2  # Pino D2 do ESP32
relay = machine.Pin(pin_relay, machine.Pin.OUT)

# Configurações do ThingSpeak
api_key_thingspeak = 'sua_chave_api_do_thingspeak'
url_thingspeak = 'https://api.thingspeak.com/update'

# Função para conectar à rede Wi-Fi
def connect_to_wifi():
    station.active(True)
    station.connect(SSID, PASSWORD)
    while not station.isconnected():
        pass
    print("Conectado à rede Wi-Fi")

def ler_temperatura_umidade():
    dht_sensor.measure()
    temp_celsius = dht_sensor.temperature()
    umidade_percentual = dht_sensor.humidity()
    return temp_celsius, umidade_percentual

def enviar_para_thingspeak(temp, umidade):
    dados = {'api_key': api_key_thingspeak, 'field1': temp, 'field2': umidade}
    resposta = urequests.post(url_thingspeak, json=dados)
    print("Status do envio para o ThingSpeak:", resposta.status_code)
    resposta.close()

def controlar_rele(temp, umidade):
    if temp > 31 or umidade > 70:
        relay.on()
    else:
        relay.off()

# Inicialização da conexão Wi-Fi
connect_to_wifi()

while True:
    try:
        temp, umidade = ler_temperatura_umidade()
        print("Temperatura:", temp, "°C, Umidade:", umidade, "%")
        
        enviar_para_thingspeak(temp, umidade)
        
        controlar_rele(temp, umidade)
    except Exception as e:
        print("Erro:", e)
    
    time.sleep(60)  # Aguarda 60 segundos antes de ler novamente
