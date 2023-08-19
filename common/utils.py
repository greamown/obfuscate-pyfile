import os, subprocess, shutil

def cmd(command, split_action=True):
    if split_action:
        print(command.split())
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
        print("PID:{},".format(process.pid))
		
    else:
        print(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
        print("PID:{},".format(process.pid))

    for line in iter(process.stdout.readline,b''):  
        line = line.rstrip().decode('ascii',errors='ignore')
        if line.isspace(): 
            continue
        else:
            print(line)
            
def goal_path(main_path:str):
    status = False
    if os.path.isdir(main_path):
        # Copy folder
        if main_path[-1] == "/":
            main_path = main_path[:-1]
        split_path = os.path.split(main_path)
        dist = os.path.join(split_path[0], split_path[-1] + "_package")
        return status, dist
    return status, "Main path is wrong:[{}]".format(main_path)
        
def collect_pyfiles(dist:str):
    file_dict = {"filename":{}, "files":[]}
    for root, dirs, files in os.walk(dist):
        if "__pycache__" in root:
            shutil.rmtree(root)
        else:
            for f in files:
                fullpath = os.path.join(root, f)
                if ".py" in fullpath:
                    file_dict["filename"][f] = root
                    file_dict["files"].append(fullpath)  
    return file_dict

def move_obf_file(dist:str, file_dict:dict, gen_path:str):
    for key, value in file_dict["filename"].items():
        file = os.path.join(value, key)
        dist_file = os.path.join(gen_path, key)
        os.remove(file)
        shutil.move(dist_file, file)
    # Move pyarmor_runtime_000000
    pyarmor_old_path = os.path.join(gen_path, "pyarmor_runtime_000000")
    pyarmor_new_path = os.path.join(dist, "pyarmor_runtime_000000")
    shutil.move(pyarmor_old_path, pyarmor_new_path)
    shutil.rmtree(gen_path)