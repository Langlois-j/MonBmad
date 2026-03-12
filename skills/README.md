# 🛠️ Skills Claude — BMAD

Ce dossier contient les skills installables dans **Claude Desktop**.
Un skill est un fichier `SKILL.md` que Claude charge automatiquement quand il détecte un contexte correspondant.

---

## 📦 Skills disponibles

| Skill | Dossier | Description |
|-------|---------|-------------|
| **bmad-autosave** | `bmad-autosave/` | Sauvegarde automatique du contexte — mode Normal et mode BMAD |

---

## 🚀 Installation d'un skill dans Claude Desktop

### Prérequis
- Claude Desktop installé
- Windows-MCP activé (voir `README.md` racine)

### Étapes

**1. Ouvre Claude Desktop**

**2. Va dans Paramètres → Skills**
```
Menu hamburger (☰) → Paramètres → Skills
```

**3. Clique sur "Ajouter un skill"**

**4. Pointe vers le fichier `SKILL.md` du skill voulu**
```
[BMAD_LOCAL_PATH]\skills\bmad-autosave\SKILL.md
```

**5. Claude lit le frontmatter YAML** (`name` + `description`) et l'ajoute à la liste.

**6. Vérifie que le skill est activé** (toggle ON)

---

## ▶️ Utilisation

Une fois installé, le skill se déclenche **automatiquement** selon sa description.
Tu n'as rien à faire — Claude détecte le contexte et charge le skill seul.

Pour `bmad-autosave` : il s'active dès qu'une conversation démarre,
qu'un agent BMAD est actif, ou que tu mentionnes "sauvegarde", "autosave", "contexte".

---

## ⏸️ Désactiver un skill temporairement

```
Claude Desktop → Paramètres → Skills → Toggle OFF
```

Utile pour une session rapide sans sauvegarde automatique.
Le skill reste installé — tu le réactives quand tu veux.

---

## 🗑️ Désinstaller un skill

```
Claude Desktop → Paramètres → Skills → [skill] → Supprimer
```

---

## ➕ Ajouter un nouveau skill dans ce repo

1. Crée un dossier `skills/[nom-skill]/`
2. Crée un fichier `SKILL.md` avec le frontmatter YAML obligatoire :

```yaml
---
name: nom-du-skill
description: Quand ce skill doit s'activer et ce qu'il fait.
             Plus la description est précise, mieux Claude déclenche le skill.
---

# Titre du skill

Instructions pour Claude...
```

3. Ajoute une ligne dans le tableau ci-dessus
4. Commit + push

---

## 📝 Contenu d'un dossier skill

```
skills/[nom-skill]/
├── SKILL.md          ← Obligatoire — instructions + frontmatter YAML
└── [scripts/]        ← Optionnel — scripts Python, références, assets
```

---

## ⚙️ Variables de configuration

Les skills lisent leurs variables depuis les **instructions du projet Claude**.
Aucun chemin local n'est hardcodé dans les fichiers `SKILL.md`.

Variables utilisées par `bmad-autosave` :

| Variable | Description |
|---|---|
| `BMAD_LOCAL_PATH` | Chemin local du repo BMAD |
| `CLAUDE_CONTEXT_PATH` | Dossier de sauvegarde des contextes |
| `LEVELDB_PATH` | Chemin LevelDB Claude Desktop (détecté auto si absent) |
| `AUTOSAVE_FREQUENCY` | Fréquence de sauvegarde (défaut : 4) |
| `AUTOSAVE_BLOCK_ON_CRITICAL` | Blocage sur livrable critique (défaut : oui) |
