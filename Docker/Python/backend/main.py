from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
import json

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode())
        elif self.path == '/get':
            # Connect to MySQL database
            cnx = mysql.connector.connect(user='userIterator', password='qwerty1234', host='172.19.0.2', database='iterator-db')
            cursor = cnx.cursor()
            # Execute your SQL SELECT statement
            query = "SELECT (state) FROM interator"
            cursor.execute(query)
            data = cursor.fetchall()
            # Process your data and send the response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
            cursor.close()
            cnx.close()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/add':
            # Get the POST data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            # Decode the JSON data
            data = json.loads(post_data.decode())
            # Connect to MySQL database
            cnx = mysql.connector.connect(user='userIterator', password='qwerty1234', host='172.19.0.2', database='iterator-db')
            cursor = cnx.cursor()
            # Execute your SQL INSERT statement
            query = f"INSERT INTO interator (state) VALUES ('{data['value']}')"
            cursor.execute(query)
            cnx.commit()
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Added successfully"}).encode())
            cursor.close()
            cnx.close()
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
