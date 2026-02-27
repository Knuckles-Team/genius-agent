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
    * [NAME](https://git-scm.com/docs/git-fsck#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-fsck#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-fsck#_description)
    * [OPTIONS](https://git-scm.com/docs/git-fsck#_options)
    * [CONFIGURATION](https://git-scm.com/docs/git-fsck#_configuration)
    * [DISCUSSION](https://git-scm.com/docs/git-fsck#_discussion)
    * [Extracted Diagnostics](https://git-scm.com/docs/git-fsck#_extracted_diagnostics)
    * [FSCK MESSAGES](https://git-scm.com/docs/git-fsck#_fsck_messages)
    * [Environment Variables](https://git-scm.com/docs/git-fsck#_environment_variables)
    * [GIT](https://git-scm.com/docs/git-fsck#_git)


[ English ▾](https://git-scm.com/docs/git-fsck)
Localized versions of **git-fsck** manual
  1. [English ](https://git-scm.com/docs/git-fsck)
  2. [Français ](https://git-scm.com/docs/git-fsck/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-fsck/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-fsck/sv)
  5. [українська мова ](https://git-scm.com/docs/git-fsck/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-fsck/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-fsck)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-fsck) git-fsck last updated in 2.53.0
Changes in the **git-fsck** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-fsck/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-fsck/2.52.0)
  3. 2.50.1 → 2.51.2 no changes
  4. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-fsck/2.50.0)
  5. 2.48.1 → 2.49.1 no changes
  6. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-fsck/2.48.0)
  7. 2.47.1 → 2.47.3 no changes
  8. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git-fsck/2.47.0)
  9. 2.45.3 → 2.46.4 no changes
  10. 2.45.2 no changes
  11. [2.45.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-fsck/2.45.1)
  12. 2.44.3 → 2.45.0 no changes
  13. 2.44.2 no changes
  14. [2.44.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git-fsck/2.44.1)
  15. 2.43.6 → 2.44.0 no changes
  16. 2.43.5 no changes
  17. [2.43.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git-fsck/2.43.4)
  18. 2.43.1 → 2.43.3 no changes
  19. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-fsck/2.43.0)
  20. 2.42.4 no changes
  21. 2.42.3 no changes
  22. [2.42.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git-fsck/2.42.2)
  23. 2.41.3 → 2.42.1 no changes
  24. 2.41.2 no changes
  25. [2.41.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git-fsck/2.41.1)
  26. 2.40.4 → 2.41.0 no changes
  27. 2.40.3 no changes
  28. [2.40.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git-fsck/2.40.2)
  29. 2.40.0 → 2.40.1 no changes
  30. 2.39.5 no changes
  31. [2.39.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git-fsck/2.39.4)
  32. 2.39.3 no changes
  33. [2.39.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-02-06_ ](https://git-scm.com/docs/git-fsck/2.39.2)
  34. 2.39.1 no changes
  35. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-fsck/2.39.0)
  36. 2.38.1 → 2.38.5 no changes
  37. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-fsck/2.38.0)
  38. 2.35.1 → 2.37.7 no changes
  39. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-fsck/2.35.0)
  40. 2.30.2 → 2.34.8 no changes
  41. 2.30.1 no changes
  42. 2.22.2 → 2.30.0 no changes
  43. [2.22.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-11_ ](https://git-scm.com/docs/git-fsck/2.22.1)
  44. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-fsck/2.22.0)
  45. 2.21.1 → 2.21.4 no changes
  46. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-fsck/2.21.0)
  47. 2.19.1 → 2.20.5 no changes
  48. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-fsck/2.19.0)
  49. 2.11.4 → 2.18.5 no changes
  50. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-fsck/2.10.5)
  51. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-fsck/2.9.5)
  52. 2.7.6 → 2.8.6 no changes
  53. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-fsck/2.6.7)
  54. 2.1.4 → 2.5.6 no changes
  55. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-fsck/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-fsck#_name)NAME
git-fsck - Verifies the connectivity and validity of the objects in the database
##  [](https://git-scm.com/docs/git-fsck#_synopsis)SYNOPSIS
```
_git fsck_ [--tags] [--root] [--unreachable] [--cache] [--no-reflogs]
	 [--[no-]full] [--strict] [--verbose] [--lost-found]
	 [--[no-]dangling] [--[no-]progress] [--connectivity-only]
	 [--[no-]name-objects] [--[no-]references] [<object>…​]
```

