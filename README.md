# 🌸 UDP-in-Python ✨

> **A little project made with love, learning, and a sprinkle of sparkle!** 💕

## 🌸 Acknowledgement for Sakshi

This project is a sincere expression of gratitude to **Sakshi** for providing the GitHub account **ce24f003-stack** and the email information shared with us. Your support has helped us present our skills, learning, and technical work in a professional and meaningful way.

**Thank you very much, Sakshi!** 💗✨ You are truly appreciated, and your encouragement means so much to us. 🌸

## ✨ About This Project

This repository demonstrates a beautiful and simple file-transfer experiment using Python's built-in UDP networking capabilities. It contains a UDP receiver and sender that transfer a text file between two processes on the same computer.

The project showcases:

- 💻 Python programming skills
- 📡 UDP socket communication
- 📁 File handling and binary data transfer
- 👩‍💻 Client-server architecture
- 🌐 Network programming concepts
- 🛡️ Error handling and safe script execution
- 🤝 Teamwork and project documentation
- 🌈️ Creative, clear, and friendly learning projects

## 🥰 Project Structure

- `UDPReceiver.py` — receives a file over UDP and saves it as `received_file.dat` 💌
- `UDPSender.py` — reads a source file and sends it to the receiver 📤
- `test.txt` — sample file used for the experiment 💫
- `README.md` — project documentation and acknowledgement 🌸

## 🚀 How to Run

### 📥 Receiver

Open Terminal 1 and run:

```powershell
python UDPReceiver.py
```

### 📤 Sender

Open Terminal 2 in the same folder and run:

```powershell
python UDPSender.py
```

The receiver will save the transferred file as `received_file.dat`. The file contents should match the original `test.txt` file. 💕

## 💡 Notes

- The sender and receiver must be running on the same computer for local testing.
- To transfer files between different computers, change `RECEIVER_IP` in `UDPSender.py` to the receiver computer's local IP address.
- The current implementation uses UDP chunks and an `EOF` marker to complete the transfer.
- Every little transfer is a step toward stronger networking skills! 🌟

## 💗 Thank You, Sakshi

We are grateful to Sakshi for supporting this project and for helping us demonstrate our skills through this repository. Thank you very much for the GitHub account, email, encouragement, and opportunity to present our work.

**Together, we are learning, building, and growing with love.** 🌸✨

---

💖 **Made with gratitude, curiosity, and a little bit of sparkle!** 💖
