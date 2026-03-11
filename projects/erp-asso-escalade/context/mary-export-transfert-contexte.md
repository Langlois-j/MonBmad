# EXPORT MARY — Business Analyst
> Transfert de contexte inter-session — GestionAsso
> Généré le 10/03/2026 (session 2) — À coller dans le nouveau contexte Mary

---

## 📋 MISSION EN COURS

**Agent :** Mary — Business Analyst
**Phase :** Résolution des bloquants réglementaires V1 (P1 → P15)
**Objectif immédiat :** Finaliser P9 (1 point en suspens) → P10 → P15, trancher Q-07 → Q-14, puis passer le relais à John (`*create-prd`)

---

## 🔑 DÉCISION TRANSVERSALE — API FFME

> **Règle validée (session 2) :** Toute donnée disponible via `https://api.core.myffme.fr/` fait **référence absolue**.
> La saisie manuelle n'est qu'un **fallback** si la donnée est absente de l'API ou si l'API est inaccessible.

- Technologie : API Platform (Symfony) — REST + GraphQL
- Authentification requise pour accès aux données
- ⚠️ **Flag Winston :** Obtenir credentials + liste exacte des endpoints disponibles pour un club affilié
- Données supposées disponibles (hypothèse de travail) : licences, diplômes, passeports

---

## ✅ DÉCISIONS VALIDÉES (P1 → P7)

### P1 + P2 — Gestion d'accident
**Hors scope V1.** Module dédié en V2.
- SORT-M17 : Déclaration accident préfecture 48h → V2
- SORT-M12 : Assistant déclaration FFME 5 jours → V2
- SORT-M06 : Rapport d'incident horodaté → V2
- SORT-M18 : Déclaration REX FFME → V2
- EPI-M06 : Procédure EPI post-accident → V2

---

### P3 — MEMB-M11 : RC obligatoire
La RC est incluse dans la cotisation FFME gérée par myFFME — pas de gestion dans GestionAsso.
- Seule vérification : **licence FFME valide pour la saison en cours**
- Champ "N° licence FFME + saison" **obligatoire et bloquant** dans la fiche membre
- Garanties optionnelles (BASE / BASE+ / BASE++) : tracées en information uniquement

---

### P4 — DIPL-M01 : Diplôme expiré
- Notification en **début de saison** au Président listant tous les recyclages nécessaires sur l'exercice
- Filtre "Recyclages à prévoir" sur le tableau de bord
- **Aucun blocage automatique mid-saison**
- Habilitation présidentielle possible : le Président peut désigner un encadrant sans diplôme formel → tracé (date + désignation formelle dans la fiche membre)
- Seul un organisme habilité peut revalider (CT FFME, Croix-Rouge, pompiers, SAMU) — le club ne valide rien

---

### P5 — DIPL-M10 : Vérification brevet × périmètre
- Alerte si diplôme incompatible avec le type de support (SAE / SNE / longueurs / ACM)
- Dérogation Président tracée possible (même mécanisme que P4)
- Deux cas d'affectation hors diplôme :
  - Diplômé hors périmètre → alerte + dérogation présidentielle
  - Sans diplôme → habilitation présidentielle préalable obligatoire

---

