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
    * [NAME](https://git-scm.com/docs/git-merge#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-merge#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-merge#_description)
    * [OPTIONS](https://git-scm.com/docs/git-merge#_options)
    * [PRE-MERGE CHECKS](https://git-scm.com/docs/git-merge#_pre_merge_checks)
    * [FAST-FORWARD MERGE](https://git-scm.com/docs/git-merge#_fast_forward_merge)
    * [TRUE MERGE](https://git-scm.com/docs/git-merge#_true_merge)
    * [MERGING TAG](https://git-scm.com/docs/git-merge#_merging_tag)
    * [HOW CONFLICTS ARE PRESENTED](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented)
    * [HOW TO RESOLVE CONFLICTS](https://git-scm.com/docs/git-merge#_how_to_resolve_conflicts)
    * [EXAMPLES](https://git-scm.com/docs/git-merge#_examples)
    * [MERGE STRATEGIES](https://git-scm.com/docs/git-merge#_merge_strategies)
    * [CONFIGURATION](https://git-scm.com/docs/git-merge#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-merge#_see_also)
    * [GIT](https://git-scm.com/docs/git-merge#_git)


[ English ▾](https://git-scm.com/docs/git-merge)
Localized versions of **git-merge** manual
  1. [English ](https://git-scm.com/docs/git-merge)
  2. [Français ](https://git-scm.com/docs/git-merge/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-merge/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-merge/sv)
  5. [українська мова ](https://git-scm.com/docs/git-merge/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-merge/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-merge)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-merge) git-merge last updated in 2.53.0
Changes in the **git-merge** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-merge/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-merge/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-merge/2.51.0)
  5. 2.50.1 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-merge/2.50.0)
  7. 2.49.1 no changes
  8. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-merge/2.49.0)
  9. 2.47.1 → 2.48.2 no changes
  10. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git-merge/2.47.0)
  11. 2.43.2 → 2.46.4 no changes
  12. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-merge/2.43.1)
  13. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-merge/2.43.0)
  14. 2.42.1 → 2.42.4 no changes
  15. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-merge/2.42.0)
  16. 2.39.4 → 2.41.3 no changes
  17. [2.39.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-04-17_ ](https://git-scm.com/docs/git-merge/2.39.3)
  18. 2.38.1 → 2.39.2 no changes
  19. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-merge/2.38.0)
  20. 2.35.1 → 2.37.7 no changes
  21. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-merge/2.35.0)
  22. 2.34.1 → 2.34.8 no changes
  23. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-merge/2.34.0)
  24. 2.33.2 → 2.33.8 no changes
  25. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git-merge/2.33.1)
  26. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-merge/2.33.0)
  27. 2.30.1 → 2.32.7 no changes
  28. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-merge/2.30.0)
  29. 2.29.1 → 2.29.3 no changes
  30. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-merge/2.29.0)
  31. 2.27.1 → 2.28.1 no changes
  32. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-merge/2.27.0)
  33. 2.25.1 → 2.26.3 no changes
  34. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-merge/2.25.0)
  35. 2.24.1 → 2.24.4 no changes
  36. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-merge/2.24.0)
  37. 2.23.1 → 2.23.4 no changes
  38. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-merge/2.23.0)
  39. 2.22.2 → 2.22.5 no changes
  40. [2.22.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-11_ ](https://git-scm.com/docs/git-merge/2.22.1)
  41. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-merge/2.22.0)
  42. 2.20.1 → 2.21.4 no changes
  43. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-merge/2.20.0)
  44. 2.19.1 → 2.19.6 no changes
  45. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-merge/2.19.0)
  46. 2.18.1 → 2.18.5 no changes
  47. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-merge/2.18.0)
  48. 2.17.1 → 2.17.6 no changes
  49. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-merge/2.17.0)
  50. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-merge/2.16.6)
  51. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-merge/2.15.4)
  52. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-merge/2.14.6)
  53. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-merge/2.13.7)
  54. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-merge/2.12.5)
  55. 2.10.5 → 2.11.4 no changes
  56. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-merge/2.9.5)
  57. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-merge/2.8.6)
  58. 2.7.6 no changes
  59. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-merge/2.6.7)
  60. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-merge/2.5.6)
  61. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-merge/2.4.12)
  62. 2.3.10 no changes
  63. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-merge/2.2.3)
  64. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-merge/2.1.4)
  65. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-merge/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-merge#_name)NAME
