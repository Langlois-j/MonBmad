# 📁 Projets BMAD

Ce dossier contient un sous-dossier par projet.
Chaque projet stocke sa propre mémoire, indépendante des autres.

## Structure d'un projet

```
projects/
├── _template/               ← Copier ce dossier pour créer un nouveau projet
│   ├── context/             ← Mémoire de chaque agent
│   └── docs/                ← Livrables du projet
└── [nom-de-ton-projet]/
```

## Créer un nouveau projet

1. Copie le dossier `_template`
2. Renomme-le avec le nom de ton projet
3. Remplis `context/project-context.md` avec les infos de base
4. C'est prêt !

## Reprendre une session

Colle dans Claude :
1. Le contenu de `context/project-context.md`
2. Le contenu de `context/[agent]-context.md` de l'agent à activer
