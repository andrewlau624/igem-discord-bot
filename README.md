# Stanford iGEM Discord Bot

A open source **Discord bot** for the Stanford iGEM team that answers **Synthetic Biology questions** using the Groq API and manages server channels.  
Built with **discord.py**, **Flask**, and **Groq LLMs**.  

---

## Features
- **AI Assistant** – Uses Groq’s LLaMA 3.1 model to answer Synthetic Biology questions.  
- **Rate Limiting** – Prevents spam by limiting each user to one query every 10 seconds.  
- **Category Relay** – Automatically reposts messages from `info` and `resources` categories (after deleting originals).  
- **Channel Restrictions** – Only responds when pinged in `#igem-bot` and `#moderation`.  
- **Webserver Keep-Alive** – Simple Flask app keeps the bot alive on services like Render.  

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/andrewlau624/igem-discord-bot
cd igem-discord-bot
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file in the project root:
```bash
DISCORD_TOKEN=your_discord_bot_token
GROQ_API_KEY=your_groq_api_key
PORT=8080
```

## Running Locally
```bash
python main.py
```

## Deploying on Render
1) Push your code to GitHub.

2) Go to Render

3) Create a New Web Service → connect your GitHub repo.

4) Set:

  - Build Command:

  ```bash
  pip install -r requirements.txt
  ```


  - Start Command:
    
  ```bash
  python main.py
  ```

  - Add environment variables in the Render Dashboard (DISCORD_TOKEN, GROQ_API_KEY, PORT).

5) Deploy 🚀


