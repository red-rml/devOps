from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='userIterator', password='qwerty1234', database='iterator-db')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/iterator':
            # Exemple: récupérer toutes les lignes de la table
            cursor.execute("SELECT * FROM interator")
            result = cursor.fetchall()

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'data': result}).encode())
        else:
            self.send_error(404)