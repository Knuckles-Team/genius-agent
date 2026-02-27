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
    * [NAME](https://git-scm.com/docs/git-rev-parse#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-rev-parse#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-rev-parse#_description)
    * [OPTIONS](https://git-scm.com/docs/git-rev-parse#_options)
    * [SPECIFYING REVISIONS](https://git-scm.com/docs/git-rev-parse#_specifying_revisions)
    * [SPECIFYING RANGES](https://git-scm.com/docs/git-rev-parse#_specifying_ranges)
    * [Revision Range Summary](https://git-scm.com/docs/git-rev-parse#_revision_range_summary)
    * [PARSEOPT](https://git-scm.com/docs/git-rev-parse#_parseopt)
    * [SQ-QUOTE](https://git-scm.com/docs/git-rev-parse#_sq_quote)
    * [EXAMPLES](https://git-scm.com/docs/git-rev-parse#_examples)
    * [GIT](https://git-scm.com/docs/git-rev-parse#_git)


[ English ▾](https://git-scm.com/docs/git-rev-parse)
Localized versions of **git-rev-parse** manual
  1. [English ](https://git-scm.com/docs/git-rev-parse)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-rev-parse/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-rev-parse/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-rev-parse/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-rev-parse)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-rev-parse) git-rev-parse last updated in 2.52.0
Changes in the **git-rev-parse** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-rev-parse/2.52.0)
  3. [2.51.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-27_ ](https://git-scm.com/docs/git-rev-parse/2.51.2)
  4. 2.45.4 → 2.51.1 no changes
  5. [2.45.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-rev-parse/2.45.3)
  6. 2.45.1 → 2.45.2 no changes
  7. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-rev-parse/2.45.0)
  8. 2.44.1 → 2.44.4 no changes
  9. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-rev-parse/2.44.0)
  10. 2.43.1 → 2.43.7 no changes
  11. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-rev-parse/2.43.0)
  12. 2.42.1 → 2.42.4 no changes
  13. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-rev-parse/2.42.0)
  14. 2.41.1 → 2.41.3 no changes
  15. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-rev-parse/2.41.0)
  16. 2.39.4 → 2.40.4 no changes
  17. [2.39.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-04-17_ ](https://git-scm.com/docs/git-rev-parse/2.39.3)
  18. 2.39.1 → 2.39.2 no changes
  19. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-rev-parse/2.39.0)
  20. 2.37.3 → 2.38.5 no changes
  21. [2.37.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-08-11_ ](https://git-scm.com/docs/git-rev-parse/2.37.2)
  22. 2.33.1 → 2.37.1 no changes
  23. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-rev-parse/2.33.0)
  24. 2.31.1 → 2.32.7 no changes
  25. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-rev-parse/2.31.0)
  26. 2.30.1 → 2.30.9 no changes
  27. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-rev-parse/2.30.0)
  28. 2.29.1 → 2.29.3 no changes
  29. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-rev-parse/2.29.0)
  30. 2.27.1 → 2.28.1 no changes
  31. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-rev-parse/2.27.0)
  32. 2.25.1 → 2.26.3 no changes
  33. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-rev-parse/2.25.0)
  34. 2.23.1 → 2.24.4 no changes
  35. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-rev-parse/2.23.0)
  36. 2.22.1 → 2.22.5 no changes
  37. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-rev-parse/2.22.0)
  38. 2.19.1 → 2.21.4 no changes
  39. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-rev-parse/2.19.0)
  40. 2.18.1 → 2.18.5 no changes
  41. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-rev-parse/2.18.0)
  42. 2.17.0 → 2.17.6 no changes
  43. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-rev-parse/2.16.6)
  44. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-rev-parse/2.15.4)
  45. 2.14.6 no changes
  46. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-rev-parse/2.13.7)
  47. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-rev-parse/2.12.5)
  48. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-rev-parse/2.11.4)
  49. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-rev-parse/2.10.5)
  50. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-rev-parse/2.9.5)
  51. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-rev-parse/2.8.6)
  52. 2.6.7 → 2.7.6 no changes
  53. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-rev-parse/2.5.6)
  54. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-rev-parse/2.4.12)
  55. 2.3.10 no changes
  56. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-rev-parse/2.2.3)
  57. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-rev-parse/2.1.4)
  58. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-rev-parse/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-rev-parse#_name)NAME
git-rev-parse - Pick out and massage parameters
##  [](https://git-scm.com/docs/git-rev-parse#_synopsis)SYNOPSIS
```
_git rev-parse_ [<options>] <arg>…​
```

##  [](https://git-scm.com/docs/git-rev-parse#_description)DESCRIPTION
Many Git porcelainish commands take a mixture of flags (i.e. parameters that begin with a dash _-_) and parameters meant for the underlying _git rev-list_ command they use internally and flags and parameters for the other commands they use downstream of _git rev-list_. The primary purpose of this command is to allow calling programs to distinguish between them. There are a few other operation modes that have nothing to do with the above "help parse command line options".
Unless otherwise specified, most of the options and operation modes require you to run this command inside a git repository or a working tree that is under the control of a git repository, and will give you a fatal error otherwise.
##  [](https://git-scm.com/docs/git-rev-parse#_options)OPTIONS
###  [](https://git-scm.com/docs/git-rev-parse#_operation_modes)Operation Modes
Each of these options must appear first on the command line. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---parseopt)--parseopt 
    
