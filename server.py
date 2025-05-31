# =============================================================================
# IMPORTS - Import required libraries for web app, encryption, and environment management
# =============================================================================
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import os
from dotenv import load_dotenv

# =============================================================================
# ENVIRONMENT SETUP - Load environment variables from .env file
# =============================================================================
# Load environment variables from .env file in project directory
# This allows storing secrets in a .env file instead of hardcoding them
load_dotenv()

# =============================================================================
# APPLICATION SETUP - Initialize Flask app and SocketIO for real-time communication
# =============================================================================
app = Flask(__name__)
socketio = SocketIO(app)

# =============================================================================
# ENCRYPTION CONFIGURATION - AES encryption key and helper functions
# =============================================================================
# Get AES key from environment variable and convert to bytes
# Environment variable allows secure key management without hardcoding
key = os.environ["AES_KEY"].ljust(16).encode()

def encrypt(msg, key):
	"""
	Encrypt a message using AES encryption
	Returns base64-encoded string for safe text transmission
	"""
	iv = get_random_bytes(16)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	padded = pad(msg.encode(), 16)
	encrypted = cipher.encrypt(padded)
	combined = iv + encrypted
	return base64.b64encode(combined).decode()
	
def decrypt(b64msg, key):
	"""
	Decrypt a base64-encoded encrypted message
	Returns original plaintext with padding removed
	"""
	data = base64.b64decode(b64msg)
	iv = data[:16]
	ciphertext = data[16:]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	decrypted = cipher.decrypt(ciphertext)
	return unpad(decrypted, 16).decode("utf-8")

# =============================================================================
# WEB ROUTES - Handle HTTP requests for serving web pages
# =============================================================================
@app.route("/")
def index():
	"""Serve the main HTML page to clients"""
	return render_template("index.html")

# =============================================================================
# WEBSOCKET EVENT HANDLERS - Process real-time messages and connections
# =============================================================================
@socketio.on('connect')
def send_key():
	"""
	Handle new client connections - automatically send AES key to frontend
	SECURITY WARNING: This sends the encryption key in plain text over the network!
	In production, use proper key exchange protocols (Diffie-Hellman, RSA, etc.)
	This approach is only suitable for learning/development purposes.
	"""
	emit('aes_key', key.decode())  # Convert bytes back to string and send to client

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
	    plaintext = decrypt(data, key)
	    print(f"Client: {plaintext}")

	    # Create and send encrypted response
	    response = encrypt(f"{plaintext}", key)
	    emit("message", response)
	except Exception as e:
	    # Log any decryption errors
	    print(f"Error decrypting: {e}")

# =============================================================================
# APPLICATION STARTUP - Start the server when script is run directly
# =============================================================================
if __name__ == "__main__":
	ssl_context = (os.getenv("SSL_CERT"), os.getenv("SSL_KEY"))
	# Run server on all network interfaces, port 5000
	socketio.run(app, host="0.0.0.0", port=5000, ssl_context=(ssl_context))
