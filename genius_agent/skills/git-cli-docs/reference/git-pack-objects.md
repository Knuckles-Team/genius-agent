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
    * [NAME](https://git-scm.com/docs/git-pack-objects#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-pack-objects#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-pack-objects#_description)
    * [OPTIONS](https://git-scm.com/docs/git-pack-objects#_options)
    * [DELTA ISLANDS](https://git-scm.com/docs/git-pack-objects#_delta_islands)
    * [CONFIGURATION](https://git-scm.com/docs/git-pack-objects#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-pack-objects#_see_also)
    * [GIT](https://git-scm.com/docs/git-pack-objects#_git)


[ English ▾](https://git-scm.com/docs/git-pack-objects)
Localized versions of **git-pack-objects** manual
  1. [English ](https://git-scm.com/docs/git-pack-objects)
  2. [Français ](https://git-scm.com/docs/git-pack-objects/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-pack-objects/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-pack-objects/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-pack-objects/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-pack-objects)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-pack-objects) git-pack-objects last updated in 2.52.0
Changes in the **git-pack-objects** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-pack-objects/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-pack-objects/2.51.0)
  5. 2.49.1 → 2.50.1 no changes
  6. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-pack-objects/2.49.0)
  7. 2.43.1 → 2.48.2 no changes
  8. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-pack-objects/2.43.0)
  9. 2.37.1 → 2.42.4 no changes
  10. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-pack-objects/2.37.0)
  11. 2.35.1 → 2.36.6 no changes
  12. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-pack-objects/2.35.0)
  13. 2.33.1 → 2.34.8 no changes
  14. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-pack-objects/2.33.0)
  15. 2.32.1 → 2.32.7 no changes
  16. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-pack-objects/2.32.0)
  17. 2.31.1 → 2.31.8 no changes
  18. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-pack-objects/2.31.0)
  19. 2.29.1 → 2.30.9 no changes
  20. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-pack-objects/2.29.0)
  21. 2.27.1 → 2.28.1 no changes
  22. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-pack-objects/2.27.0)
  23. 2.23.1 → 2.26.3 no changes
  24. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-pack-objects/2.23.0)
  25. 2.21.1 → 2.22.5 no changes
  26. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-pack-objects/2.21.0)
  27. 2.20.1 → 2.20.5 no changes
  28. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-pack-objects/2.20.0)
  29. 2.18.1 → 2.19.6 no changes
  30. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-pack-objects/2.18.0)
  31. 2.17.1 → 2.17.6 no changes
  32. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-pack-objects/2.17.0)
  33. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-pack-objects/2.16.6)
  34. 2.15.4 no changes
  35. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-pack-objects/2.14.6)
  36. 2.10.5 → 2.13.7 no changes
  37. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-pack-objects/2.9.5)
  38. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-pack-objects/2.8.6)
  39. 2.5.6 → 2.7.6 no changes
  40. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-pack-objects/2.4.12)
  41. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-pack-objects/2.3.10)
  42. 2.1.4 → 2.2.3 no changes
  43. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-pack-objects/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-pack-objects#_name)NAME
git-pack-objects - Create a packed archive of objects
##  [](https://git-scm.com/docs/git-pack-objects#_synopsis)SYNOPSIS
```
_git pack-objects_ [-q | --progress | --all-progress] [--all-progress-implied]
		   [--no-reuse-delta] [--delta-base-offset] [--non-empty]
		   [--local] [--incremental] [--window=<n>] [--depth=<n>]
		   [--revs [--unpacked | --all]] [--keep-pack=<pack-name>]
		   [--cruft] [--cruft-expiration=<time>]
		   [--stdout [--filter=<filter-spec>] | <base-name>]
		   [--shallow] [--keep-true-parents] [--[no-]sparse]
		   [--name-hash-version=<n>] [--path-walk] < <object-list>
```

##  [](https://git-scm.com/docs/git-pack-objects#_description)DESCRIPTION
Reads list of objects from the standard input, and writes either one or more packed archives with the specified base-name to disk, or a packed archive to the standard output.
A packed archive is an efficient way to transfer a set of objects between two repositories as well as an access efficient archival format. In a packed archive, an object is either stored as a compressed whole or as a difference from some other object. The latter is often called a delta.
The packed archive format (.pack) is designed to be self-contained so that it can be unpacked without any further information. Therefore, each object that a delta depends upon must be present within the pack.
A pack index file (.idx) is generated for fast, random access to the objects in the pack. Placing both the index file (.idx) and the packed archive (.pack) in the pack/ subdirectory of $GIT_OBJECT_DIRECTORY (or any of the directories on $GIT_ALTERNATE_OBJECT_DIRECTORIES) enables Git to read from the pack archive.
The _git unpack-objects_ command can read the packed archive and expand the objects contained in the pack into "one-file one-object" format; this is typically done by the smart-pull commands when a pack is created on-the-fly for efficient network transport by their peers.
##  [](https://git-scm.com/docs/git-pack-objects#_options)OPTIONS 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt-base-name)base-name 
    
