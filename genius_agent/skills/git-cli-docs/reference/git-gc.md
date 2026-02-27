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
    * [NAME](https://git-scm.com/docs/git-gc#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-gc#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-gc#_description)
    * [OPTIONS](https://git-scm.com/docs/git-gc#_options)
    * [AGGRESSIVE](https://git-scm.com/docs/git-gc#_aggressive)
    * [CONFIGURATION](https://git-scm.com/docs/git-gc#_configuration)
    * [NOTES](https://git-scm.com/docs/git-gc#_notes)
    * [HOOKS](https://git-scm.com/docs/git-gc#_hooks)
    * [SEE ALSO](https://git-scm.com/docs/git-gc#_see_also)
    * [GIT](https://git-scm.com/docs/git-gc#_git)


[ English ▾](https://git-scm.com/docs/git-gc)
Localized versions of **git-gc** manual
  1. [English ](https://git-scm.com/docs/git-gc)
  2. [Français ](https://git-scm.com/docs/git-gc/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-gc/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-gc/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-gc/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-gc)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-gc) git-gc last updated in 2.52.0
Changes in the **git-gc** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-gc/2.52.0)
  3. 2.49.1 → 2.51.2 no changes
  4. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-gc/2.49.0)
  5. 2.47.1 → 2.48.2 no changes
  6. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git-gc/2.47.0)
  7. 2.43.1 → 2.46.4 no changes
  8. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-gc/2.43.0)
  9. 2.42.1 → 2.42.4 no changes
  10. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-gc/2.42.0)
  11. 2.41.1 → 2.41.3 no changes
  12. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-gc/2.41.0)
  13. 2.38.1 → 2.40.4 no changes
  14. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-gc/2.38.0)
  15. 2.37.1 → 2.37.7 no changes
  16. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-gc/2.37.0)
  17. 2.31.1 → 2.36.6 no changes
  18. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-gc/2.31.0)
  19. 2.30.1 → 2.30.9 no changes
  20. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-gc/2.30.0)
  21. 2.24.1 → 2.29.3 no changes
  22. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-gc/2.24.0)
  23. 2.22.1 → 2.23.4 no changes
  24. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-gc/2.22.0)
  25. 2.21.1 → 2.21.4 no changes
  26. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-gc/2.21.0)
  27. 2.20.1 → 2.20.5 no changes
  28. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-gc/2.20.0)
  29. 2.19.1 → 2.19.6 no changes
  30. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-gc/2.19.0)
  31. 2.18.1 → 2.18.5 no changes
  32. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-gc/2.18.0)
  33. 2.13.7 → 2.17.6 no changes
  34. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-gc/2.12.5)
  35. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-gc/2.11.4)
  36. 2.10.5 no changes
  37. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-gc/2.9.5)
  38. 2.7.6 → 2.8.6 no changes
  39. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-gc/2.6.7)
  40. 2.5.6 no changes
  41. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-gc/2.4.12)
  42. 2.1.4 → 2.3.10 no changes
  43. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-gc/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-gc#_name)NAME
git-gc - Cleanup unnecessary files and optimize the local repository
##  [](https://git-scm.com/docs/git-gc#_synopsis)SYNOPSIS
```
_git gc_ [--aggressive] [--auto] [--[no-]detach] [--quiet] [--prune=<date> | --no-prune] [--force] [--keep-largest-pack]
```

##  [](https://git-scm.com/docs/git-gc#_description)DESCRIPTION
Runs a number of housekeeping tasks within the current repository, such as compressing file revisions (to reduce disk space and increase performance), removing unreachable objects which may have been created from prior invocations of _git add_ , packing refs, pruning reflog, rerere metadata or stale working trees. May also update ancillary indexes such as the commit-graph.
When common porcelain operations that create objects are run, they will check whether the repository has grown substantially since the last maintenance, and if so run `git` `gc` automatically. See `gc.auto` below for how to disable this behavior.
Running `git` `gc` manually should only be needed when adding objects to a repository without regularly running such porcelain commands, to do a one-off repository optimization, or e.g. to clean up a suboptimal mass-import. See the "PACKFILE OPTIMIZATION" section in [git-fast-import[1]](https://git-scm.com/docs/git-fast-import) for more details on the import case.
##  [](https://git-scm.com/docs/git-gc#_options)OPTIONS 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---aggressive)--aggressive 
    
Usually _git gc_ runs very quickly while providing good disk space utilization and performance. This option will cause _git gc_ to more aggressively optimize the repository at the expense of taking much more time. The effects of this optimization are mostly persistent. See the "AGGRESSIVE" section below for details. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---auto)--auto 
    
