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
    * [NAME](https://git-scm.com/docs/git-revert#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-revert#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-revert#_description)
    * [OPTIONS](https://git-scm.com/docs/git-revert#_options)
    * [SEQUENCER SUBCOMMANDS](https://git-scm.com/docs/git-revert#_sequencer_subcommands)
    * [EXAMPLES](https://git-scm.com/docs/git-revert#_examples)
    * [DISCUSSION](https://git-scm.com/docs/git-revert#_discussion)
    * [CONFIGURATION](https://git-scm.com/docs/git-revert#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-revert#_see_also)
    * [GIT](https://git-scm.com/docs/git-revert#_git)


[ English ▾](https://git-scm.com/docs/git-revert)
Localized versions of **git-revert** manual
  1. [English ](https://git-scm.com/docs/git-revert)
  2. [Français ](https://git-scm.com/docs/git-revert/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-revert/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-revert/sv)
  5. [українська мова ](https://git-scm.com/docs/git-revert/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-revert/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-revert)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-revert) git-revert last updated in 2.50.0
Changes in the **git-revert** manual
  1. 2.50.1 → 2.53.0 no changes
  2. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-revert/2.50.0)
  3. 2.44.1 → 2.49.1 no changes
  4. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-revert/2.44.0)
  5. 2.43.1 → 2.43.7 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-revert/2.43.0)
  7. 2.39.1 → 2.42.4 no changes
  8. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-revert/2.39.0)
  9. 2.38.1 → 2.38.5 no changes
  10. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-revert/2.38.0)
  11. 2.37.1 → 2.37.7 no changes
  12. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-revert/2.37.0)
  13. 2.30.1 → 2.36.6 no changes
  14. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-revert/2.30.0)
  15. 2.27.1 → 2.29.3 no changes
  16. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-revert/2.27.0)
  17. 2.23.1 → 2.26.3 no changes
  18. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-revert/2.23.0)
  19. 2.22.1 → 2.22.5 no changes
  20. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-revert/2.22.0)
  21. 2.10.5 → 2.21.4 no changes
  22. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-revert/2.9.5)
  23. 2.8.6 no changes
  24. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-revert/2.7.6)
  25. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-revert/2.6.7)
  26. 2.1.4 → 2.5.6 no changes
  27. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-revert/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-revert#_name)NAME
git-revert - Revert some existing commits
##  [](https://git-scm.com/docs/git-revert#_synopsis)SYNOPSIS
```
_git revert_ [--[no-]edit] [-n] [-m <parent-number>] [-s] [-S[<keyid>]] <commit>…​
_git revert_ (--continue | --skip | --abort | --quit)
```

##  [](https://git-scm.com/docs/git-revert#_description)DESCRIPTION
Given one or more existing commits, revert the changes that the related patches introduce, and record some new commits that record them. This requires your working tree to be clean (no modifications from the HEAD commit).
Note: _git revert_ is used to record some new commits to reverse the effect of some earlier commits (often only a faulty one). If you want to throw away all uncommitted changes in your working directory, you should see [git-reset[1]](https://git-scm.com/docs/git-reset), particularly the `--hard` option. If you want to extract specific files as they were in another commit, you should see [git-restore[1]](https://git-scm.com/docs/git-restore), specifically the `--source` option. Take care with these alternatives as both will discard uncommitted changes in your working directory.
See "Reset, restore and revert" in [git[1]](https://git-scm.com/docs/git) for the differences between the three commands.
##  [](https://git-scm.com/docs/git-revert#_options)OPTIONS 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt-commit)<commit>…​ 
    
Commits to revert. For a more complete list of ways to spell commit names, see [gitrevisions[7]](https://git-scm.com/docs/gitrevisions). Sets of commits can also be given but no traversal is done by default, see [git-rev-list[1]](https://git-scm.com/docs/git-rev-list) and its `--no-walk` option. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt--e)-e 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---edit)--edit 
    
With this option, _git revert_ will let you edit the commit message prior to committing the revert. This is the default if you run the command from a terminal. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt--mparent-number)-m parent-number 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---mainlineparent-number)--mainline parent-number 
    
Usually you cannot revert a merge because you do not know which side of the merge should be considered the mainline. This option specifies the parent number (starting from 1) of the mainline and allows revert to reverse the change relative to the specified parent.
Reverting a merge commit declares that you will never want the tree changes brought in by the merge. As a result, later merges will only bring in tree changes introduced by commits that are not ancestors of the previously reverted merge. This may or may not be what you want.
See the [revert-a-faulty-merge How-To](https://git-scm.com/docs/howto/revert-a-faulty-merge) for more details. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---no-edit)--no-edit 
    
With this option, _git revert_ will not start the commit message editor. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---cleanupmode)--cleanup=<mode> 
    
This option determines how the commit message will be cleaned up before being passed on to the commit machinery. See [git-commit[1]](https://git-scm.com/docs/git-commit) for more details. In particular, if the _< mode>_ is given a value of `scissors`, scissors will be appended to `MERGE_MSG` before being passed on in the case of a conflict. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt--n)-n 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---no-commit)--no-commit 
    
Usually the command automatically creates some commits with commit log messages stating which commits were reverted. This flag applies the changes necessary to revert the named commits to your working tree and the index, but does not make the commits. In addition, when this option is used, your index does not have to match the HEAD commit. The revert is done against the beginning state of your index.
This is useful when reverting more than one commits' effect to your index in a row. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt--Skeyid)-S[<keyid>] 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---gpg-signkeyid)--gpg-sign[=<keyid>] 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---no-gpg-sign)--no-gpg-sign 
    
GPG-sign commits. The `keyid` argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt--s)-s 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---signoff)--signoff 
    
