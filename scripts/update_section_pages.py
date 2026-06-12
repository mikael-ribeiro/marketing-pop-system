import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("CLICKUP_API_KEY")
ws = os.getenv("CLICKUP_WORKSPACE_ID")
doc = os.getenv("CLICKUP_DOC_ID")
headers = {"Authorization": token, "Content-Type": "application/json"}
base = "https://api.clickup.com/api/v3"

pages = {
    "2kz9y8cm-57": {
        "name": "Indice Mestre",
        "content": """# Marketing OS — Indice Mestre

Bem-vindo ao Marketing OS do Grupo Planning. Este documento centraliza todos os Procedimentos Operacionais Padrao (POPs) do time de marketing.

---

## Como usar este documento

Cada secao agrupa os POPs por area de atuacao. Dentro de cada secao voce encontra os processos detalhados com passo a passo, responsaveis por cargo, ferramentas e criterios de qualidade.

> Antes de executar qualquer processo pela primeira vez, leia o POP completo da secao correspondente.

---

## Estrutura do Marketing OS

| Secao | O que voce encontra la |
|---|---|
| Estrategia & Planejamento | Rituais de planejamento mensal e revisao semanal |
| Conteudo & Criacao | Fluxo de criacao de criativos e briefings |
| Midia Paga | Operacao de Meta Ads, Google Ads e cerimonia de sprint |
| Blog & SEO | Producao de artigos, otimizacao on-page e calendario |
| Email Marketing | Campanhas e fluxos de nutricao |
| Social Organico | Calendario e processo de aprovacao de posts |
| Analytics & Relatorios | Relatorio semanal e fechamento de ciclo |
| Operacional | Onboarding de novos membros e gestao de acessos |

---

## Metricas Principais do Time

| Metrica | Descricao | Meta |
|---|---|---|
| CPRMScore | Custo por Reuniao Marcada (North Star) | Menor possivel |
| CPMQL | Custo por Lead Qualificado | Abaixo de R$ 300 |
| New MRR | Receita Recorrente Nova Acumulada | R$ 4M/2026 |
| ROAS | Retorno sobre Investimento em Midia | >= 1,10 |

---

*Ultima atualizacao: maio/2026 — Marketing OS v1.0*""",
    },
    "2kz9y8cm-77": {
        "name": "Estrategia e Planejamento",
        "content": """# Estrategia & Planejamento

Esta secao reune os POPs dos rituais estrategicos do time — os processos que garantem alinhamento, priorizacao e visibilidade sobre o que esta sendo feito e por que.

---

## POPs desta secao

| POP | Responsavel | Frequencia |
|---|---|---|
| Planejamento Mensal | Head de Marketing | Mensal |
| Revisao Semanal | Head de Marketing | Semanal |

---

## Principio desta area

Estrategia sem ritual nao se sustenta. Os processos aqui existem para garantir que o time saiba onde esta, para onde vai e o que priorizar antes de executar qualquer coisa.""",
    },
    "2kz9y8cm-137": {
        "name": "Conteudo e Criacao",
        "content": """# Conteudo & Criacao

Esta secao cobre os processos de criacao de conteudo e criativos — desde o briefing inicial ate a entrega do material pronto para uso em midia paga, blog, social e demais canais.

---

## POPs desta secao

| POP | Responsavel | Quando usar |
|---|---|---|
| Criativos | Lider de Conteudo | A cada novo criativo de midia paga |
| Briefing | Lider de Conteudo | Antes de qualquer producao |

---

## Principio desta area

Nenhum criativo entra em producao sem briefing aprovado. Nenhum briefing e aprovado sem hipotese clara a ser testada.""",
    },
    "2kz9y8cm-197": {
        "name": "Midia Paga",
        "content": """# Midia Paga

Esta secao concentra os processos operacionais de midia paga — Meta Ads e Google Ads — com foco em ciclo de testes, analise de performance e otimizacao continua.

---

## POPs desta secao

| POP | Responsavel | Frequencia |
|---|---|---|
| Cerimonia de Sprint Criativa | Lider de Conteudo | Quinzenal (quinta-feira) |
| Gestao de Campanhas — Meta Ads | A definir | Continua |
| Gestao de Campanhas — Google Ads | A definir | Continua |

---

## Metricas de referencia

| Metrica | Benchmark | Observacao |
|---|---|---|
| CPRMScore | Menor possivel | North Star Metric |
| CPMQL Meta Ads | Abaixo de R$ 300 | |
| CPMQL Google Ads | Abaixo de R$ 1.112 | Historicamente mais caro |

---

## Principio desta area

Midia paga e ciencia aplicada. Cada real investido precisa de hipotese, teste e aprendizado registrado.""",
    },
    "2kz9y8cm-257": {
        "name": "Blog e SEO",
        "content": """# Blog & SEO

Esta secao cobre os processos de producao de conteudo para o blog da Planning e otimizacao para mecanismos de busca — desde a pauta ate a publicacao e indexacao.

---

## POPs desta secao

| POP | Responsavel | Frequencia |
|---|---|---|
| Producao de Artigo | Especialista de Conteudo | Conforme calendario |
| Otimizacao On-Page | Especialista de Conteudo | A cada publicacao |
| Gestao do Calendario Editorial | Lider de Conteudo | Mensal |

---

## Principio desta area

Conteudo de blog e ativo de longo prazo. Um artigo bem feito hoje gera trafego organico por anos — o processo precisa garantir qualidade tecnica e relevancia para o publico-alvo.""",
    },
    "2kz9y8cm-337": {
        "name": "Email Marketing",
        "content": """# Email Marketing

Esta secao reune os processos de criacao e disparo de campanhas de email e fluxos de nutricao — com foco em qualificacao de leads e aceleracao do pipeline comercial.

---

## POPs desta secao

| POP | Responsavel | Frequencia |
|---|---|---|
| Criacao de Campanha | Especialista de Conteudo | Conforme demanda |
| Fluxo de Nutricao | Lider de Conteudo | A cada novo segmento |

---

## Principio desta area

Email e o canal de menor custo e maior controle. O objetivo e mover o lead pelo funil sem depender exclusivamente de midia paga.""",
    },
    "2kz9y8cm-397": {
        "name": "Social Organico",
        "content": """# Social Organico

Esta secao cobre os processos de producao e publicacao de conteudo organico nas redes sociais da Planning — Instagram, LinkedIn e demais plataformas ativas.

---

## POPs desta secao

| POP | Responsavel | Frequencia |
|---|---|---|
| Gestao do Calendario de Posts | Lider de Conteudo | Mensal |
| Fluxo de Aprovacao de Conteudo | Lider de Conteudo | A cada post |

---

## Principio desta area

Social organico constroi autoridade e confianca no longo prazo. O processo de aprovacao existe para garantir consistencia de tom de voz e alinhamento com o posicionamento da Planning.""",
    },
    "2kz9y8cm-457": {
        "name": "Analytics e Relatorios",
        "content": """# Analytics & Relatorios

Esta secao cobre os processos de coleta, analise e comunicacao de resultados — do relatorio semanal ao fechamento mensal de ciclo.

---

## POPs desta secao

| POP | Responsavel | Frequencia |
|---|---|---|
| Relatorio Semanal de Performance | Head de Marketing | Semanal |
| Fechamento de Ciclo Mensal | Head de Marketing | Mensal |

---

## Ferramentas de referencia

- Power BI da Planning — dashboard principal de metricas
- Meta Ads — dados de midia paga
- Google Ads — dados de busca
- Pipedrive — dados de pipeline comercial

---

## Principio desta area

Dado sem contexto e ruido. O objetivo dos relatorios e transformar numeros em decisoes, nao em slides bonitos.""",
    },
    "2kz9y8cm-517": {
        "name": "Operacional",
        "content": """# Operacional

Esta secao cobre os processos de suporte interno do time — onboarding de novos membros, gestao de acessos e ferramentas, e demais processos administrativos do marketing.

---

## POPs desta secao

| POP | Responsavel | Quando usar |
|---|---|---|
| Onboarding de Novo Membro | Head de Marketing | A cada nova contratacao |
| Gestao de Acessos e Ferramentas | Head de Marketing | A cada entrada ou saida |

---

## Principio desta area

Um novo membro que entra sem processo estruturado custa tempo de todo o time. Um bom onboarding e o primeiro ato de gestao eficiente.""",
    },
}

for page_id, data in pages.items():
    url = f"{base}/workspaces/{ws}/docs/{doc}/pages/{page_id}"
    payload = {
        "name": data["name"],
        "content": data["content"],
        "content_format": "text/md",
    }
    r = requests.put(url, headers=headers, json=payload)
    status = "OK" if r.status_code == 200 else f"ERRO {r.status_code}"
    print(f"{status} — {data['name']}")
