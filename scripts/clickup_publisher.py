import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.clickup.com/api/v3"


def get_headers():
    token = os.getenv("CLICKUP_API_KEY")
    return {
        "Authorization": token,
        "Content-Type": "application/json",
    }


def criar_pagina(workspace_id, doc_id, titulo, parent_page_id=None):
    url = f"{BASE_URL}/workspaces/{workspace_id}/docs/{doc_id}/pages"
    payload = {
        "name": titulo,
        "content": "",
        "content_format": "text/md",
    }
    if parent_page_id:
        payload["parent_page_id"] = parent_page_id

    resp = requests.post(url, headers=get_headers(), json=payload)
    resp.raise_for_status()
    data = resp.json()
    page_id = data.get("id")
    print(f"✅ Página criada: {titulo} (ID: {page_id})")
    return data


def criar_estrutura(workspace_id, doc_id):
    secoes = {
        "📌 Índice Mestre": [],
        "🎯 Estratégia & Planejamento": ["Planejamento Mensal", "Revisão Semanal"],
        "🎨 Conteúdo & Criação": ["Criativos", "Briefing"],
        "📣 Mídia Paga": ["Google Ads", "Meta Ads"],
        "✍️ Blog & SEO": ["Artigo", "On-Page", "Calendário"],
        "📧 Email Marketing": ["Campanha", "Fluxo Nutrição"],
        "📱 Social Orgânico": ["Calendário", "Aprovação"],
        "📊 Analytics & Relatórios": ["Relatório Semanal", "Fechamento"],
        "🔧 Operacional": ["Onboarding", "Acessos"],
    }

    estrutura = {}
    for secao, subsecoes in secoes.items():
        pagina = criar_pagina(workspace_id, doc_id, secao)
        estrutura[secao] = {"id": pagina["id"], "subsecoes": {}}
        for sub in subsecoes:
            sub_pagina = criar_pagina(workspace_id, doc_id, sub, parent_page_id=pagina["id"])
            estrutura[secao]["subsecoes"][sub] = sub_pagina["id"]

    with open("estrutura_ids.json", "w", encoding="utf-8") as f:
        json.dump(estrutura, f, ensure_ascii=False, indent=2)

    print("✅ Estrutura criada e salva em estrutura_ids.json")
    return estrutura


def publicar_pop(workspace_id, doc_id, parent_page_id, titulo, markdown):
    pagina = criar_pagina(workspace_id, doc_id, titulo, parent_page_id=parent_page_id)
    page_id = pagina["id"]

    url = f"{BASE_URL}/workspaces/{workspace_id}/docs/{doc_id}/pages/{page_id}"
    payload = {
        "content": markdown,
        "content_format": "text/md",
    }
    resp = requests.put(url, headers=get_headers(), json=payload)
    resp.raise_for_status()

    clickup_url = f"https://app.clickup.com/docs/{doc_id}/{page_id}"
    print(f"✅ POP publicado: {clickup_url}")
    return clickup_url, page_id


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--criar-estrutura", action="store_true")
    parser.add_argument("--publicar-pop", metavar="ARQUIVO")
    parser.add_argument("--parent-id")
    parser.add_argument("--titulo")
    args = parser.parse_args()

    workspace_id = os.getenv("CLICKUP_WORKSPACE_ID")
    doc_id = os.getenv("CLICKUP_DOC_ID")

    if args.criar_estrutura:
        criar_estrutura(workspace_id, doc_id)
    elif args.publicar_pop:
        if not args.parent_id or not args.titulo:
            print("❌ --parent-id e --titulo são obrigatórios para publicar")
            return
        with open(args.publicar_pop, "r", encoding="utf-8") as f:
            markdown = f.read()
        publicar_pop(workspace_id, doc_id, args.parent_id, args.titulo, markdown)


if __name__ == "__main__":
    main()
