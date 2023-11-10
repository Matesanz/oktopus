# Description: This script is run after the devcontainer is built.
# It installs the packages defined in pyproject.toml and the local package.
# It also installs pre-commit hooks and starts mkdocs.

GREEN='\033[92m'
BLUE='\033[94m'
END='\033[0m'

# configure git
echo -e "${BLUE}🚀  Launching Devcontainer Post-Install Script${END}\n"
echo -e "${BLUE}🔧  Initializing Pyenv...${END}\n"
eval "$(pyenv init -)"
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# avoid creating virtualenvs in poetry
echo -e "${BLUE}🔧  Configuring Poetry...${END}\n"
poetry config virtualenvs.create false
echo 'poetry config virtualenvs.create false' >> ~/.bashrc

# install packages defined in pyproject.toml and the local package
echo -e "${BLUE}🔧  Installing python dependencies using Poetry..${END}\n"
if [ ! -f "poetry.lock" ]; then
    echo -e "${BLUE}ℹ️  No poetry.lock file found, resolving dependencies, this may take a while, please wait..${END}\n"
fi
poetry self add keyrings.google-artifactregistry-auth@latest  # this is needed to pull private libraries from our GCP Registry
poetry install --no-interaction --no-ansi --no-root
pip3 install -e . --no-deps 
echo -e "${GREEN}✅  Python dependencies installed!${END}\n"

# install pre-commit hooks and start mkdocs
echo -e "${GREEN}✅  Project correctly configured!${END}\n"
echo -e "${BLUE}🔧  Installing pre-commit hooks and starting mkdocs..${END}\n"
pre-commit install
mkdocs serve
