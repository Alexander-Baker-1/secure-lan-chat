# 🔐 Secure LAN Chat

A secure, LAN-based encrypted chat app built with Flask + WebSockets.  
Designed to demonstrate all **7 layers of the OSI model** through a real, working project.

---

## 🚀 How to Run

1. Clone or copy this repo to a Linux system.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required Python packages:
   ```bash
   pip install flask flask-socketio pycryptodome
   ```
4. Start the server:
   ```bash
   python3 server.py
   ```

5. On another device (phone, iPad, laptop), visit in your browser:
   ```
   http://<your-server-ip>:5000
   ```
   Example: `http://192.168.1.55:5000`  
   Make sure the device is on the **same local network (LAN)**.

---

## 💬 Features

- End-to-end AES encryption (ECB for demo purposes)
- WebSocket-based real-time messaging
- Flask backend with browser-based frontend
- Cross-device LAN access (any device w/ browser)

---

## 🧠 OSI Model Layers in Action

| Layer | How It’s Used |
|-------|---------------|
| 1. Physical     | Ethernet/Wi-Fi over LAN |
| 2. Data Link    | MAC addressing, ARP between devices |
| 3. Network      | IP addressing & routing (`192.168.x.x`) |
| 4. Transport    | TCP socket on port 5000 |
| 5. Session      | WebSocket connection over TCP |
| 6. Presentation | AES encryption + Base64 encoding |
| 7. Application  | Flask + HTML/JS web app |

---

## ⚠️ Notes

- AES-ECB is **not secure for real applications** — used here for simplicity.
- You must be on the same local network to use this app across devices.
- This is meant as an educational project and OSI model demo, not a production app.

---

## 📁 Folder Structure

```
securechat/
├── server.py
├── templates/
│   └── index.html
├── venv/ (optional)
├── .gitignore
└── README.md
```

---

## 🔧 TODO (Future Ideas)

- Use AES-GCM or TLS for real encryption
- Add multi-user rooms and usernames
- Store chat history (locally or SQLite)
- QR code for device pairing
- Dockerize for easy deployment

---

## 🧠 Author

Made with love and logic by Alexander Baker 🧠✨  
Feel free to fork, remix, and build on top 💻🔥
