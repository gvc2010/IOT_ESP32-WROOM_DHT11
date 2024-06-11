Dispositivos:

ESP32WROOM
DHT11
RELÉ 5V

Configuração do hardware: Conecte o sensor de temperatura/umidade DHT11 e o módulo de relé ao ESP32, atribuindo os pinos corretos para cada dispositivo.
Desenvolvimento do código: Foi escrito um programa em MicroPython que realiza as seguintes ações:
- Lê a temperatura e umidade do sensor DHT11.
- Transmite esses dados para a plataforma ThingSpeak usando uma requisição HTTP POST.
- Liga ou desliga o relé com base nas condições estabelecidas (temperatura > 31 °C ou umidade > 70%).

Não se esqueça que para conectar ao ThingSpeak é necessário conectividade com a internet. O ESP32 não enviará os resultados ao ThingSpeak sem conexão.
Para isso pode se usar a a biblioteca 'network' do python igual está representado no código.
