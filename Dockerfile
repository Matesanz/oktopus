# Build Svelte Frontend
FROM node:20 AS build

COPY frontend/ /app
WORKDIR /app

RUN npm install
RUN npm run build

# Build Python FastAPI app
FROM python:3.10-slim
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies using poetry
WORKDIR /app
COPY poetry.lock* pyproject.toml .
RUN pip install poetry==1.7.0 && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-root

# Copy Svelte frontend
COPY --from=build /app/build /static

# Install oktopus binaries
COPY oktopus/ /app/oktopus
RUN pip install . --no-deps 

# Launch app with uvicorn
EXPOSE 80
CMD [ "uvicorn", "oktopus.main:app", "--host", "0.0.0.0", "--port", "80" ]
