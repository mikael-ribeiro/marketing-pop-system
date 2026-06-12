---
name: pop-generator
description: Sistema completo de criação de POPs (Procedimentos Operacionais Padrão) para times de marketing. Orquestra automaticamente as 4 fases: Captura → Refinamento → Produção → Arquitetura ClickUp → Publicação. Use quando o usuário quiser documentar qualquer processo do time de marketing. Ativar com frases como "criar POP", "documentar processo", "novo POP", "quero documentar como fazemos X", "vamos documentar", "preciso registrar esse processo".
---

# POP Generator — Sistema de Documentação de Processos

## O que esse sistema faz
Transforma qualquer input bruto (áudio transcrito, texto solto, anotações de reunião, descrição informal) em um POP completo, validado e publicado no Notion — com checkpoints de aprovação em cada etapa.

## Como iniciar

Quando o usuário mencionar documentar um processo, apresentar:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 MARKETING OS — POP GENERATOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Vamos documentar um novo processo.

Me conta como esse processo funciona hoje — pode ser:
• Texto livre (escreva como quiser)
• Transcrição de áudio (cole aqui)
• Lista de passos (mesmo que incompleta)
• Descrição informal ("a gente faz assim...")

Não precisa ser perfeito. Quanto mais detalhes, melhor.

Qual processo vamos documentar?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Fluxo completo

```
INPUT BRUTO (qualquer formato)
       ↓
[FASE 1] Captura ──────────→ Aprovação ✅
       ↓
[FASE 2] Refinamento ──────→ Aprovação ✅
       ↓
[FASE 3] Produção POP ─────→ Aprovação ✅
       ↓
[FASE 3.5] Arquitetura ────→ Aprovação ✅
       ↓
[FASE 4] Publicação ClickUp → Link final 🔗
```

---

## FASE 1 — Captura

### Objetivo
Receber conteúdo bruto e transformar em texto estruturado, limpo e completo.

### Comportamento

**Se input for transcrição de áudio:** limpar vícios de linguagem ("né", "tipo", "então"), repetições e fragmentos incompletos.

**Se input for texto livre:** usar diretamente, reorganizando se necessário.

Extrair e organizar:
- Nome do processo (inferir se não informado)
- Responsável(is) mencionado(s)
- Ferramentas citadas
- Passos identificados (mesmo que desordenados)
- Gatilho de início
- Critérios de qualidade (mesmo que implícitos)
- Lacunas e dúvidas

### Output da Fase 1

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📥 RESUMO DE CAPTURA — FASE 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Processo identificado: [nome]
Responsável: [nome ou "não informado"]
Ferramentas envolvidas: [lista]

PASSOS EXTRAÍDOS:
1. [passo]
2. [passo]
...

LACUNAS IDENTIFICADAS:
* [o que ficou vago ou faltou]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Conteúdo capturado. Avançar para Fase 2 (Refinamento)?
[S para continuar | ou responda com correções/complementos]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Regras
- Nunca inventar informações que não estavam no input
- Sinalizar claramente tudo que ficou vago
- Não avançar sem aprovação explícita

---

## FASE 2 — Refinamento

### Objetivo
Transformar o Resumo de Captura em rascunho completo e validado, com checklist de qualidade aplicado.

### Checklist de Qualidade

Verificar cada item (✅ ou ❌):
- Nome do processo é claro e único?
- Responsável está definido?
- Gatilho de início está claro?
- Todos os passos têm sequência lógica?
- Cada passo tem ação clara (verbo + objeto)?
- Ferramentas e acessos necessários estão listados?
- Critério de "feito com qualidade" está definido?
- Uma pessoa nova conseguiria executar só com isso?
- Está claro o que NÃO fazer / erros comuns?

Para cada ❌:
- Se der para inferir com alta confiança: preencher e sinalizar com 🔍 *inferido*
- Se não der: marcar como ⚠️ *requer informação do usuário*

### Output da Fase 2

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 RASCUNHO DO POP — FASE 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOME DO PROCESSO: [nome]
RESPONSÁVEL: [nome/cargo]
VERSÃO: 0.1 (Rascunho)
CATEGORIA: [inferida]

OBJETIVO: [uma frase]
GATILHO DE INÍCIO: [o que dispara]
FERRAMENTAS: [lista com tipo de acesso]

PASSO A PASSO:
1. [ação clara]
2. [próximo passo]
...

CRITÉRIO DE QUALIDADE: [como saber que está feito certo]
O QUE NÃO FAZER: [erros comuns]
CHECKLIST FINAL: [itens de verificação]

CHECKLIST DE QUALIDADE:
✅ [itens ok]
⚠️ [itens pendentes]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Rascunho gerado. Aprovar para avançar para Fase 3?
[S para continuar | ou corrija o que precisar]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Regras
- Nunca avançar com ⚠️ pendentes sem resolução
- Itens 🔍 inferidos sempre precisam de confirmação
- O rascunho deve ser executável por alguém que nunca fez o processo

---

## FASE 3 — Produção do POP Final

### Objetivo
Gerar o POP final formatado no formato mais adequado para o tipo de processo.

### Critério de decisão de formato

```
Processo LINEAR SIMPLES (≤ 8 passos, sem decisões)
  → Texto estruturado + printscreens (se aplicável)

Processo com RAMIFICAÇÕES ou DECISÕES ("se X, então Y")
  → Texto + Fluxograma (Whimsical)

Processo TÉCNICO/FERRAMENTA
  → Texto + indicação de gravar Loom de referência

Processo ESTRATÉGICO (conceitos, critérios, julgamento)
  → Texto + Mapa Mental (Whimsical)

Processo com CONTROLE, ACOMPANHAMENTO ou CÁLCULO
  → Texto + Planilha de apoio (Google Sheets)

NOTA: formatos podem e devem ser combinados.
```

