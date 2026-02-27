[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --everything-is-local
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
    * [NAME](https://git-scm.com/docs/git-cat-file#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-cat-file#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-cat-file#_description)
    * [OPTIONS](https://git-scm.com/docs/git-cat-file#_options)
    * [OUTPUT](https://git-scm.com/docs/git-cat-file#_output)
    * [BATCH OUTPUT](https://git-scm.com/docs/git-cat-file#_batch_output)
    * [CAVEATS](https://git-scm.com/docs/git-cat-file#_caveats)
    * [GIT](https://git-scm.com/docs/git-cat-file#_git)


[ English ▾](https://git-scm.com/docs/git-cat-file)
Localized versions of **git-cat-file** manual
  1. [English ](https://git-scm.com/docs/git-cat-file)
  2. [Français ](https://git-scm.com/docs/git-cat-file/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-cat-file/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-cat-file/sv)
  5. [українська мова ](https://git-scm.com/docs/git-cat-file/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-cat-file/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-cat-file)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-cat-file) git-cat-file last updated in 2.52.0
Changes in the **git-cat-file** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-cat-file/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-cat-file/2.51.0)
  5. 2.50.1 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-cat-file/2.50.0)
  7. 2.46.2 → 2.49.1 no changes
  8. [2.46.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-13_ ](https://git-scm.com/docs/git-cat-file/2.46.1)
  9. 2.42.2 → 2.46.0 no changes
  10. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-cat-file/2.42.1)
  11. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-cat-file/2.42.0)
  12. 2.40.1 → 2.41.3 no changes
  13. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-cat-file/2.40.0)
  14. 2.38.1 → 2.39.5 no changes
  15. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-cat-file/2.38.0)
  16. 2.36.1 → 2.37.7 no changes
  17. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-cat-file/2.36.0)
  18. 2.34.1 → 2.35.8 no changes
  19. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-cat-file/2.34.0)
  20. 2.32.1 → 2.33.8 no changes
  21. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-cat-file/2.32.0)
  22. 2.28.1 → 2.31.8 no changes
  23. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-cat-file/2.28.0)
  24. 2.21.1 → 2.27.1 no changes
  25. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-cat-file/2.21.0)
  26. 2.19.1 → 2.20.5 no changes
  27. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-cat-file/2.19.0)
  28. 2.17.0 → 2.18.5 no changes
  29. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-cat-file/2.16.6)
  30. 2.15.4 no changes
  31. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-cat-file/2.14.6)
  32. 2.12.5 → 2.13.7 no changes
  33. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-cat-file/2.11.4)
  34. 2.10.5 no changes
  35. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-cat-file/2.9.5)
  36. 2.7.6 → 2.8.6 no changes
  37. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-cat-file/2.6.7)
  38. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-cat-file/2.5.6)
  39. 2.1.4 → 2.4.12 no changes
  40. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-cat-file/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-cat-file#_name)NAME
git-cat-file - Provide contents or details of repository objects
##  [](https://git-scm.com/docs/git-cat-file#_synopsis)SYNOPSIS
```
_git cat-file_ <type> <object>
_git cat-file_ (-e | -p | -t | -s) <object>
_git cat-file_ (--textconv | --filters)
	     [<rev>:<path|tree-ish> | --path=<path|tree-ish> <rev>]
_git cat-file_ (--batch | --batch-check | --batch-command) [--batch-all-objects]
	     [--buffer] [--follow-symlinks] [--unordered]
	     [--textconv | --filters] [-Z]
```

##  [](https://git-scm.com/docs/git-cat-file#_description)DESCRIPTION
Output the contents or other properties such as size, type or delta information of one or more objects.
This command can operate in two modes, depending on whether an option from the `--batch` family is specified.
In non-batch mode, the command provides information on an object named on the command line.
In batch mode, arguments are read from standard input.
##  [](https://git-scm.com/docs/git-cat-file#_options)OPTIONS 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-object)<object> 
    
The name of the object to show. For a more complete list of ways to spell object names, see the "SPECIFYING REVISIONS" section in [gitrevisions[7]](https://git-scm.com/docs/gitrevisions). 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--t)-t 
    
Instead of the content, show the object type identified by _< object>_. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--s)-s 
    
