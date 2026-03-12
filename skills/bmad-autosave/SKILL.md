---
name: bmad-autosave
description: Sauvegarde automatique silencieuse du contexte de conversation via Windows-MCP FileSystem. Utilise ce skill dès qu'une conversation démarre, qu'un projet BMAD est actif, ou que l'utilisateur mentionne "autosave", "sauvegarde automatique", "contexte", "session". S'applique aussi bien aux agents BMAD (Mary, John, Winston, etc.) qu'à toute conversation sans agent. Active la détection environnement (Desktop+MCP ou Web) et maintient un fichier de contexte condensé sur disque local.
---

# BMAD Autosave Skill

Sauvegarde automatique et silencieuse du contexte de conversation.
Deux modes distincts : **Normal** (conversation sans agent) et **BMAD** (agent actif).

---

## Variables de configuration (lues depuis les instructions du projet)

```
BMAD_LOCAL_PATH=[chemin local du repo BMAD]
CLAUDE_CONTEXT_PATH=[chemin du dossier de contexte Claude]
AUTOSAVE_FREQUENCY=4
AUTOSAVE_BLOCK_ON_CRITICAL=oui
LEVELDB_PATH=[chemin du LevelDB Claude Desktop]
```

> Aucun chemin local n'est hardcodé dans ce skill.
> Tout est lu depuis les instructions du projet ou demandé au démarrage.

Valeurs par défaut si absentes (demandées au démarrage) :
```
CLAUDE_CONTEXT_PATH → Documents\Claude\Contexte\
LEVELDB_PATH        → %LOCALAPPDATA%\Packages\Claude_[id]\LocalCache\Roaming\Claude\IndexedDB\https_claude.ai_0.indexeddb.leveldb\000019.log
AUTOSAVE_FREQUENCY  → 4
AUTOSAVE_BLOCK_ON_CRITICAL → oui
```

---

## MODE DÉTECTION au démarrage

Détecter si BMAD est actif :
- Présence de `BMAD_LOCAL_PATH` dans les instructions → **Mode BMAD**
- Sinon → **Mode Normal**

Afficher une seule fois :
```
🖥️ Autosave [MODE NORMAL | MODE BMAD] actif → [CHEMIN résolu]
OU
🌐 Autosave Web — tape *save pour sauvegarder
```

---

# MODE NORMAL — Conversation sans agent

---

## N1. Chemin de sauvegarde

```
[CLAUDE_CONTEXT_PATH]\[uuid]-[nom-discussion]\session-context.md
```

### Récupération UUID (source : LevelDB Claude Desktop)

Pattern dans `[LEVELDB_PATH]` :
```
store:chat-draft:[uuid]
ex: store:chat-draft:cc9cd953-63b4-4df5-9a83-b4311ef3c50c
```

### Procédure au démarrage
```
1. Lire [LEVELDB_PATH] via FileSystem → extraire tous les UUIDs
2. Snapshot → lire le nom de la discussion (titre fenêtre)
3. Sanitiser le nom (retirer : \ / : * ? " < > |)
4. Chercher dans [CLAUDE_CONTEXT_PATH] :
   a. Dossier UUID trouvé, nom identique   → continuer
   b. Dossier UUID trouvé, nom différent   → renommer le dossier
   c. Dossier UUID absent                  → créer [uuid]-[nom]\
5. Si plusieurs UUIDs → FUSION (voir N2)
6. Lire session-context.md → restaurer contexte en mémoire
```

## N2. UUID multiples — Fusion des contextes

Si plusieurs UUIDs détectés (plusieurs discussions ouvertes) :
```
1. Lire session-context.md de chaque dossier correspondant
2. Fusionner en dédupliquant :
   DECISIONS → union, doublons supprimés
   LIVRABLES → union, doublons supprimés
   PENDING   → union, doublons supprimés
   CONTEXTE  → concaténation séparée par " | "
3. Écrire dans le session-context.md de la discussion active
4. Afficher : 💾 ✅ Contexte fusionné depuis [N] sessions
```