##  [](https://git-scm.com/docs/git-fsck#_description)DESCRIPTION
Verifies the connectivity and validity of the objects in the database.
##  [](https://git-scm.com/docs/git-fsck#_options)OPTIONS 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-object)<object> 
    
An object to treat as the head of an unreachability trace.
If no objects are given, _git fsck_ defaults to using the index file, all SHA-1 references in the `refs` namespace, and all reflogs (unless --no-reflogs is given) as heads. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---unreachable)--unreachable 
    
Print out objects that exist but that aren’t reachable from any of the reference nodes. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---dangling)--dangling 


[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---no-dangling)--no-dangling 
    
Print objects that exist but that are never _directly_ used (default). `--no-dangling` can be used to omit this information from the output. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---root)--root 
    
Report root nodes. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---tags)--tags 
    
Report tags. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---cache)--cache 
    
Consider any object recorded in the index also as a head node for an unreachability trace. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---no-reflogs)--no-reflogs 
    
Do not consider commits that are referenced only by an entry in a reflog to be reachable. This option is meant only to search for commits that used to be in a ref, but now aren’t, but are still in that corresponding reflog. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---full)--full 
    
Check not just objects in GIT_OBJECT_DIRECTORY ($GIT_DIR/objects), but also the ones found in alternate object pools listed in GIT_ALTERNATE_OBJECT_DIRECTORIES or $GIT_DIR/objects/info/alternates, and in packed Git archives found in $GIT_DIR/objects/pack and corresponding pack subdirectories in alternate object pools. This is now default; you can turn it off with --no-full. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---connectivity-only)--connectivity-only 
    
Check only the connectivity of reachable objects, making sure that any objects referenced by a reachable tag, commit, or tree are present. This speeds up the operation by avoiding reading blobs entirely (though it does still check that referenced blobs exist). This will detect corruption in commits and trees, but not do any semantic checks (e.g., for format errors). Corruption in blob objects will not be detected at all.
Unreachable tags, commits, and trees will also be accessed to find the tips of dangling segments of history. Use `--no-dangling` if you don’t care about this output and want to speed it up further. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---strict)--strict 
    
Enable more strict checking, namely to catch a file mode recorded with g+w bit set, which was created by older versions of Git. Existing repositories, including the Linux kernel, Git itself, and sparse repository have old objects that trigger this check, but it is recommended to check new projects with this flag. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---verbose)--verbose 
    
Be chatty. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---lost-found)--lost-found 
    
Write dangling objects into .git/lost-found/commit/ or .git/lost-found/other/, depending on type. If the object is a blob, the contents are written into the file, rather than its object name. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---name-objects)--name-objects 
    
When displaying names of reachable objects, in addition to the SHA-1 also display a name that describes **how** they are reachable, compatible with [git-rev-parse[1]](https://git-scm.com/docs/git-rev-parse), e.g. `HEAD@{1234567890}~25^2:src/`. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---progress)--progress 


[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---no-progress)--no-progress 
    
Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --no-progress or --verbose is specified. --progress forces progress status even if the standard error stream is not directed to a terminal. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---references)--references 


[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt---no-references)--no-references 
    
