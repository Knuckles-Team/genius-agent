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
    * [NAME](https://git-scm.com/docs/git-stash#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-stash#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-stash#_description)
    * [COMMANDS](https://git-scm.com/docs/git-stash#_commands)
    * [OPTIONS](https://git-scm.com/docs/git-stash#_options)
    * [DISCUSSION](https://git-scm.com/docs/git-stash#_discussion)
    * [EXAMPLES](https://git-scm.com/docs/git-stash#_examples)
    * [CONFIGURATION](https://git-scm.com/docs/git-stash#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-stash#_see_also)
    * [GIT](https://git-scm.com/docs/git-stash#_git)


[ English ▾](https://git-scm.com/docs/git-stash)
Localized versions of **git-stash** manual
  1. [English ](https://git-scm.com/docs/git-stash)
  2. [Français ](https://git-scm.com/docs/git-stash/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-stash/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-stash/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-stash/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-stash)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-stash) git-stash last updated in 2.52.0
Changes in the **git-stash** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-stash/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-stash/2.51.0)
  5. 2.43.1 → 2.50.1 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-stash/2.43.0)
  7. 2.42.1 → 2.42.4 no changes
  8. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-stash/2.42.0)
  9. 2.39.1 → 2.41.3 no changes
  10. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-stash/2.39.0)
  11. 2.38.1 → 2.38.5 no changes
  12. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-stash/2.38.0)
  13. 2.35.1 → 2.37.7 no changes
  14. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-stash/2.35.0)
  15. 2.32.1 → 2.34.8 no changes
  16. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-stash/2.32.0)
  17. 2.31.1 → 2.31.8 no changes
  18. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-stash/2.31.0)
  19. 2.26.1 → 2.30.9 no changes
  20. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-stash/2.26.0)
  21. 2.24.1 → 2.25.5 no changes
  22. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-stash/2.24.0)
  23. 2.23.1 → 2.23.4 no changes
  24. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-stash/2.23.0)
  25. 2.22.1 → 2.22.5 no changes
  26. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-stash/2.22.0)
  27. 2.17.1 → 2.21.4 no changes
  28. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-stash/2.17.0)
  29. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-stash/2.16.6)
  30. 2.15.4 no changes
  31. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-stash/2.14.6)
  32. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-stash/2.13.7)
  33. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-stash/2.12.5)
  34. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-stash/2.11.4)
  35. 2.8.6 → 2.10.5 no changes
  36. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-stash/2.7.6)
  37. 2.1.4 → 2.6.7 no changes
  38. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-stash/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-stash#_name)NAME
git-stash - Stash the changes in a dirty working directory away
##  [](https://git-scm.com/docs/git-stash#_synopsis)SYNOPSIS
```
git stash list [_<log-options>_]
git stash show [-u | --include-untracked | --only-untracked] [_<diff-options>_] [_<stash>_]
git stash drop [-q | --quiet] [_<stash>_]
git stash pop [--index] [-q | --quiet] [_<stash>_]
git stash apply [--index] [-q | --quiet] [_<stash>_]
git stash branch _<branchname>_ [_<stash>_]
git stash [push [-p | --patch] [-S | --staged] [-k | --[no-]keep-index] [-q | --quiet]
	     [-u | --include-untracked] [-a | --all] [(-m | --message) _<message>_]
	     [--pathspec-from-file=_<file>_ [--pathspec-file-nul]]
	     [--] [_<pathspec>_…​]]
git stash save [-p | --patch] [-S | --staged] [-k | --[no-]keep-index] [-q | --quiet]
           [-u | --include-untracked] [-a | --all] [_<message>_]
git stash clear
git stash create [_<message>_]
git stash store [(-m | --message) _<message>_] [-q | --quiet] _<commit>_
git stash export (--print | --to-ref _<ref>_) [_<stash>_…​]
git stash import _<commit>_
```

##  [](https://git-scm.com/docs/git-stash#_description)DESCRIPTION
Use `git` `stash` when you want to record the current state of the working directory and the index, but want to go back to a clean working directory. The command saves your local modifications away and reverts the working directory to match the `HEAD` commit.
The modifications stashed away by this command can be listed with `git` `stash` `list`, inspected with `git` `stash` `show`, and restored (potentially on top of a different commit) with `git` `stash` `apply`. Calling `git` `stash` without any arguments is equivalent to `git` `stash` `push`. A stash is by default listed as "WIP on _< branchname>_ …​", but you can give a more descriptive message on the command line when you create one.
The latest stash you created is stored in `refs/stash`; older stashes are found in the reflog of this reference and can be named using the usual reflog syntax (e.g. `stash@{0}` is the most recently created stash, `stash@{1}` is the one before it, `stash@{2.hours.ago}` is also possible). Stashes may also be referenced by specifying just the stash index (e.g. the integer _< n>_ is equivalent to `stash@{`_< n>_`}`).
##  [](https://git-scm.com/docs/git-stash#_commands)COMMANDS 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-push-p--patch-S--staged-k--no-keep-index-u--include-untracked-a--all-q--quiet-m--messagemessage--pathspec-from-filefile--pathspec-file-nul--pathspec)`push` [`-p` | `--patch`] [`-S` | `--staged`] [`-k` | `--`[`no-`]`keep-index`] [`-u` | `--include-untracked`] [ `-a` | `--all`] [`-q` | `--quiet`] [(`-m`|`--message`) _< message>_] [`--pathspec-from-file=`_< file>_ [`--pathspec-file-nul`]] [`--`] [_< pathspec>_...] 
    
