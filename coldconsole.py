import os,platform,time,socket

clientver = '1'

ostype = platform.system()
SYSdrive = "DRIVE-E.VD"
protectedFiles = [SYSdrive]
commands = {
    "exec": "print('Use Python!');i = input('> ');exec(i)",
    "update": "update()",
    "read": "print(read())",
    "help": "for i in commands.keys():print(i)",
    "createdisk": "i=input('Disk: ');createdisk(i);leave()",
    "disks": "for drive in drives: print(drive)",
    "sysinfo": "sysinfo()",
    "CUN": "CUN()",
    "execscript":"execscript()",
#    "mkfile": "mkfile()",
    "ls": "ls()",
    "del": "DEL()",
    "clear": "clear()",
    "shutdown": "leave();exit()",
    "reboot": "leave();Boot()",
    "man": "man()",
    "write": "writedoc()",
    "mount": "i=input('Drive: ');mount(i)"
}

# short descriptions for the commands, you can access them using "man"
manuals = {
    "exec":"executes code",
    "execscript":"executes a file",
    "update":"Updates ColdConsole.",
    "read": "reads out the contents of a file on a disk. \n usage: read -d DISK -f FILE",
    "help": "lists all commands.",
    "createdisk": "creates a new virtual disk.",
    "disks": "prints out the names of all disks.",
    "sysinfo": "print out system info.",
    "CUN": "renames the user. \n usage: cun NAME",
    "mkfile": "creates a new file. \n usage: mkfile -d DISK -f NAME CONTENT",
    "ls": "lists files of a disk \n usage: ls DISK",
    "del": "deletes a file. \n usage: del -d DISK -f FILE",
    "clear": "clears the screen.",
    "shutdown": "shuts ColdConsole down.",
    "reboot": "reboots ColdConsole.",
    "man": "prints a short manual of the given command. \n usage: man COMMAND",
    "mount": "mounts a disk."
}

# the last args that the user gave
args = []

def execscript():
    i = input("Drive: ")
    if i in drives:
        i += ".VD"
        j = input("File: ")

        with open(i, "r") as f:
            exec("ddata=" + f.read(), globals())
            f.close()

        exec(ddata[j])

    else:
        print("Disk not found!")

# read file from disk
def read():
    i = get_arg_value("-d")
    if i in drives:
        i += ".VD"
        j = get_arg_value("-f")

        with open(i, "r") as f:
            exec("ddata=" + f.read(), globals())
            f.close()

        line = 1
        string = ""

        string += str(line)+ " | "

        for i in ddata[j].replace("\n","|"):
            string += i.replace("|","")

            if i.find("|") != -1:
                line += 1
                string += "\n"
                string += str(line)+ " | "
        return string

    else:
        print("Disk not found!")

# make a file on disk
#def mkfile():
#    i = get_arg_value("-d")
#    if i == 'exit':
#        pass
#
#    if i in drives:
#        i += ".VD"
#        j = get_arg_value("-f")
#        data = args[4]
#
#        if j == 'exit' or data == 'exit':
#            pass
#
#        with open(i, "r") as f:
#            exec ("ddata=" + f.read(), globals())
#            f.close()
#
#        ddata[j] = data
#
#        with open(i, "w") as f:
#            f.write(str(ddata))
#            f.close()
#    else:
#        print("Disk" + i + " not found!")

def update():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('95.90.225.117', 10000)
    print('Connecting to {}:{}'.format(*server_address))
    sock.connect(server_address)

    try:
        # Send data
        message = clientver.encode()
        print('Sending Version: {}'.format(message.decode()))
        sock.sendall(message)

        data = sock.recv(400000)
        if data:
            with open(os.path.basename(__file__),"w") as f:
                f.write(data.decode())
                f.close()

    finally:
        sock.close()
        if data:
            clear()
            print("Closing Program in 2 secounds!")
            time.sleep(2)
            exit()

# list files on disk
def ls():
    i = args[0]
    with open(i + ".VD", "r") as f:
        exec ("for i in {}.keys():print(i)".format(f.read()))
        f.close()

def mount(i):
    if not i.replace(" ", "") == "" and os.path.isfile(i+".VD"):
        if not i in drives:
            drives.append(i)

            leave()

            global SYSData
            try:
                with open(SYSdrive,"r") as f:
                    exec("SYSData = {}".format(f.read()),globals())
                    f.close()
                print("Successfully mounted drive "+i)
            except:
                clear()
                print("{} is corrupted! Please do 'init' and 'reboot'!".format(SYSdrive))
                coldrescue()

        else:
            print("Couldn't mount drive "+i)

# clear screen
def clear():
    if ostype != "Windows":
        os.system("clear")
    else:
        os.system("cls")

# Boot from System
def Boot():
    try:
        clear()
        print("███████████████████████████████")
        print("██ ColdConsole is booting... ██")
        print("███████████████████████████████")
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
    print("████░░░                                                        ░░░████")
    print("██░░░     ____      _     _ ____                                 ░░░██")
    print("██░░     / ___|___ | | __| |  _ \ ___  ___  ___ _   _  ___        ░░██")
    print("██░     | |   / _ \| |/ _` | |_) / _ \/ __|/ __| | | |/ _ \        ░██")
    print("██░     | |__| (_) | | (_| |  _ <  __/\__ \ (__| |_| |  __/        ░██")
    print("██░      \____\___/|_|\__,_|_| \_\___||___/\___|\__,_|\___| (c)    ░██")
    print("██░░     Safemode for ColdConsole                                 ░░██")
    print("██░░░                                                            ░░░██")
    print("████░░░                                                        ░░░████")
    print("██████████████████████████████████████████████████████████████████████")

    while True:
        cmd = input("COLDRESCUE$ ")
        if cmd == "init":
            i = input("Username: ")
            j = input("Password: ")
            with open(SYSdrive,"w") as f:
                f.write("['{0}','{1}'];drives = ['']".format(i,j))
                f.close()
