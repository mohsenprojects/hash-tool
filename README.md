# hash-tool
a tool for use hash algorithms
# commands:
-v for verify\n
-s for hash of string
-f for hash of file
For strings: python _hash_tool_src.py -s <string> <hash_type> [-v expected_hash]
For files:   python _hash_tool_src.py -f <file_path> <hash_type> [-v expected_hash]

# example:

python _hash_tool_src.py -s "hello world" sha256
output : SHA256 of string: b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9

python _hash_tool_src.py -s "hello world" sha256 -v b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
output : Verification: SUCCESS
