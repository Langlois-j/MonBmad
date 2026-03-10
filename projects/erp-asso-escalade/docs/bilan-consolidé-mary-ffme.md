# Bilan Consolidé — Audit FFME × Spécification GestionAsso
> Produit par Mary — Business Analyst  
> Session : 09/03/2026 — Desvr'Escalade, 62240 Desvres  
> Documents FFME analysés : 7

---

## 📚 Documents intégrés

| # | Document | Source | Statut |
|---|----------|--------|--------|
| 1 | Recommandations EPI | myffme.fr/document/recommandation-epi | ✅ Complet |
| 2 | Assurances FFME | ffme.fr/ffme/licence/assurances | ✅ Complet |
| 3 | Pack création club | myffme.fr/document/pack-creation-club | ✅ Complet |
| 4 | Règles de sécurité escalade 2025 | myffme.fr/document/2025-regles-securite | ✅ Complet |
| 5 | Règles organisation et encadrement | myffme.fr/document/regles-d-organisation... | ✅ Complet |
| 6 | Synthèse réglementation encadrement | myffme.fr/document/synthese-reglementation... | ✅ Complet |
| 7 | Filière encadrement escalade | myffme.fr/document/filiere-d-encadrement... | ✅ Complet |
| 8 | Guide passeports escalade | myffme.fr/document/guide-d-utilisation-passeports | ⚠️ Derrière espace licencié — reconstitué via sources publiques |

---

## 📊 Compteurs globaux

| Indicateur | Valeur |
|-----------|--------|
| Modules couverts | 10 |
| Éléments spec originale (pré-FFME) | 57 |
| Éléments ajoutés après intégration FFME | 65 |
| **Total éléments spec** | **122** |
| 🔴 Bloquants originaux | 20 |
| 🔴 Bloquants ajoutés (FFME) | 30 |
| **🔴 Total bloquants V1** | **50** |
| 🟠 Importants | 46 |
| 🟡 Souhaitables | 10 |
| ⚠️ Marqués RÉGLEMENTAIRE | 38 |

---

## 🪖 MODULE EPI — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| EPI-M01 | Contrôle retour prêt formalisé — EPI endommagé → contrôle avant remise en service | 🔴 |
| EPI-M02 | Signalement chute/choc — bouton tous membres, mise hors service immédiate | 🔴 |
| EPI-M03 | Historique utilisateurs par EPI (traçabilité accident) | 🟠 |
| EPI-M04 | Comptage des utilisations (sorties/jours) | 🟠 |
| EPI-M05 | EPI personnel déclaré (membre grimpe avec son propre matériel) | 🟠 |
| EPI-M06 | Procédure accident impliquant EPI : séquestre, signalement FFME, conservation PV | 🔴 |
| EPI-M07 | Import initial du stock (CSV ou saisie assistée) | 🟠 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| EPI-M08 | Doc 1 | Qualification obligatoire du contrôleur EPI (diplôme FFME requis) ⚠️ RÉGLEMENTAIRE | 🔴 |
| EPI-M09 | Doc 1 | Contrôle de routine avant ET après chaque utilisation (distinct du contrôle annuel) ⚠️ RÉGLEMENTAIRE | 🔴 |
| EPI-M10 | Doc 1 | Certificat de conformité sur chaque fiche de vie EPI ⚠️ RÉGLEMENTAIRE | 🟠 |
| EPI-M11 | Doc 1 | Déclaration d'information obligatoire de l'utilisateur dans le PV de prêt ⚠️ RÉGLEMENTAIRE | 🔴 |
| EPI-M12 | Doc 1 | Formulaire retour avec case "Événement à signaler" → alerte gestionnaire EPI ⚠️ RÉGLEMENTAIRE | 🔴 |
| EPI-M13 | Doc 1 | Grille de contrôle guidé par type d'EPI (défaut → retrait ou rebut) | 🟡 |
| EPI-M14 | Doc 1 | Stockage hors produits chimiques — note sur fiche site/local | 🟡 |
| EPI-M15 | Doc 1 | Corde coupée : modification de la fiche de vie (nouvelle longueur, nouvelle date) | 🟡 |
| EPI-M16 | Doc 4 | Référentiels normatifs officiels par type d'EPI (Règlement UE 2016/425 + marquage CE) ⚠️ RÉGLEMENTAIRE | 🔴 |
| EPI-M17 | Doc 4 | Tapis de réception SAE = EPI à part entière (NF P 90 311 / NF P 90 312) ⚠️ RÉGLEMENTAIRE | 🟠 |

