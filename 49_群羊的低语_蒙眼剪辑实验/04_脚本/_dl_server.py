"""Local receiver for browser-fetched Feishu clips.

The browser page fetches each video with its in-session credentials (token never
leaves the browser) and POSTs the raw bytes here. We write them to disk, routing
by filename prefix. Bypasses Chrome's multi-download guard. Binds localhost only.
"""
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

BASE = os.path.join(os.path.dirname(__file__), "..", "02_素材")
RAW = os.path.join(BASE, "raw_clips")
PATCH = os.path.join(BASE, "patch_clips")
REF = os.path.join(BASE, "reference")
for d in (RAW, PATCH, REF):
    os.makedirs(d, exist_ok=True)


def target_dir(name: str) -> str:
    if name.startswith("补"):
        return PATCH
    if name.startswith("成片") or name.startswith("ref_"):
        return REF
    return RAW


class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        q = parse_qs(urlparse(self.path).query)
        name = q.get("name", ["unnamed"])[0]
        n = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(n)
        path = os.path.join(target_dir(name), name + ".mp4")
        with open(path, "wb") as f:
            f.write(data)
        msg = f"{name}.mp4  {len(data)} bytes -> {os.path.relpath(path, BASE)}"
        print(msg, flush=True)
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(msg.encode("utf-8"))

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 8799), H)
    print("receiver on http://127.0.0.1:8799", flush=True)
    srv.serve_forever()
