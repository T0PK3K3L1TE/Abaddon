import os, sys, time

class MainFunctions:

    openfilelist = []
    openfilelen   = 0

    def OpenFileCheckAndSplit(self, inputfile):
        print "Checking " + str(inputfile) + " For Validity"
        checkfile = os.path.isfile(inputfile)
        if checkfile == True:
            print "Path " + str(inputfile)  + " Is Valid... Set As " + str(checkfile)
            print "Opening " + str(inputfile)
            inputcheck = open(str(inputfile)).read()
            print "Successfully Opened " + str(inputfile)
            inputstrip = inputcheck.split("\n")
            print "Successfully Split " + str(inputfile)
            self.openfilelist = inputstrip
            inputlen = len(inputstrip)
            self.openfilelen = inputlen
            print "Current Length Of file " + str(inputlen)
            return 

        else:
            print "Operation Failed Due To Invalid Entry " + str(inputfile)
            sys.exit(1)



def Main():
    
    MF = MainFunctions()
    filecheckdir = raw_input("Input File Home Directory: ")
    print "Checking " + str(filecheckdir)
    check = os.path.exists(str(filecheckdir))
    if check == True:
        os.chdir(str(filecheckdir))
        filetocheck  = raw_input("Input File               : ")
        MF.OpenFileCheckAndSplit(filetocheck)

    sys.exit(1)

if __name__ == "__main__":
    Main()

