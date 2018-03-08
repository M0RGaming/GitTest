echo "Creating a new Git Area"
echo ""
echo "Go to github.com, create an account, and create a new Repo"
echo "When you create the new repo, copy the https quick setup link"
echo "and paste it here"
read PATH

echo ""
echo "Initilizing repo"
echo "# This is a README file, enter all info you want into here" >> README.md
git init
git add README.md
git commit -m "Initial commit"
git remote add origin $PATH
git push -u origin master

echo ""
echo "Finished, press Enter to exit"
read PAUSE
