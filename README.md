<p align="center">
  <img src="https://raw.githubusercontent.com/Uwu-Kagami/Python_Vercel_Ip_Puller/refs/heads/main/src/image/5IcjJw5.gif">
</p>

<h1 align="center">IP Logger - Discord Webhook</h1>
<p align="center">
  <a href="https://github.com/tonpseudo/YourRepoName/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-important">
  </a>
  <a href="https://github.com/Uwu-Kagami/logging_py?tab=readme-ov-file">
    <img src="https://img.shields.io/github/repo-size/tonpseudo/IP-Logger.svg?label=Repo%20size&style=flat-square">
  </a>
</p>

This script is designed to log IP addresses and user-agent strings from incoming requests. When triggered, the script collects this data and sends it to a Discord webhook in a formatted message.

---

## Disclaimer 
This script is meant for educational purposes only. It should be used responsibly and within ethical guidelines. Make sure to obtain explicit consent from the users whose data you are collecting. Misuse of this script may be illegal and violate privacy rights. ( old backdoor not working anymore ) 

---

# Features
- [x] **Logs IP addresses**: Collects the IP address of incoming requests.
- [x] **Logs User-Agent**: Collects the User-Agent string from the incoming requests.
- [x] **Sends Data to Discord**: Sends the collected data (IP address and User-Agent) to a configured Discord webhook.
- [x] **Easy to Set Up**: Simple configuration via the `WEBHOOK_URL` variable for sending logs to Discord.
- [x] **Error Handling**: Catches and reports errors with a 500 status code in case of failure.

---

### Requirements
- Python 3.x
- Required libraries:
  - `requests` (for sending data to Discord)
  - `flask` (for handling HTTP requests, if using Flask as a server)
  - `fastapi` (if you prefer FastAPI instead of Flask)
  - `python-dotenv` (for environment variable management)

**Note**: The required libraries will be automatically installed if they are not already present on the user's machine. This may take some time during the first execution as the missing modules are installed in the background.

Alternatively, you can manually install the required libraries using `pip`:

```bash
pip install requests flask fastapi python-dotenv
