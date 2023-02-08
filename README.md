# telip
Telegram bot that sends the server public IP to the user when prompted with `/start`

---

By self-hosting a server, you risk having your IP changed by the internet provider without any warning, this provides a way to remotely find out what the new IP is.


Uso
---
1. Install the dependencies: `pip install -r requirements.txt`;
2. Configure your bot through telegram's [@BotFather](https://t.me/botfather);
3. Put the bot token on `config.py` (see `config.example.py`);
4. `python bot.py`;
5. Send `/start` to the bot;
6. At the console it should appear `User of id <YOUR_CHAT_ID> tried starting the bot.`;
7. Put `<YOUR_CHAT_ID>` in the file `config.py`, as a integer of the list `CHAT_ID_LIST`;
8. Run again steps 4 & 5.
