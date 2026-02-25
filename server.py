import time
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

WORDS = [
    "apple", "bridge", "castle", "dragon", "ember", "forest", "glacier", "harbor",
    "island", "jungle", "kernel", "lagoon", "marble", "nebula", "ocean", "planet",
    "quartz", "river", "signal", "thunder", "umbrella", "valley", "willow", "xenon",
    "yellow", "zenith", "anchor", "breeze", "candle", "desert", "eclipse", "falcon",
    "garden", "hollow", "ivory", "jasper", "knight", "lantern", "meadow", "north",
    "orbit", "prism", "quest", "riddle", "silver", "torch", "uplift", "violet",
    "window", "xylem", "yarn", "zephyr", "amber", "bloom", "coral", "dune",
    "eagle", "fern", "gravel", "horizon", "ink", "jade", "kite", "lava",
    "moss", "nova", "onyx", "pebble", "rain", "stone", "tide", "umber",
    "veil", "wave", "axis", "blaze", "crest", "dawn", "echo", "flame",
]


class SSEHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/sse":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            words = random.sample(WORDS, 50)
            for word in words:
                self.wfile.write(f"data: {word}\n\n".encode())
                self.wfile.flush()
                time.sleep(0.25)

            self.wfile.write(b"event: done\ndata: \n\n")
            self.wfile.flush()
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), SSEHandler)
    print("SSE server running on http://localhost:8080")
    print("Connect to http://localhost:8080/sse")
    server.serve_forever()
