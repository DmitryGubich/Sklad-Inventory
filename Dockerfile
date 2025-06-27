FROM ghcr.io/astral-sh/uv:python3.13-alpine

# Copy the application into the container.
COPY . /src

# Install the application dependencies.
WORKDIR /src
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "app/src/main.py", "--port", "8001"]