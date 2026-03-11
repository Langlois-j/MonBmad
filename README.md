# 🧠 BMAD Agents — Bibliothèque Multi-Projets

> **BMAD Method** — Breakthrough Method for Agile AI Driven Development
> Bibliothèque centralisée des agents IA réutilisables sur tous les projets.
> Dernière mise à jour : 11/03/2026

---

## 🚀 Prompt universel de démarrage

> Copie-colle ce prompt dans n'importe quelle conversation Claude pour démarrer BMAD from scratch.

```
Tu es le système BMAD — Breakthrough Method for Agile AI Driven Development.

Lis et applique ces fichiers dans l'ordre :
1. https://raw.githubusercontent.com/Langlois-j/MonMbad/main/core/orchestrator.md
2. L'agent demandé parmi :
   https://raw.githubusercontent.com/Langlois-j/MonMbad/main/agents/[nom-agent].md

Configuration du projet :
BMAD_LOCAL_PATH=C:\Users\langl\Documents\GitHub\MonMbad
BMAD_GITHUB_URL=https://raw.githubusercontent.com/Langlois-j/MonMbad/main
WINDEV_VERSION=[numéro visible dans Aide > À propos de WinDev]

Quand tu es prêt :
1. Détecte ton environnement (Desktop+MCP ou Web)
2. Demande la config sauvegarde (fréquence + blocage livrable)
3. Active l'agent demandé et affiche son menu court
```

---

## 🤖 Prompt pour créer un nouvel agent

> Utilise ce prompt dans une conversation Claude pour générer un nouvel agent depuis le template.

```
Tu es le système BMAD. Lis ce template :
https://raw.githubusercontent.com/Langlois-j/MonMbad/main/core/agent-template.md

Crée un nouvel agent avec ces caractéristiques :
- Prénom : [PRÉNOM]
- Rôle : [RÔLE]
- Domaine d'expertise : [DOMAINE]
- Activation : *[commande] ou *[alias]
- Commandes spécifiques : [liste des commandes métier]
- Interactions avec les autres agents : [avec qui, dans quel sens]
- Livrable principal : [chemin docs/]

Respecte exactement la structure du template.
Inclus : détection environnement, config sauvegarde, menu court, *history, *save, *save-config, *reload, *env, *help.
À la fin, affiche le fichier complet prêt à sauvegarder dans agents/[prénom]-[rôle].md
```

---

## 📁 Structure du repo

```
MonMbad/
├── agents/
│   ├── mary-analyst.md          ← Business Analyst
│   ├── john-pm.md               ← Product Manager
│   ├── winston-architect.md     ← Architecte
│   ├── bob-scrum.md             ← Scrum Master
│   ├── alex-dev.md              ← Développeur Senior
│   ├── quinn-qa.md              ← QA Engineer
│   ├── sophie-ux.md             ← UX Designer
│   ├── lena-dpo.md              ← DPO / Experte RGPD
│   ├── hugo-seo.md              ← Expert SEO Naturel
│   ├── iris-seo-ia.md           ← Expert SEO IA & GEO
│   ├── nova-ia.md               ← Experte IA, Prompts & Config
│   ├── victor-migration.md      ← Expert Migration & Modernisation
│   ├── maya-traduction.md       ← Experte Traduction Contextuelle
│   ├── dylan-devops.md          ← Expert DevOps & CI/CD
│   └── emma-doc.md              ← Experte Documentation Utilisateur
├── core/
│   ├── orchestrator.md          ← Règles globales BMAD
│   ├── memory-architecture.md   ← Gestion du contexte
│   ├── workflows.md             ← Quick / Standard / Enterprise
│   └── agent-template.md        ← Template pour créer un nouvel agent
├── projects/
│   ├── README.md                ← Comment créer un projet
│   └── _template/               ← Copier pour chaque nouveau projet
│       ├── context/             ← Mémoire de chaque agent
│       └── docs/                ← Livrables du projet
└── README.md                    ← Ce fichier
```

---

## 👥 Équipe BMAD

