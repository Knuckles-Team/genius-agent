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
    * [NAME](https://git-scm.com/docs/git-blame#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-blame#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-blame#_description)
    * [OPTIONS](https://git-scm.com/docs/git-blame#_options)
    * [THE DEFAULT FORMAT](https://git-scm.com/docs/git-blame#_the_default_format)
    * [THE PORCELAIN FORMAT](https://git-scm.com/docs/git-blame#_the_porcelain_format)
    * [SPECIFYING RANGES](https://git-scm.com/docs/git-blame#_specifying_ranges)
    * [INCREMENTAL OUTPUT](https://git-scm.com/docs/git-blame#_incremental_output)
    * [MAPPING AUTHORS](https://git-scm.com/docs/git-blame#_mapping_authors)
    * [CONFIGURATION](https://git-scm.com/docs/git-blame#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-blame#_see_also)
    * [GIT](https://git-scm.com/docs/git-blame#_git)


[ English ▾](https://git-scm.com/docs/git-blame)
Localized versions of **git-blame** manual
  1. [English ](https://git-scm.com/docs/git-blame)
  2. [Français ](https://git-scm.com/docs/git-blame/fr)
  3. [日本語 ](https://git-scm.com/docs/git-blame/ja)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-blame/pt_BR)
  5. [Svenska ](https://git-scm.com/docs/git-blame/sv)
  6. [українська мова ](https://git-scm.com/docs/git-blame/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-blame/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-blame)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-blame) git-blame last updated in 2.53.0
Changes in the **git-blame** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-blame/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-blame/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-blame/2.51.0)
  5. 2.50.1 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-blame/2.50.0)
  7. 2.44.1 → 2.49.1 no changes
  8. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-blame/2.44.0)
  9. 2.43.1 → 2.43.7 no changes
  10. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-blame/2.43.0)
  11. 2.41.1 → 2.42.4 no changes
  12. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-blame/2.41.0)
  13. 2.38.1 → 2.40.4 no changes
  14. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-blame/2.38.0)
  15. 2.34.1 → 2.37.7 no changes
  16. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-blame/2.34.0)
  17. 2.31.1 → 2.33.8 no changes
  18. 2.31.0 no changes
  19. 2.30.1 → 2.30.9 no changes
  20. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-blame/2.30.0)
  21. 2.29.1 → 2.29.3 no changes
  22. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-blame/2.29.0)
  23. 2.23.1 → 2.28.1 no changes
  24. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-blame/2.23.0)
  25. 2.16.6 → 2.22.5 no changes
  26. 2.15.4 no changes
  27. 2.13.7 → 2.14.6 no changes
  28. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-blame/2.12.5)
  29. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-blame/2.11.4)
  30. 2.9.5 → 2.10.5 no changes
  31. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-blame/2.8.6)
  32. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-blame/2.7.6)
  33. 2.6.7 no changes
  34. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-blame/2.5.6)
  35. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-blame/2.4.12)
  36. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-blame/2.3.10)
  37. 2.1.4 → 2.2.3 no changes
  38. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-blame/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-blame#_name)NAME
git-blame - Show what revision and author last modified each line of a file
##  [](https://git-scm.com/docs/git-blame#_synopsis)SYNOPSIS
```
git blame [-c] [-b] [-l] [--root] [-t] [-f] [-n] [-s] [-e] [-p] [-w] [--incremental]
	  [-L _<range>_] [-S _<revs-file>_] [-M] [-C] [-C] [-C] [--since=_<date>_]
	  [--ignore-rev _<rev>_] [--ignore-revs-file _<file>_]
	  [--color-lines] [--color-by-age] [--progress] [--abbrev=_<n>_]
	  [ --contents _<file>_ ] [_<rev>_ | --reverse _<rev>_.._<rev>_] [--] _<file>_
```

