[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --fast-version-control
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
    * [NAME](https://git-scm.com/docs/git-worktree#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-worktree#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-worktree#_description)
    * [COMMANDS](https://git-scm.com/docs/git-worktree#_commands)
    * [OPTIONS](https://git-scm.com/docs/git-worktree#_options)
    * [REFS](https://git-scm.com/docs/git-worktree#_refs)
    * [CONFIGURATION FILE](https://git-scm.com/docs/git-worktree#_configuration_file)
    * [DETAILS](https://git-scm.com/docs/git-worktree#_details)
    * [LIST OUTPUT FORMAT](https://git-scm.com/docs/git-worktree#_list_output_format)
    * [EXAMPLES](https://git-scm.com/docs/git-worktree#_examples)
    * [CONFIGURATION](https://git-scm.com/docs/git-worktree#_configuration)
    * [BUGS](https://git-scm.com/docs/git-worktree#_bugs)
    * [GIT](https://git-scm.com/docs/git-worktree#_git)


[ English ▾](https://git-scm.com/docs/git-worktree)
Localized versions of **git-worktree** manual
  1. [English ](https://git-scm.com/docs/git-worktree)
  2. [Français ](https://git-scm.com/docs/git-worktree/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-worktree/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-worktree/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-worktree/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-worktree)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-worktree) git-worktree last updated in 2.53.0
Changes in the **git-worktree** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-worktree/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-worktree/2.52.0)
  3. 2.48.1 → 2.51.2 no changes
  4. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-worktree/2.48.0)
  5. 2.43.2 → 2.47.3 no changes
  6. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-worktree/2.43.1)
  7. 2.42.2 → 2.43.0 no changes
  8. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-worktree/2.42.1)
  9. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-worktree/2.42.0)
  10. 2.39.1 → 2.41.3 no changes
  11. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-worktree/2.39.0)
  12. 2.36.1 → 2.38.5 no changes
  13. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-worktree/2.36.0)
  14. 2.35.1 → 2.35.8 no changes
  15. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-worktree/2.35.0)
  16. 2.33.1 → 2.34.8 no changes
  17. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-worktree/2.33.0)
  18. 2.31.1 → 2.32.7 no changes
  19. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-worktree/2.31.0)
  20. 2.30.1 → 2.30.9 no changes
  21. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-worktree/2.30.0)
  22. 2.29.1 → 2.29.3 no changes
  23. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-worktree/2.29.0)
  24. 2.28.1 no changes
  25. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-worktree/2.28.0)
  26. 2.22.1 → 2.27.1 no changes
  27. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-worktree/2.22.0)
  28. 2.20.1 → 2.21.4 no changes
  29. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-worktree/2.20.0)
  30. 2.19.3 → 2.19.6 no changes
  31. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-worktree/2.19.2)
  32. 2.19.1 no changes
  33. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-worktree/2.19.0)
  34. 2.18.1 → 2.18.5 no changes
  35. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-worktree/2.18.0)
  36. 2.17.1 → 2.17.6 no changes
  37. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-worktree/2.17.0)
  38. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-worktree/2.16.6)
  39. 2.14.6 → 2.15.4 no changes
  40. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-worktree/2.13.7)
  41. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-worktree/2.12.5)
  42. 2.11.4 no changes
  43. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-worktree/2.10.5)
  44. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-worktree/2.9.5)
  45. 2.8.6 no changes
  46. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-worktree/2.7.6)
  47. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-worktree/2.6.7)
  48. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-worktree/2.5.6)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-worktree#_name)NAME
git-worktree - Manage multiple working trees
##  [](https://git-scm.com/docs/git-worktree#_synopsis)SYNOPSIS
```
git worktree add [-f] [--detach] [--checkout] [--lock [--reason _<string>_]]
		 [--orphan] [(-b | -B) _<new-branch>_] _<path>_ [_<commit-ish>_]
git worktree list [-v | --porcelain [-z]]
git worktree lock [--reason _<string>_] _<worktree>_
git worktree move _<worktree>_ _<new-path>_
git worktree prune [-n] [-v] [--expire _<expire>_]
git worktree remove [-f] _<worktree>_
git worktree repair [_<path>_…​]
git worktree unlock _<worktree>_
```

