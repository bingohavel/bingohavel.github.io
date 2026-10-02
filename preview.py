from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit
ROOT = Path(__file__).resolve().parent / "docs"
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def do_GET(self):
        path = urlsplit(self.path).path
        if not Path(self.translate_path(path)).is_file() and Path(self.translate_path(path + ".html")).is_file():
            self.path = path + ".html"
        super().do_GET()
if __name__ == "__main__":
    print("Open http://127.0.0.1:4173 — stop with Ctrl+C", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 4173), Handler).serve_forever()
