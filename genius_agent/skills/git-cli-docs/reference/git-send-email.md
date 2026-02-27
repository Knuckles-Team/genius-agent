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
    * [NAME](https://git-scm.com/docs/git-send-email#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-send-email#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-send-email#_description)
    * [OPTIONS](https://git-scm.com/docs/git-send-email#_options)
    * [CONFIGURATION](https://git-scm.com/docs/git-send-email#_configuration)
    * [EXAMPLES OF SMTP SERVERS](https://git-scm.com/docs/git-send-email#_examples_of_smtp_servers)
    * [SENDING PATCHES](https://git-scm.com/docs/git-send-email#_sending_patches)
    * [SEE ALSO](https://git-scm.com/docs/git-send-email#_see_also)
    * [GIT](https://git-scm.com/docs/git-send-email#_git)


[ English ▾](https://git-scm.com/docs/git-send-email)
Localized versions of **git-send-email** manual
  1. [English ](https://git-scm.com/docs/git-send-email)
  2. [Français ](https://git-scm.com/docs/git-send-email/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-send-email/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-send-email/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-send-email/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-send-email)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-send-email) git-send-email last updated in 2.53.0
Changes in the **git-send-email** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-send-email/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-send-email/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-send-email/2.51.1)
  5. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-send-email/2.51.0)
  6. 2.50.1 no changes
  7. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-send-email/2.50.0)
  8. 2.47.1 → 2.49.1 no changes
  9. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git-send-email/2.47.0)
  10. 2.45.1 → 2.46.4 no changes
  11. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-send-email/2.45.0)
  12. 2.44.1 → 2.44.4 no changes
  13. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-send-email/2.44.0)
  14. 2.43.2 → 2.43.7 no changes
  15. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-send-email/2.43.1)
  16. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-send-email/2.43.0)
  17. 2.41.1 → 2.42.4 no changes
  18. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-send-email/2.41.0)
  19. 2.39.1 → 2.40.4 no changes
  20. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-send-email/2.39.0)
  21. 2.38.1 → 2.38.5 no changes
  22. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-send-email/2.38.0)
  23. 2.35.1 → 2.37.7 no changes
  24. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-send-email/2.35.0)
  25. 2.33.1 → 2.34.8 no changes
  26. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-send-email/2.33.0)
  27. 2.30.2 → 2.32.7 no changes
  28. [2.30.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-02-08_ ](https://git-scm.com/docs/git-send-email/2.30.1)
  29. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-send-email/2.30.0)
  30. 2.24.1 → 2.29.3 no changes
  31. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-send-email/2.24.0)
  32. 2.23.1 → 2.23.4 no changes
  33. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-send-email/2.23.0)
  34. 2.22.2 → 2.22.5 no changes
  35. [2.22.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-11_ ](https://git-scm.com/docs/git-send-email/2.22.1)
  36. 2.21.1 → 2.22.0 no changes
  37. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-send-email/2.21.0)
  38. 2.20.1 → 2.20.5 no changes
  39. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-send-email/2.20.0)
  40. 2.19.1 → 2.19.6 no changes
  41. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-send-email/2.19.0)
  42. 2.18.1 → 2.18.5 no changes
  43. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-send-email/2.18.0)
  44. 2.17.1 → 2.17.6 no changes
  45. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-send-email/2.17.0)
  46. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-send-email/2.16.6)
  47. 2.15.4 no changes
  48. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-send-email/2.14.6)
  49. 2.13.7 no changes
  50. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-send-email/2.12.5)
  51. 2.10.5 → 2.11.4 no changes
  52. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-send-email/2.9.5)
  53. 2.8.6 no changes
  54. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-send-email/2.7.6)
  55. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-send-email/2.6.7)
  56. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-send-email/2.5.6)
  57. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-send-email/2.4.12)
  58. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-send-email/2.3.10)
  59. 2.2.3 no changes
  60. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-send-email/2.1.4)
  61. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-send-email/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-send-email#_name)NAME
git-send-email - Send a collection of patches as emails
##  [](https://git-scm.com/docs/git-send-email#_synopsis)SYNOPSIS
```
_git send-email_ [<options>] (<file>|<directory>)…​
_git send-email_ [<options>] <format-patch-options>
_git send-email_ --dump-aliases
_git send-email_ --translate-aliases
```

