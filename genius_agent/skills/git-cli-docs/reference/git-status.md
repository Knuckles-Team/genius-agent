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
    * [NAME](https://git-scm.com/docs/git-status#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-status#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-status#_description)
    * [OPTIONS](https://git-scm.com/docs/git-status#_options)
    * [OUTPUT](https://git-scm.com/docs/git-status#_output)
    * [CONFIGURATION](https://git-scm.com/docs/git-status#_configuration)
    * [BACKGROUND REFRESH](https://git-scm.com/docs/git-status#_background_refresh)
    * [UNTRACKED FILES AND PERFORMANCE](https://git-scm.com/docs/git-status#_untracked_files_and_performance)
    * [SEE ALSO](https://git-scm.com/docs/git-status#_see_also)
    * [GIT](https://git-scm.com/docs/git-status#_git)


[ English ▾](https://git-scm.com/docs/git-status)
Localized versions of **git-status** manual
  1. [English ](https://git-scm.com/docs/git-status)
  2. [Français ](https://git-scm.com/docs/git-status/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-status/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-status/sv)
  5. [українська мова ](https://git-scm.com/docs/git-status/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-status/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-status)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-status) git-status last updated in 2.53.0
Changes in the **git-status** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-status/2.53.0)
  2. 2.45.1 → 2.52.0 no changes
  3. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-status/2.45.0)
  4. 2.44.1 → 2.44.4 no changes
  5. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-status/2.44.0)
  6. 2.43.1 → 2.43.7 no changes
  7. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-status/2.43.0)
  8. 2.40.1 → 2.42.4 no changes
  9. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-status/2.40.0)
  10. 2.39.1 → 2.39.5 no changes
  11. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-status/2.39.0)
  12. 2.35.1 → 2.38.5 no changes
  13. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-status/2.35.0)
  14. 2.34.1 → 2.34.8 no changes
  15. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-status/2.34.0)
  16. 2.31.1 → 2.33.8 no changes
  17. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-status/2.31.0)
  18. 2.30.2 → 2.30.9 no changes
  19. [2.30.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-02-08_ ](https://git-scm.com/docs/git-status/2.30.1)
  20. 2.24.1 → 2.30.0 no changes
  21. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-status/2.24.0)
  22. 2.22.1 → 2.23.4 no changes
  23. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-status/2.22.0)
  24. 2.21.1 → 2.21.4 no changes
  25. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-status/2.21.0)
  26. 2.19.1 → 2.20.5 no changes
  27. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-status/2.19.0)
  28. 2.18.1 → 2.18.5 no changes
  29. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-status/2.18.0)
  30. 2.17.1 → 2.17.6 no changes
  31. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-status/2.17.0)
  32. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-status/2.16.6)
  33. 2.15.4 no changes
  34. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-status/2.14.6)
  35. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-status/2.13.7)
  36. 2.12.5 no changes
  37. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-status/2.11.4)
  38. 2.7.6 → 2.10.5 no changes
  39. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-status/2.6.7)
  40. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-status/2.5.6)
  41. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-status/2.4.12)
  42. 2.3.10 no changes
  43. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-status/2.2.3)
  44. 2.1.4 no changes
  45. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-status/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-status#_name)NAME
git-status - Show the working tree status
##  [](https://git-scm.com/docs/git-status#_synopsis)SYNOPSIS
```
git status [_<options>_] [--] [_<pathspec>_…​]
```

##  [](https://git-scm.com/docs/git-status#_description)DESCRIPTION
Displays paths that have differences between the index file and the current HEAD commit, paths that have differences between the working tree and the index file, and paths in the working tree that are not tracked by Git (and are not ignored by [gitignore[5]](https://git-scm.com/docs/gitignore)). The first are what you _would_ commit by running `git` `commit`; the second and third are what you _could_ commit by running `git` `add` before running `git` `commit`.
##  [](https://git-scm.com/docs/git-status#_options)OPTIONS 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt--s)`-s` 


[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---short)`--short` 
    
Give the output in the short-format. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt--b)`-b` 


[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---branch)`--branch` 
    
Show the branch and tracking info even in short-format. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---show-stash)`--show-stash` 
    
Show the number of entries currently stashed away. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---porcelainversion)`--porcelain`[`=`_< version>_] 
    
Give the output in an easy-to-parse format for scripts. This is similar to the short output, but will remain stable across Git versions and regardless of user configuration. See below for details.
The _< version>_ parameter is used to specify the format version. This is optional and defaults to the original version `v1` format. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---long)`--long` 
    
