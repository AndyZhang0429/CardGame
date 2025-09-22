import sys,os,subprocess

file_name = ""
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    raise Exception("No file name provided")

file = open(file_name, "r")
file_content = file.read()
file.close()

ClassName = os.path.splitext(os.path.basename(file_name))[0]

runScript = f'''
#include "{file_name}"

int main(int argc, char* argv[]){{
    {ClassName} obj;
    obj.main(argc, argv);
    return 0;
}}
'''

with open(".runscript.cpp", "w") as f:
    f.write(runScript)

os.system(f"g++ -std=c++17 .runscript.cpp -o {ClassName}")

os.system(f".\{ClassName}.exe")
os.remove(".runscript.cpp")
os.remove(f".\{ClassName}.exe")
