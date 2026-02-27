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
    * [NAME](https://git-scm.com/docs/git-am#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-am#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-am#_description)
    * [OPTIONS](https://git-scm.com/docs/git-am#_options)
    * [DISCUSSION](https://git-scm.com/docs/git-am#_discussion)
    * [HOOKS](https://git-scm.com/docs/git-am#_hooks)
    * [CONFIGURATION](https://git-scm.com/docs/git-am#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-am#_see_also)
    * [GIT](https://git-scm.com/docs/git-am#_git)


[ English ▾](https://git-scm.com/docs/git-am)
Localized versions of **git-am** manual
  1. [English ](https://git-scm.com/docs/git-am)
  2. [Français ](https://git-scm.com/docs/git-am/fr)
  3. [日本語 ](https://git-scm.com/docs/git-am/ja)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-am/pt_BR)
  5. [Svenska ](https://git-scm.com/docs/git-am/sv)
  6. [українська мова ](https://git-scm.com/docs/git-am/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-am/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-am)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-am) git-am last updated in 2.53.0
Changes in the **git-am** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-am/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-am/2.52.0)
  3. 2.50.1 → 2.51.2 no changes
  4. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-am/2.50.0)
  5. 2.46.1 → 2.49.1 no changes
  6. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-am/2.46.0)
  7. 2.45.1 → 2.45.4 no changes
  8. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-am/2.45.0)
  9. 2.43.1 → 2.44.4 no changes
  10. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-am/2.43.0)
  11. 2.42.2 → 2.42.4 no changes
  12. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-am/2.42.1)
  13. 2.41.1 → 2.42.0 no changes
  14. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-am/2.41.0)
  15. 2.40.1 → 2.40.4 no changes
  16. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-am/2.40.0)
  17. 2.38.1 → 2.39.5 no changes
  18. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-am/2.38.0)
  19. 2.35.1 → 2.37.7 no changes
  20. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-am/2.35.0)
  21. 2.33.2 → 2.34.8 no changes
  22. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git-am/2.33.1)
  23. 2.32.1 → 2.33.0 no changes
  24. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-am/2.32.0)
  25. 2.31.1 → 2.31.8 no changes
  26. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-am/2.31.0)
  27. 2.30.1 → 2.30.9 no changes
  28. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-am/2.30.0)
  29. 2.27.1 → 2.29.3 no changes
  30. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-am/2.27.0)
  31. 2.26.1 → 2.26.3 no changes
  32. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-am/2.26.0)
  33. 2.25.1 → 2.25.5 no changes
  34. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-am/2.25.0)
  35. 2.22.1 → 2.24.4 no changes
  36. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-am/2.22.0)
  37. 2.17.1 → 2.21.4 no changes
  38. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-am/2.17.0)
  39. 2.11.4 → 2.16.6 no changes
  40. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-am/2.10.5)
  41. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-am/2.9.5)
  42. 2.8.6 no changes
  43. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-am/2.7.6)
  44. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-am/2.6.7)
  45. 2.4.12 → 2.5.6 no changes
  46. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-am/2.3.10)
  47. 2.2.3 no changes
  48. 2.1.4 no changes
  49. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-am/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-am#_name)NAME
git-am - Apply a series of patches from a mailbox
##  [](https://git-scm.com/docs/git-am#_synopsis)SYNOPSIS
```
_git am_ [--signoff] [--keep] [--[no-]keep-cr] [--[no-]utf8] [--no-verify]
	 [--[no-]3way] [--interactive] [--committer-date-is-author-date]
	 [--ignore-date] [--ignore-space-change | --ignore-whitespace]
	 [--whitespace=<action>] [-C<n>] [-p<n>] [--directory=<dir>]
	 [--exclude=<path>] [--include=<path>] [--reject] [-q | --quiet]
	 [--[no-]scissors] [-S[<keyid>]] [--patch-format=<format>]
	 [--quoted-cr=<action>]
	 [--empty=(stop|drop|keep)]
	 [(<mbox> | <Maildir>)…​]
_git am_ (--continue | --skip | --abort | --quit | --retry | --show-current-patch[=(diff|raw)] | --allow-empty)
```

##  [](https://git-scm.com/docs/git-am#_description)DESCRIPTION
Splits mail messages in a mailbox into commit log messages, authorship information, and patches, and applies them to the current branch. You could think of it as a reverse operation of [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) run on a branch with a straight history without merges.
##  [](https://git-scm.com/docs/git-am#_options)OPTIONS 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt-mboxMaildir)(<mbox>|<Maildir>)…​ 
    
The list of mailbox files to read patches from. If you do not supply this argument, the command reads from the standard input. If you supply directories, they will be treated as Maildirs. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--s)-s 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---signoff)--signoff 
    
