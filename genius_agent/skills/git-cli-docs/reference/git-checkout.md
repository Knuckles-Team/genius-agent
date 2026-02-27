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
    * [NAME](https://git-scm.com/docs/git-checkout#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-checkout#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-checkout#_description)
    * [OPTIONS](https://git-scm.com/docs/git-checkout#_options)
    * [DETACHED HEAD](https://git-scm.com/docs/git-checkout#_detached_head)
    * [ARGUMENT DISAMBIGUATION](https://git-scm.com/docs/git-checkout#_argument_disambiguation)
    * [EXAMPLES](https://git-scm.com/docs/git-checkout#_examples)
    * [CONFIGURATION](https://git-scm.com/docs/git-checkout#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-checkout#_see_also)
    * [GIT](https://git-scm.com/docs/git-checkout#_git)


[ English ▾](https://git-scm.com/docs/git-checkout)
Localized versions of **git-checkout** manual
  1. [English ](https://git-scm.com/docs/git-checkout)
  2. [Français ](https://git-scm.com/docs/git-checkout/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-checkout/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-checkout/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-checkout/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-checkout)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-checkout) git-checkout last updated in 2.53.0
Changes in the **git-checkout** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-checkout/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-checkout/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-checkout/2.51.0)
  5. 2.50.1 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-checkout/2.50.0)
  7. 2.47.2 → 2.49.1 no changes
  8. [2.47.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-25_ ](https://git-scm.com/docs/git-checkout/2.47.1)
  9. 2.44.1 → 2.47.0 no changes
  10. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-checkout/2.44.0)
  11. 2.43.2 → 2.43.7 no changes
  12. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-checkout/2.43.1)
  13. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-checkout/2.43.0)
  14. 2.41.1 → 2.42.4 no changes
  15. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-checkout/2.41.0)
  16. 2.40.1 → 2.40.4 no changes
  17. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-checkout/2.40.0)
  18. 2.39.4 → 2.39.5 no changes
  19. [2.39.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-04-17_ ](https://git-scm.com/docs/git-checkout/2.39.3)
  20. 2.38.1 → 2.39.2 no changes
  21. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-checkout/2.38.0)
  22. 2.35.1 → 2.37.7 no changes
  23. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-checkout/2.35.0)
  24. 2.34.1 → 2.34.8 no changes
  25. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-checkout/2.34.0)
  26. 2.30.1 → 2.33.8 no changes
  27. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-checkout/2.30.0)
  28. 2.29.1 → 2.29.3 no changes
  29. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-checkout/2.29.0)
  30. 2.27.1 → 2.28.1 no changes
  31. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-checkout/2.27.0)
  32. 2.25.1 → 2.26.3 no changes
  33. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-checkout/2.25.0)
  34. 2.23.1 → 2.24.4 no changes
  35. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-checkout/2.23.0)
  36. 2.22.1 → 2.22.5 no changes
  37. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-checkout/2.22.0)
  38. 2.21.1 → 2.21.4 no changes
  39. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-checkout/2.21.0)
  40. 2.19.3 → 2.20.5 no changes
  41. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-checkout/2.19.2)
  42. 2.19.1 no changes
  43. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-checkout/2.19.0)
  44. 2.17.0 → 2.18.5 no changes
  45. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-checkout/2.16.6)
  46. 2.15.4 no changes
  47. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-checkout/2.14.6)
  48. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-checkout/2.13.7)
  49. 2.11.4 → 2.12.5 no changes
  50. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-checkout/2.10.5)
  51. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-checkout/2.9.5)
  52. 2.8.6 no changes
  53. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-checkout/2.7.6)
  54. 2.6.7 no changes
  55. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-checkout/2.5.6)
  56. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-checkout/2.4.12)
  57. 2.1.4 → 2.3.10 no changes
  58. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-checkout/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-checkout#_name)NAME
