# ZEUS⚡️P2P | Finance

![Project Banner](https://img.shields.io/badge/ZEUS-P2P_Finance-0ABAB5?style=for-the-badge&logo=telegram&logoColor=white)
![Status](https://img.shields.io/badge/Status-Online-success?style=flat-square)
![License](https://img.shields.io/badge/License-Closed_Source-red?style=flat-square)

> **O futuro das finanças descentralizadas na palma da sua mão.**
> Um Telegram Mini App completo para gestão financeira, pagamentos e saques sem burocracia.

---

## ⚡️ Sobre o Projeto

**ZEUS P2P** é um ecossistema financeiro integrado ao Telegram que permite aos usuários realizar operações financeiras com total anonimato (0 KYC). O projeto combina um **Bot em Python** robusto com um **Web App (Frontend)** moderno e responsivo.

### 🚀 Funcionalidades Principais

* **🔐 Login Integrado:** Detecção automática de usuário via Telegram e opção de login por E-mail.
* **💸 Saque PIX:** Interface intuitiva com validação de saldo, taxas automáticas e envio de comprovante.
* **🪙 Saque Cripto:** Suporte multichain (BTC, ETH, SOL, TRC20, etc.) sem taxas de rede (Gas Free).
* **🧾 Pagar Boleto:** Leitor de código de barras e cálculo de taxas de serviço.
* **💰 Gerar Cobrança:** Integração via API para gerar QR Codes PIX dinâmicos e limpos.
* **📊 Analytics Dashboard:** Gráficos interativos de performance financeira e histórico.
* **🛡️ Segurança:** Validações de saldo no frontend e backend, regras de limites mínimos/máximos e proteção contra inputs inválidos.

---

## 🛠️ Tecnologias Utilizadas

### Frontend (Mini App)
* **HTML5 / CSS3:** Estilo *Dark Glassmorphism* premium e responsivo.
* **JavaScript (Vanilla):** Lógica de negócios, validações e manipulação do DOM.
* **Telegram Web App SDK:** Integração nativa com o cliente Telegram.
* **Chart.js:** Gráficos de performance financeira.
* **QRCode.js:** Geração de QR Codes para cobrança.

### Backend (Bot & Server)
* **Python 3:** Linguagem principal.
* **pyTelegramBotAPI (Telebot):** Controle do Bot e comandos.
* **Flask:** Servidor web leve para manter o bot ativo (Keep-Alive).
* **Threading:** Execução paralela do bot e do servidor web.

---

## 📂 Estrutura do Repositório

```text
/
├── index.html          # O Mini App (Frontend) - Hospedado no GitHub Pages
├── bot.py              # O Robô (Backend) - Hospedado no Render
├── requirements.txt    # Dependências do Python
└── README.md           # Documentação
