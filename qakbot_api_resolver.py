"""
Qakbot - Offline API Hash Resolving Script
@embee_research @HuntressLabs

"""

import pefile,sys,os

"""
Hashes are xor'd with a key after calcuation
This value does change between samples
and may need to be updated

The value can typically be found after a call to the hash calculation
See the readme for an example of this

#[0x137ef56a,0x343e9b56] - Common Values, Try these first
"""
#UPDATE THIS VALUE
#xor_value = 0x137ef56a 
xor_value = 0x218fe95b
DAT = b'\x00\x00\x00\x00\x64\x10\xb7\x1d\xc8\x20\x6e\x3b\xac\x30\xd9\x26\x90\x41\xdc\x76\xf4\x51\x6b\x6b\x58\x61\xb2\x4d\x3c\x71\x05\x50\x20\x83\xb8\xed\x44\x93\x0f\xf0\xe8\xa3\xd6\xd6\x8c\xb3\x61\xcb\xb0\xc2\x64\x9b\xd4\xd2\xd3\x86\x78\xe2\x0a\xa0\x1c\xf2\xbd\xbd\x25\x75\x00\x00\x3a\x00\x00\x00\x3a\x2f\x2f\x00\x20\x00\x00\x00\x66\x75\x6c\x6c\x00\x00\x00\x00\x5c\x00\x00\x00\x20\x00\x00\x00\x2c\x00\x00\x00\x3d\x00\x00\x00\x62\x00\x00\x00\x7c\x00\x00\x00\x25\x75\x3b\x25\x75\x3b\x25\x75\x00\x00\x00\x00\x25\x75\x2e\x25\x75\x2e\x25\x75\x2e\x25\x75\x3a\x25\x75\x00\x00\x70\x25\x30\x38\x78\x00\x00\x00\x25\x75\x3b\x25\x75\x3b\x25\x75\x3b\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x22\x00\x00\x00\x68\x0d\xff\xdd\x81\xa6\x3f\x25\xb6\xd9\xda\x78\x2f\x85\x54\xd4\x00\x00\x00\x00\x62\x00\x61\x00\x74\x00\x00\x00\x53\x00\x79\x00\x73\x00\x74\x00\x65\x00\x6d\x00\x44\x00\x72\x00\x69\x00\x76\x00\x65\x00\x00\x00\x55\x00\x53\x00\x45\x00\x52\x00\x50\x00\x52\x00\x4f\x00\x46\x00\x49\x00\x4c\x00\x45\x00\x00\x00\x5c\x00\x00\x00\x47\x6c\x6f\x62\x61\x6c\x00\x00\x00\x00\x00\x00\xd6\x54\x4e\x1e\x87\xe1\x9a\xea\xd4\xca\xe7\xfb\xa4\xf6\xf3\xe8\x2b\x8c\x09\x90\x2d\x51\x7c\xe0\x5b\xf5\x06\x19\x09\xf1\x1e\xd7\x75\x7e\xd7\x6e\x10\xb8\xa8\xfe\x78\xc9\xc7\x4a\x1e\x52\xd7\xc1\xaf\xfc\x1c\x91\xd0\x1e\x87\x1f\x1c\x85\x0a\x7d\x19\x47\x48\xd6\xfe\x18\xf3\x07\x9b\x3c\x01\x23\x17\xe9\x18\xa0\xe4\x8e\xe4\x9d\x07\x36\x28\xc7\x16\x6b\xa1\xc7\x11\xe4\x41\x28\x86\x1c\xdc\xec\xa4\x6f\xdb\x99\xa6\xc5\x38\xea\x54\xeb\x2b\x81\x11\xae\xa2\xf4\x50\xdd\xdf\x0f\xeb\xef\xe5\xb1\x72\x00\x60\x80\x23\xb5\xb4\x74\xc1\x1f\xa4\xf9\x16\x40\x3b\xe5\x2f\x03\x48\xce\x49\xbf\x66\xed\x8b\xea\xd3\x28\x08\xcd\x23\xf8\x84\x6f\x60\x06\x21\x82\x8f\x1f\x70\x37\x5b\xeb\x79\x13\x96\xe2\x74\x41\x70\xb3\x53\x06\xf0\x70\x96\xe4\xe1\x73\x9a\x50\x11\x45\x6f\x09\x74\xfc\xfc\x98\xd8\x6f\xf3\x04\x7d\xef\x3c\xdf\xe3\x0b\xed\x25\xab\x33\x3c\x3c\x74\xea\xa2\xa5\x95\x1b\x27\x33\xe7\x4f\x47\x20\xb2\xdd\x33\x21\x7f\x40\x21\xad\x15\xa3\x7b\xd4\x3b\x3a\x97\x7e\x9f\x04\x02\x8f\xdc\xfa\x59\x78\x57\x78\x3e\xa8\x74\x86\x74\x86\x89\x31\x48\xed\x97\x7c\xdc\xe4\x2c\xca\x4b\x65\x0f\xde\xdd\xa8\xf2\xfb\xe2\x57\xfd\x19\xd6\x56\xcf\x8a\x3a\xbe\xf9\xb0\xc1\x37\xc0\x44\x93\x80\xc2\xd4\xd3\xf4\xe5\xd9\x3e\xcb\x98\x0c\xaa\xab\xe4\xdd\xff\xf3\x09\xf1\x95\x9b\x9a\x83\xa6\xba\x45\x3d\x00\x00\x00\x00\x2f\xb0\x5b\x80\x7f\x55\x9e\x8e\xee\xe1\xea\x95\xdb\xa2\x61\xbf\xad\xd6\xc7\xb1\xe7\xd7\x99\x85\x62\x70\x08\xc5\xcc\xf3\xa2\x7d\x0b\x2e\x86\x2c\x70\x04\x14\x70\x00\x00\x00\x00\xd5\xb4\xa2\x76\x50\x89\xd5\x62\xf2\x70\x8e\x18\x8e\x73\x58\x13\x18\x37\x1d\xab\x20\x9e\x13\x6a\x56\xc0\xaa\x5f\x1f\xfb\x7b\xa0\x4f\x27\x56\x7c\x15\xcf\x2b\x80\x18\xcf\xb8\xe8\x38\xe5\xd0\xe9\xa0\xad\x18\x17\x6f\x38\x99\x5e\x7a\xce\x3d\xf2\xf9\xa7\x49\x24\x8c\x78\x83\xca\xcd\x52\xe2\x15\x72\xb4\x2f\xe4\x23\x01\xfb\x10\x75\x19\xa5\xae\x00\x00\x00\x00\x2a\x5f\xc9\xa0\x92\xf3\x12\xc0\x1e\x02\xb9\xab\x46\x19\x90\xe7\xac\x04\x39\x33\xf3\xab\xe8\xfe\x00\x00\x00\x00\x00\x00\x00\x00\xae\x1e\x1f\xc4\x94\x0c\x6c\x2c\x46\x2e\xed\x69\x8d\x91\xbc\xe6\xe6\xc0\xe2\x10\x88\x93\xb5\xe0\xa5\x44\xb6\x91\x6e\xe8\xa6\x88\xe6\x1f\xf7\x39\xb7\xaa\x23\xcd\x9a\xd9\x6f\xac\xc2\x42\x82\x6e\xc8\x29\x3b\xc0\xb9\x94\x82\xe0\x58\xb2\x9c\x53\x17\x80\xdc\x0c\xee\x78\x3b\xa0\x01\xc4\x36\x08\x84\x26\xfa\x51\xfe\xc7\xcd\x89\xb7\x41\xb6\xfe\x4b\x68\x6c\xe7\x6b\xdb\x4c\xc6\x95\xd3\xcf\x89\xd8\xcc\x75\xcc\xbb\x28\xeb\x2b\x56\x4e\x98\x71\xb3\x18\xb8\x6a\x4e'


