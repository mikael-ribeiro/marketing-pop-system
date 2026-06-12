# Marketing POP System — Setup

## Pré-requisitos
- Python 3.8+
- pip

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

1. Edite o arquivo `.env` com suas chaves:
   - `ANTHROPIC_API_KEY` — chave da API da Anthropic
   - `NOTION_TOKEN` — token de integração do Notion
   - `NOTION_ROOT_PAGE_ID` — ID da página raiz no Notion
   - `OPENAI_API_KEY` — chave OpenAI (opcional)

## Teste de Conexão

```bash
python scripts/notion_reader.py
```

## Estrutura

```
marketing-pop-system/
├── .env
├── requirements.txt
├── scripts/
│   ├── transcrever.py
│   ├── notion_reader.py
│   └── notion_publisher.py
└── skills/
    ├── pop-generator/
    ├── fase1-captura/
    ├── fase2-refinamento/
    ├── fase3-producao/
    ├── fase35-arquitetura-notion/
    └── fase4-publicacao/
```

---

**Conexões:** [[automacoes/automacoes|automacoes]]