Add a `Signed-off-by` trailer to the commit message, using the committer identity of yourself. See the signoff option in [git-commit[1]](https://git-scm.com/docs/git-commit) for more information. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--k)-k 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---keep)--keep 
    
Pass `-k` flag to _git mailinfo_ (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---keep-non-patch)--keep-non-patch 
    
Pass `-b` flag to _git mailinfo_ (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---keep-cr)--keep-cr 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-keep-cr)--no-keep-cr 
    
With `--keep-cr`, call _git mailsplit_ (see [git-mailsplit[1]](https://git-scm.com/docs/git-mailsplit)) with the same option, to prevent it from stripping CR at the end of lines. `am.keepcr` configuration variable can be used to specify the default behaviour. `--no-keep-cr` is useful to override `am.keepcr`. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--c)-c 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---scissors)--scissors 
    
Remove everything in body before a scissors line (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)). Can be activated by default using the `mailinfo.scissors` configuration variable. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-scissors)--no-scissors 
    
Ignore scissors lines (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---quoted-craction)--quoted-cr=<action> 
    
This flag will be passed down to _git mailinfo_ (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---emptydropkeepstop)--empty=(drop|keep|stop) 
    
How to handle an e-mail message lacking a patch: 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt-drop)`drop` 
    
The e-mail message will be skipped. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt-keep)`keep` 
    
An empty commit will be created, with the contents of the e-mail message as its log. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt-stop)`stop` 
    
The command will fail, stopping in the middle of the current `am` session. This is the default behavior. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--m)-m 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---message-id)--message-id 
    
Pass the `-m` flag to _git mailinfo_ (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)), so that the Message-ID header is added to the commit message. The `am.messageid` configuration variable can be used to specify the default behaviour. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-message-id)--no-message-id 
    
Do not add the Message-ID header to the commit message. `no-message-id` is useful to override `am.messageid`. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--q)-q 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---quiet)--quiet 
    
Be quiet. Only print error messages. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--u)-u 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---utf8)--utf8 
    
Pass `-u` flag to _git mailinfo_ (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)). The proposed commit log message taken from the e-mail is re-coded into UTF-8 encoding (configuration variable `i18n.commitEncoding` can be used to specify the project’s preferred encoding if it is not UTF-8).
This was optional in prior versions of git, but now it is the default. You can use `--no-utf8` to override this. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-utf8)--no-utf8 
    
Pass `-n` flag to _git mailinfo_ (see [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo)). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--3)-3 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---3way)--3way 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-3way)--no-3way 
    
When the patch does not apply cleanly, fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally. `--no-3way` can be used to override am.threeWay configuration variable. For more information, see am.threeWay in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---rerere-autoupdate)`--rerere-autoupdate` 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-rerere-autoupdate)`--no-rerere-autoupdate` 
    
After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update the index with the result of resolution. `--no-rerere-autoupdate` is a good way to double-check what `rerere` did and catch potential mismerges, before committing the result to the index with a separate `git` `add`. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---ignore-space-change)--ignore-space-change 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---ignore-whitespace)--ignore-whitespace 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---whitespaceaction)--whitespace=<action> 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--Cn)-C<n> 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--pn)-p<n> 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---directorydir)--directory=<dir> 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---excludepath)--exclude=<path> 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---includepath)--include=<path> 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---reject)--reject 
    
These flags are passed to the _git apply_ (see [git-apply[1]](https://git-scm.com/docs/git-apply)) program that applies the patch.
Valid <action> for the `--whitespace` option are: `nowarn`, `warn`, `fix`, `error`, and `error-all`. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---patch-format)--patch-format 
    
By default the command will try to detect the patch format automatically. This option allows the user to bypass the automatic detection and specify the patch format that the patch(es) should be interpreted as. Valid formats are mbox, mboxrd, stgit, stgit-series, and hg. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--i)-i 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---interactive)--interactive 
    
Run interactively. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--n)-n 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-verify)--no-verify 
    
By default, the pre-applypatch and applypatch-msg hooks are run. When any of `--no-verify` or `-n` is given, these are bypassed. See also [githooks[5]](https://git-scm.com/docs/githooks). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---committer-date-is-author-date)--committer-date-is-author-date 
    
By default the command records the date from the e-mail message as the commit author date, and uses the time of commit creation as the committer date. This allows the user to lie about the committer date by using the same value as the author date.
Warning |  The history walking machinery assumes that commits have non-decreasing commit timestamps. You should consider if you really need to use this option. Then you should only use this option to override the committer date when applying commits on top of a base which commit is older (in terms of the commit date) than the oldest patch you are applying.   
---|--- 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---ignore-date)--ignore-date 
      
By default the command records the date from the e-mail message as the commit author date, and uses the time of commit creation as the committer date. This allows the user to lie about the author date by using the same value as the committer date. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---skip)--skip 
    