git-checkout - Switch branches or restore working tree files
##  [](https://git-scm.com/docs/git-checkout#_synopsis)SYNOPSIS
```
git checkout [-q] [-f] [-m] [_<branch>_]
git checkout [-q] [-f] [-m] --detach [_<branch>_]
git checkout [-q] [-f] [-m] [--detach] _<commit>_
git checkout [-q] [-f] [-m] [[-b|-B|--orphan] _<new-branch>_] [_<start-point>_]
git checkout _<tree-ish>_ [--] _<pathspec>_…​
git checkout _<tree-ish>_ --pathspec-from-file=_<file>_ [--pathspec-file-nul]
git checkout [-f|--ours|--theirs|-m|--conflict=_<style>_] [--] _<pathspec>_…​
git checkout [-f|--ours|--theirs|-m|--conflict=_<style>_] --pathspec-from-file=_<file>_ [--pathspec-file-nul]
git checkout (-p|--patch) [_<tree-ish>_] [--] [_<pathspec>_…​]
```

##  [](https://git-scm.com/docs/git-checkout#_description)DESCRIPTION
`git` `checkout` has two main modes:
  1. **Switch branches** , with `git` `checkout` _< branch>_
  2. **Restore a different version of a file** , for example with `git` `checkout` _< commit>_ _< filename>_ or `git` `checkout` _< filename>_


See ARGUMENT DISAMBIGUATION below for how Git decides which one to do. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckoutbranch)`git` `checkout` [_< branch>_] 
    
Switch to _< branch>_. This sets the current branch to _< branch>_ and updates the files in your working directory. The checkout will fail if there are uncommitted changes to any files where _< branch>_ and your current commit have different content. Uncommitted changes will otherwise be kept.
If _< branch>_ is not found but there does exist a tracking branch in exactly one remote (call it _< remote>_) with a matching name and `--no-guess` is not specified, treat as equivalent to
```
$ git checkout -b <branch> --track <remote>/<branch>
```

Running `git` `checkout` without specifying a branch has no effect except to print out the tracking information for the current branch. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckout-bnew-branchstart-point)`git` `checkout` `-b` _< new-branch>_ [_< start-point>_] 
    
Create a new branch named _< new-branch>_, start it at _< start-point>_ (defaults to the current commit), and check out the new branch. You can use the `--track` or `--no-track` options to set the branch’s upstream tracking information.
This will fail if there’s an error checking out _< new-branch>_, for example if checking out the _< start-point>_ commit would overwrite your uncommitted changes. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckout-Bbranchstart-point)`git` `checkout` `-B` _< branch>_ [_< start-point>_] 
    
The same as `-b`, except that if the branch already exists it resets _< branch>_ to the start point instead of failing. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckout--detachbranch)`git` `checkout` `--detach` [_< branch>_] 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckout--detachcommit)`git` `checkout` [`--detach`] _< commit>_ 
    
The same as `git` `checkout` _< branch>_, except that instead of pointing `HEAD` at the branch, it points `HEAD` at the commit ID. See the "DETACHED HEAD" section below for more.
Omitting _< branch>_ detaches `HEAD` at the tip of the current branch. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckouttree-ish--pathspec)`git` `checkout` _< tree-ish>_ [`--`] _< pathspec>_... 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckouttree-ish--pathspec-from-filefile--pathspec-file-nul)`git` `checkout` _< tree-ish>_ `--pathspec-from-file=`_< file>_ [`--pathspec-file-nul`] 
    
Replace the specified files and/or directories with the version from the given commit or tree and add them to the index (also known as "staging area").
For example, `git` `checkout` `main` `file.txt` will replace `file.txt` with the version from `main`. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckout-f--ours--theirs-m--conflictstyle--pathspec)`git` `checkout` [`-f`|`--ours`|`--theirs`|`-m`|`--conflict=`_< style>_] [`--`] _< pathspec>_... 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckout-f--ours--theirs-m--conflictstyle--pathspec-from-filefile--pathspec-file-nul)`git` `checkout` [`-f`|`--ours`|`--theirs`|`-m`|`--conflict=`_< style>_] `--pathspec-from-file=`_< file>_ [`--pathspec-file-nul`] 
    
