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
    * [NAME](https://git-scm.com/docs/git-grep#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-grep#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-grep#_description)
    * [OPTIONS](https://git-scm.com/docs/git-grep#_options)
    * [EXAMPLES](https://git-scm.com/docs/git-grep#_examples)
    * [NOTES ON THREADS](https://git-scm.com/docs/git-grep#_notes_on_threads)
    * [CONFIGURATION](https://git-scm.com/docs/git-grep#_configuration)
    * [GIT](https://git-scm.com/docs/git-grep#_git)


[ English ▾](https://git-scm.com/docs/git-grep)
Localized versions of **git-grep** manual
  1. [English ](https://git-scm.com/docs/git-grep)
  2. [Français ](https://git-scm.com/docs/git-grep/fr)
  3. [日本語 ](https://git-scm.com/docs/git-grep/ja)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-grep/pt_BR)
  5. [українська мова ](https://git-scm.com/docs/git-grep/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-grep/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-grep)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-grep) git-grep last updated in 2.45.0
Changes in the **git-grep** manual
  1. 2.45.1 → 2.53.0 no changes
  2. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-grep/2.45.0)
  3. 2.43.1 → 2.44.4 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-grep/2.43.0)
  5. 2.38.1 → 2.42.4 no changes
  6. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-grep/2.38.0)
  7. 2.32.1 → 2.37.7 no changes
  8. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-grep/2.32.0)
  9. 2.30.1 → 2.31.8 no changes
  10. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-grep/2.30.0)
  11. 2.29.1 → 2.29.3 no changes
  12. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-grep/2.29.0)
  13. 2.27.1 → 2.28.1 no changes
  14. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-grep/2.27.0)
  15. 2.26.1 → 2.26.3 no changes
  16. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-grep/2.26.0)
  17. 2.25.2 → 2.25.5 no changes
  18. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-grep/2.25.1)
  19. 2.24.1 → 2.25.0 no changes
  20. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-grep/2.24.0)
  21. 2.22.1 → 2.23.4 no changes
  22. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-grep/2.22.0)
  23. 2.20.1 → 2.21.4 no changes
  24. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-grep/2.20.0)
  25. 2.19.1 → 2.19.6 no changes
  26. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-grep/2.19.0)
  27. 2.18.1 → 2.18.5 no changes
  28. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-grep/2.18.0)
  29. 2.16.6 → 2.17.6 no changes
  30. 2.15.4 no changes
  31. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-grep/2.14.6)
  32. 2.13.7 no changes
  33. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-grep/2.12.5)
  34. 2.10.5 → 2.11.4 no changes
  35. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-grep/2.9.5)
  36. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-grep/2.8.6)
  37. 2.7.6 no changes
  38. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-grep/2.6.7)
  39. 2.2.3 → 2.5.6 no changes
  40. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-grep/2.1.4)
  41. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-grep/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-grep#_name)NAME
git-grep - Print lines matching a pattern
##  [](https://git-scm.com/docs/git-grep#_synopsis)SYNOPSIS
```
_git grep_ [-a | --text] [-I] [--textconv] [-i | --ignore-case] [-w | --word-regexp]
	   [-v | --invert-match] [-h|-H] [--full-name]
	   [-E | --extended-regexp] [-G | --basic-regexp]
	   [-P | --perl-regexp]
	   [-F | --fixed-strings] [-n | --line-number] [--column]
	   [-l | --files-with-matches] [-L | --files-without-match]
	   [(-O | --open-files-in-pager) [<pager>]]
	   [-z | --null]
	   [ -o | --only-matching ] [-c | --count] [--all-match] [-q | --quiet]
	   [--max-depth <depth>] [--[no-]recursive]
	   [--color[=<when>] | --no-color]
	   [--break] [--heading] [-p | --show-function]
	   [-A <post-context>] [-B <pre-context>] [-C <context>]
	   [-W | --function-context]
	   [(-m | --max-count) <num>]
	   [--threads <num>]
	   [-f <file>] [-e] <pattern>
	   [--and|--or|--not|(|)|-e <pattern>…​]
	   [--recurse-submodules] [--parent-basename <basename>]
	   [ [--[no-]exclude-standard] [--cached | --untracked | --no-index] | <tree>…​]
	   [--] [<pathspec>…​]
```

