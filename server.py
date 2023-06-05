#!/usr/bin/python3

import re
import requests

from http import server

YTINITIALDATA_RE = re.compile(r"ytInitialData = ({.*?});</script>")

with open("index.html", "rb") as f:
  INDEX_HTML: bytes = f.read()

with open("index.js", "rb") as f:
  INDEX_JS: bytes = f.read()

HOST: str = "localhost"
PORT: int = 8080

def ytInitialData_from(id):
  ret = requests.get(f"https://www.youtube.com/channel/{id}/videos")
  ret_txt = ret.text
  return re.search(YTINITIALDATA_RE, ret_txt).group(1)

class http_server_req_handler(server.BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path.startswith("/id/"):
      print("[ == ] Serving ID")
      channel_id = self.path[4:]

      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self.end_headers()
      self.wfile.write(ytInitialData_from(channel_id).encode("utf-8"))

    # then handle `index.js`
    elif self.path == "/index.js":
      print("[ == ] Serving JS")

      self.send_response(200)
      self.send_header("Content-Type", "text/javascript")
      self.end_headers()
      self.wfile.write(INDEX_JS)

    # everything else is redirected to `index.html`
    else:
      print("[ == ] Serving HTML")

      self.send_response(200)
      self.send_header("Content-Type", "text/html")
      self.end_headers()
      self.wfile.write(INDEX_HTML)

def main():
  http_server = server.HTTPServer((HOST, PORT), http_server_req_handler)

  try:
    http_server.serve_forever()
  except KeyboardInterrupt:
    pass

  http_server.server_close()

if __name__ == "__main__":
  main()