def calc_hash(name):
    size = len(name)
    key = 0
    out = ~key
    out = out & 0xffffffff
    #print(out)
    order = "little"
    ecx = 0
    #for c in name:
    while ecx < size:
        eax = ord(name[ecx])
        out = out ^ eax
        eax = out
        out = out >> 4
        out = out & 0xffffffff
        eax = eax & 0xf
        out = out ^ int.from_bytes(DAT[eax*4:eax*4+4],order) 
        eax = out
        out = out >> 4
        out = out & 0xffffffff
        eax = eax & 0xf
        out = out ^ int.from_bytes(DAT[eax*4:eax*4+4],order)
        ecx +=1
        
    out = ~out
    out = out & 0xffffffff
    
    out ^= xor_value
    #uncomment the "hex" to build a lookup of decimal values instead
    return hex(out)


#Parse the export list from a dll file
def get_export_list(path_to_file):
    pe = pefile.PE(path_to_file)
    d = [pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_EXPORT"]]
    pe.parse_data_directories(directories=d)
    exports = [(e.name) for e in pe.DIRECTORY_ENTRY_EXPORT.symbols]
    return exports

#Retrieve DLL's from current working directory
def get_cwd_dll():
    dll_list = []
    cwd = os.listdir()
    for filename in cwd:
        if ".dll" in filename:
            dll_list.append(filename)
    return dll_list

#Get a list of all exports from DLL's in CWD
def build_export_list(dll_list):
    #For each DLL, get the exports, build a master list
    export_master_list = []
    for file_name in dll_list:
        try:
            export_master_list += get_export_list(file_name)
        except:
            print("Failed to open {}".format(file_name))
            continue
    return export_master_list

def build_hash_dictionary(export_master_list):
    #resolve each export name and calculate hashes
    hash_dict = {}
    for export_name in export_master_list:
        if export_name:
            try:
                export_name = export_name.decode()
            except:
                export_name = export_name.decode('utf-16')
                continue
            h = calc_hash(export_name)
            hash_dict[export_name] = h
            hash_dict[h] = export_name
    return hash_dict

def lookup_hash(hash_dict, value):
    try:
        return hash_dict[value]
    except Exception as e:
        print(e)
        print("Unable to Find value {}".format(lookup))
        sys.exit(1)



def main():
    #Check that at least 1 argument has been provided
    try:
        lookup = sys.argv[1].lower()
    except:
        print("failed to parse args")
        sys.exit(1)
        
    #Enumerate DLL's from current directory
    print("Calculating hash values with XOR {}".format(hex(xor_value)))
    dll_list = get_cwd_dll()
    export_master_list = build_export_list(dll_list)
    hash_dict = build_hash_dictionary(export_master_list)
    #print(hash_dict)
    
    #perform the lookup
    try:
        print("{} : {}".format(lookup,lookup_hash(hash_dict,lookup)))
    except:
        print("Failed to Find value")
        sys.exit(1)
    
if __name__ == "__main__":
    main()






    