##  [](https://git-scm.com/docs/git-send-email#_description)DESCRIPTION
Takes the patches given on the command line and emails them out. Patches can be specified as files, directories (which will send all files in the directory), or directly as a revision list. In the last case, any format accepted by [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) can be passed to `git` `send-email`, as well as options understood by [git-format-patch[1]](https://git-scm.com/docs/git-format-patch).
The header of the email is configurable via command-line options. If not specified on the command line, the user will be prompted with a ReadLine enabled interface to provide the necessary information.
There are two formats accepted for patch files:
  1. mbox format files
This is what [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) generates. Most headers and MIME formatting are ignored.
  2. The original format used by Greg Kroah-Hartman’s `send_lots_of_email.pl` script
This format expects the first line of the file to contain the `Cc:` value and the `Subject:` of the message as the second line.


##  [](https://git-scm.com/docs/git-send-email#_options)OPTIONS
###  [](https://git-scm.com/docs/git-send-email#_composing)Composing 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---annotate)--annotate 
    
Review and edit each patch you’re about to send. Default is the value of `sendemail.annotate`. See the CONFIGURATION section for `sendemail.multiEdit`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---bccaddress)--bcc=<address>,…​ 
    
Specify a `Bcc:` value for each email. Default is the value of `sendemail.bcc`.
This option may be specified multiple times. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---ccaddress)--cc=<address>,…​ 
    
Specify a starting `Cc:` value for each email. Default is the value of `sendemail.cc`.
This option may be specified multiple times. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---compose)--compose 
    
Invoke a text editor (see GIT_EDITOR in [git-var[1]](https://git-scm.com/docs/git-var)) to edit an introductory message for the patch series.
When `--compose` is used, `git` `send-email` will use the `From`, `To`, `Cc`, `Bcc`, `Subject`, `Reply-To`, and `In-Reply-To` headers specified in the message. If the body of the message (what you type after the headers and a blank line) only contains blank (or `Git:` prefixed) lines, the summary won’t be sent, but the headers mentioned above will be used unless they are removed.
Missing `From` or `In-Reply-To` headers will be prompted for.
See the CONFIGURATION section for `sendemail.multiEdit`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---fromaddress)--from=<address> 
    
Specify the sender of the emails. If not specified on the command line, the value of the `sendemail.from` configuration option is used. If neither the command-line option nor `sendemail.from` are set, then the user will be prompted for the value. The default for the prompt will be the value of `GIT_AUTHOR_IDENT`, or `GIT_COMMITTER_IDENT` if that is not set, as returned by `git` `var` `-l`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---reply-toaddress)--reply-to=<address> 
    
Specify the address where replies from recipients should go to. Use this if replies to messages should go to another address than what is specified with the `--from` parameter. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---in-reply-toidentifier)--in-reply-to=<identifier> 
    
Make the first mail (or all the mails with `--no-thread`) appear as a reply to the given Message-ID, which avoids breaking threads to provide a new patch series. The second and subsequent emails will be sent as replies according to the `--`[`no-`]`chain-reply-to` setting.
So for example when `--thread` and `--no-chain-reply-to` are specified, the second and subsequent patches will be replies to the first one like in the illustration below where [`PATCH` `v2` `0/3`] is in reply to [`PATCH` `0/2`]:
```
[PATCH 0/2] Here is what I did...
  [PATCH 1/2] Clean up and tests
  [PATCH 2/2] Implementation
  [PATCH v2 0/3] Here is a reroll
    [PATCH v2 1/3] Clean up
    [PATCH v2 2/3] New tests
    [PATCH v2 3/3] Implementation
```

Only necessary if `--compose` is also set. If `--compose` is not set, this will be prompted for. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---outlook-id-fix)--outlook-id-fix 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-outlook-id-fix)--no-outlook-id-fix 
    
Microsoft Outlook SMTP servers discard the Message-ID sent via email and assign a new random Message-ID, thus breaking threads.
With `--outlook-id-fix`, `git` `send-email` uses a mechanism specific to Outlook servers to learn the Message-ID the server assigned to fix the threading. Use it only when you know that the server reports the rewritten Message-ID the same way as Outlook servers do.
Without this option specified, the fix is done by default when talking to _smtp.office365.com_ or _smtp-mail.outlook.com_. Use `--no-outlook-id-fix` to disable even when talking to these two servers. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---subjectstring)--subject=<string> 
    
Specify the initial subject of the email thread. Only necessary if `--compose` is also set. If `--compose` is not set, this will be prompted for. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---toaddress)--to=<address>,…​ 
    
Specify the primary recipient of the emails generated. Generally, this will be the upstream maintainer of the project involved. Default is the value of the `sendemail.to` configuration value; if that is unspecified, and `--to-cmd` is not specified, this will be prompted for.
This option may be specified multiple times. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---8bit-encodingencoding)--8bit-encoding=<encoding> 
    
When encountering a non-ASCII message or subject that does not declare its encoding, add headers/quoting to indicate it is encoded in <encoding>. Default is the value of the `sendemail.assume8bitEncoding`; if that is unspecified, this will be prompted for if any non-ASCII files are encountered.
Note that no attempts whatsoever are made to validate the encoding. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---compose-encodingencoding)--compose-encoding=<encoding> 
    
