# Preparation

> **Please complete these steps before the training day.** If you run into problems, contact the trainer via [email](mailto:matthias.taeschner@uni-leipzig.de?subject=JupyterLab%20AI%20Training%20Preparation) and bring the output of the setup check notebook.

## 1. Access to an LLM endpoint

The AI assistant connects to a Large Language Model (LLM) through an **OpenAI-compatible API**. For the training you need:

* the **endpoint URL** of the API (`ENDPOINT_URL`)
* a personal **API key** (`OPENAI_API_KEY`)
* the names of two models offered by the endpoint: a general-purpose model (`LLM_MODEL`) and a model specialised in code (`LLM_MODEL_CODER`)

:::{important} TODO for the trainer: provider-specific steps
Describe here how participants get an account and an API key for the LLM endpoint used in the training, and which model names to use.
:::

Keep the API key safe and treat it like a password (because that's exactly what it is). A password manager is a good place for it.

### Optional: Zenodo Sandbox token

Only needed if you want to run the deposit in notebook 7 yourself. Otherwise you follow the trainer's live demo.

1. Register at <https://sandbox.zenodo.org>. This is a test instance and *separate* from the real zenodo.org.
2. Create a personal access token: *Applications → Personal access tokens → New token*, with the scopes `deposit:write` and `deposit:actions`.

## 2. Prepare your laptop

The practical work is done locally on your laptop.

### What you need

* Your laptop with internet access
* Administrator rights to install software
* A terminal:
  * **Windows**: Command Prompt or PowerShell
  * **macOS** / **Linux**: Terminal

### Install uv

[`uv`](https://docs.astral.sh/uv/) is a fast tool for Python project and package management. Install it as described in the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/). Then close and reopen your terminal, and verify:

```bash
uv --version
```

If Python is already installed on your system, `uv` uses it. Otherwise, `uv` [downloads a suitable Python version automatically](https://docs.astral.sh/uv/guides/install-python/#automatic-python-downloads).

### Download and unpack the training materials

* Download [`training_download.zip`](training_download.zip) and unpack it. You get a folder `jupyterlab-ai-training/` with:
  * `pyproject.toml` - the list of Python packages for the training
  * `secrets` - a template for your personal settings
  * `notebooks/`, `data/`, `checkpoints/`, `examples/`

:::{warning} Do not use cloud-synced or network folders
Do **not** place the folder inside OneDrive, Dropbox, Google Drive, iCloud or on a network drive. On many managed laptops these locations restrict running programs and keep syncing files. This can block or corrupt the Python environment, so that `uv sync` or `uv run` fails or hangs.

Use a plain **local** folder instead, e.g. `C:\Users\<you>\jupyterlab-ai-training` (Windows) or `~/jupyterlab-ai-training` (macOS/Linux).
:::

### Create the virtual environment

Open the terminal, go into the unpacked folder, and install all packages:

```bash
cd /path/to/jupyterlab-ai-training
uv sync
```

This creates a local virtual environment in the hidden folder `.venv` and a file `uv.lock` with the exact package versions.

### Fill in your `secrets` file

Open the file `secrets` in a text editor and fill in:

* `ENDPOINT_URL`, `OPENAI_API_KEY`, `LLM_MODEL`, `LLM_MODEL_CODER` - see step 1
* `ZENODO_SANDBOX_TOKEN` - optional, see step 1

Leave `SYSTEM_PROMPT_DATA_STEWARD` as provided.

> **NOTE:** Never share the `secrets` file or commit it to a git repository.

### Start JupyterLab with your secrets

From the `jupyterlab-ai-training/` folder, start JupyterLab so that it loads `secrets` as environment variables:

```bash
uv run --env-file secrets jupyter lab
```

* Your browser opens JupyterLab. If it doesn't, copy the URL shown in the terminal (starting with `http://localhost:8888/lab?token=...`) into your browser.
* To stop JupyterLab, press `Ctrl + C` in the terminal.

### Run the setup check

In JupyterLab, open `notebooks/0_setup-check.ipynb` and run `Kernel > Restart Kernel and Run All Cells...`.

> **If every check prints ✅: Congratulations!** You are ready for the training.

## 3. Recommended: basics of Python and the terminal

No extensive programming knowledge is required, but the training uses Python and the terminal. If you are new to them, these interactive resources help:

* <https://www.w3schools.com/python/default.asp>
* <https://futurecoder.io/course/>
* <https://www.terminaltutor.com/>
