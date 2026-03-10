# 🗂️ Architecture Mémoire BMAD

## Principe général

La mémoire BMAD est **hybride** :
- Un fichier **contexte global** partagé par tous les agents
- Un fichier **contexte par agent** propre à chacun

---

## Structure des fichiers de contexte

```
projects/[nom-projet]/context/
├── project-context.md      ← Global — lu et mis à jour par tous les agents
├── mary-context.md         ← Propre à Mary
├── john-context.md         ← Propre à John
├── winston-context.md      ← Propre à Winston
├── bob-context.md          ← Propre à Bob
├── alex-context.md         ← Propre à Alex
├── quinn-context.md        ← Propre à Quinn
├── sophie-context.md       ← Propre à Sophie
└── lena-context.md         ← Propre à Léna
```

---

## Format — project-context.md

```markdown
# Contexte Projet — [Nom du projet]

## Informations générales
- **Nom :** 
- **Date de début :** 
- **Phase actuelle :** [Brainstorming / PRD / Architecture / Dev / QA]
- **Dernier agent actif :** 
- **Dernière mise à jour :** 

## Décisions validées
- [DATE] [AGENT] : [Décision]
- [DATE] [AGENT] : [Décision]

## Contraintes connues
- Réglementaires :
- Techniques :
- Organisationnelles :

## Stack technique retenue
- 

## Epics identifiés
| ID | Titre | Statut |
|----|-------|--------|
|    |       |        |

## Points bloquants / en attente
- 

## Prochaine étape
- Agent : 
- Action : 
```

---

## Format — [agent]-context.md

```markdown
# Contexte [Prénom] — [Nom du projet]

## Dernière session
- **Date :**
- **Livrable produit :**
- **Statut :** Complet / En cours / Bloqué

## Décisions prises par cet agent
- [Décision + justification]

## Hypothèses posées
- [Hypothèse + niveau de confiance]

## Fichiers générés
- `docs/[chemin]` — [statut : généré / à valider / validé]

## Handoff vers agent suivant
- **Agent :** 
- **Message :**
- **Fichiers à transmettre :**

## À recoller en début de prochaine session
[Bloc de contexte minimal à copier-coller pour reprendre le travail]
```

---

## Procédure de reprise de session

Au début de chaque nouvelle session, colle :

1. `projects/[nom]/context/project-context.md`
2. `projects/[nom]/context/[agent]-context.md`

Et dis à Claude :
> "Reprends en tant que [Agent]. Voici le contexte projet et ton contexte personnel."