##  [](https://git-scm.com/docs/git-blame#_description)DESCRIPTION
Annotates each line in the given file with information from the revision which last modified the line. Optionally, start annotating from the given revision.
When specified one or more times, `-L` restricts annotation to the requested lines.
The origin of lines is automatically followed across whole-file renames (currently there is no option to turn the rename-following off). To follow lines moved from one file to another, or to follow lines that were copied and pasted from another file, etc., see the `-C` and `-M` options.
The report does not tell you anything about lines which have been deleted or replaced; you need to use a tool such as `git` `diff` or the "pickaxe" interface briefly mentioned in the following paragraph.
Apart from supporting file annotation, Git also supports searching the development history for when a code snippet occurred in a change. This makes it possible to track when a code snippet was added to a file, moved or copied between files, and eventually deleted or replaced. It works by searching for a text string in the diff. A small example of the pickaxe interface that searches for `blame_usage`:
```
$ git log --pretty=oneline -S'blame_usage'
5040f17eba15504bad66b14a645bddd9b015ebb7 blame -S <ancestry-file>
ea4c7f9bf69e781dd0cd88d2bccb2bf5cc15c9a7 git-blame: Make the output
```

##  [](https://git-scm.com/docs/git-blame#_options)OPTIONS 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--b)`-b` 
    
Show blank SHA-1 for boundary commits. This can also be controlled via the `blame.blankBoundary` config option. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---root)`--root` 
    
Do not treat root commits as boundaries. This can also be controlled via the `blame.showRoot` config option. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---show-stats)`--show-stats` 
    
Include additional statistics at the end of blame output. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--Lstartend)`-L` _< start>_`,`_< end>_ 


[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--Lfuncname)`-L` `:`_< funcname>_ 
    
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

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--l)`-l` 
    
Show long rev (Default: off). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--t)`-t` 
    
Show raw timestamp (Default: off). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--Srevs-file)`-S` _< revs-file>_ 
    
Use revisions from _< revs-file>_ instead of calling [git-rev-list[1]](https://git-scm.com/docs/git-rev-list). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---reversestartend)`--reverse` _< start>_`..`_< end>_ 
    
Walk history forward instead of backward. Instead of showing the revision in which a line appeared, this shows the last revision in which a line has existed. This requires a range of revision like _< start>_`..`_< end>_ where the path to blame exists in _< start>_. `git` `blame` `--reverse` _< start>_ is taken as `git` `blame` `--reverse` _< start>_`..HEAD` for convenience. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---first-parent)`--first-parent` 
    
Follow only the first parent commit upon seeing a merge commit. This option can be used to determine when a line was introduced to a particular integration branch, rather than when it was introduced to the history overall. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--p)`-p` 


[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---porcelain)`--porcelain` 
    
Show in a format designed for machine consumption. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---line-porcelain)`--line-porcelain` 
    
Show the porcelain format, but output commit information for each line, not just the first time a commit is referenced. Implies `--porcelain`. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---incremental)`--incremental` 
    
Show the result incrementally in a format designed for machine consumption. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---encodingencoding)`--encoding=`_< encoding>_ 
    
Specify the encoding used to output author names and commit summaries. Setting it to `none` makes blame output unconverted data. For more information see the discussion about encoding in the [git-log[1]](https://git-scm.com/docs/git-log) manual page. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---contentsfile)`--contents` _< file>_ 
    
Annotate using the contents from _< file>_, starting from _< rev>_ if it is specified, and `HEAD` otherwise. You may specify `-` to make the command read from the standard input for the file contents. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---dateformat)`--date` _< format>_ 
    
Specify the format used to output dates. If `--date` is not provided, the value of the `blame.date` config variable is used. If the `blame.date` config variable is also not set, the iso format is used. For supported values, see the discussion of the `--date` option at [git-log[1]](https://git-scm.com/docs/git-log). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---progress)`--progress` 


[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---no-progress)`--no-progress` 
    
Enable progress reporting on the standard error stream even if not attached to a terminal. By default, progress status is reported only when it is attached. You can’t use `--progress` together with `--porcelain` or `--incremental`. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--Mnum)`-M`[_< num>_] 
    