Skip the current patch. This is only meaningful when restarting an aborted patch. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--Skeyid)-S[<keyid>] 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---gpg-signkeyid)--gpg-sign[=<keyid>] 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---no-gpg-sign)--no-gpg-sign 
    
GPG-sign commits. The `keyid` argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---continue)--continue 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt--r)-r 


[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---resolved)--resolved 
    
After a patch failure (e.g. attempting to apply conflicting patch), the user has applied it by hand and the index file stores the result of the application. Make a commit using the authorship and commit log extracted from the e-mail message and the current index file, and continue. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---resolvemsgmsg)--resolvemsg=<msg> 
    
When a patch failure occurs, <msg> will be printed to the screen before exiting. This overrides the standard message informing you to use `--continue` or `--skip` to handle the failure. This is solely for internal use between _git rebase_ and _git am_. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---abort)--abort 
    
Restore the original branch and abort the patching operation. Revert the contents of files involved in the am operation to their pre-am state. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---quit)--quit 
    
Abort the patching operation but keep HEAD and the index untouched. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---retry)--retry 
    
Try to apply the last conflicting patch again. This is generally only useful for passing extra options to the retry attempt (e.g., `--3way`), since otherwise you’ll just see the same failure again. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---show-current-patchdiffraw)--show-current-patch[=(diff|raw)] 
    
Show the message at which `git` `am` has stopped due to conflicts. If `raw` is specified, show the raw contents of the e-mail message; if `diff`, show the diff portion only. Defaults to `raw`. 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt---allow-empty)--allow-empty 
    
After a patch failure on an input e-mail message lacking a patch, create an empty commit with the contents of the e-mail message as its log message.
##  [](https://git-scm.com/docs/git-am#_discussion)DISCUSSION
The commit author name is taken from the "From: " line of the message, and commit author date is taken from the "Date: " line of the message. The "Subject: " line is used as the title of the commit, after stripping common prefix "[PATCH <anything>]". The "Subject: " line is supposed to concisely describe what the commit is about in one line of text.
"From: ", "Date: ", and "Subject: " lines starting the body override the respective commit author name and title values taken from the headers.
The commit message is formed by the title taken from the "Subject: ", a blank line and the body of the message up to where the patch begins. Excess whitespace at the end of each line is automatically stripped.
The patch is expected to be inline, directly following the message. Any line that is of the form:
  * three-dashes and end-of-line, or
  * a line that begins with "diff -", or
  * a line that begins with "Index: "


is taken as the beginning of a patch, and the commit log message is terminated before the first occurrence of such a line.
When initially invoking `git` `am`, you give it the names of the mailboxes to process. Upon seeing the first patch that does not apply, it aborts in the middle. You can recover from this in one of two ways:
  1. skip the current patch by re-running the command with the `--skip` option.
  2. hand resolve the conflict in the working directory, and update the index file to bring it into a state that the patch should have produced. Then run the command with the `--continue` option.


The command refuses to process new mailboxes until the current operation is finished, so if you decide to start over from scratch, run `git` `am` `--abort` before running the command with mailbox names.
Before any patches are applied, ORIG_HEAD is set to the tip of the current branch. This is useful if you have problems with multiple commits, like running _git am_ on the wrong branch or an error in the commits that is more easily fixed by changing the mailbox (e.g. errors in the "From:" lines).
##  [](https://git-scm.com/docs/git-am#_hooks)HOOKS
This command can run `applypatch-msg`, `pre-applypatch`, and `post-applypatch` hooks. See [githooks[5]](https://git-scm.com/docs/githooks) for more information.
##  [](https://git-scm.com/docs/git-am#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt-amkeepcr)am.keepcr 
    
If true, git-am will call git-mailsplit for patches in mbox format with parameter `--keep-cr`. In this case git-mailsplit will not remove _\r_ from lines ending with _\r\n_. Can be overridden by giving `--no-keep-cr` from the command line. See [git-am[1]](https://git-scm.com/docs/git-am), [git-mailsplit[1]](https://git-scm.com/docs/git-mailsplit). 

[](https://git-scm.com/docs/git-am#Documentation/git-am.txt-amthreeWay)am.threeWay 
    
By default, `git` `am` will fail if the patch does not apply cleanly. When set to true, this setting tells `git` `am` to fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally (equivalent to giving the `--3way` option from the command line). Defaults to `false`. See [git-am[1]](https://git-scm.com/docs/git-am).
##  [](https://git-scm.com/docs/git-am#_see_also)SEE ALSO
[git-apply[1]](https://git-scm.com/docs/git-apply), [git-format-patch[1]](https://git-scm.com/docs/git-format-patch).
##  [](https://git-scm.com/docs/git-am#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### am
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
