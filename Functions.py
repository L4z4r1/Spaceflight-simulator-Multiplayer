import Network
import os
import UI_MAIN_BRIDGE as mul



#files that need to be uploaded & downloaded
files = ["Achievements.txt", "Addresses.txt", "Branches.txt", "Rockets.txt", "Version.txt", "WorldState.txt"]

#for configuring your e-mail and password for MEGA, go to "Network.py"

#saving a starting file path
startPath = os.getcwd()

##########################################################################################

#MAIN ACTIONS
def main():
    os.chdir(startPath)
    if os.path.isfile('.data.mul1'):
        print("[+] Save file found, initiating main class")
        #mul.output("[+] Save file found, initiating main class")
    else:
        print("[+] Save file not found, creating a new one")
        #mul.output("[+] Save file not found, creating a new one")
        nf = open(".data.mul1", "w+")
        nf.close()

    # try:
    #     print("[!] " + startPath)
    #     os.chdir(startPath)
    #     print("[+] loading..")
    #     m_loc = open("data.mul1", "r")
    #     load_loc = m_loc.read()
    #     m_loc.close()
    #     print("[?] file location is " + load_loc + "? (Y/n)")
    #     in1 = input("~: ")
    #
    #     if in1 == "y" or in1 == "Y":
    #         pass
    #
    #     elif in1 == "N" or in1 == "n":
    #         os.chdir(startPath)
    #         i = input("(new) SFS Multiplayer file location: ")
    #         nf = open("data.mul1", "w+")
    #         nf.write(i)
    #         nf.close()
    #         pass
    #     try:
    #         interface()

    #    except Exception:
    #       print("[x] something went wrong")
    #
    # except:
    #     os.chdir(startPath)
    #     print("[x] file location not found\n[~/] " + os.getcwd())
    #     i = input("SFS Multiplayer file location: ")
    #     nf = open("data.mul1", "w+")
    #     nf.write(i)
    #     nf.close()
    #     main()

def Upload():
    """
    Uploads the files from given location
    """
    print("[+] delteing files...")
    #mul.output("[+] delteing files...")
    Network.delaf()
    print("[+] Deleted the files")
    #mul.output("[+] Deleted the files")
    m_loc = open(".data.mul1", "r")
    load_loc = m_loc.read()
    print("[+] going to " + load_loc)
    #mul.output("[+] going to " + load_loc)
    os.chdir(load_loc)
    print("[+] declaring the file")
    #mul.output("[+] declaring the file")
    data = os.listdir(load_loc)
    print("[+] sending data")
    #mul.output("[+] sending data")
    for file in data:
        Network.upload(file)
    print("[+] data sent sucessfully")
    #mul.output("[+] data sent sucessfully")
    os.chdir(startPath)

def Download():
    print("[+] download sequence initiated")
    #mul.output("[+] download sequence initiated")
    m_loc = open(".data.mul1", "r")
    print("[+] data loaded")
    #mul.output("[+] data loaded")
    load_loc = m_loc.read()
    print("[+] data files loaded: ", files)
    #mul.output("[+] data files loaded: ", files)
    for file in files:
        Network.download(file, load_loc)
    print("[+] data downloaded")
    #mul.output("[+] data downloaded")
    m_loc.close()
    print("[+] downloaded the files")
    #mul.output("[+] downloaded the files")

def Save(data):
    print("[+] saving data.")
    #mul.output("[+] saving data.")
    m_loc = open(".data.mul1", "w+")
    print("[30%] saving data..")
    #mul.output("[30%] saving data..")
    m_loc.write(data)
    print("[70%] saving data...")
    #mul.output("[70%] saving data...")
    m_loc.close()
    print("[100%] saving data....")
    #mul.output("[100%] saving data....")

def Load():
    print("[+] loading path")
    #mul.output("[+] loading path")
    m_loc = open(".data.mul1", "r")
    print("[20%] loading path")
    #mul.output("[20%] loading path")
    i = m_loc.read()
    print("[70%] loading path")
    #mul.output("[70%] loading path")
    m_loc.close()
    print("[80%] loading path")
    #mul.output("[80%] loading path")
    #mul.output("[100%] loading path")
    return i
    print("[100%] loaded")

#triggering the main function
main()