Use _git rev-parse_ in option parsing mode (see PARSEOPT section below). The command in this mode can be used outside a repository or a working tree controlled by a repository. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---sq-quote)--sq-quote 
    
Use _git rev-parse_ in shell quoting mode (see SQ-QUOTE section below). In contrast to the `--sq` option below, this mode only does quoting. Nothing else is done to command input. The command in this mode can be used outside a repository or a working tree controlled by a repository.
###  [](https://git-scm.com/docs/git-rev-parse#_options_for_parseopt)Options for --parseopt 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---keep-dashdash)--keep-dashdash 
    
Only meaningful in `--parseopt` mode. Tells the option parser to echo out the first `--` met instead of skipping it. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---stop-at-non-option)--stop-at-non-option 
    
Only meaningful in `--parseopt` mode. Lets the option parser stop at the first non-option argument. This can be used to parse sub-commands that take options themselves. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---stuck-long)--stuck-long 
    
Only meaningful in `--parseopt` mode. Output the options in their long form if available, and with their arguments stuck.
###  [](https://git-scm.com/docs/git-rev-parse#_options_for_filtering)Options for Filtering 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---revs-only)--revs-only 
    
Do not output flags and parameters not meant for _git rev-list_ command. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---no-revs)--no-revs 
    
Do not output flags and parameters meant for _git rev-list_ command. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---flags)--flags 
    
Do not output non-flag parameters. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---no-flags)--no-flags 
    
Do not output flag parameters.
###  [](https://git-scm.com/docs/git-rev-parse#_options_for_output)Options for Output 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---defaultarg)--default <arg> 
    
If there is no parameter given by the user, use _< arg>_ instead. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---prefixarg)--prefix <arg> 
    
Behave as if _git rev-parse_ was invoked from the _< arg>_ subdirectory of the working tree. Any relative filenames are resolved as if they are prefixed by _< arg>_ and will be printed in that form.
This can be used to convert arguments to a command run in a subdirectory so that they can still be used after moving to the top-level of the repository. For example:
```
prefix=$(git rev-parse --show-prefix)
cd "$(git rev-parse --show-toplevel)"
# rev-parse provides the -- needed for 'set'
eval "set $(git rev-parse --sq --prefix "$prefix" -- "$@")"
```


[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---verify)--verify 
    
Verify that exactly one parameter is provided, and that it can be turned into a raw 20-byte SHA-1 that can be used to access the object database. If so, emit it to the standard output; otherwise, error out.
If you want to make sure that the output actually names an object in your object database and/or can be used as a specific type of object you require, you can add the `^{type}` peeling operator to the parameter. For example, `git` `rev-parse` `"$VAR^{commit}"` will make sure `$VAR` names an existing object that is a commit-ish (i.e. a commit, or an annotated tag that points at a commit). To make sure that `$VAR` names an existing object of any type, `git` `rev-parse` `"$VAR^{object}"` can be used.
Note that if you are verifying a name from an untrusted source, it is wise to use `--end-of-options` so that the name argument is not mistaken for another option. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt--q)-q 


[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---quiet)--quiet 
    
Only meaningful in `--verify` mode. Do not output an error message if the first argument is not a valid object name; instead exit with non-zero status silently. SHA-1s for valid object names are printed to stdout on success. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---sq)--sq 
    
Usually the output is made one line per flag and parameter. This option makes output a single line, properly quoted for consumption by shell. Useful when you expect your parameter to contain whitespaces and newlines (e.g. when using pickaxe `-S` with _git diff-*_). In contrast to the `--sq-quote` option, the command input is still interpreted as usual. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---shortlength)--short[=<length>] 
    
Same as `--verify` but shortens the object name to a unique prefix with at least `length` characters. The minimum length is 4, the default is the effective value of the `core.abbrev` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---not)--not 
    
When showing object names, prefix them with _^_ and strip _^_ prefix from the object names that already have one. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---abbrev-refstrictloose)--abbrev-ref[=(strict|loose)] 
    
A non-ambiguous short name of the objects name. The option core.warnAmbiguousRefs is used to select the strict abbreviation mode. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---symbolic)--symbolic 
    
Usually the object names are output in SHA-1 form (with possible _^_ prefix); this option makes them output in a form as close to the original input as possible. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---symbolic-full-name)--symbolic-full-name 
    
This is similar to --symbolic, but it omits input that are not refs (i.e. branch or tag names; or more explicitly disambiguating "heads/master" form, when you want to name the "master" branch when there is an unfortunately named tag "master"), and shows them as full refnames (e.g. "refs/heads/master"). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---output-object-formatsha1sha256storage)--output-object-format=(sha1|sha256|storage) 
    
