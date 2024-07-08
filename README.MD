## Monitoramento de Temperatura e Umidade com ESP32 e ThingSpeak
  Este repositório contém o código para monitorar temperatura e umidade utilizando um sensor DHT11 conectado a um ESP32. Os dados são enviados para a plataforma ThingSpeak para monitoramento remoto e um relé é controlado com base nas leituras de temperatura e umidade.

## Componentes Utilizados
ESP32: Microcontrolador utilizado para leitura dos sensores e controle do relé.
Sensor DHT11: Sensor utilizado para medir a temperatura e umidade.
Módulo Relé: Utilizado para controlar dispositivos elétricos com base nas leituras do sensor.
ThingSpeak: Plataforma usada para armazenar e visualizar os dados de temperatura e umidade.

## Funcionalidades
Conexão Wi-Fi: Conecta o ESP32 à rede Wi-Fi especificada.
Leitura de Sensor: Lê a temperatura e umidade do sensor DHT11.
Envio de Dados: Envia os dados lidos para o ThingSpeak.
Controle de Relé: Liga ou desliga o relé com base nas leituras de temperatura e umidade.