## N3. Format fichier session-context.md

```
DISCUSSION_ID:[uuid LevelDB]
DISCUSSION_NAME:[nom discussion]
[timestamp]|DECISIONS:[d1,d2]|LIVRABLES:[l1,l2]|PENDING:[p1,p2]|CONTEXTE:[résumé]
```

---

# MODE BMAD — Agent actif

---

## B1. Chemins de sauvegarde BMAD

```
Contexte projet  : [BMAD_LOCAL_PATH]\projects\[nom-projet]\context\project-context.md
Contexte agent   : [BMAD_LOCAL_PATH]\projects\[nom-projet]\context\[agent]-context.md
Session globale  : [BMAD_LOCAL_PATH]\projects\[nom-projet]\context\session-context.md
```

## B2. Procédure au démarrage BMAD

```
1. Lire BMAD_LOCAL_PATH depuis les instructions du projet
2. Identifier l'agent actif
3. Lire session-context.md du projet → restaurer
4. Lire [agent]-context.md → restaurer contexte agent
5. Afficher :
   🖥️ Autosave BMAD actif
   Projet : [nom-projet]
   Agent  : [prénom]
   Contexte chargé : ✅ / ❌ non trouvé
```

## B3. Format fichier session-context.md BMAD

```
PROJECT:[nom-projet]
LAST_AGENT:[agent actif]
LAST_SAVE:[timestamp]
---
[timestamp]|AGENT:[prénom]|DECISIONS:[d1,d2]|LIVRABLES:[l1,l2]|PENDING:[p1,p2]|HANDOFF:[agent-suivant ou vide]
```

## B4. Format fichier [agent]-context.md

```
AGENT:[prénom]
PROJECT:[nom-projet]
LAST_SAVE:[timestamp]
DECISIONS:[décisions de cet agent]
LIVRABLES:[fichiers produits]
PENDING:[reste à faire]
HANDOFF_TO:[agent suivant]
HANDOFF_NOTES:[points clés à transmettre]
```

## B5. Fusion inter-agents BMAD

```
1. À chaque save :
   - [agent]-context.md    → contexte de l'agent actif uniquement
   - session-context.md    → ajouter/mettre à jour la ligne de l'agent actif
2. Ne JAMAIS écraser les lignes des autres agents dans session-context.md
3. Sur *handoff [agent-suivant] :
   - Compléter HANDOFF_TO et HANDOFF_NOTES
   - Ajouter ligne handoff dans session-context.md
   - Sauvegarder immédiatement
   - Afficher : 💾 ✅ Handoff [Agent sortant] → [Agent entrant] sauvegardé
```

## B6. Déclencheurs critiques BMAD

Sauvegarder immédiatement sur :
- Activation d'un agent
- Handoff entre agents
- Livrable produit
- Décision tranchée

---

# RÈGLES COMMUNES

---

## C1. Déclenchement périodique

Toutes les N réponses (défaut : 4).
- `💾 ✅` si succès
- `💾 ❌ [motif court]` si échec
- Silence si rien à sauvegarder

## C2. Commandes disponibles

| Commande | Description |
|---|---|
| `*save` | Sauvegarde immédiate |
| `*save-config [freq] [blocage]` | Modifie fréquence et blocage |
| `*history` | Décisions de la session |
| `*reload` | Relit et restaure le contexte |
| `*env` | Environnement, mode, chemins actifs |
| `*cleanup` | Supprime le dossier de la session en cours |

## C3. Limites connues

- **Fusion UUID multiples** — ordre chronologique non garanti entre sessions
- **Renommage** — détecté au prochain démarrage uniquement
- **Suppression** — non temps réel → utiliser `bmad-cleanup.py`

## C4. Script de nettoyage

`bmad-cleanup.py` — lit `[LEVELDB_PATH]`, compare les UUIDs avec `[CLAUDE_CONTEXT_PATH]`.
```
python bmad-cleanup.py           # simulation
python bmad-cleanup.py --execute # suppression réelle
```