Control whether to check the references database consistency via _git refs verify_. See [git-refs[1]](https://git-scm.com/docs/git-refs) for details. The default is to check the references database.
##  [](https://git-scm.com/docs/git-fsck#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-fsckmsg-id)fsck.<msg-id> 
    
During fsck git may find issues with legacy data which wouldn’t be generated by current versions of git, and which wouldn’t be sent over the wire if `transfer.fsckObjects` was set. This feature is intended to support working with legacy repositories containing such data.
Setting `fsck.`_< msg-id>_ will be picked up by [git-fsck[1]](https://git-scm.com/docs/git-fsck), but to accept pushes of such data set `receive.fsck.`_< msg-id>_ instead, or to clone or fetch it set `fetch.fsck.`_< msg-id>_.
The rest of the documentation discusses `fsck.*` for brevity, but the same applies for the corresponding `receive.fsck.*` and `fetch.fsck.*`. variables.
Unlike variables like `color.ui` and `core.editor`, the `receive.fsck.`_< msg-id>_ and `fetch.fsck.`_< msg-id>_ variables will not fall back on the `fsck.`_< msg-id>_ configuration if they aren’t set. To uniformly configure the same fsck settings in different circumstances, all three of them must be set to the same values.
When `fsck.`_< msg-id>_ is set, errors can be switched to warnings and vice versa by configuring the `fsck.`_< msg-id>_ setting where the _< msg-id>_ is the fsck message ID and the value is one of `error`, `warn` or `ignore`. For convenience, fsck prefixes the error/warning with the message ID, e.g. "missingEmail: invalid author/committer line - missing email" means that setting `fsck.missingEmail` `=` `ignore` will hide that issue.
In general, it is better to enumerate existing objects with problems with `fsck.skipList`, instead of listing the kind of breakages these problematic objects share to be ignored, as doing the latter will allow new instances of the same breakages go unnoticed.
Setting an unknown `fsck.`_< msg-id>_ value will cause fsck to die, but doing the same for `receive.fsck.`_< msg-id>_ and `fetch.fsck.`_< msg-id>_ will only cause git to warn.
See the `Fsck` `Messages` section of [git-fsck[1]](https://git-scm.com/docs/git-fsck) for supported values of _< msg-id>_. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-fsckskipList)fsck.skipList 
    
The path to a list of object names (i.e. one unabbreviated SHA-1 per line) that are known to be broken in a non-fatal way and should be ignored. On versions of Git 2.20 and later, comments (_#_), empty lines, and any leading and trailing whitespace are ignored. Everything but a SHA-1 per line will error out on older versions.
This feature is useful when an established project should be accepted despite early commits containing errors that can be safely ignored, such as invalid committer email addresses. Note: corrupt objects cannot be skipped with this setting.
Like `fsck.`_< msg-id>_ this variable has corresponding `receive.fsck.skipList` and `fetch.fsck.skipList` variants.
Unlike variables like `color.ui` and `core.editor` the `receive.fsck.skipList` and `fetch.fsck.skipList` variables will not fall back on the `fsck.skipList` configuration if they aren’t set. To uniformly configure the same fsck settings in different circumstances, all three of them must be set to the same values.
Older versions of Git (before 2.20) documented that the object names list should be sorted. This was never a requirement; the object names could appear in any order, but when reading the list we tracked whether the list was sorted for the purposes of an internal binary search implementation, which could save itself some work with an already sorted list. Unless you had a humongous list there was no reason to go out of your way to pre-sort the list. After Git version 2.20 a hash implementation is used instead, so there’s now no reason to pre-sort the list.
##  [](https://git-scm.com/docs/git-fsck#_discussion)DISCUSSION
git-fsck tests SHA-1 and general object sanity, and it does full tracking of the resulting reachability and everything else. It prints out any corruption it finds (missing or bad objects), and if you use the `--unreachable` flag it will also print out objects that exist but that aren’t reachable from any of the specified head nodes (or the default set, as mentioned above).
Any corrupt objects you will have to find in backups or other archives (i.e., you can just remove them and do an _rsync_ with some other site in the hopes that somebody else has the object you have corrupted).
If core.commitGraph is true, the commit-graph file will also be inspected using _git commit-graph verify_. See [git-commit-graph[1]](https://git-scm.com/docs/git-commit-graph).
##  [](https://git-scm.com/docs/git-fsck#_extracted_diagnostics)Extracted Diagnostics 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-unreachabletypeobject)unreachable <type> <object> 
    
The <type> object <object>, isn’t actually referred to directly or indirectly in any of the trees or commits seen. This can mean that there’s another root node that you’re not specifying or that the tree is corrupt. If you haven’t missed a root node then you might as well delete unreachable nodes since they can’t be used. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingtypeobject)missing <type> <object> 
    
The <type> object <object>, is referred to but isn’t present in the database. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-danglingtypeobject)dangling <type> <object> 
    
The <type> object <object>, is present in the database but never _directly_ used. A dangling commit could be a root node. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-hashmismatchobject)hash mismatch <object> 
    
The database has an object whose hash doesn’t match the object database value. This indicates a serious data integrity problem.
##  [](https://git-scm.com/docs/git-fsck#_fsck_messages)FSCK MESSAGES
The following lists the types of errors `git` `fsck` detects and what each error means, with their default severity. The severity of the error, other than those that are marked as "(FATAL)", can be tweaked by setting the corresponding `fsck.`_< msg-id>_ configuration variable. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badDate)`badDate` 
    
(ERROR) Invalid date format in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badDateOverflow)`badDateOverflow` 
    
(ERROR) Invalid date value in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badEmail)`badEmail` 
    
(ERROR) Invalid email format in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badFilemode)`badFilemode` 
    
(INFO) A tree contains a bad filemode entry. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badGpgsig)`badGpgsig` 
    
(ERROR) A tag contains a bad (truncated) signature (e.g., `gpgsig`) header. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badHeadTarget)`badHeadTarget` 
    
