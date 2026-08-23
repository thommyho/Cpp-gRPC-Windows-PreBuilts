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


class AutoShutdownHTTPServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, *args, shutdown_delay=2.0, **kwargs):
        super().__init__(*args, **kwargs)

        self.shutdown_delay = shutdown_delay
        self._active_connections = 0
        self._lock = threading.Lock()
        self._shutdown_timer = None
        self._shutting_down = False

    def process_request_thread(self, request, client_address):
        with self._lock:
            self._active_connections += 1

            # A new connection means the server is still being used.
            if self._shutdown_timer is not None:
                self._shutdown_timer.cancel()
                self._shutdown_timer = None

        try:
            super().process_request_thread(request, client_address)
        finally:
            with self._lock:
                self._active_connections -= 1

                # Last connection disappeared.
                if (
                    self._active_connections == 0
                    and not self._shutting_down
                ):
                    self._shutdown_timer = threading.Timer(
                        self.shutdown_delay,
                        self._shutdown_if_idle
                    )
                    self._shutdown_timer.daemon = True
                    self._shutdown_timer.start()

    def _shutdown_if_idle(self):
        with self._lock:
            if self._active_connections != 0:
                return

            if self._shutting_down:
                return

            self._shutting_down = True

        print("No active connections. Shutting down...")

        # shutdown() must be called from a thread other than
        # the thread running serve_forever().
        self.shutdown()


def main():
    site_path = resource_path("site")

    if not site_path.exists():
        print(f"ERROR: Site directory not found: {site_path}")
        return 1

    os.chdir(site_path)

    server = AutoShutdownHTTPServer(
        ("127.0.0.1", 0),
        QuietHTTPRequestHandler,
        shutdown_delay=2.0,
    )

    host, port = server.server_address
    url = f"http://{host}:{port}/"

    print(f"Serving documentation from: {site_path}")
    print(f"Documentation URL: {url}")

    threading.Timer(
        0.2,
        lambda: webbrowser.open(url)
    ).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

    print("Documentation server stopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())