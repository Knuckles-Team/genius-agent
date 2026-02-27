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
    * [NAME](https://git-scm.com/docs/git-reset#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-reset#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-reset#_description)
    * [OPTIONS](https://git-scm.com/docs/git-reset#_options)
    * [EXAMPLES](https://git-scm.com/docs/git-reset#_examples)
    * [DISCUSSION](https://git-scm.com/docs/git-reset#_discussion)
    * [GIT](https://git-scm.com/docs/git-reset#_git)


[ English ▾](https://git-scm.com/docs/git-reset)
Localized versions of **git-reset** manual
  1. [English ](https://git-scm.com/docs/git-reset)
  2. [Español ](https://git-scm.com/docs/git-reset/es)
  3. [Français ](https://git-scm.com/docs/git-reset/fr)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-reset/pt_BR)
  5. [Svenska ](https://git-scm.com/docs/git-reset/sv)
  6. [українська мова ](https://git-scm.com/docs/git-reset/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-reset/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-reset)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-reset) git-reset last updated in 2.53.0
Changes in the **git-reset** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-reset/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-reset/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-reset/2.51.0)
  5. 2.50.1 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-reset/2.50.0)
  7. 2.39.4 → 2.49.1 no changes
  8. [2.39.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-04-17_ ](https://git-scm.com/docs/git-reset/2.39.3)
  9. 2.36.1 → 2.39.2 no changes
  10. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-reset/2.36.0)
  11. 2.34.1 → 2.35.8 no changes
  12. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-reset/2.34.0)
  13. 2.27.1 → 2.33.8 no changes
  14. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-reset/2.27.0)
  15. 2.25.1 → 2.26.3 no changes
  16. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-reset/2.25.0)
  17. 2.23.1 → 2.24.4 no changes
  18. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-reset/2.23.0)
  19. 2.22.1 → 2.22.5 no changes
  20. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-reset/2.22.0)
  21. 2.21.1 → 2.21.4 no changes
  22. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-reset/2.21.0)
  23. 2.20.1 → 2.20.5 no changes
  24. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-reset/2.20.0)
  25. 2.15.4 → 2.19.6 no changes
  26. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-reset/2.14.6)
  27. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-reset/2.13.7)
  28. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-reset/2.12.5)
  29. 2.1.4 → 2.11.4 no changes
  30. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-reset/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-reset#_name)NAME
git-reset - Set `HEAD` or the index to a known state
##  [](https://git-scm.com/docs/git-reset#_synopsis)SYNOPSIS
```
git reset [--soft | --mixed [-N] | --hard | --merge | --keep] [-q] [_<commit>_]
git reset [-q] [_<tree-ish>_] [--] _<pathspec>_…​
git reset [-q] [--pathspec-from-file=_<file>_ [--pathspec-file-nul]] [_<tree-ish>_]
git reset (--patch | -p) [_<tree-ish>_] [--] [_<pathspec>_…​]
```

##  [](https://git-scm.com/docs/git-reset#_description)DESCRIPTION
`git` `reset` does either of the following:
  1. `git` `reset` [_< mode>_] _< commit>_ changes which commit `HEAD` points to. This makes it possible to undo various Git operations, for example commit, merge, rebase, and pull.
  2. When you specify files or directories or pass `--patch`, `git` `reset` updates the staged version of the specified files. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-gitresetmodecommit)`git` `reset` [_< mode>_] [_< commit>_] 
    
Set the current branch head (`HEAD`) to point at _< commit>_. Depending on _< mode>_, also update the working directory and/or index to match the contents of _< commit>_. _< commit>_ defaults to `HEAD`. Before the operation, `ORIG_HEAD` is set to the tip of the current branch.
The _< mode>_ must be one of the following (default `--mixed`): 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---mixed)`--mixed` 
    
