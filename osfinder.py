import subprocess
import platform


def FindOsver():

    cat = subprocess.Popen(['cat', '/etc/os-release'], stdout=subprocess.PIPE)
    grep = subprocess.Popen(
        ['grep', "REDHAT_SUPPORT_PRODUCT="], stdin=cat.stdout, stdout=subprocess.PIPE)
    is_fedora = True if "Fedora" in (grep.communicate()[0]).decode(
        "utf-8").split("=")[1] else False

    if is_fedora == False:
        raise ValueError("System is not Fedora. Quitting")
    else:
        cat = subprocess.Popen(
            ['cat', '/etc/os-release'], stdout=subprocess.PIPE)
        grep = subprocess.Popen(
            ['grep', "VERSION_ID"], stdin=cat.stdout, stdout=subprocess.PIPE)
        version = (grep.communicate()[0]).decode("utf-8").split("=")[1].strip()
        if version == 36:
            return "eln128"
        else:
            return f"fc{version}"


def FindArch():
    arch = subprocess.Popen(['uname', '-m'], stdout=subprocess.PIPE)
    return arch.stdout.read().strip().decode("utf-8")


print(FindArch())