Write into pairs of files (.pack and .idx), using <base-name> to determine the name of the created file. When this option is used, the two files in a pair are written in <base-name>-<SHA-1>.{pack,idx} files. <SHA-1> is a hash based on the pack content and is written to the standard output of the command. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---stdout)--stdout 
    
Write the pack contents (what would have been written to .pack file) out to the standard output. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---revs)--revs 
    
Read the revision arguments from the standard input, instead of individual object names. The revision arguments are processed the same way as _git rev-list_ with the `--objects` flag uses its `commit` arguments to build the list of objects it outputs. The objects on the resulting list are packed. Besides revisions, `--not` or `--shallow` _< SHA-1>_ lines are also accepted. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---unpacked)--unpacked 
    
This implies `--revs`. When processing the list of revision arguments read from the standard input, limit the objects packed to those that are not already packed. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---all)--all 
    
This implies `--revs`. In addition to the list of revision arguments read from the standard input, pretend as if all refs under `refs/` are specified to be included. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---include-tag)--include-tag 
    
Include unasked-for annotated tags if the object they reference was included in the resulting packfile. This can be useful to send new tags to native Git clients. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---stdin-packsmode)--stdin-packs[=<mode>] 
    
Read the basenames of packfiles (e.g., `pack-1234abcd.pack`) from the standard input, instead of object names or revision arguments. The resulting pack contains all objects listed in the included packs (those not beginning with `^`), excluding any objects listed in the excluded packs (beginning with `^`).
When `mode` is "follow", objects from packs not listed on stdin receive special treatment. Objects within unlisted packs will be included if those objects are (1) reachable from the included packs, and (2) not found in any excluded packs. This mode is useful, for example, to resurrect once-unreachable objects found in cruft packs to generate packs which are closed under reachability up to the boundary set by the excluded packs.
Incompatible with `--revs`, or options that imply `--revs` (such as `--all`), with the exception of `--unpacked`, which is compatible. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---cruft)--cruft 
    
Packs unreachable objects into a separate "cruft" pack, denoted by the existence of a `.mtimes` file. Typically used by `git` `repack` `--cruft`. Callers provide a list of pack names and indicate which packs will remain in the repository, along with which packs will be deleted (indicated by the `-` prefix). The contents of the cruft pack are all objects not contained in the surviving packs which have not exceeded the grace period (see `--cruft-expiration` below), or which have exceeded the grace period, but are reachable from an other object which hasn’t.
When the input lists a pack containing all reachable objects (and lists all other packs as pending deletion), the corresponding cruft pack will contain all unreachable objects (with mtime newer than the `--cruft-expiration`) along with any unreachable objects whose mtime is older than the `--cruft-expiration`, but are reachable from an unreachable object whose mtime is newer than the `--cruft-expiration`).
Incompatible with `--unpack-unreachable`, `--keep-unreachable`, `--pack-loose-unreachable`, `--stdin-packs`, as well as any other options which imply `--revs`. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---cruft-expirationapproxidate)--cruft-expiration=<approxidate> 
    
If specified, objects are eliminated from the cruft pack if they have an mtime older than _< approxidate>_. If unspecified (and given `--cruft`), then no objects are eliminated. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---windown)--window=<n> 


[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---depthn)--depth=<n> 
    
These two options affect how the objects contained in the pack are stored using delta compression. The objects are first internally sorted by type, size and optionally names and compared against the other objects within --window to see if using delta compression saves space. --depth limits the maximum delta depth; making it too deep affects the performance on the unpacker side, because delta data needs to be applied that many times to get to the necessary object.
The default value for --window is 10 and --depth is 50. The maximum depth is 4095. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---window-memoryn)--window-memory=<n> 
    