Leave your working directory unchanged. Update the index to match the new `HEAD`, so nothing will be staged.
If `-N` is specified, mark removed paths as intent-to-add (see [git-add[1]](https://git-scm.com/docs/git-add)). 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---soft)`--soft` 
    
Leave your working tree files and the index unchanged. For example, if you have no staged changes, you can use _git reset --soft HEAD~5; git commit_ to combine the last 5 commits into 1 commit. This works even with changes in the working tree, which are left untouched, but such usage can lead to confusion. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---hard)`--hard` 
    
Overwrite all files and directories with the version from _< commit>_, and may overwrite untracked files. Tracked files not in _< commit>_ are removed so that the working tree matches _< commit>_. Update the index to match the new `HEAD`, so nothing will be staged. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---merge)`--merge` 
    
Reset the index and update the files in the working tree that are different between _< commit>_ and `HEAD`, but keep those which are different between the index and working tree (i.e. which have changes which have not been added). Mainly exists to reset unmerged index entries, like those left behind by `git` `am` `-3` or `git` `switch` `-m` in certain situations. If a file that is different between _< commit>_ and the index has unstaged changes, reset is aborted. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---keep)`--keep` 
    
Resets index entries and updates files in the working tree that are different between _< commit>_ and `HEAD`. If a file that is different between _< commit>_ and `HEAD` has local changes, reset is aborted. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---recurse-submodules)`--recurse-submodules` 


[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---no-recurse-submodules)`--no-recurse-submodules` 
    
When the working tree is updated, using `--recurse-submodules` will also recursively reset the working tree of all active submodules according to the commit recorded in the superproject, also setting the submodules' `HEAD` to be detached at that commit. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-gitreset-qtree-ish--pathspec)`git` `reset` [`-q`] [_< tree-ish>_] [`--`] _< pathspec>_... 


[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-gitreset-q--pathspec-from-filefile--pathspec-file-nultree-ish)`git` `reset` [`-q`] [`--pathspec-from-file=`_< file>_ [`--pathspec-file-nul`]] [_< tree-ish>_] 
    
For all specified files or directories, set the staged version to the version from the given commit or tree (which defaults to `HEAD`).
This means that `git` `reset` _< pathspec>_ is the opposite of `git` `add` _< pathspec>_: it unstages all changes to the specified file(s) or directories. This is equivalent to `git` `restore` `--staged` _< pathspec>_....
In this mode, `git` `reset` updates only the index (without updating the `HEAD` or working tree files). If you want to update the files as well as the index entries, use [git-restore[1]](https://git-scm.com/docs/git-restore). 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-gitreset--patch-ptree-ish--pathspec)`git` `reset` (`--patch` | `-p`) [_< tree-ish>_] [`--`] [_< pathspec>_...] 
    
Interactively select changes from the difference between the index and the specified commit or tree (which defaults to `HEAD`). The index is modified using the chosen changes.
This means that `git` `reset` `-p` is the opposite of `git` `add` `-p`, i.e. you can use it to selectively unstage changes. See the "Interactive Mode" section of [git-add[1]](https://git-scm.com/docs/git-add) to learn how to use the `--patch` option.


See "Reset, restore and revert" in [git[1]](https://git-scm.com/docs/git) for the differences between the three commands.
##  [](https://git-scm.com/docs/git-reset#_options)OPTIONS 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt--q)`-q` 


[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---quiet)`--quiet` 
    
Be quiet, only report errors. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---refresh)`--refresh` 


[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---no-refresh)`--no-refresh` 
    
Refresh the index after a mixed reset. Enabled by default. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---pathspec-from-filefile)`--pathspec-from-file=`_< file>_ 
    
Pathspec is passed in _< file>_ instead of commandline args. If _< file>_ is exactly `-` then standard input is used. Pathspec elements are separated by _LF_ or _CR_ /_LF_. Pathspec elements can be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). See also `--pathspec-file-nul` and global `--literal-pathspecs`. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---pathspec-file-nul)`--pathspec-file-nul` 
    
Only meaningful with `--pathspec-from-file`. Pathspec elements are separated with _NUL_ character and all other characters are taken literally (including newlines and quotes). 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context. Defaults to `diff.context` or 3 if the config option is unset. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---inter-hunk-contextn)`--inter-hunk-context=`_< n>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt---)`--` 
    
Do not interpret any more arguments as options. 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-pathspec)_< pathspec>_... 
    
Limits the paths affected by the operation.
For more details, see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary).
##  [](https://git-scm.com/docs/git-reset#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Undoadd)Undo add 
    
