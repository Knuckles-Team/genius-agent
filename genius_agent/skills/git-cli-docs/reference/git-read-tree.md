[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --distributed-even-if-your-workflow-isnt
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
    * [NAME](https://git-scm.com/docs/git-read-tree#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-read-tree#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-read-tree#_description)
    * [OPTIONS](https://git-scm.com/docs/git-read-tree#_options)
    * [MERGING](https://git-scm.com/docs/git-read-tree#_merging)
    * [SPARSE CHECKOUT](https://git-scm.com/docs/git-read-tree#_sparse_checkout)
    * [SEE ALSO](https://git-scm.com/docs/git-read-tree#_see_also)
    * [GIT](https://git-scm.com/docs/git-read-tree#_git)


[ English ▾](https://git-scm.com/docs/git-read-tree)
Localized versions of **git-read-tree** manual
  1. [English ](https://git-scm.com/docs/git-read-tree)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-read-tree/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-read-tree/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-read-tree/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-read-tree)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-read-tree) git-read-tree last updated in 2.52.0
Changes in the **git-read-tree** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-read-tree/2.52.0)
  3. 2.43.1 → 2.51.2 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-read-tree/2.43.0)
  5. 2.40.1 → 2.42.4 no changes
  6. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-read-tree/2.40.0)
  7. 2.39.1 → 2.39.5 no changes
  8. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-read-tree/2.39.0)
  9. 2.37.1 → 2.38.5 no changes
  10. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-read-tree/2.37.0)
  11. 2.36.1 → 2.36.6 no changes
  12. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-read-tree/2.36.0)
  13. 2.34.1 → 2.35.8 no changes
  14. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-read-tree/2.34.0)
  15. 2.27.1 → 2.33.8 no changes
  16. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-read-tree/2.27.0)
  17. 2.25.1 → 2.26.3 no changes
  18. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-read-tree/2.25.0)
  19. 2.22.1 → 2.24.4 no changes
  20. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-read-tree/2.22.0)
  21. 2.18.1 → 2.21.4 no changes
  22. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-read-tree/2.18.0)
  23. 2.17.0 → 2.17.6 no changes
  24. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-read-tree/2.16.6)
  25. 2.15.4 no changes
  26. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-read-tree/2.14.6)
  27. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-read-tree/2.13.7)
  28. 2.2.3 → 2.12.5 no changes
  29. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-read-tree/2.1.4)
  30. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-read-tree/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-read-tree#_name)NAME
git-read-tree - Reads tree information into the index
##  [](https://git-scm.com/docs/git-read-tree#_synopsis)SYNOPSIS
```
_git read-tree_ [(-m [--trivial] [--aggressive] | --reset | --prefix=<prefix>)
		[-u | -i]] [--index-output=<file>] [--no-sparse-checkout]
		(--empty | <tree-ish1> [<tree-ish2> [<tree-ish3>]])
```

##  [](https://git-scm.com/docs/git-read-tree#_description)DESCRIPTION
Reads the tree information given by <tree-ish> into the index, but does not actually **update** any of the files it "caches". (see: [git-checkout-index[1]](https://git-scm.com/docs/git-checkout-index))
Optionally, it can merge a tree into the index, perform a fast-forward (i.e. 2-way) merge, or a 3-way merge, with the `-m` flag. When used with `-m`, the `-u` flag causes it to also update the files in the work tree with the result of the merge.
Only trivial merges are done by _git read-tree_ itself. Only conflicting paths will be in an unmerged state when _git read-tree_ returns.
##  [](https://git-scm.com/docs/git-read-tree#_options)OPTIONS 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt--m)-m 
    
Perform a merge, not just a read. The command will refuse to run if your index file has unmerged entries, indicating that you have not finished a previous merge you started. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---reset)--reset 
    
Same as -m, except that unmerged entries are discarded instead of failing. When used with `-u`, updates leading to loss of working tree changes or untracked files or directories will not abort the operation. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt--u)-u 
    
After a successful merge, update the files in the work tree with the result of the merge. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt--i)-i 
    
Usually a merge requires the index file as well as the files in the working tree to be up to date with the current head commit, in order not to lose local changes. This flag disables the check with the working tree and is meant to be used when creating a merge of trees that are not directly related to the current working tree status into a temporary index file. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt--n)-n 


[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---dry-run)--dry-run 
    
Check if the command would error out, without updating the index or the files in the working tree for real. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt--v)-v 
    
Show the progress of checking files out. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---trivial)--trivial 
    
