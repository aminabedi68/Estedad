import os
import sys

Dir = os.getcwd()
os.chdir(Dir)
print(Dir + str(sys.argv[1]))
file_to_delete = str(sys.argv[1])

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("🗑 File deleted successfully.")
else:
    print("❌ File not found for deletion.")



old_name = str(sys.argv[2])
new_name = str(sys.argv[3])

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("✅ File renamed successfully.")
else:
    print("❌ File not found for renaming.")