```
$ edit                                     **(1)**
$ git add frotz.c filfre.c
$ mailx                                    **(2)**
$ git reset                                **(3)**
$ git pull git://info.example.com/ nitfol  **(4)**
```

  1. You are happily working on something, and find the changes in these files are in good order. You do not want to see them when you run `git` `diff`, because you plan to work on other files and changes with these files are distracting.
  2. Somebody asks you to pull, and the changes sound worthy of merging.
  3. However, you already dirtied the index (i.e. your index does not match the `HEAD` commit). But you know the pull you are going to make does not affect `frotz.c` or `filfre.c`, so you revert the index changes for these two files. Your changes in working tree remain there.
  4. Then you can pull and merge, leaving `frotz.c` and `filfre.c` changes still in the working tree.



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Undoacommitandredo)Undo a commit and redo 
    
```
$ git commit ...
$ git reset --soft HEAD^      **(1)**
$ edit                        **(2)**
$ git commit -a -c ORIG_HEAD  **(3)**
```

  1. This is most often done when you remembered what you just committed is incomplete, or you misspelled your commit message, or both. Leaves working tree as it was before "reset".
  2. Make corrections to working tree files.
  3. "reset" copies the old head to `.git/ORIG_HEAD`; redo the commit by starting with its log message. If you do not need to edit the message further, you can give `-C` option instead.
See also the `--amend` option to [git-commit[1]](https://git-scm.com/docs/git-commit).



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Undoacommitmakingitatopicbranch)Undo a commit, making it a topic branch 
    
```
$ git branch topic/wip          **(1)**
$ git reset --hard HEAD~3       **(2)**
$ git switch topic/wip          **(3)**
```

  1. You have made some commits, but realize they were premature to be in the `master` branch. You want to continue polishing them in a topic branch, so create `topic/wip` branch off of the current `HEAD`.
  2. Rewind the master branch to get rid of those three commits.
  3. Switch to `topic/wip` branch and keep working.



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Undocommitspermanently)Undo commits permanently 
    
```
$ git commit ...
$ git reset --hard HEAD~3   **(1)**
```

  1. The last three commits (`HEAD`, `HEAD^`, and `HEAD~2`) were bad and you do not want to ever see them again. Do **not** do this if you have already given these commits to somebody else. (See the "RECOVERING FROM UPSTREAM REBASE" section in [git-rebase[1]](https://git-scm.com/docs/git-rebase) for the implications of doing so.)



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Undoamergeorpull)Undo a merge or pull 
    
```
$ git pull                         **(1)**
Auto-merging nitfol
CONFLICT (content): Merge conflict in nitfol
Automatic merge failed; fix conflicts and then commit the result.
$ git reset --hard                 **(2)**
$ git pull . topic/branch          **(3)**
Updating from 41223... to 13134...
Fast-forward
$ git reset --hard ORIG_HEAD       **(4)**
```

  1. Try to update from the upstream resulted in a lot of conflicts; you were not ready to spend a lot of time merging right now, so you decide to do that later.
  2. "pull" has not made merge commit, so `git` `reset` `--hard` which is a synonym for `git` `reset` `--hard` `HEAD` clears the mess from the index file and the working tree.
  3. Merge a topic branch into the current branch, which resulted in a fast-forward.
  4. But you decided that the topic branch is not ready for public consumption yet. "pull" or "merge" always leaves the original tip of the current branch in `ORIG_HEAD`, so resetting hard to it brings your index file and the working tree back to that state, and resets the tip of the branch to that commit.



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Undoamergeorpullinsideadirtyworkingtree)Undo a merge or pull inside a dirty working tree 
    
```
$ git pull                         **(1)**
Auto-merging nitfol
Merge made by recursive.
 nitfol                |   20 +++++----
 ...
$ git reset --merge ORIG_HEAD      **(2)**
```

  1. Even if you may have local modifications in your working tree, you can safely say `git` `pull` when you know that the change in the other branch does not overlap with them.
  2. After inspecting the result of the merge, you may find that the change in the other branch is unsatisfactory. Running `git` `reset` `--hard` `ORIG_HEAD` will let you go back to where you were, but it will discard your local changes, which you do not want. `git` `reset` `--merge` keeps your local changes.



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Interruptedworkflow)Interrupted workflow 
    
