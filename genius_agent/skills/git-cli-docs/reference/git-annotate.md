[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --distributed-is-the-new-centralized
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
    * [NAME](https://git-scm.com/docs/git-annotate#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-annotate#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-annotate#_description)
    * [OPTIONS](https://git-scm.com/docs/git-annotate#_options)
    * [SEE ALSO](https://git-scm.com/docs/git-annotate#_see_also)
    * [GIT](https://git-scm.com/docs/git-annotate#_git)


[ English ▾](https://git-scm.com/docs/git-annotate)
Localized versions of **git-annotate** manual
  1. [English ](https://git-scm.com/docs/git-annotate)
  2. [Français ](https://git-scm.com/docs/git-annotate/fr)
  3. [日本語 ](https://git-scm.com/docs/git-annotate/ja)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-annotate/pt_BR)
  5. [Русский ](https://git-scm.com/docs/git-annotate/ru)
  6. [Svenska ](https://git-scm.com/docs/git-annotate/sv)
  7. [українська мова ](https://git-scm.com/docs/git-annotate/uk)
  8. [简体中文 ](https://git-scm.com/docs/git-annotate/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-annotate)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-annotate) git-annotate last updated in 2.53.0
Changes in the **git-annotate** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-annotate/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-annotate/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-annotate/2.51.0)
  5. 2.50.1 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-annotate/2.50.0)
  7. 2.41.1 → 2.49.1 no changes
  8. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-annotate/2.41.0)
  9. 2.39.1 → 2.40.4 no changes
  10. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-annotate/2.39.0)
  11. 2.34.1 → 2.38.5 no changes
  12. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-annotate/2.34.0)
  13. 2.31.1 → 2.33.8 no changes
  14. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-annotate/2.31.0)
  15. 2.30.1 → 2.30.9 no changes
  16. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-annotate/2.30.0)
  17. 2.29.1 → 2.29.3 no changes
  18. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-annotate/2.29.0)
  19. 2.23.1 → 2.28.1 no changes
  20. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-annotate/2.23.0)
  21. 2.18.1 → 2.22.5 no changes
  22. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-annotate/2.18.0)
  23. 2.16.6 → 2.17.6 no changes
  24. 2.15.4 no changes
  25. 2.13.7 → 2.14.6 no changes
  26. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-annotate/2.12.5)
  27. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-annotate/2.11.4)
  28. 2.9.5 → 2.10.5 no changes
  29. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-annotate/2.8.6)
  30. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-annotate/2.7.6)
  31. 2.5.6 → 2.6.7 no changes
  32. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-annotate/2.4.12)
  33. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-annotate/2.3.10)
  34. 2.1.4 → 2.2.3 no changes
  35. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-annotate/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-annotate#_name)NAME
git-annotate - Annotate file lines with commit information
##  [](https://git-scm.com/docs/git-annotate#_synopsis)SYNOPSIS
```
_git annotate_ [<options>] [<rev-opts>] [<rev>] [--] <file>
```

##  [](https://git-scm.com/docs/git-annotate#_description)DESCRIPTION
Annotates each line in the given file with information from the commit which introduced the line. Optionally annotates from a given revision.
The only difference between this command and [git-blame[1]](https://git-scm.com/docs/git-blame) is that they use slightly different output formats, and this command exists only for backward compatibility to support existing scripts, and provide a more familiar command name for people coming from other SCM systems.
##  [](https://git-scm.com/docs/git-annotate#_options)OPTIONS 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--b)`-b` 
    
Show blank SHA-1 for boundary commits. This can also be controlled via the `blame.blankBoundary` config option. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---root)`--root` 
    
Do not treat root commits as boundaries. This can also be controlled via the `blame.showRoot` config option. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---show-stats)`--show-stats` 
    
Include additional statistics at the end of blame output. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--Lstartend)`-L` _< start>_`,`_< end>_ 


[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--Lfuncname)`-L` `:`_< funcname>_ 
    
Annotate only the line range given by _< start>_`,`_< end>_, or by the function name regex _< funcname>_. May be specified multiple times. Overlapping ranges are allowed.
_< start>_ and _< end>_ are optional. `-L` _< start>_ or `-L` _< start>_`,` spans from _< start>_ to end of file. `-L` `,`_< end>_ spans from start of file to _< end>_.
_< start>_ and _< end>_ can take one of these forms:
  * _< number>_
If _< start>_ or _< end>_ is a number, it specifies an absolute line number (lines count from 1).
  * `/`_< regex>_`/`
This form will use the first line matching the given POSIX _< regex>_. If _< start>_ is a regex, it will search from the end of the previous `-L` range, if any, otherwise from the start of file. If _< start>_ is `^/`_< regex>_`/`, it will search from the start of file. If _< end>_ is a regex, it will search starting at the line given by _< start>_.
  * `+`_< offset>_ or `-`_< offset>_
This is only valid for _< end>_ and will specify a number of lines before or after the line given by _< start>_.


If `:`_< funcname>_ is given in place of _< start>_ and _< end>_, it is a regular expression that denotes the range from the first funcname line that matches _< funcname>_, up to the next funcname line. `:`_< funcname>_ searches from the end of the previous `-L` range, if any, otherwise from the start of file. `^:`_< funcname>_ searches from the start of file. The function names are determined in the same way as `git` `diff` works out patch hunk headers (see _Defining a custom hunk-header_ in [gitattributes[5]](https://git-scm.com/docs/gitattributes)). 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--l)`-l` 
    
Show long rev (Default: off). 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--t)`-t` 
    
Show raw timestamp (Default: off). 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--Srevs-file)`-S` _< revs-file>_ 
    
