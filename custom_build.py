import os
import subprocess
import shutil
from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        # Change to vendor directory
        os.chdir('vendor')
        
        # Remove existing BBTools files
        for item in os.listdir('.'):
            if item.startswith('bb'):
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)
        
        # Download and extract BBTools
        subprocess.run(['wget', 'https://pilotfiber.dl.sourceforge.net/project/bbmap/BBMap_39.08.tar.gz', '-O', 'bbtools.tar.gz'], check=True)
        subprocess.run(['tar', '-xf', 'bbtools.tar.gz'], check=True)
        
        # Change back to root directory
        os.chdir('..')
        
        # Run the original install command
        install.run(self)
        
        # Generate commands
        subprocess.run(['generate-bbmapy-commands'], check=True)

setup(
    cmdclass={
        'install': CustomInstallCommand,
    },
)