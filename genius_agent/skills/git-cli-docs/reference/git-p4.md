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
    * [NAME](https://git-scm.com/docs/git-p4#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-p4#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-p4#_description)
    * [EXAMPLES](https://git-scm.com/docs/git-p4#_examples)
    * [COMMANDS](https://git-scm.com/docs/git-p4#_commands)
    * [OPTIONS](https://git-scm.com/docs/git-p4#_options)
    * [Hooks for submit](https://git-scm.com/docs/git-p4#_hooks_for_submit)
    * [DEPOT PATH SYNTAX](https://git-scm.com/docs/git-p4#_depot_path_syntax)
    * [CLIENT SPEC](https://git-scm.com/docs/git-p4#_client_spec)
    * [BRANCH DETECTION](https://git-scm.com/docs/git-p4#_branch_detection)
    * [PERFORMANCE](https://git-scm.com/docs/git-p4#_performance)
    * [CONFIGURATION VARIABLES](https://git-scm.com/docs/git-p4#_configuration_variables)
    * [IMPLEMENTATION DETAILS](https://git-scm.com/docs/git-p4#_implementation_details)
    * [GIT](https://git-scm.com/docs/git-p4#_git)


[ English ▾](https://git-scm.com/docs/git-p4)
Localized versions of **git-p4** manual
  1. [English ](https://git-scm.com/docs/git-p4)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-p4/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-p4/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-p4/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-p4)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-p4) git-p4 last updated in 2.52.0
Changes in the **git-p4** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-p4/2.52.0)
  3. 2.50.1 → 2.51.2 no changes
  4. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-p4/2.50.0)
  5. 2.37.1 → 2.49.1 no changes
  6. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-p4/2.37.0)
  7. 2.35.1 → 2.36.6 no changes
  8. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-p4/2.35.0)
  9. 2.32.1 → 2.34.8 no changes
  10. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-p4/2.32.0)
  11. 2.30.2 → 2.31.8 no changes
  12. [2.30.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-02-08_ ](https://git-scm.com/docs/git-p4/2.30.1)
  13. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-p4/2.30.0)
  14. 2.27.1 → 2.29.3 no changes
  15. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-p4/2.27.0)
  16. 2.21.1 → 2.26.3 no changes
  17. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-p4/2.21.0)
  18. 2.20.1 → 2.20.5 no changes
  19. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-p4/2.20.0)
  20. 2.19.1 → 2.19.6 no changes
  21. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-p4/2.19.0)
  22. 2.18.1 → 2.18.5 no changes
  23. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-p4/2.18.0)
  24. 2.17.0 → 2.17.6 no changes
  25. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-p4/2.16.6)
  26. 2.13.7 → 2.15.4 no changes
  27. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-p4/2.12.5)
  28. 2.10.5 → 2.11.4 no changes
  29. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-p4/2.9.5)
  30. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-p4/2.8.6)
  31. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-p4/2.7.6)
  32. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-p4/2.6.7)
  33. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-p4/2.5.6)
  34. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-p4/2.4.12)
  35. 2.1.4 → 2.3.10 no changes
  36. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-p4/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-p4#_name)NAME
git-p4 - Import from and submit to Perforce repositories
##  [](https://git-scm.com/docs/git-p4#_synopsis)SYNOPSIS
```
_git p4 clone_ [<sync-options>] [<clone-options>] <p4-depot-path>…​
_git p4 sync_ [<sync-options>] [<p4-depot-path>…​]
_git p4 rebase_
_git p4 submit_ [<submit-options>] [<master-branch-name>]
```

##  [](https://git-scm.com/docs/git-p4#_description)DESCRIPTION
This command provides a way to interact with p4 repositories using Git.
Create a new Git repository from an existing p4 repository using _git p4 clone_ , giving it one or more p4 depot paths. Incorporate new commits from p4 changes with _git p4 sync_. The _sync_ command is also used to include new branches from other p4 depot paths. Submit Git changes back to p4 using _git p4 submit_. The command _git p4 rebase_ does a sync plus rebases the current branch onto the updated p4 remote branch.
##  [](https://git-scm.com/docs/git-p4#_examples)EXAMPLES
  * Clone a repository:
```
$ git p4 clone //depot/path/project
```

  * Do some work in the newly created Git repository:
```
$ cd project
$ vi foo.h
$ git commit -a -m "edited foo.h"
```

  * Update the Git repository with recent changes from p4, rebasing your work on top:
```
$ git p4 rebase
```

  * Submit your commits back to p4:
```
$ git p4 submit
```



##  [](https://git-scm.com/docs/git-p4#_commands)COMMANDS
###  [](https://git-scm.com/docs/git-p4#_clone)Clone
Generally, _git p4 clone_ is used to create a new Git directory from an existing p4 repository:
```
$ git p4 clone //depot/path/project
```

This:
  1. Creates an empty Git repository in a subdirectory called _project_.
  2. Imports the full contents of the head revision from the given p4 depot path into a single commit in the Git branch _refs/remotes/p4/master_.
  3. Creates a local branch, _master_ from this remote and checks it out.


To reproduce the entire p4 history in Git, use the _@all_ modifier on the depot path:
```
$ git p4 clone //depot/path/project@all
```

###  [](https://git-scm.com/docs/git-p4#_sync)Sync
As development continues in the p4 repository, those changes can be included in the Git repository using:
```
$ git p4 sync
```

This command finds new changes in p4 and imports them as Git commits.
P4 repositories can be added to an existing Git repository using _git p4 sync_ too:
```
$ mkdir repo-git
$ cd repo-git
$ git init
$ git p4 sync //path/in/your/perforce/depot
```

This imports the specified depot into _refs/remotes/p4/master_ in an existing Git repository. The `--branch` option can be used to specify a different branch to be used for the p4 content.
If a Git repository includes branches _refs/remotes/origin/p4_ , these will be fetched and consulted first during a _git p4 sync_. Since importing directly from p4 is considerably slower than pulling changes from a Git remote, this can be useful in a multi-developer environment.
If there are multiple branches, doing _git p4 sync_ will automatically use the "BRANCH DETECTION" algorithm to try to partition new changes into the right branch. This can be overridden with the `--branch` option to specify just a single branch to update.
###  [](https://git-scm.com/docs/git-p4#_rebase)Rebase
A common working pattern is to fetch the latest changes from the p4 depot and merge them with local uncommitted changes. Often, the p4 repository is the ultimate location for all code, thus a rebase workflow makes sense. This command does _git p4 sync_ followed by _git rebase_ to move local commits on top of updated p4 changes.
```
$ git p4 rebase
```

###  [](https://git-scm.com/docs/git-p4#_submit)Submit
Submitting changes from a Git repository back to the p4 repository requires a separate p4 client workspace. This should be specified using the `P4CLIENT` environment variable or the Git configuration variable _git-p4.client_. The p4 client must exist, but the client root will be created and populated if it does not already exist.
To submit all changes that are in the current Git branch but not in the _p4/master_ branch, use:
```
$ git p4 submit
```

To specify a branch other than the current one, use:
```
$ git p4 submit topicbranch
```

To specify a single commit or a range of commits, use:
```
$ git p4 submit --commit <sha1>
$ git p4 submit --commit <sha1..sha1>
```

The upstream reference is generally _refs/remotes/p4/master_ , but can be overridden using the `--origin=` command-line option.
The p4 changes will be created as the user invoking _git p4 submit_. The `--preserve-user` option will cause ownership to be modified according to the author of the Git commit. This option requires admin privileges in p4, which can be granted using _p4 protect_.
To shelve changes instead of submitting, use `--shelve` and `--update-shelve`:
```
$ git p4 submit --shelve
$ git p4 submit --update-shelve 1234 --update-shelve 2345
```