Replace the specified files and/or directories with the version from the index.
For example, if you check out a commit, edit `file.txt`, and then decide those changes were a mistake, `git` `checkout` `file.txt` will discard any unstaged changes to `file.txt`.
This will fail if the file has a merge conflict and you haven’t yet run `git` `add` `file.txt` (or something equivalent) to mark it as resolved. You can use `-f` to ignore the unmerged files instead of failing, use `--ours` or `--theirs` to replace them with the version from a specific side of the merge, or use `-m` to replace them with the original conflicted merge result. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-gitcheckout-p--patchtree-ish--pathspec)`git` `checkout` (`-p`|`--patch`) [_< tree-ish>_] [`--`] [_< pathspec>_...] 
    
This is similar to the previous two modes, but lets you use the interactive interface to show the "diff" output and choose which hunks to use in the result. See below for the description of `--patch` option.
##  [](https://git-scm.com/docs/git-checkout#_options)OPTIONS 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--q)`-q` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---quiet)`--quiet` 
    
Quiet, suppress feedback messages. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---progress)`--progress` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---no-progress)`--no-progress` 
    
Progress status is reported on the standard error stream by default when it is attached to a terminal, unless `--quiet` is specified. This flag enables progress reporting even if not attached to a terminal, regardless of `--quiet`. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--f)`-f` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---force)`--force` 
    
When switching branches, proceed even if the index or the working tree differs from `HEAD`, and even if there are untracked files in the way. This is used to throw away local changes and any untracked files or directories that are in the way.
When checking out paths from the index, do not fail upon unmerged entries; instead, unmerged entries are ignored. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---ours)`--ours` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---theirs)`--theirs` 
    
When checking out paths from the index, check out stage #2 (`ours`) or #3 (`theirs`) for unmerged paths.
Note that during `git` `rebase` and `git` `pull` `--rebase`, `ours` and `theirs` may appear swapped; `--ours` gives the version from the branch the changes are rebased onto, while `--theirs` gives the version from the branch that holds your work that is being rebased.
This is because `rebase` is used in a workflow that treats the history at the remote as the shared canonical one, and treats the work done on the branch you are rebasing as the third-party work to be integrated, and you are temporarily assuming the role of the keeper of the canonical history during the rebase. As the keeper of the canonical history, you need to view the history from the remote as `ours` (i.e. "our shared canonical history"), while what you did on your side branch as `theirs` (i.e. "one contributor’s work on top of it"). 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--bnew-branch)`-b` _< new-branch>_ 
    
Create a new branch named _< new-branch>_, start it at _< start-point>_, and check the resulting branch out; see [git-branch[1]](https://git-scm.com/docs/git-branch) for details. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--Bnew-branch)`-B` _< new-branch>_ 
    
The same as `-b`, except that if the branch already exists it resets _< branch>_ to the start point instead of failing. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--t)`-t` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---trackdirectinherit)`--track`[`=`(`direct`|`inherit`)] 
    
When creating a new branch, set up "upstream" configuration. See `--track` in [git-branch[1]](https://git-scm.com/docs/git-branch) for details. As a convenience, --track without -b implies branch creation.
If no `-b` option is given, the name of the new branch will be derived from the remote-tracking branch, by looking at the local part of the refspec configured for the corresponding remote, and then stripping the initial part up to the "*". This would tell us to use `hack` as the local branch when branching off of `origin/hack` (or `remotes/origin/hack`, or even `refs/remotes/origin/hack`). If the given name has no slash, or the above guessing results in an empty name, the guessing is aborted. You can explicitly give a name with `-b` in such a case. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---no-track)`--no-track` 
    
Do not set up "upstream" configuration, even if the `branch.autoSetupMerge` configuration variable is true. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---guess)`--guess` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---no-guess)`--no-guess` 
    
If _< branch>_ is not found but there does exist a tracking branch in exactly one remote (call it _< remote>_) with a matching name, treat as equivalent to
```
$ git checkout -b <branch> --track <remote>/<branch>
```

