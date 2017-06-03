import os, sys, time, socket, commands, threading, random

home           = os.getcwd()
host           = socket.gethostname()


class bcolors:
    HEADER     = '\033[95m'
    OKBLUE     = '\033[94m'
    OKGREEN    = '\033[92m'
    WARNING    = '\033[93m'
    FAIL       = '\033[91m'
    ENDC       = '\033[0m'
    BOLD       = '\033[1m'
    UNDERLINE  = '\033[4m'

class printouts:
    mainoutput = bcolors.OKGREEN+"["+bcolors.FAIL+"Abaddon"+bcolors.OKGREEN+"]?:>> "
    useroutput = bcolors.OKGREEN+"["+bcolors.FAIL+str(host)+bcolors.OKGREEN+"]?:>> "
    helpme     = """

      ____________________________________
  |  /    ______________________________  \  *  
 -0- :   |  .__           .__           | :     
  |  :   |  |  |__   ____ |  | ______   | : .  *
     :   |  |  |  \_/ __ \|  | \____ \  | :  .  
   . :   |  |   Y  \  ___/|  |_|  |_> > | :    |
* .  :   |  |___|  /\___  >____/   __/  | :   -0-    
     :   |       \/     \/     |__|     | : *  |
 |   :   -------------------------------  :       
-0-  \_  ______________________________  _/ .    
 |    | /~~~~~~~~~~~~Commands~~~~~~~~~~\ |
      |:________________________________:|    *      
   .  |: help           - Displays This :|
      |:                  Help SCreen   :|
      |:                                :|
 .    |: clear          - Clears Screen :|
      |:                                :|
      |: exit           - Exits Program :|
      |:                                :|
      |: adv            - Handles Mult- :|
      |:                  iple Commands :|
      |:                  In One Line   :|
      |:                                :|

    """
    

Banner         = bcolors.FAIL + """
        ##         /                     ##        ##
     /####       #/                       ##        ##
    /  ###       ##                       ##        ##
       /##       ##                       ##        ##
      /  ##      ##                       ##        ##
      /  ##      ## /###     /###     ### ##    ### ##    /###   ###  /###
     /    ##     ##/ ###  / / ###  / ######### ######### / ###  / ###/ #### /
     /    ##     ##   ###/ /   ###/ ##   #### ##   #### /   ###/   ##   ###/
    /      ##    ##    ## ##    ##  ##    ##  ##    ## ##    ##    ##    ##
    /########    ##    ## ##    ##  ##    ##  ##    ## ##    ##    ##    ##
   /        ##   ##    ## ##    ##  ##    ##  ##    ## ##    ##    ##    ##
   #        ##   ##    ## ##    ##  ##    ##  ##    ## ##    ##    ##    ##
  /####      ##  ##    /# ##    /#  ##    /#  ##    /# ##    ##    ##    ##
 /   ####    ## / ####/    ####/ ##  ####/     ####/    ######     ###   ###
/     ##      #/   ###      ###   ##  ###       ###      ####       ###   ###
#
 ##
"""

