# Contexte Projet — ERP ASSO ESCALADE (GestionAsso)

## Informations générales
- **Nom :** GestionAsso
- **Type :** Utilitaire open source de gestion d'association sportive — self-hosted
- **Club pilote :** Desvr'Escalade — Complexe du Pilbois, 62240 Desvres
- **Fédération :** FFME
- **Porteur de projet :** Développeur + gestionnaire EPI diplômé + ancien trésorier du club
- **Licence :** Open source (MIT, GPL ou AGPL — à décider en TECH-02)
- **Date de début :** Mars 2026
- **Phase actuelle :** PRD — Mary complète, en attente John
- **Dernier agent actif :** Mary
- **Dernière mise à jour :** 10/03/2026
- **Workflow :** Enterprise Flow

## Objectif immédiat
Démonstration aux présidents de club via wireframes interactifs.

## Stack / Versions
- **V1 :** 1 instance = 1 club
- **V2 (future) :** Multi-clubs + app mobile Flutter

## Charte graphique — Desvr'Escalade
```css
--blue:   #1d4e89   /* bleu faïence profond */
--accent: #2d9e6b   /* vert falaise Boulonnais */
--warm:   #c2622a   /* terre cuite / corde */
--chalk:  #f5f7fb   /* blanc calcaire */
Police : Plus Jakarta Sans (Google Fonts)
```

## Livrable existant
Maquette HTML interactive v3 : `maquette-gestionasso.html`
- 5 profils : Président (Martin P.), Trésorier (Claire T.), Gestionnaire EPI (Thomas D.), Encadrant (Alex D.), Membre (Sophie F.)
- Filtres EPI et Membres fonctionnels
- Navigation complète, toasts, modals, actions interactives

## Décisions validées (P1 → P7)

| ID | Date | Agent | Décision |
|----|------|-------|----------|
| P1 | 09/03/2026 | Mary | RC incluse dans cotisation FFME — GestionAsso vérifie uniquement licence valide |
| P2 | 09/03/2026 | Mary | Recyclage diplômes : notification début saison uniquement, pas de blocage mid-saison |
| P3 | 09/03/2026 | Mary | Validation diplômes par organisme habilité uniquement — upload justificatif externe |
| P4 | 09/03/2026 | Mary | Habilitation présidentielle : désignation encadrant sans diplôme, tracée formellement |
| P5 | 09/03/2026 | Mary | Passeport FFME = acquis permanent, génère autorisations auto surchargeables |
| P6 | 09/03/2026 | Mary | Créneau récurrent : responsable par défaut, 1 clic absence, masquage si sans responsable |
| P7 | 09/03/2026 | Mary | AST mineurs : flux numérique + flux papier toujours disponibles, blocage départ si manquante |

## Contraintes connues
- **Réglementaires :** 53 éléments marqués ⚠️ RÉGLEMENTAIRE (NF S72-701, Règlement UE 2016/425, arrêté 2006 ACM, loi 1901...)
- **Techniques :** Mode hors ligne requis (sorties terrain)
- **Organisationnelles :** Self-hosted, open source
- **Hors scope V1 :** Gestion d'accident (6 éléments — prévu V2)

## État de la spécification (post-audit FFME)

| Indicateur | Valeur |
|-----------|--------|
| Modules couverts | 10 |
| Total éléments spec | 122 |
| 🔴 Bloquants V1 | 44 |
| 🟠 Importants | 46 |
| 🟡 Souhaitables | 10 |
| ⚠️ Réglementaires | 53 |

## Modules couverts
EPI — Comptabilité — Sorties — Membres — Créneaux — Encadrement — Passeports — Bureau — Paramètres — Assurance/Licence

## Points bloquants / en attente
- P8 à P15 : validations utilisateur en attente
- Q-07 à Q-14 : questions réglementaires à trancher

## Epics identifiés
| ID | Titre | Statut |
|----|-------|--------|
| — | À définir par John | En attente |

## Prochaine étape
- **Agent :** John (*pm)
- **Action :** `*create-prd` — PRD complet avec epics, MoSCoW, stories
- **Inputs nécessaires :** Finaliser P8→P15 + trancher Q-07→Q-14 avant PRD
- **Puis :** Winston (`*create-architecture`) — Focus triangle Diplômes × Membres × Créneaux
