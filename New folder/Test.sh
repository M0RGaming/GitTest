#!/bin/sh
function pause(){
   read -p "$*"
}
echo "Hello world"
pause 'Press [Enter] to stop acceleration'
echo ------------------
echo What would you like to do?
read OP
echo "You entered in [$OP]"

if [ $OP = "end" ]; then
    echo "Have a good day"
elif [ $OP = "pull" ]; then
    git fetch origin
    git pull
elif [ $OP = "push" ]; then
    echo ---------------
    echo Create a summary for your commit
    read SUM
    git add *
    git commit -m "$SUM"
    git push -u origin master
elif [ $OP = "create" ]; then
    echo ---------------
    echo Go to github.com and create an account
    echo Create a new repo called whatever you want
    echo It will bring up a page that has something called
    echo Quick Setup near the top. Copy that link and paste it here
    read RepoLoc
    echo Enter the path to your Repo Location
    echo You can also enter * to choose the current directory
    read PATH
    if [ $PATH = "*" ]; then
	git init
    else
	cd $PATH
	git init
    fi
    echo "# Reeborg-Code" >> README.md
    git add README.md
    git commit -m "first commit"
    git remote add origin $RepoLoc
    git push -u origin master
else
    echo "Invalid command"
    echo "Valid Commands are: create, push, pull"
    break;

fi

exit 0