Specify encoding of compose message. Default is the value of the `sendemail.composeEncoding`; if that is unspecified, UTF-8 is assumed. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---transfer-encoding7bit8bitquoted-printablebase64auto)--transfer-encoding=(7bit|8bit|quoted-printable|base64|auto) 
    
Specify the transfer encoding to be used to send the message over SMTP. `7bit` will fail upon encountering a non-ASCII message. `quoted-printable` can be useful when the repository contains files that contain carriage returns, but makes the raw patch email file (as saved from an MUA) much harder to inspect manually. `base64` is even more fool proof, but also even more opaque. `auto` will use `8bit` when possible, and `quoted-printable` otherwise.
Default is the value of the `sendemail.transferEncoding` configuration value; if that is unspecified, default to `auto`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---xmailer)--xmailer 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-xmailer)--no-xmailer 
    
Add (or prevent adding) the `X-Mailer:` header. By default, the header is added, but it can be turned off by setting the `sendemail.xmailer` configuration variable to `false`.
###  [](https://git-scm.com/docs/git-send-email#_sending)Sending 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---envelope-senderaddress)--envelope-sender=<address> 
    
Specify the envelope sender used to send the emails. This is useful if your default address is not the address that is subscribed to a list. In order to use the `From` address, set the value to `auto`. If you use the `sendmail` binary, you must have suitable privileges for the `-f` parameter. Default is the value of the `sendemail.envelopeSender` configuration variable; if that is unspecified, choosing the envelope sender is left to your MTA. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---sendmail-cmdcommand)--sendmail-cmd=<command> 
    
Specify a command to run to send the email. The command should be sendmail-like; specifically, it must support the `-i` option. The command will be executed in the shell if necessary. Default is the value of `sendemail.sendmailCmd`. If unspecified, and if `--smtp-server` is also unspecified, `git` `send-email` will search for `sendmail` in `/usr/sbin`, `/usr/lib` and `$PATH`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-encryptionencryption)--smtp-encryption=<encryption> 
    
Specify in what way encrypting begins for the SMTP connection. Valid values are `ssl` and `tls`. Any other value reverts to plain (unencrypted) SMTP, which defaults to port 25. Despite the names, both values will use the same newer version of TLS, but for historic reasons have these names. `ssl` refers to "implicit" encryption (sometimes called SMTPS), that uses port 465 by default. `tls` refers to "explicit" encryption (often known as STARTTLS), that uses port 25 by default. Other ports might be used by the SMTP server, which are not the default. Commonly found alternative port for `tls` and unencrypted is 587. You need to check your provider’s documentation or your server configuration to make sure for your own case. Default is the value of `sendemail.smtpEncryption`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-domainFQDN)--smtp-domain=<FQDN> 
    
Specify the Fully Qualified Domain Name (FQDN) used in the HELO/EHLO command to the SMTP server. Some servers require the FQDN to match your IP address. If not set, `git` `send-email` attempts to determine your FQDN automatically. Default is the value of `sendemail.smtpDomain`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-authmechanisms)--smtp-auth=<mechanisms> 
    
Whitespace-separated list of allowed SMTP-AUTH mechanisms. This setting forces using only the listed mechanisms. Example:
```
$ git send-email --smtp-auth="PLAIN LOGIN GSSAPI" ...
```

If at least one of the specified mechanisms matches the ones advertised by the SMTP server and if it is supported by the utilized SASL library, the mechanism is used for authentication. If neither `sendemail.smtpAuth` nor `--smtp-auth` is specified, all mechanisms supported by the SASL library can be used. The special value `none` maybe specified to completely disable authentication independently of `--smtp-user`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-passpassword)--smtp-pass[=<password>] 
    
Password for SMTP-AUTH. The argument is optional: If no argument is specified, then the empty string is used as the password. Default is the value of `sendemail.smtpPass`, however `--smtp-pass` always overrides this value.
Furthermore, passwords need not be specified in configuration files or on the command line. If a username has been specified (with `--smtp-user` or a `sendemail.smtpUser`), but no password has been specified (with `--smtp-pass` or `sendemail.smtpPass`), then a password is obtained using [git-credential[1]](https://git-scm.com/docs/git-credential). 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-smtp-auth)--no-smtp-auth 
    
Disable SMTP authentication. Short hand for `--smtp-auth=none`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-serverhost)--smtp-server=<host> 
    
Specify the outgoing SMTP server to use (e.g. `smtp.example.com` or a raw IP address). If unspecified, and if `--sendmail-cmd` is also unspecified, the default is to search for `sendmail` in `/usr/sbin`, `/usr/lib` and `$PATH` if such a program is available, falling back to `localhost` otherwise.
For backward compatibility, this option can also specify a full pathname of a sendmail-like program instead; the program must support the `-i` option. This method does not support passing arguments or using plain command names. For those use cases, consider using `--sendmail-cmd` instead. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-server-portport)--smtp-server-port=<port> 
    