| Prénom | Rôle | Activation | Livrable principal |
|--------|------|------------|-------------------|
| **Mary** | Business Analyst | `*mary` ou `*analyst` | `docs/brainstorming/` |
| **John** | Product Manager | `*john` ou `*pm` | `docs/prd.md` |
| **Winston** | Architecte | `*winston` ou `*architect` | `docs/architecture.md` |
| **Bob** | Scrum Master | `*bob` ou `*scrum` | Planification sprints |
| **Alex** | Développeur Senior | `*alex` ou `*dev` | `docs/stories/` |
| **Quinn** | QA Engineer | `*quinn` ou `*qa` | `docs/qa/` |
| **Sophie** | UX Designer | `*sophie` ou `*ux` | `docs/ux/` |
| **Léna** | DPO / RGPD | `*léna` ou `*dpo` | `docs/rgpd/` |
| **Hugo** | SEO Naturel | `*hugo` ou `*seo` | `docs/seo/` |
| **Iris** | SEO IA & GEO | `*iris` ou `*geo` | `docs/seo/` |
| **Nova** | IA, Prompts & Config | `*nova` ou `*ia` | `docs/ia/` |
| **Victor** | Migration & Modernisation | `*victor` ou `*migration` | `docs/migration/` |
| **Maya** | Traduction Contextuelle | `*maya` ou `*trad` | `docs/translations/` |
| **Dylan** | DevOps & CI/CD | `*dylan` ou `*devops` | `docs/devops/` |
| **Emma** | Documentation Utilisateur | `*emma` ou `*doc` | `docs/documentation/` |

---

## 🖥️ Modes d'utilisation

### Claude Desktop + Windows-MCP ✅ (recommandé)
Les agents lisent et écrivent **directement** sur ton disque local, silencieusement.
```
BMAD_LOCAL_PATH=C:\Users\langl\Documents\GitHub\MonMbad
```

### Claude.ai Web 🌐
Les agents lisent via **URL GitHub raw**, écrivent via **téléchargement**.
```
BMAD_GITHUB_URL=https://raw.githubusercontent.com/Langlois-j/MonMbad/main
```

---

## ⚙️ Variables de configuration

| Variable | Description | Exemple |
|---|---|---|
| `BMAD_LOCAL_PATH` | Chemin local du repo | `C:\Users\langl\Documents\GitHub\MonMbad` |
| `BMAD_GITHUB_URL` | URL GitHub raw | `https://raw.githubusercontent.com/Langlois-j/MonMbad/main` |
| `WINDEV_VERSION` | Version PCSoft (Aide > À propos) | `3021011` |

> Pour changer de PC ou de configuration : modifier uniquement ces lignes dans les instructions du projet.

---

## 💾 Système de sauvegarde

| Comportement | Description |
|---|---|
| **Autosave périodique** | Toutes les N réponses (configurable, défaut 4) — silencieux |
| **Blocage livrable critique** | `*save` requis avant de continuer (configurable) |
| **`*save-config`** | Modifie fréquence et blocage en cours de session |
| **Config au démarrage** | Demandée à chaque activation d'agent |

---

## 🤝 Handoff inter-agents

Avant tout passage d'agent, l'agent sortant génère automatiquement un bloc :
```
## 🤝 Handoff [Agent sortant] → [Agent entrant]
- Livrable produit, décisions clés, hypothèses, points d'attention, questions ouvertes
```
L'agent entrant confirme la lecture avant de démarrer.

---

## 📋 Commandes globales

| Commande | Description |
|---|---|
| `*help` | Liste complète agents et commandes |
| `*status` | Agent actif + livrables produits |
| `*history` | Toutes les décisions prises dans la session |
| `*agent [prénom]` | Active un agent |
| `*exit` | Libère l'agent, retour Orchestrator |
| `*yolo` | Mode autonome sans interruption |
| `*doc-out` | Document en cours complet |
| `*think-deep [question]` | Raisonnement approfondi |
| `*challenge` | Avocat du diable sur le livrable |
| `*risk-analysis` | Analyse exhaustive des risques |
| `*simplify` | Version MVP réduite |
| `*memory-state` | État mémoire complet |
| `*export-files` | Tous les fichiers .md avec chemins |
| `*save` | Sauvegarde (auto MCP / téléchargement Web) |
| `*save-context` | Bloc reprise de session court |
| `*save-config` | Modifie config sauvegarde (fréquence, blocage) |
| `*reload` | Relit fichiers agent + contexte |
| `*env` | Affiche environnement + chemins config |
| `*handoff [agent]` | Génère le bloc de passation vers un agent |

---

## 🛠️ Installation Windows-MCP

### Prérequis
1. **Claude Desktop** — `claude.ai/download`
2. **Python 3.13+** — `python.org/downloads` (cocher "Add Python to PATH")
3. **UV Package Manager** :
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

### Activation
Claude Desktop → **Paramètres → Extensions → Windows-MCP** → Mode `local` → Enregistrer

### Autorisations recommandées
| Outil | Permission |
|---|---|
| FileSystem, Clipboard, Snapshot, Wait, Scrape, Notification | ✅ Toujours |
| PowerShell, App, Click, Type, Scroll | ⚠️ Approbation |
| Registry | ❌ Désactivé |

---

*Maintenu par l'équipe BMAD — Mis à jour le 11/03/2026*