If the branch exists in multiple remotes and one of them is named by the `checkout.defaultRemote` configuration variable, we’ll use that one for the purposes of disambiguation, even if the _< branch>_ isn’t unique across all remotes. Set it to e.g. `checkout.defaultRemote=origin` to always checkout remote branches from there if _< branch>_ is ambiguous but exists on the _origin_ remote. See also `checkout.defaultRemote` in [git-config[1]](https://git-scm.com/docs/git-config).
`--guess` is the default behavior. Use `--no-guess` to disable it.
The default behavior can be set via the `checkout.guess` configuration variable. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--l)`-l` 
    
Create the new branch’s reflog; see [git-branch[1]](https://git-scm.com/docs/git-branch) for details. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--d)`-d` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---detach)`--detach` 
    
Rather than checking out a branch to work on it, check out a commit for inspection and discardable experiments. This is the default behavior of `git` `checkout` _< commit>_ when _< commit>_ is not a branch name. See the "DETACHED HEAD" section below for details. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---orphannew-branch)`--orphan` _< new-branch>_ 
    
Create a new unborn branch, named _< new-branch>_, started from _< start-point>_ and switch to it. The first commit made on this new branch will have no parents and it will be the root of a new history totally disconnected from all the other branches and commits.
The index and the working tree are adjusted as if you had previously run `git` `checkout` _< start-point>_. This allows you to start a new history that records a set of paths similar to _< start-point>_ by easily running `git` `commit` `-a` to make the root commit.
This can be useful when you want to publish the tree from a commit without exposing its full history. You might want to do this to publish an open source branch of a project whose current tree is "clean", but whose full history contains proprietary or otherwise encumbered bits of code.
If you want to start a disconnected history that records a set of paths that is totally different from the one of _< start-point>_, then you should clear the index and the working tree right after creating the orphan branch by running `git` `rm` `-rf` `.` from the top level of the working tree. Afterwards you will be ready to prepare your new files, repopulating the working tree, by copying them from elsewhere, extracting a tarball, etc. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---ignore-skip-worktree-bits)`--ignore-skip-worktree-bits` 
    
In sparse checkout mode, `git` `checkout` `--` _< path>_... would update only entries matched by _< paths>_ and sparse patterns in `$GIT_DIR/info/sparse-checkout`. This option ignores the sparse patterns and adds back any files in _< path>_.... 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--m)`-m` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---merge)`--merge` 
    
When switching branches, if you have local modifications to one or more files that are different between the current branch and the branch to which you are switching, the command refuses to switch branches in order to preserve your modifications in context. However, with this option, a three-way merge between the current branch, your working tree contents, and the new branch is done, and you will be on the new branch.
When a merge conflict happens, the index entries for conflicting paths are left unmerged, and you need to resolve the conflicts and mark the resolved paths with `git` `add` (or `git` `rm` if the merge should result in deletion of the path).
When checking out paths from the index, this option lets you recreate the conflicted merge in the specified paths. This option cannot be used when checking out paths from a tree-ish.
When switching branches with `--merge`, staged changes may be lost. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---conflictstyle)`--conflict=`_< style>_ 
    
The same as `--merge` option above, but changes the way the conflicting hunks are presented, overriding the `merge.conflictStyle` configuration variable. Possible values are `merge` (default), `diff3`, and `zdiff3`. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--p)`-p` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---patch)`--patch` 
    
Interactively select hunks in the difference between the _< tree-ish>_ (or the index, if unspecified) and the working tree. The chosen hunks are then applied in reverse to the working tree (and if a _< tree-ish>_ was specified, the index).
This means that you can use `git` `checkout` `-p` to selectively discard edits from your current working tree. See the "Interactive Mode" section of [git-add[1]](https://git-scm.com/docs/git-add) to learn how to operate the `--patch` mode.
Note that this option uses the no overlay mode by default (see also `--overlay`), and currently doesn’t support overlay mode. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context. Defaults to `diff.context` or 3 if the config option is unset. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---inter-hunk-contextn)`--inter-hunk-context=`_< n>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---ignore-other-worktrees)`--ignore-other-worktrees` 
    