Specify a port different from the default port (SMTP servers typically listen to smtp port 25, but may also listen to submission port 587, or the common SSL smtp port 465); symbolic port names (e.g. `submission` instead of 587) are also accepted. The port can also be set with the `sendemail.smtpServerPort` configuration variable. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-server-optionoption)--smtp-server-option=<option> 
    
Specify the outgoing SMTP server option to use. Default value can be specified by the `sendemail.smtpServerOption` configuration option.
The `--smtp-server-option` option must be repeated for each option you want to pass to the server. Likewise, different lines in the configuration files must be used for each option. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-ssl)--smtp-ssl 
    
Legacy alias for `--smtp-encryption` `ssl`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-ssl-cert-pathpath)--smtp-ssl-cert-path <path> 
    
Path to a store of trusted CA certificates for SMTP SSL/TLS certificate validation (either a directory that has been processed by `c_rehash`, or a single file containing one or more PEM format certificates concatenated together: see the description of the `-CAfile` _< file>_ and the `-CApath` _< dir>_ options of <https://docs.openssl.org/master/man1/openssl-verify/> [OpenSSL’s verify(1) manual page] for more information on these). Set it to an empty string to disable certificate verification. Defaults to the value of the `sendemail.smtpSSLCertPath` configuration variable, if set, or the backing SSL library’s compiled-in default otherwise (which should be the best choice on most platforms). 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-useruser)--smtp-user=<user> 
    
Username for SMTP-AUTH. Default is the value of `sendemail.smtpUser`; if a username is not specified (with `--smtp-user` or `sendemail.smtpUser`), then authentication is not attempted. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---smtp-debug01)--smtp-debug=(0|1) 
    
Enable (1) or disable (0) debug output. If enabled, SMTP commands and replies will be printed. Useful to debug TLS connection and authentication problems. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---imap-sent-folderfolder)--imap-sent-folder=<folder> 
    
Some email providers (e.g. iCloud) do not send a copy of the emails sent using SMTP to the `Sent` folder or similar in your mailbox. Use this option to use `git` `imap-send` to send a copy of the emails to the folder specified using this option. You can run `git` `imap-send` `--list` to get a list of valid folder names, including the correct name of the `Sent` folder in your mailbox. You can also use this option to send emails to a dedicated IMAP folder of your choice.
This feature requires setting up `git` `imap-send`. See [git-imap-send[1]](https://git-scm.com/docs/git-imap-send) for instructions. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---use-imap-only)--use-imap-only 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-use-imap-only)--no-use-imap-only 
    
If this is set, all emails will only be copied to the IMAP folder specified with `--imap-sent-folder` or `sendemail.imapSentFolder` and will not be sent to the recipients. Useful if you just want to create a draft of the emails and use another email client to send them. If disabled with `--no-use-imap-only`, the emails will be sent like usual. Disabled by default, but the `sendemail.useImapOnly` configuration variable can be used to enable it.
This feature requires setting up `git` `imap-send`. See [git-imap-send[1]](https://git-scm.com/docs/git-imap-send) for instructions. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---batch-sizenum)--batch-size=<num> 
    
Some email servers (e.g. _smtp.163.com_) limit the number of emails to be sent per session (connection) and this will lead to a failure when sending many messages. With this option, send-email will disconnect after sending _< num>_ messages and wait for a few seconds (see `--relogin-delay`) and reconnect, to work around such a limit. You may want to use some form of credential helper to avoid having to retype your password every time this happens. Defaults to the `sendemail.smtpBatchSize` configuration variable. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---relogin-delayint)--relogin-delay=<int> 
    
Waiting _< int>_ seconds before reconnecting to SMTP server. Used together with `--batch-size` option. Defaults to the `sendemail.smtpReloginDelay` configuration variable.
###  [](https://git-scm.com/docs/git-send-email#_automating)Automating 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-to)--no-to 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-cc)--no-cc 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-bcc)--no-bcc 
    
Clear any list of `To:`, `Cc:`, `Bcc:` addresses previously set via config. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-identity)--no-identity 
    
Clear the previously read value of `sendemail.identity` set via config, if any. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---to-cmdcommand)--to-cmd=<command> 
    
Specify a command to execute once per patch file which should generate patch file specific `To:` entries. Output of this command must be single email address per line. Default is the value of `sendemail.toCmd` configuration value. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---cc-cmdcommand)--cc-cmd=<command> 
    