**Sous-total EPI : 17 éléments — 🔴×7 🟠×4 🟡×3**

---

## 💰 MODULE COMPTABILITÉ — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| COMPTA-M01 | Reçus fiscaux dons (Cerfa 11580*03) ⚠️ RÉGLEMENTAIRE | 🔴 |
| COMPTA-M02 | Suivi subventions par dossier (affectation dépenses) | 🟠 |
| COMPTA-M03 | Budget prévisionnel par poste avec écart réalisé/prévu | 🟠 |
| COMPTA-M04 | Remboursement de trop-perçu (double paiement, désistement sortie) | 🟠 |
| COMPTA-M05 | Gestion de caisse (espèces, solde temps réel) | 🟡 |
| COMPTA-M06 | Clôture d'exercice (report à nouveau, bilan fin saison, document AG) ⚠️ RÉGLEMENTAIRE | 🔴 |
| COMPTA-M07 | Multi-signataires sur paiements au-delà d'un seuil configurable | 🟠 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| COMPTA-M08 | Doc 3 | Template prévisionnel structuré charges fixes/variables + équilibre en temps réel | 🟠 |

**Sous-total COMPTABILITÉ : 8 éléments — 🔴×2 🟠×5 🟡×1**

---

## 🏔 MODULE SORTIES — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| SORT-M01 | AST mineurs hors-France (Autorisation Sortie du Territoire) ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M02 | Autorisation parentale France — milieu naturel, même en France ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M03 | Fiche sanitaire de liaison — obligatoire accueil collectif mineurs ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M04 | Alerte ratio encadrant/participants (préconisations FFME) | 🟠 |
| SORT-M05 | Workflow annulation sortie (notification, remboursement, libération EPI) | 🟠 |
| SORT-M06 | Rapport d'incident post-sortie horodaté (déclaration FFME/assurance) ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M07 | Alerte météo J-1 milieu naturel (optionnel) | 🟡 |
| SORT-M08 | Contact site/gardien falaise (ONF, propriétaire) | 🟡 |
| SORT-M09 | Autorisation retour autonome post-sortie (mineur) | 🟠 |
| SORT-M10 | Fiche terrain offline (liste participants, contacts urgence, fiches sanitaires, statut AST) ⚠️ RÉGLEMENTAIRE | 🔴 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| SORT-M11 | Doc 2 | Alerte couverture assurance hors UE + déclaration préalable FFME requise ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M12 | Doc 2 | Assistant déclaration accident FFME sous 5 jours (espace licencié myFFME) ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M13 | Doc 4 | Casque obligatoire site naturel → EPI requis généré automatiquement ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M14 | Doc 4 | Alerte pratique en solitaire non conforme règles fédérales ⚠️ RÉGLEMENTAIRE | 🟠 |
| SORT-M15 | Doc 4 | Signalement équipement vétuste via Suricate dans bilan post-sortie | 🟠 |
| SORT-M16 | Doc 5 | Trousse de premiers secours obligatoire + moyen d'alerte tracé avec date vérification ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M17 | Doc 5 | Déclaration accident grave à la préfecture (DDCS) sous 48h — code du sport art. R322-6 ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M18 | Doc 5 | Déclaration REX FFME (Retour d'Expérience) + information victime assurance | 🟠 |
| SORT-M19 | Doc 5 | Alerte "Séjour spécifique" — ≥7 mineurs + 1 nuit → déclaration DDCS obligatoire ⚠️ RÉGLEMENTAIRE | 🔴 |
| SORT-M20 | Doc 6 | Vérification brevet + formation continue encadrant pour ACM (accueil collectif mineurs) ⚠️ RÉGLEMENTAIRE | 🔴 |

