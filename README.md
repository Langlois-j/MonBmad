# 🧠 BMAD Agents — Bibliothèque Multi-Projets

> **BMAD Method** — Breakthrough Method for Agile AI Driven Development  
> Bibliothèque centralisée des agents IA réutilisables sur tous les projets.

---

## 📁 Structure du repo

```
bmad-agents/
├── agents/
│   ├── mary-analyst.md          ← Business Analyst
│   ├── john-pm.md               ← Product Manager
│   ├── winston-architect.md     ← Architecte
│   ├── bob-scrum.md             ← Scrum Master
│   ├── alex-dev.md              ← Développeur Senior
│   ├── quinn-qa.md              ← QA Engineer
│   ├── sophie-ux.md             ← UX Designer
│   └── lena-dpo.md              ← DPO / Experte RGPD
├── core/
│   ├── orchestrator.md          ← Règles globales BMAD
│   ├── memory-architecture.md   ← Gestion du contexte
│   └── workflows.md             ← Quick / Standard / Enterprise
└── README.md                    ← Ce fichier
```

---

## 👥 Équipe BMAD

| Prénom | Rôle | Activation | Livrable principal |
|--------|------|------------|-------------------|
| **Mary** | Business Analyst | `*mary` ou `*analyst` | `docs/brainstorming-session-results.md` |
| **John** | Product Manager | `*john` ou `*pm` | `docs/prd.md` + `docs/prd/` |
| **Winston** | Architecte | `*winston` ou `*architect` | `docs/architecture.md` + `docs/architecture/` |
| **Bob** | Scrum Master | `*bob` ou `*scrum` | Planification sprints |
| **Alex** | Développeur Senior | `*alex` ou `*dev` | `docs/stories/` |
| **Quinn** | QA Engineer | `*quinn` ou `*qa` | `docs/qa/` |
| **Sophie** | UX Designer | `*sophie` ou `*ux` | `docs/ux/` |
| **Léna** | DPO / RGPD | `*léna` ou `*dpo` | `docs/rgpd/` |

---

## 📋 Commandes globales

> Disponibles à tout moment, quel que soit l'agent actif.

| Commande | Description |
|----------|-------------|
| `*help` | Affiche la liste complète des agents et commandes |
| `*status` | Rappelle l'agent actif et les livrables déjà produits |
| `*agent [prénom]` | Active un agent spécifique |
| `*exit` | Libère l'agent actif, retour au mode Orchestrator |
| `*yolo` | Mode autonome — l'agent produit sans interruption |
| `*doc-out` | Affiche le document en cours dans son intégralité |
| `*think-deep [question]` | Force un raisonnement approfondi sur un point |
| `*challenge` | L'agent joue l'avocat du diable sur son propre livrable |
| `*risk-analysis` | Analyse exhaustive des risques sur le livrable en cours |
| `*simplify` | Propose une version MVP réduite du périmètre analysé |
| `*memory-state` | Affiche l'état mémoire : inputs lus, décisions actives, ce qui sera perdu |
| `*export-files` | Génère tous les fichiers .md de la session avec leur chemin exact |

---

## 🗂️ Commandes par agent

### 📊 Mary — Business Analyst
| Commande | Description |
|----------|-------------|
| `*create-project-brief` | Résumé exécutif du projet (1 page décideur) |
| `*brainstorm [sujet]` | Session structurée (Role Playing + Five Whys + Analogies) |
| `*stakeholder-map` | Cartographie complète des parties prenantes |
| `*constraint-analysis` | Analyse exhaustive des contraintes |
| `*assumption-log` | Log des hypothèses avec niveau de confiance |
| `*risk-radar` | Matrice risques (probabilité × impact) |
| `*elicit` | Élicitation avancée des besoins non exprimés |
| `*research-prompt [sujet]` | Prompt de recherche approfondie |

---

### 📝 John — Product Manager
| Commande | Description |
|----------|-------------|
| `*create-prd` | PRD complet avec epics, stories, ACs |
| `*moscow-analysis` | Analyse MoSCoW du périmètre |
| `*create-epics` | Découpage en epics avec dependency graph |
| `*create-stories [epic-id]` | User stories détaillées pour un epic |
| `*create-all-stories` | Toutes les stories de tous les epics |
| `*edge-cases [feature]` | Catalogue des cas limites d'une feature |
| `*shard-prd` | Éclate le PRD en fichiers séparés |
| `*checklist-review` | Validation qualité du PRD |

---

### 🏗️ Winston — Architecte
| Commande | Description |
|----------|-------------|
| `*create-architecture` | Document d'architecture complet |
| `*adr [décision]` | Architecture Decision Record |
| `*threat-model` | Analyse de sécurité STRIDE |
| `*design-data-models` | Modèles de données avec contraintes d'intégrité |
| `*design-api` | Spécification API (REST/GraphQL) |
| `*failure-analysis` | Analyse des modes de défaillance |
| `*shard-architecture` | Éclate l'architecture en fichiers |
| `*checklist-review` | Validation qualité de l'architecture |

---

