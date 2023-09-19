# Use a imagem base Python
FROM python:3.11
ENV PYTHONUNBUFFERED 1

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt

