"""Build the participant download preparation/training_download.zip.

Usage (from the repository root):  python scripts/build_download.py

The zip contains one folder `jupyterlab-ai-training/` with everything participants need:
pyproject.toml, a `secrets` template, notebooks (outputs stripped), data, checkpoints,
examples and - if present - the slides as PDF. Uses the standard library only.
"""
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "preparation" / "training_download.zip"
PREFIX = "jupyterlab-ai-training"

# (source, path inside the zip folder)
FILES = [
    (ROOT / "preparation" / "pyproject.toml", "pyproject.toml"),
    (ROOT / "preparation" / "secrets.sample", "secrets"),
]
FOLDERS = ["notebooks", "data", "checkpoints", "examples"]
OPTIONAL = [(ROOT / "slides" / "training.pdf", "slides/training.pdf")]
SKIP_NAMES = {".DS_Store", ".ipynb_checkpoints", "__pycache__"}
# files participants generate during the training - never ship stale copies
SKIP_FILES = {"notebooks/my-plan.md", "notebooks/field_samples_exploration.ipynb", "notebooks/dmp_draft.md"}


def strip_outputs(raw: bytes) -> bytes:
    nb = json.loads(raw)
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    return (json.dumps(nb, indent=1, ensure_ascii=False) + "\n").encode("utf-8")


def main():
    entries = list(FILES)
    for folder in FOLDERS:
        for path in sorted((ROOT / folder).rglob("*")):
            rel = path.relative_to(ROOT).as_posix()
            if path.is_file() and not SKIP_NAMES & set(path.parts) and rel not in SKIP_FILES:
                entries.append((path, rel))
    entries += [(src, dst) for src, dst in OPTIONAL if src.exists()]

    with zipfile.ZipFile(TARGET, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, dst in entries:
            data = src.read_bytes()
            # notebooks in the examples folder keep their outputs, they are reference solutions
            if src.suffix == ".ipynb" and not dst.startswith("examples/"):
                data = strip_outputs(data)
            zf.writestr(f"{PREFIX}/{dst}", data)
    print(f"Wrote {TARGET.relative_to(ROOT)} with {len(entries)} files")


if __name__ == "__main__":
    main()
