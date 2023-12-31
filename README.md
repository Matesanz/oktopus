# 🐙 Oktopus

![image](https://user-images.githubusercontent.com/44867923/282287164-c5e8f61d-9b9d-418a-821e-72bde01e89aa.jpg)

## 🪧 Description

Store information and retrieve it quickly thanks to NLP techniques (open and **light Transformers models**, not OpenAI api key required 🤗) while **visualizing your data source in a graph**.

Our platform empowers you to **find insight hidden at first sight** by leveraging all your raw data as well as other text-based information sources. We use **extremely lightweight models to reduce the environmental footprint** of all your analysis operations. No need for huge resource-hungry LLMs that take forever on super expensive hardware to run, process documents in just a few milliseconds!

- 🐍 We used Python Backend (**FastAPI**). Powered by **Sentence Transformers** and **Qdrant** Vector Database.
- 💅 **Svelte** Front-End (**Bulma** components and **Svelvet** for points graph)
- 🐳 CI/CD **Github** workflows that deploys on **Dockerhub** and **Digital Ocean** when branches are merged with main on GitHub.

## 🚀 Quick Start

### 🐋 Using Docker

Use **Docker** (🐋💙) to launch the app:

```console
docker run --rm -p 8080:8080 matesanz/oktopus:latest
```

👉 Then go to [http://localhost:80](http://localhost:80)

### 🐍 Using Pip

Use **Pip** (🐍💙) to launch the app: 

```console
git clone https://github.com/Matesanz/oktopus.git
cd oktopus
pip install .
uvicorn oktopus.main:app --reload
```

👉 Then go to [http://localhost:80](http://localhost:80)

## 🚀 Basic Usage

Oktopus is a python package that can be easyly installed with pip:

```bash
pip install git+https://github.com/Matesanz/oktopus.git
```

Then is as simple as:

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
