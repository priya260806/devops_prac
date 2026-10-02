Practical: Git Repository Management

Aim

Create a Git repository, initialize it, and add a Python project.


Software Required

• Git for Windows (already installed)
• Visual Studio Code
• Python (installed)
• GitHub account (optional for Part A)


Folder Structure

You will create this folder:

Git_Practical
│
├── hello.py
├── README.md
└── .git


Step 1: Open Visual Studio Code

1. Click Start Menu.
2. Search for Visual Studio Code.
3. Open it.


Step 2: Open the Terminal

In VS Code,

Click

Terminal
↓
New Terminal

A terminal opens at the bottom.

It looks like:

PS C:\Users\YourName>

(PS means PowerShell.)


Step 3: Go to Desktop

Type:

cd Desktop

Press Enter.

Now you are inside the Desktop folder.

Example:

PS C:\Users\Nikhita\Desktop>


Step 4: Create a Folder

Type:

mkdir Git_Practical

Press Enter.

Nothing will happen on the screen.

It simply creates the folder.


Step 5: Move into the Folder

Type:

cd Git_Practical

Press Enter.

Now terminal becomes:

PS C:\Users\Nikhita\Desktop\Git_Practical>


Step 6: Open this Folder in VS Code

Type:

code .

Press Enter.

The folder opens inside VS Code.

You should now see:

Git_Practical

on the left Explorer.


Step 7: Create Python File

Click:

New File

Name it:

hello.py


Step 8: Write Python Program

Inside hello.py:

print("Hello Git!")

Save:

Ctrl + S


Step 9: Create README File

Again click:

New File

Name it:

README.md

Write:

# Git Practical
This is my first Git repository.
Project Name: Python Demo
Created by: Your Name

Save it.


Step 10: Check Folder

Your folder now contains:

Git_Practical
hello.py
README.md


Step 11: Initialize Git Repository

Go to Terminal.

Type:

git init

Press Enter.

Output:

Initialized empty Git repository in
C:/Users/Nikhita/Desktop/Git_Practical/.git/

Now Git creates a hidden folder:

.git

This folder stores all version history.


Step 12: Check Git Status

Type:

git status

Output:

On branch master
No commits yet
Untracked files:
hello.py
README.md

Meaning:

Git has found two files.

But they are not being tracked.


Step 13: Add Files

To add all files:

git add .

Press Enter.

OR

Add only one file:

git add hello.py


Step 14: Check Status Again

Type:

git status

Output:

Changes to be committed:
new file: hello.py
new file: README.md

Now Git is ready to save these files.


Step 15: Configure Git (First Time Only)

If this is your first Git project, configure your identity.

Type:

git config --global user.name "Your Name"

Example:

git config --global user.name "Nikhita"

Press Enter.

Now email:

git config --global user.email "your@email.com"

Example:

git config --global user.email "nikhita@gmail.com"

Press Enter.


Step 16: Commit the Project

Now save the project permanently.

Type:

git commit -m "Initial Python Project"

Press Enter.

Example output:

[master (root-commit) abc1234]
2 files changed
create mode 100644 hello.py
create mode 100644 README.md

Congratulations!

Your first Git commit is complete.


Step 17: Check Status

Type:

git status

Output:

On branch master
nothing to commit, working tree clean

This means:

• All changes are saved.
• Repository is up to date.
• There are no pending changes.


Step 18: View Commit History

Type:

git log

Output:

commit a12bc34d56...
Author: Nikhita
Date: ...
Initial Python Project

This shows the commit history.


Step 19: Modify the Python File

Open:

hello.py

Change it to:

print("Hello Git!")
print("Welcome to Git Repository")

Save the file.


Step 20: Check Status

Type:

git status

Output:

modified: hello.py

Git detects that the file has changed.


Step 21: Save the Changes

Stage the modified file:

git add hello.py

Commit the changes:

git commit -m "Updated hello.py"


Step 22: View All Commits

Type:

git log

Now you'll see two commits:

Updated hello.py
Initial Python Project


Final Folder Structure

Git_Practical
│
├── .git
├── hello.py
└── README.md