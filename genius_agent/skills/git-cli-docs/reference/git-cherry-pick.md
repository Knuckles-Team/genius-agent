[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --fast-version-control
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
    * [NAME](https://git-scm.com/docs/git-cherry-pick#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-cherry-pick#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-cherry-pick#_description)
    * [OPTIONS](https://git-scm.com/docs/git-cherry-pick#_options)
    * [SEQUENCER SUBCOMMANDS](https://git-scm.com/docs/git-cherry-pick#_sequencer_subcommands)
    * [EXAMPLES](https://git-scm.com/docs/git-cherry-pick#_examples)
    * [SEE ALSO](https://git-scm.com/docs/git-cherry-pick#_see_also)
    * [GIT](https://git-scm.com/docs/git-cherry-pick#_git)


[ English ▾](https://git-scm.com/docs/git-cherry-pick)
Localized versions of **git-cherry-pick** manual
  1. [English ](https://git-scm.com/docs/git-cherry-pick)
  2. [Français ](https://git-scm.com/docs/git-cherry-pick/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-cherry-pick/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-cherry-pick/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-cherry-pick/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-cherry-pick)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-cherry-pick) git-cherry-pick last updated in 2.50.0
Changes in the **git-cherry-pick** manual
  1. 2.50.1 → 2.53.0 no changes
  2. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-cherry-pick/2.50.0)
  3. 2.45.1 → 2.49.1 no changes
  4. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-cherry-pick/2.45.0)
  5. 2.39.4 → 2.44.4 no changes
  6. [2.39.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-04-17_ ](https://git-scm.com/docs/git-cherry-pick/2.39.3)
  7. 2.38.1 → 2.39.2 no changes
  8. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-cherry-pick/2.38.0)
  9. 2.35.1 → 2.37.7 no changes
  10. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-cherry-pick/2.35.0)
  11. 2.30.1 → 2.34.8 no changes
  12. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-cherry-pick/2.30.0)
  13. 2.27.1 → 2.29.3 no changes
  14. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-cherry-pick/2.27.0)
  15. 2.23.1 → 2.26.3 no changes
  16. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-cherry-pick/2.23.0)
  17. 2.22.1 → 2.22.5 no changes
  18. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-cherry-pick/2.22.0)
  19. 2.21.1 → 2.21.4 no changes
  20. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-cherry-pick/2.21.0)
  21. 2.10.5 → 2.20.5 no changes
  22. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-cherry-pick/2.9.5)
  23. 2.8.6 no changes
  24. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-cherry-pick/2.7.6)
  25. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-cherry-pick/2.6.7)
  26. 2.4.12 → 2.5.6 no changes
  27. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-cherry-pick/2.3.10)
  28. 2.1.4 → 2.2.3 no changes
  29. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-cherry-pick/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-cherry-pick#_name)NAME
git-cherry-pick - Apply the changes introduced by some existing commits
##  [](https://git-scm.com/docs/git-cherry-pick#_synopsis)SYNOPSIS
```
_git cherry-pick_ [--edit] [-n] [-m <parent-number>] [-s] [-x] [--ff]
		  [-S[<keyid>]] <commit>…​
_git cherry-pick_ (--continue | --skip | --abort | --quit)
```