git-merge - Join two or more development histories together
##  [](https://git-scm.com/docs/git-merge#_synopsis)SYNOPSIS
```
git merge [-n] [--stat] [--compact-summary] [--no-commit] [--squash] [--[no-]edit]
	[--no-verify] [-s _<strategy>_] [-X _<strategy-option>_] [-S[_<keyid>_]]
	[--[no-]allow-unrelated-histories]
	[--[no-]rerere-autoupdate] [-m _<msg>_] [-F _<file>_]
	[--into-name _<branch>_] [_<commit>_…​]
git merge (--continue | --abort | --quit)
```

##  [](https://git-scm.com/docs/git-merge#_description)DESCRIPTION
Incorporates changes from the named commits (since the time their histories diverged from the current branch) into the current branch. This command is used by `git` `pull` to incorporate changes from another repository and can be used by hand to merge changes from one branch into another.
Assume the following history exists and the current branch is `master`:
```
          A---B---C topic
         /
    D---E---F---G master
```

Then `git` `merge` `topic` will replay the changes made on the `topic` branch since it diverged from `master` (i.e., `E`) until its current commit (`C`) on top of `master`, and record the result in a new commit along with the names of the two parent commits and a log message from the user describing the changes. Before the operation, `ORIG_HEAD` is set to the tip of the current branch (`G`).
```
          A---B---C topic
         /         \
    D---E---F---G---H master
```

A merge stops if there’s a conflict that cannot be resolved automatically or if `--no-commit` was provided when initiating the merge. At that point you can run `git` `merge` `--abort` or `git` `merge` `--continue`.
`git` `merge` `--abort` will abort the merge process and try to reconstruct the pre-merge state. However, if there were uncommitted changes when the merge started (and especially if those changes were further modified after the merge was started), `git` `merge` `--abort` will in some cases be unable to reconstruct the original (pre-merge) changes. Therefore:
Warning |  Running `git` `merge` with non-trivial uncommitted changes is discouraged: while possible, it may leave you in a state that is hard to back out of in the case of a conflict.   
---|---  
##  [](https://git-scm.com/docs/git-merge#_options)OPTIONS 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---commit)`--commit` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-commit)`--no-commit` 
    
Perform the merge and commit the result. This option can be used to override `--no-commit`.
With `--no-commit` perform the merge and stop just before creating a merge commit, to give the user a chance to inspect and further tweak the merge result before committing.
Note that fast-forward updates do not create a merge commit and therefore there is no way to stop those merges with `--no-commit`. Thus, if you want to ensure your branch is not changed or updated by the merge command, use `--no-ff` with `--no-commit`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---edit)`--edit` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--e)`-e` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-edit)`--no-edit` 
    
Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain and justify the merge. The `--no-edit` option can be used to accept the auto-generated message (this is generally discouraged). The `--edit` (or `-e`) option is still useful if you are giving a draft message with the `-m` option from the command line and want to edit it in the editor.
Older scripts may depend on the historical behaviour of not allowing the user to edit the merge log message. They will see an editor opened when they run `git` `merge`. To make it easier to adjust such scripts to the updated behaviour, the environment variable `GIT_MERGE_AUTOEDIT` can be set to `no` at the beginning of them. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---cleanupmode)`--cleanup=`_< mode>_ 
    
This option determines how the merge message will be cleaned up before committing. See [git-commit[1]](https://git-scm.com/docs/git-commit) for more details. In addition, if the _< mode>_ is given a value of `scissors`, scissors will be appended to `MERGE_MSG` before being passed on to the commit machinery in the case of a merge conflict. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---ff)`--ff` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-ff)`--no-ff` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---ff-only)`--ff-only` 
    
Specifies how a merge is handled when the merged-in history is already a descendant of the current history. `--ff` is the default unless merging an annotated (and possibly signed) tag that is not stored in its natural place in the `refs/tags/` hierarchy, in which case `--no-ff` is assumed.
With `--ff`, when possible resolve the merge as a fast-forward (only update the branch pointer to match the merged branch; do not create a merge commit). When not possible (when the merged-in history is not a descendant of the current history), create a merge commit.
With `--no-ff`, create a merge commit in all cases, even when the merge could instead be resolved as a fast-forward.
With `--ff-only`, resolve the merge as a fast-forward when possible. When not possible, refuse to merge and exit with a non-zero status. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--Skey-id)`-S`[_< key-id>_] 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---gpg-signkey-id)`--gpg-sign`[`=`_< key-id>_] 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-gpg-sign)`--no-gpg-sign` 
    
GPG-sign the resulting merge commit. The _< key-id>_ argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---logn)`--log`[`=`_< n>_] 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-log)`--no-log` 
    
In addition to branch names, populate the log message with one-line descriptions from at most _< n>_ actual commits that are being merged. See also [git-fmt-merge-msg[1]](https://git-scm.com/docs/git-fmt-merge-msg).
With `--no-log` do not list one-line descriptions from the actual commits being merged. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---signoff)`--signoff` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-signoff)`--no-signoff` 
    
