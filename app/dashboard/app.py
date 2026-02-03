import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Lead Qualification Dashboard",
    layout="wide"
)

st.title("📊 Lead Qualification Dashboard")
st.caption("Análise de leads qualificados automaticamente via IA e fallback")

# =========================
# Upload do CSV
# =========================
uploaded_file = st.file_uploader(
    "Faça upload do arquivo CSV de leads",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Envie um CSV exportado do Google Sheets para iniciar a análise.")
    st.stop()

# =========================
# Leitura dos dados
# =========================
df = pd.read_csv(uploaded_file)

# Normalização básica
df.columns = [c.lower() for c in df.columns]

# =========================
# Métricas principais
# =========================
total_leads = len(df)
quentes = (df["score"] == "QUENTE").sum()
mornos = (df["score"] == "MORNO").sum()
frios = (df["score"] == "FRIO").sum()

fallbacks = df["motivo"].astype(str).str.contains("Fallback", na=False).sum()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total de Leads", total_leads)
col2.metric("🔥 Quentes", quentes)
col3.metric("🟡 Mornos", mornos)
col4.metric("❄️ Frios", frios)
col5.metric("⚠️ Fallbacks", fallbacks)

st.divider()

# =========================
# Gráfico 1 — Distribuição de Leads
# =========================
st.subheader("Distribuição de Leads por Score")

fig1, ax1 = plt.subplots()
score_counts = (
    df["score"]
    .fillna("DESCONHECIDO")
    .astype(str)
    .value_counts()
)

if score_counts.empty:
    st.warning("Coluna 'score' sem dados para exibir.")
else:
    score_counts.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Score")
ax1.set_ylabel("Quantidade")

st.pyplot(fig1)

# =========================
# Gráfico 2 — Leads por Cargo
# =========================
st.subheader("Leads por Cargo")

top_cargos = df["cargo"].value_counts().head(10)

fig2, ax2 = plt.subplots()
top_cargos.plot(
    kind="barh",
    ax=ax2
)
ax2.set_xlabel("Quantidade")
ax2.set_ylabel("Cargo")

st.pyplot(fig2)

# =========================
# Gráfico 3 — IA vs Fallback
# =========================
st.subheader("Origem da Decisão")

df["decision_source"] = df["motivo"].apply(
    lambda x: "Fallback" if "Fallback" in str(x) else "IA"
)

fig3, ax3 = plt.subplots()
df["decision_source"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax3
)
ax3.set_ylabel("")

st.pyplot(fig3)

# =========================
# Tabela detalhada
# =========================
st.subheader("Detalhamento dos Leads")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# =========================
# Insights automáticos
# =========================
st.subheader("Insights Rápidos")

if quentes > mornos:
    st.success("Alta proporção de leads quentes. Pipeline saudável.")
else:
    st.warning("Maioria dos leads exige qualificação adicional.")

if fallbacks > 0:
    st.info("Parte das decisões utilizou fallback devido a indisponibilidade da IA.")

st.caption("Dashboard desenvolvido para análise operacional e tomada de decisão.")
