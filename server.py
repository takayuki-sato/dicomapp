import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import dicom
import datetime

class MyDate():
    def get(self):
        return ['date', datetime.date.today().isoformat()]
    
class MyFile():
    def get(self):
        data = dicom.read_file("IM-0001-0069.dcm")
        return ['PatientName', getattr(data, "PatientName")]
    
class MyRequestHandler (BaseHTTPRequestHandler):
    def route(self):
        return {
                '/dates': MyDate(),
                '/files': MyFile(),
        }.get(self.path, None)
    
    def do_GET(self):
        model = self.route()
        
        if model is not None:
            self.send_response(200)
            self.send_header("Content-type:", "application/json")
            self.end_headers()
            
            self.wfile.write(json.dumps(model.get()))
        else:
            self.send_error(404, "Not found")

PORT = 8000
ROOT = '/home/ubuntu/dicomapp/'
os.chdir(ROOT + 'static')

httpd = HTTPServer(("", PORT), MyRequestHandler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

