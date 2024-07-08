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


## Configuração
Conexão dos Componentes
Conecte o sensor DHT11 ao pino D4 do ESP32.
Conecte o módulo relé ao pino D2 do ESP32.
Configuração da Rede Wi-Fi
Substitua nome_da_rede_wifi e senha_da_rede_wifi pelas credenciais da sua rede Wi-Fi.

## Configuração do ThingSpeak
Substitua sua_chave_api_do_thingspeak pela chave de API do seu canal no ThingSpeak.

## Execução
Faça o upload do código para o ESP32.
Acompanhe a saída serial para verificar a conexão Wi-Fi e as leituras de temperatura e umidade.
Verifique os dados enviados no painel do ThingSpeak.


## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
