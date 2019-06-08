from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep

PORT = 8080

class theHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if self.path.endswith(".mp3"):
                mimetype = 'audio/mpeg'
                sendReply = True
            if self.path.endswit(".mp4"):
                mimetype = 'video/mp4'
                sendReply =  True

            if sendReply == True:
                f = open(curdir + sep +self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
try:
    server = HTTPServer(('', PORT), theHandler)
    print('Started the web server on port number ', PORT)

    server.serve_forever()

except KeyboardInterrupt:
    print('^C recieved, shutting down the web server')
    server.socket.close()
