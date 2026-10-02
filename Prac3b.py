Practical B: Demonstrate Branching and
Merging Using Pull Requests


Prerequisites

Before starting, make sure you have:

• Git installed
• VS Code installed
• GitHub account
• Completed Part (a)
• Your project (Git_Practical) already committed


Current Project Structure

Git_Practical
│
├── hello.py
├── README.md
└── .git


Step 1: Open Your Project

Open VS Code.

Go to:

File → Open Folder → Git_Practical

Open the terminal:

Terminal → New Terminal


Step 2: Check the Current Branch

Type:

git branch

Output:

* master

or

* main

If your repository shows master, use master in the commands below instead of main.


Step 3: Rename master to main (Optional)

Modern repositories use main.

If your branch is master, type:

git branch -M main

Check again:

git branch

Output:

* main


Step 4: Create a New Feature Branch

Create a branch called feature-login:

git checkout -b feature-login

Output:

Switched to a new branch 'feature-login'


Step 5: Verify the Branch

git branch

Output:

* feature-login
  main

The * indicates the current branch.


Step 6: Modify the Python File

Open:

hello.py

Current code:

print("Hello Git!")
print("Welcome to Git Repository")

Add new lines:

print("Hello Git!")
print("Welcome to Git Repository")
print("Login Feature Added")
print("Feature Branch Example")

Save the file (Ctrl + S).


Step 7: Check Status

git status

Output:

modified: hello.py


Step 8: Stage the Changes

git add hello.py


Step 9: Commit the Changes

git commit -m "Added login feature"

Example output:

[feature-login abc123]
1 file changed


Step 10: View Commit History

git log --oneline

Example:

7b8c91 Added login feature
2a3bc4 Updated hello.py
1f23de Initial Python Project


Step 11: Create a Repository on GitHub

1. Open GitHub.
2. Click New Repository.
3. Repository name:

Git_Practical

4. Keep it Public.
5. Do not add a README (you already have one).
6. Click Create Repository.


Step 12: Connect Local Repository to GitHub

Copy your GitHub repository URL, for example:

https://github.com/yourusername/Git_Practical.git

Run:

git remote add origin https://github.com/yourusername/Git_Practical.git

Verify:

git remote -v

Output:

origin  https://github.com/yourusername/Git_Practical.git


Step 13: Push the Main Branch

Switch to the main branch:

git checkout main

Push it:

git push -u origin main


Step 14: Push the Feature Branch

Switch back:

git checkout feature-login

Push:

git push -u origin feature-login

Output:

Branch 'feature-login' set up to track remote branch.


Step 15: Create a Pull Request

Go to GitHub.

You will see:

Compare & Pull Request

Click it.


Step 16: Fill Pull Request Details

Title:

Added Login Feature

Description:

This pull request adds a login feature to the Python project.

Click:

Create Pull Request


Step 17: Merge the Pull Request

Click:

Merge Pull Request

Then:

Confirm Merge

GitHub will display:

Pull Request Successfully Merged


Step 18: Switch Back to Main

In VS Code:

git checkout main


Step 19: Pull the Latest Changes

git pull origin main

Output:

Updating...
Fast-forward


Step 20: Verify the Merge

Open:

hello.py

You should see:

print("Hello Git!")
print("Welcome to Git Repository")
print("Login Feature Added")
print("Feature Branch Example")

The feature branch changes are now in the main branch.


Step 21: View Branches

git branch

Output:

  feature-login
* main


Step 22: Delete the Feature Branch

(Optional)

Delete the local branch:

git branch -d feature-login

Delete the remote branch:

git push origin --delete feature-login


Workflow Diagram

main
│
│
├───────────────┐
│               │
│          feature-login
│               │
│        Add new Python code
│               │
│        Commit changes
│               │
│        Push to GitHub
│               │
│        Create Pull Request
│               │
└──────── Merge into main
                │
             git pull
                │
          Updated main