Give the output in the long-format. This is the default. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt--v)`-v` 


[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---verbose)`--verbose` 
    
In addition to the names of files that have been changed, also show the textual changes that are staged to be committed (i.e., like the output of `git` `diff` `--cached`). If `-v` is specified twice, then also show the changes in the working tree that have not yet been staged (i.e., like the output of `git` `diff`). 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt--umode)`-u`[_< mode>_] 


[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---untracked-filesmode)`--untracked-files`[`=`_< mode>_] 
    
Show untracked files.
The mode parameter is used to specify the handling of untracked files. It is optional: it defaults to `all`, and if specified, it must be stuck to the option (e.g. `-uno`, but not `-u` `no`).
The possible options are: 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-no)`no` 
    
Show no untracked files. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-normal)`normal` 
    
Show untracked files and directories. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-all)`all` 
    
Also show individual files in untracked directories.
When `-u` option is not used, untracked files and directories are shown (i.e. the same as specifying `normal`), to help you avoid forgetting to add newly created files. Because it takes extra work to find untracked files in the filesystem, this mode may take some time in a large working tree. Consider enabling untracked cache and split index if supported (see `git` `update-index` `--untracked-cache` and `git` `update-index` `--split-index`), Otherwise you can use `no` to have `git` `status` return more quickly without showing untracked files. All usual spellings for Boolean value `true` are taken as `normal` and `false` as `no`.
The default can be changed using the `status.showUntrackedFiles` configuration variable documented in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---ignore-submoduleswhen)`--ignore-submodules`[`=`_< when>_] 
    
Ignore changes to submodules when looking for changes. _< when>_ can be either `none`, `untracked`, `dirty` or `all`, which is the default. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-none)`none` 
    
will consider the submodule modified when it either contains untracked or modified files or its HEAD differs from the commit recorded in the superproject and can be used to override any settings of the `ignore` option in [git-config[1]](https://git-scm.com/docs/git-config) or [gitmodules[5]](https://git-scm.com/docs/gitmodules). 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-untracked)`untracked` 
    
submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-dirty)`dirty` 
    
ignore all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior before 1.7.0). 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-all-1)`all` 
    
hide all changes to submodules (and suppresses the output of submodule summaries when the config option `status.submoduleSummary` is set). 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---ignoredmode)`--ignored`[`=`_< mode>_] 
    
Show ignored files as well.
The mode parameter is used to specify the handling of ignored files. It is optional: it defaults to `traditional`.
The possible options are: 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-traditional)`traditional` 
    
Show ignored files and directories, unless `--untracked-files=all` is specified, in which case individual files in ignored directories are displayed. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-no-1)`no` 
    
Show no ignored files. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-matching)`matching` 
    
Show ignored files and directories matching an ignore pattern.
Paths that explicitly match an ignored pattern are shown. If a directory matches an ignore pattern, then it is shown, but not paths contained in the ignored directory. If a directory does not match an ignore pattern, but all contents are ignored, then the directory is not shown, but all contents are shown. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt--z)`-z` 
    
Terminate entries with _NUL_ , instead of _LF_. This implies the `--porcelain=v1` output format if no other format is given. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---columnoptions)`--column`[`=`_< options>_] 


[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---no-column)`--no-column` 
    
Display untracked files in columns. See configuration variable `column.status` for option syntax. `--column` and `--no-column` without options are equivalent to `always` and `never` respectively. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---ahead-behind)`--ahead-behind` 


[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---no-ahead-behind)`--no-ahead-behind` 
    
Display or do not display detailed ahead/behind counts for the branch relative to its upstream branch. Defaults to `true`. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---renames)`--renames` 


[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---no-renames)`--no-renames` 
    
Turn on/off rename detection regardless of user configuration. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--no-renames`. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt---find-renamesn)`--find-renames`[`=`_< n>_] 
    
Turn on rename detection, optionally setting the similarity threshold. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--find-renames`. 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-pathspec)_< pathspec>_... 
    
See the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary).
##  [](https://git-scm.com/docs/git-status#_output)OUTPUT
The output from this command is designed to be used as a commit template comment. The default, long format, is designed to be human readable, verbose and descriptive. Its contents and format are subject to change at any time.
The paths mentioned in the output, unlike many other Git commands, are made relative to the current directory if you are working in a subdirectory (this is on purpose, to help cutting and pasting). See the status.relativePaths config option below.
###  [](https://git-scm.com/docs/git-status#_short_format)Short Format
In the short-format, the status of each path is shown as one of these forms
```
<xy> <path>
<xy> <orig-path> -> <path>
```

