import os
import platform
import time
import subprocess
from colors import Colors

current_user = os.getlogin()
system_type = platform.system()
base_color = Colors.GREEN

print(f'{Colors.GREEN}Welcome!{Colors.RESET}')
print(f'{Colors.GREEN}Type "help" to see all commands.{Colors.RESET}')

try:
    while True:
        current_directory = os.getcwd()
        command_input = input(f'{base_color}{current_user.lower()}@{system_type.lower()}: {current_directory}> {Colors.RESET}')
        command_parts = command_input.split()
        command = command_parts[0] if command_parts else ''

        if command == 'exit':
            print(f'{Colors.RED}Exiting...{Colors.RESET}')
            time.sleep(0.5)
            break
        elif command == 'time':
            print(f'Current Unix timestamp: {Colors.CYAN}{time.ctime()} {Colors.RESET}')
        elif command == 'help':
            print(f'{Colors.GREEN}\nexit - quit the shell\ntime - print the current Unix timestamp\ncd <path> - change directory\nclear - clear the screen\nls - list files in the current directory\nmkdir <dir> - create a new directory\nrmdir <dir> - remove a directory\nmkf <file> - create a new file\nrmf <file> - remove a file\ncat <file> - display file content\nrun <file> - execute a file\nnano <file> - open a file in nano text editor\n{Colors.RESET}')
        elif command == 'ls':
            files = os.listdir()
            print(f'\nFiles in the current directory:\n{Colors.CYAN}', '\n'.join(files), f'\n{Colors.RESET}')
        elif command == 'clear':
            subprocess.run('clear', shell=True)
        elif command == 'cd':
            if len(command_parts) < 2:
                print('Please specify a path.')
            else:
                path = ' '.join(command_parts[1:])
                try:
                    os.chdir(path)
                    print(f'Changed directory to: {os.getcwd()}')
                except OSError as e:
                    print(e)
        elif command == 'mkdir':
            if len(command_parts) < 2:
                print('Please specify a directory name.')
            else:
                dir_name = ' '.join(command_parts[1:])
                try:
                    os.mkdir(dir_name)
                    print(f'Directory created: {dir_name}')
                except OSError as e:
                    print(e)
        elif command == 'rmdir':
            if len(command_parts) < 2:
                print('Please specify a directory name.')
            else:
                dir_name = ' '.join(command_parts[1:])
                try:
                    os.rmdir(dir_name)
                    print(f'Directory removed: {dir_name}')
                except OSError as e:
                    print(e)
        elif command == 'mkf':
            if len(command_parts) < 2:
                print('Please specify a file name.')
            else:
                file_name = ' '.join(command_parts[1:])
                try:
                    with open(file_name, 'w') as f:
                        pass
                    print(f'File created: {file_name}')
                except OSError as e:
                    print(e)
        elif command == 'rmf':
            if len(command_parts) < 2:
                print('Please specify a file name.')
            else:
                file_name = ' '.join(command_parts[1:])
                try:
                    os.remove(file_name)
                    print(f'File removed: {file_name}')
                except OSError as e:
                    print(e)
        elif command == 'cat':
            if len(command_parts) < 2:
                print('Please specify a file name.')
            else:
                file_name = ' '.join(command_parts[1:])
                try:
                    with open(file_name, 'r') as f:
                        print(f.read())
                except OSError as e:
                    print(e)
        elif command == 'run':
            if len(command_parts) < 2:
                print('Please specify a file to run.')
            else:
                file_name = ' '.join(command_parts[1:])
                try:
                    subprocess.run(f'start {file_name}', check=True)
                except subprocess.CalledProcessError as e:
                    print(f'Error running file: {e}')
                except FileNotFoundError:
                    print(f'File not found: {file_name}')
        elif command == 'nano':
            if len(command_parts) < 2:
                print('Please specify a file to edit.')
            else:
                file_name = ' '.join(command_parts[1:])
                subprocess.run(['nano', file_name])
        elif command == 'ch_color':
            color = input('Select color - Green, Red, Yellow, Blue, Magenta, Cyan, White\n')
            if color == 'Green':
                base_color = Colors.GREEN
            elif color == 'Red':
                base_color = Colors.RED
            elif color == 'Yellow':
                base_color = Colors.YELLOW
            elif color == 'Blue':
                base_color = Colors.BLUE
            elif color == 'Magenta':
                base_color = Colors.MAGENTA
            elif color == 'Cyan':
                base_color = Colors.CYAN
            elif color == 'White':
                base_color = Colors.WHITE
            else:
                print('Unknown color')
        else:
            print(f'Unknown command: {command}')
except KeyboardInterrupt:
    print(f'{Colors.RED}\nExiting...{Colors.RESET}')
    time.sleep(0.5)