Save your local modifications to a new _stash entry_ and roll them back to `HEAD` (in the working tree and in the index). The _< message>_ part is optional and gives the description along with the stashed state.
For quickly making a snapshot, you can omit "push". In this mode, non-option arguments are not allowed to prevent a misspelled subcommand from making an unwanted stash entry. The two exceptions to this are `stash` `-p` which acts as alias for `stash` `push` `-p` and pathspec elements, which are allowed after a double hyphen `--` for disambiguation. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-save-p--patch-S--staged-k--no-keep-index-u--include-untracked-a--all-q--quietmessage)`save` [`-p` | `--patch`] [`-S` | `--staged`] [`-k` | `--`[`no-`]`keep-index`] [`-u` | `--include-untracked`] [`-a` | `--all`] [`-q` | `--quiet`] [_< message>_] 
    
This option is deprecated in favour of _git stash push_. It differs from "stash push" in that it cannot take pathspec. Instead, all non-option arguments are concatenated to form the stash message. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-listlog-options)`list` [_< log-options>_] 
    
List the stash entries that you currently have. Each _stash entry_ is listed with its name (e.g. `stash@{0}` is the latest entry, `stash@{1}` is the one before, etc.), the name of the branch that was current when the entry was made, and a short description of the commit the entry was based on.
```
stash@{0}: WIP on submit: 6ebd0e2... Update git-stash documentation
stash@{1}: On master: 9cc0589... Add git-stash
```

The command takes options applicable to the _git log_ command to control what is shown and how. See [git-log[1]](https://git-scm.com/docs/git-log). 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-show-u--include-untracked--only-untrackeddiff-optionsstash)`show` [`-u` | `--include-untracked` | `--only-untracked`] [_< diff-options>_] [_< stash>_] 
    
Show the changes recorded in the stash entry as a diff between the stashed contents and the commit back when the stash entry was first created. By default, the command shows the diffstat, but it will accept any format known to _git diff_ (e.g., `git` `stash` `show` `-p` `stash@{1}` to view the second most recent entry in patch form). If no _< diff-option>_ is provided, the default behavior will be given by the `stash.showStat`, and `stash.showPatch` config variables. You can also use `stash.showIncludeUntracked` to set whether `--include-untracked` is enabled by default. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-pop--index-q--quietstash)`pop` [`--index`] [`-q` | `--quiet`] [_< stash>_] 
    
Remove a single stashed state from the stash list and apply it on top of the current working tree state, i.e., do the inverse operation of `git` `stash` `push`. The working directory must match the index.
Applying the state can fail with conflicts; in this case, it is not removed from the stash list. You need to resolve the conflicts by hand and call `git` `stash` `drop` manually afterwards. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-apply--index-q--quietstash)`apply` [`--index`] [`-q` | `--quiet`] [_< stash>_] 
    
Like `pop`, but do not remove the state from the stash list. Unlike `pop`, _< stash>_ may be any commit that looks like a commit created by `stash` `push` or `stash` `create`. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-branchbranchnamestash)`branch` _< branchname>_ [_< stash>_] 
    
Creates and checks out a new branch named _< branchname>_ starting from the commit at which the _< stash>_ was originally created, applies the changes recorded in _< stash>_ to the new working tree and index. If that succeeds, and _< stash>_ is a reference of the form `stash@{`_< revision>_`}`, it then drops the _< stash>_.
This is useful if the branch on which you ran `git` `stash` `push` has changed enough that `git` `stash` `apply` fails due to conflicts. Since the stash entry is applied on top of the commit that was HEAD at the time `git` `stash` was run, it restores the originally stashed state with no conflicts. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-clear)`clear` 
    
Remove all the stash entries. Note that those entries will then be subject to pruning, and may be impossible to recover (see _EXAMPLES_ below for a possible strategy). 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-drop-q--quietstash)`drop` [`-q` | `--quiet`] [_< stash>_] 
    
Remove a single stash entry from the list of stash entries. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-create)`create` 
    