Detect moved or copied lines within a file. When a commit moves or copies a block of lines (e.g. the original file has _A_ and then _B_ , and the commit changes it to _B_ and then _A_), the traditional `blame` algorithm notices only half of the movement and typically blames the lines that were moved up (i.e. _B_) to the parent and assigns blame to the lines that were moved down (i.e. _A_) to the child commit. With this option, both groups of lines are blamed on the parent by running extra passes of inspection.
_< num>_ is optional, but it is the lower bound on the number of alphanumeric characters that Git must detect as moving/copying within a file for it to associate those lines with the parent commit. The default value is 20. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--Cnum)`-C`[_< num>_] 
    
In addition to `-M`, detect lines moved or copied from other files that were modified in the same commit. This is useful when you reorganize your program and move code around across files. When this option is given twice, the command additionally looks for copies from other files in the commit that creates the file. When this option is given three times, the command additionally looks for copies from other files in any commit.
_< num>_ is optional, but it is the lower bound on the number of alphanumeric characters that Git must detect as moving/copying between files for it to associate those lines with the parent commit. And the default value is 40. If there are more than one `-C` options given, the _< num>_ argument of the last `-C` will take effect. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---ignore-revrev)`--ignore-rev` _< rev>_ 
    
Ignore changes made by the revision when assigning blame, as if the change never happened. Lines that were changed or added by an ignored commit will be blamed on the previous commit that changed that line or nearby lines. This option may be specified multiple times to ignore more than one revision. If the `blame.markIgnoredLines` config option is set, then lines that were changed by an ignored commit and attributed to another commit will be marked with a _?_ in the blame output. If the `blame.markUnblamableLines` config option is set, then those lines touched by an ignored commit that we could not attribute to another revision are marked with a `*`. In the porcelain modes, we print `ignored` and `unblamable` on a newline respectively. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---ignore-revs-filefile)`--ignore-revs-file` _< file>_ 
    
Ignore revisions listed in _< file>_, which must be in the same format as an `fsck.skipList`. This option may be repeated, and these files will be processed after any files specified with the `blame.ignoreRevsFile` config option. An empty file name, `""`, will clear the list of revs from previously processed files. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---color-lines)`--color-lines` 
    
Color line annotations in the default format differently if they come from the same commit as the preceding line. This makes it easier to distinguish code blocks introduced by different commits. The color defaults to cyan and can be adjusted using the `color.blame.repeatedLines` config option. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---color-by-age)`--color-by-age` 
    
Color line annotations depending on the age of the line in the default format. The `color.blame.highlightRecent` config option controls what color is used for each range of age. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--h)`-h` 
    
Show help message. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--c)`-c` 
    
Use the same output mode as [git-annotate[1]](https://git-scm.com/docs/git-annotate) (Default: off). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---score-debug)`--score-debug` 
    
Include debugging information related to the movement of lines between files (see `-C`) and lines moved within a file (see `-M`). The first number listed is the score. This is the number of alphanumeric characters detected as having been moved between or within files. This must be above a certain threshold for `git` `blame` to consider those lines of code to have been moved. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--f)`-f` 


[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---show-name)`--show-name` 
    
Show the filename in the original commit. By default the filename is shown if there is any line that came from a file with a different name, due to rename detection. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--n)`-n` 


[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---show-number)`--show-number` 
    
Show the line number in the original commit (Default: off). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--s)`-s` 
    
Suppress the author name and timestamp from the output. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--e)`-e` 


[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---show-email)`--show-email` 
    
Show the author email instead of the author name (Default: off). This can also be controlled via the `blame.showEmail` config option. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt--w)`-w` 
    
Ignore whitespace when comparing the parent’s version and the child’s to find where the lines came from. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---diff-algorithmpatienceminimalhistogrammyers)`--diff-algorithm=`(`patience`|`minimal`|`histogram`|`myers`) 
    