Add a `Signed-off-by` trailer at the end of the commit message. See the signoff option in [git-commit[1]](https://git-scm.com/docs/git-commit) for more information. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---strategystrategy)--strategy=<strategy> 
    
Use the given merge strategy. Should only be used once. See the MERGE STRATEGIES section in [git-merge[1]](https://git-scm.com/docs/git-merge) for details. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt--Xoption)-X<option> 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---strategy-optionoption)--strategy-option=<option> 
    
Pass the merge strategy-specific option through to the merge strategy. See [git-merge[1]](https://git-scm.com/docs/git-merge) for details. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---rerere-autoupdate)`--rerere-autoupdate` 


[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---no-rerere-autoupdate)`--no-rerere-autoupdate` 
    
After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update the index with the result of resolution. `--no-rerere-autoupdate` is a good way to double-check what `rerere` did and catch potential mismerges, before committing the result to the index with a separate `git` `add`. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---reference)--reference 
    
Instead of starting the body of the log message with "This reverts <full-object-name-of-the-commit-being-reverted>.", refer to the commit using "--pretty=reference" format (cf. [git-log[1]](https://git-scm.com/docs/git-log)). The `revert.reference` configuration variable can be used to enable this option by default.
##  [](https://git-scm.com/docs/git-revert#_sequencer_subcommands)SEQUENCER SUBCOMMANDS 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---continue)--continue 
    
Continue the operation in progress using the information in `.git/sequencer`. Can be used to continue after resolving conflicts in a failed cherry-pick or revert. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---skip)--skip 
    
Skip the current commit and continue with the rest of the sequence. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---quit)--quit 
    
Forget about the current operation in progress. Can be used to clear the sequencer state after a failed cherry-pick or revert. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt---abort)--abort 
    
Cancel the operation and return to the pre-sequence state.
##  [](https://git-scm.com/docs/git-revert#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt-gitrevertHEAD3)`git` `revert` `HEAD~3` 
    
Revert the changes specified by the fourth last commit in HEAD and create a new commit with the reverted changes. 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt-gitrevert-nmaster5master2)`git` `revert` `-n` `master~5..master~2` 
    
Revert the changes done by commits from the fifth last commit in master (included) to the third last commit in master (included), but do not create any commit with the reverted changes. The revert only modifies the working tree and the index.
##  [](https://git-scm.com/docs/git-revert#_discussion)DISCUSSION
While git creates a basic commit message automatically, it is _strongly_ recommended to explain why the original commit is being reverted. In addition, repeatedly reverting reverts will result in increasingly unwieldy subject lines, for example _Reapply "Reapply " <original-subject>""_. Please consider rewording these to be shorter and more unique.
##  [](https://git-scm.com/docs/git-revert#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-revert#Documentation/git-revert.txt-revertreference)revert.reference 
    
Setting this variable to true makes `git` `revert` behave as if the `--reference` option is given.
##  [](https://git-scm.com/docs/git-revert#_see_also)SEE ALSO
[git-cherry-pick[1]](https://git-scm.com/docs/git-cherry-pick)
##  [](https://git-scm.com/docs/git-revert#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### revert
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