###  [](https://git-scm.com/docs/git-p4#_unshelve)Unshelve
Unshelving will take a shelved P4 changelist, and produce the equivalent git commit in the branch refs/remotes/p4-unshelved/<changelist>.
The git commit is created relative to the current origin revision (HEAD by default). A parent commit is created based on the origin, and then the unshelve commit is created based on that.
The origin revision can be changed with the "--origin" option.
If the target branch in refs/remotes/p4-unshelved already exists, the old one will be renamed.
```
$ git p4 sync
$ git p4 unshelve 12345
$ git show p4-unshelved/12345
<submit more changes via p4 to the same files>
$ git p4 unshelve 12345
<refuses to unshelve until git is in sync with p4 again>
```

##  [](https://git-scm.com/docs/git-p4#_options)OPTIONS
###  [](https://git-scm.com/docs/git-p4#_general_options)General options
All commands except clone accept these options. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---git-dirdir)--git-dir <dir> 
    
Set the `GIT_DIR` environment variable. See [git[1]](https://git-scm.com/docs/git). 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt--v)-v 


[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---verbose)--verbose 
    
Provide more progress information.
###  [](https://git-scm.com/docs/git-p4#_sync_options)Sync options
These options can be used in the initial _clone_ as well as in subsequent _sync_ operations. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---branchref)--branch <ref> 
    
Import changes into <ref> instead of refs/remotes/p4/master. If <ref> starts with refs/, it is used as is. Otherwise, if it does not start with p4/, that prefix is added.
By default a <ref> not starting with refs/ is treated as the name of a remote-tracking branch (under refs/remotes/). This behavior can be modified using the --import-local option.
The default <ref> is "master".
This example imports a new remote "p4/proj2" into an existing Git repository:
```
    $ git init
    $ git p4 sync --branch=refs/remotes/p4/proj2 //depot/proj2
```


[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---detect-branches)--detect-branches 
    
Use the branch detection algorithm to find new paths in p4. It is documented below in "BRANCH DETECTION". 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---changesfilefile)--changesfile <file> 
    
Import exactly the p4 change numbers listed in _file_ , one per line. Normally, _git p4_ inspects the current p4 repository state and detects the changes it should import. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---silent)--silent 
    
Do not print any progress information. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---detect-labels)--detect-labels 
    
Query p4 for labels associated with the depot paths, and add them as tags in Git. Limited usefulness as only imports labels associated with new changelists. Deprecated. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---import-labels)--import-labels 
    
Import labels from p4 into Git. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---import-local)--import-local 
    
By default, p4 branches are stored in _refs/remotes/p4/_ , where they will be treated as remote-tracking branches by [git-branch[1]](https://git-scm.com/docs/git-branch) and other commands. This option instead puts p4 branches in _refs/heads/p4/_. Note that future sync operations must specify `--import-local` as well so that they can find the p4 branches in refs/heads. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---max-changesn)--max-changes <n> 
    
Import at most _n_ changes, rather than the entire range of changes included in the given revision specifier. A typical usage would be use _@all_ as the revision specifier, but then to use _--max-changes 1000_ to import only the last 1000 revisions rather than the entire revision history. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---changes-block-sizen)--changes-block-size <n> 
    
The internal block size to use when converting a revision specifier such as _@all_ into a list of specific change numbers. Instead of using a single call to _p4 changes_ to find the full list of changes for the conversion, there are a sequence of calls to _p4 changes -m_ , each of which requests one block of changes of the given size. The default block size is 500, which should usually be suitable. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---keep-path)--keep-path 
    
The mapping of file names from the p4 depot path to Git, by default, involves removing the entire depot path. With this option, the full p4 depot path is retained in Git. For example, path _//depot/main/foo/bar.c_ , when imported from _//depot/main/_ , becomes _foo/bar.c_. With `--keep-path`, the Git path is instead _depot/main/foo/bar.c_. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---use-client-spec)--use-client-spec 
    