Specify a command to execute once per patch file which should generate patch file specific `Cc:` entries. Output of this command must be single email address per line. Default is the value of `sendemail.ccCmd` configuration value. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---header-cmdcommand)--header-cmd=<command> 
    
Specify a command that is executed once per outgoing message and output RFC 2822 style header lines to be inserted into them. When the `sendemail.headerCmd` configuration variable is set, its value is always used. When `--header-cmd` is provided at the command line, its value takes precedence over the `sendemail.headerCmd` configuration variable. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-header-cmd)--no-header-cmd 
    
Disable any header command in use. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---chain-reply-to)--chain-reply-to 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-chain-reply-to)--no-chain-reply-to 
    
If this is set, each email will be sent as a reply to the previous email sent. If disabled with `--no-chain-reply-to`, all emails after the first will be sent as replies to the first email sent. When using this, it is recommended that the first file given be an overview of the entire patch series. Disabled by default, but the `sendemail.chainReplyTo` configuration variable can be used to enable it. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---identityidentity)--identity=<identity> 
    
A configuration identity. When given, causes values in the `sendemail.`_< identity>_ subsection to take precedence over values in the `sendemail` section. The default identity is the value of `sendemail.identity`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---signed-off-by-cc)--signed-off-by-cc 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-signed-off-by-cc)--no-signed-off-by-cc 
    
If this is set, add emails found in the `Signed-off-by` trailer or `Cc:` lines to the cc list. Default is the value of `sendemail.signedOffByCc` configuration value; if that is unspecified, default to `--signed-off-by-cc`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---cc-cover)--cc-cover 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-cc-cover)--no-cc-cover 
    
If this is set, emails found in `Cc:` headers in the first patch of the series (typically the cover letter) are added to the cc list for each email set. Default is the value of `sendemail.ccCover` configuration value; if that is unspecified, default to `--no-cc-cover`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---to-cover)--to-cover 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-to-cover)--no-to-cover 
    
If this is set, emails found in `To:` headers in the first patch of the series (typically the cover letter) are added to the to list for each email set. Default is the value of `sendemail.toCover` configuration value; if that is unspecified, default to `--no-to-cover`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---suppress-cccategory)--suppress-cc=<category> 
    
Specify an additional category of recipients to suppress the auto-cc of:
  * `author` will avoid including the patch author.
  * `self` will avoid including the sender.
  * `cc` will avoid including anyone mentioned in Cc lines in the patch header except for self (use `self` for that).
  * `bodycc` will avoid including anyone mentioned in Cc lines in the patch body (commit message) except for self (use `self` for that).
  * `sob` will avoid including anyone mentioned in the Signed-off-by trailers except for self (use `self` for that).
  * `misc-by` will avoid including anyone mentioned in Acked-by, Reviewed-by, Tested-by and other "-by" lines in the patch body, except Signed-off-by (use `sob` for that).
  * `cccmd` will avoid running the --cc-cmd.
  * `body` is equivalent to `sob` + `bodycc` + `misc-by`.
  * `all` will suppress all auto cc values.


Default is the value of `sendemail.suppressCc` configuration value; if that is unspecified, default to `self` if `--suppress-from` is specified, as well as `body` if `--no-signed-off-cc` is specified. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---suppress-from)--suppress-from 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-suppress-from)--no-suppress-from 
    
If this is set, do not add the `From:` address to the `Cc:` list. Default is the value of `sendemail.suppressFrom` configuration value; if that is unspecified, default to `--no-suppress-from`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---thread)--thread 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-thread)--no-thread 
    
If this is set, the `In-Reply-To` and `References` headers will be added to each email sent. Whether each mail refers to the previous email (`deep` threading per `git` `format-patch` wording) or to the first email (`shallow` threading) is governed by `--`[`no-`]`chain-reply-to`.
If disabled with `--no-thread`, those headers will not be added (unless specified with `--in-reply-to`). Default is the value of the `sendemail.thread` configuration value; if that is unspecified, default to `--thread`.
It is up to the user to ensure that no In-Reply-To header already exists when `git` `send-email` is asked to add it (especially note that `git` `format-patch` can be configured to do the threading itself). Failure to do so may not produce the expected result in the recipient’s MUA. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---mailmap)--mailmap 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-mailmap)--no-mailmap 
    
Use the mailmap file (see [gitmailmap[5]](https://git-scm.com/docs/gitmailmap)) to map all addresses to their canonical real name and email address. Additional mailmap data specific to `git` `send-email` may be provided using the `sendemail.mailmap.file` or `sendemail.mailmap.blob` configuration values. Defaults to `sendemail.mailmap`.
###  [](https://git-scm.com/docs/git-send-email#_administering)Administering 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---confirmmode)--confirm=<mode> 
    
Confirm just before sending:
  * `always` will always confirm before sending.
  * `never` will never confirm before sending.
  * `cc` will confirm before sending when send-email has automatically added addresses from the patch to the Cc list.
  * `compose` will confirm before sending the first message when using --compose.
  * `auto` is equivalent to `cc` + `compose`.


Default is the value of `sendemail.confirm` configuration value; if that is unspecified, default to `auto` unless any of the suppress options have been specified, in which case default to `compose`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---dry-run)--dry-run 
    
Do everything except actually send the emails. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---format-patch)--format-patch 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-format-patch)--no-format-patch 
    
