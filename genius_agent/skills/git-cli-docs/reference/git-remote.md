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
    * [NAME](https://git-scm.com/docs/git-remote#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-remote#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-remote#_description)
    * [OPTIONS](https://git-scm.com/docs/git-remote#_options)
    * [COMMANDS](https://git-scm.com/docs/git-remote#_commands)
    * [DISCUSSION](https://git-scm.com/docs/git-remote#_discussion)
    * [EXIT STATUS](https://git-scm.com/docs/git-remote#_exit_status)
    * [EXAMPLES](https://git-scm.com/docs/git-remote#_examples)
    * [SEE ALSO](https://git-scm.com/docs/git-remote#_see_also)
    * [GIT](https://git-scm.com/docs/git-remote#_git)


[ English ▾](https://git-scm.com/docs/git-remote)
Localized versions of **git-remote** manual
  1. [English ](https://git-scm.com/docs/git-remote)
  2. [Français ](https://git-scm.com/docs/git-remote/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-remote/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-remote/sv)
  5. [українська мова ](https://git-scm.com/docs/git-remote/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-remote/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-remote)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-remote) git-remote last updated in 2.53.0
Changes in the **git-remote** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-remote/2.53.0)
  2. 2.45.1 → 2.52.0 no changes
  3. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-remote/2.45.0)
  4. 2.37.1 → 2.44.4 no changes
  5. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-remote/2.37.0)
  6. 2.36.1 → 2.36.6 no changes
  7. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-remote/2.36.0)
  8. 2.35.1 → 2.35.8 no changes
  9. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-remote/2.35.0)
  10. 2.30.1 → 2.34.8 no changes
  11. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-remote/2.30.0)
  12. 2.29.1 → 2.29.3 no changes
  13. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-remote/2.29.0)
  14. 2.23.1 → 2.28.1 no changes
  15. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-remote/2.23.0)
  16. 2.18.1 → 2.22.5 no changes
  17. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-remote/2.18.0)
  18. 2.17.1 → 2.17.6 no changes
  19. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-remote/2.17.0)
  20. 2.10.5 → 2.16.6 no changes
  21. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-remote/2.9.5)
  22. 2.8.6 no changes
  23. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-remote/2.7.6)
  24. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-remote/2.6.7)
  25. 2.4.12 → 2.5.6 no changes
  26. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-remote/2.3.10)
  27. 2.1.4 → 2.2.3 no changes
  28. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-remote/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-remote#_name)NAME
git-remote - Manage set of tracked repositories
##  [](https://git-scm.com/docs/git-remote#_synopsis)SYNOPSIS
```
git remote [-v | --verbose]
git remote add [-t _<branch>_] [-m _<master>_] [-f] [--[no-]tags] [--mirror=(fetch|push)] _<name>_ _<URL>_
git remote rename [--[no-]progress] _<old>_ _<new>_
git remote remove _<name>_
git remote set-head _<name>_ (-a | --auto | -d | --delete | _<branch>_)
git remote set-branches [--add] _<name>_ _<branch>_…​
git remote get-url [--push] [--all] _<name>_
git remote set-url [--push] _<name>_ _<newurl>_ [_<oldurl>_]
git remote set-url --add [--push] _<name>_ _<newurl>_
git remote set-url --delete [--push] _<name>_ _<URL>_
git remote [-v | --verbose] show [-n] _<name>_…​
git remote prune [-n | --dry-run] _<name>_…​
git remote [-v | --verbose] update [-p | --prune] [(_<group>_ | _<remote>_)…​]
```

##  [](https://git-scm.com/docs/git-remote#_description)DESCRIPTION
Manage the set of repositories ("remotes") whose branches you track.
##  [](https://git-scm.com/docs/git-remote#_options)OPTIONS 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v)`-v` 


[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt---verbose)`--verbose` 
    
