import os

# Update these hex signatures to match the ones you found
signatures = {
    "rbx_luau_load": b"\xFD\x7B\x02\xA9\xFD\x83\x00\x91\x68\x2C\x00\xD0\x08\x75\x43\xF9",
    "rbx_lua_pcall": b"\xFD\x7B\x03\xA9\xFD\x03\x00\x91", 
    "rbx_lua_gettop": b"\xFD\x7B\x01\xA9\xF4\x4F\x02\xA9\xFD\x03\x00\x91",
}

def scan():
    # This looks for the 'Roblox' file in your repo's root folder
    binary_path = "Roblox" 
    
    if not os.path.exists(binary_path):
        print(f"Error: {binary_path} not found in repo!")
        return

    with open(binary_path, "rb") as f:
        data = f.read()
        with open("offsets.h", "w") as out:
            out.write("// Auto-generated offsets\n")
            for name, sig in signatures.items():
                offset = data.find(sig)
                if offset != -1:
                    # Subtract 0x100000000 if your IDA offsets look like 0x1000E3B0
                    out.write(f"#define {name}_offset 0x{offset:X}\n")
                    print(f"Found {name} at 0x{offset:X}")
                else:
                    out.write(f"#define {name}_offset 0x0 // NOT FOUND\n")

if __name__ == "__main__":
    scan()