Use a client spec to find the list of interesting files in p4. See the "CLIENT SPEC" section below. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt--path)-/ <path> 
    
Exclude selected depot paths when cloning or syncing.
###  [](https://git-scm.com/docs/git-p4#_clone_options)Clone options
These options can be used in an initial _clone_ , along with the _sync_ options described above. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---destinationdirectory)--destination <directory> 
    
Where to create the Git repository. If not provided, the last component in the p4 depot path is used to create a new directory. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---bare)--bare 
    
Perform a bare clone. See [git-clone[1]](https://git-scm.com/docs/git-clone).
###  [](https://git-scm.com/docs/git-p4#_submit_options)Submit options
These options can be used to modify _git p4 submit_ behavior. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---origincommit)--origin <commit> 
    
Upstream location from which commits are identified to submit to p4. By default, this is the most recent p4 commit reachable from `HEAD`. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt--M)-M 
    
Detect renames. See [git-diff[1]](https://git-scm.com/docs/git-diff). Renames will be represented in p4 using explicit _move_ operations. There is no corresponding option to detect copies, but there are variables for both moves and copies. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---preserve-user)--preserve-user 
    
Re-author p4 changes before submitting to p4. This option requires p4 admin privileges. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---export-labels)--export-labels 
    
Export tags from Git as p4 labels. Tags found in Git are applied to the perforce working directory. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt--n)-n 


[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---dry-run)--dry-run 
    
Show just what commits would be submitted to p4; do not change state in Git or p4. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---prepare-p4-only)--prepare-p4-only 
    
Apply a commit to the p4 workspace, opening, adding and deleting files in p4 as for a normal submit operation. Do not issue the final "p4 submit", but instead print a message about how to submit manually or revert. This option always stops after the first (oldest) commit. Git tags are not exported to p4. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---shelve)--shelve 
    
Instead of submitting create a series of shelved changelists. After creating each shelve, the relevant files are reverted/deleted. If you have multiple commits pending multiple shelves will be created. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---update-shelveCHANGELIST)--update-shelve CHANGELIST 
    
Update an existing shelved changelist with this commit. Implies --shelve. Repeat for multiple shelved changelists. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---conflictaskskipquit)--conflict=(ask|skip|quit) 
    
Conflicts can occur when applying a commit to p4. When this happens, the default behavior ("ask") is to prompt whether to skip this commit and continue, or quit. This option can be used to bypass the prompt, causing conflicting commits to be automatically skipped, or to quit trying to apply commits, without prompting. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---branchbranch)--branch <branch> 
    
After submitting, sync this named branch instead of the default p4/master. See the "Sync options" section above for more information. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---commitsha1sha1sha1)--commit (<sha1>|<sha1>..<sha1>) 
    
Submit only the specified commit or range of commits, instead of the full list of changes that are in the current Git branch. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---disable-rebase)--disable-rebase 
    
Disable the automatic rebase after all commits have been successfully submitted. Can also be set with git-p4.disableRebase. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---disable-p4sync)--disable-p4sync 
    
