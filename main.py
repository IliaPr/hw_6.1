import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'Localhost'
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        '''GET запрос с возвратом текста'''
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('Hello, World wide web!', 'utf-8'))

    def load_json(self):
        with open('user_data.json', 'r') as f:
            return json.load(f)

    def save_json(self, json_data):
        with open('user_data.json', 'w') as f:
            json.dump(json_data, f)
    def do_POST(self):
        '''Прием POST запроса и печать полученных данных'''
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started! http://%s:%s' % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped!')
