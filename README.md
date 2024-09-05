# dotcoin-bot

dotcoin bot auto tap multiple account https://t.me/dotcoin_bot

<img width="592" alt="Code_FSk1Mykde5" src="https://github.com/user-attachments/assets/bcdda8ef-d035-429e-9c40-b73698faf92d">

## Features
- Auto create token (login by query_id)
- Auto tap-tap
- Auto complete/claim task
- Auto upgrade booster (multitap and daily attemps)
- Auto refresh token

## Requirement
- Python 3.8+

## How to run
1. Clone/download this repository
2. > pip install -r requirements.txt
3. > python main.py
4. Fill query.txt

## How to get query_id?
1. Open telegram web/desktop
2. Go to Settings - Advanced - Experimental settings - Enable webview inspecting
3. Open bot https://t.me/dotcoin_bot
4. Press F12 or right click then select inspect element
5. Go to Application tab - Session storage - Select app.dotcoin.bot - Select '__telegram__initParams' (copy value start with ```query_id=```)
6. Separate query_id with the newline (for multiple account)
