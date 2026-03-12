# 👥 Agents BMAD

Ce dossier contient les 15 agents spécialisés de la méthode BMAD.
Chaque agent est un fichier `.md` autonome qui définit son identité, ses commandes et ses règles de comportement.

---

## Comment utiliser un agent

### Claude Desktop + Windows-MCP
L'agent lit et écrit directement sur le disque local via le FileSystem MCP.
Les chemins sont lus depuis les variables de configuration du projet.

### Claude.ai Web
Colle l'URL raw GitHub de l'agent dans le prompt ou les instructions du projet :
```
https://raw.githubusercontent.com/Langlois-j/MonMbad/main/agents/[nom-agent].md
```

### Activation dans la conversation
```
*agent [prénom]   → active un agent spécifique
*exit             → libère l'agent actif
*help             → liste toutes les commandes de l'agent actif
```

---

## Les 15 agents

### 🔵 Agents Projet (cycle de vie logiciel)

| Agent | Fichier | Activation | Rôle |
|-------|---------|------------|------|
| **Mary** | `mary-analyst.md` | `*mary` / `*analyst` | Business Analyst — brainstorming, stakeholders, risques |
| **John** | `john-pm.md` | `*john` / `*pm` | Product Manager — PRD, epics, user stories, ACs |
| **Winston** | `winston-architect.md` | `*winston` / `*architect` | Architecte — architecture, ADR, sécurité, données |
| **Bob** | `bob-scrum.md` | `*bob` / `*scrum` | Scrum Master — sprints, vélocité, Definition of Ready |
| **Alex** | `alex-dev.md` | `*alex` / `*dev` | Développeur Senior — implémentation, tests, refactoring |
| **Quinn** | `quinn-qa.md` | `*quinn` / `*qa` | QA Engineer — quality gates, validation, bugs |
| **Sophie** | `sophie-ux.md` | `*sophie` / `*ux` | UX Designer — parcours, wireframes, accessibilité |
| **Léna** | `lena-dpo.md` | `*léna` / `*dpo` | DPO / RGPD — traitements, PIA, Privacy by Design |
| **Dylan** | `dylan-devops.md` | `*dylan` / `*devops` | DevOps — CI/CD, Docker, déploiement, monitoring |
| **Emma** | `emma-doc.md` | `*emma` / `*doc` | Documentation — guides, FAQ, onboarding, release notes |

### 🟢 Agents Spécialisés

| Agent | Fichier | Activation | Rôle |
|-------|---------|------------|------|
| **Hugo** | `hugo-seo.md` | `*hugo` / `*seo` | SEO Naturel — mots-clés, audit, netlinking, Core Web Vitals |
| **Iris** | `iris-seo-ia.md` | `*iris` / `*geo` | SEO IA & GEO — AI Overviews, Perplexity, citations LLM |
| **Nova** | `nova-ia.md` | `*nova` / `*ia` | IA & Prompts — prompt engineering, MCP, RAG, évaluation |
| **Victor** | `victor-migration.md` | `*victor` / `*migration` | Migration — legacy WinDev→cible, mapping WLangage, doc PCSoft |
| **Maya** | `maya-traduction.md` | `*maya` / `*trad` | Traduction contextuelle — technique, éditorial, juridique |

---

## Commandes communes à tous les agents

| Commande | Description |
|----------|-------------|
| `*help` | Liste complète des commandes de l'agent |
| `*status` | Agent actif + livrables produits |
| `*history` | Toutes les décisions prises dans la session |
| `*exit` | Libère l'agent, retour Orchestrator |
| `*yolo` | Mode autonome sans interruption |
| `*doc-out` | Affiche le document en cours complet |
| `*think-deep [question]` | Force un raisonnement approfondi |
| `*challenge` | L'agent joue l'avocat du diable |
| `*risk-analysis` | Analyse exhaustive des risques |
| `*simplify` | Propose une version MVP réduite |
| `*memory-state` | État mémoire complet |
| `*export-files` | Génère tous les fichiers .md avec chemins |
| `*save` | Sauvegarde (auto MCP / téléchargement Web) |
| `*save-context` | Bloc de reprise de session court |
| `*save-config` | Modifie la config sauvegarde (fréquence, blocage) |
| `*reload` | Relit fichiers agent + contexte |
| `*env` | Affiche environnement et chemins actifs |
| `*handoff [agent]` | Génère le bloc de passation vers un agent |

---

## Commandes spécifiques par agent

### 📊 Mary — Business Analyst
`*create-project-brief` `*brainstorm [sujet]` `*stakeholder-map` `*constraint-analysis` `*assumption-log` `*risk-radar` `*elicit` `*research-prompt [sujet]`