##  [](https://git-scm.com/docs/git-cherry-pick#_description)DESCRIPTION
Given one or more existing commits, apply the change each one introduces, recording a new commit for each. This requires your working tree to be clean (no modifications from the HEAD commit).
When it is not obvious how to apply a change, the following happens:
  1. The current branch and `HEAD` pointer stay at the last commit successfully made.
  2. The `CHERRY_PICK_HEAD` ref is set to point at the commit that introduced the change that is difficult to apply.
  3. Paths in which the change applied cleanly are updated both in the index file and in your working tree.
  4. For conflicting paths, the index file records up to three versions, as described in the "TRUE MERGE" section of [git-merge[1]](https://git-scm.com/docs/git-merge). The working tree files will include a description of the conflict bracketed by the usual conflict markers _< <<<<<<_ and _> >>>>>>_.
  5. No other modifications are made.


See [git-merge[1]](https://git-scm.com/docs/git-merge) for some hints on resolving such conflicts.
##  [](https://git-scm.com/docs/git-cherry-pick#_options)OPTIONS 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-commit)<commit>…​ 
    
Commits to cherry-pick. For a more complete list of ways to spell commits, see [gitrevisions[7]](https://git-scm.com/docs/gitrevisions). Sets of commits can be passed but no traversal is done by default, as if the `--no-walk` option was specified, see [git-rev-list[1]](https://git-scm.com/docs/git-rev-list). Note that specifying a range will feed all <commit>…​ arguments to a single revision walk (see a later example that uses _maint master..next_). 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--e)-e 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---edit)--edit 
    
With this option, _git cherry-pick_ will let you edit the commit message prior to committing. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---cleanupmode)--cleanup=<mode> 
    
This option determines how the commit message will be cleaned up before being passed on to the commit machinery. See [git-commit[1]](https://git-scm.com/docs/git-commit) for more details. In particular, if the _< mode>_ is given a value of `scissors`, scissors will be appended to `MERGE_MSG` before being passed on in the case of a conflict. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--x)-x 
    
When recording the commit, append a line that says "(cherry picked from commit …​)" to the original commit message in order to indicate which commit this change was cherry-picked from. This is done only for cherry picks without conflicts. Do not use this option if you are cherry-picking from your private branch because the information is useless to the recipient. If on the other hand you are cherry-picking between two publicly visible branches (e.g. backporting a fix to a maintenance branch for an older release from a development branch), adding this information can be useful. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--r)-r 
    
It used to be that the command defaulted to do `-x` described above, and `-r` was to disable it. Now the default is not to do `-x` so this option is a no-op. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--mparent-number)-m <parent-number> 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---mainlineparent-number)--mainline <parent-number> 
    
Usually you cannot cherry-pick a merge because you do not know which side of the merge should be considered the mainline. This option specifies the parent number (starting from 1) of the mainline and allows cherry-pick to replay the change relative to the specified parent. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--n)-n 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---no-commit)--no-commit 
    
Usually the command automatically creates a sequence of commits. This flag applies the changes necessary to cherry-pick each named commit to your working tree and the index, without making any commit. In addition, when this option is used, your index does not have to match the HEAD commit. The cherry-pick is done against the beginning state of your index.
This is useful when cherry-picking more than one commits' effect to your index in a row. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--s)-s 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---signoff)--signoff 
    
Add a `Signed-off-by` trailer at the end of the commit message. See the signoff option in [git-commit[1]](https://git-scm.com/docs/git-commit) for more information. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--Skeyid)-S[<keyid>] 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---gpg-signkeyid)--gpg-sign[=<keyid>] 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---no-gpg-sign)--no-gpg-sign 
    
GPG-sign commits. The `keyid` argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---ff)--ff 
    
If the current HEAD is the same as the parent of the cherry-pick’ed commit, then a fast forward to this commit will be performed. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---allow-empty)--allow-empty 
    
By default, cherry-picking an empty commit will fail, indicating that an explicit invocation of `git` `commit` `--allow-empty` is required. This option overrides that behavior, allowing empty commits to be preserved automatically in a cherry-pick. Note that when "--ff" is in effect, empty commits that meet the "fast-forward" requirement will be kept even without this option. Note also, that use of this option only keeps commits that were initially empty (i.e. the commit recorded the same tree as its parent). Commits which are made empty due to a previous commit will cause the cherry-pick to fail. To force the inclusion of those commits, use `--empty=keep`. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---allow-empty-message)--allow-empty-message 
    
By default, cherry-picking a commit with an empty message will fail. This option overrides that behavior, allowing commits with empty messages to be cherry picked. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---emptydropkeepstop)--empty=(drop|keep|stop) 
    
How to handle commits being cherry-picked that are redundant with changes already in the current history. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-drop)`drop` 
    
The commit will be dropped. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-keep)`keep` 
    
The commit will be kept. Implies `--allow-empty`. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-stop)`stop` 
    
The cherry-pick will stop when the commit is applied, allowing you to examine the commit. This is the default behavior.
Note that `--empty=drop` and `--empty=stop` only specify how to handle a commit that was not initially empty, but rather became empty due to a previous commit. Commits that were initially empty will still cause the cherry-pick to fail unless one of `--empty=keep` or `--allow-empty` are specified. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---keep-redundant-commits)--keep-redundant-commits 
    
Deprecated synonym for `--empty=keep`. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---strategystrategy)--strategy=<strategy> 
    