`git` `checkout` refuses when the wanted branch is already checked out or otherwise in use by another worktree. This option makes it check the branch out anyway. In other words, the branch can be in use by more than one worktree. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---overwrite-ignore)`--overwrite-ignore` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---no-overwrite-ignore)`--no-overwrite-ignore` 
    
Silently overwrite ignored files when switching branches. This is the default behavior. Use `--no-overwrite-ignore` to abort the operation when the new branch contains ignored files. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---recurse-submodules)`--recurse-submodules` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---no-recurse-submodules)`--no-recurse-submodules` 
    
Using `--recurse-submodules` will update the content of all active submodules according to the commit recorded in the superproject. If local modifications in a submodule would be overwritten the checkout will fail unless `-f` is used. If nothing (or `--no-recurse-submodules`) is used, submodules working trees will not be updated. Just like [git-submodule[1]](https://git-scm.com/docs/git-submodule), this will detach `HEAD` of the submodule. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---overlay)`--overlay` 


[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---no-overlay)`--no-overlay` 
    
In the default overlay mode, `git` `checkout` never removes files from the index or the working tree. When specifying `--no-overlay`, files that appear in the index and working tree, but not in _< tree-ish>_ are removed, to make them match _< tree-ish>_ exactly. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---pathspec-from-filefile)`--pathspec-from-file=`_< file>_ 
    
Pathspec is passed in _< file>_ instead of commandline args. If _< file>_ is exactly `-` then standard input is used. Pathspec elements are separated by _LF_ or _CR_ /_LF_. Pathspec elements can be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). See also `--pathspec-file-nul` and global `--literal-pathspecs`. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---pathspec-file-nul)`--pathspec-file-nul` 
    
Only meaningful with `--pathspec-from-file`. Pathspec elements are separated with _NUL_ character and all other characters are taken literally (including newlines and quotes). 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-branch)_< branch>_ 
    
Branch to checkout; if it refers to a branch (i.e., a name that, when prepended with "refs/heads/", is a valid ref), then that branch is checked out. Otherwise, if it refers to a valid commit, your `HEAD` becomes "detached" and you are no longer on any branch (see below for details).
You can use the `@{-N}` syntax to refer to the N-th last branch/commit checked out using "git checkout" operation. You may also specify `-` which is synonymous to `@{-1}`.
As a special case, you may use _< rev-a>_`...`_< rev-b>_ as a shortcut for the merge base of _< rev-a>_ and _< rev-b>_ if there is exactly one merge base. You can leave out at most one of _< rev-a>_ and _< rev-b>_, in which case it defaults to `HEAD`. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-new-branch)_< new-branch>_ 
    
Name for the new branch. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-start-point)_< start-point>_ 
    
The name of a commit at which to start the new branch; see [git-branch[1]](https://git-scm.com/docs/git-branch) for details. Defaults to `HEAD`.
As a special case, you may use _< rev-a>_`...`_< rev-b>_ as a shortcut for the merge base of _< rev-a>_ and _< rev-b>_ if there is exactly one merge base. You can leave out at most one of _< rev-a>_ and _< rev-b>_, in which case it defaults to `HEAD`. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-tree-ish)_< tree-ish>_ 
    
Tree to checkout from (when paths are given). If not specified, the index will be used.
As a special case, you may use _< rev-a>_`...`_< rev-b>_ as a shortcut for the merge base of _< rev-a>_ and _< rev-b>_ if there is exactly one merge base. You can leave out at most one of _< rev-a>_ and _< rev-b>_, in which case it defaults to `HEAD`. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt---)`--` 
    
Do not interpret any more arguments as options. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-pathspec)_< pathspec>_... 
    
Limits the paths affected by the operation.
For more details, see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary).
##  [](https://git-scm.com/docs/git-checkout#_detached_head)DETACHED HEAD
`HEAD` normally refers to a named branch (e.g. `master`). Meanwhile, each branch refers to a specific commit. Let’s look at a repo with three commits, one of them tagged, and with branch `master` checked out:
```
           HEAD (refers to branch 'master')
            |
            v
a---b---c  branch 'master' (refers to commit 'c')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
```