Use revisions from _< revs-file>_ instead of calling [git-rev-list[1]](https://git-scm.com/docs/git-rev-list). 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---reversestartend)`--reverse` _< start>_`..`_< end>_ 
    
Walk history forward instead of backward. Instead of showing the revision in which a line appeared, this shows the last revision in which a line has existed. This requires a range of revision like _< start>_`..`_< end>_ where the path to blame exists in _< start>_. `git` `blame` `--reverse` _< start>_ is taken as `git` `blame` `--reverse` _< start>_`..HEAD` for convenience. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---first-parent)`--first-parent` 
    
Follow only the first parent commit upon seeing a merge commit. This option can be used to determine when a line was introduced to a particular integration branch, rather than when it was introduced to the history overall. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--p)`-p` 


[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---porcelain)`--porcelain` 
    
Show in a format designed for machine consumption. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---line-porcelain)`--line-porcelain` 
    
Show the porcelain format, but output commit information for each line, not just the first time a commit is referenced. Implies `--porcelain`. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---incremental)`--incremental` 
    
Show the result incrementally in a format designed for machine consumption. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---encodingencoding)`--encoding=`_< encoding>_ 
    
Specify the encoding used to output author names and commit summaries. Setting it to `none` makes blame output unconverted data. For more information see the discussion about encoding in the [git-log[1]](https://git-scm.com/docs/git-log) manual page. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---contentsfile)`--contents` _< file>_ 
    
Annotate using the contents from _< file>_, starting from _< rev>_ if it is specified, and `HEAD` otherwise. You may specify `-` to make the command read from the standard input for the file contents. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---dateformat)`--date` _< format>_ 
    
Specify the format used to output dates. If `--date` is not provided, the value of the `blame.date` config variable is used. If the `blame.date` config variable is also not set, the iso format is used. For supported values, see the discussion of the `--date` option at [git-log[1]](https://git-scm.com/docs/git-log). 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---progress)`--progress` 


[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---no-progress)`--no-progress` 
    
Enable progress reporting on the standard error stream even if not attached to a terminal. By default, progress status is reported only when it is attached. You can’t use `--progress` together with `--porcelain` or `--incremental`. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--Mnum)`-M`[_< num>_] 
    
Detect moved or copied lines within a file. When a commit moves or copies a block of lines (e.g. the original file has _A_ and then _B_ , and the commit changes it to _B_ and then _A_), the traditional `blame` algorithm notices only half of the movement and typically blames the lines that were moved up (i.e. _B_) to the parent and assigns blame to the lines that were moved down (i.e. _A_) to the child commit. With this option, both groups of lines are blamed on the parent by running extra passes of inspection.
_< num>_ is optional, but it is the lower bound on the number of alphanumeric characters that Git must detect as moving/copying within a file for it to associate those lines with the parent commit. The default value is 20. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--Cnum)`-C`[_< num>_] 
    
In addition to `-M`, detect lines moved or copied from other files that were modified in the same commit. This is useful when you reorganize your program and move code around across files. When this option is given twice, the command additionally looks for copies from other files in the commit that creates the file. When this option is given three times, the command additionally looks for copies from other files in any commit.
_< num>_ is optional, but it is the lower bound on the number of alphanumeric characters that Git must detect as moving/copying between files for it to associate those lines with the parent commit. And the default value is 40. If there are more than one `-C` options given, the _< num>_ argument of the last `-C` will take effect. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---ignore-revrev)`--ignore-rev` _< rev>_ 
    
Ignore changes made by the revision when assigning blame, as if the change never happened. Lines that were changed or added by an ignored commit will be blamed on the previous commit that changed that line or nearby lines. This option may be specified multiple times to ignore more than one revision. If the `blame.markIgnoredLines` config option is set, then lines that were changed by an ignored commit and attributed to another commit will be marked with a _?_ in the blame output. If the `blame.markUnblamableLines` config option is set, then those lines touched by an ignored commit that we could not attribute to another revision are marked with a `*`. In the porcelain modes, we print `ignored` and `unblamable` on a newline respectively. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---ignore-revs-filefile)`--ignore-revs-file` _< file>_ 
    
Ignore revisions listed in _< file>_, which must be in the same format as an `fsck.skipList`. This option may be repeated, and these files will be processed after any files specified with the `blame.ignoreRevsFile` config option. An empty file name, `""`, will clear the list of revs from previously processed files. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---color-lines)`--color-lines` 
    
Color line annotations in the default format differently if they come from the same commit as the preceding line. This makes it easier to distinguish code blocks introduced by different commits. The color defaults to cyan and can be adjusted using the `color.blame.repeatedLines` config option. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt---color-by-age)`--color-by-age` 
    
Color line annotations depending on the age of the line in the default format. The `color.blame.highlightRecent` config option controls what color is used for each range of age. 

[](https://git-scm.com/docs/git-annotate#Documentation/git-annotate.txt--h)`-h` 
    
Show help message.
##  [](https://git-scm.com/docs/git-annotate#_see_also)SEE ALSO
[git-blame[1]](https://git-scm.com/docs/git-blame)
##  [](https://git-scm.com/docs/git-annotate#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### annotate
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
