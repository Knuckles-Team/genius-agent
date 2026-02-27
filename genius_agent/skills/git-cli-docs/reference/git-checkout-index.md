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
    * [NAME](https://git-scm.com/docs/git-checkout-index#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-checkout-index#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-checkout-index#_description)
    * [OPTIONS](https://git-scm.com/docs/git-checkout-index#_options)
    * [Using --temp or --stage=all](https://git-scm.com/docs/git-checkout-index#_using_temp_or_stageall)
    * [EXAMPLES](https://git-scm.com/docs/git-checkout-index#_examples)
    * [GIT](https://git-scm.com/docs/git-checkout-index#_git)


[ English ▾](https://git-scm.com/docs/git-checkout-index)
Localized versions of **git-checkout-index** manual
  1. [English ](https://git-scm.com/docs/git-checkout-index)
  2. [Français ](https://git-scm.com/docs/git-checkout-index/fr)
  3. [日本語 ](https://git-scm.com/docs/git-checkout-index/ja)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-checkout-index/pt_BR)
  5. [Svenska ](https://git-scm.com/docs/git-checkout-index/sv)
  6. [українська мова ](https://git-scm.com/docs/git-checkout-index/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-checkout-index/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-checkout-index)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-checkout-index) git-checkout-index last updated in 2.43.0
Changes in the **git-checkout-index** manual
  1. 2.43.1 → 2.53.0 no changes
  2. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-checkout-index/2.43.0)
  3. 2.36.1 → 2.42.4 no changes
  4. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-checkout-index/2.36.0)
  5. 2.1.4 → 2.35.8 no changes
  6. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-checkout-index/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-checkout-index#_name)NAME
git-checkout-index - Copy files from the index to the working tree
##  [](https://git-scm.com/docs/git-checkout-index#_synopsis)SYNOPSIS
```
_git checkout-index_ [-u] [-q] [-a] [-f] [-n] [--prefix=<string>]
		   [--stage=<number>|all]
		   [--temp]
		   [--ignore-skip-worktree-bits]
		   [-z] [--stdin]
		   [--] [<file>…​]
```

##  [](https://git-scm.com/docs/git-checkout-index#_description)DESCRIPTION
Copies all listed files from the index to the working directory (not overwriting existing files).
##  [](https://git-scm.com/docs/git-checkout-index#_options)OPTIONS 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt--u)-u 


[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---index)--index 
    
update stat information for the checked out entries in the index file. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt--q)-q 


[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---quiet)--quiet 
    
be quiet if files exist or are not in the index 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt--f)-f 


[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---force)--force 
    
forces overwrite of existing files 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt--a)-a 


[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---all)--all 
    
checks out all files in the index except for those with the skip-worktree bit set (see `--ignore-skip-worktree-bits`). Cannot be used together with explicit filenames. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt--n)-n 


[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---no-create)--no-create 
    
Don’t checkout new files, only refresh files already checked out. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---prefixstring)--prefix=<string> 
    
When creating files, prepend <string> (usually a directory including a trailing /) 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---stagenumberall)--stage=<number>|all 
    
Instead of checking out unmerged entries, copy out the files from the named stage. <number> must be between 1 and 3. Note: --stage=all automatically implies --temp. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---temp)--temp 
    
Instead of copying the files to the working directory, write the content to temporary files. The temporary name associations will be written to stdout. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---ignore-skip-worktree-bits)--ignore-skip-worktree-bits 
    
Check out all files, including those with the skip-worktree bit set. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---stdin)--stdin 
    
Instead of taking a list of paths from the command line, read the list of paths from the standard input. Paths are separated by LF (i.e. one path per line) by default. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt--z)-z 
    
Only meaningful with `--stdin`; paths are separated with NUL character instead of LF. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt---)-- 
    
Do not interpret any more arguments as options.
The order of the flags used to matter, but not anymore.
Just doing `git` `checkout-index` does nothing. You probably meant `git` `checkout-index` `-a`. And if you want to force it, you want `git` `checkout-index` `-f` `-a`.
Intuitiveness is not the goal here. Repeatability is. The reason for the "no arguments means no work" behavior is that from scripts you are supposed to be able to do:
```
$ find . -name '*.h' -print0 | xargs -0 git checkout-index -f --
```

which will force all existing `*.h` files to be replaced with their cached copies. If an empty command line implied "all", then this would force-refresh everything in the index, which was not the point. But since _git checkout-index_ accepts --stdin it would be faster to use:
```
$ find . -name '*.h' -print0 | git checkout-index -f -z --stdin
```

The `--` is just a good idea when you know the rest will be filenames; it will prevent problems with a filename of, for example, `-a`. Using `--` is probably a good policy in scripts.
##  [](https://git-scm.com/docs/git-checkout-index#_using_temp_or_stageall)Using --temp or --stage=all
When `--temp` is used (or implied by `--stage=all`) _git checkout-index_ will create a temporary file for each index entry being checked out. The index will not be updated with stat information. These options can be useful if the caller needs all stages of all unmerged entries so that the unmerged files can be processed by an external merge tool.
A listing will be written to stdout providing the association of temporary file names to tracked path names. The listing format has two variations:
  1. tempname TAB path RS
The first format is what gets used when `--stage` is omitted or is not `--stage=all`. The field tempname is the temporary file name holding the file content and path is the tracked path name in the index. Only the requested entries are output.
  2. stage1temp SP stage2temp SP stage3tmp TAB path RS
The second format is what gets used when `--stage=all`. The three stage temporary fields (stage1temp, stage2temp, stage3temp) list the name of the temporary file if there is a stage entry in the index or `.` if there is no stage entry. Paths which only have a stage 0 entry will always be omitted from the output.


In both formats RS (the record separator) is newline by default but will be the null byte if -z was passed on the command line. The temporary file names are always safe strings; they will never contain directory separators or whitespace characters. The path field is always relative to the current directory and the temporary file names are always relative to the top level directory.
If the object being copied out to a temporary file is a symbolic link the content of the link will be written to a normal file. It is up to the end-user or the Porcelain to make use of this information.
##  [](https://git-scm.com/docs/git-checkout-index#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt-Toupdateandrefreshonlythefilesalreadycheckedout)To update and refresh only the files already checked out 
    
```
$ git checkout-index -n -f -a && git update-index --ignore-missing --refresh
```


[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt-Usinggitcheckout-indextoexportanentiretree)Using _git checkout-index_ to "export an entire tree" 
    
The prefix ability basically makes it trivial to use _git checkout-index_ as an "export as tree" function. Just read the desired tree into the index, and do:
```
$ git checkout-index --prefix=git-export-dir/ -a
```

`git` `checkout-index` will "export" the index into the specified directory.
The final "/" is important. The exported name is literally just prefixed with the specified string. Contrast this with the following example. 

[](https://git-scm.com/docs/git-checkout-index#Documentation/git-checkout-index.txt-Exportfileswithaprefix)Export files with a prefix 
    
```
$ git checkout-index --prefix=.merged- Makefile
```

This will check out the currently cached copy of `Makefile` into the file `.merged-Makefile`.
##  [](https://git-scm.com/docs/git-checkout-index#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### checkout-index
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
