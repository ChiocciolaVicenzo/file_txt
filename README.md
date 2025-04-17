Requisiti:
- Python 3.10+
- PostgreSQL installato e in esecuzione

Clona il progetto: 
https://github.com/ChiocciolaVicenzo/file_txt.git

Crea un Venv sul terminale:

python -m venv venv

Installa le dipendenze:

pip install -r requirements.txt

Crea il file .env:
- DB_NAME: "il nome del db"
- DB_USER: "il nome del utente del db"
- DB_PASSWORD: "la password del utente su del db"
- DB_HOST:host.docker.internal
- DB_PORT: "la porta del db"

Avvio applicazione (su terminale):
- docker-compose up --build