Disable the automatic sync of p4/master from Perforce after commits have been submitted. Implies --disable-rebase. Can also be set with git-p4.disableP4Sync. Sync with origin/master still goes ahead if possible.
##  [](https://git-scm.com/docs/git-p4#_hooks_for_submit)Hooks for submit
###  [](https://git-scm.com/docs/git-p4#_p4_pre_submit)p4-pre-submit
The `p4-pre-submit` hook is executed if it exists and is executable. The hook takes no parameters and nothing from standard input. Exiting with non-zero status from this script prevents `git-p4` `submit` from launching. It can be bypassed with the `--no-verify` command line option.
One usage scenario is to run unit tests in the hook.
###  [](https://git-scm.com/docs/git-p4#_p4_prepare_changelist)p4-prepare-changelist
The `p4-prepare-changelist` hook is executed right after preparing the default changelist message and before the editor is started. It takes one parameter, the name of the file that contains the changelist text. Exiting with a non-zero status from the script will abort the process.
The purpose of the hook is to edit the message file in place, and it is not suppressed by the `--no-verify` option. This hook is called even if `--prepare-p4-only` is set.
###  [](https://git-scm.com/docs/git-p4#_p4_changelist)p4-changelist
The `p4-changelist` hook is executed after the changelist message has been edited by the user. It can be bypassed with the `--no-verify` option. It takes a single parameter, the name of the file that holds the proposed changelist text. Exiting with a non-zero status causes the command to abort.
The hook is allowed to edit the changelist file and can be used to normalize the text into some project standard format. It can also be used to refuse the Submit after inspect the message file.
###  [](https://git-scm.com/docs/git-p4#_p4_post_changelist)p4-post-changelist
The `p4-post-changelist` hook is invoked after the submit has successfully occurred in P4. It takes no parameters and is meant primarily for notification and cannot affect the outcome of the git p4 submit action.
###  [](https://git-scm.com/docs/git-p4#_rebase_options)Rebase options
These options can be used to modify _git p4 rebase_ behavior. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---import-labels-1)--import-labels 
    
Import p4 labels.
###  [](https://git-scm.com/docs/git-p4#_unshelve_options)Unshelve options 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt---origin)--origin 
    
Sets the git refspec against which the shelved P4 changelist is compared. Defaults to p4/master.
##  [](https://git-scm.com/docs/git-p4#_depot_path_syntax)DEPOT PATH SYNTAX
The p4 depot path argument to _git p4 sync_ and _git p4 clone_ can be one or more space-separated p4 depot paths, with an optional p4 revision specifier on the end: 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-depotmyproject)"//depot/my/project" 
    
Import one commit with all files in the _#head_ change under that tree. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-depotmyprojectall)"//depot/my/project@all" 
    
Import one commit for each change in the history of that depot path. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-depotmyproject16)"//depot/my/project@1,6" 
    
Import only changes 1 through 6. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-depotproj1alldepotproj2all)"//depot/proj1@all //depot/proj2@all" 
    
Import all changes from both named depot paths into a single repository. Only files below these directories are included. There is not a subdirectory in Git for each "proj1" and "proj2". You must use the `--destination` option when specifying more than one depot path. The revision specifier must be specified identically on each depot path. If there are files in the depot paths with the same name, the path with the most recently updated version of the file is the one that appears in Git.
See _p4 help revisions_ for the full syntax of p4 revision specifiers.
##  [](https://git-scm.com/docs/git-p4#_client_spec)CLIENT SPEC
The p4 client specification is maintained with the _p4 client_ command and contains among other fields, a View that specifies how the depot is mapped into the client repository. The _clone_ and _sync_ commands can consult the client spec when given the `--use-client-spec` option or when the useClientSpec variable is true. After _git p4 clone_ , the useClientSpec variable is automatically set in the repository configuration file. This allows future _git p4 submit_ commands to work properly; the submit command looks only at the variable and does not have a command-line option.
The full syntax for a p4 view is documented in _p4 help views_. _git p4_ knows only a subset of the view syntax. It understands multi-line mappings, overlays with _+_ , exclusions with _-_ and double-quotes around whitespace. Of the possible wildcards, _git p4_ only handles _…​_ , and only when it is at the end of the path. _git p4_ will complain if it encounters an unhandled wildcard.
Bugs in the implementation of overlap mappings exist. If multiple depot paths map through overlays to the same location in the repository, _git p4_ can choose the wrong one. This is hard to solve without dedicating a client spec just for _git p4_.
The name of the client can be given to _git p4_ in multiple ways. The variable _git-p4.client_ takes precedence if it exists. Otherwise, normal p4 mechanisms of determining the client are used: environment variable `P4CLIENT`, a file referenced by `P4CONFIG`, or the local host name.
##  [](https://git-scm.com/docs/git-p4#_branch_detection)BRANCH DETECTION
P4 does not have the same concept of a branch as Git. Instead, p4 organizes its content as a directory tree, where by convention different logical branches are in different locations in the tree. The _p4 branch_ command is used to maintain mappings between different areas in the tree, and indicate related content. _git p4_ can use these mappings to determine branch relationships.
If you have a repository where all the branches of interest exist as subdirectories of a single depot path, you can use `--detect-branches` when cloning or syncing to have _git p4_ automatically find subdirectories in p4, and to generate these as branches in Git.
For example, if the P4 repository structure is:
```
//depot/main/...
//depot/branch1/...
```