Choose a diff algorithm. The variants are as follows: 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-default)`default` 


[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-myers)`myers` 
    
The basic greedy diff algorithm. Currently, this is the default. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-minimal)`minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-patience)`patience` 
    
Use "patience diff" algorithm when generating patches. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-histogram)`histogram` 
    
This algorithm extends the patience algorithm to "support low-occurrence common elements".
For instance, if you configured the `diff.algorithm` variable to a non-default value and want to use the default one, then you have to use `--diff-algorithm=default` option. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---abbrevn)`--abbrev=`_< n>_ 
    
Instead of using the default _7+1_ hexadecimal digits as the abbreviated object name, use _< m>+1_ digits, where _< m>_ is at least _< n>_ but ensures the commit object names are unique. Note that 1 column is used for a caret to mark the boundary commit.
##  [](https://git-scm.com/docs/git-blame#_the_default_format)THE DEFAULT FORMAT
When neither `--porcelain` nor `--incremental` option is specified, `git` `blame` will output annotation for each line with:
  * abbreviated object name for the commit the line came from;
  * author ident (by default the author name and date, unless `-s` or `-e` is specified); and
  * line number


before the line contents.
##  [](https://git-scm.com/docs/git-blame#_the_porcelain_format)THE PORCELAIN FORMAT
In this format, each line is output after a header; the header at the minimum has the first line which has:
  * 40-byte SHA-1 of the commit the line is attributed to;
  * the line number of the line in the original file;
  * the line number of the line in the final file;
  * on a line that starts a group of lines from a different commit than the previous one, the number of lines in this group. On subsequent lines this field is absent.


This header line is followed by the following information at least once for each commit:
  * the author name (`author`), email (`author-mail`), time (`author-time`), and time zone (`author-tz`); similarly for committer.
  * the filename in the commit that the line is attributed to.
  * the first line of the commit log message (`summary`).


The contents of the actual line are output after the above header, prefixed by a _TAB_. This is to allow adding more header elements later.
The porcelain format generally suppresses commit information that has already been seen. For example, two lines that are blamed to the same commit will both be shown, but the details for that commit will be shown only once. Information which is specific to individual lines will not be grouped together, like revs to be marked `ignored` or `unblamable`. This is more efficient, but may require more state be kept by the reader. The `--line-porcelain` option can be used to output full commit information for each line, allowing simpler (but less efficient) usage like:
```
# count the number of lines attributed to each author
git blame --line-porcelain file |
sed -n 's/^author //p' |
sort | uniq -c | sort -rn
```

##  [](https://git-scm.com/docs/git-blame#_specifying_ranges)SPECIFYING RANGES
Unlike `git` `blame` and `git` `annotate` in older versions of git, the extent of the annotation can be limited to both line ranges and revision ranges. The `-L` option, which limits annotation to a range of lines, may be specified multiple times.
When you are interested in finding the origin for lines 40-60 for file `foo`, you can use the `-L` option like so (they mean the same thing — both ask for 21 lines starting at line 40):
```
git blame -L 40,60 foo
git blame -L 40,+21 foo
```

Also you can use a regular expression to specify the line range:
```
git blame -L '/^sub hello {/,/^}$/' foo
```

which limits the annotation to the body of the `hello` subroutine.
When you are not interested in changes older than version v2.6.18, or changes older than 3 weeks, you can use revision range specifiers similar to `git` `rev-list`:
```
git blame v2.6.18.. -- foo
git blame --since=3.weeks -- foo
```

When revision range specifiers are used to limit the annotation, lines that have not changed since the range boundary (either the commit v2.6.18 or the most recent commit that is more than 3 weeks old in the above example) are blamed for that range boundary commit.
A particularly useful way is to see if an added file has lines created by copy-and-paste from existing files. Sometimes this indicates that the developer was being sloppy and did not refactor the code properly. You can first find the commit that introduced the file with:
```
git log --diff-filter=A --pretty=short -- foo
```

and then annotate the change between the commit and its parents, using `commit^!` notation:
```
git blame -C -C -f $commit^! -- foo
```

##  [](https://git-scm.com/docs/git-blame#_incremental_output)INCREMENTAL OUTPUT
When called with `--incremental` option, the command outputs the result as it is built. The output generally will talk about lines touched by more recent commits first (i.e. the lines will be annotated out of order) and is meant to be used by interactive viewers.
The output format is similar to the Porcelain format, but it does not contain the actual lines from the file that is being annotated.
  1. Each blame entry always starts with a line of:
```
_<40-byte-hex-sha1>_ _<sourceline>_ _<resultline>_ _<num-lines>_
```

Line numbers count from 1.
  2. The first time that a commit shows up in the stream, it has various other information about it printed out with a one-word tag at the beginning of each line describing the extra commit information (author, email, committer, dates, summary, etc.).
  3. Unlike the Porcelain format, the filename information is always given and terminates the entry:
```
filename _<whitespace-quoted-filename-goes-here>_
```

and thus it is really quite easy to parse for some line- and word-oriented parser (which should be quite natural for most scripting languages).
Note |  For people who do parsing: to make it more robust, just ignore any lines between the first and last one (_< 40-byte-hex-sha1>_ and `filename` lines) where you do not recognize the tag words (or care about that particular one) at the beginning of the "extended information" lines. That way, if there is ever added information (like the commit encoding or extended commit commentary), a blame viewer will not care.   
---|---  


##  [](https://git-scm.com/docs/git-blame#_mapping_authors)MAPPING AUTHORS
See [gitmailmap[5]](https://git-scm.com/docs/gitmailmap).
##  [](https://git-scm.com/docs/git-blame#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blameblankBoundary)blame.blankBoundary 
    
Show blank commit object name for boundary commits in [git-blame[1]](https://git-scm.com/docs/git-blame). This option defaults to false. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blamecoloring)blame.coloring 
    
This determines the coloring scheme to be applied to blame output. It can be _repeatedLines_ , _highlightRecent_ , or _none_ which is the default. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blamedate)blame.date 
    
Specifies the format used to output dates in [git-blame[1]](https://git-scm.com/docs/git-blame). If unset the iso format is used. For supported values, see the discussion of the `--date` option at [git-log[1]](https://git-scm.com/docs/git-log). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blameshowEmail)blame.showEmail 
    
Show the author email instead of author name in [git-blame[1]](https://git-scm.com/docs/git-blame). This option defaults to false. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blameshowRoot)blame.showRoot 
    
Do not treat root commits as boundaries in [git-blame[1]](https://git-scm.com/docs/git-blame). This option defaults to false. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blameignoreRevsFile)blame.ignoreRevsFile 
    
Ignore revisions listed in the file, one unabbreviated object name per line, in [git-blame[1]](https://git-scm.com/docs/git-blame). Whitespace and comments beginning with `#` are ignored. This option may be repeated multiple times. Empty file names will reset the list of ignored revisions. This option will be handled before the command line option `--ignore-revs-file`. 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blamemarkUnblamableLines)blame.markUnblamableLines 
    
Mark lines that were changed by an ignored revision that we could not attribute to another commit with a _*_ in the output of [git-blame[1]](https://git-scm.com/docs/git-blame). 

[](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt-blamemarkIgnoredLines)blame.markIgnoredLines 
    
Mark lines that were changed by an ignored revision that we attributed to another commit with a _?_ in the output of [git-blame[1]](https://git-scm.com/docs/git-blame).
##  [](https://git-scm.com/docs/git-blame#_see_also)SEE ALSO
[git-annotate[1]](https://git-scm.com/docs/git-annotate)
##  [](https://git-scm.com/docs/git-blame#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### blame
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
