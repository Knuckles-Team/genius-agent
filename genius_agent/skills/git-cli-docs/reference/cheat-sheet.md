[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --everything-is-local
![](https://git-scm.com/images/dark-mode.svg)
  * [About](https://git-scm.com/about)
    * [Trademark](https://git-scm.com/about/trademark)
  * [Learn](https://git-scm.com/learn)
    * [Book](https://git-scm.com/book)
    * [Cheat Sheet](https://git-scm.com/cheat-sheet)
    * [Videos](https://git-scm.com/videos)
    * [External Links](https://git-scm.com/doc/ext)
  * [Tools](https://git-scm.com/tools)
    * [Command Line](https://git-scm.com/tools/command-line)
    * [GUIs](https://git-scm.com/tools/guis)
    * [Hosting](https://git-scm.com/tools/hosting)
  * [Reference](https://git-scm.com/docs)
  * [Install](https://git-scm.com/install/linux)
  * [Community](https://git-scm.com/community)


  * Table of Contents 
    * [Getting Started](https://git-scm.com/cheat-sheet#getting-started)
    * [Prepare to Commit](https://git-scm.com/cheat-sheet#prepare-to-commit)
    * [Make Commits](https://git-scm.com/cheat-sheet#make-commits)
    * [Move Between Branches](https://git-scm.com/cheat-sheet#move-between-branches)
    * [Diff Staged/Unstaged Changes](https://git-scm.com/cheat-sheet#diff-staged-unstaged-changes)
    * [Diff Commits](https://git-scm.com/cheat-sheet#diff-commits)
    * [Ways to refer to a commit](https://git-scm.com/cheat-sheet#ways-to-refer-to-a-commit)
    * [Discard Your Changes](https://git-scm.com/cheat-sheet#discard-your-changes)
    * [Edit History](https://git-scm.com/cheat-sheet#edit-history)
    * [Code Archaeology](https://git-scm.com/cheat-sheet#code-archaeology)
    * [Combine Diverged Branches](https://git-scm.com/cheat-sheet#combine-diverged-branches)
    * [Restore an Old File](https://git-scm.com/cheat-sheet#restore-an-old-file)
    * [Add a Remote](https://git-scm.com/cheat-sheet#add-a-remote)
    * [Push Your Changes](https://git-scm.com/cheat-sheet#push-your-changes)
    * [Pull Changes](https://git-scm.com/cheat-sheet#pull-changes)
    * [Configure Git](https://git-scm.com/cheat-sheet#configure-git)
    * [Important Files](https://git-scm.com/cheat-sheet#important-files)


* * *
The entire **[Pro Git book](https://git-scm.com/book)** written by Scott Chacon and Ben Straub is available to [read online for free](https://git-scm.com/book). Dead tree versions are available on [Amazon.com](https://www.amazon.com/Pro-Git-Scott-Chacon/dp/1484200772?ie=UTF8&camp=1789&creative=9325&creativeASIN=1430218339&linkCode=as2&tag=git-sfconservancy-20). 
[![](https://git-scm.com/images/pdf.png)](https://git-scm.com/cheat-sheet.pdf)
# Git Cheat Sheet
## Getting Started
### Start a new repo:
`git init`
### Clone an existing repo:
`git clone <url>`
## Prepare to Commit
### Add untracked file or unstaged changes:
`git add <file>`
### Add all untracked files and unstaged changes:
`git add .`
### Choose which parts of a file to stage:
`git add -p`
### Move file:
`git mv <old> <new>`
### Delete file:
`git rm <file>`
### Tell Git to forget about a file without deleting it:
`git rm --cached <file>`
### Unstage one file:
`git reset <file>`
### Unstage everything:
`git reset`
### Check what you added:
`git status`
## Make Commits
### Make a commit (and open text editor to write message):
`git commit`
### Make a commit:
`git commit -m 'message'`
### Commit all unstaged changes:
`git commit -am 'message'`
## Move Between Branches
### Switch branches:
`git switch <name>` OR `git checkout <name>`
### Create a branch:
`git switch -c <name>` OR `git checkout -b <name>`
### List branches:
`git branch`
### List branches by most recently committed to:
`git branch --sort=-committerdate`
### Delete a branch:
`git branch -d <name>`
### Force delete a branch:
`git branch -D <name>`
## Diff Staged/Unstaged Changes
### Diff all staged and unstaged changes:
`git diff HEAD`
### Diff just staged changes:
`git diff --staged`
### Diff just unstaged changes:
`git diff`
## Diff Commits
### Show diff between a commit and its parent:
`git show <commit>`
### Diff two commits:
`git diff <commit> <commit>`
### Diff one file since a commit:
`git diff <commit> <file>`
### Show a summary of a diff:
`git diff <commit> --stat` `git show <commit> --stat`
## Ways to refer to a commit
Every time we say `<commit>`, you can use any of these:  

a branch
    main 

a tag
    v0.1 

a commit ID
    3e887ab 

a remote branch
    origin/main 

current commit
    HEAD 

3 commits ago
    HEAD^^^ or HEAD~3
## Discard Your Changes
### Delete unstaged changes to one file:
`git restore <file>` OR `git checkout <file>`
### Delete all staged and unstaged changes to one file:
`git restore --staged --worktree <file>` OR `git checkout HEAD <file>`
### Delete all staged and unstaged changes:
`git reset --hard`
### Delete untracked files:
`git clean`
### 'Stash' all staged and unstaged changes:
`git stash`
## Edit History
### "Undo" the most recent commit (keep your working directory the same):
`git reset HEAD^`
### Squash the last 5 commits into one:
`git rebase -i HEAD~6`
Then change "pick" to "fixup" for any commit you want to combine with the previous one
### Undo a failed rebase:
`git reflog BRANCHNAME`
Then manually find the right commit ID in the reflog, then run:
`git reset --hard <commit>`
### Change a commit message (or add a file you forgot):
`git commit --amend`
## Code Archaeology
### Look at a branch's history:
`git log main` `git log --graph main` `git log --oneline`
### Show every commit that modified a file:
`git log <file>`
### Show every commit that modified a file, including before it was renamed:
`git log --follow <file>`
### Find every commit that added or removed some text:
`git log -G banana`
### Show who last changed each line of a file:
`git blame <file>`
## Combine Diverged Branches
### Combine with rebase:
`git switch banana` `git rebase main` Before: ![](https://git-scm.com/cheat-sheet) After: ![](https://git-scm.com/cheat-sheet)
### Combine with merge:
`git switch main` `git merge banana` Before: ![](https://git-scm.com/cheat-sheet) After: ![](https://git-scm.com/cheat-sheet)
### Combine with squash merge:
`git switch main` `git merge --squash banana` `git commit` Before: ![](https://git-scm.com/cheat-sheet) After: ![](https://git-scm.com/cheat-sheet)
### Bring a branch up to date with another branch (aka "fast-forward merge"):
`git switch main` `git merge banana` Before: ![](https://git-scm.com/cheat-sheet) After: ![](https://git-scm.com/cheat-sheet)
### Copy one commit onto the current branch:
`git cherry-pick <commit>` Before: ![](https://git-scm.com/cheat-sheet) After: ![](https://git-scm.com/cheat-sheet)
## Restore an Old File
### Get the version of a file from another commit:
`git checkout <commit> <file>` OR `git restore <file> --source <commit>`
## Add a Remote
`git remote add <name> <url>`
## Push Your Changes
### Push the `main` branch to the remote `origin`:
`git push origin main`
### Push the current branch to its remote "tracking branch":
`git push`
### Push a branch that you've never pushed before:
`git push -u origin <name>`
### Force push:
`git push --force-with-lease`
### Push tags:
`git push --tags`
## Pull Changes
### Fetch changes (but don't change any of your local branches):
`git fetch origin main`
### Fetch changes and then rebase your current branch:
`git pull --rebase`
### Fetch changes and then merge them into your current branch:
`git pull origin main` OR `git pull`
## Configure Git
### Set a config option:
`git config user.name 'Your Name'`
### Set option globally:
`git config --global ...`
### Add an alias:
`git config alias.st status`
### See all possible config options:
`man git-config`
## Important Files
### Local git config:
`.git/config`
### Global git config:
`~/.gitconfig`
### List of files to ignore:
`.gitignore`
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
