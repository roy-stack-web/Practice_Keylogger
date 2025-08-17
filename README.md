# Practice Keylogger (Python)

This is my very first practice project in Python.  
I built a simple keylogger as part of learning **Python programming** and **cybersecurity basics**.  
It captures keystrokes with timestamps and writes them into a log file. The program can be stopped safely by pressing the `Esc` key.


## Why I made this
I am learning cybersecurity, and I wanted to understand how keyloggers work at a basic level.  
By making this project, I learned:
- How to use the `pynput` library
- How to capture and handle keyboard events
- How to write logs with timestamps
- How to safely exit a running listener


## Features
- Logs keystrokes with date and time
- Ignores unwanted keys (Shift, Ctrl, etc.)
- Adds a session header each time the program starts
- Safe exit when pressing `Esc`

## How to Run (Step by Step in PyCharm)
1. Clone or download the repository

If you have Git installed, run:
git clone https://github.com/roy-stack-web/Practice_Keylogger.git
** Or click the green Code → Download ZIP button on GitHub, then unzip it.

2. Open the project in PyCharm

Start PyCharm.

Click File -> Open… and select the folder Practice_Keylogger.
PyCharm will automatically detect the project and may create a virtual environment (.venv) for you.

3. Install the required library

Open the Terminal inside PyCharm (bottom panel).
Run: pip install pynput

4. Run the script

In the Project panel, right-click main.py.
Select Run 'main'.
The keylogger will now start running in the background.

5. Test the program

Open any window (like Notepad, browser, etc.) and type some keys.
Your keystrokes will be saved automatically into a file called log.txt in the project folder.

6. Stop the program

Simply press the Esc key.
The listener will stop, and logging will end for that session.