Use the given merge strategy. Should only be used once. See the MERGE STRATEGIES section in [git-merge[1]](https://git-scm.com/docs/git-merge) for details. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt--Xoption)-X<option> 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---strategy-optionoption)--strategy-option=<option> 
    
Pass the merge strategy-specific option through to the merge strategy. See [git-merge[1]](https://git-scm.com/docs/git-merge) for details. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---rerere-autoupdate)`--rerere-autoupdate` 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---no-rerere-autoupdate)`--no-rerere-autoupdate` 
    
After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update the index with the result of resolution. `--no-rerere-autoupdate` is a good way to double-check what `rerere` did and catch potential mismerges, before committing the result to the index with a separate `git` `add`.
##  [](https://git-scm.com/docs/git-cherry-pick#_sequencer_subcommands)SEQUENCER SUBCOMMANDS 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---continue)--continue 
    
Continue the operation in progress using the information in `.git/sequencer`. Can be used to continue after resolving conflicts in a failed cherry-pick or revert. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---skip)--skip 
    
Skip the current commit and continue with the rest of the sequence. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---quit)--quit 
    
Forget about the current operation in progress. Can be used to clear the sequencer state after a failed cherry-pick or revert. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt---abort)--abort 
    
Cancel the operation and return to the pre-sequence state.
##  [](https://git-scm.com/docs/git-cherry-pick#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pickmaster)`git` `cherry-pick` `master` 
    
Apply the change introduced by the commit at the tip of the master branch and create a new commit with this change. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pickmaster-1)`git` `cherry-pick` `..master` 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pickHEADmaster)`git` `cherry-pick` `^HEAD` `master` 
    
Apply the changes introduced by all commits that are ancestors of master but not of HEAD to produce new commits. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pickmaintnextmaster)`git` `cherry-pick` `maint` `next` `^master` 


[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pickmaintmasternext)`git` `cherry-pick` `maint` `master..next` 
    
Apply the changes introduced by all commits that are ancestors of maint or next, but not master or any of its ancestors. Note that the latter does not mean `maint` and everything between `master` and `next`; specifically, `maint` will not be used if it is included in `master`. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pickmaster4master2)`git` `cherry-pick` `master~4` `master~2` 
    
Apply the changes introduced by the fifth and third last commits pointed to by master and create 2 new commits with these changes. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pick-nmaster1next)`git` `cherry-pick` `-n` `master~1` `next` 
    
Apply to the working tree and the index the changes introduced by the second last commit pointed to by master and by the last commit pointed to by next, but do not create any commit with these changes. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitcherry-pick--ffnext)`git` `cherry-pick` `--ff` `..next` 
    
If history is linear and HEAD is an ancestor of next, update the working tree and advance the HEAD pointer to match next. Otherwise, apply the changes introduced by those commits that are in next but not HEAD to the current branch, creating a new commit for each new change. 

[](https://git-scm.com/docs/git-cherry-pick#Documentation/git-cherry-pick.txt-gitrev-list--reversemaster--READMEgitcherry-pick-n--stdin)`git` `rev-list` `--reverse` `master` `--` `README` | `git` `cherry-pick` `-n` `--stdin` 
    
Apply the changes introduced by all commits on the master branch that touched README to the working tree and index, so the result can be inspected and made into a single new commit if suitable.
The following sequence attempts to backport a patch, bails out because the code the patch applies to has changed too much, and then tries again, this time exercising more care about matching up context lines.
```
$ git cherry-pick topic^             **(1)**
$ git diff                           **(2)**
$ git cherry-pick --abort            **(3)**
$ git cherry-pick -Xpatience topic^  **(4)**
```

  1. apply the change that would be shown by `git` `show` `topic^`. In this example, the patch does not apply cleanly, so information about the conflict is written to the index and working tree and no new commit results.
  2. summarize changes to be reconciled
  3. cancel the cherry-pick. In other words, return to the pre-cherry-pick state, preserving any local modifications you had in the working tree.
  4. try to apply the change introduced by `topic^` again, spending extra time to avoid mistakes based on incorrectly matching context lines.


##  [](https://git-scm.com/docs/git-cherry-pick#_see_also)SEE ALSO
[git-revert[1]](https://git-scm.com/docs/git-revert)
##  [](https://git-scm.com/docs/git-cherry-pick#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### cherry-pick
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
