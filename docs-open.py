#!/usr/bin/env python3

import os
import sys
import threading
import webbrowser
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path


class QuietHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def main():
    site_path = resource_path("site")

    if not site_path.exists():
        print(f"ERROR: Site directory not found: {site_path}")
        return 1

    # Serve files from the bundled site directory
    os.chdir(site_path)

    # Use port 0 so Windows chooses an available port
    server = ThreadingHTTPServer(
        ("127.0.0.1", 0),
        QuietHTTPRequestHandler
    )

    host, port = server.server_address
    url = f"http://{host}:{port}/"

    print(f"Serving documentation from: {site_path}")
    print(f"Documentation URL: {url}")

    # Start browser after server is ready
    threading.Timer(
        0.2,
        lambda: webbrowser.open(url)
    ).start()

    try:
        # IMPORTANT: keep the executable alive
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
        server.server_close()

    return 0


if __name__ == "__main__":
    sys.exit(main())