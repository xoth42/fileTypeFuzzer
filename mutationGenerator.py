
import os
class MutationGenerator:
    def __init__(self,inputFile,fileType):
        self.inputFile = inputFile
        self.fileType=fileType
        self.fileSize = os.path.getsize(inputFile) / 1000000000 # in bytes -> gigabytes
        
        """F1: replace byte null
        F2: FF
        F3: replace 7f
        F4: replace 4bits with 0
        f5 ...
        """
       
    def getGeneratedFilesAmount(self,sizeLimit=1):
        return Math.floor(sizeLimit / self.fileSize) 
    
        """generate replacement mutation files for fuzzing.
        The sizeLimit is in gigabytes
        """
    def generate(self,mutations,outPath, sizeLimit=1):
        fileAmount =self.getGeneratedFilesAmount(sizeLimit)
        byteFile = open(inputFile, "rb").read()
        byteslength = len(byteFile)
        byteFile = bytearray(byteFile)
        
        def muteReplace(inputF,replacement, location):
            for i in range(location,location+2):
                inputF[i] = replacement

        n = 0
        for i in range(0,bytesLength - 1):
            # walk through file
            for j in range(len(mutations)):
                n+= 1
                if (n >= fileAmount):
                    print("done")
                    quit()
                mutedFile = byteFile # copy for this new file
                muteReplace(mutedFile, mutations[j], i)
                with open(f"{outPath}{i}_{j}.{fileType}", "wb") as F:
                    F.write(mutedFile)
        
    
    