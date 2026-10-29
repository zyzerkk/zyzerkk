<div align="center">
  <img src="./banner.svg" alt="Luís Otávio Guero — Engenharia Aeroespacial / Python & Embedded" width="100%"/>
</div>

<br/>

<img src="./about.svg" alt="Quem sou · O que faço · Visão · Além do código" width="100%"/>

<br/>

<div align="center">
  <a href="https://linkedin.com/in/luisotavioguero"><img src="./connect-linkedin.svg" alt="LinkedIn" width="140"/></a>
  <a href="https://github.com/zyzerkk"><img src="./connect-github.svg" alt="GitHub" width="140"/></a>
  <a href="mailto:contatoguero@gmail.com"><img src="./connect-gmail.svg" alt="Gmail" width="140"/></a>
</div>

<br/>

<div align="center">
  <img src="./profile-3d-contrib/profile-night-view.svg" alt="Gráfico 3D de contribuições" width="100%"/>
</div>

<br/>

<img src="./h-skills.svg" alt="Habilidades" width="100%"/>
<img src="./skills.svg" alt="Python, C++, C, TypeScript, JavaScript, PostgreSQL, MySQL, MongoDB, SQL Server, Firebird, FastAPI, Node.js, OpenAI, React, Tailwind, Vite, Arduino, NVIDIA, Colab, HuggingFace, Playwright, Docker, Git, Figma" width="100%"/>

<br/>

<img src="./h-activity.svg" alt="Atividade recente" width="100%"/>

### 🧠 NVIDIA Modulus — Digital Twins & Physics-ML
**`UFSM · GEDRE (Grupo de Estudos de Reatores Eletrônicos)`** · em andamento

Projeto Python aplicado a **Digital Twins com IA**, dentro da iniciativa de Comunicação por Luz Visível (VLC) do GEDRE. O foco é usar o **NVIDIA Modulus** (framework de Physics-Informed Machine Learning) para modelar e simular sistemas físicos.

| Etapa | Status |
|:---|:---:|
| Tentativa inicial no Visual Studio Code | ❌ Abandonada — sem tutoriais compatíveis |
| Migração para Google Colab (Python + GPU) | ✅ Concluída |
| Contorno de link quebrado no GitLab da Nvidia | ✅ Resolvido via fóruns e comunidades |
| Clonagem do repositório com token de acesso pessoal | ✅ Concluída |
| Instalação das dependências (`setup.py install`) | ✅ Concluída |
| Downgrade de versão do Python no Colab | 🟠 Em andamento |
| Execução do exemplo oficial da Nvidia | ⏳ Próximo passo |

```bash
# Ambiente: Google Colab (Python + GPU)
!git clone https://<username>:<token>@gitlab.com/nvidia/modulus/modulus.git
%cd ./modulus/
!python setup.py install
```

**Próximos passos:** finalizar o downgrade do Python, rodar o exemplo oficial da Nvidia até a conclusão, validar o ambiente e consolidar o entendimento dos conceitos-base do Modulus, e testar exemplos adicionais de aplicações.

<br/>

<img src="./h-experience.svg" alt="Experiência profissional" width="100%"/>

### Zucchetti Software e Sistemas — Suporte Técnico N1 → N3
`2021 – presente · +4 anos`

Iniciei no N1 e em **6 meses fui convidado a criar e liderar a equipe N2**. Promovido a **N3** pela capacidade de resolver problemas críticos que demandavam conhecimento profundo de banco de dados, comportamento de sistema e debugging avançado.

**Responsabilidades N3:**
- Correção de bugs em sistemas de gestão fiscal (ERP)
- Restauração de bancos de dados corrompidos via IBExpert
- Reparos em tabelas e índices no Firebird (FDB)
- Análise de logs e relatórios técnicos para diagnóstico de falhas
- Liderança técnica do time N2

<details>
<summary><b>Especialidade — Migração e Conversão de Banco de Dados (6 meses dedicados)</b></summary>

```sql
-- Pipeline de migração desenvolvido e executado em produção

-- 1. FDB → FDB: reestruturação de schema sem perda de dados
BACKUP DATABASE 'origem.fdb' TO 'backup.fbk';
RESTORE DATABASE 'backup.fbk' TO 'destino.fdb' PAGE_SIZE 8192;

-- 2. PostgreSQL → FDB: conversão de tipos e charset
-- PSQL uuid → FDB CHAR(36), PSQL jsonb → FDB BLOB SUB_TYPE TEXT

-- 3. CSV → FDB: importação massiva com validação
-- Limpeza de encoding (UTF-8/latin-1), normalização de datas

-- 4. MySQL → FDB: mapeamento de engines e collations
-- AUTO_INCREMENT → BEFORE INSERT trigger + NEXT VALUE FOR gen

-- 5. GDB → FDB: atualização de versão Firebird
```

