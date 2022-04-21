# Libraries to execute command-line processes
import subprocess
import sys

# Class for package installation
class Installer:
    
    # Constructor
    def __init__(self, package = '', root = False):
        self.package = package
        self.root = root
        return

    # This function installs a package
    def install(self, package = '', root = False):
        if package == '' and self.package == '':
            return None

        self.package = package

        if root == True or self.root == True:
            subprocess.check_call([sys.executable, "-m", "pip", "install", self.package, '--user'])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", self.package])

        return