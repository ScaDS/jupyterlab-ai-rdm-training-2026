# Trainer notes

Internal notes for running the one-day format (10:00–16:00). These notes are not part of the published site.

## Before the day

- [ ] Fill in the provider-specific section in `preparation/readme.md` (account, API key, model names).
- [ ] Put the same model names into `preparation/secrets.sample` as defaults (`LLM_MODEL`, `LLM_MODEL_CODER`), so participants only need to add their key.
- [ ] Check the endpoint's **rate limits and concurrency** for the expected number of participants. Every hands-on block from 11:15 onwards sends requests from all participants at the same time.
- [ ] Run all notebooks once against the endpoint (`0` to `7`, including the generated notebook in `3`) and time the slowest prompts, especially the notebook generation with `LLM_MODEL_CODER`.
- [ ] Send a reminder about the preparation a few days before, asking participants to run `0_setup-check`.
- [ ] Update the slides: date, venue/event template, training-materials link and QR code, and screenshots of the LLM service you use.
- [ ] Rebuild the participant download: `python scripts/build_download.py` (CI does this automatically on push).

## Timing per block

| Time | Min | Block | Must do | Cut first if late |
|---|---|---|---|---|
| 10:00 | 15 | Welcome, pipeline | Pipeline slide: it is the storyline of the day | "Who are you?" round → show of hands |
| 10:15 | 25 | Setup, uv | `0_setup-check` for everyone; uv slides | Explain uv only via the slides |
| 10:40 | 20 | NB 1 | Run cells, Markdown, execution-order pitfall | Keyboard-shortcut practice |
| 11:00 | 15 | Break | | |
| 11:15 | 50 | LLM slides + NB 2 | env vars, init, `%bob`, `{var}`, `%%fix`, system prompt, loading the steward prompt from env | Letting the assistant write a system prompt (demo only), `%%doc` |
| 12:05 | 25 | NB 3 part 1 | First look + `{df}` impression, plan, code generation; **start the notebook generation at ~12:25** | Plan prompt → show `examples/my-plan.md` |
| 12:30 | 60 | Lunch | | |
| 13:30 | 15 | NB 3 part 2 | Review the generated notebook against the checklist | Show `examples/field_samples_exploration.ipynb` instead |
| 13:45 | 40 | NB 4 | Schema, validation with `lazy=True`, failure table, save YAML | Schema comparison prompt; "Your turn" |
| 14:25 | 35 | NB 5 | Report, alerts, cleaning, re-validation, fix vs. flag | Report on cleaned data (optional cell) |
| 15:00 | 30 | NB 6 | describe → descriptions → package → validate | Assistant prompt for descriptions (use the reference) |
| 15:30 | 20 | NB 7 | Part A: DMP draft and critical reading | Part B hands-on → trainer demo only |
| 15:50 | 10 | Wrap-up | | |

The afternoon runs 2.5 hours without a planned break. Suggest a 5-minute stretch between notebooks 5 and 6 if the group is tired. The time for it comes out of the NB 5 buffer.

## Fallbacks

- **Slow or failing LLM responses:** every generating prompt has a reference cell right below it. Participants run the reference cell and continue. The checkpoints (`checkpoints/`) cover the file hand-offs between notebooks 4 → 5 → 6 → 7.
- **Participant without a working setup:** pair them with a neighbour. Do not debug installations for more than a few minutes during the setup block.
- **No Zenodo token:** the deposit cells skip themselves. The publish cell defaults to `confirm = False`, so publish in your demo only after reviewing the draft.

## What changed compared to the two-session version

- One dataset (`field_samples_raw.csv`) for the whole day. The former Session 1 exploration on `penguins_raw.csv` now runs on the same data and replaces the Session 2 toolbelt overview.
- Session 1 notebooks 2 and 3 are merged into `2_ai-assistant`.
- Model names come from `LLM_MODEL` / `LLM_MODEL_CODER` in `secrets` instead of being hard-coded (`mini`, `coder`).
- New: `0_setup-check`, catch-up cells, `checkpoints/`, `examples/field_samples_exploration.ipynb` (hand-written reference).
- The API key is no longer printed in notebook 2 (masked check instead).
- The Zenodo publish cell defaults to `confirm = False`.
- All packages are installed via `pyproject.toml` up front, no `uv add` needed on the day.