Allow oids to be input from any object format that the current repository supports.
Specifying "sha1" translates if necessary and returns a sha1 oid.
Specifying "sha256" translates if necessary and returns a sha256 oid.
Specifying "storage" translates if necessary and returns an oid in encoded in the storage hash algorithm.
###  [](https://git-scm.com/docs/git-rev-parse#_options_for_objects)Options for Objects 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---all)--all 
    
Show all refs found in `refs/`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---branchespattern)--branches[=<pattern>] 


[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---tagspattern)--tags[=<pattern>] 


[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---remotespattern)--remotes[=<pattern>] 
    
Show all branches, tags, or remote-tracking branches, respectively (i.e., refs found in `refs/heads`, `refs/tags`, or `refs/remotes`, respectively).
If a `pattern` is given, only refs matching the given shell glob are shown. If the pattern does not contain a globbing character (_?_ , `*`, or [), it is turned into a prefix match by appending `/*`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---globpattern)--glob=<pattern> 
    
Show all refs matching the shell glob pattern `pattern`. If the pattern does not start with `refs/`, this is automatically prepended. If the pattern does not contain a globbing character (_?_ , `*`, or [), it is turned into a prefix match by appending `/*`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---excludeglob-pattern)--exclude=<glob-pattern> 
    
Do not include refs matching _< glob-pattern>_ that the next `--all`, `--branches`, `--tags`, `--remotes`, or `--glob` would otherwise consider. Repetitions of this option accumulate exclusion patterns up to the next `--all`, `--branches`, `--tags`, `--remotes`, or `--glob` option (other options or arguments do not clear accumulated patterns).
The patterns given should not begin with `refs/heads`, `refs/tags`, or `refs/remotes` when applied to `--branches`, `--tags`, or `--remotes`, respectively, and they must begin with `refs/` when applied to `--glob` or `--all`. If a trailing _/*_ is intended, it must be given explicitly. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---exclude-hiddenfetchreceiveuploadpack)--exclude-hidden=(fetch|receive|uploadpack) 
    
Do not include refs that would be hidden by `git-fetch`, `git-receive-pack` or `git-upload-pack` by consulting the appropriate `fetch.hideRefs`, `receive.hideRefs` or `uploadpack.hideRefs` configuration along with `transfer.hideRefs` (see [git-config[1]](https://git-scm.com/docs/git-config)). This option affects the next pseudo-ref option `--all` or `--glob` and is cleared after processing them. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---disambiguateprefix)--disambiguate=<prefix> 
    
Show every object whose name begins with the given prefix. The <prefix> must be at least 4 hexadecimal digits long to avoid listing each and every object in the repository by mistake.
###  [](https://git-scm.com/docs/git-rev-parse#_options_for_files)Options for Files 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---local-env-vars)--local-env-vars 
    
List the GIT_* environment variables that are local to the repository (e.g. GIT_DIR or GIT_WORK_TREE, but not GIT_EDITOR). Only the names of the variables are listed, not their value, even if they are set. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---path-formatabsoluterelative)--path-format=(absolute|relative) 
    
Controls the behavior of certain other options. If specified as absolute, the paths printed by those options will be absolute and canonical. If specified as relative, the paths will be relative to the current working directory if that is possible. The default is option specific.
This option may be specified multiple times and affects only the arguments that follow it on the command line, either to the end of the command line or the next instance of this option.
The following options are modified by `--path-format`: 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---git-dir)--git-dir 
    
Show `$GIT_DIR` if defined. Otherwise show the path to the .git directory. The path shown, when relative, is relative to the current working directory.
If `$GIT_DIR` is not defined and the current directory is not detected to lie in a Git repository or work tree print a message to stderr and exit with nonzero status. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---git-common-dir)--git-common-dir 
    
Show `$GIT_COMMON_DIR` if defined, else `$GIT_DIR`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---resolve-git-dirpath)--resolve-git-dir <path> 
    
Check if <path> is a valid repository or a gitfile that points at a valid repository, and print the location of the repository. If <path> is a gitfile then the resolved path to the real repository is printed. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---git-pathpath)--git-path <path> 
    
Resolve "$GIT_DIR/<path>" and takes other path relocation variables such as $GIT_OBJECT_DIRECTORY, $GIT_INDEX_FILE…​ into account. For example, if $GIT_OBJECT_DIRECTORY is set to /foo/bar then "git rev-parse --git-path objects/abc" returns /foo/bar/abc. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---show-toplevel)--show-toplevel 
    
Show the (by default, absolute) path of the top-level directory of the working tree. If there is no working tree, report an error. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---show-superproject-working-tree)--show-superproject-working-tree 
    
Show the absolute path of the root of the superproject’s working tree (if exists) that uses the current repository as its submodule. Outputs nothing if the current repository is not used as a submodule by any project. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---shared-index-path)--shared-index-path 
    
Show the path to the shared index file in split index mode, or empty if not in split-index mode.
The following options are unaffected by `--path-format`: 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---absolute-git-dir)--absolute-git-dir 
    
Like `--git-dir`, but its output is always the canonicalized absolute path. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---is-inside-git-dir)--is-inside-git-dir 
    
When the current working directory is below the repository directory print "true", otherwise "false". 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---is-inside-work-tree)--is-inside-work-tree 
    
When the current working directory is inside the work tree of the repository print "true", otherwise "false". 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---is-bare-repository)--is-bare-repository 
    
When the repository is bare print "true", otherwise "false". 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---is-shallow-repository)--is-shallow-repository 
    
When the repository is shallow print "true", otherwise "false". 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---show-cdup)--show-cdup 
    
When the command is invoked from a subdirectory, show the path of the top-level directory relative to the current directory (typically a sequence of "../", or an empty string). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---show-prefix)--show-prefix 
    
When the command is invoked from a subdirectory, show the path of the current directory relative to the top-level directory. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---show-object-formatstorageinputoutputcompat)--show-object-format[=(storage|input|output|compat)] 
    
Show the object format (hash algorithm) used for the repository for storage inside the `.git` directory, input, output, or compatibility. For input, multiple algorithms may be printed, space-separated. If `compat` is requested and no compatibility algorithm is enabled, prints an empty line. If not specified, the default is "storage". 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---show-ref-format)--show-ref-format 
    
Show the reference storage format used for the repository.
###  [](https://git-scm.com/docs/git-rev-parse#_other_options)Other Options 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---sincedatestring)--since=<datestring> 


[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---afterdatestring)--after=<datestring> 
    
Parse the date string, and output the corresponding --max-age= parameter for _git rev-list_. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---untildatestring)--until=<datestring> 


[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt---beforedatestring)--before=<datestring> 
    
Parse the date string, and output the corresponding --min-age= parameter for _git rev-list_. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-arg)<arg>…​ 
    
Flags and parameters to be parsed.
##  [](https://git-scm.com/docs/git-rev-parse#_specifying_revisions)SPECIFYING REVISIONS
A revision parameter _< rev>_ typically, but not necessarily, names a commit object. It uses what is called an _extended SHA-1_ syntax. Here are various ways to spell object names. The ones listed near the end of this list name trees and blobs contained in a commit.
Note |  This document shows the "raw" syntax as seen by git. The shell and other UIs might require additional quoting to protect special characters and to avoid word splitting.   
---|--- 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-sha1egdae86e1950b1277e545cee180551750029cfe735dae86e)_< sha1>_, e.g. _dae86e1950b1277e545cee180551750029cfe735_ , _dae86e_ 
      
The full SHA-1 object name (40-byte hexadecimal string), or a leading substring that is unique within the repository. E.g. dae86e1950b1277e545cee180551750029cfe735 and dae86e both name the same commit object if there is no other object in your repository whose object name starts with dae86e. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-describeOutputegv1742-679-g3bee7fb)_< describeOutput>_, e.g. _v1.7.4.2-679-g3bee7fb_ 
    
Output from `git` `describe`; i.e. a closest tag, optionally followed by a dash and a number of commits, followed by a dash, a _g_ , and an abbreviated object name. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-refnameegmasterheadsmasterrefsheadsmaster)_< refname>_, e.g. _master_ , _heads/master_ , _refs/heads/master_ 
    
A symbolic ref name. E.g. _master_ typically means the commit object referenced by _refs/heads/master_. If you happen to have both _heads/master_ and _tags/master_ , you can explicitly say _heads/master_ to tell Git which one you mean. When ambiguous, a _< refname>_ is disambiguated by taking the first match in the following rules:
  1. If _$GIT_DIR/ <refname>_ exists, that is what you mean (this is usually useful only for `HEAD`, `FETCH_HEAD`, `ORIG_HEAD`, `MERGE_HEAD`, `REBASE_HEAD`, `REVERT_HEAD`, `CHERRY_PICK_HEAD`, `BISECT_HEAD` and `AUTO_MERGE`);
  2. otherwise, _refs/ <refname>_ if it exists;
  3. otherwise, _refs/tags/ <refname>_ if it exists;
  4. otherwise, _refs/heads/ <refname>_ if it exists;
  5. otherwise, _refs/remotes/ <refname>_ if it exists;
  6. otherwise, _refs/remotes/ <refname>/HEAD_ if it exists. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-HEAD)`HEAD` 
    
names the commit on which you based the changes in the working tree. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-FETCHHEAD)`FETCH_HEAD` 
    
records the branch which you fetched from a remote repository with your last `git` `fetch` invocation. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-ORIGHEAD)`ORIG_HEAD` 
    
is created by commands that move your `HEAD` in a drastic way (`git` `am`, `git` `merge`, `git` `rebase`, `git` `reset`), to record the position of the `HEAD` before their operation, so that you can easily change the tip of the branch back to the state before you ran them. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-MERGEHEAD)`MERGE_HEAD` 
    
records the commit(s) which you are merging into your branch when you run `git` `merge`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-REBASEHEAD)`REBASE_HEAD` 
    
during a rebase, records the commit at which the operation is currently stopped, either because of conflicts or an `edit` command in an interactive rebase. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-REVERTHEAD)`REVERT_HEAD` 
    
records the commit which you are reverting when you run `git` `revert`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-CHERRYPICKHEAD)`CHERRY_PICK_HEAD` 
    
records the commit which you are cherry-picking when you run `git` `cherry-pick`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-BISECTHEAD)`BISECT_HEAD` 
    
records the current commit to be tested when you run `git` `bisect` `--no-checkout`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-AUTOMERGE)`AUTO_MERGE` 
    
records a tree object corresponding to the state the _ort_ merge strategy wrote to the working tree when a merge operation resulted in conflicts.


Note that any of the _refs/*_ cases above may come either from the `$GIT_DIR/refs` directory or from the `$GIT_DIR/packed-refs` file. While the ref name encoding is unspecified, UTF-8 is preferred as some output processing may assume ref names in UTF-8. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-)_@_ 
    
_@_ alone is a shortcut for `HEAD`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-refnamedateegmasteryesterdayHEAD5minutesago)_[ <refname>]@{<date>}_, e.g. _master@{yesterday}_ , _HEAD@{5 minutes ago}_ 
    
A ref followed by the suffix _@_ with a date specification enclosed in a brace pair (e.g. _{yesterday}_ , _{1 month 2 weeks 3 days 1 hour 1 second ago}_ or _{1979-02-26 18:30:00}_) specifies the value of the ref at a prior point in time. This suffix may only be used immediately following a ref name and the ref must have an existing log (_$GIT_DIR/logs/ <ref>_). Note that this looks up the state of your **local** ref at a given time; e.g., what was in your local _master_ branch last week. If you want to look at commits made during certain times, see `--since` and `--until`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-refnamenegmaster1)_< refname>@{<n>}_, e.g. _master@{1}_ 
    
A ref followed by the suffix _@_ with an ordinal specification enclosed in a brace pair (e.g. _{1}_ , _{15}_) specifies the n-th prior value of that ref. For example _master@{1}_ is the immediate prior value of _master_ while _master@{5}_ is the 5th prior value of _master_. This suffix may only be used immediately following a ref name and the ref must have an existing log (_$GIT_DIR/logs/ <refname>_). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-neg1)_@{ <n>}_, e.g. _@{1}_ 
    
You can use the _@_ construct with an empty ref part to get at a reflog entry of the current branch. For example, if you are on branch _blabla_ then _@{1}_ means the same as _blabla@{1}_. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt--neg-1)_@{- <n>}_, e.g. _@{-1}_ 
    
The construct _@{- <n>}_ means the <n>th branch/commit checked out before the current one. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-branchnameupstreamegmasterupstreamu)_[ <branchname>]@{upstream}_, e.g. _master@{upstream}_ , _@{u}_ 
    
A branch B may be set up to build on top of a branch X (configured with `branch.`_< name>_`.merge`) at a remote R (configured with `branch.`_< name>_`.remote`). B@{u} refers to the remote-tracking branch for the branch X taken from remote R, typically found at `refs/remotes/R/X`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-branchnamepushegmasterpushpush)_[ <branchname>]@{push}_, e.g. _master@{push}_ , _@{push}_ 
    
The suffix _@{push}_ reports the branch "where we would push to" if `git` `push` were run while `branchname` was checked out (or the current `HEAD` if no branchname is specified). Like for _@{upstream}_ , we report the remote-tracking branch that corresponds to that branch at the remote.
Here’s an example to make it more clear:
```
$ git config push.default current
$ git config remote.pushdefault myfork
$ git switch -c mybranch origin/master

$ git rev-parse --symbolic-full-name @{upstream}
refs/remotes/origin/master

$ git rev-parse --symbolic-full-name @{push}
refs/remotes/myfork/mybranch
```

Note in the example that we set up a triangular workflow, where we pull from one location and push to another. In a non-triangular workflow, _@{push}_ is the same as _@{upstream}_ , and there is no need for it.
This suffix is also accepted when spelled in uppercase, and means the same thing no matter the case. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revnegHEADv1510)_< rev>^[<n>]_, e.g. _HEAD^, v1.5.1^0_ 
    
A suffix _^_ to a revision parameter means the first parent of that commit object. _^ <n>_ means the <n>th parent (i.e. _< rev>^_ is equivalent to _< rev>^1_). As a special rule, _< rev>^0_ means the commit itself and is used when _< rev>_ is the object name of a tag object that refers to a commit object. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revnegHEADmaster3)_< rev>~[<n>]_, e.g. _HEAD~, master~3_ 
    
A suffix _~_ to a revision parameter means the first parent of that commit object. A suffix _~ <n>_ to a revision parameter means the commit object that is the <n>th generation ancestor of the named commit object, following only the first parents. I.e. _< rev>~3_ is equivalent to _< rev>^^^_ which is equivalent to _< rev>^1^1^1_. See below for an illustration of the usage of this form. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revtypeegv0998commit)_< rev>^{<type>}_, e.g. _v0.99.8^{commit}_ 
    
A suffix _^_ followed by an object type name enclosed in brace pair means dereference the object at _< rev>_ recursively until an object of type _< type>_ is found or the object cannot be dereferenced anymore (in which case, barf). For example, if _< rev>_ is a commit-ish, _< rev>^{commit}_ describes the corresponding commit object. Similarly, if _< rev>_ is a tree-ish, _< rev>^{tree}_ describes the corresponding tree object. _< rev>^0_ is a short-hand for _< rev>^{commit}_.
_< rev>^{object}_ can be used to make sure _< rev>_ names an object that exists, without requiring _< rev>_ to be a tag, and without dereferencing _< rev>_; because a tag is already an object, it does not have to be dereferenced even once to get to an object.
_< rev>^{tag}_ can be used to ensure that _< rev>_ identifies an existing tag object. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revegv0998)_< rev>^{}_, e.g. _v0.99.8^{}_ 
    
A suffix _^_ followed by an empty brace pair means the object could be a tag, and dereference the tag recursively until a non-tag object is found. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revtextegHEADfixnastybug)_< rev>^{/<text>}_, e.g. _HEAD^{/fix nasty bug}_ 
    
A suffix _^_ to a revision parameter, followed by a brace pair that contains a text led by a slash, is the same as the _:/fix nasty bug_ syntax below except that it returns the youngest matching commit which is reachable from the _< rev>_ before _^_. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-textegfixnastybug)_:/ <text>_, e.g. _:/fix nasty bug_ 
    
A colon, followed by a slash, followed by a text, names a commit whose commit message matches the specified regular expression. This name returns the youngest matching commit which is reachable from any ref, including HEAD. The regular expression can match any part of the commit message. To match messages starting with a string, one can use e.g. _:/^foo_. The special sequence _:/!_ is reserved for modifiers to what is matched. _:/!-foo_ performs a negative match, while _:/!!foo_ matches a literal _!_ character, followed by _foo_. Any other sequence beginning with _:/!_ is reserved for now. Depending on the given text, the shell’s word splitting rules might require additional quoting. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revpathegHEADREADMEmasterREADME)_< rev>:<path>_, e.g. _HEAD:README_ , _master:./README_ 
    
A suffix _:_ followed by a path names the blob or tree at the given path in the tree-ish object named by the part before the colon. A path starting with _./_ or _../_ is relative to the current working directory. The given path will be converted to be relative to the working tree’s root directory. This is most useful to address a blob or tree from a commit or tree that has the same tree structure as the working tree. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-npatheg0READMEREADME)_:[ <n>:]<path>_, e.g. _:0:README_ , _:README_ 
    
A colon, optionally followed by a stage number (0 to 3) and a colon, followed by a path, names a blob object in the index at the given path. A missing stage number (and the colon that follows it) names a stage 0 entry. During a merge, stage 1 is the common ancestor, stage 2 is the target branch’s version (typically the current branch), and stage 3 is the version from the branch which is being merged.
Here is an illustration, by Jon Loeliger. Both commit nodes B and C are parents of commit node A. Parent commits are ordered left-to-right.
```
G   H   I   J
 \ /     \ /
  D   E   F
   \  |  / \
    \ | /   |
     \|/    |
      B     C
       \   /
        \ /
         A
```

```
A =      = A^0
B = A^   = A^1     = A~1
C =      = A^2
D = A^^  = A^1^1   = A~2
E = B^2  = A^^2
F = B^3  = A^^3
G = A^^^ = A^1^1^1 = A~3
H = D^2  = B^^2    = A^^^2  = A~2^2
I = F^   = B^3^    = A^^3^
J = F^2  = B^3^2   = A^^3^2
```

##  [](https://git-scm.com/docs/git-rev-parse#_specifying_ranges)SPECIFYING RANGES
History traversing commands such as `git` `log` operate on a set of commits, not just a single commit.
For these commands, specifying a single revision, using the notation described in the previous section, means the set of commits `reachable` from the given commit.
Specifying several revisions means the set of commits reachable from any of the given commits.
A commit’s reachable set is the commit itself and the commits in its ancestry chain.
There are several notations to specify a set of connected commits (called a "revision range"), illustrated below.
###  [](https://git-scm.com/docs/git-rev-parse#_commit_exclusions)Commit Exclusions 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revcaretNotation)_^ <rev>_ (caret) Notation 
    
To exclude commits reachable from a commit, a prefix _^_ notation is used. E.g. _^r1 r2_ means commits reachable from _r2_ but exclude the ones reachable from _r1_ (i.e. _r1_ and its ancestors).
###  [](https://git-scm.com/docs/git-rev-parse#_dotted_range_notations)Dotted Range Notations 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-Thetwo-dotRangeNotation)The _.._ (two-dot) Range Notation 
    
The _^r1 r2_ set operation appears so often that there is a shorthand for it. When you have two commits _r1_ and _r2_ (named according to the syntax explained in SPECIFYING REVISIONS above), you can ask for commits that are reachable from r2 excluding those that are reachable from r1 by _^r1 r2_ and it can be written as _r1..r2_. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-Thethree-dotSymmetricDifferenceNotation)The _..._ (three-dot) Symmetric Difference Notation 
    
A similar notation _r1...r2_ is called symmetric difference of _r1_ and _r2_ and is defined as _r1 r2 --not $(git merge-base --all r1 r2)_. It is the set of commits that are reachable from either one of _r1_ (left side) or _r2_ (right side) but not from both.
In these two shorthand notations, you can omit one end and let it default to HEAD. For example, _origin.._ is a shorthand for _origin..HEAD_ and asks "What did I do since I forked from the origin branch?" Similarly, _..origin_ is a shorthand for _HEAD..origin_ and asks "What did the origin do since I forked from them?" Note that _.._ would mean _HEAD..HEAD_ which is an empty range that is both reachable and unreachable from HEAD.
Commands that are specifically designed to take two distinct ranges (e.g. "git range-diff R1 R2" to compare two ranges) do exist, but they are exceptions. Unless otherwise noted, all "git" commands that operate on a set of commits work on a single revision range. In other words, writing two "two-dot range notation" next to each other, e.g.
```
$ git log A..B C..D
```

does **not** specify two revision ranges for most commands. Instead it will name a single connected set of commits, i.e. those that are reachable from either B or D but are reachable from neither A or C. In a linear history like this:
```
---A---B---o---o---C---D
```

because A and B are reachable from C, the revision range specified by these two dotted ranges is a single commit D.
###  [](https://git-scm.com/docs/git-rev-parse#_other_rev_parent_shorthand_notations)Other <rev>^ Parent Shorthand Notations
Three other shorthands exist, particularly useful for merge commits, for naming a set that is formed by a commit and its parent commits.
The _r1^@_ notation means all parents of _r1_.
The _r1^!_ notation includes commit _r1_ but excludes all of its parents. By itself, this notation denotes the single commit _r1_.
The _< rev>^-[<n>]_ notation includes _< rev>_ but excludes the <n>th parent (i.e. a shorthand for _< rev>^<n>..<rev>_), with _< n>_ = 1 if not given. This is typically useful for merge commits where you can just pass _< commit>^-_ to get all the commits in the branch that was merged in merge commit _< commit>_ (including _< commit>_ itself).
While _< rev>^<n>_ was about specifying a single commit parent, these three notations also consider its parents. For example you can say _HEAD^2^@_ , however you cannot say _HEAD^@^2_.
##  [](https://git-scm.com/docs/git-rev-parse#_revision_range_summary)Revision Range Summary 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-rev)_< rev>_ 
    
Include commits that are reachable from <rev> (i.e. <rev> and its ancestors). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-rev-1)_^ <rev>_ 
    
Exclude commits that are reachable from <rev> (i.e. <rev> and its ancestors). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-rev1rev2)_< rev1>..<rev2>_ 
    
Include commits that are reachable from <rev2> but exclude those that are reachable from <rev1>. When either <rev1> or <rev2> is omitted, it defaults to `HEAD`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-rev1rev2-1)_< rev1>...<rev2>_ 
    
Include commits that are reachable from either <rev1> or <rev2> but exclude those that are reachable from both. When either <rev1> or <rev2> is omitted, it defaults to `HEAD`. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revegHEAD)_< rev>^@_, e.g. _HEAD^@_ 
    
A suffix _^_ followed by an at sign is the same as listing all parents of _< rev>_ (meaning, include anything reachable from its parents, but not the commit itself). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-revegHEAD-1)_< rev>^!_, e.g. _HEAD^!_ 
    
A suffix _^_ followed by an exclamation mark is the same as giving commit _< rev>_ and all its parents prefixed with _^_ to exclude them (and their ancestors). 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-rev-negHEAD-HEAD-2)_< rev>^-<n>_, e.g. _HEAD^-, HEAD^-2_ 
    
Equivalent to _< rev>^<n>..<rev>_, with _< n>_ = 1 if not given.
Here are a handful of examples using the Loeliger illustration above, with each step in the notation’s expansion and selection carefully spelt out:
```
   Args   Expanded arguments    Selected commits
   D                            G H D
   D F                          G H I J D F
   ^G D                         H D
   ^D B                         E I J F B
   ^D B C                       E I J F B C
   C                            I J F C
   B..C   = ^B C                C
   B...C  = B ^F C              G H D E B C
   B^-    = B^..B
	  = ^B^1 B              E I J F B
   C^@    = C^1
	  = F                   I J F
   B^@    = B^1 B^2 B^3
	  = D E F               D G H E F I J
   C^!    = C ^C^@
	  = C ^C^1
	  = C ^F                C
   B^!    = B ^B^@
	  = B ^B^1 ^B^2 ^B^3
	  = B ^D ^E ^F          B
   F^! D  = F ^I ^J D           G H D F
```

##  [](https://git-scm.com/docs/git-rev-parse#_parseopt)PARSEOPT
In `--parseopt` mode, _git rev-parse_ helps massaging options to bring to shell scripts the same facilities C builtins have. It works as an option normalizer (e.g. splits single switches aggregate values), a bit like `getopt`(`1`) does.
It takes on the standard input the specification of the options to parse and understand, and echoes on the standard output a string suitable for `sh`(`1`) `eval` to replace the arguments with normalized ones. In case of error, it outputs usage on the standard error stream, and exits with code 129.
Note: Make sure you quote the result when passing it to `eval`. See below for an example.
###  [](https://git-scm.com/docs/git-rev-parse#_input_format)Input Format
_git rev-parse --parseopt_ input format is fully text based. It has two parts, separated by a line that contains only `--`. The lines before the separator (should be one or more) are used for the usage. The lines after the separator describe the options.
Each line of options has this format:
```
<opt-spec><flags>*<arg-hint>? SP+ help LF
```


[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-opt-spec)_< opt-spec>_ 
    
its format is the short option character, then the long option name separated by a comma. Both parts are not required, though at least one is necessary. May not contain any of the _< flags>_ characters. `h,help`, `dry-run` and `f` are examples of correct _< opt-spec>_. 

[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-flags)_< flags>_ 
    
_< flags>_ are of `*`, `=`, _?_ or `!`.
  * Use `=` if the option takes an argument.
  * Use _?_ to mean that the option takes an optional argument. You probably want to use the `--stuck-long` mode to be able to unambiguously parse the optional argument.
  * Use `*` to mean that this option should not be listed in the usage generated for the `-h` argument. It’s shown for `--help-all` as documented in [gitcli[7]](https://git-scm.com/docs/gitcli).
  * Use `!` to not make the corresponding negated long option available.



[](https://git-scm.com/docs/git-rev-parse#Documentation/git-rev-parse.txt-arg-hint)_< arg-hint>_ 
    
_< arg-hint>_, if specified, is used as a name of the argument in the help output, for options that take arguments. _< arg-hint>_ is terminated by the first whitespace. It is customary to use a dash to separate words in a multi-word argument hint.
The remainder of the line, after stripping the spaces, is used as the help associated with the option.
Blank lines are ignored, and lines that don’t match this specification are used as option group headers (start the line with a space to create such lines on purpose).
###  [](https://git-scm.com/docs/git-rev-parse#_example)Example
```
OPTS_SPEC="\
some-command [<options>] <args>...

some-command does foo and bar!
--
h,help!   show the help

foo       some nifty option --foo
bar=      some cool option --bar with an argument
baz=arg   another cool option --baz with a named argument
qux?path  qux may take a path argument but has meaning by itself

  An option group Header
C?        option C with an optional argument"

eval "$(echo "$OPTS_SPEC" | git rev-parse --parseopt -- "$@" || echo exit $?)"
```

###  [](https://git-scm.com/docs/git-rev-parse#_usage_text)Usage text
When `"$@"` is `-h` or `--help` in the above example, the following usage text would be shown:
```
usage: some-command [<options>] <args>...

    some-command does foo and bar!

    -h, --help            show the help
    --[no-]foo            some nifty option --foo
    --[no-]bar ...        some cool option --bar with an argument
    --[no-]baz <arg>      another cool option --baz with a named argument
    --[no-]qux[=<path>]   qux may take a path argument but has meaning by itself

An option group Header
    -C[...]               option C with an optional argument
```

##  [](https://git-scm.com/docs/git-rev-parse#_sq_quote)SQ-QUOTE
In `--sq-quote` mode, _git rev-parse_ echoes on the standard output a single line suitable for `sh`(`1`) `eval`. This line is made by normalizing the arguments following `--sq-quote`. Nothing other than quoting the arguments is done.
If you want command input to still be interpreted as usual by _git rev-parse_ before the output is shell quoted, see the `--sq` option.
###  [](https://git-scm.com/docs/git-rev-parse#_example_2)Example
```
$ cat >your-git-script.sh <<\EOF
#!/bin/sh
args=$(git rev-parse --sq-quote "$@")   # quote user-supplied arguments
command="git frotz -n24 $args"          # and use it inside a handcrafted
					# command line
eval "$command"
EOF

$ sh your-git-script.sh "a b'c"
```

##  [](https://git-scm.com/docs/git-rev-parse#_examples)EXAMPLES
  * Print the object name of the current commit:
```
$ git rev-parse --verify HEAD
```

  * Print the commit object name from the revision in the $REV shell variable:
```
$ git rev-parse --verify --end-of-options $REV^{commit}
```

This will error out if $REV is empty or not a valid revision.
  * Similar to above:
```
$ git rev-parse --default master --verify --end-of-options $REV
```

but if $REV is empty, the commit object name from master will be printed.


##  [](https://git-scm.com/docs/git-rev-parse#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### rev-parse
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