where _< orig-path>_ is where the renamed/copied contents came from. _< orig-path>_ is only shown when the entry is renamed or copied. The _< xy>_ is a two-letter status code `XY`.
The fields (including the _- >_) are separated from each other by a single space. If a filename contains whitespace or other nonprintable characters, that field will be quoted in the manner of a C string literal: surrounded by ASCII double quote (34) characters, and with interior special characters backslash-escaped.
There are three different types of states that are shown using this format, and each one uses the _< xy>_ syntax differently:
  * When a merge is occurring and the merge was successful, or outside of a merge situation, `X` shows the status of the index and `Y` shows the status of the working tree.
  * When a merge conflict has occurred and has not yet been resolved, `X` and `Y` show the state introduced by each head of the merge, relative to the common ancestor. These paths are said to be _unmerged_.
  * When a path is untracked, `X` and `Y` are always the same, since they are unknown to the index. _??_ is used for untracked paths. Ignored files are not listed unless `--ignored` is used; if it is, ignored files are indicated by `!!`.


Note that the term _merge_ here also includes rebases using the default `--merge` strategy, cherry-picks, and anything else using the merge machinery.
In the following table, these three classes are shown in separate sections, and these characters are used for `X` and `Y` fields for the first two sections that show tracked paths: 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-)' ' 
    
unmodified 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-M)`M` 
    
modified 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-T)`T` 
    
file type changed (regular file, symbolic link or submodule) 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-A)`A` 
    
added 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-D)`D` 
    
deleted 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-R)`R` 
    
renamed 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-C)`C` 
    
copied (if config option status.renames is set to "copies") 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-U)`U` 
    
updated but unmerged
X | Y | Meaning  
---|---|---  
| [`AMD`] | not updated  
`M` | [ `MTD`] | updated in index  
`T` | [ `MTD`] | type changed in index  
`A` | [ `MTD`] | added to index  
`D` |  | deleted from index  
`R` | [ `MTD`] | renamed in index  
`C` | [ `MTD`] | copied in index  
[`MTARC`] |  | index and work tree matches  
[ `MTARC`] | `M` | work tree changed since index  
[ `MTARC`] | `T` | type changed in work tree since index  
[ `MTARC`] | `D` | deleted in work tree  
| `R` | renamed in work tree  
| `C` | copied in work tree  
`D` | `D` | unmerged, both deleted  
`A` | `U` | unmerged, added by us  
`U` | `D` | unmerged, deleted by them  
`U` | `A` | unmerged, added by them  
`D` | `U` | unmerged, deleted by us  
`A` | `A` | unmerged, both added  
`U` | `U` | unmerged, both modified  
_?_ | _?_ | untracked  
`!` | `!` | ignored  
Submodules have more state and instead report 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-M-1)`M` 
    
the submodule has a different HEAD than recorded in the index 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt-m)`m` 
    
the submodule has modified content 

