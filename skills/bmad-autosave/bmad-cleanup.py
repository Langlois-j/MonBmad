"""
BMAD Autosave — Script de nettoyage des contextes de discussion
Langage : Python 3 — NE PAS UTILISER POWERSHELL
Usage   : python bmad-cleanup.py [--execute]

Les chemins sont lus depuis les variables d'environnement ou les valeurs par défaut.
Aucun chemin local n'est hardcodé dans ce script.

Variables d'environnement optionnelles :
  CLAUDE_CONTEXT_PATH  → dossier Documents\Claude\Contexte\
  LEVELDB_PATH         → fichier 000019.log du LevelDB Claude Desktop
"""

import os
import re
import shutil
import glob
from pathlib import Path

# ─── Configuration via variables d'environnement ───────────────────────────────

def trouver_leveldb() -> Path:
    """
    Cherche automatiquement le fichier LevelDB de Claude Desktop.
    Supporte plusieurs versions du package (id variable selon installation).
    """
    # Chercher dans LocalAppData\Packages tous les packages Claude
    local_app = Path(os.environ.get("LOCALAPPDATA", ""))
    packages = local_app / "Packages"
    candidats = list(packages.glob("Claude_*/LocalCache/Roaming/Claude/IndexedDB/https_claude.ai_0.indexeddb.leveldb/000019.log"))
    if candidats:
        return candidats[0]
    raise FileNotFoundError("LevelDB Claude Desktop introuvable. Claude Desktop est-il installé ?")


LEVELDB_LOG = Path(os.environ.get("LEVELDB_PATH", "")) if os.environ.get("LEVELDB_PATH") else None
if not LEVELDB_LOG:
    try:
        LEVELDB_LOG = trouver_leveldb()
    except FileNotFoundError as e:
        LEVELDB_LOG = None

CONTEXTE_DIR = Path(os.environ.get(
    "CLAUDE_CONTEXT_PATH",
    Path.home() / "Documents" / "Claude" / "Contexte"
))

# ─── Fonctions ────────────────────────────────────────────────────────────────

def lire_uuids_actifs(leveldb_path: Path) -> set:
    """
    Lit le fichier LevelDB en mode binaire et extrait tous les UUIDs
    de discussion actifs (pattern: store:chat-draft:[uuid])
    """
    uuids = set()
    try:
        contenu = leveldb_path.read_bytes().decode("utf-8", errors="ignore")
        matches = re.findall(
            r"store:chat[-\w]*:([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})",
            contenu
        )
        uuids = set(matches)
        print(f"✅ {len(uuids)} discussion(s) active(s) trouvée(s) dans Claude Desktop")
    except FileNotFoundError:
        print(f"❌ Fichier LevelDB introuvable : {leveldb_path}")
    except Exception as e:
        print(f"❌ Erreur lecture LevelDB : {e}")
    return uuids


def lister_dossiers_contexte(contexte_dir: Path) -> list:
    """
    Liste les dossiers dans [CLAUDE_CONTEXT_PATH]
    Format attendu : [uuid]-[nom-discussion]
    Retourne une liste de tuples (dossier, uuid, nom)
    """
    dossiers = []
    if not contexte_dir.exists():
        print(f"⚠️  Dossier Contexte introuvable : {contexte_dir}")
        return dossiers

    for dossier in contexte_dir.iterdir():
        if not dossier.is_dir():
            continue
        match = re.match(
            r"^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-?(.*)$",
            dossier.name
        )
        if match:
            uuid = match.group(1)
            nom = match.group(2) or "(sans nom)"
            dossiers.append((dossier, uuid, nom))
        else:
            print(f"⚠️  Dossier ignoré (format non reconnu) : {dossier.name}")

    return dossiers


def nettoyer(uuids_actifs: set, dossiers: list, simulation: bool = True):
    """
    Compare les dossiers locaux avec les UUIDs actifs.
    UUID absent → discussion supprimée → supprimer le dossier
    """
    supprimes = 0
    conserves = 0

    for dossier, uuid, nom in dossiers:
        if uuid not in uuids_actifs:
            if simulation:
                print(f"  🗑️  [SIMULATION] Serait supprimé : {dossier.name}")
            else:
                try:
                    shutil.rmtree(dossier)
                    print(f"  🗑️  Supprimé : {dossier.name}")
                    supprimes += 1
                except Exception as e:
                    print(f"  ❌ Erreur suppression {dossier.name} : {e}")
        else:
            print(f"  ✅ Conservé  : {dossier.name}")
            conserves += 1

    print()
    if simulation:
        print(f"[SIMULATION] {len(dossiers) - conserves} dossier(s) seraient supprimés, {conserves} conservés.")
        print("Lance avec --execute pour appliquer les suppressions.")
    else:
        print(f"Nettoyage terminé — {supprimes} supprimé(s), {conserves} conservé(s).")


# ─── Point d'entrée ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    simulation = "--execute" not in sys.argv

    print("=" * 60)
    print("  BMAD Autosave — Nettoyage des contextes de discussion")
    print("=" * 60)
    print()

    if simulation:
        print("⚠️  Mode simulation — aucun fichier ne sera supprimé")
        print("   Ajoute --execute pour appliquer les suppressions")
        print()

    if not LEVELDB_LOG:
        print("❌ LevelDB introuvable — Claude Desktop est-il installé ?")
        sys.exit(1)

    print(f"📂 Dossier Contexte : {CONTEXTE_DIR}")
    print(f"📄 LevelDB          : {LEVELDB_LOG}")
    print()

    uuids_actifs = lire_uuids_actifs(LEVELDB_LOG)
    if not uuids_actifs:
        print("⚠️  Aucun UUID trouvé — abandon pour éviter une suppression incorrecte.")
        sys.exit(1)

    dossiers = lister_dossiers_contexte(CONTEXTE_DIR)
    if not dossiers:
        print("✅ Aucun dossier de contexte à vérifier.")
        sys.exit(0)

    print(f"📁 {len(dossiers)} dossier(s) de contexte trouvé(s)\n")
    nettoyer(uuids_actifs, dossiers, simulation=simulation)
