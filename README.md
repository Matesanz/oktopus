# 👋 oktopus

## 🪧 Description

Graph-GPT your own data with small and efficient llm models!

## 🚀 Basic Usage

```python
import oktopus
```

### 📚 Documentation

To launch documentation:

```bash
mkdocs serve
```

👉 Then go to http://localhost:8000

## 📦 Installation

After cloning the repo, you can install the package using **pip** or **poetry**:

### 🐍 Using Pip

```console
pip install .
```

### 🌹 Using Poetry

```console
poetry install
```

## 🏗️ Development

### 🐋 Devcontainer Environment

It is possible to have a **development environment** up an ready **[using Docker and vscode](https://code.visualstudio.com/docs/remote/containers)**:

![devcontainer_gif](https://microsoft.github.io/vscode-remote-release/images/remote-containers-readme.gif)

1. Install [remote containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in **VSCode**.
   1. Press `Ctrl+P`
   2. Paste `ext install ms-vscode-remote.remote-containers`
   3. Press `Enter`

2. Run the **docker** in development in **VSCode** *(wait, first time takes some time to run)* :

   ```console
   F1 > Open Folder in Container
   Select the desired folder (backend, frontend...)
   ```

It automatically searches for de `.devcontainer/devcontainer.json` file in the root folder.
To apply changes made to the [dockerfile](docker/Dockerfile) or the [devcontainer.json](.devcontainer/devcontainer.json):

   ```console
   F1 > Rebuild Container
   ```

👍 It will **install** automatically **`oktopus`** in development mode and all the [pre-commit hooks](.pre-commit-config.yaml) along all the tools needed for a correct development: black, isort, pylint, mypy, pytest...

### 🧑‍⚖️ Pre-Commit

In order to **keep code and commits quality** we enforce the use of pre-commit by doing:

```console
pre-commit install
```

This will install a bunch of hooks that will check staged files (only the `*.py` staged files) to check that they stick to black, autopep8, isort and some other standards.

## 🙋 Author

🙋 **Name**: Move38

📩 **Email**: matesanz.cuadrado@gmail.com