And "p4 branch -o branch1" shows a View line that looks like:
```
//depot/main/... //depot/branch1/...
```

Then this _git p4 clone_ command:
```
git p4 clone --detect-branches //depot@all
```

produces a separate branch in _refs/remotes/p4/_ for //depot/main, called _master_ , and one for //depot/branch1 called _depot/branch1_.
However, it is not necessary to create branches in p4 to be able to use them like branches. Because it is difficult to infer branch relationships automatically, a Git configuration setting _git-p4.branchList_ can be used to explicitly identify branch relationships. It is a list of "source:destination" pairs, like a simple p4 branch specification, where the "source" and "destination" are the path elements in the p4 repository. The example above relied on the presence of the p4 branch. Without p4 branches, the same result will occur with:
```
git init depot
cd depot
git config git-p4.branchList main:branch1
git p4 clone --detect-branches //depot@all .
```

##  [](https://git-scm.com/docs/git-p4#_performance)PERFORMANCE
The fast-import mechanism used by _git p4_ creates one pack file for each invocation of _git p4 sync_. Normally, Git garbage compression ([git-gc[1]](https://git-scm.com/docs/git-gc)) automatically compresses these to fewer pack files, but explicit invocation of _git repack -adf_ may improve performance.
##  [](https://git-scm.com/docs/git-p4#_configuration_variables)CONFIGURATION VARIABLES
The following config settings can be used to modify _git p4_ behavior. They all are in the _git-p4_ section.
###  [](https://git-scm.com/docs/git-p4#_general_variables)General variables 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4user)git-p4.user 
    
User specified as an option to all p4 commands, with _-u <user>_. The environment variable `P4USER` can be used instead. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4password)git-p4.password 
    
Password specified as an option to all p4 commands, with _-P <password>_. The environment variable `P4PASS` can be used instead. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4port)git-p4.port 
    
Port specified as an option to all p4 commands, with _-p <port>_. The environment variable `P4PORT` can be used instead. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4host)git-p4.host 
    
Host specified as an option to all p4 commands, with _-h <host>_. The environment variable `P4HOST` can be used instead. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4client)git-p4.client 
    
Client specified as an option to all p4 commands, with _-c <client>_, including the client spec. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4retries)git-p4.retries 
    
Specifies the number of times to retry a p4 command (notably, _p4 sync_) if the network times out. The default value is 3. Set the value to 0 to disable retries or if your p4 version does not support retries (pre 2012.2).
###  [](https://git-scm.com/docs/git-p4#_clone_and_sync_variables)Clone and sync variables 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4syncFromOrigin)git-p4.syncFromOrigin 
    
Because importing commits from other Git repositories is much faster than importing them from p4, a mechanism exists to find p4 changes first in Git remotes. If branches exist under _refs/remote/origin/p4_ , those will be fetched and used when syncing from p4. This variable can be set to _false_ to disable this behavior. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4branchUser)git-p4.branchUser 
    
One phase in branch detection involves looking at p4 branches to find new ones to import. By default, all branches are inspected. This option limits the search to just those owned by the single user named in the variable. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4branchList)git-p4.branchList 
    
List of branches to be imported when branch detection is enabled. Each entry should be a pair of branch names separated by a colon (:). This example declares that both branchA and branchB were created from main:
```
git config       git-p4.branchList main:branchA
git config --add git-p4.branchList main:branchB
```