This option provides an additional limit on top of `--window`; the window size will dynamically scale down so as to not take up more than _< n>_ bytes in memory. This is useful in repositories with a mix of large and small objects to not run out of memory with a large window, but still be able to take advantage of the large window for the smaller objects. The size can be suffixed with "k", "m", or "g". `--window-memory=0` makes memory usage unlimited. The default is taken from the `pack.windowMemory` configuration variable. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---max-pack-sizen)--max-pack-size=<n> 
    
In unusual scenarios, you may not be able to create files larger than a certain size on your filesystem, and this option can be used to tell the command to split the output packfile into multiple independent packfiles, each not larger than the given size. The size can be suffixed with "k", "m", or "g". The minimum size allowed is limited to 1 MiB. The default is unlimited, unless the config variable `pack.packSizeLimit` is set. Note that this option may result in a larger and slower repository; see the discussion in `pack.packSizeLimit`. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---honor-pack-keep)--honor-pack-keep 
    
This flag causes an object already in a local pack that has a .keep file to be ignored, even if it would have otherwise been packed. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---keep-packpack-name)--keep-pack=<pack-name> 
    
This flag causes an object already in the given pack to be ignored, even if it would have otherwise been packed. _< pack-name>_ is the pack file name without leading directory (e.g. `pack-123.pack`). The option could be specified multiple times to keep multiple packs. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---incremental)--incremental 
    
This flag causes an object already in a pack to be ignored even if it would have otherwise been packed. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---local)--local 
    
This flag causes an object that is borrowed from an alternate object store to be ignored even if it would have otherwise been packed. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---non-empty)--non-empty 
    
Only create a packed archive if it would contain at least one object. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---progress)--progress 
    
Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---all-progress)--all-progress 
    
When --stdout is specified then progress report is displayed during the object count and compression phases but inhibited during the write-out phase. The reason is that in some cases the output stream is directly linked to another command which may wish to display progress status of its own as it processes incoming pack data. This flag is like --progress except that it forces progress report for the write-out phase as well even if --stdout is used. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---all-progress-implied)--all-progress-implied 
    
This is used to imply --all-progress whenever progress display is activated. Unlike --all-progress this flag doesn’t actually force any progress display by itself. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt--q)-q 
    
This flag makes the command not to report its progress on the standard error stream. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---no-reuse-delta)--no-reuse-delta 
    
When creating a packed archive in a repository that has existing packs, the command reuses existing deltas. This sometimes results in a slightly suboptimal pack. This flag tells the command not to reuse existing deltas but compute them from scratch. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---no-reuse-object)--no-reuse-object 
    
This flag tells the command not to reuse existing object data at all, including non deltified object, forcing recompression of everything. This implies --no-reuse-delta. Useful only in the obscure case where wholesale enforcement of a different compression level on the packed data is desired. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---compressionn)--compression=<n> 
    
Specifies compression level for newly-compressed data in the generated pack. If not specified, pack compression level is determined first by pack.compression, then by core.compression, and defaults to -1, the zlib default, if neither is set. Add --no-reuse-object if you want to force a uniform compression level on all data no matter the source. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---sparse)--sparse 


[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---no-sparse)--no-sparse 
    
Toggle the "sparse" algorithm to determine which objects to include in the pack, when combined with the "--revs" option. This algorithm only walks trees that appear in paths that introduce new objects. This can have significant performance benefits when computing a pack to send a small change. However, it is possible that extra objects are added to the pack-file if the included commits contain certain types of direct renames. If this option is not included, it defaults to the value of `pack.useSparse`, which is true unless otherwise specified. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---thin)--thin 
    
