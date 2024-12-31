from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.end_headers()

if __name__ == "__main__":
    # 切换到项目根目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 启动HTTP服务器
    port = 8080
    httpd = HTTPServer(('0.0.0.0', port), CORSRequestHandler)
    print(f"提供静态文件服务在 http://localhost:{port}")
    httpd.serve_forever() 