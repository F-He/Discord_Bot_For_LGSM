# A Discord Bot For [LGSM](https://linuxgsm.com/)

Tired of logging into your server?  
Do you just want to manage your game servers via discord?  
I got the solution for you!

## Features
- Start and stop your game servers
- Check if a game server is running
- List all your configured game servers

## How to install:
1. Install [python3.7.x](https://www.python.org/downloads/release/python-373/)
2. Clone this repo to the directory you want it to be:  
`git clone https://github.com/F-He/Discord_Bot_For_LGSM.git`
3. Install the dependenices:  
`pip install -r requirements.txt`
4. Add your [discord bot](https://discordapp.com/developers/applications/) token to the `config.ini`
5. Add the servers you want to control via the bot to the `config.ini`
6. Adjust the `config.ini` to your needs
7. `cd` into the `/discord_bot` directory and start the bot with `sudo python3.7 main.py`


## Example Config

```ini
[general_settings]
bot_status = !help for infos
bot_token = YOUR_BOT_TOKEN_HERE
command_prefix = !

; Needs to be a Hex value.
bot_embed_color = #547e34

; Specify if and how many game servers can run at the same time.
; If turned off only one server can run at the same time.
allow_parallel_running = on
max_parallel_running_count = 200


[command_settings]
; Cooldown time in seconds between server commands.
start_server_cooldown = 30
stop_server_cooldown = 10

; Specify which role can execute a command.
; Can currently only be one role.
; The role name needs to be the exact same as in discord(including caps and spelling).
list = @everyone
status = @everyone
start = @everyone
stop = @everyone
update = @everyone
reloadConfig = @everyone


[game_servers]
; Specify here which game servers the bot should manage.
; For example a gmod server is registered like this:
; gmodserver = /home/gmodserver/gmodserver
; The value on the left represents the corresponding Linux User
; and the value on the right represents the path to the server file.
gmodserver = /home/gmodserver/gmodserver
mcserver = /home/mcserver/mcserver
hexxit = /home/hexxit/mcserver
the1710 = /home/the1710/mcserver
mc_creative = /home/mc_creative/mcserver
mc_vanilla = /home/mc_vanilla/mcserver
mc_skyblocks = /home/mc_skyblocks/mcserver
mc_173 = /home/mc_173/mcserver
seven_days = /home/seven_days/sdtdserver


[command_aliases]
; Split aliases with "," like this: help,info,?,serverinfo 
help = info,?,hp
status = stat,su
start = st
stop = sp
update = ud
reloadConfig = rc
list = ls


[command_descriptions]
help = Shows all Commands.
start = Starts a Server. [`start <serverName>`]
stop = Stops a Server. [`stop <serverName>`]
list = Lists every configured server.
update = Updates the bot if an update is available
reloadConfig = Reloads the bot config.
```
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details