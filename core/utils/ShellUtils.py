import subprocess


def executeScript(command_list):
    sub_cmd = subprocess.run(command_list, shell=True, capture_output=True)
    return sub_cmd.returncode, sub_cmd.stdout


def sudoTest(sudo_pass):
    err, user = executeScript("echo '%s' | sudo -S whoami" % sudo_pass)
    if str(user, "utf8").strip() == 'root':
        return True
    return False