#        elif cmd == "read":
#            with open(SYSdrive,"r") as f:
#                print(f.read())
#                f.close()
#        elif cmd == "write":
#            i = input("Data: ")
#            with open(SYSdrive,"w") as f:
#                f.write(i)
#                f.close()
        elif cmd == "reboot":
            Boot()
        else:
            print("Can't find command: "+cmd)

def OS():
    #update()
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
        login = True

        print("Please input your password to login.")
        print("Type *exit to leave.")

        while login:
            passw = input("Password > ")
            if passw == "*exit":
                leave()
                exit()

            if passw == SYSData[1]:
                login = not login
                clear()
            else:
                print("Wrong Password!")

        print("███████████████████████████████████████████████████████████████████████████████████████")
        print("████░░░  \__    __/                                                             ░░░████")
        print("██░░░    /_/ /\ \_\        ____      _     _  ____                      _         ░░░██")
        print("██░░    __ \ \/ / __      / ___|___ | | __| |/ ___|___  _ __  ___  ___ | | ___     ░░██")
        print("██░     \_\_\/\/_/_/     | |   / _ \| |/ _` | |   / _ \| '_ \/ __|/ _ \| |/ _ \     ░██")
        print("██░ __/\___\_\/_/___/\__ | |__| (_) | | (_| | |__| (_) | | | \__ \ (_) | |  __/     ░██")
        print("██░   \/ __/_/\_\__ \/    \____\___/|_|\__,_|\____\___/|_| |_|___/\___/|_|\___| (c) ░██")
        print("██░     /_/ /\/\ \_\      Developed by CreepiYT                                     ░██")
        print("██░░     __/ /\ \__                                                                ░░██")
        print("██░░░    \_\ \/ /_/                                                               ░░░██")
        print("████░░░   /      \                                                              ░░░████")
        print("███████████████████████████████████████████████████████████████████████████████████████")
        print("██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Welcome {}!".format(SYSData[0]),end="")
        print(("░"*(42-len(SYSData[0]))+"██"))
        print("███████████████████████████████████████████████████████████████████████████████████████")

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

# make a Disk
def createdisk(i):
    if not i.replace(" ", "") == "":
        if not i in drives:
            drives.append(i)
        with open(i + ".VD", "w") as f:
            f.write("{'diskinfo.tmp':''}")
            f.close()

# systeminfo
def sysinfo():
    print("Processor: " + platform.processor()[0:36].replace("64","").replace("32",""))
    print("Processor Type: " + platform.processor()[5:7] + "x")

# remove file from Disk
def DEL():
    i = get_arg_value("-d")

    if i in drives:
        i += ".VD"
        j = get_arg_value("-f")

        with open(i, "r") as f:
            exec ("ddata=" + f.read(), globals())
            f.close()

        del ddata[j]

        with open(i, "w") as f:
            f.write(str(ddata))
            f.close()
    else:
        print("Disk" + i + " not found!")

# change Username
def CUN():
    i = args[0]
    if not i == "":
        SYSData[0] = i
        with open(SYSdrive, "w") as f:
            f.write(str(SYSData) + ";" + str(drives))
            f.close()
    else:
        print(i + " is not a valid username.")

def writedoc():
    clear()
    print("█████████████████████████")
    print("██ Write *exit to exit ██")
    print("█████████████████████████")

    text = ""
    textin = True
    line = 1

    while(textin):
        texttmp = input(str(line)+" | ");
        if (texttmp == "*exit"):
            textin = False
        else:
            if not line == 1:
                text += "\n"
            line += 1
            text += texttmp

    clear()
    filenamevalid = False

    while (filenamevalid == False):
        filenametmp = input("Enter file name: ")
        if (len(filenametmp) > 0):
            filenamevalid = True
            drivenamevalid = False
            drivenametmp = ""
            while (drivenamevalid == False and drivenametmp != "*exit"):
                drivenametmp = input("Enter drive name: ")
                if drivenametmp in drives:
                    i = drivenametmp + ".VD"
                    j = filenametmp

                    data = text

                    with open(i, "r") as f:
                        exec ("ddata=" + f.read(), globals())
                        f.close()

                    ddata[j] = data

                    with open(i, "w") as f:
                        f.write(str(ddata))
                        f.close()
                    clear()
                    print("Your document has been saved!")
                    drivenamevalid = True
                else:
                    print("This drive does not exist")

# save Sysdrive
def leave():
    with open(SYSdrive, "w") as f:
        f.write(str(SYSData) + ";drives=" + str(drives))
        f.close()

def commandparser(cmd):
    args.clear()

    if not cmd == "":
        # get the different part of the commands by splitting it on every space char
        cmdParts = cmd.split()
        # the actual command is the first entity in the array
        command = cmdParts[0]

        # make sure that the actually command is not taken as an argument
        index = 0

        for part in cmdParts:
            index += 1
            if index == 1:
                continue
            else:
                args.append(part)

        for Key in commands.keys():
            if command == Key:
                exec (commands[Key])
                return True
                break
        else:
            print("Can't find command: " + command)


def man():
    command = args[0]
    command = command.replace(" ", "")
    if not command == "":
        for Key in manuals.keys():
            if command == Key:
                print(manuals[Key])
                return True
                break
        else:
            print("Can't find command: " + command)


# returns the value of the given key-arg.
def get_arg_value(key):
    key_passed = False
    for arg in args:
        if key_passed:
            return arg
        elif arg == key:
            key_passed = True


Boot()
