import http.server
import socket
import ssl
import os
from pystyle import Anime, Colorate, Colors, Center, System, Write

port = 443
server_address = ('0.0.0.0', port)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(Center.XCenter(f"Server running on https://localhost:{port}"))

info = '''
╔═════════════════════════════════════════════════╗
║                HTTP FILE SERVER                 ║
║               coded by CHAINSKI                 ║
║       For Educational Purposes Only             ║
║             Made with Python 3                  ║ 
╚═════════════════════════════════════════════════╝
'''  
print(Colorate.Diagonal(Colors.red_to_white, Center.XCenter(info)))



#os.chdir("./dist/")

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js': 'application/x-javascript',
        '.wasm': 'application/wasm',
        '.json': 'application/json',
        '.xml': 'application/xml',
    }

    def end_headers(self):
        # Include additional response headers here. CORS for example:
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

httpd = http.server.HTTPServer(server_address, CORSHTTPRequestHandler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.check_hostname = False
ctx.load_cert_chain(certfile='cert.pem')  # with key inside
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
