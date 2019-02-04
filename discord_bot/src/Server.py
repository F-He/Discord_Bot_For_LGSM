from subprocess import Popen, PIPE
# sudo -u gmodserver /home/gmodserver/gmodserver details
class ServerManager():
    def __init__(self):
        pass
        
    
    async def start(self, serverName):
        # call(f"sudo -u gmodserver /home/gmodserver/gmodserver stop", shell=True)
        output = Popen(["sudo", "-u", serverName, f"/home/{serverName}/{serverName}", "start"], stdout=PIPE)
        output_list = output.stdout.readlines()
        print(output_list[len(output_list) - 2].decode("utf-8"))
    
    async def isOnline(self, serverName):
        output = Popen(["sudo", "-u", serverName, f"/home/{serverName}/{serverName}", "details"], stdout=PIPE)
        output_lines = output.stdout.readlines()
        status_line = output_lines[len(output_lines) - 2].decode("utf-8")
        if "online" in status_line.lower():
            return True
        else:
            return False

if __name__ == "__main__":
    servermanager = ServerManager()
    servermanager.start("test")