When an argument may be understood either as a reference or as a file name, choose to understand it as a format-patch argument (`--format-patch`) or as a file name (`--no-format-patch`). By default, when such a conflict occurs, `git` `send-email` will fail. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---quiet)--quiet 
    
Make `git` `send-email` less verbose. One line per email should be all that is output. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---validate)--validate 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---no-validate)--no-validate 
    
Perform sanity checks on patches. Currently, validation means the following:
  * Invoke the sendemail-validate hook if present (see [githooks[5]](https://git-scm.com/docs/githooks)).
  * Warn of patches that contain lines longer than 998 characters unless a suitable transfer encoding (`auto`, `base64`, or `quoted-printable`) is used; this is due to SMTP limits as described by <https://www.ietf.org/rfc/rfc5322.txt>.


Default is the value of `sendemail.validate`; if this is not set, default to `--validate`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---force)--force 
    
Send emails even if safety checks would prevent it.
###  [](https://git-scm.com/docs/git-send-email#_information)Information 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---dump-aliases)--dump-aliases 
    
Instead of the normal operation, dump the shorthand alias names from the configured alias file(s), one per line in alphabetical order. Note that this only includes the alias name and not its expanded email addresses. See `sendemail.aliasesFile` for more information about aliases. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt---translate-aliases)--translate-aliases 
    
Instead of the normal operation, read from standard input and interpret each line as an email alias. Translate it according to the configured alias file(s). Output each translated name and email address to standard output, one per line. See `sendemail.aliasFile` for more information about aliases.
##  [](https://git-scm.com/docs/git-send-email#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailidentity)sendemail.identity 
    
A configuration identity. When given, causes values in the `sendemail.`_< identity>_ subsection to take precedence over values in the `sendemail` section. The default identity is the value of `sendemail.identity`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpEncryption)sendemail.smtpEncryption 
    
See [git-send-email[1]](https://git-scm.com/docs/git-send-email) for description. Note that this setting is not subject to the `identity` mechanism. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpSSLCertPath)sendemail.smtpSSLCertPath 
    
Path to ca-certificates (either a directory or a single file). Set it to an empty string to disable certificate verification. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailidentity-1)sendemail.<identity>.* 
    
Identity-specific versions of the `sendemail.*` parameters found below, taking precedence over those when this identity is selected, through either the command-line or `sendemail.identity`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailmultiEdit)sendemail.multiEdit 
    
If `true` (default), a single editor instance will be spawned to edit files you have to edit (patches when `--annotate` is used, and the summary when `--compose` is used). If `false`, files will be edited one after the other, spawning a new editor each time. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailconfirm)sendemail.confirm 
    
Sets the default for whether to confirm before sending. Must be one of `always`, `never`, `cc`, `compose`, or `auto`. See `--confirm` in the [git-send-email[1]](https://git-scm.com/docs/git-send-email) documentation for the meaning of these values. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailmailmap)sendemail.mailmap 
    
If `true`, makes [git-send-email[1]](https://git-scm.com/docs/git-send-email) assume `--mailmap`, otherwise assume `--no-mailmap`. `False` by default. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailmailmapfile)sendemail.mailmap.file 
    
The location of a [git-send-email[1]](https://git-scm.com/docs/git-send-email) specific augmenting mailmap file. The default mailmap and `mailmap.file` are loaded first. Thus, entries in this file take precedence over entries in the default mailmap locations. See [gitmailmap[5]](https://git-scm.com/docs/gitmailmap). 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailmailmapblob)sendemail.mailmap.blob 
    
Like `sendemail.mailmap.file`, but consider the value as a reference to a blob in the repository. Entries in `sendemail.mailmap.file` take precedence over entries here. See [gitmailmap[5]](https://git-scm.com/docs/gitmailmap). 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailaliasesFile)sendemail.aliasesFile 
    
To avoid typing long email addresses, point this to one or more email aliases files. You must also supply `sendemail.aliasFileType`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailaliasFileType)sendemail.aliasFileType 
    
Format of the file(s) specified in sendemail.aliasesFile. Must be one of `mutt`, `mailrc`, `pine`, `elm`, `gnus`, or `sendmail`.
What an alias file in each format looks like can be found in the documentation of the email program of the same name. The differences and limitations from the standard formats are described below: 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendmail)sendmail 
    
  * Quoted aliases and quoted addresses are not supported: lines that contain a `"` symbol are ignored.
  * Redirection to a file (`/path/name`) or pipe (|`command`) is not supported.
  * File inclusion (`:include:` `/path/name`) is not supported.
  * Warnings are printed on the standard error output for any explicitly unsupported constructs, and any other lines that are not recognized by the parser.



[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailannotate)sendemail.annotate 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailbcc)sendemail.bcc 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailcc)sendemail.cc 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailccCmd)sendemail.ccCmd 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailchainReplyTo)sendemail.chainReplyTo 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailenvelopeSender)sendemail.envelopeSender 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailfrom)sendemail.from 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailheaderCmd)sendemail.headerCmd 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsignedOffByCc)sendemail.signedOffByCc 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpPass)sendemail.smtpPass 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsuppressCc)sendemail.suppressCc 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsuppressFrom)sendemail.suppressFrom 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailto)sendemail.to 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailtoCmd)sendemail.toCmd 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpDomain)sendemail.smtpDomain 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpServer)sendemail.smtpServer 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpServerPort)sendemail.smtpServerPort 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpServerOption)sendemail.smtpServerOption 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpUser)sendemail.smtpUser 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailimapSentFolder)sendemail.imapSentFolder 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailuseImapOnly)sendemail.useImapOnly 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailthread)sendemail.thread 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailtransferEncoding)sendemail.transferEncoding 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailvalidate)sendemail.validate 


