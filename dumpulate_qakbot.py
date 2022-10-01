#Dumpulator Script To Extract Encrypted Qakbot Strings
#Author: Matthew Brennan @HuntressLabs
#Twitter: @embee_research

#Note that this script assumes you have a valid MiniDump file...
#   obtained from an unpacked Qakbot Dump


from dumpulator import Dumpulator


#Load MiniDump file saved from x32dbg
#Quiet mode to avoid info about loading
dp = Dumpulator("qakbot.dmp", quiet=True)


result = ""

#Iterate through primary encrypted string block
#Try decreasing this value if you run into issues
for i in range(0xa8f):
    #use a try/except so that values can be bruteforced and errors ignored
    try:
        #store last result, used to avoid repeats
        last = result
        #set registers to argument defaults
        #change .ecx to 0x1001e0b0 for second set of strings
        dp.regs.ecx = 0x1001e5e8 
        dp.regs.edx = 0x0000104e
        #Change esp+0x4 to 0x1001e050 for second set of strings
        dp.write_ptr(dp.regs.esp+0x4,0x1001f638) #or 0x1001e050
        dp.write_ptr(dp.regs.esp+0x8,0xffffffff)

        #Set last register to index of encrypted string
        #This is the part that changes with each call to the function
        #essentially brute forcing this value
        dp.write_ptr(dp.regs.esp+0xc,i)
        #Call the decryption function, stop at the ret
        dp.start(0x10008c4a,end=0x10008D2D)
        #Read the value of EAX at the end of the decryption function
        result = dp.read_str(dp.regs.eax,'utf-16')
        #if not a a repeat, print to screen
        if result not in last:
            print(result)
    #Catch and ignore errors
    except:
        continue

