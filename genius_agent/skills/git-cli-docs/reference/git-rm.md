[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --local-branching-on-the-cheap
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
    * [NAME](https://git-scm.com/docs/git-rm#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-rm#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-rm#_description)
    * [OPTIONS](https://git-scm.com/docs/git-rm#_options)
    * [REMOVING FILES THAT HAVE DISAPPEARED FROM THE FILESYSTEM](https://git-scm.com/docs/git-rm#_removing_files_that_have_disappeared_from_the_filesystem)
    * [SUBMODULES](https://git-scm.com/docs/git-rm#_submodules)
    * [EXAMPLES](https://git-scm.com/docs/git-rm#_examples)
    * [BUGS](https://git-scm.com/docs/git-rm#_bugs)
    * [SEE ALSO](https://git-scm.com/docs/git-rm#_see_also)
    * [GIT](https://git-scm.com/docs/git-rm#_git)


[ English ▾](https://git-scm.com/docs/git-rm)
Localized versions of **git-rm** manual
  1. [English ](https://git-scm.com/docs/git-rm)
  2. [Español ](https://git-scm.com/docs/git-rm/es)
  3. [Français ](https://git-scm.com/docs/git-rm/fr)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-rm/pt_BR)
  5. [Svenska ](https://git-scm.com/docs/git-rm/sv)
  6. [українська мова ](https://git-scm.com/docs/git-rm/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-rm/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-rm)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-rm) git-rm last updated in 2.50.0
Changes in the **git-rm** manual
  1. 2.50.1 → 2.53.0 no changes
  2. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-rm/2.50.0)
  3. 2.43.1 → 2.49.1 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-rm/2.43.0)
  5. 2.34.1 → 2.42.4 no changes
  6. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-rm/2.34.0)
  7. 2.32.1 → 2.33.8 no changes
  8. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-rm/2.32.0)
  9. 2.26.1 → 2.31.8 no changes
  10. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-rm/2.26.0)
  11. 2.16.6 → 2.25.5 no changes
  12. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-rm/2.15.4)
  13. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-rm/2.14.6)
  14. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-rm/2.13.7)
  15. 2.1.4 → 2.12.5 no changes
  16. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-rm/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-rm#_name)NAME
git-rm - Remove files from the working tree and from the index
##  [](https://git-scm.com/docs/git-rm#_synopsis)SYNOPSIS
```
git rm [-f | --force] [-n] [-r] [--cached] [--ignore-unmatch]
       [--quiet] [--pathspec-from-file=_<file>_ [--pathspec-file-nul]]
       [--] [_<pathspec>_…​]
```

##  [](https://git-scm.com/docs/git-rm#_description)DESCRIPTION
Remove files matching pathspec from the index, or from the working tree and the index. `git` `rm` will not remove a file from just your working directory. (There is no option to remove a file only from the working tree and yet keep it in the index; use `/bin/rm` if you want to do that.) The files being removed have to be identical to the tip of the branch, and no updates to their contents can be staged in the index, though that default behavior can be overridden with the `-f` option. When `--cached` is given, the staged content has to match either the tip of the branch or the file on disk, allowing the file to be removed from just the index. When sparse-checkouts are in use (see [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout)), `git` `rm` will only remove paths within the sparse-checkout patterns.
##  [](https://git-scm.com/docs/git-rm#_options)OPTIONS 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt-pathspec)_< pathspec>_... 
    
Files to remove. A leading directory name (e.g. `dir` to remove `dir/file1` and `dir/file2`) can be given to remove all files in the directory, and recursively all sub-directories, but this requires the `-r` option to be explicitly given.
The command removes only the paths that are known to Git.
File globbing matches across directory boundaries. Thus, given two directories `d` and `d2`, there is a difference between using `git` `rm` `d*'` and `git` `rm` `d/*'`, as the former will also remove all of directory `d2`.
For more details, see the _< pathspec>_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary). 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt--f)`-f` 


[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---force)`--force` 
    
Override the up-to-date check. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt--n)`-n` 


[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---dry-run)`--dry-run` 
    
Don’t actually remove any file(s). Instead, just show if they exist in the index and would otherwise be removed by the command. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt--r)`-r` 
    
Allow recursive removal when a leading directory name is given. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---)`--` 
    
This option can be used to separate command-line options from the list of files, (useful when filenames might be mistaken for command-line options). 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---cached)`--cached` 
    
Use this option to unstage and remove paths only from the index. Working tree files, whether modified or not, will be left alone. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---ignore-unmatch)`--ignore-unmatch` 
    
Exit with a zero status even if no files matched. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---sparse)`--sparse` 
    
Allow updating index entries outside of the sparse-checkout cone. Normally, `git` `rm` refuses to update index entries whose paths do not fit within the sparse-checkout cone. See [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) for more. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt--q)`-q` 