##  [](https://git-scm.com/docs/git-worktree#_description)DESCRIPTION
Manage multiple working trees attached to the same repository.
A git repository can support multiple working trees, allowing you to check out more than one branch at a time. With `git` `worktree` `add` a new working tree is associated with the repository, along with additional metadata that differentiates that working tree from others in the same repository. The working tree, along with this metadata, is called a "worktree".
This new worktree is called a "linked worktree" as opposed to the "main worktree" prepared by [git-init[1]](https://git-scm.com/docs/git-init) or [git-clone[1]](https://git-scm.com/docs/git-clone). A repository has one main worktree (if it’s not a bare repository) and zero or more linked worktrees. When you are done with a linked worktree, remove it with `git` `worktree` `remove`.
In its simplest form, `git` `worktree` `add` _< path>_ automatically creates a new branch whose name is the final component of _< path>_, which is convenient if you plan to work on a new topic. For instance, `git` `worktree` `add` `../hotfix` creates new branch `hotfix` and checks it out at path `../hotfix`. To instead work on an existing branch in a new worktree, use `git` `worktree` `add` _< path>_ _< branch>_. On the other hand, if you just plan to make some experimental changes or do testing without disturbing existing development, it is often convenient to create a _throwaway_ worktree not associated with any branch. For instance, `git` `worktree` `add` `-d` _< path>_ creates a new worktree with a detached `HEAD` at the same commit as the current branch.
If a working tree is deleted without using `git` `worktree` `remove`, then its associated administrative files, which reside in the repository (see "DETAILS" below), will eventually be removed automatically (see `gc.worktreePruneExpire` in [git-config[1]](https://git-scm.com/docs/git-config)), or you can run `git` `worktree` `prune` in the main or any linked worktree to clean up any stale administrative files.
If the working tree for a linked worktree is stored on a portable device or network share which is not always mounted, you can prevent its administrative files from being pruned by issuing the `git` `worktree` `lock` command, optionally specifying `--reason` to explain why the worktree is locked.
##  [](https://git-scm.com/docs/git-worktree#_commands)COMMANDS 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-addpathcommit-ish)`add` _< path>_ [_< commit-ish>_] 
    
Create a worktree at _< path>_ and checkout _< commit-ish>_ into it. The new worktree is linked to the current repository, sharing everything except per-worktree files such as `HEAD`, `index`, etc. As a convenience, _< commit-ish>_ may be a bare "`-`", which is synonymous with `@{-1}`.
If _< commit-ish>_ is a branch name (call it _< branch>_) and is not found, and neither `-b` nor `-B` nor `--detach` are used, but there does exist a tracking branch in exactly one remote (call it _< remote>_) with a matching name, treat as equivalent to:
```
$ git worktree add --track -b <branch> <path> <remote>/<branch>
```

If the branch exists in multiple remotes and one of them is named by the `checkout.defaultRemote` configuration variable, we’ll use that one for the purposes of disambiguation, even if the _< branch>_ isn’t unique across all remotes. Set it to e.g. `checkout.defaultRemote=origin` to always checkout remote branches from there if _< branch>_ is ambiguous but exists on the `origin` remote. See also `checkout.defaultRemote` in [git-config[1]](https://git-scm.com/docs/git-config).
If _< commit-ish>_ is omitted and neither `-b` nor `-B` nor `--detach` used, then, as a convenience, the new worktree is associated with a branch (call it _< branch>_) named after `$`(`basename` _< path>_). If _< branch>_ doesn’t exist, a new branch based on `HEAD` is automatically created as if `-b` _< branch>_ was given. If _< branch>_ does exist, it will be checked out in the new worktree, if it’s not checked out anywhere else, otherwise the command will refuse to create the worktree (unless `--force` is used).
If _< commit-ish>_ is omitted, neither `--detach`, or `--orphan` is used, and there are no valid local branches (or remote branches if `--guess-remote` is specified) then, as a convenience, the new worktree is associated with a new unborn branch named _< branch>_ (after `$`(`basename` _< path>_) if neither `-b` or `-B` is used) as if `--orphan` was passed to the command. In the event the repository has a remote and `--guess-remote` is used, but no remote or local branches exist, then the command fails with a warning reminding the user to fetch from their remote first (or override by using `-f`/`--force`). 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-list)`list` 
    
List details of each worktree. The main worktree is listed first, followed by each of the linked worktrees. The output details include whether the worktree is bare, the revision currently checked out, the branch currently checked out (or "detached HEAD" if none), "locked" if the worktree is locked, "prunable" if the worktree can be pruned by the `prune` command. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-lock)`lock` 
    
If a worktree is on a portable device or network share which is not always mounted, lock it to prevent its administrative files from being pruned automatically. This also prevents it from being moved or deleted. Optionally, specify a reason for the lock with `--reason`. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-move)`move` 
    
Move a worktree to a new location. Note that the main worktree or linked worktrees containing submodules cannot be moved with this command. (The `git` `worktree` `repair` command, however, can reestablish the connection with linked worktrees if you move the main worktree manually.) 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-prune)`prune` 
    
