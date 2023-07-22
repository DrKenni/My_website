from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def get_html_content(self):
        with open('index.html', encoding='utf-8') as index_page:
            return index_page.read()

    def do_GET(self):
        query_comp = parse_qs(urlparse(self.path).query)
        print(query_comp)
        page_content = self.get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")