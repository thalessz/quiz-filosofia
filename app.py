from flask import Flask
import mysql.connector as mysql

app = Flask(__name__)

def connect_sql():
  db_config = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'projeto-filosfia'
  }
  return mysql.connect(**db_config)

@app.route('/')
def main():
  #roda a tela inicial

if __name__ == "__main__":
  app.run(debug=True)