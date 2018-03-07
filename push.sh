echo "Pushing Source"
echo "Enter a summary/name for commit"
read NAME
git add *
git commit -m "$NAME"
git push origin master
echo "Pushing Finished"
echo "Press Enter to continue"