With this option, _git gc_ checks whether any housekeeping is required; if not, it exits without performing any work.
See the `gc.auto` option in the "CONFIGURATION" section below for how this heuristic works.
Once housekeeping is triggered by exceeding the limits of configuration options such as `gc.auto` and `gc.autoPackLimit`, all other housekeeping tasks (e.g. rerere, working trees, reflog…​) will be performed as well. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---detach)--detach 


[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---no-detach)--no-detach 
    
Run in the background if the system supports it. This option overrides the `gc.autoDetach` config. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---cruft)--cruft 


[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---no-cruft)--no-cruft 
    
When expiring unreachable objects, pack them separately into a cruft pack instead of storing them as loose objects. `--cruft` is on by default. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---max-cruft-sizen)--max-cruft-size=<n> 
    
When packing unreachable objects into a cruft pack, limit the size of new cruft packs to be at most _< n>_ bytes. Overrides any value specified via the `gc.maxCruftSize` configuration. See the `--max-cruft-size` option of [git-repack[1]](https://git-scm.com/docs/git-repack) for more. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---expire-todir)--expire-to=<dir> 
    
When packing unreachable objects into a cruft pack, write a cruft pack containing pruned objects (if any) to the directory _< dir>_. This option only has an effect when used together with `--cruft`. See the `--expire-to` option of [git-repack[1]](https://git-scm.com/docs/git-repack) for more information. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---prunedate)--prune=<date> 
    
Prune loose objects older than date (default is 2 weeks ago, overridable by the config variable `gc.pruneExpire`). --prune=now prunes loose objects regardless of their age and increases the risk of corruption if another process is writing to the repository concurrently; see "NOTES" below. --prune is on by default. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---no-prune)--no-prune 
    
Do not prune any loose objects. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---quiet)--quiet 
    
Suppress all progress reports. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---force)--force 
    
Force `git` `gc` to run even if there may be another `git` `gc` instance running on this repository. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt---keep-largest-pack)--keep-largest-pack 
    
All packs except the largest non-cruft pack, any packs marked with a `.keep` file, and any cruft pack(s) are consolidated into a single pack. When this option is used, `gc.bigPackThreshold` is ignored.
##  [](https://git-scm.com/docs/git-gc#_aggressive)AGGRESSIVE
When the `--aggressive` option is supplied, [git-repack[1]](https://git-scm.com/docs/git-repack) will be invoked with the `-f` flag, which in turn will pass `--no-reuse-delta` to [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects). This will throw away any existing deltas and re-compute them, at the expense of spending much more time on the repacking.
The effects of this are mostly persistent, e.g. when packs and loose objects are coalesced into one another pack the existing deltas in that pack might get re-used, but there are also various cases where we might pick a sub-optimal delta from a newer pack instead.
Furthermore, supplying `--aggressive` will tweak the `--depth` and `--window` options passed to [git-repack[1]](https://git-scm.com/docs/git-repack). See the `gc.aggressiveDepth` and `gc.aggressiveWindow` settings below. By using a larger window size we’re more likely to find more optimal deltas.
It’s probably not worth it to use this option on a given repository without running tailored performance benchmarks on it. It takes a lot more time, and the resulting space/delta optimization may or may not be worth it. Not using this at all is the right trade-off for most users and their repositories.
##  [](https://git-scm.com/docs/git-gc#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcaggressiveDepth)gc.aggressiveDepth 
    
The depth parameter used in the delta compression algorithm used by _git gc --aggressive_. This defaults to 50, which is the default for the `--depth` option when `--aggressive` isn’t in use.
See the documentation for the `--depth` option in [git-repack[1]](https://git-scm.com/docs/git-repack) for more details. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcaggressiveWindow)gc.aggressiveWindow 
    
The window size parameter used in the delta compression algorithm used by _git gc --aggressive_. This defaults to 250, which is a much more aggressive window size than the default `--window` of 10.
See the documentation for the `--window` option in [git-repack[1]](https://git-scm.com/docs/git-repack) for more details. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcauto)gc.auto 
    
When there are approximately more than this many loose objects in the repository, `git` `gc` `--auto` will pack them. Some Porcelain commands use this command to perform a light-weight garbage collection from time to time. The default value is 6700.
Setting this to 0 disables not only automatic packing based on the number of loose objects, but also any other heuristic `git` `gc` `--auto` will otherwise use to determine if there’s work to do, such as `gc.autoPackLimit`. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcautoPackLimit)gc.autoPackLimit 
    
When there are more than this many packs that are not marked with `*.keep` file in the repository, `git` `gc` `--auto` consolidates them into one larger pack. The default value is 50. Setting this to 0 disables it. Setting `gc.auto` to 0 will also disable this.
See the `gc.bigPackThreshold` configuration variable below. When in use, it’ll affect how the auto pack limit works. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcautoDetach)gc.autoDetach 
    
Make `git` `gc` `--auto` return immediately and run in the background if the system supports it. Default is true. This config variable acts as a fallback in case `maintenance.autoDetach` is not set. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcbigPackThreshold)gc.bigPackThreshold 
    
If non-zero, all non-cruft packs larger than this limit are kept when `git` `gc` is run. This is very similar to `--keep-largest-pack` except that all non-cruft packs that meet the threshold are kept, not just the largest pack. Defaults to zero. Common unit suffixes of _k_ , _m_ , or _g_ are supported.
Note that if the number of kept packs is more than gc.autoPackLimit, this configuration variable is ignored, all packs except the base pack will be repacked. After this the number of packs should go below gc.autoPackLimit and gc.bigPackThreshold should be respected again.
If the amount of memory estimated for `git` `repack` to run smoothly is not available and `gc.bigPackThreshold` is not set, the largest pack will also be excluded (this is the equivalent of running `git` `gc` with `--keep-largest-pack`). 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcwriteCommitGraph)gc.writeCommitGraph 
    