Restrict three-way merge by _git read-tree_ to happen only if there is no file-level merging required, instead of resolving merge for trivial cases and leaving conflicting files unresolved in the index. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---aggressive)--aggressive 
    
Usually a three-way merge by _git read-tree_ resolves the merge for really trivial cases and leaves other cases unresolved in the index, so that porcelains can implement different merge policies. This flag makes the command resolve a few more cases internally:
  * when one side removes a path and the other side leaves the path unmodified. The resolution is to remove that path.
  * when both sides remove a path. The resolution is to remove that path.
  * when both sides add a path identically. The resolution is to add that path.



[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---prefixprefix)--prefix=<prefix> 
    
Keep the current index contents, and read the contents of the named tree-ish under the directory at _< prefix>_. The command will refuse to overwrite entries that already existed in the original index file. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---index-outputfile)--index-output=<file> 
    
Instead of writing the results out to `$GIT_INDEX_FILE`, write the resulting index in the named file. While the command is operating, the original index file is locked with the same mechanism as usual. The file must allow to be rename(2)ed into from a temporary file that is created next to the usual index file; typically this means it needs to be on the same filesystem as the index file itself, and you need write permission to the directories the index file and index output file are located in. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---recurse-submodules)--recurse-submodules 


[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---no-recurse-submodules)--no-recurse-submodules 
    
Using --recurse-submodules will update the content of all active submodules according to the commit recorded in the superproject by calling read-tree recursively, also setting the submodules' HEAD to be detached at that commit. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---no-sparse-checkout)--no-sparse-checkout 
    
Disable sparse checkout support even if `core.sparseCheckout` is true. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---empty)--empty 
    
Instead of reading tree object(s) into the index, just empty it. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt--q)-q 


[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt---quiet)--quiet 
    
Quiet, suppress feedback messages. 

