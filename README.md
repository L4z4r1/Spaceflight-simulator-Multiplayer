# Spaceflight-simulator-Multiplayer

Welcome to spaceflight simulator multiplayer made by L4z41

# HOW DOES IT WORK?
This app uses mega's api to upload quick-saves to a cloud, then another client can download the same file


# IS IT SAFE?
YES. It is 100% safe to use, operator of the server can encrypt the data for another security layer


# HOW TO SETUP:

**1.** download python **from their official site**: https://www.python.org/downloads/

**2.** install all the nececary modules:

```pip install mega.py```

```pip install kivy```

*In some cases mega.py wont work, then do ```pip uninstall mega.py``` and then ```pip install mega```*

**3.** download the files:
```git clone https://github.com/L4z4r1/Spaceflight-simulator-Multiplayer.git```

**4.** go to https://mega.nz/ and create a new account

**5.** open the cloned folder and you will see all the scripts, go to ```Network.py``` and find
```python
#Your e-mail and password for MEGA
email = "example@example.com"
password = "xxxxxxxxxxxxx"
```
edit the ```email``` and ```password``` to your email and password for mega.nz

**5.** open the terminal or cmd and type python Main.py

*your working directory must be in the sfs multiplayer folder*

**6.** run ```pyinstaller "~/SFS Multiplayer/Main.py" --noconfirm --onefile --console --name "SFS Multiplayer" --key "[your key]"```
in the working directory

**7.** share the files with some people and enjoy!

# IMAGES:
![mulEx1](https://user-images.githubusercontent.com/107078837/203858883-5b6e576f-cc63-4e5a-99db-fbf84cca435b.png)

# PLANS:

**-** make a way to ban users and operate the "server"

**-** make the app compatible with mods

**-** enhance security

**-** make a way for it to work with android

**-** make it automaticaly sync 

**-** make it automaticaly back-up worlds

**-** fix some known bugs

