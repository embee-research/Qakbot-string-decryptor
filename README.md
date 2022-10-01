# Qakbot Dumpulate Script
A dumpulator script to extract encrypted strings from recent Qakbot malware. 

This is primarily a POC and example of a working script. 

You will likely need to modify it slightly (updating exact register values etc) to suit your sample. 

Notes:

- A valid minidump file is required, you can obtain this using Process Hacker or x32Dbg with MiniDump plugin. 
- Addresses and registers may change between samples, so you might need to modify these. 
- If you need to update registers, run your sample until the decryption function and note the registers in a debugger. 