Suppose you are interrupted by an urgent fix request while you are in the middle of a large change. The files in your working tree are not in any shape to be committed yet, but you need to get to the other branch for a quick bugfix.
```
$ git switch feature  ;# you were working in "feature" branch and
$ work work work      ;# got interrupted
$ git commit -a -m "snapshot WIP"                 **(1)**
$ git switch master
$ fix fix fix
$ git commit ;# commit with real log
$ git switch feature
$ git reset --soft HEAD^ ;# go back to WIP state  **(2)**
$ git reset                                       **(3)**
```

  1. This commit will get blown away so a throw-away log message is OK.
  2. This removes the _WIP_ commit from the commit history, and sets your working tree to the state just before you made that snapshot.
  3. At this point the index file still has all the WIP changes you committed as _snapshot WIP_. This updates the index to show your WIP files as uncommitted.
See also [git-stash[1]](https://git-scm.com/docs/git-stash).



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Resetasinglefileintheindex)Reset a single file in the index 
    
Suppose you have added a file to your index, but later decide you do not want to add it to your commit. You can remove the file from the index while keeping your changes with git reset.
```
$ git reset -- frotz.c                      **(1)**
$ git commit -m "Commit files in index"     **(2)**
$ git add frotz.c                           **(3)**
```

  1. This removes the file from the index while keeping it in the working directory.
  2. This commits all other changes in the index.
  3. Adds the file to the index again.



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Keepchangesinworkingtreewhilediscardingsomepreviouscommits)Keep changes in working tree while discarding some previous commits 
    
Suppose you are working on something and you commit it, and then you continue working a bit more, but now you think that what you have in your working tree should be in another branch that has nothing to do with what you committed previously. You can start a new branch and reset it while keeping the changes in your working tree.
```
$ git tag start
$ git switch -c branch1
$ edit
$ git commit ...                            **(1)**
$ edit
$ git switch -c branch2                     **(2)**
$ git reset --keep start                    **(3)**
```

  1. This commits your first edits in `branch1`.
  2. In the ideal world, you could have realized that the earlier commit did not belong to the new topic when you created and switched to `branch2` (i.e. `git` `switch` `-c` `branch2` `start`), but nobody is perfect.
  3. But you can use `reset` `--keep` to remove the unwanted commit after you switched to `branch2`.



