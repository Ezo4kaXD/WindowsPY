import os
import pyfiglet
import time

from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system("cls")

def print_green(text):
    print(Fore.GREEN + text + Fore.RESET)

def print_red_bold(text):
    print(Fore.RED + Style.BRIGHT + text + Fore.RESET + Style.RESET_ALL)

def clear():
    os.system("cls")

def pause():
    os.system("pause >nul")


art = pyfiglet.figlet_format("Cosnole")
print_red_bold(art)

helping = """
    dir - список файлов.
    cd - Открыть деректорию.
    created - создать свой file.py или с любым другим расширением.
    clear - очистка экрана.
    cmd - Обчная CMD.
"""
print(helping)

command = input("Python:")
if command == "dir":
    path = input("Path:")
    os.system(f"dir {path}")
    coomand = input("Python:")


if command == "created":
    directory = input("Путь к директории: ")
    file_name = input("Имя файла: ")
    file_extension = input("Расширение файла: ")
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    full_file_name = os.path.join(directory, f"{file_name}.{file_extension}")
    
    with open(full_file_name, 'w') as f:
        f.write("")  
    
    print_green(f"{full_file_name} Успешно создан!")
    command = input("Python:")

if command == "clear":
    os.system("cls")
    print_red_bold(art)
    print(helping)
    command = input("Python:")

if command == "cmd":
    os.system("cls")
    os.system("title C:/Windows/system32/cmd.exe")
    os.system("cmd.exe")