[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---quiet)`--quiet` 
    
`git` `rm` normally outputs one line (in the form of an `rm` command) for each file removed. This option suppresses that output. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---pathspec-from-filefile)`--pathspec-from-file=`_< file>_ 
    
Pathspec is passed in _< file>_ instead of args. If _< file>_ is exactly `-` then standard input is used. Pathspec elements are separated by _LF_ or _CR_ /_LF_. Pathspec elements can be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). See also `--pathspec-file-nul` and global `--literal-pathspecs`. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt---pathspec-file-nul)`--pathspec-file-nul` 
    
Only meaningful with `--pathspec-from-file`. Pathspec elements are separated with _NUL_ character and all other characters are taken literally (including newlines and quotes).
##  [](https://git-scm.com/docs/git-rm#_removing_files_that_have_disappeared_from_the_filesystem)REMOVING FILES THAT HAVE DISAPPEARED FROM THE FILESYSTEM
There is no option for `git` `rm` to remove from the index only the paths that have disappeared from the filesystem. However, depending on the use case, there are several ways that can be done.
###  [](https://git-scm.com/docs/git-rm#_using_git_commit_a)Using “git commit -a”
If you intend that your next commit should record all modifications of tracked files in the working tree and record all removals of files that have been removed from the working tree with `rm` (as opposed to `git` `rm`), use `git` `commit` `-a`, as it will automatically notice and record all removals. You can also have a similar effect without committing by using `git` `add` `-u`.
###  [](https://git-scm.com/docs/git-rm#_using_git_add_a)Using “git add -A”
When accepting a new code drop for a vendor branch, you probably want to record both the removal of paths and additions of new paths as well as modifications of existing paths.
Typically you would first remove all tracked files from the working tree using this command:
```
git ls-files -z | xargs -0 rm -f
```

and then untar the new code in the working tree. Alternately you could _rsync_ the changes into the working tree.
After that, the easiest way to record all removals, additions, and modifications in the working tree is:
```
git add -A
```

See [git-add[1]](https://git-scm.com/docs/git-add).
###  [](https://git-scm.com/docs/git-rm#_other_ways)Other ways
If all you really want to do is to remove from the index the files that are no longer present in the working tree (perhaps because your working tree is dirty so that you cannot use `git` `commit` `-a`), use the following command:
```
git diff --name-only --diff-filter=D -z | xargs -0 git rm --cached
```

##  [](https://git-scm.com/docs/git-rm#_submodules)SUBMODULES
Only submodules using a gitfile (which means they were cloned with a Git version 1.7.8 or newer) will be removed from the work tree, as their repository lives inside the `.git` directory of the superproject. If a submodule (or one of those nested inside it) still uses a `.git` directory, `git` `rm` moves the submodules git directory into the superprojects git directory to protect the submodule’s history. If it exists the `submodule.`_< name>_ section in the [gitmodules[5]](https://git-scm.com/docs/gitmodules) file will also be removed and that file will be staged (unless `--cached` or `-n` are used).
A submodule is considered up to date when the `HEAD` is the same as recorded in the index, no tracked files are modified and no untracked files that aren’t ignored are present in the submodule’s work tree. Ignored files are deemed expendable and won’t stop a submodule’s work tree from being removed.
If you only want to remove the local checkout of a submodule from your work tree without committing the removal, use [git-submodule[1]](https://git-scm.com/docs/git-submodule) `deinit` instead. Also see [gitsubmodules[7]](https://git-scm.com/docs/gitsubmodules) for details on submodule removal.
##  [](https://git-scm.com/docs/git-rm#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt-gitrmDocumentationtxt)_git rm Documentation/\\*.txt_ 
    
Removes all `*.txt` files from the index that are under the `Documentation` directory and any of its subdirectories.
Note that the asterisk `*` is quoted from the shell in this example; this lets Git, and not the shell, expand the pathnames of files and subdirectories under the `Documentation/` directory. 

[](https://git-scm.com/docs/git-rm#Documentation/git-rm.txt-gitrm-fgit-sh)`git` `rm` `-f` `git-*.sh` 
    
Because this example lets the shell expand the asterisk (i.e. you are listing the files explicitly), it does not remove `subdir/git-foo.sh`.
##  [](https://git-scm.com/docs/git-rm#_bugs)BUGS
Each time a superproject update removes a populated submodule (e.g. when switching between commits before and after the removal) a stale submodule checkout will remain in the old location. Removing the old directory is only safe when it uses a gitfile, as otherwise the history of the submodule will be deleted too. This step will be obsolete when recursive submodule update has been implemented.
##  [](https://git-scm.com/docs/git-rm#_see_also)SEE ALSO
[git-add[1]](https://git-scm.com/docs/git-add)
##  [](https://git-scm.com/docs/git-rm#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### rm
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