### 📝 John — Product Manager
`*create-prd` `*moscow-analysis` `*create-epics` `*create-stories [epic-id]` `*create-all-stories` `*edge-cases [feature]` `*shard-prd` `*checklist-review`

### 🏗️ Winston — Architecte
`*create-architecture` `*adr [décision]` `*threat-model` `*design-data-models` `*design-api` `*failure-analysis` `*shard-architecture` `*checklist-review`

### 🔄 Bob — Scrum Master
`*sprint-planning [num]` `*next-story` `*story-status` `*update-story [id] [statut]` `*ready-check [id]` `*velocity-report`

### 💻 Alex — Développeur Senior
`*dev-story [id]` `*impl-plan [id]` `*code-review` `*debug [description]` `*refactor [composant]` `*test-coverage [id]` `*security-check`

### 🧪 Quinn — QA Engineer
`*create-qa-gate [id]` `*validate-story [id]` `*test-plan [epic-id]` `*automate [id]` `*regression-check` `*bug-report [description]` `*non-functional-check`

### 🎨 Sophie — UX Designer
`*user-journey [persona]` `*wireframe [écran]` `*ux-audit [feature]` `*design-system` `*accessibility-check`

### 🔏 Léna — DPO / RGPD
`*data-mapping` `*create-ropa` `*pia [feature]` `*legal-basis [traitement]` `*privacy-by-design [composant]` `*retention-policy` `*consent-flow [feature]` `*breach-procedure` `*dpia-checklist` `*third-party-audit [service]`

### ⚙️ Dylan — DevOps & CI/CD
`*pipeline [projet]` `*docker [projet]` `*deploy [env]` `*monitor` `*infra [cloud]` `*secrets` `*rollback [service]` `*healthcheck [service]` `*env-matrix`

### 📚 Emma — Documentation
`*user-guide [module]` `*faq [sujet]` `*release-notes [version]` `*onboarding` `*glossary` `*quick-start` `*tutorial [feature]` `*admin-guide` `*troubleshooting` `*doc-audit`

### 🔍 Hugo — SEO Naturel
`*audit-seo [url]` `*keyword-strategy [sujet]` `*content-brief [mot-clé]` `*competitor-analysis [url]` `*technical-audit` `*meta-tags [page]` `*schema-markup [type]` `*internal-linking` `*content-audit` `*netlinking-strategy` `*serp-analysis [mot-clé]`

### 🤖 Iris — SEO IA & GEO
`*geo-audit [url]` `*ai-overview-strategy` `*llm-content-brief [sujet]` `*structured-data-audit` `*entity-mapping` `*aeo-strategy` `*perplexity-audit [sujet]` `*citation-strategy` `*content-rewrite [page]` `*compare-seo-geo`

### ⚡ Nova — IA & Prompts
`*prompt-review [prompt]` `*prompt-create [objectif]` `*agent-config [agent]` `*model-selection [cas]` `*system-prompt [agent]` `*rag-design` `*mcp-config [outil]` `*prompt-test [prompt]` `*workflow-ia [objectif]` `*eval-framework` `*cost-estimate [usage]` `*compare-models [tâche]`

### 🔄 Victor — Migration
`*check-source-format` `*read-legacy [fichier]` `*fetch-doc [fonction]` `*map-to [fonction] [langage]` `*learn [construct]=[équivalent]` `*migration-plan` `*inventory` `*mapping-dict` `*migrate-context` `*complexity-analysis`

### 🌐 Maya — Traduction
`*translate [texte]` `*switch-type [type]` `*set-register [registre]` `*set-lang [source]>[cible]` `*glossary` `*review [traduction]` `*back-translate` `*adapt [texte]` `*consistency-check`

---

## Créer un nouvel agent

Utilise le template disponible dans `core/agent-template.md` ou ce prompt :

```
Tu es le système BMAD. Lis ce template :
https://raw.githubusercontent.com/Langlois-j/MonMbad/main/core/agent-template.md

Crée un nouvel agent avec ces caractéristiques :
- Prénom : [PRÉNOM]
- Rôle : [RÔLE]
- Domaine d'expertise : [DOMAINE]
- Activation : *[commande] / *[alias]
- Commandes spécifiques : [liste]
- Interactions avec les autres agents : [avec qui, dans quel sens]
- Livrable principal : [chemin docs/]

Respecte exactement la structure du template.
Inclus : détection environnement, config sauvegarde, menu court, *history, *save, *save-config, *reload, *env, *help.
```