### P6 — SORT-M01 : AST + Compte Responsable légal
**Décision architecturale N:N Mineur ↔ Responsable :**
- N responsables sans limite (cas : maison d'enfance, éducateurs spécialisés, ASE, foyer)
- Types : Parent / Tuteur légal / Éducateur spécialisé / Référent institutionnel / Autre (champ libre)
- Personne morale possible (institution + contact référent nommé)
- Case "Destinataire documents officiels" par responsable — envoi AST uniquement aux cochés
- Compte GestionAsso **optionnel** par responsable (email = login, type "Responsable légal", droits limités)
- **Flux numérique** si compte : AST pré-remplie envoyée, première signature reçue valide
- **Flux papier universel** : PDF imprimable, scan uploadable, toujours disponible
- **Mode hors ligne** : fiche terrain inclut statut AST + version vierge imprimable
- Blocage au statut "Départ confirmé" si AST manquante (pas à l'inscription)
- Rappels automatiques J-7 / J-3 / J-1 configurables
- Compte Responsable légal = **nouveau type utilisateur** (voir uniquement sorties de son enfant, déposer documents, signer formulaires)

---

### P7 — CREN-M11 : Responsable de séance obligatoire
- Créneau **non publiable** sans responsable assigné
- Créneau **récurrent** : responsable par défaut défini à la création, appliqué à toutes les occurrences automatiquement
- Le responsable peut signaler son absence en **1 clic** (tableau de bord ou email) → créneau passe en "Responsable manquant" + alerte Président pour réassignation
- Si aucun remplaçant trouvé → créneau **masqué** aux membres
- Distinction : Responsable de séance ≠ Encadrant diplômé (deux rôles indépendants)

---

### ✅ P8 — CREN-M12 : Niveaux d'autonomie sur feuille de présence (validé session 2)

| Icône | Niveau | Passeport |
|-------|--------|-----------|
| 🔴 | Encadrement obligatoire | < Jaune |
| 🟡 | Bloc SAE + moulinette | Jaune |
| 🟠 | SAE complète | Orange |
| 🟢 | SNE encadrée | Vert |
| 🔵 | SNE 1 longueur | Bleu |
| 🟣 | SNE plusieurs longueurs | Violet+ |

- Source de vérité : **API FFME en priorité** — saisie manuelle = fallback
- Saisie : membre/responsable pour soi uniquement · encadrant+ pour tous
- Donnée absente → 🔴 par défaut (principe de précaution)
- Visibilité : **encadrants et rôles supérieurs uniquement**
- Pas de synchronisation automatique (pas d'API FFME temps réel confirmée)
- ⚠️ **Flag Léna :** Base légale de l'affichage d'une donnée issue du référentiel FFME sans lien technique officiel

---

## ⏳ EN ATTENTE DE VALIDATION UTILISATEUR (P9 → P15)

### 🔶 P9 — EPI-M08 : Qualification contrôleur EPI (partiellement validé)

**Validé :**
- Champ "Gestionnaire EPI" obligatoire dans paramètres club, lié à un membre
- Vérification diplôme via **API FFME en priorité**, saisie manuelle = fallback
- Diplômes reconnus : Initiateur SAE minimum ou formation "gestion et contrôle EPI" FFME
- Alerte permanente tableau de bord Président si qualification manquante

**⏳ EN ATTENTE — 1 point :**
- Nombre de gestionnaires EPI : **1 seul** ou **titulaire + suppléant** ?

---

### P10 — EPI-M09 : Contrôle de routine avant/après séance
Checklist simplifiée début séance, validation 1 clic + horodatage. Case "Signalement EPI" fin de créneau → alerte gestionnaire EPI si cochée. Séparé du contrôle annuel dans le registre.

**Statut :** ⏳ Non soumis

---

### P11 — MEMB-M16 : Passeport → autorisations de pratique
Champ "Dernier passeport validé" (couleur + date + validateur). Autorisations auto-générées selon matrice. Restrictions manuelles possibles (visibles encadrants/Président uniquement, pas du membre).

**Statut :** ⏳ Non soumis

---

### P12 — SORT-M19 : Alerte séjour spécifique → DDCS
Compteur mineurs temps réel sur sorties avec hébergement. Bannière orange à 7 mineurs, rouge à clôture inscriptions. Case "Déclaration effectuée" tracée. Seuil 7 non paramétrable (loi).

**Statut :** ⏳ Non soumis

---

### P13 — PARAM-M09 : Alerte renouvellement affiliation FFME
Calcul automatique montant probable (80/150/250€ selon licenciés au 31/08). Alertes J-60/J-30. Attestation uploadable avec date expiration sur tableau de bord.

**Statut :** ⏳ Non soumis

---

### P14 — BUR-M08 : Contrat engagement républicain
Documents fondateurs, signature unique. Alerte si >5 ans et demande subvention. Inclus dans checklist installation.

**Statut :** ⏳ Non soumis

---

### P15 — SORT-M20 : Brevet + formation continue pour ACM
Si séjour spécifique → vérification formation continue encadrant. Blocage si expirée. Dérogation Président tracée possible.

**Statut :** ⏳ Non soumis

---

## ❓ QUESTIONS RÉGLEMENTAIRES OUVERTES (Q-04, Q-07 → Q-14)

> ⚠️ Ces questions n'ont **jamais été soumises** au porteur de projet. À traiter après P9→P15.

| ID | Question | Module concerné |
|----|----------|----------------|
| Q-04 | Seuil autonomie SAE mineurs : 14 ans FFME ou paramétrable par le club ? | CREN + SORT |
| Q-07 | CS Escalade Santé : données prescription médicale stockées dans GestionAsso (RGPD art. 9) ou attestées uniquement ? | MEMB |
| Q-08 | Diplômes abrogés : comment les identifier dans le formulaire sans confondre avec invalides ? | DIPL |
| Q-09 | Attestation assurance club FFME : téléchargeable myFFME ou saisie manuelle ? | PARAM |
| Q-10 | Durée conservation AST : 3 mois ou prescription quinquennale RC ? | SORT |
| Q-11 | CERFA AST : modèle 15646*01 officiel ou modèle libre suffisant ? | SORT |
| Q-12 | Fiche sanitaire liaison mineurs : durée conservation réglementaire (arrêté 2006) ? | SORT |
| Q-13 | Contrat engagement républicain : renouvellement annuel ou une fois ? | BUR |
| Q-14 | Carte professionnelle encadrant salarié : vérifiable en ligne DDCS ? | DIPL |

---

## 🔴 POINTS À RETRAVAILLER — DÉCISIONS INCOMPLÈTES

### 🟠 À PRÉCISER

| ID | Élément | Ce qui manque |
|----|---------|--------------|
| P6 | Flux AST : délai de validité d'une AST signée (durée entre signature et départ) | À demander |
| P4 | Habilitation présidentielle : durée maximale ? Renouvelable automatiquement ou re-validation explicite ? | À préciser |
| P5 | Périmètre "ACM" dans la matrice diplômes : diplôme minimum pour ACM avec hébergement ? | À confirmer |
| CREN | Seuil âge autonomie : valeurs min/max admises ? Le club peut-il descendre sous 14 ans ? | À cadrer |

### 🟡 HYPOTHÈSES NON VÉRIFIÉES

| Hypothèse | Fondée sur | À valider |
|-----------|-----------|-----------|
| Passeport = acquis permanent, jamais expiré | Interprétation règles FFME | Confirmer avec source officielle |
| Diplômes abrogés = prérogatives conservées | Droit acquis habituel | Vérifier texte FFME ou circulaire |
| Seuil ACM = 7 mineurs non paramétrable | Texte de loi (ACM) | Citer la référence exacte |
| Modèle libre suffisant pour AST | Pratique courante | Vérifier si CERFA 15646*01 obligatoire |
| API FFME expose licences/diplômes/passeports | API Platform détectée | À confirmer avec credentials |

---

## 📊 COMPTEURS SPEC (état au transfert session 2)

| Indicateur | Valeur |
|-----------|--------|
| Modules couverts | 10 |
| Total éléments spec | 122 |
| 🔴 Bloquants V1 actifs | 44 |
| 🟠 Importants | 46 |
| 🟡 Souhaitables | 10 |
| ⚠️ Réglementaires | 53 |
| Hors scope V1 | 6 (module Gestion Accident V2) |
| Bloquants résolus | 8 (P1→P8) |
| Bloquants restants à valider | 7 (P9→P15, dont P9 partiellement) |

---

## 🚀 ORDRE DE REPRISE RECOMMANDÉ

```
1. Finaliser P9 : répondre "1 gestionnaire EPI ou titulaire + suppléant ?"
2. Soumettre P10 → P15 une par une
3. Trancher Q-04 (impact immédiat créneaux + sorties)
4. Traiter Q-07 → Q-14 (réglementaire)
5. Préciser les 4 points "à préciser"
6. Vérifier les 5 hypothèses non confirmées (dont API FFME)
   ↓
Passage à John → *create-prd
```

---

*Export produit par Mary — Business Analyst*
*Destination : nouveau contexte Claude projet GestionAsso*
*Session 2 — 10/03/2026*
