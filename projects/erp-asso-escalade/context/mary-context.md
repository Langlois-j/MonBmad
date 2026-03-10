# Contexte Mary — ERP ASSO ESCALADE (GestionAsso)

## Dernière session
- **Date :** 09/03/2026
- **Livrable produit :** Bilan consolidé audit FFME × Spécification GestionAsso
- **Statut :** ✅ Complet — 7 documents FFME intégrés, 122 éléments spec

## Décisions prises par Mary

| ID | Décision | Confiance |
|----|----------|-----------|
| P1 | RC = cotisation FFME, pas dans GestionAsso | ✅ Élevée |
| P2 | Recyclage : alerte début saison, pas de blocage mid-saison | ✅ Élevée |
| P3 | Validation diplômes = organisme habilité, upload justificatif | ✅ Élevée |
| P4 | Habilitation présidentielle tracée | ✅ Élevée |
| P5 | Passeport permanent, autorisations auto surchargeables | ✅ Élevée |
| P6 | Créneau : responsable obligatoire, masquage si absent | ✅ Élevée |
| P7 | AST : double flux numérique + papier, blocage départ | ✅ Élevée |

## Hypothèses posées

| Hypothèse | Confiance |
|-----------|-----------|
| Guide passeports FFME reconstitué (derrière espace licencié) | ⚠️ Moyenne |
| Diplômes abrogés : prérogatives conservées sans signalement invalide | ⚠️ Moyenne — Q-08 non tranchée |
| Contrat engagement républicain : 1 signature suffit | ⚠️ Moyenne — Q-13 non tranchée |

## Questions ouvertes restantes (à trancher avant PRD)

### Validations utilisateur P8 → P15
| ID | Proposition |
|----|-------------|
| P8 | CREN-M12 : 4 niveaux autonomie générés par passeport, surchargeables, icône feuille présence |
| P9 | EPI-M08 : Gestionnaire EPI = champ obligatoire, diplôme requis, alerte TDB si manquant |
| P10 | EPI-M09 : Contrôle routine = checklist 1 clic + horodatage + case signalement fin créneau |
| P11 | MEMB-M16 : Passeport validé → autorisations auto, restrictions visibles encadrants/Président uniquement |
| P12 | SORT-M19 : Compteur mineurs temps réel, alerte séjour spécifique à 7 (non paramétrable) |
| P13 | PARAM-M09 : Calcul montant affiliation auto, alertes J-60/J-30, attestation uploadable |
| P14 | BUR-M08 : Contrat engagement républicain — 1 signature, alerte si > 5 ans + subvention |
| P15 | SORT-M20 : Brevet + formation continue vérifiés ACM, blocage si expiré, dérogation Présidente tracée |

### Questions réglementaires Q-07 → Q-14
| ID | Question |
|----|----------|
| Q-07 | CS Escalade Santé : données prescription médicale RGPD art. 9 ou attestées uniquement ? |
| Q-08 | Diplômes abrogés : comment les identifier sans confusion avec invalides ? |
| Q-09 | Attestation assurance FFME : téléchargeable myFFME ou saisie manuelle ? |
| Q-10 | Durée conservation AST : 3 mois ou prescription quinquennale RC ? |
| Q-11 | CERFA AST : modèle 15646*01 officiel ou modèle libre suffit ? |
| Q-12 | Fiche sanitaire liaison mineurs : durée conservation réglementaire (arrêté 2006) ? |
| Q-13 | Contrat engagement républicain : nouvelle signature chaque saison ou une fois suffit ? |
| Q-14 | N° carte professionnelle encadrant salarié : vérifiable en ligne DDCS ? |

## Fichiers générés

| Fichier | Statut |
|---------|--------|
| `projects/erp-asso-escalade/docs/brainstorming/bilan-consolidé-mary-ffme.md` | ✅ Généré |
| `projects/erp-asso-escalade/context/project-context.md` | ✅ Généré |

## Handoff vers agent suivant
- **Agent :** John (*pm)
- **Pré-requis :** Trancher P8→P15 et Q-07→Q-14 avec l'utilisateur
- **Message :** "Spécification complète disponible. 122 éléments, 10 modules. Attends validation des 15 points ouverts avant de lancer *create-prd."
- **Fichiers à transmettre :** `bilan-consolidé-mary-ffme.md` + `project-context.md`

## Bloc de reprise de session
```
Reprends en tant que Mary — Business Analyst sur le projet GestionAsso.
Session précédente : 09/03/2026 — Audit FFME complet, 122 éléments spec.
Il reste à trancher P8→P15 (validations) et Q-07→Q-14 (réglementaire) avant passage à John.
Charge le fichier : https://raw.githubusercontent.com/Langlois-j/MonMbad/main/projects/erp-asso-escalade/context/project-context.md
```

---
*Contexte produit par Mary — Business Analyst*