If true, then gc will rewrite the commit-graph file when [git-gc[1]](https://git-scm.com/docs/git-gc) is run. When using `git` `gc` `--auto` the commit-graph will be updated if housekeeping is required. Default is true. See [git-commit-graph[1]](https://git-scm.com/docs/git-commit-graph) for details. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gclogExpiry)gc.logExpiry 
    
If the file gc.log exists, then `git` `gc` `--auto` will print its content and exit with status zero instead of running unless that file is more than _gc.logExpiry_ old. Default is "1.day". See `gc.pruneExpire` for more ways to specify its value. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcpackRefs)gc.packRefs 
    
Running `git` `pack-refs` in a repository renders it unclonable by Git versions prior to 1.5.1.2 over dumb transports such as HTTP. This variable determines whether _git gc_ runs `git` `pack-refs`. This can be set to `notbare` to enable it within all non-bare repos or it can be set to a boolean value. The default is `true`. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gccruftPacks)gc.cruftPacks 
    
Store unreachable objects in a cruft pack (see [git-repack[1]](https://git-scm.com/docs/git-repack)) instead of as loose objects. The default is `true`. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcmaxCruftSize)gc.maxCruftSize 
    
Limit the size of new cruft packs when repacking. When specified in addition to `--max-cruft-size`, the command line option takes priority. See the `--max-cruft-size` option of [git-repack[1]](https://git-scm.com/docs/git-repack). 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcpruneExpire)gc.pruneExpire 
    
When _git gc_ is run, it will call _prune --expire 2.weeks.ago_ (and _repack --cruft --cruft-expiration 2.weeks.ago_ if using cruft packs via `gc.cruftPacks` or `--cruft`). Override the grace period with this config variable. The value "now" may be used to disable this grace period and always prune unreachable objects immediately, or "never" may be used to suppress pruning. This feature helps prevent corruption when _git gc_ runs concurrently with another process writing to the repository; see the "NOTES" section of [git-gc[1]](https://git-scm.com/docs/git-gc). 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcworktreePruneExpire)gc.worktreePruneExpire 
    
When _git gc_ is run, it calls _git worktree prune --expire 3.months.ago_. This config variable can be used to set a different grace period. The value "now" may be used to disable the grace period and prune `$GIT_DIR/worktrees` immediately, or "never" may be used to suppress pruning. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcreflogExpire)gc.reflogExpire 


[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcpatternreflogExpire)gc.<pattern>.reflogExpire 
    
_git reflog expire_ removes reflog entries older than this time; defaults to 90 days. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. With "<pattern>" (e.g. "refs/stash") in the middle the setting applies only to the refs that match the <pattern>. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcreflogExpireUnreachable)gc.reflogExpireUnreachable 


[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcpatternreflogExpireUnreachable)gc.<pattern>.reflogExpireUnreachable 
    
_git reflog expire_ removes reflog entries older than this time and are not reachable from the current tip; defaults to 30 days. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. With "<pattern>" (e.g. "refs/stash") in the middle, the setting applies only to the refs that match the <pattern>.
These types of entries are generally created as a result of using `git` `commit` `--amend` or `git` `rebase` and are the commits prior to the amend or rebase occurring. Since these changes are not part of the current project most users will want to expire them sooner, which is why the default is more aggressive than `gc.reflogExpire`. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcrecentObjectsHook)gc.recentObjectsHook 
    
When considering whether or not to remove an object (either when generating a cruft pack or storing unreachable objects as loose), use the shell to execute the specified command(s). Interpret their output as object IDs which Git will consider as "recent", regardless of their age. By treating their mtimes as "now", any objects (and their descendants) mentioned in the output will be kept regardless of their true age.
Output must contain exactly one hex object ID per line, and nothing else. Objects which cannot be found in the repository are ignored. Multiple hooks are supported, but all must exit successfully, else the operation (either generating a cruft pack or unpacking unreachable objects) will be halted. 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcrepackFilter)gc.repackFilter 
    
