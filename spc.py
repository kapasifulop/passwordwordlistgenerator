import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_help():
	print(bcolors.WARNING + "----- Help for SPC -----")
	print(bcolors.OKCYAN + "  -ofile <output file name> set output file name")
	print(bcolors.OKCYAN + "  -output <true or false> show console generated passwords" )
	print(bcolors.WARNING + "      correct usage")
	print(bcolors.OKCYAN + "  python3 spc.py -ofile <output file name> -outuput <true or false>")
	print("")
	
def pw_gen_2_var(var1, var2):
    pws = [var1 + var2]
    pws.append(var1[0][0].upper() + var1[1:] + var2)
    pws.append(var1 + var2[0][0].upper() + var2[1:])
    pws.append(var1[0][0].upper() + var1[1:] + var2[0][0].upper() + var2[1:])
    return pws
	
def gen_pws(fm, bd, fmem, sname):
    pws = [fm + bd]
    pws.append(bd + fm)
    pws.append(fm[0][0].upper() + fm[1:] + bd)
    
    for pw in pw_gen_2_var(fm, sname):
        pws.append(pw)
    for pw in pw_gen_2_var(sname, fm):
        pws.append(pw)
        
    for pw in pw_gen_2_var(fm, sname):    
        pws.append(pw + bd)
        pws.append(bd + pw)
    for pw in pw_gen_2_var(sname, fm):    
        pws.append(pw + bd)
        pws.append(bd + pw)    
    
    for name in fmem:
        ## WITHOUT BIRTHDAY
        pws.append(fm + name)
        pws.append(name + fm)
        #FIRSTNAME UPPER
        pws.append(fm[0][0].upper() + fm[1:] + name)
        pws.append(name + fm[0][0].upper() + fm[1:])
        #"NAME" UPPER
        pws.append(fm + name[0][0].upper() + name[1:])
        pws.append(name[0][0].upper() + name[1:] + fm)
        #ALL UPPER
        pws.append(fm[0][0].upper() + fm[1:] + name[0][0].upper() + name[1:])
        pws.append(name[0][0].upper() + name[1:] + fm[0][0].upper() + fm[1:])
        ## WITH BIRTHDAY
        pws.append(fm + name + bd)
        pws.append(fm + bd + name)
        pws.append(bd + fm + name)
        pws.append(name + fm + bd)
        pws.append(bd + name + fm)
        pws.append(name + bd + fm)
        #FIRSTNAME UPPER
        pws.append(fm[0][0].upper() + fm[1:] + name + bd)
        pws.append(fm[0][0].upper() + fm[1:] + bd + name)
        pws.append(bd + fm[0][0].upper() + fm[1:] + name)
        pws.append(name + fm[0][0].upper() + fm[1:] + bd)
        pws.append(bd + name + fm[0][0].upper() + fm[1:])
        pws.append(name + bd + fm[0][0].upper() + fm[1:])
        #"NAME" UPPER
        pws.append(fm + name[0][0].upper() + name[1:] + bd)
        pws.append(fm + bd + name[0][0].upper() + name[1:])
        pws.append(bd + fm + name[0][0].upper() + name[1:])
        pws.append(name[0][0].upper() + name[1:] + fm + bd)
        pws.append(bd + name[0][0].upper() + name[1:] + fm)
        pws.append(name[0][0].upper() + name[1:] + bd + fm)
        #ALL UPPER
        pws.append(fm[0][0].upper() + fm[1:] + name[0][0].upper() + name[1:] + bd)
        pws.append(fm[0][0].upper() + fm[1:] + bd + name[0][0].upper() + name[1:])
        pws.append(bd + fm[0][0].upper() + fm[1:] + name[0][0].upper() + name[1:])
        pws.append(name[0][0].upper() + name[1:] + fm[0][0].upper() + fm[1:] + bd)
        pws.append(bd + name[0][0].upper() + name[1:] + fm[0][0].upper() + fm[1:])
        pws.append(name[0][0].upper() + name[1:] + bd + fm[0][0].upper() + fm[1:])
    return pws
	
def generate_passwords(fname, bd, fmem, sname, output, o_file):
    f = open(o_file, "w")
    pws = gen_pws(fname, bd, fmem, sname)
    length = len(pws)
    for pw in pws:
        if(output == "true"):
            print(pw)
        else:
            print(bcolors.OKBLUE + str(round((pws.index(pw) + 1) / (length / 100))) + "%")
        f.write(pw + "\n")
    f.close()
    print(bcolors.OKCYAN + "File has been created!")
    
	
if len(sys.argv) < 5 or len(sys.argv) > 5 or sys.argv[1] == "--help":
    print_help()
elif(sys.argv[1] == "-ofile" and sys.argv[3] == "-output" and (sys.argv[4] == "true" or sys.argv[4] == "false")):
    print(bcolors.OKCYAN + "Is woman or man?(woman/man)" + bcolors.OKBLUE)
    wm = input().lower()
    sh = "he"
    hihe = "her"
    if(wm == "woman" or wm == "w"):
        sh = "she"
        hihe = "her"
    elif(wm == "man" or wm == "m"):
        sh = "he"
        hihe = "her"
    else:
        print(bcolors.FAIL + "FAIL: The input could not be interpreted, so I use \"man\"!")
        print(" -_- ")
        print("")
    print(bcolors.OKCYAN + "What is " + hihe + " surname?" + bcolors.OKBLUE) 
    sirname = input().lower()
    print(bcolors.OKCYAN +"What is " + hihe + " first name?" + bcolors.OKBLUE)
    firstname = input().lower()
    print(bcolors.OKCYAN + "When " + sh + " was born(YYYY)?" + bcolors.OKBLUE)
    birthday = input().lower()
    print(bcolors.OKCYAN + "A member first name of her family:" + bcolors.OKBLUE)
    family_member = [input().lower()]
    print(bcolors.OKCYAN + "Do you want to enter more name? Y/N" + bcolors.OKBLUE)
    y_n = input().lower()
    if(y_n == "y"):
        print(bcolors.OKCYAN + "Enter the name" + bcolors.OKBLUE)
        family_member.append(input().lower())
    print(bcolors.OKCYAN + "Creating file!")
    generate_passwords(firstname, birthday, family_member, sirname, sys.argv[4], sys.argv[2])
else:
    print_help()

