# 🧠 MonBMAD — Bibliothèque Multi-Agents IA

> **BMAD Method** — Breakthrough Method for Agile AI Driven Development
> Un système de 15 agents IA spécialisés, réutilisables sur tous tes projets.

---

## C'est quoi BMAD ?

BMAD est une méthode de développement agile assistée par IA. Chaque étape du projet (analyse, architecture, développement, QA, doc...) est confiée à un agent spécialisé avec une identité, des commandes et des règles de comportement précises.

Les agents s'enchaînent via des **handoffs structurés** et partagent un contexte persistant sauvegardé automatiquement sur ton disque local.

---

## 🚀 Démarrage rapide

### Étape 1 — Configurer les variables

Dans les **instructions du projet Claude**, coller et adapter :

```
BMAD_GITHUB_URL=https://raw.githubusercontent.com/Langlois-j/MonMbad/main
BMAD_LOCAL_PATH=[chemin local de ce repo sur ton PC]
AUTOSAVE_FREQUENCY=4
AUTOSAVE_BLOCK_ON_CRITICAL=oui
```

> `BMAD_LOCAL_PATH` est le seul chemin local à renseigner — il ne sera jamais versionné.

### Étape 2 — Prompt de démarrage

Colle ce prompt dans n'importe quelle conversation Claude :

```
Tu es le système BMAD — Breakthrough Method for Agile AI Driven Development.

Lis et applique dans l'ordre :
1. [BMAD_GITHUB_URL]/core/orchestrator.md
2. L'agent demandé parmi :
   [BMAD_GITHUB_URL]/agents/[nom-agent].md

Lis les variables de configuration dans les instructions du projet.

Quand tu es prêt :
1. Détecte ton environnement (Desktop+MCP ou Web)
2. Affiche le menu court de l'agent
```

---

## 📁 Structure du repo

```
MonMbad/
├── agents/                      ← 15 agents spécialisés
│   ├── README.md                ← Documentation agents et commandes
│   ├── mary-analyst.md
│   ├── john-pm.md
│   ├── winston-architect.md
│   ├── bob-scrum.md
│   ├── alex-dev.md
│   ├── quinn-qa.md
│   ├── sophie-ux.md
│   ├── lena-dpo.md
│   ├── hugo-seo.md
│   ├── iris-seo-ia.md
│   ├── nova-ia.md
│   ├── victor-migration.md
│   ├── maya-traduction.md
│   ├── dylan-devops.md
│   └── emma-doc.md
├── core/                        ← Moteur BMAD
│   ├── orchestrator.md          ← Règles globales, autosave, handoff
│   ├── memory-architecture.md   ← Gestion du contexte inter-agents
│   ├── workflows.md             ← Quick / Standard / Enterprise Flow
│   └── agent-template.md        ← Template pour créer un nouvel agent
├── skills/                      ← Skills Claude (installables dans Claude Desktop)
│   └── bmad-autosave/
│       ├── SKILL.md             ← Sauvegarde automatique universelle
│       └── bmad-cleanup.py      ← Nettoyage des contextes orphelins
└── projects/                    ← Contextes et livrables par projet
    └── [nom-projet]/
        ├── context/             ← Mémoire persistante de chaque agent
        └── docs/                ← Livrables produits
```

---

## 👥 Les 15 agents

### Agents Projet

| Agent | Activation | Rôle |
|-------|------------|------|
| **Mary** | `*mary` / `*analyst` | Business Analyst — brainstorming, stakeholders, risques |
| **John** | `*john` / `*pm` | Product Manager — PRD, epics, user stories |
| **Winston** | `*winston` / `*architect` | Architecte — architecture, ADR, sécurité |
| **Bob** | `*bob` / `*scrum` | Scrum Master — sprints, vélocité, backlog |
| **Alex** | `*alex` / `*dev` | Développeur Senior — code, tests, refactoring |
| **Quinn** | `*quinn` / `*qa` | QA Engineer — quality gates, validation, bugs |
| **Sophie** | `*sophie` / `*ux` | UX Designer — parcours, wireframes, accessibilité |
| **Léna** | `*léna` / `*dpo` | DPO / RGPD — traitements, PIA, Privacy by Design |
| **Dylan** | `*dylan` / `*devops` | DevOps — CI/CD, Docker, déploiement, monitoring |
| **Emma** | `*emma` / `*doc` | Documentation — guides, FAQ, onboarding |

### Agents Spécialisés

