// ==========================================
// 1. SISTEMA DE LOGS
// ==========================================
const terminalLogs = document.getElementById('terminal-logs');
let ultimoEstadoTemp = ""; // Guarda se tava frio, quente ou ideal para não flodar o log

function adicionarLog(mensagem, tipo = "normal") {
    const dataAtual = new Date();
    const horaFormatada = dataAtual.toLocaleTimeString('pt-BR');
    
    let classeCor = "";
    if(tipo === "alerta") classeCor = "log-warn";
    if(tipo === "info") classeCor = "log-info";

    const logHTML = `<div class="log-entry">
        <span class="log-time">[${horaFormatada}]</span>
        <span class="${classeCor}">${mensagem}</span>
    </div>`;
    
    // Adiciona no topo
    terminalLogs.innerHTML = logHTML + terminalLogs.innerHTML;
    
    // Limita a 50 logs para não travar o navegador
    if (terminalLogs.children.length > 50) {
        terminalLogs.removeChild(terminalLogs.lastChild);
    }
}

// ==========================================
// 2. BUSCA DE CLIMA MUNDIAL (API OPEN-METEO)
// ==========================================
// Coordenadas das cidades (Latitude e Longitude)
const cidades = [
    { nome: "Boituva, SP", lat: -23.28, lon: -47.67 },
    { nome: "Nova York, EUA", lat: 40.71, lon: -74.00 },
    { nome: "Londres, UK", lat: 51.50, lon: -0.12 },
    { nome: "Tóquio, JP", lat: 35.68, lon: 139.69 }
];

async function carregarClimaMundial() {
    const listaClima = document.getElementById('lista-clima');
    listaClima.innerHTML = ""; // Limpa a lista
    
    adicionarLog("Buscando dados meteorológicos via satélite...", "info");

    for (let cidade of cidades) {
        try {
            // Faz uma requisição para a API gratuita Open-Meteo
            const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${cidade.lat}&longitude=${cidade.lon}&current_weather=true`);
            const data = await response.json();
            const tempExterna = data.current_weather.temperature;

            listaClima.innerHTML += `
                <li class="weather-item">
                    <span class="weather-city">${cidade.nome}</span>
                    <span class="weather-temp">${tempExterna.toFixed(1)}°C</span>
                </li>
            `;
        } catch (error) {
            console.log("Erro ao buscar clima de " + cidade.nome);
        }
    }
    adicionarLog("Dados meteorológicos externos atualizados.", "normal");
}

// ==========================================
// 3. COMUNICAÇÃO COM O ARDUINO (PAINEL)
// ==========================================
let sistemaLigado = false;

async function obterDados() {
    try {
        const res = await fetch('/api/temperatura');
        const dados = await res.json();
        const temp = dados.temperatura;
        
        const tempEl = document.getElementById('temp-valor');
        const sugestaoEl = document.getElementById('texto-sugestao');
        
        tempEl.innerText = temp.toFixed(1) + " °C";
        tempEl.classList.remove('temp-frio', 'temp-ideal', 'temp-quente');

        let estadoAtual = "";

        if (temp < 22) {
            tempEl.classList.add('temp-frio');
            sugestaoEl.innerText = "Ambiente frio. Sugestão: Aquecedor.";
            estadoAtual = "frio";
        } else if (temp > 26) {
            tempEl.classList.add('temp-quente');
            sugestaoEl.innerText = "Ambiente quente. Sugestão: Ar-condicionado.";
            estadoAtual = "quente";
        } else {
            tempEl.classList.add('temp-ideal');
            sugestaoEl.innerText = "Temperatura confortável.";
            estadoAtual = "ideal";
        }

        // Se a temperatura mudar de estado (ex: de ideal pra quente), ele gera um log
        if (estadoAtual !== ultimoEstadoTemp && ultimoEstadoTemp !== "") {
            let msg = `Aviso do Sensor: Temperatura mudou para ${temp.toFixed(1)}°C. Status: ${estadoAtual.toUpperCase()}`;
            adicionarLog(msg, estadoAtual === "ideal" ? "normal" : "alerta");
        }
        ultimoEstadoTemp = estadoAtual;

    } catch (e) { 
        // Evita flodar erro no log, se quiser ver o erro use console.log
    }
}

async function enviarComandoAr() {
    try {
        await fetch('/api/comando', { method: 'POST' });
        sistemaLigado = !sistemaLigado;
        atualizarVisualBotao();
        
        adicionarLog(`Comando Manual: Sistema de Climatização foi ${sistemaLigado ? 'LIGADO' : 'DESLIGADO'}.`, "info");
    } catch (e) {
        adicionarLog("ERRO: Falha ao enviar comando para o Arduino.", "alerta");
    }
}

function atualizarVisualBotao() {
    const btn = document.getElementById('btn-power');
    const badge = document.getElementById('badge-status');

    if (sistemaLigado) {
        badge.innerText = "LIGADO";
        badge.className = "badge badge-ligado";
        btn.style.borderColor = "#10b981"; 
        btn.style.color = "#10b981";
    } else {
        badge.innerText = "DESLIGADO";
        badge.className = "badge badge-desligado";
        btn.style.borderColor = "#ef4444"; 
        btn.style.color = "#ef4444";
    }
}

// ==========================================
// INICIALIZAÇÃO
// ==========================================
adicionarLog("Sistema SmartClima iniciado.", "info");
adicionarLog("Aguardando conexão com a porta serial...", "normal");

obterDados();
carregarClimaMundial(); // Carrega o clima externo 1x ao abrir

// Fica checando o Arduino a cada 2 segundos
setInterval(obterDados, 2000);

// Atualiza o clima mundial a cada 10 minutos (600000 ms) para não sobrecarregar a API
setInterval(carregarClimaMundial, 600000);