import os

# SHORTENED SIGNATURES (More reliable)
signatures = {
    "rbx_luau_load": b"\xFD\x7B\x02\xA9\xFD\x83\x00\x91", 
    "rbx_lua_pcall": b"\xFD\x7B\x03\xA9\xFD\x03\x00\x91",
    "rbx_lua_gettop": b"\xFD\x7B\x01\xA9\xF4\x4F\x02\xA9",
}

def scan():
    # Make sure the file in your GitHub is named EXACTLY "Roblox"
    binary_path = "Roblox" 
    
    if not os.path.exists(binary_path):
        print(f"Error: {binary_path} not found!")
        return

    with open(binary_path, "rb") as f:
        data = f.read()
        print(f"Scanning binary (Size: {len(data)} bytes)...")
        
        with open("offsets.h", "w") as out:
            out.write("// Auto-generated offsets\n")
            for name, sig in signatures.items():
                # find() looks for the first occurrence of these bytes
                offset = data.find(sig)
                if offset != -1:
                    out.write(f"#define {name}_offset 0x{offset:X}\n")
                    print(f"✅ Found {name} at 0x{offset:X}")
                else:
                    out.write(f"#define {name}_offset 0x0 // NOT FOUND\n")
                    print(f"❌ Could not find {name}")

if __name__ == "__main__":
    scan()