[](https://git-scm.com/docs/git-status#Documentation/git-status.txt--1)_?_ 
    
the submodule has untracked files
This is since modified content or untracked files in a submodule cannot be added via `git` `add` in the superproject to prepare a commit.
`m` and _?_ are applied recursively. For example if a nested submodule in a submodule contains an untracked file, this is reported as _?_ as well.
If `-b` is used the short-format status is preceded by a line
```
{empty}## _<branchname>_ _<tracking-info>_
```

###  [](https://git-scm.com/docs/git-status#_porcelain_format_version_1)Porcelain Format Version 1
Version 1 porcelain format is similar to the short format, but is guaranteed not to change in a backwards-incompatible way between Git versions or based on user configuration. This makes it ideal for parsing by scripts. The description of the short format above also describes the porcelain format, with a few exceptions:
  1. The user’s `color.status` configuration is not respected; color will always be off.
  2. The user’s `status.relativePaths` configuration is not respected; paths shown will always be relative to the repository root.


There is also an alternate `-z` format recommended for machine parsing. In that format, the status field is the same, but some other things change. First, the _- >_ is omitted from rename entries and the field order is reversed (e.g _from - > to_ becomes `to` `from`). Second, a _NUL_ (ASCII 0) follows each filename, replacing space as a field separator and the terminating newline (but a space still separates the status field from the first filename). Third, filenames containing special characters are not specially formatted; no quoting or backslash-escaping is performed.
Any submodule changes are reported as modified `M` instead of `m` or single _?_.
###  [](https://git-scm.com/docs/git-status#_porcelain_format_version_2)Porcelain Format Version 2
Version 2 format adds more detailed information about the state of the worktree and changed items. Version 2 also defines an extensible set of easy to parse optional headers.
Header lines start with `#` and are added in response to specific command line arguments. Parsers should ignore headers they don’t recognize.
####  [](https://git-scm.com/docs/git-status#_branch_headers)Branch Headers
If `--branch` is given, a series of header lines are printed with information about the current branch.
Line | Notes  
---|---  
`#` `branch.oid` _< commit>_ | (`initial`) | Current commit.  
`#` `branch.head` _< branch>_ | (`detached`) | Current branch.  
`#` `branch.upstream` _< upstream-branch>_ | If upstream is set.  
`#` `branch.ab` `+`_< ahead>_ `-`_< behind>_ | If upstream is set and the commit is present.  
####  [](https://git-scm.com/docs/git-status#_stash_information)Stash Information
If `--show-stash` is given, one line is printed showing the number of stash entries if non-zero:
```
# stash <N>
```

####  [](https://git-scm.com/docs/git-status#_changed_tracked_entries)Changed Tracked Entries
Following the headers, a series of lines are printed for tracked entries. One of three different line formats may be used to describe an entry depending on the type of change. Tracked entries are printed in an undefined order; parsers should allow for a mixture of the 3 line types in any order.
Ordinary changed entries have the following format:
```
1 _<XY>_ _<sub>_ _<mH>_ _<mI>_ _<mW>_ _<hH>_ _<hI>_ _<path>_
```

Renamed or copied entries have the following format:
```
2 _<XY>_ _<sub>_ _<mH>_ _<mI>_ _<mW>_ _<hH>_ _<hI>_ _<X>__<score>_ _<path>__<sep>__<origPath>_
```

Field | Meaning  
---|---  
_< XY>_ |  A 2 character field containing the staged and unstaged XY values described in the short format, with unchanged indicated by a "." rather than a space.  
_< sub>_ |  A 4 character field describing the submodule state. "N…​" when the entry is not a submodule. `S`_< c>__< m>__< u>_ when the entry is a submodule.
  * _< c>_ is "C" if the commit changed; otherwise ".".
  * _< m>_ is "M" if it has tracked changes; otherwise ".".
  * _< u>_ is "U" if there are untracked changes; otherwise ".".

  
_< mH>_ |  The octal file mode in HEAD.  
_< mI>_ |  The octal file mode in the index.  
_< mW>_ |  The octal file mode in the worktree.  
_< hH>_ |  The object name in HEAD.  
_< hI>_ |  The object name in the index.  
_< X><score>_ |  The rename or copy score (denoting the percentage of similarity between the source and target of the move or copy). For example "R100" or "C75".  
_< path>_ |  The pathname. In a renamed/copied entry, this is the target path.  
_< sep>_ |  When the `-z` option is used, the 2 pathnames are separated with a _NUL_ (ASCII 0x00) byte; otherwise, a _TAB_ (ASCII 0x09) byte separates them.  
_< origPath>_ |  The pathname in the commit at HEAD or in the index. This is only present in a renamed/copied entry, and tells where the renamed/copied contents came from.  
Unmerged entries have the following format; the first character is a "u" to distinguish from ordinary changed entries.
```
u _<XY>_ _<sub>_ _<m1>_ _<m2>_ _<m3>_ _<mW>_ _<h1>_ _<h2>_ _<h3>_ _<path>_
```

Field | Meaning  
---|---  
_< XY>_ |  A 2 character field describing the conflict type as described in the short format.  
_< sub>_ |  A 4 character field describing the submodule state as described above.  
_< m1>_ |  The octal file mode in stage 1.  
_< m2>_ |  The octal file mode in stage 2.  
_< m3>_ |  The octal file mode in stage 3.  
_< mW>_ |  The octal file mode in the worktree.  
_< h1>_ |  The object name in stage 1.  
_< h2>_ |  The object name in stage 2.  
_< h3>_ |  The object name in stage 3.  
_< path>_ |  The pathname.  
####  [](https://git-scm.com/docs/git-status#_other_items)Other Items
Following the tracked entries (and if requested), a series of lines will be printed for untracked and then ignored items found in the worktree.
Untracked items have the following format:
```
? <path>
```

Ignored items have the following format:
```
! <path>
```

####  [](https://git-scm.com/docs/git-status#_pathname_format_notes_and_z)Pathname Format Notes and -z
When the `-z` option is given, pathnames are printed as is and without any quoting and lines are terminated with a _NUL_ (ASCII 0x00) byte.
Without the `-z` option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)).
##  [](https://git-scm.com/docs/git-status#_configuration)CONFIGURATION
The command honors `color.status` (or `status.color` — they mean the same thing and the latter is kept for backward compatibility) and `color.status.`_< slot>_ configuration variables to colorize its output.
If the config variable `status.relativePaths` is set to false, then all paths shown are relative to the repository root, not to the current directory.
If `status.submoduleSummary` is set to a non zero number or true (identical to -1 or an unlimited number), the submodule summary will be enabled for the long format and a summary of commits for modified submodules will be shown (see `--summary-limit` option of [git-submodule[1]](https://git-scm.com/docs/git-submodule)). Please note that the summary output from the status command will be suppressed for all submodules when `diff.ignoreSubmodules` is set to `all` or only for those submodules where `submodule.`_< name>_`.ignore=all`. To also view the summary for ignored submodules you can either use the `--ignore-submodules=dirty` command line option or the _git submodule summary_ command, which shows a similar output but does not honor these settings.
##  [](https://git-scm.com/docs/git-status#_background_refresh)BACKGROUND REFRESH
By default, `git` `status` will automatically refresh the index, updating the cached stat information from the working tree and writing out the result. Writing out the updated index is an optimization that isn’t strictly necessary (`status` computes the values for itself, but writing them out is just to save subsequent programs from repeating our computation). When `status` is run in the background, the lock held during the write may conflict with other simultaneous processes, causing them to fail. Scripts running `status` in the background should consider using `git` `--no-optional-locks` `status` (see [git[1]](https://git-scm.com/docs/git) for details).
##  [](https://git-scm.com/docs/git-status#_untracked_files_and_performance)UNTRACKED FILES AND PERFORMANCE
`git` `status` can be very slow in large worktrees if/when it needs to search for untracked files and directories. There are many configuration options available to speed this up by either avoiding the work or making use of cached results from previous Git commands. There is no single optimum set of settings right for everyone. We’ll list a summary of the relevant options to help you, but before going into the list, you may want to run `git` `status` again, because your configuration may already be caching `git` `status` results, so it could be faster on subsequent runs.
  * The `--untracked-files=no` flag or the `status.showUntrackedFiles=no` config (see above for both): indicate that `git` `status` should not report untracked files. This is the fastest option. `git` `status` will not list the untracked files, so you need to be careful to remember if you create any new files and manually `git` `add` them.
  * `advice.statusUoption=false` (see [git-config[1]](https://git-scm.com/docs/git-config)): setting this variable to `false` disables the warning message given when enumerating untracked files takes more than 2 seconds. In a large project, it may take longer and the user may have already accepted the trade off (e.g. using `-uno` may not be an acceptable option for the user), in which case, there is no point issuing the warning message, and in such a case, disabling the warning may be the best.
  * `core.untrackedCache=true` (see [git-update-index[1]](https://git-scm.com/docs/git-update-index)): enable the untracked cache feature and only search directories that have been modified since the previous `git` `status` command. Git remembers the set of untracked files within each directory and assumes that if a directory has not been modified, then the set of untracked files within has not changed. This is much faster than enumerating the contents of every directory, but still not without cost, because Git still has to search for the set of modified directories. The untracked cache is stored in the `.git/index` file. The reduced cost of searching for untracked files is offset slightly by the increased size of the index and the cost of keeping it up-to-date. That reduced search time is usually worth the additional size.
  * `core.untrackedCache=true` and `core.fsmonitor=true` or `core.fsmonitor=`_< hook-command-pathname>_ (see [git-update-index[1]](https://git-scm.com/docs/git-update-index)): enable both the untracked cache and FSMonitor features and only search directories that have been modified since the previous `git` `status` command. This is faster than using just the untracked cache alone because Git can also avoid searching for modified directories. Git only has to enumerate the exact set of directories that have changed recently. While the FSMonitor feature can be enabled without the untracked cache, the benefits are greatly reduced in that case.


Note that after you turn on the untracked cache and/or FSMonitor features it may take a few `git` `status` commands for the various caches to warm up before you see improved command times. This is normal.
##  [](https://git-scm.com/docs/git-status#_see_also)SEE ALSO
[gitignore[5]](https://git-scm.com/docs/gitignore)
##  [](https://git-scm.com/docs/git-status#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### status
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
