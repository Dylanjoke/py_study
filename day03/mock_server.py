"""一个假的 API 服务器，离线使用。"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

DATA = {
    "id": 1,
    "hitokoto": "今天也要元气满满哦！",
    "from": "本地测试数据",
    "type": "动漫",
    "length": 20,
}


class Handlers(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(DATA, ensure_ascii=False).encode())

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print("本地测试服务器启动，访问 http://127.0.0.1:8000/")
    print("按 Ctrl+C 停止")
    HTTPServer(("127.0.0.1", 8000), Handlers).serve_forever()