Create a stash entry (which is a regular commit object) and return its object name, without storing it anywhere in the ref namespace. This is intended to be useful for scripts. It is probably not the command you want to use; see "push" above. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-store)`store` 
    
Store a given stash created via _git stash create_ (which is a dangling merge commit) in the stash ref, updating the stash reflog. This is intended to be useful for scripts. It is probably not the command you want to use; see "push" above. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-export--print--to-refrefstash)`export` ( `--print` | `--to-ref` _< ref>_ ) [_< stash>_...] 
    
Export the specified stashes, or all of them if none are specified, to a chain of commits which can be transferred using the normal fetch and push mechanisms, then imported using the `import` subcommand. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-importcommit)`import` _< commit>_ 
    
Import the specified stashes from the specified commit, which must have been created by `export`, and add them to the list of stashes. To replace the existing stashes, use `clear` first.
##  [](https://git-scm.com/docs/git-stash#_options)OPTIONS 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt--a)`-a` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---all)`--all` 
    
This option is only valid for `push` and `save` commands.
All ignored and untracked files are also stashed and then cleaned up with `git` `clean`. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt--u)`-u` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---include-untracked)`--include-untracked` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---no-include-untracked)`--no-include-untracked` 
    
When used with the `push` and `save` commands, all untracked files are also stashed and then cleaned up with `git` `clean`.
When used with the `show` command, show the untracked files in the stash entry as part of the diff. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---only-untracked)`--only-untracked` 
    
This option is only valid for the `show` command.
Show only the untracked files in the stash entry as part of the diff. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---index)`--index` 
    
This option is only valid for `pop` and `apply` commands.
Tries to reinstate not only the working tree’s changes, but also the index’s ones. However, this can fail, when you have conflicts (which are stored in the index, where you therefore can no longer apply the changes as they were originally). 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt--k)`-k` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---keep-index)`--keep-index` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---no-keep-index)`--no-keep-index` 
    
This option is only valid for `push` and `save` commands.
All changes already added to the index are left intact. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt--p)`-p` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---patch)`--patch` 
    
This option is only valid for `push` and `save` commands.
Interactively select hunks from the diff between HEAD and the working tree to be stashed. The stash entry is constructed such that its index state is the same as the index state of your repository, and its worktree contains only the changes you selected interactively. The selected changes are then rolled back from your worktree. See the “Interactive Mode” section of [git-add[1]](https://git-scm.com/docs/git-add) to learn how to operate the `--patch` mode.
The `--patch` option implies `--keep-index`. You can use `--no-keep-index` to override this. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context. Defaults to `diff.context` or 3 if the config option is unset. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---inter-hunk-contextn)`--inter-hunk-context=`_< n>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt--S)`-S` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---staged)`--staged` 
    
This option is only valid for `push` and `save` commands.
Stash only the changes that are currently staged. This is similar to basic `git` `commit` except the state is committed to the stash instead of current branch.
The `--patch` option has priority over this one. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---pathspec-from-filefile)`--pathspec-from-file=`_< file>_ 
    
This option is only valid for `push` command.
Pathspec is passed in _< file>_ instead of commandline args. If _< file>_ is exactly `-` then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). See also `--pathspec-file-nul` and global `--literal-pathspecs`. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---pathspec-file-nul)`--pathspec-file-nul` 
    
This option is only valid for `push` command.
Only meaningful with `--pathspec-from-file`. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes). 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt--q)`-q` 


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---quiet)`--quiet` 
    
This option is only valid for `apply`, `drop`, `pop`, `push`, `save`, `store` commands.
Quiet, suppress feedback messages. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---print)`--print` 
    
This option is only valid for the `export` command.
Create the chain of commits representing the exported stashes without storing it anywhere in the ref namespace and print the object ID to standard output. This is designed for scripts. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---to-ref)`--to-ref` 
    
This option is only valid for the `export` command.
Create the chain of commits representing the exported stashes and store it to the specified ref. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt---)`--` 
    
This option is only valid for `push` command.
Separates pathspec from options for disambiguation purposes. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-pathspec)_< pathspec>_... 
    
This option is only valid for `push` command.
The new stash entry records the modified states only for the files that match the pathspec. The index entries and working tree files are then rolled back to the state in HEAD only for these files, too, leaving files that do not match the pathspec intact.
For more details, see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary). 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-stash)_< stash>_ 
    
This option is only valid for `apply`, `branch`, `drop`, `pop`, `show`, and `export` commands.
A reference of the form `stash@{`_< revision>_`}`. When no _< stash>_ is given, the latest stash is assumed (that is, `stash@{0}`).
##  [](https://git-scm.com/docs/git-stash#_discussion)DISCUSSION
A stash entry is represented as a commit whose tree records the state of the working directory, and its first parent is the commit at `HEAD` when the entry was created. The tree of the second parent records the state of the index when the entry is made, and it is made a child of the `HEAD` commit. The ancestry graph looks like this:
```
       .----W
      /    /
-----H----I
```

