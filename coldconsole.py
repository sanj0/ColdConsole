import os,platform,time

ostype = platform.system()
SYSdrive = "DRIVE-E.VD"
protectedFiles = [SYSdrive]
commands = {
"read":"read()",
"help":"for i in commands.keys():print(i)",
"createdisk":"i=input('Disk: ');createdisk(i);leave()",
"disks":"for drive in drives: print(drive)",
"sysinfo":"sysinfo()",
"CUN":"i = input('Name: ');CUN(i)",
"mkfile":"mkfile()",
"ls":"ls()",
"del":"DEL()",
"clear":"clear()",
"shutdown":"leave();exit()",
"reboot":"leave();Boot()",
"man":"i = input('Command: ');man(i)"
}

# short descriptions for the commands, you can access them using "man"
manuals = {
"read":"reads out the contents of a file on a disk.",
"help":"lists all commands.",
"createdisk":"creates a new virtual disk.",
"disks":"prints out the names of all disks.",
"sysinfo":"print out system info.",
"CUN":"renames the user.",
"mkfile":"creates a new file.",
"ls":"lists files of a disk",
"del":"deletes a file.",
"clear":"clears the screen.",
"shutdown":"shuts ColdConsole down.",
"reboot":"reboots ColdConsole.",
}

def read():
    i = input("Disk: ")
    if i in drives:
        i += ".VD"
        j = input("Filename: ")

        with open(i,"r") as f:
            exec("ddata="+f.read(),globals())
            f.close()
        print(ddata[j])

    else:
        print("Disk not found!")

def mkfile():
    i = input("Disk: ")
    if i == 'exit':
        pass

    if i in drives:
        i += ".VD"
        j = input("Filename: ")
        data = input("Content: ")

        if j == 'exit' or data == 'exit':
            pass

        with open(i,"r") as f:
            exec("ddata="+f.read(),globals())
            f.close()

        ddata[j]=data

        with open(i,"w") as f:
            f.write(str(ddata))
            f.close()
    else:
        print("Disk not found!")

def ls():
    i = input("Disk: ")
    with open(i+".VD","r") as f:
        exec("for i in {}.keys(): print(i)".format(f.read()))
        f.close()

def clear():
    if ostype != "Windows":
        os.system("clear")
    else:
        os.system("cls")

def Boot():
    try:
        clear()
        print("███████████████████████████████████████")
        print("██ ColdConsole is booting...         ██")
        print("██ Press Ctrl+C to get to ColdRescue ██")
        print("███████████████████████████████████████")
        if not os.path.isfile(SYSdrive):
            clear()
            print("CAN NOT FIND {}! PLEASE DO 'init' and 'reboot'!".format(SYSdrive))
            coldrescue()
        else:
            time.sleep(1.5)
            OS()

    except KeyboardInterrupt:
        clear()
        coldrescue()


def coldrescue():
    print("██████████████████████████████████████████████████████████████████████")
    print("████                                                              ████")
    print("██        ____      _     _ ____                                    ██")
    print("██       / ___|___ | | __| |  _ \ ___  ___  ___ _   _  ___          ██")
    print("██      | |   / _ \| |/ _` | |_) / _ \/ __|/ __| | | |/ _ \         ██")
    print("██      | |__| (_) | | (_| |  _ <  __/\__ \ (__| |_| |  __/         ██")
    print("██       \____\___/|_|\__,_|_| \_\___||___/\___|\__,_|\___| (c)     ██")
    print("██       Safemode for ColdConsole                                   ██")
    print("██                                                                  ██")
    print("████                                                              ████")
    print("██████████████████████████████████████████████████████████████████████")

    while True:
        cmd = input("COLDRESCUE$ ")
        if cmd == "init":
            i = input("Username: ")
            with open(SYSdrive,"w") as f:
                f.write("['{}'];drives = ['']".format(i))
                f.close()
        elif cmd == "read":
            with open(SYSdrive,"r") as f:
                print(f.read())
                f.close()
        elif cmd == "write":
            i = input("Data: ")
            with open(SYSdrive,"w") as f:
                f.write(i)
                f.close()
        elif cmd == "reboot":
            Boot()
        else:
            print("Can't find command: "+cmd)

def OS():
    global drives
    global SYSData
    try:
        try:
            with open(SYSdrive,"r") as f:
                exec("SYSData = {}".format(f.read()),globals())
                f.close()
        except:
            clear()
            print("{} is corrupted! Please do 'init' and 'reboot'!".format(SYSdrive))
            coldrescue()

        clear()
        print("██████████████████████████████████████████████████████████████████████████████████████")
        print("████    \__    __/                                                                ████")
        print("██      /_/ /\ \_\        ____      _     _  ____                      _            ██")
        print("██     __ \ \/ / __      / ___|___ | | __| |/ ___|___  _ __  ___  ___ | | ___       ██")
        print("██     \_\_\/\/_/_/     | |   / _ \| |/ _` | |   / _ \| '_ \/ __|/ _ \| |/ _ \      ██")
        print("██ __/\___\_\/_/___/\__ | |__| (_) | | (_| | |__| (_) | | | \__ \ (_) | |  __/      ██")
        print("██   \/ __/_/\_\__ \/    \____\___/|_|\__,_|\____\___/|_| |_|___/\___/|_|\___| (c)  ██")
        print("██     /_/ /\/\ \_\      Developed by CreepiYT                                      ██")
        print("██      __/ /\ \__                                                                  ██")
        print("██      \_\ \/ /_/                                                                  ██")
        print("████     /      \                                                                 ████")
        print("██████████████████████████████████████████████████████████████████████████████████████")

        while True:
            if not os.path.isfile(SYSdrive):
                clear()
                print("CAN NOT FIND {}! PLEASE DO 'init' and 'reboot'!".format(SYSdrive))
                coldrescue()

            CMD = input("{}$ ".format(SYSData[0]))
            commandparser(CMD)

    except Exception as e:
        clear()
        print(str(e))
        coldrescue()

def createdisk(i):
    if not i.replace(" ","") == "":
        if not i in drives:
            drives.append(i)
        with open(i+".VD","w") as f:
            f.write("{'diskinfo.tmp':''}")
            f.close()

def sysinfo():
    print("Processor: "+platform.processor())

def DEL():
    i = input("Disk: ")

    if i in drives:
        i += ".VD"
        j = input("Filename: ")

        with open(i,"r") as f:
            exec("ddata="+f.read(),globals())
            f.close()

        del ddata[j]

        with open(i,"w") as f:
            f.write(str(ddata))
            f.close()
    else:
        print("Disk not found!")

def CUN(i):
    if not i == "":
        SYSData[0] = i
        with open(SYSdrive,"w") as f:
            f.write(str(SYSData)+";"+str(drives))
            f.close()
    else:
        print("That is not a valid username.");

def leave():
    with open(SYSdrive,"w") as f:
        f.write(str(SYSData)+";drives="+str(drives))
        f.close()

def commandparser(cmd):
    cmd = cmd.replace(" ", "");
    if not cmd == "":
        for Key in commands.keys():
            if cmd == Key:
                exec(commands[Key])
                return True
                break
        else:
            print("Can't find command: "+cmd)

def man(command):
    command = command.replace(" ", "");
    if not command == "":
        for Key in manuals.keys():
            if command == Key:
                print(manuals[Key])
                return True
                break
        else:
            print("Can't find command: " + command)

Boot()