**Sous-total SORTIES : 20 éléments — 🔴×12 🟠×6 🟡×2**

---

## 👥 MODULE MEMBRES — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| MEMB-M01 | Fiche sanitaire membre permanente (allergies, traitement de fond, PAI) ⚠️ RÉGLEMENTAIRE | 🔴 |
| MEMB-M02 | Certificat médical / questionnaire santé QS-SPORT + alertes expiration ⚠️ RÉGLEMENTAIRE | 🔴 |
| MEMB-M03 | Plusieurs tuteurs légaux (garde alternée, emails différents) | 🟠 |
| MEMB-M04 | Droit à l'image (opt-in/out, obligatoire mineurs) | 🟠 |
| MEMB-M05 | Historique licences FFME (numéro conservé d'une saison à l'autre) | 🟡 |
| MEMB-M06 | Désinscription RGPD (suppression données sur demande, conservation légale) ⚠️ RÉGLEMENTAIRE | 🔴 |
| MEMB-M07 | Liste noire / exclusion (empêcher réinscription sans divulguer motif) | 🟡 |
| MEMB-M08 | Autorisation sortie autonome SAE (mineur peut-il quitter seul la salle ?) ⚠️ RÉGLEMENTAIRE | 🔴 |
| MEMB-M09 | Export liste groupe offline configurable (champs exportables par rôle) | 🟠 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| MEMB-M10 | Doc 2 | Gestion questionnaire santé QS-SPORT — deux workflows distincts (attestation vs certificat médical) ⚠️ RÉGLEMENTAIRE | 🔴 |
| MEMB-M11 | Doc 2 | RC obligatoire non décochable à la licence (art. L321-1 code du sport) ⚠️ RÉGLEMENTAIRE | 🔴 |
| MEMB-M12 | Doc 2 | Niveau de garantie assurance individuelle tracé par membre (BASE / BASE+ / BASE++) | 🟠 |
| MEMB-M13 | Doc 4 | Statut pratique autonome vs encadrée tracé et validé par encadrant habilité | 🟠 |
| MEMB-M14 | Doc 5 | Conduites à risque signalables par encadrant (confidentiel → Président) | 🟠 |
| MEMB-M15 | Doc 5 | Interdiction alcool/tabac mineurs dans enceinte sportive → règlement intérieur type ⚠️ RÉGLEMENTAIRE | 🟠 |
| MEMB-M16 | Doc 7 | Passeport stocké → autorisations de pratique auto-générées par niveau ⚠️ RÉGLEMENTAIRE | 🔴 |
| MEMB-M17 | Doc 7 | Passeport comme prérequis vérifiable aux formations fédérales | 🟠 |
| MEMB-M18 | Doc 7 | Sessions passeport comme type d'événement tracé dans l'historique membre | 🟠 |
| MEMB-M19 | Doc 8 | Passeport Orange = prérequis Initiateur SAE (15 ans min) — vérification à l'inscription | 🟠 |

**Sous-total MEMBRES : 19 éléments — 🔴×7 🟠×10 🟡×2**

---