Add a `Signed-off-by` trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you’re committing. For example, it may certify that the committer has the rights to submit the work under the project’s license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See <https://developercertificate.org> for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you’re contributing to understand how the signoffs are used in that project.
The `--no-signoff` option can be used to countermand an earlier `--signoff` option on the command line.
Git does not (and will not) have a configuration variable to enable the `--signoff` command line option by default; see the `commit.signoff` entry in [gitfaq[7]](https://git-scm.com/docs/gitfaq) for more details. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---stat)`--stat` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--n)`-n` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-stat)`--no-stat` 
    
Show a diffstat at the end of the merge. The diffstat is also controlled by the configuration option merge.stat.
With `-n` or `--no-stat` do not show a diffstat at the end of the merge. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---compact-summary)`--compact-summary` 
    
Show a compact-summary at the end of the merge. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---squash)`--squash` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-squash)`--no-squash` 
    
Produce the working tree and index state as if a real merge happened (except for the merge information), but do not actually make a commit, move the `HEAD`, or record `$GIT_DIR/MERGE_HEAD` (to cause the next `git` `commit` command to create a merge commit). This allows you to create a single commit on top of the current branch whose effect is the same as merging another branch (or more in case of an octopus).
With `--no-squash` perform the merge and commit the result. This option can be used to override `--squash`.
With `--squash`, `--commit` is not allowed, and will fail. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---verify)`--verify` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-verify)`--no-verify` 
    
By default, the pre-merge and commit-msg hooks are run. When `--no-verify` is given, these are bypassed. See also [githooks[5]](https://git-scm.com/docs/githooks). 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--sstrategy)`-s` _< strategy>_ 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---strategystrategy)`--strategy=`_< strategy>_ 
    
Use the given merge strategy; can be supplied more than once to specify them in the order they should be tried. If there is no `-s` option, a built-in list of strategies is used instead (`ort` when merging a single head, `octopus` otherwise). 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--Xoption)`-X` _< option>_ 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---strategy-optionoption)`--strategy-option=`_< option>_ 
    
Pass merge strategy specific option through to the merge strategy. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---verify-signatures)`--verify-signatures` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-verify-signatures)`--no-verify-signatures` 
    
Verify that the tip commit of the side branch being merged is signed with a valid key, i.e. a key that has a valid uid: in the default trust model, this means the signing key has been signed by a trusted key. If the tip commit of the side branch is not signed with a valid key, the merge is aborted. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---summary)`--summary` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-summary)`--no-summary` 
    
Synonyms to `--stat` and `--no-stat`; these are deprecated and will be removed in the future. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--q)`-q` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---quiet)`--quiet` 
    
Operate quietly. Implies `--no-progress`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--v)`-v` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---verbose)`--verbose` 
    
Be verbose. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---progress)`--progress` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-progress)`--no-progress` 
    
Turn progress on/off explicitly. If neither is specified, progress is shown if standard error is connected to a terminal. Note that not all merge strategies may support progress reporting. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---autostash)`--autostash` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-autostash)`--no-autostash` 
    
Automatically create a temporary stash entry before the operation begins, record it in the ref `MERGE_AUTOSTASH` and apply it after the operation ends. This means that you can run the operation on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---allow-unrelated-histories)`--allow-unrelated-histories` 
    
By default, `git` `merge` command refuses to merge histories that do not share a common ancestor. This option can be used to override this safety when merging histories of two projects that started their lives independently. As that is a very rare occasion, no configuration variable to enable this by default exists or will be added. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--mmsg)`-m` _< msg>_ 
    
Set the commit message to be used for the merge commit (in case one is created).
If `--log` is specified, a shortlog of the commits being merged will be appended to the specified message.
The `git` `fmt-merge-msg` command can be used to give a good default for automated `git` `merge` invocations. The automated message can include the branch description. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---into-namebranch)`--into-name` _< branch>_ 
    
Prepare the default merge message as if merging to the branch _< branch>_, instead of the name of the real branch to which the merge is made. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt--Ffile)`-F` _< file>_ 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---filefile)`--file=`_< file>_ 
    
Read the commit message to be used for the merge commit (in case one is created).
If `--log` is specified, a shortlog of the commits being merged will be appended to the specified message. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---rerere-autoupdate)`--rerere-autoupdate` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-rerere-autoupdate)`--no-rerere-autoupdate` 
    
After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update the index with the result of resolution. `--no-rerere-autoupdate` is a good way to double-check what `rerere` did and catch potential mismerges, before committing the result to the index with a separate `git` `add`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---overwrite-ignore)`--overwrite-ignore` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---no-overwrite-ignore)`--no-overwrite-ignore` 
    
