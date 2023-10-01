FROM python:3.11.5-alpine

# Install poetry
RUN pip install poetry

# Copy everything
COPY . /app

WORKDIR /app

# Install dependencies
RUN poetry install

CMD ["/bin/sh"]