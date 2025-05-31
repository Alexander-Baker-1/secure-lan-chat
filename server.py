# =============================================================================
# IMPORTS - Import required libraries for web app, encryption, and encoding
# =============================================================================

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from Crypto.Cipher import AES
import base64

# =============================================================================
# APPLICATION SETUP - Initialize Flask app and SocketIO for real-time communication
# =============================================================================

app = Flask(__name__)
socketio = SocketIO(app)

# =============================================================================
# ENCRYPTION CONFIGURATION - AES encryption key and helper functions
# =============================================================================

# 16-byte AES key (must be exactly 16 bytes for AES-128)
key = b"ThisIsA16ByteKey"

def pad(s):
	"""
	Pad string to make length a multiple of 16 bytes (required for AES)
    	Adds spaces to reach the next multiple of 16
    	"""
    	return s + " " * (16 - len(s) % 16)

def encrypt(msg):
    	"""
    	Encrypt a message using AES encryption
    	Returns base64-encoded string for safe text transmission
    	"""
	cipher = AES.new(key, AES.MODE_ECB)
    	padded = pad(msg)
    	encrypted = cipher.encrypt(padded.encode())
    	return base64.b64encode(encrypted).decode()

def decrypt(b64msg):
    	"""
    	Decrypt a base64-encoded encrypted message
    	Returns original plaintext with padding removed
    	"""
	cipher = AES.new(key, AES.MODE_ECB)
    	encrypted = base64.b64decode(b64msg)
    	decrypted = cipher.decrypt(encrypted).decode()
    	return decrypted.strip()

# =============================================================================
# WEB ROUTES - Handle HTTP requests for serving web pages
# =============================================================================

@app.route("/")
def index():
	"""Serve the main HTML page to clients"""
    	return render_template("index.html")

# =============================================================================
# WEBSOCKET EVENT HANDLERS - Process real-time messages from clients
# =============================================================================

@socketio.on("message")
def handle_message(data):
	"""
    	Handle incoming encrypted messages from clients
    	Decrypt, log, create response, and send back encrypted reply
    	"""
    	try:
		# Decrypt the incoming message
        	plaintext = decrypt(data)
        	print(f"Client: {plaintext}")

		# Create and send encrypted response
        	response = encrypt(f"Server says: {plaintext}")
        	emit("message", response)
    	except Exception as e:
		# Log any decryption errors
        	print(f"Error decrypting: {e}")

# =============================================================================
# APPLICATION STARTUP - Start the server when script is run directly
# =============================================================================

if __name__ == "__main__":
	# Run server on all network interfaces, port 5000
    	socketio.run(app, host="0.0.0.0", port=5000)
