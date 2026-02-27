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
    * [NAME](https://git-scm.com/docs/git-clean#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-clean#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-clean#_description)
    * [OPTIONS](https://git-scm.com/docs/git-clean#_options)
    * [Interactive mode](https://git-scm.com/docs/git-clean#_interactive_mode)
    * [CONFIGURATION](https://git-scm.com/docs/git-clean#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-clean#_see_also)
    * [GIT](https://git-scm.com/docs/git-clean#_git)


[ English ▾](https://git-scm.com/docs/git-clean)
Localized versions of **git-clean** manual
  1. [English ](https://git-scm.com/docs/git-clean)
  2. [Français ](https://git-scm.com/docs/git-clean/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-clean/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-clean/sv)
  5. [українська мова ](https://git-scm.com/docs/git-clean/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-clean/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-clean)
### Setup and Config
  * [ git ](https://git-scm.com/docs/git)
  * [ config ](https://git-scm.com/docs/git-config)
  * [ help ](https://git-scm.com/docs/git-help)
  * [ bugreport ](https://git-scm.com/docs/git-bugreport)
  * [ Credential helpers ](https://git-scm.com/doc/credential-helpers)


### Getting and Creating Projects
  * [ init ](https://git-scm.com/docs/git-init)
  * [ clone ](https://git-scm.com/docs/git-clone)


### Basic Snapshotting
  * [ add ](https://git-scm.com/docs/git-add)
  * [ status ](https://git-scm.com/docs/git-status)
  * [ diff ](https://git-scm.com/docs/git-diff)
  * [ commit ](https://git-scm.com/docs/git-commit)
  * [ notes ](https://git-scm.com/docs/git-notes)
  * [ restore ](https://git-scm.com/docs/git-restore)
  * [ reset ](https://git-scm.com/docs/git-reset)
  * [ rm ](https://git-scm.com/docs/git-rm)
  * [ mv ](https://git-scm.com/docs/git-mv)


### Branching and Merging
  * [ branch ](https://git-scm.com/docs/git-branch)
  * [ checkout ](https://git-scm.com/docs/git-checkout)
  * [ switch ](https://git-scm.com/docs/git-switch)
  * [ merge ](https://git-scm.com/docs/git-merge)
  * [ mergetool ](https://git-scm.com/docs/git-mergetool)
  * [ log ](https://git-scm.com/docs/git-log)
  * [ stash ](https://git-scm.com/docs/git-stash)
  * [ tag ](https://git-scm.com/docs/git-tag)
  * [ worktree ](https://git-scm.com/docs/git-worktree)


### Sharing and Updating Projects
  * [ fetch ](https://git-scm.com/docs/git-fetch)
  * [ pull ](https://git-scm.com/docs/git-pull)
  * [ push ](https://git-scm.com/docs/git-push)
  * [ remote ](https://git-scm.com/docs/git-remote)
  * [ submodule ](https://git-scm.com/docs/git-submodule)


### Inspection and Comparison
  * [ show ](https://git-scm.com/docs/git-show)
  * [ log ](https://git-scm.com/docs/git-log)
  * [ diff ](https://git-scm.com/docs/git-diff)
  * [ difftool ](https://git-scm.com/docs/git-difftool)
  * [ range-diff ](https://git-scm.com/docs/git-range-diff)
  * [ shortlog ](https://git-scm.com/docs/git-shortlog)
  * [ describe ](https://git-scm.com/docs/git-describe)


### Patching
  * [ apply ](https://git-scm.com/docs/git-apply)
  * [ cherry-pick ](https://git-scm.com/docs/git-cherry-pick)
  * [ diff ](https://git-scm.com/docs/git-diff)
  * [ rebase ](https://git-scm.com/docs/git-rebase)
  * [ revert ](https://git-scm.com/docs/git-revert)


### Debugging
  * [ bisect ](https://git-scm.com/docs/git-bisect)
  * [ blame ](https://git-scm.com/docs/git-blame)
  * [ grep ](https://git-scm.com/docs/git-grep)


### Email
  * [ am ](https://git-scm.com/docs/git-am)
  * [ apply ](https://git-scm.com/docs/git-apply)
  * [ imap-send ](https://git-scm.com/docs/git-imap-send)
  * [ format-patch ](https://git-scm.com/docs/git-format-patch)
  * [ send-email ](https://git-scm.com/docs/git-send-email)
  * [ request-pull ](https://git-scm.com/docs/git-request-pull)


### External Systems
  * [ svn ](https://git-scm.com/docs/git-svn)
  * [ fast-import ](https://git-scm.com/docs/git-fast-import)


### Server Admin
  * [ daemon ](https://git-scm.com/docs/git-daemon)
  * [ update-server-info ](https://git-scm.com/docs/git-update-server-info)


### Guides
  * [ gitattributes ](https://git-scm.com/docs/gitattributes)
  * [ Command-line interface conventions ](https://git-scm.com/docs/gitcli)
  * [ Everyday Git ](https://git-scm.com/docs/giteveryday)
  * [ Frequently Asked Questions (FAQ) ](https://git-scm.com/docs/gitfaq)
  * [ Glossary ](https://git-scm.com/docs/gitglossary)
  * [ Hooks ](https://git-scm.com/docs/githooks)
  * [ gitignore ](https://git-scm.com/docs/gitignore)
  * [ gitmodules ](https://git-scm.com/docs/gitmodules)
  * [ Revisions ](https://git-scm.com/docs/gitrevisions)
  * [ Submodules ](https://git-scm.com/docs/gitsubmodules)
  * [ Tutorial ](https://git-scm.com/docs/gittutorial)
  * [ Workflows ](https://git-scm.com/docs/gitworkflows)
  * [ All guides... ](https://git-scm.com/docs/git#_guides)


### Administration
  * [ clean ](https://git-scm.com/docs/git-clean)
  * [ gc ](https://git-scm.com/docs/git-gc)
  * [ fsck ](https://git-scm.com/docs/git-fsck)
  * [ reflog ](https://git-scm.com/docs/git-reflog)
  * [ filter-branch ](https://git-scm.com/docs/git-filter-branch)
  * [ instaweb ](https://git-scm.com/docs/git-instaweb)
  * [ archive ](https://git-scm.com/docs/git-archive)
  * [ bundle ](https://git-scm.com/docs/git-bundle)


### Plumbing Commands
  * [ cat-file ](https://git-scm.com/docs/git-cat-file)
  * [ check-ignore ](https://git-scm.com/docs/git-check-ignore)
  * [ checkout-index ](https://git-scm.com/docs/git-checkout-index)
  * [ commit-tree ](https://git-scm.com/docs/git-commit-tree)
  * [ count-objects ](https://git-scm.com/docs/git-count-objects)
  * [ diff-index ](https://git-scm.com/docs/git-diff-index)
  * [ for-each-ref ](https://git-scm.com/docs/git-for-each-ref)
  * [ hash-object ](https://git-scm.com/docs/git-hash-object)
  * [ ls-files ](https://git-scm.com/docs/git-ls-files)
  * [ ls-tree ](https://git-scm.com/docs/git-ls-tree)
  * [ merge-base ](https://git-scm.com/docs/git-merge-base)
  * [ read-tree ](https://git-scm.com/docs/git-read-tree)
  * [ rev-list ](https://git-scm.com/docs/git-rev-list)
  * [ rev-parse ](https://git-scm.com/docs/git-rev-parse)
  * [ show-ref ](https://git-scm.com/docs/git-show-ref)
  * [ symbolic-ref ](https://git-scm.com/docs/git-symbolic-ref)
  * [ update-index ](https://git-scm.com/docs/git-update-index)
  * [ update-ref ](https://git-scm.com/docs/git-update-ref)
  * [ verify-pack ](https://git-scm.com/docs/git-verify-pack)
  * [ write-tree ](https://git-scm.com/docs/git-write-tree)


[ Latest version ▾ ](https://git-scm.com/docs/git-clean) git-clean last updated in 2.45.0
Changes in the **git-clean** manual
  1. 2.45.1 → 2.53.0 no changes
  2. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-clean/2.45.0)
  3. 2.43.1 → 2.44.4 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-clean/2.43.0)
  5. 2.42.2 → 2.42.4 no changes
  6. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-clean/2.42.1)
  7. 2.39.1 → 2.42.0 no changes
  8. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-clean/2.39.0)
  9. 2.38.1 → 2.38.5 no changes
  10. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-clean/2.38.0)
  11. 2.24.1 → 2.37.7 no changes
  12. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-clean/2.24.0)
  13. 2.23.1 → 2.23.4 no changes
  14. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-clean/2.23.0)
  15. 2.22.1 → 2.22.5 no changes
  16. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-clean/2.22.0)
  17. 2.10.5 → 2.21.4 no changes
  18. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-clean/2.9.5)
  19. 2.8.6 no changes
  20. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-clean/2.7.6)
  21. 2.4.12 → 2.6.7 no changes
  22. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-clean/2.3.10)
  23. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-clean/2.2.3)
  24. 2.1.4 no changes
  25. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-clean/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-clean#_name)NAME
git-clean - Remove untracked files from the working tree
##  [](https://git-scm.com/docs/git-clean#_synopsis)SYNOPSIS
```
_git clean_ [-d] [-f] [-i] [-n] [-q] [-e <pattern>] [-x | -X] [--] [<pathspec>…​]
```

##  [](https://git-scm.com/docs/git-clean#_description)DESCRIPTION
Cleans the working tree by recursively removing files that are not under version control, starting from the current directory.
Normally, only files unknown to Git are removed, but if the `-x` option is specified, ignored files are also removed. This can, for example, be useful to remove all build products.
If any optional _< pathspec>_... arguments are given, only those paths that match the pathspec are affected.
##  [](https://git-scm.com/docs/git-clean#_options)OPTIONS 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--d)-d 
    
Normally, when no <pathspec> is specified, git clean will not recurse into untracked directories to avoid removing too much. Specify -d to have it recurse into such directories as well. If a <pathspec> is specified, -d is irrelevant; all untracked files matching the specified paths (with exceptions for nested git directories mentioned under `--force`) will be removed. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--f)-f 


[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt---force)--force 
    
If the Git configuration variable clean.requireForce is not set to false, _git clean_ will refuse to delete files or directories unless given -f. Git will refuse to modify untracked nested git repositories (directories with a .git subdirectory) unless a second -f is given. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--i)-i 


[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt---interactive)--interactive 
    
Show what would be done and clean files interactively. See “Interactive mode” for details. Configuration variable `clean.requireForce` is ignored, as this mode gives its own safety protection by going interactive. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--n)-n 


[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt---dry-run)--dry-run 
    
Don’t actually remove anything, just show what would be done. Configuration variable `clean.requireForce` is ignored, as nothing will be deleted anyway. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--q)-q 


[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt---quiet)--quiet 
    
Be quiet, only report errors, but not the files that are successfully removed. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--epattern)-e <pattern> 


[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt---excludepattern)--exclude=<pattern> 
    
Use the given exclude pattern in addition to the standard ignore rules (see [gitignore[5]](https://git-scm.com/docs/gitignore)). 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--x)-x 
    
Don’t use the standard ignore rules (see [gitignore[5]](https://git-scm.com/docs/gitignore)), but still use the ignore rules given with `-e` options from the command line. This allows removing all untracked files, including build products. This can be used (possibly in conjunction with _git restore_ or _git reset_) to create a pristine working directory to test a clean build. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt--X)-X 
    
Remove only files ignored by Git. This may be useful to rebuild everything from scratch, but keep manually created files.
##  [](https://git-scm.com/docs/git-clean#_interactive_mode)Interactive mode
When the command enters the interactive mode, it shows the files and directories to be cleaned, and goes into its interactive command loop.
The command loop shows the list of subcommands available, and gives a prompt "What now> ". In general, when the prompt ends with a single _>_ , you can pick only one of the choices given and type return, like this:
```
    *** Commands ***
	1: clean                2: filter by pattern    3: select by numbers
	4: ask each             5: quit                 6: help
    What now> 1
```

You also could say `c` or `clean` above as long as the choice is unique.
The main command loop has 6 subcommands. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt-clean)clean 
    
Start cleaning files and directories, and then quit. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt-filterbypattern)filter by pattern 
    
This shows the files and directories to be deleted and issues an "Input ignore patterns>>" prompt. You can input space-separated patterns to exclude files and directories from deletion. E.g. "*.c *.h" will exclude files ending with ".c" and ".h" from deletion. When you are satisfied with the filtered result, press ENTER (empty) back to the main menu. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt-selectbynumbers)select by numbers 
    
This shows the files and directories to be deleted and issues an "Select items to delete>>" prompt. When the prompt ends with double _> >_ like this, you can make more than one selection, concatenated with whitespace or comma. Also you can say ranges. E.g. "2-5 7,9" to choose 2,3,4,5,7,9 from the list. If the second number in a range is omitted, all remaining items are selected. E.g. "7-" to choose 7,8,9 from the list. You can say _*_ to choose everything. Also when you are satisfied with the filtered result, press ENTER (empty) back to the main menu. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt-askeach)ask each 
    
This will start to clean, and you must confirm one by one in order to delete items. Please note that this action is not as efficient as the above two actions. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt-quit)quit 
    
This lets you quit without doing any cleaning. 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt-help)help 
    
Show brief usage of interactive git-clean.
##  [](https://git-scm.com/docs/git-clean#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-clean#Documentation/git-clean.txt-cleanrequireForce)clean.requireForce 
    
A boolean to make git-clean refuse to delete files unless -f is given. Defaults to true.
##  [](https://git-scm.com/docs/git-clean#_see_also)SEE ALSO
[gitignore[5]](https://git-scm.com/docs/gitignore)
##  [](https://git-scm.com/docs/git-clean#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### clean
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