Instead of the content, show the object size identified by _< object>_. If used with `--use-mailmap` option, will show the size of updated object after replacing idents using the mailmap mechanism. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--e)-e 
    
Exit with zero status if _< object>_ exists and is a valid object. If _< object>_ is of an invalid format, exit with non-zero status and emit an error on stderr. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--p)-p 
    
Pretty-print the contents of _< object>_ based on its type. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-type)<type> 
    
Typically this matches the real type of _< object>_ but asking for a type that can trivially be dereferenced from the given _< object>_ is also permitted. An example is to ask for a "tree" with _< object>_ being a commit object that contains it, or to ask for a "blob" with _< object>_ being a tag object that points at it. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---mailmap)--mailmap 


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---no-mailmap)--no-mailmap 


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---use-mailmap)--use-mailmap 


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---no-use-mailmap)--no-use-mailmap 
    
Use mailmap file to map author, committer and tagger names and email addresses to canonical real names and email addresses. See [git-shortlog[1]](https://git-scm.com/docs/git-shortlog). 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---textconv)--textconv 
    
Show the content as transformed by a textconv filter. In this case, _< object>_ has to be of the form _< tree-ish>_`:`_< path>_, or `:`_< path>_ in order to apply the filter to the content recorded in the index at _< path>_. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---filters)--filters 
    
Show the content as converted by the filters configured in the current working tree for the given _< path>_ (i.e. smudge filters, end-of-line conversion, etc). In this case, _< object>_ has to be of the form _< tree-ish>_`:`_< path>_, or `:`_< path>_. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---filterfilter-spec)--filter=<filter-spec> 


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---no-filter)--no-filter 
    
Omit objects from the list of printed objects. This can only be used in combination with one of the batched modes. Excluded objects that have been explicitly requested via any of the batch modes that read objects via standard input (`--batch`, `--batch-check`) will be reported as "filtered". Excluded objects in `--batch-all-objects` mode will not be printed at all. The _< filter-spec>_ may be one of the following:
The form _--filter=blob:none_ omits all blobs.
The form _--filter=blob:limit= <n>[kmg]_ omits blobs of size at least n bytes or units. n may be zero. The suffixes k, m, and g can be used to name units in KiB, MiB, or GiB. For example, _blob:limit=1k_ is the same as _blob:limit=1024_.
The form _--filter=object:type=(tag|commit|tree|blob)_ omits all objects which are not of the requested type. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---pathpath)--path=<path> 
    
For use with `--textconv` or `--filters`, to allow specifying an object name and a path separately, e.g. when it is difficult to figure out the revision from which the blob came. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---batch)--batch 


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---batchformat)--batch=<format> 
    
Print object information and contents for each object provided on stdin. May not be combined with any other options or arguments except `--textconv`, `--filters`, or `--use-mailmap`.
  * When used with `--textconv` or `--filters`, the input lines must specify the path, separated by whitespace. See the section `BATCH` `OUTPUT` below for details.
  * When used with `--use-mailmap`, for commit and tag objects, the contents part of the output shows the identities replaced using the mailmap mechanism, while the information part of the output shows the size of the object as if it actually recorded the replacement identities.



[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---batch-check)--batch-check 


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---batch-checkformat)--batch-check=<format> 
    
Print object information for each object provided on stdin. May not be combined with any other options or arguments except `--textconv`, `--filters` or `--use-mailmap`.
  * When used with `--textconv` or `--filters`, the input lines must specify the path, separated by whitespace. See the section `BATCH` `OUTPUT` below for details.
  * When used with `--use-mailmap`, for commit and tag objects, the printed object information shows the size of the object as if the identities recorded in it were replaced by the mailmap mechanism.



[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---batch-command)--batch-command 


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---batch-commandformat)--batch-command=<format> 
    
Enter a command mode that reads commands and arguments from stdin. May only be combined with `--buffer`, `--textconv`, `--use-mailmap` or `--filters`.
  * When used with `--textconv` or `--filters`, the input lines must specify the path, separated by whitespace. See the section `BATCH` `OUTPUT` below for details.
  * When used with `--use-mailmap`, for commit and tag objects, the `contents` command shows the identities replaced using the mailmap mechanism, while the `info` command shows the size of the object as if it actually recorded the replacement identities.


`--batch-command` recognizes the following commands: 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-contentsobject)contents <object> 
    
