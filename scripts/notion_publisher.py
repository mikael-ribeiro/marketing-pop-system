#!/usr/bin/env python3
import os, sys, json, argparse, requests
from pathlib import Path
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(Path(__file__).parent.parent / ".env")

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

def get_headers():
    token = os.getenv("NOTION_TOKEN")
    if not token:
        print("❌ NOTION_TOKEN não configurado")
        sys.exit(1)
    return {"Authorization": f"Bearer {token}", "Notion-Version": NOTION_VERSION, "Content-Type": "application/json"}

def criar_pagina(parent_id, titulo):
    payload = {"parent": {"page_id": parent_id}, "properties": {"title": {"title": [{"type": "text", "text": {"content": titulo}}]}}}
    response = requests.post(f"{NOTION_API_URL}/pages", headers=get_headers(), json=payload)
    if response.status_code not in (200, 201):
        raise Exception(f"Erro ao criar '{titulo}': {response.status_code} — {response.text}")
    data = response.json()
    print(f"  ✅ Criada: {titulo} (ID: {data['id']})")
    return data

def criar_estrutura(root_id):
    print("🏗️ Criando estrutura do Marketing OS...\n")
    estrutura = [
        ("📌 Índice Mestre", []),
        ("🎯 Estratégia & Planejamento", ["Planejamento Mensal de Campanhas", "Revisão Semanal de Performance"]),
        ("🎨 Conteúdo & Criação", ["Produção de Criativos (vídeo + motion)", "Briefing de Criativo"]),
        ("📣 Mídia Paga", ["Google Ads", "Meta Ads"]),
        ("✍️ Blog & SEO", ["Produção de Artigo", "Otimização On-Page", "Calendário Editorial"]),
        ("📧 Email Marketing", ["Criação de Campanha", "Fluxo de Nutrição"]),
        ("📱 Social Orgânico", ["Calendário de Publicações", "Processo de Aprovação de Post"]),
        ("📊 Analytics & Relatórios", ["Relatório Semanal", "Fechamento Mensal de Métricas"]),
        ("🔧 Operacional", ["Onboarding de Novo Membro", "Gestão de Acessos e Ferramentas"]),
    ]
    ids = {}
    for secao, subsecoes in estrutura:
        pagina = criar_pagina(root_id, secao)
        ids[secao] = pagina["id"]
        for sub in subsecoes:
            sub_pagina = criar_pagina(pagina["id"], sub)
            ids[sub] = sub_pagina["id"]
    print(f"\n✅ Estrutura criada com sucesso!")
    with open(Path(__file__).parent.parent / "estrutura_ids.json", "w", encoding="utf-8") as f:
        json.dump(ids, f, ensure_ascii=False, indent=2)
    print("📄 IDs salvos em estrutura_ids.json")
    return ids

def markdown_para_blocks(markdown):
    blocks = []
    for line in markdown.split('\n'):
        if line.startswith('# ') and not line.startswith('## '):
            blocks.append({"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}})
        elif line.startswith('## '):
            blocks.append({"object": "block", "type": "heading_2", "heading_2": {"rich_text": [{"type": "text", "text": {"content": line[3:]}}]}})
        elif line.startswith('### '):
            blocks.append({"object": "block", "type": "heading_3", "heading_3": {"rich_text": [{"type": "text", "text": {"content": line[4:]}}]}})
        elif line.strip() == '---':
            blocks.append({"object": "block", "type": "divider", "divider": {}})
        elif line.startswith('- [ ] '):
            blocks.append({"object": "block", "type": "to_do", "to_do": {"rich_text": [{"type": "text", "text": {"content": line[6:]}}], "checked": False}})
        elif line.startswith('- ') or line.startswith('* '):
            blocks.append({"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}})
        elif line.startswith('> '):
            blocks.append({"object": "block", "type": "quote", "quote": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}})
        elif line.strip() and not line.startswith('|') and not line.startswith('```'):
            blocks.append({"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": line}}]}})
    return blocks

def publicar_pop(parent_id, titulo, markdown):
    print(f"\n📄 Publicando POP: {titulo}...")
    blocks = markdown_para_blocks(markdown)
    pagina = criar_pagina(parent_id, titulo)
    page_id = pagina["id"]
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i+100]
        requests.patch(f"{NOTION_API_URL}/blocks/{page_id}/children", headers=get_headers(), json={"children": batch})
    url = pagina.get("url", f"https://notion.so/{page_id.replace('-','')}")
    print(f"  🔗 Link: {url}")
    return url, page_id

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--criar-estrutura', action='store_true')
    parser.add_argument('--publicar-pop', type=str)
    parser.add_argument('--parent-id', type=str)
    parser.add_argument('--titulo', type=str)
    args = parser.parse_args()

    root_id = os.getenv("NOTION_ROOT_PAGE_ID")
    if not root_id:
        print("❌ NOTION_ROOT_PAGE_ID não configurado")
        sys.exit(1)

    if args.criar_estrutura:
        criar_estrutura(root_id)

    elif args.publicar_pop:
        if not args.parent_id:
            print("❌ --parent-id obrigatório")
            sys.exit(1)
        pop_file = Path(args.publicar_pop)
        if not pop_file.exists():
            print(f"❌ Arquivo não encontrado: {args.publicar_pop}")
            sys.exit(1)
        titulo = args.titulo or pop_file.stem.replace('-', ' ').title()
        markdown = pop_file.read_text(encoding='utf-8')
        publicar_pop(args.parent_id, titulo, markdown)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