where `H` is the `HEAD` commit, `I` is a commit that records the state of the index, and `W` is a commit that records the state of the working tree.
##  [](https://git-scm.com/docs/git-stash#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-Pullingintoadirtytree)Pulling into a dirty tree 
    
When you are in the middle of something, you learn that there are upstream changes that are possibly relevant to what you are doing. When your local changes do not conflict with the changes in the upstream, a simple `git` `pull` will let you move forward.
However, there are cases in which your local changes do conflict with the upstream changes, and `git` `pull` refuses to overwrite your changes. In such a case, you can stash your changes away, perform a pull, and then unstash, like this:
```
$ git pull
 ...
file foobar not up to date, cannot merge.
$ git stash
$ git pull
$ git stash pop
```


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-Interruptedworkflow)Interrupted workflow 
    
When you are in the middle of something, your boss comes in and demands that you fix something immediately. Traditionally, you would make a commit to a temporary branch to store your changes away, and return to your original branch to make the emergency fix, like this:
```
# ... hack hack hack ...
$ git switch -c my_wip
$ git commit -a -m "WIP"
$ git switch master
$ edit emergency fix
$ git commit -a -m "Fix in a hurry"
$ git switch my_wip
$ git reset --soft HEAD^
# ... continue hacking ...
```

You can use _git stash_ to simplify the above, like this:
```
# ... hack hack hack ...
$ git stash
$ edit emergency fix
$ git commit -a -m "Fix in a hurry"
$ git stash pop
# ... continue hacking ...
```


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-Testingpartialcommits)Testing partial commits 
    
You can use `git` `stash` `push` `--keep-index` when you want to make two or more commits out of the changes in the work tree, and you want to test each change before committing:
```
# ... hack hack hack ...
$ git add --patch foo            # add just first part to the index
$ git stash push --keep-index    # save all other changes to the stash
$ edit/build/test first part
$ git commit -m 'First part'     # commit fully tested change
$ git stash pop                  # prepare to work on all other changes
# ... repeat above five steps until one commit remains ...
$ edit/build/test remaining parts
$ git commit foo -m 'Remaining parts'
```


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-Savingunrelatedchangesforfutureuse)Saving unrelated changes for future use 
    
When you are in the middle of massive changes and you find some unrelated issue that you don’t want to forget to fix, you can do the change(s), stage them, and use `git` `stash` `push` `--staged` to stash them out for future use. This is similar to committing the staged changes, only the commit ends-up being in the stash and not on the current branch.
```
# ... hack hack hack ...
$ git add --patch foo           # add unrelated changes to the index
$ git stash push --staged       # save these changes to the stash
# ... hack hack hack, finish current changes ...
$ git commit -m 'Massive'       # commit fully tested changes
$ git switch fixup-branch       # switch to another branch
$ git stash pop                 # to finish work on the saved changes
```


[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-Recoveringstashentriesthatwerecleareddroppederroneously)Recovering stash entries that were cleared/dropped erroneously 
    
If you mistakenly drop or clear stash entries, they cannot be recovered through the normal safety mechanisms. However, you can try the following incantation to get a list of stash entries that are still in your repository, but not reachable any more:
```
git fsck --unreachable |
grep commit | cut -d\  -f3 |
xargs git log --merges --no-walk --grep=WIP
```

##  [](https://git-scm.com/docs/git-stash#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-stashindex)`stash.index` 
    
If this is set to true, `git` `stash` `apply` and `git` `stash` `pop` will behave as if `--index` was supplied. Defaults to false. 

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-stashshowIncludeUntracked)`stash.showIncludeUntracked` 
    
If this is set to true, the `git` `stash` `show` command will show the untracked files of a stash entry. Defaults to false.  

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-stashshowPatch)`stash.showPatch` 
    
If this is set to true, the `git` `stash` `show` command without an option will show the stash entry in patch form. Defaults to false.  

[](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-stashshowStat)`stash.showStat` 
    
If this is set to true, the `git` `stash` `show` command without an option will show a diffstat of the stash entry. Defaults to true. 
##  [](https://git-scm.com/docs/git-stash#_see_also)SEE ALSO
[git-checkout[1]](https://git-scm.com/docs/git-checkout), [git-commit[1]](https://git-scm.com/docs/git-commit), [git-reflog[1]](https://git-scm.com/docs/git-reflog), [git-reset[1]](https://git-scm.com/docs/git-reset), [git-switch[1]](https://git-scm.com/docs/git-switch)
##  [](https://git-scm.com/docs/git-stash#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### stash
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