When repacking, use the specified filter to move certain objects into a separate packfile. See the `--filter=`_< filter-spec>_ option of [git-repack[1]](https://git-scm.com/docs/git-repack). 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcrepackFilterTo)gc.repackFilterTo 
    
When repacking and using a filter, see `gc.repackFilter`, the specified location will be used to create the packfile containing the filtered out objects. **WARNING:** The specified location should be accessible, using for example the Git alternates mechanism, otherwise the repo could be considered corrupt by Git as it might not be able to access the objects in that packfile. See the `--filter-to=`_< dir>_ option of [git-repack[1]](https://git-scm.com/docs/git-repack) and the `objects/info/alternates` section of [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout). 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcrerereResolved)gc.rerereResolved 
    
Records of conflicted merge you resolved earlier are kept for this many days when _git rerere gc_ is run. You can also use more human-readable "1.month.ago", etc. The default is 60 days. See [git-rerere[1]](https://git-scm.com/docs/git-rerere). 

[](https://git-scm.com/docs/git-gc#Documentation/git-gc.txt-gcrerereUnresolved)gc.rerereUnresolved 
    
Records of conflicted merge you have not resolved are kept for this many days when _git rerere gc_ is run. You can also use more human-readable "1.month.ago", etc. The default is 15 days. See [git-rerere[1]](https://git-scm.com/docs/git-rerere).
##  [](https://git-scm.com/docs/git-gc#_notes)NOTES
_git gc_ tries very hard not to delete objects that are referenced anywhere in your repository. In particular, it will keep not only objects referenced by your current set of branches and tags, but also objects referenced by the index, remote-tracking branches, reflogs (which may reference commits in branches that were later amended or rewound), and anything else in the refs/* namespace. Note that a note (of the kind created by _git notes_) attached to an object does not contribute in keeping the object alive. If you are expecting some objects to be deleted and they aren’t, check all of those locations and decide whether it makes sense in your case to remove those references.
On the other hand, when _git gc_ runs concurrently with another process, there is a risk of it deleting an object that the other process is using but hasn’t created a reference to. This may just cause the other process to fail or may corrupt the repository if the other process later adds a reference to the deleted object. Git has two features that significantly mitigate this problem:
  1. Any object with modification time newer than the `--prune` date is kept, along with everything reachable from it.
  2. Most operations that add an object to the database update the modification time of the object if it is already present so that #1 applies.


However, these features fall short of a complete solution, so users who run commands concurrently have to live with some risk of corruption (which seems to be low in practice).
##  [](https://git-scm.com/docs/git-gc#_hooks)HOOKS
The _git gc --auto_ command will run the _pre-auto-gc_ hook. See [githooks[5]](https://git-scm.com/docs/githooks) for more information.
##  [](https://git-scm.com/docs/git-gc#_see_also)SEE ALSO
[git-prune[1]](https://git-scm.com/docs/git-prune) [git-reflog[1]](https://git-scm.com/docs/git-reflog) [git-repack[1]](https://git-scm.com/docs/git-repack) [git-rerere[1]](https://git-scm.com/docs/git-rerere)
##  [](https://git-scm.com/docs/git-gc#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gc
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
