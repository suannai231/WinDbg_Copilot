README for WinDbg Copilot

WinDbg Copilot is a ChatGPT powered AI assistant integrated with WinDbg. It analyzes the output of the commands, and provides guidance to solve the stated problem.

# Prerequisites

        1. Operating System: Windows 10 and above.
        2. If you want to use OpenAI API, add environmet variable:
                OPENAI_API_KEY = <Openai API Key>
        3. If you want to use Azure OpenAI, add following environment variables:
                AZURE_OPENAI_ENDPOINT = <Azure OpenAI Endpoint>
                AZURE_OPENAI_KEY = <Azure OpenAI Key>
                AZURE_OPENAI_DEPLOYMENT = <Azure OpenAI Deployment Name>
        4. The Debugging Tools for Windows WinDbg (classic) installed on your machine, download url: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools
           For example: C:\Program Files\Debugging Tools for Windows (x64)
           Add environment variable WinDbg_PATH = C:\Program Files\Debugging Tools for Windows (x64).
           Add environment variable _NT_SYMBOL_PATH = srv*c:\symbols*https://msdl.microsoft.com/download/symbols
        5. Python version >=3.9, <3.12 installed on your machine.
        6. An Internet connection for downloading and installing the package.

## Installation:

1. First, you need to ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/windows/) if you haven't already.

2. Open the Command Prompt or PowerShell.

3. Install the package using `pip`:
    ```
    pip install WinDbg_Copilot
    ```

## Running the Console and GUI versions:

Users can run the console or GUI version as follows:

### Running the Console App:

Simply type in the Command Prompt or PowerShell:
```
windbg-copilot-console
```

### Running the GUI App:

Type in the Command Prompt or PowerShell:
```
windbg-copilot-gui
```

## Running using Python (as per your latest preference):

If users want to run the apps directly using Python:

### Running the Console App:

```
python -m WinDbg_Copilot.WinDbg_Copilot_Console
```

### Running the GUI App:

```
python -m WinDbg_Copilot.WinDbg_Copilot_GUI
```

Remember: The latter approach requires users to be in a directory containing the `WinDbg_Copilot` package directory, or to have the appropriate Python paths set up. If they installed the package via `pip`, the paths should be set up automatically.

## Choosing between Console and GUI:

# WinDbg Copilot Console App Usage

Hello, I am WinDbg Copilot, I'm here to assist you.

The given commands are used to interact with WinDbg Copilot, a tool that utilizes the OpenAI model for assistance with debugging. The commands include:

        !auto: auto mode, user provides a problem description, ChatGPT can reply with simple explanations or suggesting a single command to execute to further analyze the problem. Ask user to execute the suggested command or not.
        !chat: chat mode, user inputs are forwarded to ChatGPT, ChatGPT can reply with simple answers or suggesting a single command to execute to further analyze the problem.
        !command: command mode, user inputs are forwarded to debugger like manual debugging in WinDbg, debugger outputs are forwarded to ChatGPT, ChatGPT can reply with simple explanations or suggesting a single command to execute to further analyze the problem. User will decide to execute the suggested command or not.
        !quit or !q or q or qq: Terminates the debugger session.
        !help or !h: Provides help information.

Note: WinDbg Copilot requires an active Internet connection to function properly, as it relies on Openai API.

# WinDbg Copilot GUI App

Welcome to the WinDbg Copilot GUI App - your go-to solution for an enhanced debugging experience powered by AI!

## Overview

The WinDbg Copilot GUI App seamlessly blends the power of WinDbg with the intelligence of OpenAI, providing you with intelligent suggestions throughout your debugging session. With configurable settings, support for various file types, and an integrated AI assistant, this app takes debugging to a whole new level.

## Features

1. **Configurable Settings Menu:** Tailor the app to your needs through a user-friendly settings menu.
2. **File Support:** Open local memory dump files or time travel trace files directly within the app.
3. **Remote Debugger Connection:** Need to debug remotely? Connect effortlessly to a remote debugger from within the app.
4. **Integrated WinDbg Command Window:** 
   - Positioned on the left side of the app.
   - View debugger outputs conveniently in a dedicated text widget.
   - Enter your debug commands in an entry widget located just below the display.
5. **AI-Powered Assistant:** 
   - Located on the right side of the app.
   - Input your problem description and send it to OpenAI for smart debugging suggestions.
   - The AI assistant's suggestions are not just textual; they're actionable! Receive clickable command links, and with a simple click, execute them in the debugger.
   - Enjoy a conversational debugging flow. As debugger outputs are returned, they are processed by OpenAI for further suggestions, creating an interactive loop to assist you until resolution.

## How It Works

1. Begin by entering a problem description in the AI assistant window.
2. Send this description to OpenAI via the app.
3. Receive a suggested debug command from OpenAI, presented as a clickable link.
4. Click on the suggestion to execute it in the WinDbg command window.
5. View the debugger output and await further suggestions from the AI assistant.
6. Continue this interactive process until you receive no more suggestions or until your problem is resolved.

# Uninstallation

        Open a command prompt or terminal window.
        Use pip to uninstall the WinDbg Copilot package:

                pip uninstall WinDbg_Copilot

        The packages will be uninstalled automatically.

## Conclusion

Gone are the days of sifting through endless logs and documentation. With the WinDbg Copilot GUI App, you have a powerful AI sidekick to guide you through the debugging process, making it more intuitive, interactive, and efficient. Happy debugging!

# Disclaimer: WinDbg Copilot

WinDbg Copilot is an application designed for debugging learning purposes only. It is important to note that this application should not be used to load or handle any customer data. WinDbg Copilot is intended solely for the purpose of providing a platform for debugging practice and learning experiences.

When using WinDbg Copilot, please be aware that any debugging input and output generated during your debugging sessions will be sent to OpenAI or Azure OpenAI according to your selection. This data may be used for analysis and improvement of the application's performance and capabilities. However, it is crucial to understand that no customer data should be loaded or shared through WinDbg Copilot.

WinDbg Copilot project takes the privacy and security of user information seriously and endeavors to handle all data with utmost care and in accordance with applicable laws and regulations. Nevertheless, it is strongly recommended to refrain from providing any sensitive or confidential information while using WinDbg Copilot.

By using WinDbg Copilot, you acknowledge and agree that any debugging input and output you generate may be transmitted to OpenAI or Azure OpenAI for research and development purposes. You also understand that WinDbg Copilot should not be used with customer data and that WinDbg Copilot project is not responsible for any consequences that may arise from the misuse or mishandling of such data.

Please ensure that you exercise caution and adhere to best practices when utilizing WinDbg Copilot to ensure the privacy and security of your own data. WinDbg Copilot project will not be held liable for any damages, losses, or unauthorized access resulting from the misuse of this application.

By proceeding to use WinDbg Copilot, you signify your understanding and acceptance of these terms and conditions.