Create a "thin" pack by omitting the common objects between a sender and a receiver in order to reduce network transfer. This option only makes sense in conjunction with --stdout.
Note: A thin pack violates the packed archive format by omitting required objects and is thus unusable by Git without making it self-contained. Use `git` `index-pack` `--fix-thin` (see [git-index-pack[1]](https://git-scm.com/docs/git-index-pack)) to restore the self-contained property. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---shallow)--shallow 
    
Optimize a pack that will be provided to a client with a shallow repository. This option, combined with --thin, can result in a smaller pack at the cost of speed. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---delta-base-offset)--delta-base-offset 
    
A packed archive can express the base object of a delta as either a 20-byte object name or as an offset in the stream, but ancient versions of Git don’t understand the latter. By default, _git pack-objects_ only uses the former format for better compatibility. This option allows the command to use the latter format for compactness. Depending on the average delta chain length, this option typically shrinks the resulting packfile by 3-5 per-cent.
Note: Porcelain commands such as `git` `gc` (see [git-gc[1]](https://git-scm.com/docs/git-gc)), `git` `repack` (see [git-repack[1]](https://git-scm.com/docs/git-repack)) pass this option by default in modern Git when they put objects in your repository into pack files. So does `git` `bundle` (see [git-bundle[1]](https://git-scm.com/docs/git-bundle)) when it creates a bundle. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---threadsn)--threads=<n> 
    
Specifies the number of threads to spawn when searching for best delta matches. This requires that pack-objects be compiled with pthreads otherwise this option is ignored with a warning. This is meant to reduce packing time on multiprocessor machines. The required amount of memory for the delta search window is however multiplied by the number of threads. Specifying 0 will cause Git to auto-detect the number of CPU’s and set the number of threads accordingly. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---index-versionversionoffset)--index-version=<version>[,<offset>] 
    
This is intended to be used by the test suite only. It allows to force the version for the generated pack index, and to force 64-bit index entries on objects located above the given offset. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---keep-true-parents)--keep-true-parents 
    
With this option, parents that are hidden by grafts are packed nevertheless. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---filterfilter-spec)--filter=<filter-spec> 
    
Omits certain objects (usually blobs) from the resulting packfile. See [git-rev-list[1]](https://git-scm.com/docs/git-rev-list) for valid _< filter-spec>_ forms. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---no-filter)--no-filter 
    
Turns off any previous `--filter=` argument. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---missingmissing-action)--missing=<missing-action> 
    
A debug option to help with future "partial clone" development. This option specifies how missing objects are handled.
The form _--missing=error_ requests that pack-objects stop with an error if a missing object is encountered. If the repository is a partial clone, an attempt to fetch missing objects will be made before declaring them missing. This is the default action.
The form _--missing=allow-any_ will allow object traversal to continue if a missing object is encountered. No fetch of a missing object will occur. Missing objects will silently be omitted from the results.
The form _--missing=allow-promisor_ is like _allow-any_ , but will only allow object traversal to continue for EXPECTED promisor missing objects. No fetch of a missing object will occur. An unexpected missing object will raise an error. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---exclude-promisor-objects)--exclude-promisor-objects 
    
Omit objects that are known to be in the promisor remote. (This option has the purpose of operating only on locally created objects, so that when we repack, we still maintain a distinction between locally created objects [without .promisor] and objects from the promisor remote [with .promisor].) This is used with partial clone. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---keep-unreachable)--keep-unreachable 
    
Objects unreachable from the refs in packs named with --unpacked= option are added to the resulting pack, in addition to the reachable objects that are not in packs marked with *.keep files. This implies `--revs`. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---pack-loose-unreachable)--pack-loose-unreachable 
    
Pack unreachable loose objects (and their loose counterparts removed). This implies `--revs`. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---unpack-unreachable)--unpack-unreachable 
    
Keep unreachable objects in loose form. This implies `--revs`. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---delta-islands)--delta-islands 
    
Restrict delta matches based on "islands". See DELTA ISLANDS below. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---name-hash-versionn)--name-hash-version=<n> 
    
While performing delta compression, Git groups objects that may be similar based on heuristics using the path to that object. While grouping objects by an exact path match is good for paths with many versions, there are benefits for finding delta pairs across different full paths. Git collects objects by type and then by a "name hash" of the path and then by size, hoping to group objects that will compress well together.
The default name hash version is `1`, which prioritizes hash locality by considering the final bytes of the path as providing the maximum magnitude to the hash function. This version excels at distinguishing short paths and finding renames across directories. However, the hash function depends primarily on the final 16 bytes of the path. If there are many paths in the repo that have the same final 16 bytes and differ only by parent directory, then this name-hash may lead to too many collisions and cause poor results. At the moment, this version is required when writing reachability bitmap files with `--write-bitmap-index`.
The name hash version `2` has similar locality features as version `1`, except it considers each path component separately and overlays the hashes with a shift. This still prioritizes the final bytes of the path, but also "salts" the lower bits of the hash using the parent directory names. This method allows for some of the locality benefits of version `1` while breaking most of the collisions from a similarly-named file appearing in many different directories. At the moment, this version is not allowed when writing reachability bitmap files with `--write-bitmap-index` and it will be automatically changed to version `1`. 