Prune worktree information in `$GIT_DIR/worktrees`. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-remove)`remove` 
    
Remove a worktree. Only clean worktrees (no untracked files and no modification in tracked files) can be removed. Unclean worktrees or ones with submodules can be removed with `--force`. The main worktree cannot be removed. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-repairpath)`repair` [_< path>_...] 
    
Repair worktree administrative files, if possible, if they have become corrupted or outdated due to external factors.
For instance, if the main worktree (or bare repository) is moved, linked worktrees will be unable to locate it. Running `repair` in the main worktree will reestablish the connection from linked worktrees back to the main worktree.
Similarly, if the working tree for a linked worktree is moved without using `git` `worktree` `move`, the main worktree (or bare repository) will be unable to locate it. Running `repair` within the recently-moved worktree will reestablish the connection. If multiple linked worktrees are moved, running `repair` from any worktree with each tree’s new _< path>_ as an argument, will reestablish the connection to all the specified paths.
If both the main worktree and linked worktrees have been moved or copied manually, then running `repair` in the main worktree and specifying the new _< path>_ of each linked worktree will reestablish all connections in both directions. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-unlock)`unlock` 
    
Unlock a worktree, allowing it to be pruned, moved or deleted.
##  [](https://git-scm.com/docs/git-worktree#_options)OPTIONS 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--f)`-f` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---force)`--force` 
    
By default, `add` refuses to create a new worktree when _< commit-ish>_ is a branch name and is already checked out by another worktree, or if _< path>_ is already assigned to some worktree but is missing (for instance, if _< path>_ was deleted manually). This option overrides these safeguards. To add a missing but locked worktree path, specify `--force` twice.
`move` refuses to move a locked worktree unless `--force` is specified twice. If the destination is already assigned to some other worktree but is missing (for instance, if _< new-path>_ was deleted manually), then `--force` allows the move to proceed; use `--force` twice if the destination is locked.
`remove` refuses to remove an unclean worktree unless `--force` is used. To remove a locked worktree, specify `--force` twice. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--bnew-branch)`-b` _< new-branch>_ 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--Bnew-branch)`-B` _< new-branch>_ 
    
With `add`, create a new branch named _< new-branch>_ starting at _< commit-ish>_, and check out _< new-branch>_ into the new worktree. If _< commit-ish>_ is omitted, it defaults to `HEAD`. By default, `-b` refuses to create a new branch if it already exists. `-B` overrides this safeguard, resetting _< new-branch>_ to _< commit-ish>_. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--d)`-d` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---detach)`--detach` 
    
With `add`, detach `HEAD` in the new worktree. See "DETACHED HEAD" in [git-checkout[1]](https://git-scm.com/docs/git-checkout). 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---checkout)`--checkout` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---no-checkout)`--no-checkout` 
    
By default, `add` checks out _< commit-ish>_, however, `--no-checkout` can be used to suppress checkout in order to make customizations, such as configuring sparse-checkout. See "Sparse checkout" in [git-read-tree[1]](https://git-scm.com/docs/git-read-tree). 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---guess-remote)`--guess-remote` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---no-guess-remote)`--no-guess-remote` 
    
With `worktree` `add` _< path>_, without _< commit-ish>_, instead of creating a new branch from `HEAD`, if there exists a tracking branch in exactly one remote matching the basename of _< path>_, base the new branch on the remote-tracking branch, and mark the remote-tracking branch as "upstream" from the new branch.
This can also be set up as the default behaviour by using the `worktree.guessRemote` config option. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---relative-paths)`--relative-paths` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---no-relative-paths)`--no-relative-paths` 
    
