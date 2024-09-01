import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

with open('requirements.txt') as f:
    required = f.read().splitlines()

for package in required:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", package.split('==')[0]])
    except subprocess.CalledProcessError:
        print(f"Installing missing package: {package}")
        install(package)

print("All requirements are installed.")