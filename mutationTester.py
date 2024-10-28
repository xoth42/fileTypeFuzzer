import os
runner = "open"
from time import sleep
import subprocess
import signal

class fuzzTester:
    def __init__(self, runner, muteDirectory, dumpDirectory, coreDumpDirectory):
        self.muteDirectory = muteDirectory
        self.runner = runner
        self.dumpDirectory = dumpDirectory
        self.coreDumpDirectory = coreDumpDirectory
    def startTesting(self, waitTime,buffer=0,killSignal=signal.SIGTERM):
        for name in os.listdir(self.muteDirectory):
            process = subprocess.Popen([runner, f"{muteDirectory}/{name}"])
            sleep(waitTime)
            
            os.kill(process.pid,killSignal)
         
            sleep(buffer)

            dump=checkfordump()
            if dump is not None:
                os.rename(f"{coreDumpDirectory}", f"./{dumpDirectory}{dump}")
                print("dumped ",end="")
            else:
                os.remove(f"{muteDirectory}/{name}")
            print(name) 

