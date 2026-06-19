# 🌡️ SmartClima - Dashboard IoT

Um sistema completo de monitoramento e controle de temperatura (Internet das Coisas - IoT) integrando **Arduino**, **Python (Flask)** e uma interface web moderna (Dashboard) com dados meteorológicos em tempo real.

---

## ✨ Funcionalidades

* **Monitoramento em Tempo Real:** Leitura contínua da temperatura interna usando o sensor DHT11.
* **Comunicação Bidirecional:** O Arduino envia os dados do sensor para o painel web, e o painel web envia comandos de volta para o Arduino (acionando o sistema de climatização).
* **Dashboard Interativo (Dark Mode):** Interface moderna dividida em 3 módulos principais:
  * 🌍 **Clima Mundial:** Consumo da API pública Open-Meteo para exibir a temperatura atual de cidades globais.
  * 📜 **Sistema de Logs:** Registro em tempo real de eventos, alertas e mudanças de temperatura no sistema.
  * 🎛️ **Painel de Controle:** Visualização da temperatura local e botão de controle manual (Power).
* **Feedback Visual Físico:** LEDs conectados ao Arduino indicam se a temperatura está ideal, muito quente, ou se o sistema de ar foi acionado.

---

## 🛠️ Tecnologias Utilizadas

**Hardware:**
* Placa Arduino (Uno, Nano, Mega, etc.)
* Sensor de Temperatura e Umidade DHT11
* 3 LEDs (Verde, Vermelho e um de sua escolha para simular o Ar-Condicionado)
* Jumpers e Protoboard

**Software:**
* **C++ (Arduino IDE):** Para a lógica embarcada. Biblioteca `DHT11` de Dhruba Saha.
* **Python 3:** Backend responsável por fazer a ponte entre a porta serial e a web.
* **Flask & PySerial:** Frameworks Python para servir a página web e ler o cabo USB.
* **HTML5, CSS3, JavaScript:** Frontend puro (Vanilla), utilizando CSS Grid e Fetch API.

---

## 📂 Estrutura do Projeto

A arquitetura do projeto segue o padrão MVC adaptado para Flask, separando as responsabilidades de hardware, servidor e interface visual:

```text
projeto_ihm/
│
├── codigo_arduino.ino     # Código fonte para subir na placa Arduino
├── app.py                 # Servidor web e comunicador serial (Python)
│
├── templates/             # Pasta obrigatória do Flask para o HTML
│   └── index.html         # Estrutura principal do Dashboard
│
└── static/                # Arquivos estáticos da interface
    ├── css/
    │   └── style.css      # Estilização visual (Dark Theme)
    └── js/
        └── script.js      # Lógica da interface, Logs e consumo de APIs
```
        
## ⚡ Como Rodar o Projeto

Siga os passos abaixo para rodar o projeto localmente na sua máquina.

### 1. Configurando o Hardware (Arduino)
1. Conecte o pino de dados do sensor **DHT11** no pino digital **2** do Arduino.
2. Conecte os LEDs nos pinos digitais **8 (Verde)**, **9 (Vermelho)** e **10 (Ar-Condicionado)**.
3. Abra a Arduino IDE, instale a biblioteca `DHT11` (por Dhruba Saha) e faça o upload do código `ProvaIOT-2026.ino` para a placa.
4. **Importante:** Feche o Monitor Serial da Arduino IDE após o upload.

### 2. Configurando o Ambiente Python
Certifique-se de ter o Python 3 instalado. No terminal do seu computador, instale as dependências necessárias:

```bash
pip install flask pyserial
```
### 3. Ajustando a Porta Serial
Abra o arquivo app.py com o seu editor de texto e verifique a variável da porta serial (próximo à linha 9). Altere de acordo com a porta em que seu Arduino está conectado (ex: COM3, COM4 no Windows, ou /dev/ttyUSB0 no Linux/Mac).

Python
porta_arduino = 'COM3' # Altere para a sua porta

### 4. Iniciando o Servidor
No terminal, navegue até a pasta do projeto e rode o arquivo Python:

Bash
python app.py

### 5. Acessando o Dashboard
Abra o seu navegador de preferência e acesse o endereço local fornecido pelo Flask:
👉 http://127.0.0.1:5000