class MainFunctions:

    global Banner

    hm                = os.getcwd()

    PO                = printouts()  # Setting Class printouts As Global
    BC                = bcolors()    # Setting Class bcolors   As Global

    globalinformation = {}           # Creating List For Storing Information

    def _Startup(self):              # Defining StartUp Function


        cdir = os.getcwd()           # Setting Current Directory
        cspt = cdir.split('/')       # Splitting Directory By '/'

        clen = len(cspt)             # Grabbing Length Of Created List

        ckln = clen-1                # Taking Length - 1 For Current Home Dir Variable
        cstr = cspt[ckln]            # Setting Home String

        pchk = ckln-1                # Grabbing Parent Directory String
        pstr = cspt[pchk]            # Setting Parent String To Variable

        config   = open('CONFIG.txt').read().splitlines() # Grabbing Varibles From CONFIG.txt

        ifaceset = config[0]          # Setting Iface String From config
        ifacespt = ifaceset.split('=')# Splitting ifaceset By '='

        iface    = ifacespt[1]        # Grabbing iface Name

        proxcset = config[1]          # Setting Proxychains Value
        proxcspt = proxcset.split('=')# Splitting proxcset By '='

        proxych  = proxcspt[1]        # Grabbing proxych Variable

        autupset = config[2]          # Setting AutoUpdate Value
        autupspt = autupset.split('=')# Splitting autupset By '='

        autoup   = autupspt[1]        # Grabbing autoup Variable

        assetspathset = os.path.exists('Assets') # Checking For Assets  Child Dir
        buildspathset = os.path.exists('Build')  # Checking For Build   Child Dir
        systempathset = os.path.exists('System') # Checking For Systems Child Dir

        self.globalinformation['home']        = cstr    # Creating Home   Key Value In GI
        self.globalinformation['parent']      = pstr    # Creating Parent Key Value In GI
        self.globalinformation['iface']       = iface   # Creating Iface  Key Value In GI
        self.globalinformation['proxychains'] = proxych # Creating PC     Key Value In GI
        self.globalinformation['autoupdate']  = autoup  # Creating AU     Key Value In GI
        self.globalinformation['dircheckval'] = [assetspathset, buildspathset, systempathset]  # Creating Path Key Value In GI

        return

    def _commandhubPrintOut(self):

        print self.BC.OKGREEN + """
..:::                      CopyRight @ TopKekInc                           :::..
---------------------------------------------------------------------------------
        Home Directory:""" + self.BC.FAIL +self.globalinformation['home'] + self.BC.OKGREEN +"""            Parent Directory:""" + self.BC.FAIL + self.globalinformation['parent'] + self.BC.OKGREEN +"""
        Iface         :""" + self.BC.FAIL +self.globalinformation['iface'] + self.BC.OKGREEN +"""              Proxychains4    :""" + self.BC.FAIL + self.globalinformation['proxychains'] + self.BC.OKGREEN + """
        Autoupdate    :""" + self.BC.FAIL +self.globalinformation['autoupdate'] + self.BC.OKGREEN +"""
---------------------------------------------------------------------------------
**:::  """+ self.BC.HEADER + """Created By The Hive"""+self.BC.OKGREEN+"""           |                        """+self.BC.HEADER+"""For The Hive"""+self.BC.OKGREEN+"""  **:::
---------------------------------------------------------------------------------
        """
        return

    def _CallEntryHandle(self, ui):

        uisplit     = ui.split(' ')                         # Splitting Userinput Into uisplit

        assettocall = uisplit[1]                            # Grabbing Asset To Call

        os.chdir('Assets')

        cmd         = 'ls'                                  # Grabbing List Of Assets

        op          = commands.getoutput(cmd)               # Running Through System For Output

        opsplit     = op.split('/')                         # Splitting Into List By '/'

        if assettocall in opsplit:                          # Checking If The Asset Exists
            print self.PO.mainoutput + "Running: " + str(assettocall)
            import assettocall                              # Importing called asset 
            assettocall.Run()                               # Attempting To Call The Run Part Of The Module
            return
        else:
            print self.PO.mainoutput + "Operation Failed Due To Inability To Find Asset"
            return

    def _AdvEntryHandle(self, ui):

        entrylist   = []                                     # For Storage And Return

        elen        = len(entrylist)                         # Checking Length Of entrylist

        if elen > 0:
            del entrylist
            entrylist = []

        usergendict = {}                                     # For User Generated Keys
    
        openarglist = ['s', 'l', 'h', 'q']                   # Open Arg List 
        opendiction = {'tie':0001,                           # Tie Entry Key 0001 - IE: If operation == 'tie' set entry list from 'tie' to 0001 
                       'gen':0010,                           # Gen Entry Key 0010 - IE: If operation == 'gen' set entry list from 'gen' to 0010
                       'com':0100,                           # Com Entry Key 0100 - IE: If operation == 'com' set entry list from 'com' to 0100
                       'cll':1000                            # Cll Entry Key 1000 - IE: If operation == 'cll' set entry list from 'cll' to 1000
                      }
        uisplit     = ui.split(' ')                          # Splits String Into List For Handling

        del uisplit[0]                                       # Deleting adv Out Of List

        openfun     = uisplit[0]                             # Setting Opening Function

        if str(openfun) == str('tie'):                       # If OpeningFunction == 'tie' Append 0001 To entrylist
            entrylist.append('0001')                           # Appending
            secondaryvar = uisplit[1]                        # Function To Tie
            tievar       = uisplit[2]                        # Function To Tie To
            entrylist.append(secondaryvar)                   # Appending 
            entrylist.append(tievar)                         # Appending
        elif str(openfun) == str('gen'):                     # If OpeningFunction == 'gen' Append 0010 To entrylist
            entrylist.append('0010')                         # Appending
            secondaryvar = uisplit[1]                        # Function To Gen From
            genvar       = uisplit[2]                        # Intiger  Range 
            entrylist.append(secondaryvar)                   # Appending 
            entrylist.append(genvar)                         # Appending

        print entrylist

        return 

def commandhub():

    ae       = False                       # Setting ae AS False

    exitlist = ['exit', 'abort', 'quit']   # Possible Exit  Variables To Test On UI
    adventry = ['adv', 'Adv', 'AVD']       # Possible Advanced Option Splits First Character As Opening And Grabs Secondary String As Operation 
    cleentry = ['cls', 'clear', 'clean']   # Possible Clear Variables To Test On UI
    helentry = ['help', '-?', '-h']        # Possible Help  Variables To Test On UI
    calentry = ['call', 'cll']             # Possible Call  Variables To Test On UI
    lisentry = ['list', 'lst']             # Possible List  Variables To Test On UI

    MF = MainFunctions()
    PO = printouts()

    userinput = raw_input(PO.useroutput)

    if userinput in exitlist:
        print PO.mainoutput + " {*} Exiting... "                                                                     # Exit Entry Check
        sys.exit(1)

    elif userinput in cleentry:                                                                                      # Clear Entry Check 
        beforecommandhub()

    elif userinput in helentry:
        print PO.helpme
        commandhub()

    elif userinput in adventry:
        MF._AdvEntryHandle(userinput)
        commandhub()

    else:                                                                                                            # Failed Entry Check
        uisplit = userinput.split(' ')
        uiopen  = uisplit[0]

        if str(uiopen) in adventry:
            MF._AdvEntryHandle(userinput)
            commandhub()
        elif str(uiopen) in calentry:
            MF._CallEntryHandle(userinput)
            commandhub()
        elif str(uiopen) in lisentry:
            MF._ListEntryHandle(userinput)
            commandhub()
        
        print PO.mainoutput + "Operation Failed Due To Invalid Entry: " + bcolors.WARNING + str(userinput)
        commandhub()

def beforecommandhub():

    MF = MainFunctions()

    os.system("clear")

    print Banner
    MF._commandhubPrintOut()
    commandhub()

def startup():

    os.system("clear")
    MF = MainFunctions()

    MF._Startup()

    beforecommandhub()

startup()
