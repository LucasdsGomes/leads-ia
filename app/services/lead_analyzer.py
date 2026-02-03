import requests
import json
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "deepseek/deepseek-r1-0528:free"


def qualify_lead(lead: dict) -> dict:
    """
    Recebe um lead e retorna score + motivo usando LLM
    """

    prompt = f"""
Você é um assistente comercial.

Classifique o lead abaixo como:
- QUENTE
- MORNO
- FRIO

Retorne APENAS um JSON no formato:
{{
  "score": "QUENTE | MORNO | FRIO",
  "motivo": "explicação curta"
}}

Lead:
Nome: {lead.get("nome")}
Empresa: {lead.get("empresa")}
Cargo: {lead.get("cargo")}
Tamanho da empresa: {lead.get("tamanho_empresa")}
Mensagem: {lead.get("mensagem")}
"""

    response = requests.post(
        url=OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "AI Lead Qualifier",
        },
        data=json.dumps({
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }),
        timeout=30
    )

    response.raise_for_status()

    content = response.json()["choices"][0]["message"]["content"]

    # segurança básica caso venha texto extra
    result = json.loads(content)

    return {
        "score": result["score"],
        "motivo": result["motivo"]
    }