(ERROR) The `HEAD` ref is a symref that does not refer to a branch. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badHeaderContinuation)`badHeaderContinuation` 
    
(ERROR) A continuation header (such as for `gpgsig`) is unexpectedly truncated. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badName)`badName` 
    
(ERROR) An author/committer name is empty. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badObjectSha1)`badObjectSha1` 
    
(ERROR) An object has a bad sha1. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badPackedRefEntry)`badPackedRefEntry` 
    
(ERROR) The "packed-refs" file contains an invalid entry. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badPackedRefHeader)`badPackedRefHeader` 
    
(ERROR) The "packed-refs" file contains an invalid header. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badParentSha1)`badParentSha1` 
    
(ERROR) A commit object has a bad parent sha1. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badRefContent)`badRefContent` 
    
(ERROR) A ref has bad content. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badRefFiletype)`badRefFiletype` 
    
(ERROR) A ref has a bad file type. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badRefName)`badRefName` 
    
(ERROR) A ref has an invalid format. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badRefOid)`badRefOid` 
    
(ERROR) A ref points to an invalid object ID. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badReferentName)`badReferentName` 
    
(ERROR) The referent name of a symref is invalid. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badReftableTableName)`badReftableTableName` 
    
(WARN) A reftable table has an invalid name. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badTagName)`badTagName` 
    
(INFO) A tag has an invalid format. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badTimezone)`badTimezone` 
    
(ERROR) Found an invalid time zone in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badTree)`badTree` 
    
(ERROR) A tree cannot be parsed. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badTreeSha1)`badTreeSha1` 
    
(ERROR) A tree has an invalid format. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-badType)`badType` 
    
(ERROR) Found an invalid object type. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-duplicateEntries)`duplicateEntries` 
    
(ERROR) A tree contains duplicate file entries. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-emptyName)`emptyName` 
    
(WARN) A path contains an empty name. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-emptyPackedRefsFile)`emptyPackedRefsFile` 
    
(INFO) "packed-refs" file is empty. Report to the git@vger.kernel.org mailing list if you see this error. As only very early versions of Git would create such an empty "packed_refs" file, we might tighten this rule in the future. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-extraHeaderEntry)`extraHeaderEntry` 
    
(IGNORE) Extra headers found after `tagger`. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-fullPathname)`fullPathname` 
    
(WARN) A path contains the full path starting with "/". 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitattributesBlob)`gitattributesBlob` 
    
(ERROR) A non-blob found at `.gitattributes`. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitattributesLarge)`gitattributesLarge` 
    
(ERROR) The `.gitattributes` blob is too large. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitattributesLineLength)`gitattributesLineLength` 
    
(ERROR) The `.gitattributes` blob contains too long lines. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitattributesMissing)`gitattributesMissing` 
    
(ERROR) Unable to read `.gitattributes` blob. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitattributesSymlink)`gitattributesSymlink` 
    
(INFO) `.gitattributes` is a symlink. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitignoreSymlink)`gitignoreSymlink` 
    
(INFO) `.gitignore` is a symlink. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesBlob)`gitmodulesBlob` 
    
(ERROR) A non-blob found at `.gitmodules`. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesLarge)`gitmodulesLarge` 
    
(ERROR) The `.gitmodules` file is too large to parse. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesMissing)`gitmodulesMissing` 
    
(ERROR) Unable to read `.gitmodules` blob. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesName)`gitmodulesName` 
    
(ERROR) A submodule name is invalid. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesParse)`gitmodulesParse` 
    
(INFO) Could not parse `.gitmodules` blob. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesPath)`gitmodulesPath` 
    
(ERROR) `.gitmodules` path is invalid. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesSymlink)`gitmodulesSymlink` 
    
(ERROR) `.gitmodules` is a symlink. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesUpdate)`gitmodulesUpdate` 
    
(ERROR) Found an invalid submodule update setting. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-gitmodulesUrl)`gitmodulesUrl` 
    
(ERROR) Found an invalid submodule url. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-hasDot)`hasDot` 
    
(WARN) A tree contains an entry named `.`. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-hasDotdot)`hasDotdot` 
    
(WARN) A tree contains an entry named `..`. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-hasDotgit)`hasDotgit` 
    
(WARN) A tree contains an entry named `.git`. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-largePathname)`largePathname` 
    
(WARN) A tree contains an entry with a very long path name. If the value of `fsck.largePathname` contains a colon, that value is used as the maximum allowable length (e.g., "warn:10" would complain about any path component of 11 or more bytes). The default value is 4096. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-mailmapSymlink)`mailmapSymlink` 
    
