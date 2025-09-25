import sys,os,subprocess
import Project

root = Project.FindRoot("./")
route_file = ""
with open(os.path.join(root, 'routes.json'), "r") as route:
    route_file = route.read()

file_name = ""
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    raise Exception("No file name provided")

file = open(file_name, "r")
file_content = file.read()
file.close()

file_path = os.path.relpath(file_name, os.path.join(root, "build/"))

ClassName = os.path.splitext(os.path.basename(file_name))[0]

runScript = f'''
#include "{file_path}"

int main(int argc, char* argv[]){{
    {ClassName} obj;
    obj.main(argc, argv);
    return 0;
}}
'''
os.system("pause")
with open(os.path.join(root, "build/.runscript.cpp"), "w") as f:
    f.write(runScript)

os.system(f"cd {root}")
os.system("pause")
os.system(f"{Project.Route(route_file, 'g++')} -std=c++17 build/.runscript.cpp -o {ClassName}")
os.system("pause")

os.system(f".\{ClassName}.exe")

os.remove(os.path.join(root, ".build/runscript.cpp"))
os.remove(f".\{ClassName}.exe")