[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4ignoredP4Labels)git-p4.ignoredP4Labels 
    
List of p4 labels to ignore. This is built automatically as unimportable labels are discovered. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4importLabels)git-p4.importLabels 
    
Import p4 labels into git, as per --import-labels. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4labelImportRegexp)git-p4.labelImportRegexp 
    
Only p4 labels matching this regular expression will be imported. The default value is _[a-zA-Z0-9_\\-.]+$_. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4useClientSpec)git-p4.useClientSpec 
    
Specify that the p4 client spec should be used to identify p4 depot paths of interest. This is equivalent to specifying the option `--use-client-spec`. See the "CLIENT SPEC" section above. This variable is a boolean, not the name of a p4 client. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4pathEncoding)git-p4.pathEncoding 
    
Perforce keeps the encoding of a path as given by the originating OS. Git expects paths encoded as UTF-8. Use this config to tell git-p4 what encoding Perforce had used for the paths. This encoding is used to transcode the paths to UTF-8. As an example, Perforce on Windows often uses "cp1252" to encode path names. If this option is passed into a p4 clone request, it is persisted in the resulting new git repo. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4metadataDecodingStrategy)git-p4.metadataDecodingStrategy 
    
Perforce keeps the encoding of a changelist descriptions and user full names as stored by the client on a given OS. The p4v client uses the OS-local encoding, and so different users can end up storing different changelist descriptions or user full names in different encodings, in the same depot. Git tolerates inconsistent/incorrect encodings in commit messages and author names, but expects them to be specified in utf-8. git-p4 can use three different decoding strategies in handling the encoding uncertainty in Perforce: _passthrough_ simply passes the original bytes through from Perforce to git, creating usable but incorrectly-encoded data when the Perforce data is encoded as anything other than utf-8. _strict_ expects the Perforce data to be encoded as utf-8, and fails to import when this is not true. _fallback_ attempts to interpret the data as utf-8, and otherwise falls back to using a secondary encoding - by default the common windows encoding _cp-1252_ - with upper-range bytes escaped if decoding with the fallback encoding also fails. Under python2 the default strategy is _passthrough_ for historical reasons, and under python3 the default is _fallback_. When _strict_ is selected and decoding fails, the error message will propose changing this config parameter as a workaround. If this option is passed into a p4 clone request, it is persisted into the resulting new git repo. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4metadataFallbackEncoding)git-p4.metadataFallbackEncoding 
    
Specify the fallback encoding to use when decoding Perforce author names and changelists descriptions using the _fallback_ strategy (see git-p4.metadataDecodingStrategy). The fallback encoding will only be used when decoding as utf-8 fails. This option defaults to cp1252, a common windows encoding. If this option is passed into a p4 clone request, it is persisted into the resulting new git repo. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4largeFileSystem)git-p4.largeFileSystem 
    
Specify the system that is used for large (binary) files. Please note that large file systems do not support the _git p4 submit_ command. Only Git LFS is implemented right now (see <https://git-lfs.github.com/> for more information). Download and install the Git LFS command line extension to use this option and configure it like this:
```
git config       git-p4.largeFileSystem GitLFS
```


[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4largeFileExtensions)git-p4.largeFileExtensions 
    
All files matching a file extension in the list will be processed by the large file system. Do not prefix the extensions with _._. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4largeFileThreshold)git-p4.largeFileThreshold 
    
All files with an uncompressed size exceeding the threshold will be processed by the large file system. By default the threshold is defined in bytes. Add the suffix k, m, or g to change the unit. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4largeFileCompressedThreshold)git-p4.largeFileCompressedThreshold 
    
All files with a compressed size exceeding the threshold will be processed by the large file system. This option might slow down your clone/sync process. By default the threshold is defined in bytes. Add the suffix k, m, or g to change the unit. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4largeFilePush)git-p4.largeFilePush 
    
Boolean variable which defines if large files are automatically pushed to a server. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4keepEmptyCommits)git-p4.keepEmptyCommits 
    