When a commit is created in this state, the branch is updated to refer to the new commit. Specifically, `git` `commit` creates a new commit `d`, whose parent is commit `c`, and then updates branch `master` to refer to new commit `d`. `HEAD` still refers to branch `master` and so indirectly now refers to commit `d`:
```
$ edit; git add; git commit

               HEAD (refers to branch 'master')
                |
                v
a---b---c---d  branch 'master' (refers to commit 'd')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
```

It is sometimes useful to be able to checkout a commit that is not at the tip of any named branch, or even to create a new commit that is not referenced by a named branch. Let’s look at what happens when we checkout commit `b` (here we show two ways this may be done):
```
$ git checkout v2.0  # or
$ git checkout master^^

   HEAD (refers to commit 'b')
    |
    v
a---b---c---d  branch 'master' (refers to commit 'd')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
```

Notice that regardless of which checkout command we use, `HEAD` now refers directly to commit `b`. This is known as being in detached `HEAD` state. It means simply that `HEAD` refers to a specific commit, as opposed to referring to a named branch. Let’s see what happens when we create a commit:
```
$ edit; git add; git commit

     HEAD (refers to commit 'e')
      |
      v
      e
     /
a---b---c---d  branch 'master' (refers to commit 'd')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
```

There is now a new commit `e`, but it is referenced only by `HEAD`. We can of course add yet another commit in this state:
```
$ edit; git add; git commit

	 HEAD (refers to commit 'f')
	  |
	  v
      e---f
     /
a---b---c---d  branch 'master' (refers to commit 'd')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
```

In fact, we can perform all the normal Git operations. But, let’s look at what happens when we then checkout `master`:
```
$ git checkout master

               HEAD (refers to branch 'master')
      e---f     |
     /          v
a---b---c---d  branch 'master' (refers to commit 'd')
    ^
    |
  tag 'v2.0' (refers to commit 'b')
```

It is important to realize that at this point nothing refers to commit `f`. Eventually commit `f` (and by extension commit `e`) will be deleted by the routine Git garbage collection process, unless we create a reference before that happens. If we have not yet moved away from commit `f`, any of these will create a reference to it:
```
$ git checkout -b foo  # or "git switch -c foo"  **(1)**
$ git branch foo                                 **(2)**
$ git tag foo                                    **(3)**
```

  1. creates a new branch `foo`, which refers to commit `f`, and then updates `HEAD` to refer to branch `foo`. In other words, we’ll no longer be in detached `HEAD` state after this command.
  2. similarly creates a new branch `foo`, which refers to commit `f`, but leaves `HEAD` detached.
  3. creates a new tag `foo`, which refers to commit `f`, leaving `HEAD` detached.


If we have moved away from commit `f`, then we must first recover its object name (typically by using git reflog), and then we can create a reference to it. For example, to see the last two commits to which `HEAD` referred, we can use either of these commands:
```
$ git reflog -2 HEAD # or
$ git log -g -2 HEAD
```

##  [](https://git-scm.com/docs/git-checkout#_argument_disambiguation)ARGUMENT DISAMBIGUATION
When you run `git` `checkout` _< something>_, Git tries to guess whether _< something>_ is intended to be a branch, a commit, or a set of file(s), and then either switches to that branch or commit, or restores the specified files.
If there’s any ambiguity, Git will treat _< something>_ as a branch or commit, but you can use the double dash `--` to force Git to treat the parameter as a list of files and/or directories, like this:
```
git checkout -- file.txt
```

##  [](https://git-scm.com/docs/git-checkout#_examples)EXAMPLES
###  [](https://git-scm.com/docs/git-checkout#_1_paths)1. Paths
The following sequence checks out the `master` branch, reverts the `Makefile` to two revisions back, deletes `hello.c` by mistake, and gets it back from the index.
```
$ git checkout master             **(1)**
$ git checkout master~2 Makefile  **(2)**
$ rm -f hello.c
$ git checkout hello.c            **(3)**
```

  1. switch branch
  2. take a file out of another commit
  3. restore `hello.c` from the index


