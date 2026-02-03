import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

def qualify_lead(lead: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Lead Qualifier"
    }

    prompt = f"""
Você é um analista comercial.
Classifique o lead como QUENTE, MORNO ou FRIO.

Dados:
Cargo: {lead.get("cargo")}
Empresa: {lead.get("empresa")}
Tamanho da empresa: {lead.get("tamanho_empresa")}
Mensagem: {lead.get("mensagem")}

Responda em JSON no formato:
{{"score": "...", "motivo": "..."}}
"""

    payload = {
        "model": "openai/gpt-oss-20b:free",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=20
        )

        if response.status_code != 200:
            raise Exception(f"OpenRouter error {response.status_code}: {response.text}")

        data = response.json()

        # Validação defensiva
        if "choices" not in data:
            raise Exception(f"Resposta inesperada: {data}")

        content = data["choices"][0]["message"]["content"]

        return eval(content)  # simples por agora

    except Exception as e:
        cargo = lead.get("cargo", "").lower()
        tamanho = lead.get("tamanho_empresa", 0)

        if "ceo" in cargo or "diretor" in cargo or tamanho >= 100:
            score = "QUENTE"
            motivo = "Fallback: cargo decisor ou empresa grande"
        else:
            score = "MORNO"
            status = "Arquivado"
            motivo = "Fallback: análise manual necessária"

        return {
            "score": score,
            "motivo": f"{motivo} | IA indisponível ({str(e)})"
        }