A changelist that contains only excluded files will be imported as an empty commit if this boolean option is set to true. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4mapUser)git-p4.mapUser 
    
Map a P4 user to a name and email address in Git. Use a string with the following format to create a mapping:
```
git config --add git-p4.mapUser "p4user = First Last <mail@address.com>"
```

A mapping will override any user information from P4. Mappings for multiple P4 user can be defined.
###  [](https://git-scm.com/docs/git-p4#_submit_variables)Submit variables 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4detectRenames)git-p4.detectRenames 
    
Detect renames. See [git-diff[1]](https://git-scm.com/docs/git-diff). This can be true, false, or a score as expected by _git diff -M_. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4detectCopies)git-p4.detectCopies 
    
Detect copies. See [git-diff[1]](https://git-scm.com/docs/git-diff). This can be true, false, or a score as expected by _git diff -C_. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4detectCopiesHarder)git-p4.detectCopiesHarder 
    
Detect copies harder. See [git-diff[1]](https://git-scm.com/docs/git-diff). A boolean. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4preserveUser)git-p4.preserveUser 
    
On submit, re-author changes to reflect the Git author, regardless of who invokes _git p4 submit_. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4allowMissingP4Users)git-p4.allowMissingP4Users 
    
When _preserveUser_ is true, _git p4_ normally dies if it cannot find an author in the p4 user map. This setting submits the change regardless. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4skipSubmitEdit)git-p4.skipSubmitEdit 
    
The submit process invokes the editor before each p4 change is submitted. If this setting is true, though, the editing step is skipped. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4skipSubmitEditCheck)git-p4.skipSubmitEditCheck 
    
After editing the p4 change message, _git p4_ makes sure that the description really was changed by looking at the file modification time. This option disables that test. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4allowSubmit)git-p4.allowSubmit 
    
By default, any branch can be used as the source for a _git p4 submit_ operation. This configuration variable, if set, permits only the named branches to be used as submit sources. Branch names must be the short names (no "refs/heads/"), and should be separated by commas (","), with no spaces. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4skipUserNameCheck)git-p4.skipUserNameCheck 
    
If the user running _git p4 submit_ does not exist in the p4 user map, _git p4_ exits. This option can be used to force submission regardless. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4attemptRCSCleanup)git-p4.attemptRCSCleanup 
    
If enabled, _git p4 submit_ will attempt to cleanup RCS keywords ($Header$, etc). These would otherwise cause merge conflicts and prevent the submit going ahead. This option should be considered experimental at present. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4exportLabels)git-p4.exportLabels 
    
Export Git tags to p4 labels, as per --export-labels. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4labelExportRegexp)git-p4.labelExportRegexp 
    
Only p4 labels matching this regular expression will be exported. The default value is _[a-zA-Z0-9_\\-.]+$_. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4conflict)git-p4.conflict 
    
Specify submit behavior when a conflict with p4 is found, as per --conflict. The default behavior is _ask_. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4disableRebase)git-p4.disableRebase 
    
Do not rebase the tree against p4/master following a submit. 

[](https://git-scm.com/docs/git-p4#Documentation/git-p4.txt-git-p4disableP4Sync)git-p4.disableP4Sync 
    
Do not sync p4/master with Perforce following a submit. Implies git-p4.disableRebase.
##  [](https://git-scm.com/docs/git-p4#_implementation_details)IMPLEMENTATION DETAILS
  * Changesets from p4 are imported using Git fast-import.
  * Cloning or syncing does not require a p4 client; file contents are collected using _p4 print_.
  * Submitting requires a p4 client, which is not in the same location as the Git repository. Patches are applied, one at a time, to this p4 client and submitted from there.
  * Each commit imported by _git p4_ has a line at the end of the log message indicating the p4 depot location and change number. This line is used by later _git p4 sync_ operations to know which p4 changes are new.


##  [](https://git-scm.com/docs/git-p4#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### p4
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
