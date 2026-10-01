# open vs code
# open terminal 
cd Desktop
mkdir Git_Practical
cd Git_Practical
# open folder in vs code
# hello.py
print("Hello git!")

# README.md
# Git Practical
This is my first Git repository.
Project Name: Python Demo
Created by: Priya

# open terminal
git init  # initialize git repository
git status # check status
git add . # add all files
git add hello.py # add 1 file
git status # check again now it will be commited

# Configure Git # for 1st time only
git config --global user.name "Priya"              
git config --global user.email "priyathadhani26@gmail.com"

git commit -m "Initial Python Project"  # commit project
git status  # everything clear
git log # commit history

now modify the hello.py file
add: print("Welcome to git repository")
git status 
git add hello.py
git commit -m "Updated hello.py"
git log