Silently overwrite ignored files from the merge result. This is the default behavior. Use `--no-overwrite-ignore` to abort. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---abort)`--abort` 
    
Abort the current conflict resolution process, and try to reconstruct the pre-merge state. If an autostash entry is present, apply it to the worktree.
If there were uncommitted worktree changes present when the merge started, `git` `merge` `--abort` will in some cases be unable to reconstruct these changes. It is therefore recommended to always commit or stash your changes before running `git` `merge`.
`git` `merge` `--abort` is equivalent to `git` `reset` `--merge` when `MERGE_HEAD` is present unless `MERGE_AUTOSTASH` is also present in which case `git` `merge` `--abort` applies the stash entry to the worktree whereas `git` `reset` `--merge` will save the stashed changes in the stash list. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---quit)`--quit` 
    
Forget about the current merge in progress. Leave the index and the working tree as-is. If `MERGE_AUTOSTASH` is present, the stash entry will be saved to the stash list. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---continue)`--continue` 
    
After a `git` `merge` stops due to conflicts you can conclude the merge by running `git` `merge` `--continue` (see "HOW TO RESOLVE CONFLICTS" section below). 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-commit)_< commit>_... 
    
Commits, usually other branch heads, to merge into our branch. Specifying more than one commit will create a merge with more than two parents (affectionately called an Octopus merge).
If no commit is given from the command line, merge the remote-tracking branches that the current branch is configured to use as its upstream. See also the configuration section of this manual page.
When `FETCH_HEAD` (and no other commit) is specified, the branches recorded in the `.git/FETCH_HEAD` file by the previous invocation of `git` `fetch` for merging are merged to the current branch.
##  [](https://git-scm.com/docs/git-merge#_pre_merge_checks)PRE-MERGE CHECKS
Before applying outside changes, you should get your own work in good shape and committed locally, so it will not be clobbered if there are conflicts. See also [git-stash[1]](https://git-scm.com/docs/git-stash). `git` `pull` and `git` `merge` will stop without doing anything when local uncommitted changes overlap with files that `git` `pull`/`git` `merge` may need to update.
To avoid recording unrelated changes in the merge commit, `git` `pull` and `git` `merge` will also abort if there are any changes registered in the index relative to the `HEAD` commit. (Special narrow exceptions to this rule may exist depending on which merge strategy is in use, but generally, the index must match `HEAD`.)
If all named commits are already ancestors of `HEAD`, `git` `merge` will exit early with the message "Already up to date."
##  [](https://git-scm.com/docs/git-merge#_fast_forward_merge)FAST-FORWARD MERGE
Often the current branch head is an ancestor of the named commit. This is the most common case especially when invoked from `git` `pull`: you are tracking an upstream repository, you have committed no local changes, and now you want to update to a newer upstream revision. In this case, a new commit is not needed to store the combined history; instead, the `HEAD` (along with the index) is updated to point at the named commit, without creating an extra merge commit.
This behavior can be suppressed with the `--no-ff` option.
##  [](https://git-scm.com/docs/git-merge#_true_merge)TRUE MERGE
Except in a fast-forward merge (see above), the branches to be merged must be tied together by a merge commit that has both of them as its parents.
A merged version reconciling the changes from all branches to be merged is committed, and your `HEAD`, index, and working tree are updated to it. It is possible to have modifications in the working tree as long as they do not overlap; the update will preserve them.
When it is not obvious how to reconcile the changes, the following happens:
  1. The `HEAD` pointer stays the same.
  2. The `MERGE_HEAD` ref is set to point to the other branch head.
  3. Paths that merged cleanly are updated both in the index file and in your working tree.
  4. For conflicting paths, the index file records up to three versions: stage 1 stores the version from the common ancestor, stage 2 from `HEAD`, and stage 3 from `MERGE_HEAD` (you can inspect the stages with `git` `ls-files` `-u`). The working tree files contain the result of the merge operation; i.e. 3-way merge results with familiar conflict markers _< <<_ `===` _> >>_.
  5. A ref named `AUTO_MERGE` is written, pointing to a tree corresponding to the current content of the working tree (including conflict markers for textual conflicts). Note that this ref is only written when the `ort` merge strategy is used (the default).
  6. No other changes are made. In particular, the local modifications you had before you started merge will stay the same and the index entries for them stay as they were, i.e. matching `HEAD`.


If you tried a merge which resulted in complex conflicts and want to start over, you can recover with `git` `merge` `--abort`.
##  [](https://git-scm.com/docs/git-merge#_merging_tag)MERGING TAG
When merging an annotated (and possibly signed) tag, Git always creates a merge commit even if a fast-forward merge is possible, and the commit message template is prepared with the tag message. Additionally, if the tag is signed, the signature check is reported as a comment in the message template. See also [git-tag[1]](https://git-scm.com/docs/git-tag).
When you want to just integrate with the work leading to the commit that happens to be tagged, e.g. synchronizing with an upstream release point, you may not want to make an unnecessary merge commit.
In such a case, you can "unwrap" the tag yourself before feeding it to `git` `merge`, or pass `--ff-only` when you do not have any work on your own. e.g.
```
git fetch origin
git merge v1.2.3^0
git merge --ff-only v1.2.3
```

##  [](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented)HOW CONFLICTS ARE PRESENTED
During a merge, the working tree files are updated to reflect the result of the merge. Among the changes made to the common ancestor’s version, non-overlapping ones (that is, you changed an area of the file while the other side left that area intact, or vice versa) are incorporated in the final result verbatim. When both sides made changes to the same area, however, Git cannot randomly pick one side over the other, and asks you to resolve it by leaving what both sides did to that area.
By default, Git uses the same style as the one used by the "merge" program from the RCS suite to present such a conflicted hunk, like this:
```
Here are lines that are either unchanged from the common
ancestor, or cleanly resolved because only one side changed,
or cleanly resolved because both sides changed the same way.
<<<<<<< yours:sample.txt
Conflict resolution is hard;
let's go shopping.
=======
Git makes conflict resolution easy.
>>>>>>> theirs:sample.txt
And here is another line that is cleanly resolved or unmodified.
```

The area where a pair of conflicting changes happened is marked with markers _< <<<<<<_, `=======`, and _> >>>>>>_. The part before the `=======` is typically your side, and the part afterwards is typically their side.
The default format does not show what the original said in the conflicting area. You cannot tell how many lines are deleted and replaced with Barbie’s remark on your side. The only thing you can tell is that your side wants to say it is hard and you’d prefer to go shopping, while the other side wants to claim it is easy.
An alternative style can be used by setting the `merge.conflictStyle` configuration variable to either `diff3` or `zdiff3`. In `diff3` style, the above conflict may look like this:
```
Here are lines that are either unchanged from the common
ancestor, or cleanly resolved because only one side changed,
<<<<<<< yours:sample.txt
or cleanly resolved because both sides changed the same way.
Conflict resolution is hard;
let's go shopping.
||||||| base:sample.txt
or cleanly resolved because both sides changed identically.
Conflict resolution is hard.
=======
or cleanly resolved because both sides changed the same way.
Git makes conflict resolution easy.
>>>>>>> theirs:sample.txt
And here is another line that is cleanly resolved or unmodified.
```

while in `zdiff3` style, it may look like this:
```
Here are lines that are either unchanged from the common
ancestor, or cleanly resolved because only one side changed,
or cleanly resolved because both sides changed the same way.
<<<<<<< yours:sample.txt
Conflict resolution is hard;
let's go shopping.
||||||| base:sample.txt
or cleanly resolved because both sides changed identically.
Conflict resolution is hard.
=======
Git makes conflict resolution easy.
>>>>>>> theirs:sample.txt
And here is another line that is cleanly resolved or unmodified.
```

In addition to the _< <<<<<<_, `=======`, and _> >>>>>>_ markers, it uses another ||||||| marker that is followed by the original text. You can tell that the original just stated a fact, and your side simply gave in to that statement and gave up, while the other side tried to have a more positive attitude. You can sometimes come up with a better resolution by viewing the original.
##  [](https://git-scm.com/docs/git-merge#_how_to_resolve_conflicts)HOW TO RESOLVE CONFLICTS
After seeing a conflict, you can do two things:
  * Decide not to merge. The only clean-ups you need are to reset the index file to the `HEAD` commit to reverse 2. and to clean up working tree changes made by 2. and 3.; `git` `merge` `--abort` can be used for this.
  * Resolve the conflicts. Git will mark the conflicts in the working tree. Edit the files into shape and `git` `add` them to the index. Use `git` `commit` or `git` `merge` `--continue` to seal the deal. The latter command checks whether there is a (interrupted) merge in progress before calling `git` `commit`.


You can work through the conflict with a number of tools:
  * Use a mergetool. `git` `mergetool` to launch a graphical mergetool which will work through the merge with you.
  * Look at the diffs. `git` `diff` will show a three-way diff, highlighting changes from both the `HEAD` and `MERGE_HEAD` versions. `git` `diff` `AUTO_MERGE` will show what changes you’ve made so far to resolve textual conflicts.
  * Look at the diffs from each branch. `git` `log` `--merge` `-p` _< path>_ will show diffs first for the `HEAD` version and then the `MERGE_HEAD` version.
  * Look at the originals. `git` `show` `:1:filename` shows the common ancestor, `git` `show` `:2:filename` shows the `HEAD` version, and `git` `show` `:3:filename` shows the `MERGE_HEAD` version.


##  [](https://git-scm.com/docs/git-merge#_examples)EXAMPLES
  * Merge branches `fixes` and `enhancements` on top of the current branch, making an octopus merge:
```
$ git merge fixes enhancements
```

  * Merge branch `obsolete` into the current branch, using `ours` merge strategy:
```
$ git merge -s ours obsolete
```

  * Merge branch `maint` into the current branch, but do not make a new commit automatically:
```
$ git merge --no-commit maint
```

This can be used when you want to include further changes to the merge, or want to write your own merge commit message.
You should refrain from abusing this option to sneak substantial changes into a merge commit. Small fixups like bumping release/version name would be acceptable.


##  [](https://git-scm.com/docs/git-merge#_merge_strategies)MERGE STRATEGIES
The merge mechanism (`git` `merge` and `git` `pull` commands) allows the backend _merge strategies_ to be chosen with `-s` option. Some strategies can also take their own options, which can be passed by giving `-X`_< option>_ arguments to `git` `merge` and/or `git` `pull`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-ort)`ort` 
    
This is the default merge strategy when pulling or merging one branch. This strategy can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this strategy can detect and handle merges involving renames. It does not make use of detected copies. The name for this algorithm is an acronym ("Ostensibly Recursive’s Twin") and came from the fact that it was written as a replacement for the previous default algorithm, `recursive`.
In the case where the path is a submodule, if the submodule commit used on one side of the merge is a descendant of the submodule commit used on the other side of the merge, Git attempts to fast-forward to the descendant. Otherwise, Git will treat this case as a conflict, suggesting as a resolution a submodule commit that is descendant of the conflicting ones, if one exists.
The `ort` strategy can take the following options: 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-ours)`ours` 
    