[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailxmailer)sendemail.xmailer 
    
These configuration variables all provide a default for [git-send-email[1]](https://git-scm.com/docs/git-send-email) command-line options. See its documentation for details. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailoutlookidfix)sendemail.outlookidfix 
    
If `true`, makes [git-send-email[1]](https://git-scm.com/docs/git-send-email) assume `--outlook-id-fix`, and if `false` assume `--no-outlook-id-fix`. If not specified, it will behave the same way as if `--outlook-id-fix` is not specified. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsignedOffCcdeprecated)sendemail.signedOffCc (deprecated) 
    
Deprecated alias for `sendemail.signedOffByCc`. 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpBatchSize)sendemail.smtpBatchSize 
    
Number of messages to be sent per connection, after that a relogin will happen. If the value is `0` or undefined, send all messages in one connection. See also the `--batch-size` option of [git-send-email[1]](https://git-scm.com/docs/git-send-email). 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailsmtpReloginDelay)sendemail.smtpReloginDelay 
    
Seconds to wait before reconnecting to the smtp server. See also the `--relogin-delay` option of [git-send-email[1]](https://git-scm.com/docs/git-send-email). 

[](https://git-scm.com/docs/git-send-email#Documentation/git-send-email.txt-sendemailforbidSendmailVariables)sendemail.forbidSendmailVariables 
    
To avoid common misconfiguration mistakes, [git-send-email[1]](https://git-scm.com/docs/git-send-email) will abort with a warning if any configuration options for `sendmail` exist. Set this variable to bypass the check.
##  [](https://git-scm.com/docs/git-send-email#_examples_of_smtp_servers)EXAMPLES OF SMTP SERVERS
###  [](https://git-scm.com/docs/git-send-email#_use_gmail_as_the_smtp_server)Use Gmail as the SMTP Server
To use `git` `send-email` to send your patches through the Gmail SMTP server, edit `~/.gitconfig` to specify your account settings:
```
[sendemail]
	smtpEncryption = ssl
	smtpServer = smtp.gmail.com
	smtpUser = yourname@gmail.com
	smtpServerPort = 465
```

Gmail does not allow using your regular password for `git` `send-email`. If you have multi-factor authentication set up on your Gmail account, you can generate an app-specific password for use with `git` `send-email`. Visit <https://security.google.com/settings/security/apppasswords> to create it.
Alternatively, instead of using an app-specific password, you can use OAuth2.0 authentication with Gmail. OAuth2.0 is more secure than app-specific passwords, and works regardless of whether you have multi-factor authentication set up. `OAUTHBEARER` and `XOAUTH2` are common mechanisms used for this type of authentication. Gmail supports both of them. As an example, if you want to use `OAUTHBEARER`, edit your `~/.gitconfig` file and add `smtpAuth` `=` `OAUTHBEARER` to your account settings:
```
[sendemail]
	smtpEncryption = ssl
	smtpServer = smtp.gmail.com
	smtpUser = yourname@gmail.com
	smtpServerPort = 465
	smtpAuth = OAUTHBEARER
```

Another alternative is using a tool developed by Google known as [sendgmail](https://github.com/google/gmail-oauth2-tools/tree/master/go/sendgmail) to send emails using `git` `send-email`.
###  [](https://git-scm.com/docs/git-send-email#_use_microsoft_outlook_as_the_smtp_server)Use Microsoft Outlook as the SMTP Server
Unlike Gmail, Microsoft Outlook no longer supports app-specific passwords. Therefore, OAuth2.0 authentication must be used for Outlook. Also, it only supports `XOAUTH2` authentication mechanism.
Edit `~/.gitconfig` to specify your account settings for Outlook and use its SMTP server with `git` `send-email`:
```
[sendemail]
	smtpEncryption = tls
	smtpServer = smtp.office365.com
	smtpUser = yourname@outlook.com
	smtpServerPort = 587
	smtpAuth = XOAUTH2
```

##  [](https://git-scm.com/docs/git-send-email#_sending_patches)SENDING PATCHES
Once your commits are ready to be sent to the mailing list, run the following commands:
```
$ git format-patch --cover-letter -M origin/master -o outgoing/
$ edit outgoing/0000-*
$ git send-email outgoing/*
```

The first time you run it, you will be prompted for your credentials. Enter the app-specific or your regular password as appropriate.
If you have a credential helper configured (see [git-credential[1]](https://git-scm.com/docs/git-credential)), the password will be saved in the credential store so you won’t have to type it the next time.
If you are using OAuth2.0 authentication, you need to use an access token in place of a password when prompted. Various OAuth2.0 token generators are available online. Community maintained credential helpers are also available:
  * [git-credential-gmail](https://github.com/AdityaGarg8/git-credential-email) (cross platform, dedicated helper for authenticating Gmail accounts)
  * [git-credential-outlook](https://github.com/AdityaGarg8/git-credential-email) (cross platform, dedicated helper for authenticating Microsoft Outlook accounts)
  * [git-credential-yahoo](https://github.com/AdityaGarg8/git-credential-email) (cross platform, dedicated helper for authenticating Yahoo accounts)
  * [git-credential-aol](https://github.com/AdityaGarg8/git-credential-email) (cross platform, dedicated helper for authenticating AOL accounts)


You can also see [gitcredentials[7]](https://git-scm.com/docs/gitcredentials) for more OAuth based authentication helpers.
Proton Mail does not provide an SMTP server to send emails. If you are a paid customer of Proton Mail, you can use [Proton Mail Bridge](https://proton.me/mail/bridge) officially provided by Proton Mail to create a local SMTP server for sending emails. For both free and paid users, community maintained projects like [git-protonmail](https://github.com/AdityaGarg8/git-credential-email) can be used.
Note: the following core Perl modules that may be installed with your distribution of Perl are required:
[MIME::Base64](https://metacpan.org/pod/MIME::Base64), [MIME::QuotedPrint](https://metacpan.org/pod/MIME::QuotedPrint), [Net::Domain](https://metacpan.org/pod/Net::Domain) and [Net::SMTP](https://metacpan.org/pod/Net::SMTP).
These additional Perl modules are also required:
[Authen::SASL](https://metacpan.org/pod/Authen::SASL) and [Mail::Address](https://metacpan.org/pod/Mail::Address).
###  [](https://git-scm.com/docs/git-send-email#_exploiting_the_sendmailcmd_option_of_git_send_email)Exploiting the `sendmailCmd` option of `git` `send-email`
Apart from sending emails via an SMTP server, `git` `send-email` can also send emails through any application that supports sendmail-like commands. You can read documentation of `--sendmail-cmd=`_< command>_ above for more information. This ability can be very useful if you want to use another application as an SMTP client for `git` `send-email`, or if your email provider uses proprietary APIs instead of SMTP to send emails.
As an example, lets see how to configure [msmtp](https://marlam.de/msmtp/), a popular SMTP client found in many Linux distributions. Edit `~/.gitconfig` to instruct `git-send-email` to use it for sending emails.
```
[sendemail]
	sendmailCmd = /usr/bin/msmtp # Change this to the path where msmtp is installed
```

Links of a few such community maintained helpers are:
  * [msmtp](https://marlam.de/msmtp/) (popular SMTP client with many features, available for Linux and macOS)
  * [git-protonmail](https://github.com/AdityaGarg8/git-credential-email) (cross platform client that can send emails using the ProtonMail API)
  * [git-msgraph](https://github.com/AdityaGarg8/git-credential-email) (cross platform client that can send emails using the Microsoft Graph API)


##  [](https://git-scm.com/docs/git-send-email#_see_also)SEE ALSO
[git-format-patch[1]](https://git-scm.com/docs/git-format-patch), [git-imap-send[1]](https://git-scm.com/docs/git-imap-send), mbox(5)
##  [](https://git-scm.com/docs/git-send-email#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### send-email
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
