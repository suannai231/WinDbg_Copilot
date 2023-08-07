# setup.py
from setuptools import setup

if __name__ == "__main__":
  setup(packages = ['WinDbg_Copilot'],
        entry_points={
        'console_scripts': [
            'windbg-copilot-console=WinDbg_Copilot.WinDbg_Copilot_Console:main',         # Assumes main() function in WinDbg_Copilot.py
            'windbg-copilot-gui=WinDbg_Copilot.WinDbg_Copilot_GUI:main', # Assumes main() function in WinDbg_Copilot_GUI.py
        ],
    },
    package_data={
        'WinDbg_Copilot': ['thumbnail.ico', 'config.ini'],
    })