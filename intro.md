# JupyterLab, AI Assistant, and Python for Research Data Management

A one-day hands-on training by [Come2Data](https://come2data.de/) and [ScaDS.AI](https://scads.ai/). Participants learn to use JupyterLab with an integrated AI assistant as a workbench for research data management tasks. They use it to turn a messy raw dataset into a validated, documented, deposit-ready data package.

Slides: [jupyter-ai-rdm.pdf](slides/jupyter-ai-rdm.pdf)

## Learning objectives

By the end of the day you will be able to:

1. Manage a reproducible Python project and environment with `uv`.
2. Work in JupyterLab and Jupyter notebooks.
3. Use the `bia-bob` AI assistant to generate, explain, and fix code, and adapt it to the Research Data Management domain with a system prompt.
4. Explore a raw dataset and draft a plan and documentation with the assistant, then read and verify what it produced.
5. Define and enforce a data schema (a "data contract") with `pandera`.
6. Generate a data quality report with `fg-data-profiling` and apply light, documented cleaning.
7. Build a documented, FAIR data package with `frictionless`.
8. Draft a Data Management Plan (DMP) section and, optionally, deposit the package to the Zenodo Sandbox via its API.

The rule for the whole day is **AI-first, but always understand and verify**: the assistant drafts, you read, run, and check.

## Before the training

Follow the [preparation](preparation/readme.md) instructions and run the setup check notebook. **Make sure to complete this a few days before the training session.** The setup slot on the day is only meant for fixing small problems, not for installing everything from scratch.

## Agenda

| Time | Block | Material |
|---|---|---|
| 10:00 – 10:15 | Welcome, introduction, the data steward pipeline | Slides |
| 10:15 – 10:40 | Setup check, Python projects with `uv` | Slides, `0_setup-check` |
| 10:40 – 11:00 | JupyterLab and notebooks | `1_jupyterlab-basics` |
| 11:00 – 11:15 | *Coffee break* | |
| 11:15 – 12:05 | LLMs and the AI assistant in JupyterLab | Slides, `2_ai-assistant` |
| 12:05 – 12:30 | Explore and plan (part 1) - start notebook generation before lunch | `3_explore-and-plan` |
| 12:30 – 13:30 | *Lunch break* | |
| 13:30 – 13:45 | Explore and plan (part 2) - review the generated notebook | `3_explore-and-plan` |
| 13:45 – 14:25 | Validate: schema as data contract | `4_data-validation` |
| 14:25 – 15:00 | Report and clean | `5_quality-report` |
| 15:00 – 15:30 | Metadata and FAIR packaging | `6_metadata-packaging` |
| 15:30 – 15:50 | DMP and deposit | `7_dmp-and-deposit` |
| 15:50 – 16:00 | Wrap-up | Slides |

The morning is about *getting to know your tools*, and the afternoon about *using them productively*. One dataset runs through the whole day:

> EXPLORE → VALIDATE → REPORT & CLEAN → PACKAGE → DMP & DEPOSIT

## Falling behind?

Every notebook from 5 onwards starts with a **catch-up** cell. It copies the reference results of the previous notebook from `checkpoints/` into `outputs/`, so you can continue with the group at any time. Every step where the assistant generates code also comes with a reference solution.

## After the training

Everything you need to repeat the exercises at home is in the [download](). You can use any OpenAI-compatible LLM endpoint you have access to.

## License

Content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).  
Code: [MIT](https://opensource.org/licenses/MIT).