[](https://git-scm.com/docs/git-pack-objects#Documentation/git-pack-objects.txt---path-walk)--path-walk 
    
Perform compression by first organizing objects by path, then a second pass that compresses across paths as normal. This has the potential to improve delta compression especially in the presence of filenames that cause collisions in Git’s default name-hash algorithm.
Incompatible with `--delta-islands`, `--shallow`, or `--filter`. The `--use-bitmap-index` option will be ignored in the presence of `--path-walk.`
##  [](https://git-scm.com/docs/git-pack-objects#_delta_islands)DELTA ISLANDS
When possible, `pack-objects` tries to reuse existing on-disk deltas to avoid having to search for new ones on the fly. This is an important optimization for serving fetches, because it means the server can avoid inflating most objects at all and just send the bytes directly from disk. This optimization can’t work when an object is stored as a delta against a base which the receiver does not have (and which we are not already sending). In that case the server "breaks" the delta and has to find a new one, which has a high CPU cost. Therefore it’s important for performance that the set of objects in on-disk delta relationships match what a client would fetch.
In a normal repository, this tends to work automatically. The objects are mostly reachable from the branches and tags, and that’s what clients fetch. Any deltas we find on the server are likely to be between objects the client has or will have.
But in some repository setups, you may have several related but separate groups of ref tips, with clients tending to fetch those groups independently. For example, imagine that you are hosting several "forks" of a repository in a single shared object store, and letting clients view them as separate repositories through `GIT_NAMESPACE` or separate repos using the alternates mechanism. A naive repack may find that the optimal delta for an object is against a base that is only found in another fork. But when a client fetches, they will not have the base object, and we’ll have to find a new delta on the fly.
A similar situation may exist if you have many refs outside of `refs/heads/` and `refs/tags/` that point to related objects (e.g., `refs/pull` or `refs/changes` used by some hosting providers). By default, clients fetch only heads and tags, and deltas against objects found only in those other groups cannot be sent as-is.
Delta islands solve this problem by allowing you to group your refs into distinct "islands". Pack-objects computes which objects are reachable from which islands, and refuses to make a delta from an object `A` against a base which is not present in all of `A`'s islands. This results in slightly larger packs (because we miss some delta opportunities), but guarantees that a fetch of one island will not have to recompute deltas on the fly due to crossing island boundaries.
When repacking with delta islands the delta window tends to get clogged with candidates that are forbidden by the config. Repacking with a big --window helps (and doesn’t take as long as it otherwise might because we can reject some object pairs based on islands before doing any computation on the content).
Islands are configured via the `pack.island` option, which can be specified multiple times. Each value is a left-anchored regular expressions matching refnames. For example:
```
[pack]
island = refs/heads/
island = refs/tags/
```

puts heads and tags into an island (whose name is the empty string; see below for more on naming). Any refs which do not match those regular expressions (e.g., `refs/pull/123`) is not in any island. Any object which is reachable only from `refs/pull/` (but not heads or tags) is therefore not a candidate to be used as a base for `refs/heads/`.
Refs are grouped into islands based on their "names", and two regexes that produce the same name are considered to be in the same island. The names are computed from the regexes by concatenating any capture groups from the regex, with a _-_ dash in between. (And if there are no capture groups, then the name is the empty string, as in the above example.) This allows you to create arbitrary numbers of islands. Only up to 14 such capture groups are supported though.
For example, imagine you store the refs for each fork in `refs/virtual/ID`, where `ID` is a numeric identifier. You might then configure:
```
[pack]
island = refs/virtual/([0-9]+)/heads/
island = refs/virtual/([0-9]+)/tags/
island = refs/virtual/([0-9]+)/(pull)/
```

That puts the heads and tags for each fork in their own island (named "1234" or similar), and the pull refs for each go into their own "1234-pull".
Note that we pick a single island for each regex to go into, using "last one wins" ordering (which allows repo-specific config to take precedence over user-wide config, and so forth).
##  [](https://git-scm.com/docs/git-pack-objects#_configuration)CONFIGURATION
Various configuration variables affect packing, see [git-config[1]](https://git-scm.com/docs/git-config) (search for "pack" and "delta").
Notably, delta compression is not used on objects larger than the `core.bigFileThreshold` configuration variable and on files with the attribute `delta` set to false.
##  [](https://git-scm.com/docs/git-pack-objects#_see_also)SEE ALSO
[git-rev-list[1]](https://git-scm.com/docs/git-rev-list) [git-repack[1]](https://git-scm.com/docs/git-repack) [git-prune-packed[1]](https://git-scm.com/docs/git-prune-packed)
##  [](https://git-scm.com/docs/git-pack-objects#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### pack-objects
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
