# 🔄 Workflows BMAD

## Quick Flow
> Pour bug fix ou petite feature isolée

```
Alex (*dev-story) → Quinn (*validate-story) → Done
```

---

## BMad Method Standard
> Pour une feature ou un module complet

```
Mary (*brainstorm)
  → John (*create-prd)
    → Winston (*create-architecture)
      → John (*create-all-stories)
        → Bob (*sprint-planning)
          → [par story] Alex (*dev-story)
            → Quinn (*validate-story)
```

---

## Enterprise Flow
> Pour un projet complet multi-plateformes avec contraintes réglementaires

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

## Règle de transition entre agents

Chaque agent, avant de passer la main :
1. Génère son bloc `> 🗂️ Mémoire`
2. Liste les fichiers dans `> 💾 Fichiers générés`
3. Met à jour `projects/[nom]/context/project-context.md`
4. Met à jour `projects/[nom]/context/[son-prénom]-context.md`
