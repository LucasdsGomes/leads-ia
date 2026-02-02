def qualify_lead(lead: dict):
    cargo = lead.get("cargo", "").lower()
    tamanho = int(lead.get("tamanho_empresa", 0))
    mensagem = lead.get("mensagem", "").lower()

    if "ceo" in cargo or "diretor" in cargo:
        if tamanho > 50 and "entender" in mensagem or "demonstração" in mensagem:
            return {
                "score": "QUENTE",
                "motivo": "Cargo decisor e interesse claro."
            }

    return {
        "score": "MORNO",
        "motivo": "Lead com interesse, mas sem urgência clara."
    }
