import sys, os, shutil
from argparse import ArgumentParser, SUPPRESS
from common import cmd, goal_path, collect_pyfiles, move_obf_file

def build_argparser():
    parser = ArgumentParser(add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h', '--help', action='help', default=SUPPRESS, help='Show this help message and exit.')
    args.add_argument('-p', '--path', required=True, help = "The path of encrypt folder")
    return parser

def main(args):
    gen_path = os.path.join(os.getcwd(), "dist")
    if os.path.isdir( args.path ):
        try:
            main_path = os.path.join(os.getcwd(), args.path)
            status, dist = goal_path(main_path)
            if status:
                print(dist)
                sys.exit(0)
            # Check fodler does exist?!
            if os.path.exists(dist):
                print("This folder does exist:[{}]".format(dist))
                while True:
                    status = input("Do you want to delete the old one and create a new one. y or n :")
                    if status == "y":
                        shutil.rmtree(dist)
                        break
                    elif status == "n":
                        sys.exit(0)
                    else:
                        continue
            # Copy project to new dist
            shutil.copytree(args.path, dist)
            # Collect all .py
            file_dict = collect_pyfiles(dist)
            # Generate obfuscate code
            files = " ".join(file_dict["files"])
            command = "pyarmor gen {}".format(files)
            cmd(command, split_action=True)
            # Remove all *.py file and move obfuscate file
            move_obf_file(dist, file_dict, gen_path)
            print("The path of obfuscate pyfiles:[{}]".format(dist))
        except Exception as e:
            print(e)
    else:
        print("This path is not a folder.")


if __name__ == '__main__':
    args = build_argparser().parse_args()
    sys.exit(main(args) or 0)