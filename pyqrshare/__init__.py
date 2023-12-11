import sys
import netifaces as ni
from flask import Flask, make_response, send_file
import pyqrcode
from . import fileToServe
app = Flask(__name__, static_url_path='/')


def check_args():
	if(len(sys.argv)) == 1:
		sys.exit("Provide a file/dir path")
	elif(len(sys.argv)) == 2:
		fileToServe.set_file_to_serve(sys.argv[1])
	elif(len(sys.argv)) > 2:
		sys.exit("Too many arguments")


def return_wlan0_ip():
	try: 
		ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
		return ip
	except KeyError:
		sys.exit("Make sure you are connected to a WiFi network")


def generate_qr():
	url = pyqrcode.create(str(return_wlan0_ip())+':5000')
	return url.terminal(quiet_zone=1)


@app.route('/')
def index():
	response = make_response(send_file(sys.argv[1], as_attachment=True))
	return response


def main():
	check_args()
	print((generate_qr()))
	try:
		app.run(host=return_wlan0_ip(), threaded = True, debug=False, use_reloader = False)
	except:
		sys.exit("Could not establish connection. :( ")
