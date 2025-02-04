import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os
from functools import partial

# Set up constants
PORT = 8010
AUTHORIZED_IPS = ["192.168.27.87", "192.168.0.101"]  # Replace with allowed IP addresses
USERNAME = "admin"
PASSWORD = "password"  # Change this to a secure password

# Set the working directory to Downloads
desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Downloads")
os.chdir(desktop)

# Get the local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
s.close()

# Generate a QR code
link = IP
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)

# Open the QR code in the browser
webbrowser.open("myqr.svg")


# Define a custom request handler with security features
class SecureHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]

        # IP whitelisting
        if client_ip not in AUTHORIZED_IPS:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"403 Forbidden: Your IP is not authorized.")
            print(f"Unauthorized access attempt from IP: {client_ip}")
            return

        # Basic Authentication
        auth_header = self.headers.get("Authorization")
        if not auth_header or not self.is_authenticated(auth_header):
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="Secure Area"')
            self.end_headers()
            self.wfile.write(
                b"401 Unauthorized: You must log in to access this server."
            )
            return

        # Serve the file if authentication and IP check pass
        super().do_GET()

    def is_authenticated(self, auth_header):
        import base64

        auth_type, encoded_credentials = auth_header.split(" ", 1)
        if auth_type != "Basic":
            return False
        credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        username, password = credentials.split(":", 1)
        return username == USERNAME and password == PASSWORD


# Start the HTTP server with security
with socketserver.TCPServer(("", PORT), partial(SecureHTTPRequestHandler)) as httpd:
    print("Serving at port", PORT)
    print("Type this in your Browser:", IP)
    print("or Use the QRCode")
    httpd.serve_forever()
