Para ajustar as dependências, execute:

python3 -m venv auth

pip install flask flask-sqlalchemy flask-login flask-migrate
pip install python-dotenv
pip install db-sqlite3
pip install Flask psycopg2 psycopg2-binary
pip install Flask-Session

Para executar a aplicação, execute:

(auth)$ flask run

Read: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login