##  [](https://git-scm.com/docs/git-grep#_description)DESCRIPTION
Look for specified patterns in the tracked files in the work tree, blobs registered in the index file, or blobs in given tree objects. Patterns are lists of one or more search expressions separated by newline characters. An empty string as search expression matches all lines.
##  [](https://git-scm.com/docs/git-grep#_options)OPTIONS 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---cached)--cached 
    
Instead of searching tracked files in the working tree, search blobs registered in the index file. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---untracked)--untracked 
    
In addition to searching in the tracked files in the working tree, search also in untracked files. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---no-index)--no-index 
    
Search files in the current directory that is not managed by Git, or by ignoring that the current directory is managed by Git. This is rather similar to running the regular `grep`(`1`) utility with its `-r` option specified, but with some additional benefits, such as using pathspec patterns to limit paths; see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary) for more information.
This option cannot be used together with `--cached` or `--untracked`. See also `grep.fallbackToNoIndex` in _CONFIGURATION_ below. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---no-exclude-standard)--no-exclude-standard 
    
Also search in ignored files by not honoring the `.gitignore` mechanism. Only useful with `--untracked`. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---exclude-standard)--exclude-standard 
    
Do not pay attention to ignored files specified via the `.gitignore` mechanism. Only useful when searching files in the current directory with `--no-index`. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---recurse-submodules)--recurse-submodules 
    
Recursively search in each submodule that is active and checked out in the repository. When used in combination with the _< tree>_ option the prefix of all submodule output will be the name of the parent project’s _< tree>_ object. This option cannot be used together with `--untracked`, and it has no effect if `--no-index` is specified. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--a)-a 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---text)--text 
    
Process binary files as if they were text. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---textconv)--textconv 
    
Honor textconv filter settings. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---no-textconv)--no-textconv 
    
Do not honor textconv filter settings. This is the default. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--i)-i 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---ignore-case)--ignore-case 
    
Ignore case differences between the patterns and the files. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--I)-I 
    
Don’t match the pattern in binary files. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---max-depthdepth)--max-depth <depth> 
    
For each <pathspec> given on command line, descend at most <depth> levels of directories. A value of -1 means no limit. This option is ignored if <pathspec> contains active wildcards. In other words if "a*" matches a directory named "a*", "*" is matched literally so --max-depth is still effective. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--r)-r 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---recursive)--recursive 
    
Same as `--max-depth=-1`; this is the default. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---no-recursive)--no-recursive 
    
Same as `--max-depth=0`. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--w)-w 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---word-regexp)--word-regexp 
    
Match the pattern only at word boundary (either begin at the beginning of a line, or preceded by a non-word character; end at the end of a line or followed by a non-word character). 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--v)-v 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---invert-match)--invert-match 
    
Select non-matching lines. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--h)-h 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--H)-H 
    
By default, the command shows the filename for each match. `-h` option is used to suppress this output. `-H` is there for completeness and does not do anything except it overrides `-h` given earlier on the command line. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---full-name)--full-name 
    
When run from a subdirectory, the command usually outputs paths relative to the current directory. This option forces paths to be output relative to the project top directory. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--E)-E 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---extended-regexp)--extended-regexp 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--G)-G 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---basic-regexp)--basic-regexp 
    
Use POSIX extended/basic regexp for patterns. Default is to use basic regexp. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--P)-P 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---perl-regexp)--perl-regexp 
    
Use Perl-compatible regular expressions for patterns.
Support for these types of regular expressions is an optional compile-time dependency. If Git wasn’t compiled with support for them providing this option will cause it to die. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--F)-F 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---fixed-strings)--fixed-strings 
    