Be a little more verbose and show remote url after name. For promisor remotes, also show which filters (`blob:none` etc.) are configured. NOTE: This must be placed between `remote` and subcommand.
##  [](https://git-scm.com/docs/git-remote#_commands)COMMANDS
With no arguments, show a list of existing remotes. Several subcommands are available to perform operations on the remotes. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-add)`add` 
    
Add a remote named _< name>_ for the repository at _< URL>_. The command `git` `fetch` _< name>_ can then be used to create and update remote-tracking branches _< name>_`/`_< branch>_.
With `-f` option, `git` `fetch` _< name>_ is run immediately after the remote information is set up.
With `--tags` option, `git` `fetch` _< name>_ imports every tag from the remote repository.
With `--no-tags` option, `git` `fetch` _< name>_ does not import tags from the remote repository.
By default, only tags on fetched branches are imported (see [git-fetch[1]](https://git-scm.com/docs/git-fetch)).
With `-t` _< branch>_ option, instead of the default glob refspec for the remote to track all branches under the `refs/remotes/`_< name>_`/` namespace, a refspec to track only _< branch>_ is created. You can give more than one `-t` _< branch>_ to track multiple branches without grabbing all branches.
With `-m` _< master>_ option, a symbolic-ref `refs/remotes/`_< name>_`/HEAD` is set up to point at remote’s _< master>_ branch. See also the set-head command.
When a fetch mirror is created with `--mirror=fetch`, the refs will not be stored in the `refs/remotes/` namespace, but rather everything in `refs/` on the remote will be directly mirrored into `refs/` in the local repository. This option only makes sense in bare repositories, because a fetch would overwrite any local commits.
When a push mirror is created with `--mirror=push`, then `git` `push` will always behave as if `--mirror` was passed. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-rename)`rename` 
    
Rename the remote named _< old>_ to _< new>_. All remote-tracking branches and configuration settings for the remote are updated.
In case _< old>_ and _< new>_ are the same, and _< old>_ is a file under `$GIT_DIR/remotes` or `$GIT_DIR/branches`, the remote is converted to the configuration file format. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-remove)`remove` 


[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-rm)`rm` 
    
Remove the remote named _< name>_. All remote-tracking branches and configuration settings for the remote are removed. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-set-head)`set-head` 
    
Set or delete the default branch (i.e. the target of the symbolic-ref `refs/remotes/`_< name>_`/HEAD`) for the named remote. Having a default branch for a remote is not required, but allows the name of the remote to be specified in lieu of a specific branch. For example, if the default branch for `origin` is set to `master`, then `origin` may be specified wherever you would normally specify `origin/master`.
With `-d` or `--delete`, the symbolic ref `refs/remotes/`_< name>_`/HEAD` is deleted.
With `-a` or `--auto`, the remote is queried to determine its `HEAD`, then the symbolic-ref `refs/remotes/`_< name>_`/HEAD` is set to the same branch. e.g., if the remote `HEAD` is pointed at `next`, `git` `remote` `set-head` `origin` `-a` will set the symbolic-ref `refs/remotes/origin/HEAD` to `refs/remotes/origin/next`. This will only work if `refs/remotes/origin/next` already exists; if not it must be fetched first.
Use _< branch>_ to set the symbolic-ref `refs/remotes/`_< name>_`/HEAD` explicitly. e.g., `git` `remote` `set-head` `origin` `master` will set the symbolic-ref `refs/remotes/origin/HEAD` to `refs/remotes/origin/master`. This will only work if `refs/remotes/origin/master` already exists; if not it must be fetched first. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-set-branches)`set-branches` 
    
Change the list of branches tracked by the named remote. This can be used to track a subset of the available remote branches after the initial setup for a remote.
The named branches will be interpreted as if specified with the `-t` option on the `git` `remote` `add` command line.
With `--add`, instead of replacing the list of currently tracked branches, adds to that list. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-get-url)`get-url` 
    
Retrieves the URLs for a remote. Configurations for `insteadOf` and `pushInsteadOf` are expanded here. By default, only the first URL is listed.
With `--push`, push URLs are queried rather than fetch URLs.
With `--all`, all URLs for the remote will be listed. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-set-url)`set-url` 
    
