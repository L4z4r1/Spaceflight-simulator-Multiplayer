from mega import Mega

mega = Mega({'verbose': True})

#Your e-mail and password for MEGA
email = "example@example.com"
password = "xxxxxxxxxxxxx"

m = mega.login(email, password)

output = ""

def upload(uploadFile):
    #print("[+] files recieved")
    try:
        print("[+] uploading " + uploadFile)
        m.upload(uploadFile)

    except Exception:
        print("[x] something went wrong while uploading files, please check the file destination or make sure that you have internet connection")

def download(data, location):
    print("[+] downloading...")
    try:
      print("[+] finding data...")
      dataf = m.find(data)
      print("[+] found " + data)
      m.download(dataf, location)
      print("[+] downloaded data.zip")

    except Exception:
      print("[x] something went wrong while downloading files, please check the file destination or make sure that you have internet connection")

def delaf():
  print("[+] intitiated deletion...")
  try:
    print("[+] deleting...")
    files = ["Achievements.txt", "Addresses.txt", "Branches.txt", "Rockets.txt", "Version.txt", "WorldState.txt"]
    for file in files:
      print("[+] deleting " + file)
      files1 = m.find(file)
      m.delete(files1[0])
  except:
    print ('[x] An error occurred')