Use fixed strings for patterns (don’t interpret pattern as a regex). 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--n)-n 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---line-number)--line-number 
    
Prefix the line number to matching lines. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---column)--column 
    
Prefix the 1-indexed byte-offset of the first match from the start of the matching line. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--l)-l 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---files-with-matches)--files-with-matches 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---name-only)--name-only 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--L)-L 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---files-without-match)--files-without-match 
    
Instead of showing every matched line, show only the names of files that contain (or do not contain) matches. For better compatibility with _git diff_ , `--name-only` is a synonym for `--files-with-matches`. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--Opager)-O[<pager>] 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---open-files-in-pagerpager)--open-files-in-pager[=<pager>] 
    
Open the matching files in the pager (not the output of _grep_). If the pager happens to be "less" or "vi", and the user specified only one pattern, the first file is positioned at the first match automatically. The `pager` argument is optional; if specified, it must be stuck to the option without a space. If `pager` is unspecified, the default pager will be used (see `core.pager` in [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--z)-z 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---null)--null 
    
Use \0 as the delimiter for pathnames in the output, and print them verbatim. Without this option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--o)-o 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---only-matching)--only-matching 
    
Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--c)-c 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---count)--count 
    
Instead of showing every matched line, show the number of lines that match. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---colorwhen)--color[=<when>] 
    
Show colored matches. The value must be always (the default), never, or auto. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---no-color)--no-color 
    
Turn off match highlighting, even when the configuration file gives the default to color output. Same as `--color=never`. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---break)--break 
    
Print an empty line between matches from different files. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---heading)--heading 
    
Show the filename above the matches in that file instead of at the start of each shown line. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--p)-p 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---show-function)--show-function 
    
Show the preceding line that contains the function name of the match, unless the matching line is a function name itself. The name is determined in the same way as `git` `diff` works out patch hunk headers (see _Defining a custom hunk-header_ in [gitattributes[5]](https://git-scm.com/docs/gitattributes)). 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--num)-<num> 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--Cnum)-C <num> 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---contextnum)--context <num> 
    
Show <num> leading and trailing lines, and place a line containing `--` between contiguous groups of matches. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--Anum)-A <num> 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---after-contextnum)--after-context <num> 
    
Show <num> trailing lines, and place a line containing `--` between contiguous groups of matches. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--Bnum)-B <num> 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---before-contextnum)--before-context <num> 
    
Show <num> leading lines, and place a line containing `--` between contiguous groups of matches. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--W)-W 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---function-context)--function-context 
    
Show the surrounding text from the previous line containing a function name up to the one before the next function name, effectively showing the whole function in which the match was found. The function names are determined in the same way as `git` `diff` works out patch hunk headers (see _Defining a custom hunk-header_ in [gitattributes[5]](https://git-scm.com/docs/gitattributes)). 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--mnum)-m <num> 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---max-countnum)--max-count <num> 
    
Limit the amount of matches per file. When using the `-v` or `--invert-match` option, the search stops after the specified number of non-matches. A value of -1 will return unlimited results (the default). A value of 0 will exit immediately with a non-zero status. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---threadsnum)--threads <num> 
    
Number of `grep` worker threads to use. See _NOTES ON THREADS_ and `grep.threads` in _CONFIGURATION_ for more information. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--ffile)-f <file> 
    
Read patterns from <file>, one per line.
Passing the pattern via <file> allows for providing a search pattern containing a \0.
Not all pattern types support patterns containing \0. Git will error out if a given pattern type can’t support such a pattern. The `--perl-regexp` pattern type when compiled against the PCRE v2 backend has the widest support for these types of patterns.
In versions of Git before 2.23.0 patterns containing \0 would be silently considered fixed. This was never documented, there were also odd and undocumented interactions between e.g. non-ASCII patterns containing \0 and `--ignore-case`.
In future versions we may learn to support patterns containing \0 for more search backends, until then we’ll die when the pattern type in question doesn’t support them. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--e)-e 
    