This option forces conflicting hunks to be auto-resolved cleanly by favoring _our_ version. Changes from the other tree that do not conflict with our side are reflected in the merge result. For a binary file, the entire contents are taken from our side.
This should not be confused with the `ours` merge strategy, which does not even look at what the other tree contains at all. It discards everything the other tree did, declaring _our_ history contains all that happened in it. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-theirs)`theirs` 
    
This is the opposite of `ours`; note that, unlike `ours`, there is no `theirs` merge strategy to confuse this merge option with. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-ignore-space-change)`ignore-space-change` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-ignore-all-space)`ignore-all-space` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-ignore-space-at-eol)`ignore-space-at-eol` 


[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-ignore-cr-at-eol)`ignore-cr-at-eol` 
    
Treats lines with the indicated type of whitespace change as unchanged for the sake of a three-way merge. Whitespace changes mixed with other changes to a line are not ignored. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `-b`, `-w`, `--ignore-space-at-eol`, and `--ignore-cr-at-eol`.
  * If _their_ version only introduces whitespace changes to a line, _our_ version is used;
  * If _our_ version introduces whitespace changes but _their_ version includes a substantial change, _their_ version is used;
  * Otherwise, the merge proceeds in the usual way.



[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-renormalize)`renormalize` 
    
This runs a virtual check-out and check-in of all three stages of any file which needs a three-way merge. This option is meant to be used when merging branches with different clean filters or end-of-line normalization rules. See "Merging branches with differing checkin/checkout attributes" in [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-no-renormalize)`no-renormalize` 
    