**Ferramentas dominadas:** IBExpert · DB Visualizer · SQL Server · MySQL Workbench · MongoDB Compass · pgAdmin

</details>

<br/>

<img src="./h-projects.svg" alt="Projetos" width="100%"/>

### 🛰️ OBSAT — CubeSat Meteorológico · Equipe Halley

![OBSAT](https://img.shields.io/badge/🥇_1°_Lugar_Nacional-OBSAT_2022_e_2023-112240?style=flat-square)
![Lançamento](https://img.shields.io/badge/Lançamento_Sub--Orbital-CLBI_Natal%2FRN_Dez_2023-112240?style=flat-square)

Capitão, programador e desenvolvedor estrutural de um **CubeSat meteorológico** para detecção antecipada de tornados e ciclones tropicais em Santa Catarina. Projeto desenvolvido do zero, evoluindo por 4 fases até o lançamento real.

**Arquitetura do sistema:**

| Subsistema | Tecnologia | Especificação |
|:---|:---|:---|
| Computador de Bordo | PION Labs (C++) | Orquestra todos os módulos |
| Comunicação RF | LoRa 433 MHz · Helicoidal | 30 dBi · 100mm · 280g |
| Posicionamento | GPS + TinyGPS++ | Lat, Long, Alt, Velocidade em tempo real |
| Sensoriamento | C++/Arduino IDE | Temp, Pressão, CO₂, Acelerômetro XYZ, Giroscópio XYZ |
| Armazenamento | Cartão SD duplo (backup) | CSV organizado + backup redundante |
| Estrutura | Alumínio Aeronáutico 7075 | 100×100×100 mm · 420 g · Etaflon térmico |

**Testes de qualificação realizados:**

| Teste | Condição | Resultado |
|:---|:---|:---:|
| ❄️ Criogênico | Gelo seco → −33.33 °C | ✅ Nenhum dano |
| 🔥 Térmico | Secador → +50.65 °C | ✅ Nenhum dano |
| 🌌 Vácuo | 946 mbar → 6 mbar por 120s (parceria BRF) | ✅ Aprovado |
| 📳 Vibração | Simulação shaker, 5 repetições | ✅ Estrutura intacta |
| 🧲 Magnético | Magnetômetro x:−25.7 y:80.7 µT | ✅ Funcional |
| 💡 Luminosidade | 0% → 102% | ✅ Sensor calibrado |
| 🎈 Voo | Balão atmosférico ~40 km de altitude | ✅ Satélite ativo |

<details>
<summary><b>Ver código embarcado — telemetria, CSV e RF LoRa</b></summary>

```cpp
#include "PION_System.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include "FS.h"
#include <PION_Storage.h>
#include <ArduinoJson.h>
#include <SoftwareSerial.h>
#include <HardwareSerial.h>
#include <TinyGPS++.h>

TinyGPSPlus gps;
SoftwareSerial loraSerial(2, 3); // TX, RX

void loop() {
  DynamicJsonDocument jsonBuffer(512);
  jsonBuffer["equipe"]      = TEAM_NUM;
  jsonBuffer["bateria"]     = cubeSat.getBattery();
  jsonBuffer["temperatura"] = cubeSat.getTemperature();
  jsonBuffer["pressao"]     = cubeSat.getPressure();
  jsonBuffer["co2"]         = cubeSat.getCO2Level();

  JsonArray accel = jsonBuffer.createNestedArray("acelerometro");
  accel.add(cubeSat.getAccelerometer(0));
  accel.add(cubeSat.getAccelerometer(1));
  accel.add(cubeSat.getAccelerometer(2));

  while (Serial1.available()) {
    char cIn = Serial1.read();
    gps.encode(cIn);
    payload.add("Latitude: "  + String(gps.location.lat(), 4));
    payload.add("Longitude: " + String(gps.location.lng(), 4));
  }
}
```

**Antena selecionada: Helicoidal** — 433 MHz · 30 dBi · 280g · 100mm altura × 66mm diâmetro, escolhida pela alta direcionalidade e ganho para comunicação sub-órbita → terra, com trade-off de fragilidade a vibrações mitigado por isolamento estrutural.

</details>

---

### 🤖 Automação de Atendimento via WhatsApp com IA

Consultoria e desenvolvimento de backend Python que conecta WhatsApp Business a um LLM via API oficial, com sistema de memória contextual, fluxos de atendimento e deploy em produção.

```mermaid
flowchart TD
    A["📱 Cliente WhatsApp"] -->|mensagem| B["🔗 360Dialog API"]
    B -->|webhook POST| C["⚡ FastAPI Server"]
    C -->|histórico + prompt| D["🤖 OpenAI GPT-4o"]
    D -->|reply| C
    C -->|resposta| B
    B -->|entrega| A
```

<details>
<summary><b>Ver código do webhook FastAPI</b></summary>

```python
from fastapi import FastAPI, Request
from openai import OpenAI
import httpx

app    = FastAPI()
client = OpenAI(api_key="...")
historico: dict[str, list] = {}

@app.post("/webhook")
async def receber_mensagem(req: Request):
    body = await req.json()
    numero, texto = body["from"], body["text"]["body"]

    if numero not in historico:
        historico[numero] = [{"role": "system", "content": PROMPT_MESTRE}]

    historico[numero].append({"role": "user", "content": texto})
    resposta = client.chat.completions.create(model="gpt-4o", messages=historico[numero])
    reply = resposta.choices[0].message.content
    historico[numero].append({"role": "assistant", "content": reply})

    await enviar_whatsapp(numero, reply)
    return {"status": "ok"}
```

</details>

**Entregáveis (6 semanas):** levantamento de requisitos · backend + webhook · prompt mestre · fluxos de atendimento · deploy Render · documentação técnica · treinamento da equipe

---

### 🧪 Testes E2E Automatizados — Meta Pixel + Checkout

Suite Playwright que abre o link do criativo do anúncio, scrolla a página, clica nos botões e preenche o checkout automaticamente — validando cada evento do Meta Pixel interceptando as requisições HTTP em tempo real.

**Cobertura:**
```
✓ PageView            — pixel inicializado e disparado
✓ InitiateCheckout    — evento ao clicar no CTA
✓ Scroll comportamental — simula usuário real
✓ Preenchimento checkout — todos os campos
✓ Smoke: fbq() presente — pixel carregado
✓ Smoke: zero erros de console
✓ Desktop (Chrome) + Mobile (iPhone 14)
```

<details>
<summary><b>Ver código do teste Playwright</b></summary>

```typescript
import { test, expect } from '@playwright/test'

test('jornada completa: criativo → scroll → CTA → checkout', async ({ page }) => {
  const eventos: string[] = []

  page.on('request', (req) => {
    const url = req.url()
    if (url.includes('facebook.com/tr/')) {
      const ev = new URLSearchParams(url.split('?')[1] ?? '').get('ev')
      if (ev) eventos.push(ev)
    }
  })

  await page.goto(AD_URL, { waitUntil: 'networkidle' })
  expect(eventos).toContain('PageView')

  const cta = page.locator('button:has-text("Comprar")').first()
  await cta.click()
  await page.waitForURL(/checkout|cart/, { timeout: 8000 }).catch(() => {})
  expect(eventos).toContain('InitiateCheckout')
})
```

</details>

<br/>

<img src="./h-awards.svg" alt="Premiações" width="100%"/>

| Medalha | Competição | Período | Contexto |
|:---:|:---|:---:|:---|
| 🥇 Ouro | OBSAT — Regional e Nacional | 2022 · 2023 | CubeSat · lançamento sub-orbital CLBI/RN |
| 🥇 Ouro | MOBFOG | 2020 · 2021 | Mostra Brasileira de Foguetes |
| 🥉 Bronze | Olimpíada de Foguetes Sólidos | 2021 | — |
| 🥉 Bronze | Olimpíada Canguru de Matemática | 2021 | — |
| 🥇 Ouro | Copa Brasileira Mangahigh | 2020 | Matemática |
| 🥉 Bronze | Copa Brasileira Mangahigh | 2019 | Matemática |

<br/>

<div align="center">

`contatoguero@gmail.com` · `Santa Maria, RS · Brasil` · [`linkedin.com/in/luisotavioguero`](https://linkedin.com/in/luisotavioguero)

</div>