[](https://git-scm.com/docs/git-reset#Documentation/git-reset.txt-Splitacommitapartintoasequenceofcommits)Split a commit apart into a sequence of commits 
    
Suppose that you have created lots of logically separate changes and committed them together. Then, later you decide that it might be better to have each logical chunk associated with its own commit. You can use git reset to rewind history without changing the contents of your local files, and then successively use `git` `add` `-p` to interactively select which hunks to include into each commit, using `git` `commit` `-c` to pre-populate the commit message.
```
$ git reset -N HEAD^                        **(1)**
$ git add -p                                **(2)**
$ git diff --cached                         **(3)**
$ git commit -c HEAD@{1}                    **(4)**
...                                         **(5)**
$ git add ...                               **(6)**
$ git diff --cached                         **(7)**
$ git commit ...                            **(8)**
```

  1. First, reset the history back one commit so that we remove the original commit, but leave the working tree with all the changes. The `-N` ensures that any new files added with `HEAD` are still marked so that `git` `add` `-p` will find them.
  2. Next, we interactively select diff hunks to add using the `git` `add` `-p` facility. This will ask you about each diff hunk in sequence and you can use simple commands such as "yes, include this", "No don’t include this" or even the very powerful "edit" facility.
  3. Once satisfied with the hunks you want to include, you should verify what has been prepared for the first commit by using `git` `diff` `--cached`. This shows all the changes that have been moved into the index and are about to be committed.
  4. Next, commit the changes stored in the index. The `-c` option specifies to pre-populate the commit message from the original message that you started with in the first commit. This is helpful to avoid retyping it. The `HEAD@{1}` is a special notation for the commit that `HEAD` used to be at prior to the original reset commit (1 change ago). See [git-reflog[1]](https://git-scm.com/docs/git-reflog) for more details. You may also use any other valid commit reference.
  5. You can repeat steps 2-4 multiple times to break the original code into any number of commits.
  6. Now you’ve split out many of the changes into their own commits, and might no longer use the patch mode of `git` `add`, in order to select all remaining uncommitted changes.
  7. Once again, check to verify that you’ve included what you want to. You may also wish to verify that git diff doesn’t show any remaining changes to be committed later.
  8. And finally create the final commit.


##  [](https://git-scm.com/docs/git-reset#_discussion)DISCUSSION
The tables below show what happens when running:
```
git reset --option target
```

to reset the `HEAD` to another commit (`target`) with the different reset options depending on the state of the files.
In these tables, `A`, `B`, `C` and `D` are some different states of a file. For example, the first line of the first table means that if a file is in state `A` in the working tree, in state `B` in the index, in state `C` in `HEAD` and in state `D` in the target, then `git` `reset` `--soft` `target` will leave the file in the working tree in state `A` and in the index in state `B`. It resets (i.e. moves) the `HEAD` (i.e. the tip of the current branch, if you are on one) to `target` (which has the file in state `D`).
```
working index HEAD target         working index HEAD
----------------------------------------------------
 A       B     C    D     --soft   A       B     D
			  --mixed  A       D     D
			  --hard   D       D     D
			  --merge (disallowed)
			  --keep  (disallowed)
```

```
working index HEAD target         working index HEAD
----------------------------------------------------
 A       B     C    C     --soft   A       B     C
			  --mixed  A       C     C
			  --hard   C       C     C
			  --merge (disallowed)
			  --keep   A       C     C
```

```
working index HEAD target         working index HEAD
----------------------------------------------------
 B       B     C    D     --soft   B       B     D
			  --mixed  B       D     D
			  --hard   D       D     D
			  --merge  D       D     D
			  --keep  (disallowed)
```

```
working index HEAD target         working index HEAD
----------------------------------------------------
 B       B     C    C     --soft   B       B     C
			  --mixed  B       C     C
			  --hard   C       C     C
			  --merge  C       C     C
			  --keep   B       C     C
```

```
working index HEAD target         working index HEAD
----------------------------------------------------
 B       C     C    D     --soft   B       C     D
			  --mixed  B       D     D
			  --hard   D       D     D
			  --merge (disallowed)
			  --keep  (disallowed)
```

```
working index HEAD target         working index HEAD
----------------------------------------------------
 B       C     C    C     --soft   B       C     C
			  --mixed  B       C     C
			  --hard   C       C     C
			  --merge  B       C     C
			  --keep   B       C     C
```

`git` `reset` `--merge` is meant to be used when resetting out of a conflicted merge. Any mergy operation guarantees that the working tree file that is involved in the merge does not have a local change with respect to the index before it starts, and that it writes the result out to the working tree. So if we see some difference between the index and the target and also between the index and the working tree, then it means that we are not resetting out from a state that a mergy operation left after failing with a conflict. That is why we disallow `--merge` option in this case.
`git` `reset` `--keep` is meant to be used when removing some of the last commits in the current branch while keeping changes in the working tree. If there could be conflicts between the changes in the commit we want to remove and the changes in the working tree we want to keep, the reset is disallowed. That’s why it is disallowed if there are both changes between the working tree and `HEAD`, and between `HEAD` and the target. To be safe, it is also disallowed when there are unmerged entries.
The following tables show what happens when there are unmerged entries:
```
working index HEAD target         working index HEAD
----------------------------------------------------
 X       U     A    B     --soft  (disallowed)
			  --mixed  X       B     B
			  --hard   B       B     B
			  --merge  B       B     B
			  --keep  (disallowed)
```

```
working index HEAD target         working index HEAD
----------------------------------------------------
 X       U     A    A     --soft  (disallowed)
			  --mixed  X       A     A
			  --hard   A       A     A
			  --merge  A       A     A
			  --keep  (disallowed)
```

`X` means any state and `U` means an unmerged index.
##  [](https://git-scm.com/docs/git-reset#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### reset
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
