# A Discord Bot For [LGSM](https://linuxgsm.com/)

Tired of logging into your server?  
Do you just want to manage your game servers via discord?  
I got the solution for you!

## Features
- Start and stop your game servers
- Check if a game server is running
- List all your configured game servers

## Example Config

```ini
[general_settings]
bot_token = BOT_TOKEN_HERE
bot_status = !help for infos
command_prefix = !

; Needs to be a Hex value.
bot_embed_color = #547e34

; Specify if and how many game servers can run at the same time.
allow_parallel_running = True
max_parallel_running_count = 1


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
reloadConfig = @everyone


[game_servers]
; Specify here which game servers the bot should manage.
; For example a gmod server is registered like this:
; gmodserver = /home/gmodserver/gmodserver
; The value on the left represents the corresponding Linux User
; and the value on the right represents the path to the server file.
gmodserver = /home/gmodserver/gmodserver
mcserver = /home/mcserver/mcserver


[command_aliases]
; Split aliases with "," like this: help,info,?,serverinfo 
help = info,?,hp
list = ls
status = stat,su
start = st
stop = sp
reloadConfig = rc


[command_descriptions]
help = Shows all Commands.
start = Starts a Server. [`start <serverName>`]
stop = Stops a Server. [`stop <serverName>`]
```