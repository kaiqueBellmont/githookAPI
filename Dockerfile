# Use a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho
COPY . .

# Define as variáveis de ambiente para a execução do Django
ENV DJANGO_SETTINGS_MODULE=githookapi.settings

# Executa as migrações do Django
RUN python manage.py migrate

# Expõe a porta 8000 para acessar a API
EXPOSE 8000

# Comando para iniciar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