Link worktrees using relative paths or absolute paths (default). Overrides the `worktree.useRelativePaths` config option, see [git-config[1]](https://git-scm.com/docs/git-config).
With `repair`, the linking files will be updated if there’s an absolute/relative mismatch, even if the links are correct. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---track)`--track` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---no-track)`--no-track` 
    
When creating a new branch, if _< commit-ish>_ is a branch, mark it as "upstream" from the new branch. This is the default if _< commit-ish>_ is a remote-tracking branch. See `--track` in [git-branch[1]](https://git-scm.com/docs/git-branch) for details. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---lock)`--lock` 
    
Keep the worktree locked after creation. This is the equivalent of `git` `worktree` `lock` after `git` `worktree` `add`, but without a race condition. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--n)`-n` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---dry-run)`--dry-run` 
    
With `prune`, do not remove anything; just report what it would remove. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---orphan)`--orphan` 
    
With `add`, make the new worktree and index empty, associating the worktree with a new unborn branch named _< new-branch>_. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---porcelain)`--porcelain` 
    
With `list`, output in an easy-to-parse format for scripts. This format will remain stable across Git versions and regardless of user configuration. It is recommended to combine this with `-z`. See below for details. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--z)`-z` 
    
Terminate each line with a _NUL_ rather than a newline when `--porcelain` is specified with `list`. This makes it possible to parse the output when a worktree path contains a newline character. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--q)`-q` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---quiet)`--quiet` 
    
With `add`, suppress feedback messages. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt--v)`-v` 


[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---verbose)`--verbose` 
    
With `prune`, report all removals.
With `list`, output additional information about worktrees (see below). 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---expiretime)`--expire` _< time>_ 
    
With `prune`, only expire unused worktrees older than _< time>_.
With `list`, annotate missing worktrees as prunable if they are older than _< time>_. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt---reasonstring)`--reason` _< string>_ 
    
With `lock` or with `add` `--lock`, an explanation why the worktree is locked. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-worktree)_< worktree>_ 
    
