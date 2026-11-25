# JupyterLab, AI Assistant, and Python for Data Stewards

Materials for a one-day hands-on training (10:00–16:00) by [ScaDS.AI](https://scads.ai/). Participants use JupyterLab with an integrated AI assistant ([bia-bob](https://github.com/haesleinhuepf/bia-bob)) as a data steward workbench. They then turn a messy raw dataset into a validated, documented, deposit-ready data package:

> EXPLORE → VALIDATE → REPORT & CLEAN → PACKAGE → DMP & DEPOSIT

The rendered materials are published via GitHub Pages (see the repository's *About* section).

## Repository layout

| Path | Content |
|---|---|
| `intro.md` | Landing page: learning objectives and agenda |
| `preparation/` | Participant preparation, `pyproject.toml` and `secrets.sample` for the participant environment |
| `notebooks/` | `0_setup-check` and the training notebooks `1`–`7` |
| `data/` | Raw dataset and data dictionary |
| `checkpoints/` | Reference outputs of notebooks 4–6 for catching up |
| `examples/` | Reference results of assistant tasks (plan, exploration notebook, DMP draft) |
| `slides/` | Slide deck (`.pptx` source and `.pdf`) |
| `trainer/` | Trainer notes: timing, cut list, fallbacks (not published) |

## Development

```bash
uv sync                                     # environment incl. jupyter-book
uv run jupyter book start                   # local preview of the site
```

For the notebooks, create a `secrets` file from `preparation/secrets.sample` and start JupyterLab with `uv run --env-file=secrets jupyter lab`.

On every push to `main`, the GitHub Actions workflow builds the site and deploys it to GitHub Pages. In the repository settings, set *Pages → Source* to *GitHub Actions*.

## License

Content: [CC BY 4.0](LICENSE). Code: MIT.

Derived from the two-session materials of the [EOSC CZ Summer School for Data Stewards 2026](https://github.com/ScaDS/eosc-ssds-2026).
