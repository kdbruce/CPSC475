# Small Eliza simulationimport reimport sysdef doreply(instr):    instr = instr.lower()    if re.search(r'^hello|hi$', instr):        return 'Hi there!'    if re.search(r'\W(hate|despise|loathe)\W', instr):        return 'Wow! Those are some strong feelings you have! Tell me more...'    if re.search(r"^(are|aren't|what|where|who|when|is|isn't|why|how)\W", instr):        return 'good question!'    return "So, tell me something about your mother."def main():    print "Welcome! How may I help you? (type \"bye\" to quit.)\n"    while True:        # Read user's input        instr = raw_input("Patient: ")        instr = instr.lower()        if re.search(r'\bbye\b', instr):            print "Nice chatting with you!\n"            return 0        print doreply(instr)        print'''The folowing is considered good practice in a program that is intended to be runas a module.  It prevents the program from being run as an import into anotherprogramTry creating a program tst.py with the single line: import ex11You'll see that this program will not run.Now remove the first line, below, and move main() to the right margin. Now runtst.py.  This program will run.try printing the variable __name__it's value is set to __main__ when the program is called directly but to ex11when it is imported'''print __name__if __name__ == "__main__":    sys.exit(main())