The next parameter is the pattern. This option has to be used for patterns starting with `-` and should be used in scripts passing user input to grep. Multiple patterns are combined by _or_. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---and)--and 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---or)--or 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---not)--not 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-)( …​ ) 
    
Specify how multiple patterns are combined using Boolean expressions. `--or` is the default operator. `--and` has higher precedence than `--or`. `-e` has to be used for all patterns. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---all-match)--all-match 
    
When giving multiple pattern expressions combined with `--or`, this flag is specified to limit the match to files that have lines to match all of them. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt--q)-q 


[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---quiet)--quiet 
    
Do not output matched lines; instead, exit with status 0 when there is a match and with non-zero status when there isn’t. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-tree)<tree>…​ 
    
Instead of searching tracked files in the working tree, search blobs in the given trees. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt---)-- 
    
Signals the end of options; the rest of the parameters are <pathspec> limiters. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-pathspec)<pathspec>…​ 
    
If given, limit the search to paths matching at least one pattern. Both leading paths match and glob(7) patterns are supported.
For more details about the <pathspec> syntax, see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary).
##  [](https://git-scm.com/docs/git-grep#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-gitgreptimet--ch)`git` `grep` `time_t'` `--` `*.`[`ch`] 
    
Looks for `time_t` in all tracked .c and .h files in the working directory and its subdirectories. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-gitgrep-edefine--and-eMAXPATH-ePATHMAX)_git grep -e '#define' --and \\( -e MAX_PATH -e PATH_MAX \\)_ 
    
Looks for a line that has `#define` and either `MAX_PATH` or `PATH_MAX`. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-gitgrep--all-match-eNODE-eUnexpected)`git` `grep` `--all-match` `-e` `NODE` `-e` `Unexpected` 
    
Looks for a line that has `NODE` or `Unexpected` in files that have lines that match both. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-gitgrepsolution--Documentation)`git` `grep` `solution` `--` `:^Documentation` 
    
Looks for `solution`, excluding files in `Documentation`.
##  [](https://git-scm.com/docs/git-grep#_notes_on_threads)NOTES ON THREADS
The `--threads` option (and the `grep.threads` configuration) will be ignored when `--open-files-in-pager` is used, forcing a single-threaded execution.
When grepping the object store (with `--cached` or giving tree objects), running with multiple threads might perform slower than single-threaded if `--textconv` is given and there are too many text conversions. Thus, if low performance is experienced in this case, it might be desirable to use `--threads=1`.
##  [](https://git-scm.com/docs/git-grep#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-greplineNumber)grep.lineNumber 
    
If set to true, enable `-n` option by default. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-grepcolumn)grep.column 
    
If set to true, enable the `--column` option by default. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-greppatternType)grep.patternType 
    
Set the default matching behavior. Using a value of _basic_ , _extended_ , _fixed_ , or _perl_ will enable the `--basic-regexp`, `--extended-regexp`, `--fixed-strings`, or `--perl-regexp` option accordingly, while the value _default_ will use the `grep.extendedRegexp` option to choose between _basic_ and _extended_. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-grepextendedRegexp)grep.extendedRegexp 
    
If set to true, enable `--extended-regexp` option by default. This option is ignored when the `grep.patternType` option is set to a value other than _default_. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-grepthreads)grep.threads 
    
Number of grep worker threads to use. If unset (or set to 0), Git will use as many threads as the number of logical cores available. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-grepfullName)grep.fullName 
    
If set to true, enable `--full-name` option by default. 

[](https://git-scm.com/docs/git-grep#Documentation/git-grep.txt-grepfallbackToNoIndex)grep.fallbackToNoIndex 
    
If set to true, fall back to `git` `grep` `--no-index` if `git` `grep` is executed outside of a git repository. Defaults to false.
##  [](https://git-scm.com/docs/git-grep#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### grep
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