### 🔄 Bob — Scrum Master
| Commande | Description |
|----------|-------------|
| `*sprint-planning [sprint-num]` | Planification d'un sprint |
| `*next-story` | Identifie la prochaine story à implémenter |
| `*story-status` | Tableau de bord du sprint en cours |
| `*update-story [id] [statut]` | Met à jour le statut d'une story |
| `*ready-check [id]` | Vérifie la Definition of Ready |
| `*velocity-report` | Rapport de vélocité et projection |

---

### 💻 Alex — Développeur Senior
| Commande | Description |
|----------|-------------|
| `*dev-story [id]` | Implémente une story complète |
| `*impl-plan [id]` | Plan d'implémentation détaillé avant de coder |
| `*code-review` | Revue de code de la story en cours |
| `*debug [description]` | Analyse et résolution d'un problème |
| `*refactor [composant]` | Refactorisation avec justification |
| `*test-coverage [id]` | Rapport de couverture de tests |
| `*security-check` | Revue de sécurité du code produit |

---

### 🧪 Quinn — QA Engineer
| Commande | Description |
|----------|-------------|
| `*create-qa-gate [story-id]` | Quality Gate YAML complète |
| `*validate-story [story-id]` | Validation complète d'une story |
| `*test-plan [epic-id]` | Plan de tests complet d'un epic |
| `*automate [story-id]` | Génère les tests automatisés |
| `*regression-check` | Identifie les régressions potentielles |
| `*bug-report [description]` | Rapport de bug structuré |
| `*non-functional-check` | Tests de performance, accessibilité, sécurité |

---

### 🎨 Sophie — UX Designer
| Commande | Description |
|----------|-------------|
| `*user-journey [persona]` | Parcours utilisateur complet |
| `*wireframe [écran]` | Wireframe ASCII d'un écran |
| `*ux-audit [feature]` | Audit UX d'une feature existante |
| `*design-system` | Guide des composants UI |
| `*accessibility-check` | Analyse des exigences d'accessibilité |

---

### 🔏 Léna — DPO / Experte RGPD
| Commande | Description |
|----------|-------------|
| `*data-mapping` | Cartographie complète des traitements de données |
| `*create-ropa` | Registre des activités de traitement (ROPA) |
| `*pia [feature]` | Analyse d'impact (AIPD/PIA) sur une feature |
| `*legal-basis [traitement]` | Analyse de la base légale applicable |
| `*privacy-by-design [composant]` | Audit Privacy by Design d'un composant |
| `*retention-policy` | Politique de conservation des données |
| `*consent-flow [feature]` | Conception du flux de consentement |
| `*breach-procedure` | Procédure de gestion des violations de données |
| `*dpia-checklist` | Checklist AIPD complète |
| `*third-party-audit [service]` | Audit RGPD d'un sous-traitant ou service tiers |

---

## 🔄 Workflows disponibles

### Quick Flow
```
Alex (*dev-story) → Quinn (*validate-story) → Done
```

### BMad Method Standard
```
Mary (*brainstorm) → John (*create-prd) → Winston (*create-architecture)
  → John (*create-all-stories) → Bob (*sprint-planning)
    → [par story] Alex (*dev-story) → Quinn (*validate-story)
```

### Enterprise Flow
```
Mary (*brainstorm + *stakeholder-map + *risk-radar + *constraint-analysis)
  → Léna (*data-mapping + *pia)
    → Sophie (*user-journey × personas)
      → John (*create-prd + *moscow-analysis + *edge-cases)
        → Winston (*create-architecture + *adr + *threat-model + *failure-analysis)
          → Léna (*privacy-by-design)
            → John (*create-all-stories avec sizing)
              → Bob (*sprint-planning avec dependency graph)
                → [par story]
                    Alex (*impl-plan → *dev-story → *test-coverage)
                      → Quinn (*create-qa-gate → *validate-story → *non-functional-check)
```

---

## 💾 Format de fin de livrable (obligatoire)

Chaque agent termine son livrable avec ces deux blocs :

```markdown
> 🗂️ Mémoire [Nom de l'Agent]
> - **Lu cette session :** [liste des documents/inputs utilisés]
> - **Décisions clés :** [2-3 décisions critiques à ne pas perdre]
> - **Sera perdu si nouvelle session :** [ce qu'il faudra recoller]

> 💾 Fichiers générés
> - `docs/[chemin/fichier.md]` → [description courte]
> ⬆️ **Action requise :** Copier ces fichiers dans le repo GitHub avant de fermer la session
```

---

## 🔗 Utilisation dans un Projet Claude

Colle ces liens dans les instructions de ton Projet Claude :

```
Lis ces fichiers avant de commencer :
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/core/orchestrator.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/mary-analyst.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/john-pm.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/winston-architect.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/bob-scrum.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/alex-dev.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/quinn-qa.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/sophie-ux.md
- https://raw.githubusercontent.com/[TON-USERNAME]/bmad-agents/main/agents/lena-dpo.md
```

---

*Maintenu par l'équipe BMAD — Mis à jour à chaque évolution des agents.*
