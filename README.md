# 🧠 Mini Treinamento Prático — Qualificação de Leads com IA e Automação

Este repositório apresenta um **mini treinamento prático** que simula um **cenário real de empresa**, focado em **automação de processos comerciais utilizando IA, APIs e análise de dados**.

O objetivo não é apenas mostrar tecnologia, mas **como tomar decisões de negócio**, lidar com **falhas reais** (limites de IA, serviços externos) e manter o fluxo operacional.

<img width="911" height="464" alt="image" src="https://github.com/user-attachments/assets/3c356148-1e78-4076-8b0b-5734f773eef0" />

---

## 🎯 Objetivo do Projeto

Demonstrar, de forma prática, como:

* Qualificar leads automaticamente
* Integrar sistemas distintos (Sheets, API, n8n, Slack)
* Utilizar IA de forma resiliente
* Gerar dados para análise e tomada de decisão

Tudo isso simulando um **treinamento interno** para times técnicos ou de automação.

---

## 🏗️ Arquitetura Geral

Fluxo simplificado:

1. **Google Sheets** — Entrada e armazenamento dos leads
2. **n8n** — Orquestração do workflow
3. **FastAPI (Python)** — API de qualificação
4. **IA (via API)** — Classificação do lead
5. **Fallback de regras** — Garantia de continuidade
6. **Slack** — Notificação automática
7. **Streamlit** — Dashboard de análise

---

## 🔁 Fluxo de Funcionamento

### 1️⃣ Entrada de Leads

Os leads são inseridos em uma planilha do Google Sheets, simulando fontes reais como formulários, CRM ou landing pages.

### 2️⃣ Orquestração com n8n

O n8n é responsável por:

* Detectar novos leads ou atualizações
* Enviar os dados para a API via HTTP Request
* Tomar decisões com base no score retornado

### 3️⃣ Qualificação com IA

A API em FastAPI tenta classificar o lead como:

* **QUENTE**
* **MORNO**
* **FRIO**

Utilizando IA para análise contextual.

### 4️⃣ Fallback Inteligente

Caso a IA esteja indisponível ou atinja limite de uso:

* Entram regras de negócio
* O fluxo **não para**
* O motivo do fallback é registrado

> Isso reflete um cenário real de produção.

### 5️⃣ Persistência dos Resultados

O score, motivo e status retornam para o Google Sheets, garantindo:

* Histórico
* Rastreabilidade
* Auditoria simples

### 6️⃣ Notificações

Com base no score:

* Leads relevantes geram mensagens automáticas no **Slack**

### 7️⃣ Análise de Dados

Os dados são consumidos por um **dashboard em Streamlit**, permitindo:

* Visualizar distribuição dos leads
* Identificar volume de fallbacks
* Apoiar decisões de negócio

---

## 🛠️ Tecnologias Utilizadas

* Python
* FastAPI
* n8n
* Google Sheets
* Streamlit
* APIs de IA
* Slack Webhook

---

## 📊 Aprendizados Demonstrados

* Integração de sistemas via API
* Automação de workflows
* Uso consciente de IA e limites
* Implementação de fallback de negócio
* Análise de dados aplicada
* Comunicação entre times técnicos e não técnicos

---

## 🚀 Conclusão

Este projeto serve como um **mini treinamento prático** para demonstrar como soluções de IA podem ser aplicadas no dia a dia de empresas, indo além do "happy path" e considerando falhas, limites e decisões reais.

---

📌 *Projeto educacional e demonstrativo*
