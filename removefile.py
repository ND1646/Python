import os
if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("your file is removed successfully.......")
else:
    print("the file does not exists!!!!!")
    


import os
if os.path.exists("abc"):
    os.remove("abc")
    print("your folder is removed successfully.......")
else:
    print("the folder does not exists!!!!!")
    
