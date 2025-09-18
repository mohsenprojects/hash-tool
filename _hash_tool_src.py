import sys
import hashlib
import os


    
def calculate_hash(input_data, hash_type, is_file=False):
    hash_type = hash_type.lower()
    hash_obj = None
    
    
    if hash_type == "md5":
        hash_obj = hashlib.md5()
    elif hash_type == "sha1":
        hash_obj = hashlib.sha1()
    elif hash_type == "sha224":
        hash_obj = hashlib.sha224()
    elif hash_type == "sha256":
        hash_obj = hashlib.sha256()
    elif hash_type == "sha384":
        hash_obj = hashlib.sha384()
    elif hash_type == "sha512":
        hash_obj = hashlib.sha512()
    elif hash_type == "sha3_224":
        hash_obj = hashlib.sha3_224()
    elif hash_type == "sha3_256":
        hash_obj = hashlib.sha3_256()
    elif hash_type == "sha3_384":
        hash_obj = hashlib.sha3_384()
    elif hash_type == "sha3_512":
        hash_obj = hashlib.sha3_512()
    elif hash_type == "blake2b":
        hash_obj = hashlib.blake2b()
    elif hash_type == "blake2s":
        hash_obj = hashlib.blake2s()
    else:
        raise ValueError(f"Unsupported hash type: {hash_type}")

    if is_file:
        
        if not os.path.isfile(input_data):
            raise FileNotFoundError(f"File not found: {input_data}")
        
        with open(input_data, 'rb') as f:
            while chunk := f.read(8192):  
                hash_obj.update(chunk)
    else:
       
        hash_obj.update(input_data.encode())

    return hash_obj.hexdigest()

if __name__ == "__main__":
    
    with open('hash_debug.txt', 'w') as f:
        f.write(f"Received args: {sys.argv}\n")
    
    
    if getattr(sys, 'frozen', False):
        
        args = sys.argv[1:] if len(sys.argv) > 1 else []
    else:
        
        args = sys.argv[1:]
    
    if len(args) < 3:
        print("Usage:")
        print("  For strings: hash_tool.exe -s <string> <hash_type> [-v expected_hash]")
        print("  For files:   hash_tool.exe -f <file_path> <hash_type> [-v expected_hash]")
        print("\nPress Enter to exit...")
        input()
        sys.exit(1)

    mode = args[0]
    input_data = args[1]
    hash_type = args[2]

    try:
        if mode == "-s":
            result = calculate_hash(input_data, hash_type, is_file=False)
            print(f"{hash_type.upper()} of string: {result}")
        elif mode == "-f":
            result = calculate_hash(input_data, hash_type, is_file=True)
            print(f"{hash_type.upper()} of file: {result}")
        else:
            raise ValueError("Invalid mode. Use -s for string or -f for file")

        if len(args) >= 5 and args[3] == "-v":
            if result == args[4]:
                print("Verification: SUCCESS")
            else:
                print("Verification: FAILED")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        input("Press Enter to exit...")
        sys.exit(1)