Print object contents for object reference _< object>_. This corresponds to the output of `--batch`. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-infoobject)info <object> 
    
Print object info for object reference _< object>_. This corresponds to the output of `--batch-check`. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-flush)flush 
    
Used with `--buffer` to execute all preceding commands that were issued since the beginning or since the last flush was issued. When `--buffer` is used, no output will come until a `flush` is issued. When `--buffer` is not used, commands are flushed each time without issuing `flush`. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---batch-all-objects)--batch-all-objects 
    
Instead of reading a list of objects on stdin, perform the requested batch operation on all objects in the repository and any alternate object stores (not just reachable objects). Requires `--batch` or `--batch-check` be specified. By default, the objects are visited in order sorted by their hashes; see also `--unordered` below. Objects are presented as-is, without respecting the "replace" mechanism of [git-replace[1]](https://git-scm.com/docs/git-replace). 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---buffer)--buffer 
    
Normally batch output is flushed after each object is output, so that a process can interactively read and write from `cat-file`. With this option, the output uses normal stdio buffering; this is much more efficient when invoking `--batch-check` or `--batch-command` on a large number of objects. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---unordered)--unordered 
    
When `--batch-all-objects` is in use, visit objects in an order which may be more efficient for accessing the object contents than hash order. The exact details of the order are unspecified, but if you do not require a specific order, this should generally result in faster output, especially with `--batch`. Note that `cat-file` will still show each object only once, even if it is stored multiple times in the repository. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt---follow-symlinks)--follow-symlinks 
    
With `--batch` or `--batch-check`, follow symlinks inside the repository when requesting objects with extended SHA-1 expressions of the form tree-ish:path-in-tree. Instead of providing output about the link itself, provide output about the linked-to object. If a symlink points outside the tree-ish (e.g. a link to `/foo` or a root-level link to `../foo`), the portion of the link which is outside the tree will be printed.
This option does not (currently) work correctly when an object in the index is specified (e.g. `:link` instead of `HEAD:link`) rather than one in the tree.
This option cannot (currently) be used unless `--batch` or `--batch-check` is used.
For example, consider a git repository containing:
```
f: a file containing "hello\n"
link: a symlink to f
dir/link: a symlink to ../f
plink: a symlink to ../f
alink: a symlink to /etc/passwd
```

For a regular file `f`, `echo` `HEAD:f` | `git` `cat-file` `--batch` would print
```
ce013625030ba8dba906f756967f9e9ca394464a blob 6
```

And `echo` `HEAD:link` | `git` `cat-file` `--batch` `--follow-symlinks` would print the same thing, as would `HEAD:dir/link`, as they both point at `HEAD:f`.
Without `--follow-symlinks`, these would print data about the symlink itself. In the case of `HEAD:link`, you would see
```
4d1ae35ba2c8ec712fa2a379db44ad639ca277bd blob 1
```

Both `plink` and `alink` point outside the tree, so they would respectively print:
```
symlink 4
../f
```

```
symlink 11
/etc/passwd
```


[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--Z)-Z 
    
Only meaningful with `--batch`, `--batch-check`, or `--batch-command`; input and output is NUL-delimited instead of newline-delimited. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--z)-z 
    
Only meaningful with `--batch`, `--batch-check`, or `--batch-command`; input is NUL-delimited instead of newline-delimited. This option is deprecated in favor of `-Z` as the output can otherwise be ambiguous.
##  [](https://git-scm.com/docs/git-cat-file#_output)OUTPUT
If `-t` is specified, one of the _< type>_.
If `-s` is specified, the size of the _< object>_ in bytes.
If `-e` is specified, no output, unless the _< object>_ is malformed.
If `-p` is specified, the contents of _< object>_ are pretty-printed.
If _< type>_ is specified, the raw (though uncompressed) contents of the _< object>_ will be returned.
##  [](https://git-scm.com/docs/git-cat-file#_batch_output)BATCH OUTPUT
If `--batch` or `--batch-check` is given, `cat-file` will read objects from stdin, one per line, and print information about them in the same order as they have been read. By default, the whole line is considered as an object, as if it were fed to [git-rev-parse[1]](https://git-scm.com/docs/git-rev-parse).
When `--batch-command` is given, `cat-file` will read commands from stdin, one per line, and print information based on the command given. With `--batch-command`, the `info` command followed by an object will print information about the object the same way `--batch-check` would, and the `contents` command followed by an object prints contents in the same way `--batch` would.
You can specify the information shown for each object by using a custom _< format>_. The _< format>_ is copied literally to stdout for each object, with placeholders of the form `%`(`atom`) expanded, followed by a newline. The available atoms are: 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-objectname)`objectname` 
    
