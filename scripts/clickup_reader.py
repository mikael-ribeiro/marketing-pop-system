import os
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


def get_all_pages(workspace_id, doc_id):
    url = f"{BASE_URL}/workspaces/{workspace_id}/docs/{doc_id}/pages"
    resp = requests.get(url, headers=get_headers())
    resp.raise_for_status()
    data = resp.json()
    pages = data if isinstance(data, list) else data.get("pages", [])
    return pages


def build_tree(pages, parent_page_id=None, depth=0):
    result = []
    for page in pages:
        if page.get("parent_page_id") == parent_page_id:
            node = {
                "id": page["id"],
                "title": page.get("name") or "(sem título)",
                "depth": depth,
                "children": build_tree(pages, page["id"], depth + 1),
            }
            result.append(node)
    return result


def print_tree(nodes, prefix=""):
    for i, node in enumerate(nodes):
        is_last = i == len(nodes) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node['title']} (ID: {node['id']})")
        child_prefix = prefix + ("    " if is_last else "│   ")
        print_tree(node["children"], child_prefix)


def main():
    workspace_id = os.getenv("CLICKUP_WORKSPACE_ID")
    doc_id = os.getenv("CLICKUP_DOC_ID")

    url = f"{BASE_URL}/workspaces/{workspace_id}/docs/{doc_id}"
    resp = requests.get(url, headers=get_headers())

    if resp.status_code != 200:
        print(f"❌ Erro ao conectar ao ClickUp: {resp.status_code}")
        print(resp.text)
        return

    data = resp.json()
    print(f"✅ Conectado ao doc: {data.get('name', doc_id)}")

    pages = get_all_pages(workspace_id, doc_id)
    tree = build_tree(pages)
    if not tree:
        print("(doc vazio — pronto para receber a estrutura)")
    else:
        print_tree(tree)


if __name__ == "__main__":
    main()
