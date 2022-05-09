# Libraries to execute command-line processes
import subprocess
import sys

# Class for package installation
class Installer:
    """
    Class used to install Python packages via ``pip`` in an easy and secure way.

    Parameters
    ----------
    package : str
        - Name of the package to install.
        
    root : bool
        - If needed, access to root user.
    
    Attributes
    ----------
    None

    Methods
    -------
        install(package='')
        - Installs a package via pip.
    """
    
    # Constructor
    def __init__(self, package:str = '', root:str = False) -> None:
        self.package = package
        self.root = root
        return

    # This function installs a package
    def install(self, package:str = '', root:str = False) -> None:
        """
        Installs Python packages via ``pip``.

        Parameters
        ----------
        package : str
            - Name of the package to install.
        root : bool
            - If needed, access to root user.
        """
        if package == '' and self.package == '':
            return None

        if package:
            self.package = package

        if root == True or self.root == True:
            subprocess.check_call([sys.executable, "-m", "pip", "install", self.package, '--user'])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", self.package])
        return