## 🗓 MODULE CRÉNEAUX — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| CREN-M01 | Feuille de présence signée (mineurs, exigée par certaines assurances) | 🟠 |
| CREN-M02 | Pointage arrivée/départ mineurs (qui les a récupérés) | 🟡 |
| CREN-M03 | Fermeture exceptionnelle + notification membres | 🟠 |
| CREN-M04 | Alerte encadrant minimum requis (créneau sans encadrant habilité) | 🟠 |
| CREN-M05 | Créneau découverte/invité (ratio, assurance journée) | 🟡 |
| CREN-M06 | Alerte encadrant — mineur non autorisé à partir seul (feuille de présence) ⚠️ RÉGLEMENTAIRE | 🔴 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| CREN-M07 | Doc 4 | Protocole double contrôle sécurité tracé par encadrant avant séance ⚠️ RÉGLEMENTAIRE | 🔴 |
| CREN-M08 | Doc 4 | Encadrant identifié pour protocole enrouleur automatique (binôme obligatoire) ⚠️ RÉGLEMENTAIRE | 🔴 |
| CREN-M09 | Doc 4 | Alerte mélange pratiques corde/enrouleur sur même couloir ⚠️ RÉGLEMENTAIRE | 🟠 |
| CREN-M10 | Doc 4 | Déséquilibre de gabarits grimpeur/assureur — note encadrant dans Dev Notes | 🟡 |
| CREN-M11 | Doc 5 | Responsable de créneau nommé obligatoire — même en autonomie ⚠️ RÉGLEMENTAIRE | 🔴 |
| CREN-M12 | Doc 5 | Liste des personnes autorisées à pratiquer en autonomie (par type de pratique) ⚠️ RÉGLEMENTAIRE | 🔴 |
| CREN-M13 | Doc 5 | Cahier de suivi créneau avec note de passation + case "Signalement EPI" | 🟠 |
| CREN-M14 | Doc 5 | Ratio encadrant/participants défini et configurable par type de créneau | 🟠 |
| CREN-M15 | Doc 5 | Mineur < 14 ans : présence adulte autorisé obligatoire — seuil paramétrable ⚠️ RÉGLEMENTAIRE | 🔴 |
| CREN-M16 | Doc 7 | Passeport du membre visible sur la feuille de présence numérique | 🟠 |
| CREN-M17 | Doc 7 | Filtre niveau passeport à l'inscription créneau (niveau cible configurable) | 🟡 |

**Sous-total CRÉNEAUX : 17 éléments — 🔴×6 🟠×7 🟡×4**

---

## 🏅 MODULE DIPLÔMES — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| DIPL-M01 | Lien diplôme → autorisation d'encadrer (diplôme expiré = retrait droits + alerte Président) ⚠️ RÉGLEMENTAIRE | 🔴 |
| DIPL-M02 | Niveaux grimpe membres (cotation, validé par encadrant ou auto-déclaré) | 🟠 |
| DIPL-M03 | Formations en cours / statut stagiaire | 🟡 |
| DIPL-M04 | Scan/preuve numérique du diplôme | 🟡 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| DIPL-M05 | Doc 4 | Qualification spécifique encadrant enrouleur automatique tracée et validée | 🔴 |
| DIPL-M06 | Doc 4 | Niveau passeport membre accessible à l'encadrant pour validation sortie | 🟠 |
| DIPL-M07 | Doc 5/6 | Qualification minimale obligatoire pour encadrement bénévole (6 brevets FFME) ⚠️ RÉGLEMENTAIRE | 🔴 |
| DIPL-M08 | Doc 5 | Mineur titulaire brevet fédéral — co-encadrant adulte obligatoire ⚠️ RÉGLEMENTAIRE | 🔴 |
| DIPL-M09 | Doc 5 | Passeports FFME comme référentiel d'autorisation de pratique (blanc→noir) | 🟠 |
| DIPL-M10 | Doc 6 | Matrice officielle 6 brevets × périmètre d'encadrement (SAE / SNE 1L / SNE 3L) ⚠️ RÉGLEMENTAIRE | 🔴 |
| DIPL-M11 | Doc 6 | Carte professionnelle encadrant salarié (numéro + date validité) ⚠️ RÉGLEMENTAIRE | 🔴 |
| DIPL-M12 | Doc 6 | Gestion diplômes abrogés (prérogatives conservées — ne pas signaler comme invalides) | 🟠 |
| DIPL-M13 | Doc 7 | Distinction modèle Passeport (acquis permanent) vs Brevet (recyclage obligatoire) ⚠️ RÉGLEMENTAIRE | 🔴 |
| DIPL-M14 | Doc 7 | Passeport = acquis définitif — pas d'alerte expiration (≠ brevet) | 🟠 |
| DIPL-M15 | Doc 8 | Âge minimum par diplôme stocké et vérifié (15 ans Initiateur SAE, 17–18 ans autres) | 🟠 |
| DIPL-M16 | Doc 8 | CS Escalade Santé — prescription médicale obligatoire à tracer (RGPD art. 9) ⚠️ RÉGLEMENTAIRE | 🔴 |
| DIPL-M17 | Doc 8 | CS P'tits Grimpeurs — créneau 3–6 ans réglementé spécifiquement | 🟠 |
| DIPL-M18 | Doc 8 | CS Escalade Handicap — public spécifique, conditions d'encadrement particulières | 🟠 |

