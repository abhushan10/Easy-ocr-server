## "Coded By" : "ABHUSHAN",
## "Country" : "Nepal"
## contact : github/abhushan10 
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import *
import easyocr
import base64 ,json
encode_img_fetch = ""
image_to_text_converted = ''
class echohandler(BaseHTTPRequestHandler):    
    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        global encode_img_fetch
        global image_to_text_converted
        if self.path.startswith('/admin'):
            encode_img_fetch =self.path[7:].encode().decode()
            encode_img_fetch = unquote(encode_img_fetch)
            base64_img_bytes = encode_img_fetch.encode('utf-8')
            decoded_image_data = base64.decodebytes(base64_img_bytes)
            if encode_img_fetch != "":
                print("[+] Encoded Image Recieved")
                def recognize_text(img_path):
                    #loads an image and recognizes text.
                    text = ''
                    reader = easyocr.Reader(['en'],gpu = False)
                    results = reader.readtext(img_path)
                    for result in results:
                        text += result[1] + ' '
                    return text
                image_to_text_converted = recognize_text(decoded_image_data)
                print('\n =================== \n')
            else:
                print("[!] No Encoded Image Recieved")
            
        
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path.endswith('/bot'):
            if encode_img_fetch != "" and encode_img_fetch != "None" and encode_img_fetch != None:
                global image_to_text_converted
                created = {
                "Text-From-Image" : "{}".format(image_to_text_converted),
                }
                self.wfile.write(json.dumps(created).encode())
            else:
                print("[!] Wait No Image have Recieved: Wait dude..!!")
        

        ## "Coded By" : "ABHUSHAN",
         ## "Country" : "Nepal"
#-------------CONNECTION--------------#      
def main():
    try:
        port = 8080
        server = HTTPServer(('0.0.0.0',port), echohandler)
        print("[+] Server Running on : ", port)
        server.serve_forever()
    except KeyboardInterrupt:
        print("[-] Closing Server.!!")


if __name__ == '__main__':
    main()


    ## "Coded By" : "ABHUSHAN",
         ## "Country" : "Nepal"