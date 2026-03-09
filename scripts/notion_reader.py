#!/usr/bin/env python3
import os, sys, json, requests
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

def get_headers():
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
    token = os.getenv("NOTION_TOKEN")
    if not token:
        print("❌ NOTION_TOKEN não configurado no .env")
        sys.exit(1)
    return {"Authorization": f"Bearer {token}", "Notion-Version": NOTION_VERSION, "Content-Type": "application/json"}

def get_child_pages(page_id):
    headers = get_headers()
    children = []
    cursor = None
    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor
        response = requests.get(f"{NOTION_API_URL}/blocks/{page_id}/children", headers=headers, params=params)
        if response.status_code != 200:
            return children
        data = response.json()
        for block in data.get("results", []):
            if block.get("type") == "child_page":
                children.append({"id": block["id"], "title": block.get("child_page", {}).get("title", "Sem título")})
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return children

def build_tree(page_id, depth=0, max_depth=3):
    if depth >= max_depth:
        return []
    children = get_child_pages(page_id)
    result = []
    for child in children:
        result.append({"id": child["id"], "title": child["title"], "depth": depth, "children": build_tree(child["id"], depth+1, max_depth)})
    return result

def print_tree(nodes, prefix=""):
    for i, node in enumerate(nodes):
        is_last = i == len(nodes) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node['title']} (ID: {node['id']})")
        if node["children"]:
            print_tree(node["children"], prefix + ("    " if is_last else "│   "))

def main():
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
    root_page_id = os.getenv("NOTION_ROOT_PAGE_ID")
    if not root_page_id:
        print("❌ NOTION_ROOT_PAGE_ID não configurado no .env")
        sys.exit(1)
    headers = get_headers()
    response = requests.get(f"{NOTION_API_URL}/pages/{root_page_id}", headers=headers)
    if response.status_code != 200:
        print(f"❌ Erro ao acessar página raiz: {response.status_code}")
        print(f"   Resposta: {response.text}")
        sys.exit(1)
    print(f"✅ Conexão com Notion OK!")
    print(f"📁 Marketing OS (ID: {root_page_id})")
    tree = build_tree(root_page_id)
    if not tree:
        print("   (página vazia — pronta para receber a estrutura)")
    else:
        print_tree(tree)

if __name__ == "__main__":
    main()
