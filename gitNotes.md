Git common commands
1. "git init"							|||for initialization git repositories (it would create 'master' branch automatically)
2. "git add filename"						|||for adding file into git repository, if you don't do this, git won't do anyting version control
3. "git commit -m somethingORfilename" 				|||would commit filename in git repository
4. "git show master:filename" 					|||it would show the git repository Over command line screen
5. "git ls-files" 						|||it would show all the files that is in the git repository
6. "git rm file.txt" --> "git commit -m 'remove file.txt'"    		|||this would remove file on repository only
7. "git rm --cached file.txt" --> "git commit -m 'remove file.txt'"   		|||this would remove from both repository and filesystem
8. "git log -p filename"
9. "gitk [filename]   						|||This command would show the log in gui??
10. "git show HEAD"  						|||to get just the diff for a specific commit.
11. "git branch branchName" 					|||Create branch
12. "git checkout branchName" 					|||switch branch
13. "git status"
14. "git remote add origin remoteGitRepot_url
15. "git push -u origin master"   
16. "git push -u -f origin master" if you want to forcely change git repository
17. "git config --global user.email "you@example.com" 		|||before you can actually commit something you have to add your name and email to the git configuration.   the <config> file is on the route: "c:\Users\<username>\.gitconfig"  the global config can be used without setting config user.name and user.email everytime.
18. "git config --global user.name "your name"			||| same as 17. you should add your name to the configuration to make the commit know who you are.
19. "git config --local user.email "you@example.com"		|||pretty much the similar situation as 17. and 18. but you are add the config to the local and you have to set the config user.name and user.email everytimes you create repo.  the config file route: "git repo's .git folder"
20. "git ls-files"						|||Show the files that is managed by git.
21. "git merge branchName"    					||| First checkout to the master branch and then use merge then you can merge branch to the master.
22. "git clone git://github.com/cmcculloh/repo.git"     	||| clone remote repo to the local.  This would copy all the repo to the local, you should use this once, unless you want to many clones in your local or something.
23. "git remote add origin git://github.com/cmcculloh/repo.git"	||| set the remote repo
24. "git fetch -all"
25. "git pull origin master"					||| update local from remote repo.    You should definitely understand the difference between "clone", "fetch" and "pull", here's some reference you have to check it out:
 https://stackoverflow.com/questions/3620633/what-is-the-difference-between-pull-and-clone-in-git
https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch
26. "git reflog" 						||| this command would show the history that you modified before that can be checkout. very useful. Here's some reference: https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog 
27. "git remote set-url origin https://<githubtoken>@github.com/<username>/<repositoryname>.git"	||| when you want to push or pull something, github has already change their login method, you have to use token to login when you want to push or pull something. This command would make thing done. here's some reference: https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed-please-use-a-personal
28. "git clone https://<username>:<githubtoken>@github.com/<username>/<repositoryname>.git"		||| This one is for clone, pretty much similar as 27.
29. "git branch -m newBranchName" 				||| You can use this command to rename your current branch


