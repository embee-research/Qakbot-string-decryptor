# Qakbot Dumpulate Script
A dumpulator script to extract encrypted strings from recent Qakbot malware. 

This is primarily a POC and example of a working script. 

You will likely need to modify it slightly (updating exact register values etc) to suit your sample. 

Notes:

- A valid minidump file is required, you can obtain this using Process Hacker or x32Dbg with MiniDump plugin. 
- Addresses and registers may change between samples, so you might need to modify these. 
- If you need to update registers, run your sample until the decryption function and note the registers in a debugger. 

Steps to Recreate
- Obtain a qakbot Sample
- Unpack it, obtaining the second DLL
- Using Ghidra/IDA, identify the string decryption function
- Load the unpacked DLL into x32/x64dbg, and break on the decryption function. 
- Take note of the registers and arguments (ecx/edx etc)
- Use the MiniDump plugin to create a minidump file. 
- Point this script to your minidump file. 
- Run the script, updating any register values to those observed in x32/64dbg. 


Example of string decryption Function. 
![image](https://user-images.githubusercontent.com/82847168/193444418-74b2eee7-562d-435d-921b-aa9d784ef926.png)

Example of another function within that function. I found it easier to point my script here. 
![image](https://user-images.githubusercontent.com/82847168/193444438-e3f4e3c8-098d-4b0e-819d-2826654569d2.png)

Example of x32dbg at point of MiniDump. 
![image](https://user-images.githubusercontent.com/82847168/193444448-f86fcbd6-5896-4398-8de4-173eba93ea41.png)

Example of Script with some extra notes. 
![image](https://user-images.githubusercontent.com/82847168/193444458-f608fd1f-e927-4908-bcbd-7c9a447cc015.png)