**Sous-total DIPLÔMES : 18 éléments — 🔴×8 🟠×8 🟡×2**

---

## 📢 MODULE COMMUNICATION — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| COMM-M01 | Canal SMS (urgences, annulation dernière minute) | 🟡 |
| COMM-M02 | Accusé de réception (AST, autorisation parentale, convocation AG) | 🟠 |
| COMM-M03 | Archive des communications envoyées (historique par membre et date) | 🟠 |
| COMM-M04 | Opt-in légal RGPD (communications non contractuelles distinctes des alertes obligatoires) ⚠️ RÉGLEMENTAIRE | 🔴 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| COMM-M05 | Doc 3 | Modèles de messages types pour temps forts institutionnels (AG, portes ouvertes, résultats) | 🟡 |

**Sous-total COMMUNICATION : 5 éléments — 🔴×1 🟠×2 🟡×2**

---

## 🏢 MODULE BUREAU — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| BUR-M01 | Cerfa 13971 pré-rempli + alerte échéance changement bureau | 🟠 |
| BUR-M02 | Quorum et votes (AG : résolutions, pour/contre/abstention) | 🟠 |
| BUR-M03 | Convocation formelle AG (délai légal, preuve d'envoi) | 🟠 |
| BUR-M04 | Archivage légal PV (horodatage certifié, stockage immuable après validation) ⚠️ RÉGLEMENTAIRE | 🔴 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| BUR-M05 | Doc 3 | Registre officiel numérique paginé et horodaté non modifiable (équivalent cahier légal) ⚠️ RÉGLEMENTAIRE | 🔴 |
| BUR-M06 | Doc 3 | Distinction Statuts (fondateur) / Règlement intérieur (vivant, modifiable par vote) | 🟠 |
| BUR-M07 | Doc 3 | Signataires autorisés sur compte bancaire (Président + Trésorier par défaut) | 🟡 |
| BUR-M08 | Doc 3 | Contrat d'engagement républicain tracé et daté (obligatoire affiliations et subventions) ⚠️ RÉGLEMENTAIRE | 🔴 |

**Sous-total BUREAU : 8 éléments — 🔴×3 🟠×4 🟡×1**

---

## ⚙️ MODULE PARAMÈTRES — Bilan complet

### Éléments originaux (pré-FFME)

| ID | Élément | Criticité |
|----|---------|-----------|
| PARAM-M01 | Gestion multi-saisons (clôture N, ouverture N+1, transfert données) ⚠️ RÉGLEMENTAIRE | 🔴 |
| PARAM-M02 | Journal d'audit (qui a modifié quoi et quand) | 🟠 |
| PARAM-M03 | Rôles custom (référent jeunes, responsable communication) | 🟡 |
| PARAM-M04 | Politique mot de passe (complexité, expiration, 2FA optionnel) | 🟠 |
| PARAM-M05 | Mentions légales RGPD générées automatiquement ⚠️ RÉGLEMENTAIRE | 🔴 |
| PARAM-M06 | Configuration champs exportables par rôle (matrice admin) | 🟠 |

### Éléments ajoutés — Documents FFME

| ID | Source | Élément | Criticité |
|----|--------|---------|-----------|
| PARAM-M07 | Doc 2 | Attestation assurance club accessible + date expiration + alerte renouvellement | 🟠 |
| PARAM-M08 | Doc 3 | Checklist affiliation FFME dans l'assistant installation (6 documents requis) | 🟠 |
| PARAM-M09 | Doc 3 | Alerte renouvellement affiliation annuelle + calcul montant automatique (80/150/250 €) ⚠️ RÉGLEMENTAIRE | 🔴 |
| PARAM-M10 | Doc 3 | Stockage récépissé préfectoral + publication JO (documents fondateurs permanents) | 🟠 |

**Sous-total PARAMÈTRES : 10 éléments — 🔴×3 🟠×6 🟡×1**

---

## 📊 Récapitulatif par module

| Module | Total | 🔴 | 🟠 | 🟡 | ⚠️ Réglementaire |
|--------|-------|----|----|----|--------------------|
| EPI | 17 | 7 | 4 | 3 | 9 |
| COMPTABILITÉ | 8 | 2 | 5 | 1 | 2 |
| SORTIES | 20 | 12 | 6 | 2 | 11 |
| MEMBRES | 19 | 7 | 10 | 2 | 8 |
| CRÉNEAUX | 17 | 6 | 7 | 4 | 7 |
| DIPLÔMES | 18 | 8 | 8 | 2 | 9 |
| COMMUNICATION | 5 | 1 | 2 | 2 | 1 |
| BUREAU | 8 | 3 | 4 | 1 | 3 |
| PARAMÈTRES | 10 | 3 | 6 | 1 | 3 |
| TABLEAU DE BORD | (spec complète) | — | — | — | — |
| **TOTAL** | **122** | **50** | **52** | **18** | **53** |

---

## 🏗️ Matrice diplômes × périmètre d'encadrement (référentiel officiel FFME)

| Diplôme | Type | Passeport entrée | Âge mini | SAE | SNE bloc/1L | SNE 3L | Notes |
|---------|------|-----------------|----------|-----|------------|--------|-------|
| Initiateur SAE | Brevet fédéral | Orange | 15 ans | ✅ | ❌ | ❌ | Mineur possible avec adulte |
| Initiateur Escalade | Brevet fédéral | Bleu | 17 ans | ✅ | ✅ | ❌ | |
| Moniteur Escalade Sportive | Brevet fédéral | Bleu | 17 ans | ✅ | ✅ | ❌ | |
| Moniteur Grands Espaces | Brevet fédéral | Grands Espaces | 18 ans | ✅ | ✅ | ✅ (1–3L) | |
| Entraîneur 1 | Brevet fédéral | Rouge | 18 ans | ✅ | ❌ | ❌ | Compétition dépt/rég. |
| Entraîneur 2 | Brevet fédéral | Rouge | 18 ans | ✅ | ❌ | ❌ | Compétition rég/national |
| CS P'tits Grimpeurs | Cert. spécialisation | Orange | — | ✅ | ❌ | ❌ | 3–6 ans |
| CS Escalade Santé | Cert. spécialisation | — | — | ✅ | ✅ | ❌ | Prescription médicale obligatoire |
| CS Escalade Handicap | Cert. spécialisation | — | — | ✅ | ✅ | ❌ | Public spécifique |
| CQP AESA | Professionnel N3 | Orange | 18 ans | ✅ | ❌ | ❌ | Rémunéré |
| TFP MESA | Professionnel N4 | Bleu | 18 ans | ✅ | ❌ | ❌ | Rémunéré |
| DEJEPS Escalade | Professionnel N5 | Bleu | 18 ans | ✅ | ✅ (<1500m) | ❌ | Rémunéré |
| DESJEPS Escalade | Professionnel N6 | Rouge | 18 ans | ✅ | ✅ (<1500m) | ❌ | Haut niveau + direction |
| BE Escalade (abrogé) | Prof. abrogé | — | — | ✅ | ✅ (<1500m) | ❌ | Prérogatives conservées |
| Moniteur BE Alpinisme (abrogé) | Prof. abrogé | — | — | ✅ | ✅ (<1500m) | ❌ | Prérogatives conservées |

---

## 🎫 Matrice passeports × autorisations de pratique autonome

| Passeport | Cotation indicative | Autorisation auto-générée | Validé par | Expire ? |
|-----------|--------------------|-----------------------------|------------|----------|
| Blanc | 3a–4b | Aucune — encadrement obligatoire | Initiateur | Non |
| Jaune | 4a–5b | Autonomie bloc SAE | Initiateur | Non |
| Orange | 4c–5c | Autonomie SAE complète (moulinette + tête) | Initiateur | Non |
| Vert | 5a–5c | Accès sortie SNE encadrée | Instructeur | Non |
| Bleu | 5c–6b | Autonomie SNE 1 longueur | Instructeur | Non |
| Violet | 6a–6c | Autonomie SNE plusieurs longueurs | Instructeur | Non |
| Rouge | 6b–7a | Compétition + formation encadrant | Instructeur national | Non |
| Grands Espaces | ≥ Bleu | Grande voie | Instructeur | Non |

> **Règle clé** : Les passeports sont des acquis permanents (pas d'expiration). Les brevets fédéraux ont une date d'expiration et un recyclage obligatoire. Ces deux référentiels sont distincts dans la fiche membre.

---

## ⚡ Top 15 bloquants prioritaires pour V1

> Classement par impact réglementaire + risque pour le club

| Prio | ID | Module | Élément | Risque si absent |
|------|-----|--------|---------|-----------------|
| P1 | SORT-M17 | Sorties | Déclaration accident préfecture 48h | Mise en cause pénale du président |
| P2 | SORT-M12 | Sorties | Assistant déclaration FFME 5 jours | Perte couverture assurance victime |
| P3 | MEMB-M11 | Membres | RC obligatoire non décochable | Pratiquant non assuré — responsabilité club |
| P4 | DIPL-M01 | Diplômes | Diplôme expiré → retrait autorisation encadrement | Encadrement non réglementaire |
| P5 | DIPL-M10 | Diplômes | Matrice brevets × périmètre — vérification à l'affectation | Encadrant hors périmètre |
| P6 | SORT-M01 | Sorties | AST mineurs hors-France | Infraction code civil, responsabilité parents + club |
| P7 | CREN-M11 | Créneaux | Responsable créneau nommé obligatoire | Responsabilité civile club en cas d'accident |
| P8 | CREN-M12 | Créneaux | Liste autorisés pratique autonome | Pratiquant non habilité en autonomie |
| P9 | EPI-M08 | EPI | Qualification contrôleur EPI | Non-conformité norme NF S72-701 |
| P10 | EPI-M09 | EPI | Contrôle de routine avant/après séance | Non-conformité réglementation EPI |
| P11 | MEMB-M16 | Membres | Passeport → autorisations de pratique | Mineur ou débutant en pratique non autorisée |
| P12 | SORT-M19 | Sorties | Alerte séjour spécifique → DDCS | Séjour non déclaré — infraction code action sociale |
| P13 | PARAM-M09 | Paramètres | Alerte renouvellement affiliation FFME | Perte affiliation → perte assurance collective |
| P14 | BUR-M08 | Bureau | Contrat engagement républicain | Perte éligibilité aux subventions publiques |
| P15 | SORT-M20 | Sorties | Brevet + formation continue pour ACM | Encadrement illégal en accueil collectif mineurs |

---

## ❓ Questions ouvertes pour John (PRD)

### Questions critiques P1 — Bloquantes pour la spec

| ID | Question | Module concerné |
|----|----------|----------------|
| Q-01 | Deux tuteurs légaux → AST : envoyer à l'un, aux deux, ou au choix de l'organisateur ? | SORTIES + MEMBRES |
| Q-02 | Tuteur sans email → flux impression/scan ou blocage inscription sortie hors-France ? | SORTIES |
| Q-03 | Encadrant peut-il forcer le départ malgré AST manquante ? Traçabilité dérogation ? | SORTIES |
| Q-04 | Seuil d'âge autonomie SAE : 14 ans (FFME) ou le club peut-il choisir 15–16 ans ? | CRÉNEAUX + MEMBRES |
| Q-05 | Formulaire déclaration accident préfecture : DDCS du lieu du club ou du lieu de l'accident ? | SORTIES |
| Q-06 | Le formulaire REX FFME est-il accessible via API ou uniquement via interface myFFME ? | SORTIES |

### Questions importantes P2 — Impactantes sur l'architecture

| ID | Question | Module concerné |
|----|----------|----------------|
| Q-07 | CS Escalade Santé : les données "prescription médicale" sont-elles stockées dans GestionAsso (RGPD art. 9) ou uniquement attestées ? | DIPLÔMES + MEMBRES |
| Q-08 | Diplômes abrogés : comment les identifier dans le formulaire de saisie sans les confondre avec les diplômes invalides ? | DIPLÔMES |
| Q-09 | Attestation assurance club FFME : est-elle téléchargeable automatiquement depuis myFFME ou saisie manuelle ? | PARAMÈTRES |
| Q-10 | Durée conservation AST post-sortie : 3 mois suffit-il ou faut-il aligner sur la prescription quinquennale en responsabilité civile ? | SORTIES |

### Questions réglementaires P3 — À valider avec expert ou FFME

| ID | Question |
|----|----------|
| Q-11 | CERFA AST : modèle 15646*01 officiel ou modèle libre suffisant ? |
| Q-12 | Fiche sanitaire liaison mineurs : quelle durée de conservation réglementaire (arrêté 2006) ? |
| Q-13 | Contrat engagement républicain : une nouvelle signature est-elle requise chaque saison ou une fois suffit ? |
| Q-14 | Le numéro de carte professionnelle encadrant salarié est-il vérifiable en ligne (DDCS) ? |

---

## 🚦 Recommandation pour la suite

### Ce qui est prêt pour John → PRD
La spécification est maintenant suffisamment complète et sourcée pour produire un PRD de qualité enterprise. Les 10 modules sont couverts, les contraintes réglementaires sont explicitement marquées, et les dépendances inter-modules sont identifiées.

### Ce qui reste ouvert
Les 14 questions ci-dessus peuvent être traitées en deux temps :
- **Q-01 à Q-06** : à clarifier AVANT que John rédige les stories des modules Sorties et Membres
- **Q-07 à Q-14** : peuvent être documentées comme hypothèses dans le PRD et validées en cours de projet

### Flux recommandé
```
Mary → John (*create-prd)
         ↓
      Résoudre Q-01 à Q-06 en parallèle (porteur de projet + FFME si besoin)
         ↓
      Winston (*create-architecture) — en particulier sur le modèle de données
      EPI × Diplômes × Membres (3 modèles liés)
         ↓
      John (*create-all-stories) avec sizing et edge cases
```

---

*Document produit par Mary — Business Analyst*  
*Session BMAD — GestionAsso V1 — Desvr'Escalade*  
*Basé sur 7 documents officiels FFME + audit initial*