Disables the `renormalize` option. This overrides the `merge.renormalize` configuration variable. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-find-renamesn)`find-renames`[`=`_< n>_] 
    
Turn on rename detection, optionally setting the similarity threshold. This is the default. This overrides the `merge.renames` configuration variable. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--find-renames`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-rename-thresholdn)`rename-threshold=`_< n>_ 
    
Deprecated synonym for `find-renames=`_< n>_. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-no-renames)`no-renames` 
    
Turn off rename detection. This overrides the `merge.renames` configuration variable. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--no-renames`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-histogram)`histogram` 
    
Deprecated synonym for `diff-algorithm=histogram`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-patience)`patience` 
    
Deprecated synonym for `diff-algorithm=patience`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-diff-algorithmhistogramminimalmyerspatience)`diff-algorithm=`(`histogram`|`minimal`|`myers`|`patience`) 
    
Use a different diff algorithm while merging, which can help avoid mismerges that occur due to unimportant matching lines (such as braces from distinct functions). See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--diff-algorithm`. Note that `ort` defaults to `diff-algorithm=histogram`, while regular diffs currently default to the `diff.algorithm` config setting. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-subtreepath)`subtree`[`=`_< path>_] 
    
This option is a more advanced form of _subtree_ strategy, where the strategy makes a guess on how two trees must be shifted to match with each other when merging. Instead, the specified path is prefixed (or stripped from the beginning) to make the shape of two trees to match. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-recursive)`recursive` 
    
This is now a synonym for `ort`. It was an alternative implementation until v2.49.0, but was redirected to mean `ort` in v2.50.0. The previous recursive strategy was the default strategy for resolving two heads from Git v0.99.9k until v2.33.0. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-resolve)`resolve` 
    
This can only resolve two heads (i.e. the current branch and another branch you pulled from) using a 3-way merge algorithm. It tries to carefully detect criss-cross merge ambiguities. It does not handle renames. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-octopus)`octopus` 
    
This resolves cases with more than two heads, but refuses to do a complex merge that needs manual resolution. It is primarily meant to be used for bundling topic branch heads together. This is the default merge strategy when pulling or merging more than one branch. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-ours-1)`ours` 
    
This resolves any number of heads, but the resulting tree of the merge is always that of the current branch head, effectively ignoring all changes from all other branches. It is meant to be used to supersede old development history of side branches. Note that this is different from the `-Xours` option to the `ort` merge strategy. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-subtree)`subtree` 
    
This is a modified `ort` strategy. When merging trees A and B, if B corresponds to a subtree of A, B is first adjusted to match the tree structure of A, instead of reading the trees at the same level. This adjustment is also done to the common ancestor tree.
With the strategies that use 3-way merge (including the default, `ort`), if a change is made on both branches, but later reverted on one of the branches, that change will be present in the merged result; some people find this behavior confusing. It occurs because only the heads and the merge base are considered when performing a merge, not the individual commits. The merge algorithm therefore considers the reverted change as no change at all, and substitutes the changed version instead.
##  [](https://git-scm.com/docs/git-merge#_configuration)CONFIGURATION 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-branchnamemergeOptions)`branch.`_< name>_`.mergeOptions` 
    
Sets default options for merging into branch _< name>_. The syntax and supported options are the same as those of `git` `merge`, but option values containing whitespace characters are currently not supported.
Everything above this line in this section isn’t included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content that follows is the same as what’s found there: 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergeconflictStyle)`merge.conflictStyle` 
    
Specify the style in which conflicted hunks are written out to working tree files upon merge. The default is "merge", which shows a _< <<<<<<_ conflict marker, changes made by one side, a `=======` marker, changes made by the other side, and then a _> >>>>>>_ marker. An alternate style, "diff3", adds a ||||||| marker and the original text before the `=======` marker. The "merge" style tends to produce smaller conflict regions than diff3, both because of the exclusion of the original text, and because when a subset of lines match on the two sides, they are just pulled out of the conflict region. Another alternate style, "zdiff3", is similar to diff3 but removes matching lines on the two sides from the conflict region when those matching lines appear near either the beginning or end of a conflict region. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergedefaultToUpstream)`merge.defaultToUpstream` 
    
If merge is called without any commit argument, merge the upstream branches configured for the current branch by using their last observed values stored in their remote-tracking branches. The values of the _branch. <current branch>.merge_ that name the branches at the remote named by `branch.`_< current-branch>_`.remote` are consulted, and then they are mapped via `remote.`_< remote>_`.fetch` to their corresponding remote-tracking branches, and the tips of these tracking branches are merged. Defaults to true. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergeff)`merge.ff` 
    
By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to `false`, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the `--no-ff` option from the command line). When set to `only`, only such fast-forward merges are allowed (equivalent to giving the `--ff-only` option from the command line). 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergeverifySignatures)`merge.verifySignatures` 
    
If true, this is equivalent to the `--verify-signatures` command line option. See [git-merge[1]](https://git-scm.com/docs/git-merge) for details. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergebranchdesc)`merge.branchdesc` 
    
In addition to branch names, populate the log message with the branch description text associated with them. Defaults to false. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergelog)`merge.log` 
    
In addition to branch names, populate the log message with at most the specified number of one-line descriptions from the actual commits that are being merged. Defaults to false, and true is a synonym for 20. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergesuppressDest)`merge.suppressDest` 
    
By adding a glob that matches the names of integration branches to this multi-valued configuration variable, the default merge message computed for merges into these integration branches will omit "into _< branch-name>_" from its title.
An element with an empty value can be used to clear the list of globs accumulated from previous configuration entries. When there is no `merge.suppressDest` variable defined, the default value of `master` is used for backward compatibility. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergerenameLimit)`merge.renameLimit` 
    
The number of files to consider in the exhaustive portion of rename detection during a merge. If not specified, defaults to the value of `diff.renameLimit`. If neither `merge.renameLimit` nor `diff.renameLimit` are specified, currently defaults to 7000. This setting has no effect if rename detection is turned off. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergerenames)`merge.renames` 
    
Whether Git detects renames. If set to `false`, rename detection is disabled. If set to `true`, basic rename detection is enabled. Defaults to the value of diff.renames. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergedirectoryRenames)`merge.directoryRenames` 
    
Whether Git detects directory renames, affecting what happens at merge time to new files added to a directory on one side of history when that directory was renamed on the other side of history. Possible values are: 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-false)`false` 
    
Directory rename detection is disabled, meaning that such new files will be left behind in the old directory. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-true)`true` 
    
Directory rename detection is enabled, meaning that such new files will be moved into the new directory. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-conflict)`conflict` 
    
A conflict will be reported for such paths.
If `merge.renames` is `false`, `merge.directoryRenames` is ignored and treated as `false`. Defaults to `conflict`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergerenormalize)`merge.renormalize` 
    
Tell Git that canonical representation of files in the repository has changed over time (e.g. earlier commits record text files with _CRLF_ line endings, but recent ones use _LF_ line endings). In such a repository, for each file where a three-way content merge is needed, Git can convert the data recorded in commits to a canonical form before performing a merge to reduce unnecessary conflicts. For more information, see section "Merging branches with differing checkin/checkout attributes" in [gitattributes[5]](https://git-scm.com/docs/gitattributes). 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergestat)`merge.stat` 
    
What, if anything, to print between `ORIG_HEAD` and the merge result at the end of the merge. Possible values are: 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-false-1)`false` 
    
Show nothing. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-true-1)`true` 
    
Show `git` `diff` `--diffstat` `--summary` `ORIG_HEAD`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-compact)`compact` 
    
Show `git` `diff` `--compact-summary` `ORIG_HEAD`.
but any unrecognised value (e.g., a value added by a future version of Git) is taken as `true` instead of triggering an error. Defaults to `true`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergeautoStash)`merge.autoStash` 
    
When set to `true`, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run merge on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. This option can be overridden by the `--no-autostash` and `--autostash` options of [git-merge[1]](https://git-scm.com/docs/git-merge). Defaults to `false`. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergetool)`merge.tool` 
    
Controls which merge tool is used by [git-mergetool[1]](https://git-scm.com/docs/git-mergetool). The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding `mergetool.`_< tool>_`.cmd` variable is defined. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergeguitool)`merge.guitool` 
    
Controls which merge tool is used by [git-mergetool[1]](https://git-scm.com/docs/git-mergetool) when the `-g`/`--gui` flag is specified. The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding `mergetool.`_< guitool>_`.cmd` variable is defined.
  * araxis
  * bc
  * codecompare
  * deltawalker
  * diffmerge
  * diffuse
  * ecmerge
  * emerge
  * examdiff
  * guiffy
  * gvimdiff
  * kdiff3
  * meld
  * nvimdiff
  * opendiff
  * p4merge
  * smerge
  * tkdiff
  * tortoisemerge
  * vimdiff
  * vscode
  * winmerge
  * xxdiff



[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergeverbosity)`merge.verbosity` 
    
Controls the amount of output shown by the recursive merge strategy. Level 0 outputs nothing except a final error message if conflicts were detected. Level 1 outputs only conflicts, 2 outputs conflicts and file changes. Level 5 and above outputs debugging information. The default is level 2. Can be overridden by the `GIT_MERGE_VERBOSITY` environment variable. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergedrivername)`merge.`_< driver>_`.name` 
    
Defines a human-readable name for a custom low-level merge driver. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergedriverdriver)`merge.`_< driver>_`.driver` 
    
Defines the command that implements a custom low-level merge driver. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt-mergedriverrecursive)`merge.`_< driver>_`.recursive` 
    
Names a low-level merge driver to be used when performing an internal merge between common ancestors. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details.
##  [](https://git-scm.com/docs/git-merge#_see_also)SEE ALSO
[git-fmt-merge-msg[1]](https://git-scm.com/docs/git-fmt-merge-msg), [git-pull[1]](https://git-scm.com/docs/git-pull), [gitattributes[5]](https://git-scm.com/docs/gitattributes), [git-reset[1]](https://git-scm.com/docs/git-reset), [git-diff[1]](https://git-scm.com/docs/git-diff), [git-ls-files[1]](https://git-scm.com/docs/git-ls-files), [git-add[1]](https://git-scm.com/docs/git-add), [git-rm[1]](https://git-scm.com/docs/git-rm), [git-mergetool[1]](https://git-scm.com/docs/git-mergetool)
##  [](https://git-scm.com/docs/git-merge#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### merge
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