[](https://git-scm.com/docs/git-read-tree#Documentation/git-read-tree.txt-tree-ish)<tree-ish#> 
    
The id of the tree object(s) to be read/merged.
##  [](https://git-scm.com/docs/git-read-tree#_merging)MERGING
If `-m` is specified, _git read-tree_ can perform 3 kinds of merge, a single tree merge if only 1 tree is given, a fast-forward merge with 2 trees, or a 3-way merge if 3 or more trees are provided.
###  [](https://git-scm.com/docs/git-read-tree#_single_tree_merge)Single Tree Merge
If only 1 tree is specified, _git read-tree_ operates as if the user did not specify `-m`, except that if the original index has an entry for a given pathname, and the contents of the path match with the tree being read, the stat info from the index is used. (In other words, the index’s stat()s take precedence over the merged tree’s).
That means that if you do a `git` `read-tree` `-m` _< newtree>_ followed by a `git` `checkout-index` `-f` `-u` `-a`, the _git checkout-index_ only checks out the stuff that really changed.
This is used to avoid unnecessary false hits when _git diff-files_ is run after _git read-tree_.
###  [](https://git-scm.com/docs/git-read-tree#_two_tree_merge)Two Tree Merge
Typically, this is invoked as `git` `read-tree` `-m` `$H` `$M`, where $H is the head commit of the current repository, and $M is the head of a foreign tree, which is simply ahead of $H (i.e. we are in a fast-forward situation).
When two trees are specified, the user is telling _git read-tree_ the following:
  1. The current index and work tree is derived from $H, but the user may have local changes in them since $H.
  2. The user wants to fast-forward to $M.


In this case, the `git` `read-tree` `-m` `$H` `$M` command makes sure that no local change is lost as the result of this "merge". Here are the "carry forward" rules, where "I" denotes the index, "clean" means that index and work tree coincide, and "exists"/"nothing" refer to the presence of a path in the specified commit:
```
	I                   H        M        Result
       -------------------------------------------------------
     0  nothing             nothing  nothing  (does not happen)
     1  nothing             nothing  exists   use M
     2  nothing             exists   nothing  remove path from index
     3  nothing             exists   exists,  use M if "initial checkout",
				     H == M   keep index otherwise
				     exists,  fail
				     H != M

        clean I==H  I==M
       ------------------
     4  yes   N/A   N/A     nothing  nothing  keep index
     5  no    N/A   N/A     nothing  nothing  keep index

     6  yes   N/A   yes     nothing  exists   keep index
     7  no    N/A   yes     nothing  exists   keep index
     8  yes   N/A   no      nothing  exists   fail
     9  no    N/A   no      nothing  exists   fail

     10 yes   yes   N/A     exists   nothing  remove path from index
     11 no    yes   N/A     exists   nothing  fail
     12 yes   no    N/A     exists   nothing  fail
     13 no    no    N/A     exists   nothing  fail

	clean (H==M)
       ------
     14 yes                 exists   exists   keep index
     15 no                  exists   exists   keep index

        clean I==H  I==M (H!=M)
       ------------------
     16 yes   no    no      exists   exists   fail
     17 no    no    no      exists   exists   fail
     18 yes   no    yes     exists   exists   keep index
     19 no    no    yes     exists   exists   keep index
     20 yes   yes   no      exists   exists   use M
     21 no    yes   no      exists   exists   fail
```

In all "keep index" cases, the index entry stays as in the original index file. If the entry is not up to date, _git read-tree_ keeps the copy in the work tree intact when operating under the -u flag.
When this form of _git read-tree_ returns successfully, you can see which of the "local changes" that you made were carried forward by running `git` `diff-index` `--cached` `$M`. Note that this does not necessarily match what `git` `diff-index` `--cached` `$H` would have produced before such a two tree merge. This is because of cases 18 and 19 — if you already had the changes in $M (e.g. maybe you picked it up via e-mail in a patch form), `git` `diff-index` `--cached` `$H` would have told you about the change before this merge, but it would not show in `git` `diff-index` `--cached` `$M` output after the two-tree merge.
Case 3 is slightly tricky and needs explanation. The result from this rule logically should be to remove the path if the user staged the removal of the path and then switching to a new branch. That however will prevent the initial checkout from happening, so the rule is modified to use M (new tree) only when the content of the index is empty. Otherwise the removal of the path is kept as long as $H and $M are the same.
###  [](https://git-scm.com/docs/git-read-tree#_3_way_merge)3-Way Merge
Each "index" entry has two bits worth of "stage" state. stage 0 is the normal one, and is the only one you’d see in any kind of normal use.
However, when you do _git read-tree_ with three trees, the "stage" starts out at 1.
This means that you can do
```
$ git read-tree -m <tree1> <tree2> <tree3>
```

and you will end up with an index with all of the <tree1> entries in "stage1", all of the <tree2> entries in "stage2" and all of the <tree3> entries in "stage3". When performing a merge of another branch into the current branch, we use the common ancestor tree as <tree1>, the current branch head as <tree2>, and the other branch head as <tree3>.
Furthermore, _git read-tree_ has special-case logic that says: if you see a file that matches in all respects in the following states, it "collapses" back to "stage0":
  * stage 2 and 3 are the same; take one or the other (it makes no difference - the same work has been done on our branch in stage 2 and their branch in stage 3)
  * stage 1 and stage 2 are the same and stage 3 is different; take stage 3 (our branch in stage 2 did not do anything since the ancestor in stage 1 while their branch in stage 3 worked on it)
  * stage 1 and stage 3 are the same and stage 2 is different take stage 2 (we did something while they did nothing)


The _git write-tree_ command refuses to write a nonsensical tree, and it will complain about unmerged entries if it sees a single entry that is not stage 0.
OK, this all sounds like a collection of totally nonsensical rules, but it’s actually exactly what you want in order to do a fast merge. The different stages represent the "result tree" (stage 0, aka "merged"), the original tree (stage 1, aka "orig"), and the two trees you are trying to merge (stage 2 and 3 respectively).
The order of stages 1, 2 and 3 (hence the order of three <tree-ish> command-line arguments) are significant when you start a 3-way merge with an index file that is already populated. Here is an outline of how the algorithm works:
  * if a file exists in identical format in all three trees, it will automatically collapse to "merged" state by _git read-tree_.
  * a file that has _any_ difference what-so-ever in the three trees will stay as separate entries in the index. It’s up to "porcelain policy" to determine how to remove the non-0 stages, and insert a merged version.
  * the index file saves and restores with all this information, so you can merge things incrementally, but as long as it has entries in stages 1/2/3 (i.e., "unmerged entries") you can’t write the result. So now the merge algorithm ends up being really simple:
    * you walk the index in order, and ignore all entries of stage 0, since they’ve already been done.
    * if you find a "stage1", but no matching "stage2" or "stage3", you know it’s been removed from both trees (it only existed in the original tree), and you remove that entry.
    * if you find a matching "stage2" and "stage3" tree, you remove one of them, and turn the other into a "stage0" entry. Remove any matching "stage1" entry if it exists too. .. all the normal trivial rules ..


You would normally use _git merge-index_ with supplied _git merge-one-file_ to do this last step. The script updates the files in the working tree as it merges each path and at the end of a successful merge.
When you start a 3-way merge with an index file that is already populated, it is assumed that it represents the state of the files in your work tree, and you can even have files with changes unrecorded in the index file. It is further assumed that this state is "derived" from the stage 2 tree. The 3-way merge refuses to run if it finds an entry in the original index file that does not match stage 2.
This is done to prevent you from losing your work-in-progress changes, and mixing your random changes in an unrelated merge commit. To illustrate, suppose you start from what has been committed last to your repository:
```
$ JC=`git rev-parse --verify "HEAD^0"`
$ git checkout-index -f -u -a $JC
```

You do random edits, without running _git update-index_. And then you notice that the tip of your "upstream" tree has advanced since you pulled from him:
```
$ git fetch git://.... linus
$ LT=`git rev-parse FETCH_HEAD`
```

Your work tree is still based on your HEAD ($JC), but you have some edits since. Three-way merge makes sure that you have not added or modified index entries since $JC, and if you haven’t, then does the right thing. So with the following sequence:
```
$ git read-tree -m -u `git merge-base $JC $LT` $JC $LT
$ git merge-index git-merge-one-file -a
$ echo "Merge with Linus" | \
  git commit-tree `git write-tree` -p $JC -p $LT
```

what you would commit is a pure merge between $JC and $LT without your work-in-progress changes, and your work tree would be updated to the result of the merge.
However, if you have local changes in the working tree that would be overwritten by this merge, _git read-tree_ will refuse to run to prevent your changes from being lost.
In other words, there is no need to worry about what exists only in the working tree. When you have local changes in a part of the project that is not involved in the merge, your changes do not interfere with the merge, and are kept intact. When they **do** interfere, the merge does not even start (_git read-tree_ complains loudly and fails without modifying anything). In such a case, you can simply continue doing what you were in the middle of doing, and when your working tree is ready (i.e. you have finished your work-in-progress), attempt the merge again.
##  [](https://git-scm.com/docs/git-read-tree#_sparse_checkout)SPARSE CHECKOUT
Note: The skip-worktree capabilities in [git-update-index[1]](https://git-scm.com/docs/git-update-index) and `read-tree` predated the introduction of [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout). Users are encouraged to use the `sparse-checkout` command in preference to these plumbing commands for sparse-checkout/skip-worktree related needs. However, the information below might be useful to users trying to understand the pattern style used in non-cone mode of the `sparse-checkout` command.
"Sparse checkout" allows populating the working directory sparsely. It uses the skip-worktree bit (see [git-update-index[1]](https://git-scm.com/docs/git-update-index)) to tell Git whether a file in the working directory is worth looking at.
_git read-tree_ and other merge-based commands (_git merge_ , _git checkout_ …​) can help maintaining the skip-worktree bitmap and working directory update. `$GIT_DIR/info/sparse-checkout` is used to define the skip-worktree reference bitmap. When _git read-tree_ needs to update the working directory, it resets the skip-worktree bit in the index based on this file, which uses the same syntax as .gitignore files. If an entry matches a pattern in this file, or the entry corresponds to a file present in the working tree, then skip-worktree will not be set on that entry. Otherwise, skip-worktree will be set.
Then it compares the new skip-worktree value with the previous one. If skip-worktree turns from set to unset, it will add the corresponding file back. If it turns from unset to set, that file will be removed.
While `$GIT_DIR/info/sparse-checkout` is usually used to specify what files are in, you can also specify what files are _not_ in, using negate patterns. For example, to remove the file `unwanted`:
```
/*
!unwanted
```

Another tricky thing is fully repopulating the working directory when you no longer want sparse checkout. You cannot just disable "sparse checkout" because skip-worktree bits are still in the index and your working directory is still sparsely populated. You should re-populate the working directory with the `$GIT_DIR/info/sparse-checkout` file content as follows:
```
/*
```

Then you can disable sparse checkout. Sparse checkout support in _git read-tree_ and similar commands is disabled by default. You need to turn `core.sparseCheckout` on in order to have sparse checkout support.
##  [](https://git-scm.com/docs/git-read-tree#_see_also)SEE ALSO
[git-write-tree[1]](https://git-scm.com/docs/git-write-tree), [git-ls-files[1]](https://git-scm.com/docs/git-ls-files), [gitignore[5]](https://git-scm.com/docs/gitignore), [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout)
##  [](https://git-scm.com/docs/git-read-tree#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### read-tree
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