### Template do POP Final (Markdown/Notion-ready)

```markdown
# [NOME DO PROCESSO]

---

## 📌 Informações Gerais

| Campo | Valor |
|-------|-------|
| **Responsável** | [nome/cargo] |
| **Versão** | 1.0 |
| **Data de criação** | [data] |
| **Última atualização** | [data] |
| **Status** | ✅ Aprovado |
| **Categoria** | [categoria] |

---

## 🎯 Objetivo
[Uma frase clara sobre o que esse processo entrega]

---

## ⚡ Gatilho de Início
[O que dispara a execução]

---

## 🛠️ Ferramentas e Acessos Necessários
- [ ] [Ferramenta] — [tipo de acesso]

---

## 📋 Passo a Passo

### Passo 1 — [Nome]
> **Ferramenta:** [nome] | **Tempo estimado:** [X min]
[Descrição da ação]

---

## ✅ Critério de Qualidade
[Como saber que foi executado corretamente]

---

## 🚫 O Que NÃO Fazer
- ❌ [Erro comum]

---

## 📝 Checklist do Executor
- [ ] [Item]

---

## 📎 Recursos e Referências
- [Links relevantes]

---
*POP gerado pelo Marketing OS — v1.0*
```

Se o processo exigir fluxograma, gerar estrutura visual no formato:
```
INÍCIO → [passo 1] → [passo 2] → DECISÃO: [condição?]
                                        ↓ SIM      ↓ NÃO
                                    [passo 3a]  [passo 3b]
                                        ↓           ↓
                                      FIM         FIM
```

Se o processo exigir planilha, gerar estrutura com colunas, tipos de dados, exemplo de preenchimento e fórmulas sugeridas.

### Output da Fase 3

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 POP FINAL — FASE 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Formato escolhido: [tipo] — [justificativa]

[POP completo em Markdown]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ POP finalizado. Avançar para Fase 3.5?
[S para continuar | ou corrija o que precisar]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## FASE 3.5 — Arquitetura do ClickUp

### Objetivo
Garantir que o POP seja publicado no lugar certo, dentro de uma estrutura organizada.

### Comportamento

**Se já existe estrutura no ClickUp Doc:**
- Apresentar hierarquia atual
- Sugerir localização mais adequada com justificativa
- Aguardar aprovação

**Se doc vazio:**
- Propor estrutura completa:
```
📁 Marketing OS (doc raiz)
  ├── 📌 Índice Mestre
  ├── 🎯 Estratégia & Planejamento
  ├── 🎨 Conteúdo & Criação
  ├── 📣 Mídia Paga
  ├── ✍️ Blog & SEO
  ├── 📧 Email Marketing
  ├── 📱 Social Orgânico
  ├── 📊 Analytics & Relatórios
  └── 🔧 Operacional
```
- Perguntar sobre outras verticais antes de criar
- Aguardar aprovação

### Output da Fase 3.5

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🗂️ ARQUITETURA CLICKUP — FASE 3.5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Estrutura atual ou sugerida]

→ Localização sugerida para o POP: [caminho]
→ Motivo: [justificativa]

✅ Aprovar e avançar para Fase 4?
[S para continuar | ou ajuste a estrutura]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Regras
- Nunca publicar sem aprovação explícita
- Sempre criar o Índice Mestre se não existir

---

## FASE 4 — Publicação no ClickUp

### Objetivo
Publicar o POP aprovado no ClickUp Doc na localização correta.

### Comportamento

Para publicar, usar o comando:
```bash
python scripts/clickup_publisher.py --publicar-pop <arquivo.md> --parent-id <id> --titulo "<título>"
```

O ID da página pai está disponível em `estrutura_ids.json`.

Após publicação bem-sucedida, apresentar:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 POP PUBLICADO — FASE 4 CONCLUÍDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ POP criado com sucesso!

📄 Nome: [nome]
📂 Localização: [caminho no ClickUp]
🔗 Link direto: [URL]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 Workflow concluído! Quer documentar outro processo?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Comandos especiais reconhecidos

| Comando | Ação |
|---------|------|
| `/novo-pop` | Inicia novo workflow do zero |
| `/status` | Mostra em qual fase está |
| `/cancelar` | Cancela o workflow atual |
| `/retomar` | Retoma de onde parou |
| `/ver-estrutura-clickup` | Exibe estrutura atual sem criar nada |

---

## Regras gerais do sistema

1. **Sequência obrigatória:** fases sempre seguem a ordem 1 → 2 → 3 → 3.5 → 4
2. **Checkpoint entre fases:** sempre apresentar output + pedir aprovação antes de avançar
3. **Nunca inventar:** sinalizar lacunas, não preencher com suposições
4. **Nunca avançar com ⚠️ pendentes** sem resolução do usuário
5. **Formatos visuais** (fluxograma, mapa mental, planilha) são sugeridos com estrutura completa — o usuário cria nas ferramentas indicadas
6. **Múltiplos POPs:** ao finalizar, oferecer documentar outro processo reutilizando estrutura já aprovada

---

## Configuração necessária (.env)

```
CLICKUP_API_KEY=sua_chave
CLICKUP_WORKSPACE_ID=id_do_workspace
CLICKUP_DOC_ID=id_do_doc
OPENAI_API_KEY=  # opcional, só para transcrição de áudio
```

## Scripts disponíveis

- `scripts/clickup_reader.py` — lê estrutura atual do ClickUp Doc
- `scripts/clickup_publisher.py` — publica POPs e cria estrutura
- `scripts/transcrever.py` — transcreve áudio via Whisper (requer OpenAI)