Change URLs for the remote. Sets first URL for remote _< name>_ that matches regex _< oldurl>_ (first URL if no _< oldurl>_ is given) to _< newurl>_. If _< oldurl>_ doesn’t match any URL, an error occurs and nothing is changed.
With `--push`, push URLs are manipulated instead of fetch URLs.
With `--add`, instead of changing existing URLs, new URL is added.
With `--delete`, instead of changing existing URLs, all URLs matching regex _< URL>_ are deleted for remote _< name>_. Trying to delete all non-push URLs is an error.
Note that the push URL and the fetch URL, even though they can be set differently, must still refer to the same place. What you pushed to the push URL should be what you would see if you immediately fetched from the fetch URL. If you are trying to fetch from one place (e.g. your upstream) and push to another (e.g. your publishing repository), use two separate remotes. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-show)`show` 
    
Give some information about the remote _< name>_.
With `-n` option, the remote heads are not queried first with `git` `ls-remote` _< name>_; cached information is used instead. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-prune)`prune` 
    
Delete stale references associated with _< name>_. By default, stale remote-tracking branches under _< name>_ are deleted, but depending on global configuration and the configuration of the remote we might even prune local tags that haven’t been pushed there. Equivalent to `git` `fetch` `--prune` _< name>_, except that no new references will be fetched.
See the PRUNING section of [git-fetch[1]](https://git-scm.com/docs/git-fetch) for what it’ll prune depending on various configuration.
With `--dry-run` option, report what branches would be pruned, but do not actually prune them. 

[](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-update)`update` 
    
Fetch updates for remotes or remote groups in the repository as defined by `remotes.`_< group>_. If neither group nor remote is specified on the command line, the configuration parameter `remotes.default` will be used; if `remotes.default` is not defined, all remotes which do not have the configuration parameter `remote.`_< name>_`.skipDefaultUpdate` set to `true` will be updated. (See [git-config[1]](https://git-scm.com/docs/git-config)).
With `--prune` option, run pruning against all the remotes that are updated.
##  [](https://git-scm.com/docs/git-remote#_discussion)DISCUSSION
The remote configuration is achieved using the `remote.origin.url` and `remote.origin.fetch` configuration variables. (See [git-config[1]](https://git-scm.com/docs/git-config)).
##  [](https://git-scm.com/docs/git-remote#_exit_status)EXIT STATUS
On success, the exit status is `0`.
When subcommands such as `add`, `rename`, and `remove` can’t find the remote in question, the exit status is `2`. When the remote already exists, the exit status is `3`.
On any other error, the exit status may be any other non-zero value.
##  [](https://git-scm.com/docs/git-remote#_examples)EXAMPLES
  * Add a new remote, fetch, and check out a branch from it
```
$ git remote
origin
$ git branch -r
  origin/HEAD -> origin/master
  origin/master
$ git remote add staging git://git.kernel.org/.../gregkh/staging.git
$ git remote
origin
staging
$ git fetch staging
...
From git://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging
 * [new branch]      master     -> staging/master
 * [new branch]      staging-linus -> staging/staging-linus
 * [new branch]      staging-next -> staging/staging-next
$ git branch -r
  origin/HEAD -> origin/master
  origin/master
  staging/master
  staging/staging-linus
  staging/staging-next
$ git switch -c staging staging/master
...
```

  * Imitate `git` `clone` but track only selected branches
```
$ mkdir project.git
$ cd project.git
$ git init
$ git remote add -f -t master -m master origin git://example.com/git.git/
$ git merge origin
```



##  [](https://git-scm.com/docs/git-remote#_see_also)SEE ALSO
[git-fetch[1]](https://git-scm.com/docs/git-fetch) [git-branch[1]](https://git-scm.com/docs/git-branch) [git-config[1]](https://git-scm.com/docs/git-config)
##  [](https://git-scm.com/docs/git-remote#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### remote
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
