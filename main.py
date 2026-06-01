from saludos import saludar
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(saludar("Nadia").encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    print("Servidor corriendo...")
    server.serve_forever()