If you want to check out _all_ C source files out of the index, you can say
```
$ git checkout -- '*.c'
```

Note the quotes around `*.c`. The file `hello.c` will also be checked out, even though it is no longer in the working tree, because the file globbing is used to match entries in the index (not in the working tree by the shell).
If you have an unfortunate branch that is named `hello.c`, this step would be confused as an instruction to switch to that branch. You should instead write:
```
$ git checkout -- hello.c
```

###  [](https://git-scm.com/docs/git-checkout#_2_merge)2. Merge
After working in the wrong branch, switching to the correct branch would be done using:
```
$ git checkout mytopic
```

However, your "wrong" branch and correct `mytopic` branch may differ in files that you have modified locally, in which case the above checkout would fail like this:
```
$ git checkout mytopic
error: You have local changes to 'frotz'; not switching branches.
```

You can give the `-m` flag to the command, which would try a three-way merge:
```
$ git checkout -m mytopic
Auto-merging frotz
```

After this three-way merge, the local modifications are _not_ registered in your index file, so `git` `diff` would show you what changes you made since the tip of the new branch.
###  [](https://git-scm.com/docs/git-checkout#_3_merge_conflict)3. Merge conflict
When a merge conflict happens during switching branches with the `-m` option, you would see something like this:
```
$ git checkout -m mytopic
Auto-merging frotz
ERROR: Merge conflict in frotz
fatal: merge program failed
```

At this point, `git` `diff` shows the changes cleanly merged as in the previous example, as well as the changes in the conflicted files. Edit and resolve the conflict and mark it resolved with `git` `add` as usual:
```
$ edit frotz
$ git add frotz
```

##  [](https://git-scm.com/docs/git-checkout#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-checkoutdefaultRemote)`checkout.defaultRemote` 
    
When you run `git` `checkout` _< something>_ or `git` `switch` _< something>_ and only have one remote, it may implicitly fall back on checking out and tracking e.g. `origin/`_< something>_. This stops working as soon as you have more than one remote with a _< something>_ reference. This setting allows for setting the name of a preferred remote that should always win when it comes to disambiguation. The typical use-case is to set this to `origin`.
Currently this is used by [git-switch[1]](https://git-scm.com/docs/git-switch) and [git-checkout[1]](https://git-scm.com/docs/git-checkout) when `git` `checkout` _< something>_ or `git` `switch` _< something>_ will checkout the _< something>_ branch on another remote, and by [git-worktree[1]](https://git-scm.com/docs/git-worktree) when `git` `worktree` `add` refers to a remote branch. This setting might be used for other checkout-like commands or functionality in the future. 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-checkoutguess)`checkout.guess` 
    
Provides the default value for the `--guess` or `--no-guess` option in `git` `checkout` and `git` `switch`. See [git-switch[1]](https://git-scm.com/docs/git-switch) and [git-checkout[1]](https://git-scm.com/docs/git-checkout). 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-checkoutworkers)`checkout.workers` 
    
The number of parallel workers to use when updating the working tree. The default is one, i.e. sequential execution. If set to a value less than one, Git will use as many workers as the number of logical cores available. This setting and `checkout.thresholdForParallelism` affect all commands that perform checkout. E.g. checkout, clone, reset, sparse-checkout, etc.
Note |  Parallel checkout usually delivers better performance for repositories located on SSDs or over NFS. For repositories on spinning disks and/or machines with a small number of cores, the default sequential checkout often performs better. The size and compression level of a repository might also influence how well the parallel version performs.   
---|--- 

[](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-checkoutthresholdForParallelism)`checkout.thresholdForParallelism` 
      
When running parallel checkout with a small number of files, the cost of subprocess spawning and inter-process communication might outweigh the parallelization gains. This setting allows you to define the minimum number of files for which parallel checkout should be attempted. The default is 100.
##  [](https://git-scm.com/docs/git-checkout#_see_also)SEE ALSO
[git-switch[1]](https://git-scm.com/docs/git-switch), [git-restore[1]](https://git-scm.com/docs/git-restore)
##  [](https://git-scm.com/docs/git-checkout#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### checkout
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