Worktrees can be identified by path, either relative or absolute.
If the last path components in the worktree’s path is unique among worktrees, it can be used to identify a worktree. For example if you only have two worktrees, at `/abc/def/ghi` and `/abc/def/ggg`, then `ghi` or `def/ghi` is enough to point to the former worktree.
##  [](https://git-scm.com/docs/git-worktree#_refs)REFS
When using multiple worktrees, some refs are shared between all worktrees, but others are specific to an individual worktree. One example is `HEAD`, which is different for each worktree. This section is about the sharing rules and how to access refs of one worktree from another.
In general, all pseudo refs are per-worktree and all refs starting with `refs/` are shared. Pseudo refs are ones like `HEAD` which are directly under `$GIT_DIR` instead of inside `$GIT_DIR/refs`. There are exceptions, however: refs inside `refs/bisect`, `refs/worktree` and `refs/rewritten` are not shared.
Refs that are per-worktree can still be accessed from another worktree via two special paths, `main-worktree` and `worktrees`. The former gives access to per-worktree refs of the main worktree, while the latter to all linked worktrees.
For example, `main-worktree/HEAD` or `main-worktree/refs/bisect/good` resolve to the same value as the main worktree’s `HEAD` and `refs/bisect/good` respectively. Similarly, `worktrees/foo/HEAD` or `worktrees/bar/refs/bisect/bad` are the same as `$GIT_COMMON_DIR/worktrees/foo/HEAD` and `$GIT_COMMON_DIR/worktrees/bar/refs/bisect/bad`.
To access refs, it’s best not to look inside `$GIT_DIR` directly. Instead use commands such as [git-rev-parse[1]](https://git-scm.com/docs/git-rev-parse) or [git-update-ref[1]](https://git-scm.com/docs/git-update-ref) which will handle refs correctly.
##  [](https://git-scm.com/docs/git-worktree#_configuration_file)CONFIGURATION FILE
By default, the repository `config` file is shared across all worktrees. If the config variables `core.bare` or `core.worktree` are present in the common config file and `extensions.worktreeConfig` is disabled, then they will be applied to the main worktree only.
In order to have worktree-specific configuration, you can turn on the `worktreeConfig` extension, e.g.:
```
$ git config extensions.worktreeConfig true
```

In this mode, specific configuration stays in the path pointed by `git` `rev-parse` `--git-path` `config.worktree`. You can add or update configuration in this file with `git` `config` `--worktree`. Older Git versions will refuse to access repositories with this extension.
Note that in this file, the exception for `core.bare` and `core.worktree` is gone. If they exist in `$GIT_DIR/config`, you must move them to the `config.worktree` of the main worktree. You may also take this opportunity to review and move other configuration that you do not want to share to all worktrees:
  * `core.worktree` should never be shared.
  * `core.bare` should not be shared if the value is `core.bare=true`.
  * `core.sparseCheckout` should not be shared, unless you are sure you always use sparse checkout for all worktrees.


See the documentation of `extensions.worktreeConfig` in [git-config[1]](https://git-scm.com/docs/git-config) for more details.
##  [](https://git-scm.com/docs/git-worktree#_details)DETAILS
Each linked worktree has a private sub-directory in the repository’s `$GIT_DIR/worktrees` directory. The private sub-directory’s name is usually the base name of the linked worktree’s path, possibly appended with a number to make it unique. For example, when `$GIT_DIR=/path/main/.git` the command `git` `worktree` `add` `/path/other/test-next` `next` creates the linked worktree in `/path/other/test-next` and also creates a `$GIT_DIR/worktrees/test-next` directory (or `$GIT_DIR/worktrees/test-next1` if `test-next` is already taken).
Within a linked worktree, `$GIT_DIR` is set to point to this private directory (e.g. `/path/main/.git/worktrees/test-next` in the example) and `$GIT_COMMON_DIR` is set to point back to the main worktree’s `$GIT_DIR` (e.g. `/path/main/.git`). These settings are made in a `.git` file located at the top directory of the linked worktree.
Path resolution via `git` `rev-parse` `--git-path` uses either `$GIT_DIR` or `$GIT_COMMON_DIR` depending on the path. For example, in the linked worktree `git` `rev-parse` `--git-path` `HEAD` returns `/path/main/.git/worktrees/test-next/HEAD` (not `/path/other/test-next/.git/HEAD` or `/path/main/.git/HEAD`) while `git` `rev-parse` `--git-path` `refs/heads/master` uses `$GIT_COMMON_DIR` and returns `/path/main/.git/refs/heads/master`, since refs are shared across all worktrees, except `refs/bisect`, `refs/worktree` and `refs/rewritten`.
See [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout) for more information. The rule of thumb is do not make any assumption about whether a path belongs to `$GIT_DIR` or `$GIT_COMMON_DIR` when you need to directly access something inside `$GIT_DIR`. Use `git` `rev-parse` `--git-path` to get the final path.
If you manually move a linked worktree, you need to update the `gitdir` file in the entry’s directory. For example, if a linked worktree is moved to `/newpath/test-next` and its `.git` file points to `/path/main/.git/worktrees/test-next`, then update `/path/main/.git/worktrees/test-next/gitdir` to reference `/newpath/test-next` instead. Better yet, run `git` `worktree` `repair` to reestablish the connection automatically.
To prevent a `$GIT_DIR/worktrees` entry from being pruned (which can be useful in some situations, such as when the entry’s worktree is stored on a portable device), use the `git` `worktree` `lock` command, which adds a file named `locked` to the entry’s directory. The file contains the reason in plain text. For example, if a linked worktree’s `.git` file points to `/path/main/.git/worktrees/test-next` then a file named `/path/main/.git/worktrees/test-next/locked` will prevent the `test-next` entry from being pruned. See [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout) for details.
When `extensions.worktreeConfig` is enabled, the config file `.git/worktrees/`_< id>_`/config.worktree` is read after `.git/config` is.
##  [](https://git-scm.com/docs/git-worktree#_list_output_format)LIST OUTPUT FORMAT
The `worktree` `list` command has two output formats. The default format shows the details on a single line with columns. For example:
```
$ git worktree list
/path/to/bare-source            (bare)
/path/to/linked-worktree        abcd1234 [master]
/path/to/other-linked-worktree  1234abc  (detached HEAD)
```

The command also shows annotations for each worktree, according to its state. These annotations are:
  * `locked`, if the worktree is locked.
  * `prunable`, if the worktree can be pruned via `git` `worktree` `prune`.


```
$ git worktree list
/path/to/linked-worktree    abcd1234 [master]
/path/to/locked-worktree    acbd5678 (brancha) locked
/path/to/prunable-worktree  5678abc  (detached HEAD) prunable
```

For these annotations, a reason might also be available and this can be seen using the verbose mode. The annotation is then moved to the next line indented followed by the additional information.
```
$ git worktree list --verbose
/path/to/linked-worktree              abcd1234 [master]
/path/to/locked-worktree-no-reason    abcd5678 (detached HEAD) locked
/path/to/locked-worktree-with-reason  1234abcd (brancha)
	locked: worktree path is mounted on a portable device
/path/to/prunable-worktree            5678abc1 (detached HEAD)
	prunable: gitdir file points to non-existent location
```

Note that the annotation is moved to the next line if the additional information is available, otherwise it stays on the same line as the worktree itself.
###  [](https://git-scm.com/docs/git-worktree#_porcelain_format)Porcelain Format
The porcelain format has a line per attribute. If `-z` is given then the lines are terminated with NUL rather than a newline. Attributes are listed with a label and value separated by a single space. Boolean attributes (like `bare` and `detached`) are listed as a label only, and are present only if the value is true. Some attributes (like `locked`) can be listed as a label only or with a value depending upon whether a reason is available. The first attribute of a worktree is always `worktree`, an empty line indicates the end of the record. For example:
```
$ git worktree list --porcelain
worktree /path/to/bare-source
bare

worktree /path/to/linked-worktree
HEAD abcd1234abcd1234abcd1234abcd1234abcd1234
branch refs/heads/master

worktree /path/to/other-linked-worktree
HEAD 1234abc1234abc1234abc1234abc1234abc1234a
detached

worktree /path/to/linked-worktree-locked-no-reason
HEAD 5678abc5678abc5678abc5678abc5678abc5678c
branch refs/heads/locked-no-reason
locked

worktree /path/to/linked-worktree-locked-with-reason
HEAD 3456def3456def3456def3456def3456def3456b
branch refs/heads/locked-with-reason
locked reason why is locked

worktree /path/to/linked-worktree-prunable
HEAD 1233def1234def1234def1234def1234def1234b
detached
prunable gitdir file points to non-existent location
```

Unless `-z` is used any "unusual" characters in the lock reason such as newlines are escaped and the entire reason is quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). For Example:
```
$ git worktree list --porcelain
...
locked "reason\nwhy is locked"
...
```

##  [](https://git-scm.com/docs/git-worktree#_examples)EXAMPLES
You are in the middle of a refactoring session and your boss comes in and demands that you fix something immediately. You might typically use [git-stash[1]](https://git-scm.com/docs/git-stash) to store your changes away temporarily, however, your working tree is in such a state of disarray (with new, moved, and removed files, and other bits and pieces strewn around) that you don’t want to risk disturbing any of it. Instead, you create a temporary linked worktree to make the emergency fix, remove it when done, and then resume your earlier refactoring session.
```
$ git worktree add -b emergency-fix ../temp master
$ pushd ../temp
# ... hack hack hack ...
$ git commit -a -m 'emergency fix for boss'
$ popd
$ git worktree remove ../temp
```

##  [](https://git-scm.com/docs/git-worktree#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-worktreeguessRemote)`worktree.guessRemote` 
    
If no branch is specified and neither `-b` nor `-B` nor `--detach` is used, then `git` `worktree` `add` defaults to creating a new branch from HEAD. If `worktree.guessRemote` is set to true, `worktree` `add` tries to find a remote-tracking branch whose name uniquely matches the new branch name. If such a branch exists, it is checked out and set as "upstream" for the new branch. If no such match can be found, it falls back to creating a new branch from the current `HEAD`. 

[](https://git-scm.com/docs/git-worktree#Documentation/git-worktree.txt-worktreeuseRelativePaths)`worktree.useRelativePaths` 
    
Link worktrees using relative paths (when "`true`") or absolute paths (when "`false`"). This is particularly useful for setups where the repository and worktrees may be moved between different locations or environments. Defaults to "`false`".
Note that setting `worktree.useRelativePaths` to "`true`" implies enabling the `extensions.relativeWorktrees` config (see [git-config[1]](https://git-scm.com/docs/git-config)), thus making it incompatible with older versions of Git.
##  [](https://git-scm.com/docs/git-worktree#_bugs)BUGS
Multiple checkout in general is still experimental, and the support for submodules is incomplete. It is NOT recommended to make multiple checkouts of a superproject.
##  [](https://git-scm.com/docs/git-worktree#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### worktree
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