The full hex representation of the object name. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-objecttype)`objecttype` 
    
The type of the object (the same as `cat-file` `-t` reports). 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-objectmode)`objectmode` 
    
If the specified object has mode information (such as a tree or index entry), the mode expressed as an octal integer. Otherwise, empty string. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-objectsize)`objectsize` 
    
The size, in bytes, of the object (the same as `cat-file` `-s` reports). 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-objectsizedisk)`objectsize:disk` 
    
The size, in bytes, that the object takes up on disk. See the note about on-disk sizes in the `CAVEATS` section below. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-deltabase)`deltabase` 
    
If the object is stored as a delta on-disk, this expands to the full hex representation of the delta base object name. Otherwise, expands to the null OID (all zeroes). See `CAVEATS` below. 

[](https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt-rest)`rest` 
    
If this atom is used in the output string, input lines are split at the first whitespace boundary. All characters before that whitespace are considered to be the object name; characters after that first run of whitespace (i.e., the "rest" of the line) are output in place of the `%`(`rest`) atom.
If no format is specified, the default format is `%`(`objectname`) `%`(`objecttype`) `%`(`objectsize`).
If `--batch` is specified, or if `--batch-command` is used with the `contents` command, the object information is followed by the object contents (consisting of `%`(`objectsize`) bytes), followed by a newline.
For example, `--batch` without a custom format would produce:
```
<oid> SP <type> SP <size> LF
<contents> LF
```

Whereas `--batch-check='%`(`objectname`) `%`(`objecttype`) would produce:
```
<oid> SP <type> LF
```

If a name is specified on stdin that cannot be resolved to an object in the repository, then `cat-file` will ignore any custom format and print:
```
<object> SP missing LF
```

If a name is specified on stdin that is filtered out via `--filter=`, then `cat-file` will ignore any custom format and print:
```
<object> SP excluded LF
```

If a name is specified that might refer to more than one object (an ambiguous short sha), then `cat-file` will ignore any custom format and print:
```
<object> SP ambiguous LF
```

If a name is specified that refers to a submodule entry in a tree and the target object does not exist in the repository, then `cat-file` will ignore any custom format and print (with the object ID of the submodule):
```
<oid> SP submodule LF
```

If `--follow-symlinks` is used, and a symlink in the repository points outside the repository, then `cat-file` will ignore any custom format and print:
```
symlink SP <size> LF
<symlink> LF
```

The symlink will either be absolute (beginning with a `/`), or relative to the tree root. For instance, if dir/link points to `../../foo`, then _< symlink>_ will be `../foo`. _< size>_ is the size of the symlink in bytes.
If `--follow-symlinks` is used, the following error messages will be displayed:
```
<object> SP missing LF
```

is printed when the initial symlink requested does not exist.
```
dangling SP <size> LF
<object> LF
```

is printed when the initial symlink exists, but something that it (transitive-of) points to does not.
```
loop SP <size> LF
<object> LF
```

is printed for symlink loops (or any symlinks that require more than 40 link resolutions to resolve).
```
notdir SP <size> LF
<object> LF
```

is printed when, during symlink resolution, a file is used as a directory name.
Alternatively, when `-Z` is passed, the line feeds in any of the above examples are replaced with NUL terminators. This ensures that output will be parsable if the output itself would contain a linefeed and is thus recommended for scripting purposes.
##  [](https://git-scm.com/docs/git-cat-file#_caveats)CAVEATS
Note that the sizes of objects on disk are reported accurately, but care should be taken in drawing conclusions about which refs or objects are responsible for disk usage. The size of a packed non-delta object may be much larger than the size of objects which delta against it, but the choice of which object is the base and which is the delta is arbitrary and is subject to change during a repack.
Note also that multiple copies of an object may be present in the object database; in this case, it is undefined which copy’s size or delta base will be reported.
##  [](https://git-scm.com/docs/git-cat-file#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### cat-file
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