(INFO) `.mailmap` is a symlink. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingAuthor)`missingAuthor` 
    
(ERROR) Author is missing. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingCommitter)`missingCommitter` 
    
(ERROR) Committer is missing. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingEmail)`missingEmail` 
    
(ERROR) Email is missing in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingNameBeforeEmail)`missingNameBeforeEmail` 
    
(ERROR) Missing name before an email in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingObject)`missingObject` 
    
(ERROR) Missing `object` line in tag object. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingSpaceBeforeDate)`missingSpaceBeforeDate` 
    
(ERROR) Missing space before date in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingSpaceBeforeEmail)`missingSpaceBeforeEmail` 
    
(ERROR) Missing space before the email in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingTag)`missingTag` 
    
(ERROR) Unexpected end after `type` line in a tag object. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingTagEntry)`missingTagEntry` 
    
(ERROR) Missing `tag` line in a tag object. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingTaggerEntry)`missingTaggerEntry` 
    
(INFO) Missing `tagger` line in a tag object. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingTree)`missingTree` 
    
(ERROR) Missing `tree` line in a commit object. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingType)`missingType` 
    
(ERROR) Invalid type value on the `type` line in a tag object. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-missingTypeEntry)`missingTypeEntry` 
    
(ERROR) Missing `type` line in a tag object. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-multipleAuthors)`multipleAuthors` 
    
(ERROR) Multiple author lines found in a commit. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-nulInCommit)`nulInCommit` 
    
(WARN) Found a NUL byte in the commit object body. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-nulInHeader)`nulInHeader` 
    
(FATAL) NUL byte exists in the object header. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-nullSha1)`nullSha1` 
    
(WARN) Tree contains entries pointing to a null sha1. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-packedRefEntryNotTerminated)`packedRefEntryNotTerminated` 
    
(ERROR) The "packed-refs" file contains an entry that is not terminated by a newline. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-packedRefUnsorted)`packedRefUnsorted` 
    
(ERROR) The "packed-refs" file is not sorted. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-refMissingNewline)`refMissingNewline` 
    
(INFO) A loose ref that does not end with newline(LF). As valid implementations of Git never created such a loose ref file, it may become an error in the future. Report to the git@vger.kernel.org mailing list if you see this error, as we need to know what tools created such a file. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-symlinkRef)`symlinkRef` 
    
(INFO) A symbolic link is used as a symref. Report to the git@vger.kernel.org mailing list if you see this error, as we are assessing the feasibility of dropping the support to drop creating symbolic links as symrefs. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-symrefTargetIsNotARef)`symrefTargetIsNotARef` 
    
(INFO) The target of a symbolic reference points neither to a root reference nor to a reference starting with "refs/". Although we allow create a symref pointing to the referent which is outside the "ref" by using `git` `symbolic-ref`, we may tighten the rule in the future. Report to the git@vger.kernel.org mailing list if you see this error, as we need to know what tools created such a file. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-trailingRefContent)`trailingRefContent` 
    
(INFO) A loose ref has trailing content. As valid implementations of Git never created such a loose ref file, it may become an error in the future. Report to the git@vger.kernel.org mailing list if you see this error, as we need to know what tools created such a file. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-treeNotSorted)`treeNotSorted` 
    
(ERROR) A tree is not properly sorted. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-unknownType)`unknownType` 
    
(ERROR) Found an unknown object type. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-unterminatedHeader)`unterminatedHeader` 
    
(FATAL) Missing end-of-line in the object header. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-zeroPaddedDate)`zeroPaddedDate` 
    
(ERROR) Found a zero padded date in an author/committer line. 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-zeroPaddedFilemode)`zeroPaddedFilemode` 
    
(WARN) Found a zero padded filemode in a tree.
##  [](https://git-scm.com/docs/git-fsck#_environment_variables)Environment Variables 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-GITOBJECTDIRECTORY)GIT_OBJECT_DIRECTORY 
    
used to specify the object database root (usually $GIT_DIR/objects) 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-GITINDEXFILE)GIT_INDEX_FILE 
    
used to specify the index file of the index 

[](https://git-scm.com/docs/git-fsck#Documentation/git-fsck.txt-GITALTERNATEOBJECTDIRECTORIES)GIT_ALTERNATE_OBJECT_DIRECTORIES 
    
used to specify additional object database roots (usually unset)
##  [](https://git-scm.com/docs/git-fsck#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### fsck
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