| Agent | Activation | Rôle |
|-------|------------|------|
| **Hugo** | `*hugo` / `*seo` | SEO Naturel — mots-clés, audit, netlinking |
| **Iris** | `*iris` / `*geo` | SEO IA & GEO — AI Overviews, Perplexity, LLM |
| **Nova** | `*nova` / `*ia` | IA & Prompts — prompt engineering, RAG, MCP |
| **Victor** | `*victor` / `*migration` | Migration — legacy WinDev→cible, mapping WLangage |
| **Maya** | `*maya` / `*trad` | Traduction — technique, éditorial, juridique |

> Détail des commandes par agent → [`agents/README.md`](agents/README.md)

---

## 🖥️ Modes d'utilisation

### Claude Desktop + Windows-MCP ✅ (recommandé)

Les agents lisent et écrivent **directement sur le disque** via MCP, silencieusement.
Le skill `bmad-autosave` gère la sauvegarde automatique du contexte.

### Claude.ai Web 🌐

Les agents lisent via URL GitHub raw, écrivent via téléchargement ou copier-coller.

---

## ⚙️ Variables de configuration

Toutes les variables sont définies dans les **instructions du projet Claude**.
Aucun chemin local n'est hardcodé dans les fichiers agents ou core.

| Variable | Description |
|---|---|
| `BMAD_LOCAL_PATH` | Chemin local du repo sur ton PC |
| `BMAD_GITHUB_URL` | URL GitHub raw de base |
| `AUTOSAVE_FREQUENCY` | Fréquence de sauvegarde auto (défaut : 4 réponses) |
| `AUTOSAVE_BLOCK_ON_CRITICAL` | Blocage sur livrable critique (défaut : oui) |
| `CLAUDE_CONTEXT_PATH` | Dossier de sauvegarde des contextes (mode Normal) |
| `LEVELDB_PATH` | Chemin du LevelDB Claude Desktop (détecté auto si absent) |
| `WINDEV_VERSION` | Version PCSoft — visible dans Aide > À propos de WinDev |

---

## 💾 Sauvegarde automatique

Gérée par le skill `skills/bmad-autosave/SKILL.md` — deux modes :

**Mode Normal** (conversation sans agent)
```
[CLAUDE_CONTEXT_PATH]\[uuid-discussion]-[nom]\session-context.md
```

**Mode BMAD** (agent actif)
```
[BMAD_LOCAL_PATH]\projects\[nom-projet]\context\session-context.md
[BMAD_LOCAL_PATH]\projects\[nom-projet]\context\[agent]-context.md
```

| Indicateur | Signification |
|---|---|
| `💾 ✅` | Sauvegarde réussie |
| `💾 ❌ [motif]` | Échec avec raison |
| silence | Rien à sauvegarder |

Commandes : `*save` `*save-config` `*reload` `*cleanup`

---

## 🤝 Handoff inter-agents

Avant tout passage d'agent, l'agent sortant génère un bloc structuré :
```
## 🤝 Handoff [Agent sortant] → [Agent entrant]
Livrable produit | Décisions clés | Hypothèses | Points d'attention | Questions ouvertes
```
L'agent entrant confirme la lecture avant de démarrer.

---

## 📋 Commandes globales

Disponibles dans tous les agents :

| Commande | Description |
|---|---|
| `*help` | Liste complète commandes de l'agent |
| `*status` | Agent actif + livrables produits |
| `*history` | Décisions prises dans la session |
| `*exit` | Libère l'agent |
| `*yolo` | Mode autonome sans interruption |
| `*handoff [agent]` | Bloc de passation vers un agent |
| `*save` | Sauvegarde immédiate |
| `*save-config` | Modifie fréquence et blocage |
| `*reload` | Relit fichiers agent + contexte |
| `*env` | Environnement détecté et variables actives |

---

## ➕ Créer un nouvel agent

```
Tu es le système BMAD. Lis ce template :
[BMAD_GITHUB_URL]/core/agent-template.md

Crée un nouvel agent avec ces caractéristiques :
- Prénom : [PRÉNOM]
- Rôle : [RÔLE]
- Domaine : [DOMAINE]
- Activation : *[commande] / *[alias]
- Commandes spécifiques : [liste]
- Interactions : [avec qui, dans quel sens]
- Livrable principal : [chemin docs/]

Inclus obligatoirement : détection environnement, config sauvegarde,
menu court, *history, *save, *save-config, *reload, *env, *help.
Aucun chemin local hardcodé — utiliser les variables de configuration.
```

---

## 🛠️ Installation Windows-MCP

1. **Claude Desktop** — [claude.ai/download](https://claude.ai/download)
2. **Python 3.13+** — [python.org](https://python.org/downloads) — cocher "Add to PATH"
3. **UV Package Manager** — suivre la documentation officielle Windows-MCP

Claude Desktop → Paramètres → Extensions → Windows-MCP → Activer

---

*MonBMAD — Mis à jour le 12/03/2026*
