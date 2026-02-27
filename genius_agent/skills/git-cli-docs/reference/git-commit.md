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
    * [NAME](https://git-scm.com/docs/git-commit#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-commit#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-commit#_description)
    * [OPTIONS](https://git-scm.com/docs/git-commit#_options)
    * [EXAMPLES](https://git-scm.com/docs/git-commit#_examples)
    * [COMMIT INFORMATION](https://git-scm.com/docs/git-commit#_commit_information)
    * [DATE FORMATS](https://git-scm.com/docs/git-commit#_date_formats)
    * [DISCUSSION](https://git-scm.com/docs/git-commit#_discussion)
    * [ENVIRONMENT AND CONFIGURATION VARIABLES](https://git-scm.com/docs/git-commit#_environment_and_configuration_variables)
    * [HOOKS](https://git-scm.com/docs/git-commit#_hooks)
    * [FILES](https://git-scm.com/docs/git-commit#_files)
    * [SEE ALSO](https://git-scm.com/docs/git-commit#_see_also)
    * [GIT](https://git-scm.com/docs/git-commit#_git)


[ English ▾](https://git-scm.com/docs/git-commit)
Localized versions of **git-commit** manual
  1. [English ](https://git-scm.com/docs/git-commit)
  2. [Español ](https://git-scm.com/docs/git-commit/es)
  3. [Français ](https://git-scm.com/docs/git-commit/fr)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-commit/pt_BR)
  5. [Русский ](https://git-scm.com/docs/git-commit/ru)
  6. [Svenska ](https://git-scm.com/docs/git-commit/sv)
  7. [українська мова ](https://git-scm.com/docs/git-commit/uk)
  8. [简体中文 ](https://git-scm.com/docs/git-commit/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-commit)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-commit) git-commit last updated in 2.53.0
Changes in the **git-commit** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-commit/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-commit/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-commit/2.51.0)
  5. 2.50.1 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-commit/2.50.0)
  7. 2.49.1 no changes
  8. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-commit/2.49.0)
  9. 2.46.2 → 2.48.2 no changes
  10. [2.46.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-13_ ](https://git-scm.com/docs/git-commit/2.46.1)
  11. 2.45.1 → 2.46.0 no changes
  12. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-commit/2.45.0)
  13. 2.43.2 → 2.44.4 no changes
  14. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-commit/2.43.1)
  15. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-commit/2.43.0)
  16. 2.38.1 → 2.42.4 no changes
  17. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-commit/2.38.0)
  18. 2.35.1 → 2.37.7 no changes
  19. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-commit/2.35.0)
  20. 2.34.1 → 2.34.8 no changes
  21. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-commit/2.34.0)
  22. 2.33.1 → 2.33.8 no changes
  23. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-commit/2.33.0)
  24. 2.32.1 → 2.32.7 no changes
  25. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-commit/2.32.0)
  26. 2.31.1 → 2.31.8 no changes
  27. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-commit/2.31.0)
  28. 2.30.1 → 2.30.9 no changes
  29. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-commit/2.30.0)
  30. 2.27.1 → 2.29.3 no changes
  31. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-commit/2.27.0)
  32. 2.25.2 → 2.26.3 no changes
  33. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-commit/2.25.1)
  34. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-commit/2.25.0)
  35. 2.24.1 → 2.24.4 no changes
  36. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-commit/2.24.0)
  37. 2.23.1 → 2.23.4 no changes
  38. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-commit/2.23.0)
  39. 2.21.1 → 2.22.5 no changes
  40. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-commit/2.21.0)
  41. 2.17.0 → 2.20.5 no changes
  42. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-commit/2.16.6)
  43. 2.14.6 → 2.15.4 no changes
  44. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-commit/2.13.7)
  45. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-commit/2.12.5)
  46. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-commit/2.11.4)
  47. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-commit/2.10.5)
  48. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-commit/2.9.5)
  49. 2.8.6 no changes
  50. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-commit/2.7.6)
  51. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-commit/2.6.7)
  52. 2.5.6 no changes
  53. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-commit/2.4.12)
  54. 2.3.10 no changes
  55. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-commit/2.2.3)
  56. 2.1.4 no changes
  57. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-commit/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-commit#_name)NAME
git-commit - Record changes to the repository
##  [](https://git-scm.com/docs/git-commit#_synopsis)SYNOPSIS
```
git commit [-a | --interactive | --patch] [-s] [-v] [-u[_<mode>_]] [--amend]
	   [--dry-run] _<commit>__ | --fixup [(amend|reword):"><commit>]
	   [-F _<file>_ | -m _<msg>_] [--reset-author] [--allow-empty]
	   [--allow-empty-message] [--no-verify] [-e] [--author=_<author>_]
	   [--date=_<date>_] [--cleanup=_<mode>_] [--[no-]status]
	   [-i | -o] [--pathspec-from-file=_<file>_ [--pathspec-file-nul]]
	   [(--trailer _<token>_[(=|:)_<value>_])…​] [-S[_<keyid>_]]
	   [--] [_<pathspec>_…​]
```

##  [](https://git-scm.com/docs/git-commit#_description)DESCRIPTION
Create a new commit containing the current contents of the index and the given log message describing the changes. The new commit is a direct child of HEAD, usually the tip of the current branch, and the branch is updated to point to it (unless no branch is associated with the working tree, in which case `HEAD` is "detached" as described in [git-checkout[1]](https://git-scm.com/docs/git-checkout)).
The content to be committed can be specified in several ways:
  1. by using [git-add[1]](https://git-scm.com/docs/git-add) to incrementally "add" changes to the index before using the `commit` command (Note: even modified files must be "added");
  2. by using [git-rm[1]](https://git-scm.com/docs/git-rm) to remove files from the working tree and the index, again before using the `commit` command;
  3. by listing files as arguments to the `commit` command (without `--interactive` or `--patch` switch), in which case the commit will ignore changes staged in the index, and instead record the current content of the listed files (which must already be known to Git);
  4. by using the `-a` switch with the `commit` command to automatically "add" changes from all known files (i.e. all files that are already listed in the index) and to automatically "rm" files in the index that have been removed from the working tree, and then perform the actual commit;
  5. by using the `--interactive` or `--patch` switches with the `commit` command to decide one by one which files or hunks should be part of the commit in addition to contents in the index, before finalizing the operation. See the “Interactive Mode” section of [git-add[1]](https://git-scm.com/docs/git-add) to learn how to operate these modes.


The `--dry-run` option can be used to obtain a summary of what is included by any of the above for the next commit by giving the same set of parameters (options and paths).
If you make a commit and then find a mistake immediately after that, you can recover from it with `git` `reset`.
##  [](https://git-scm.com/docs/git-commit#_options)OPTIONS 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--a)`-a` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---all)`--all` 
    
Automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--p)`-p` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---patch)`--patch` 
    
Use the interactive patch selection interface to choose which changes to commit. See [git-add[1]](https://git-scm.com/docs/git-add) for details. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context. Defaults to `diff.context` or 3 if the config option is unset. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---inter-hunk-contextn)`--inter-hunk-context=`_< n>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--Ccommit)`-C` _< commit>_ 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---reuse-messagecommit)`--reuse-message=`_< commit>_ 
    
Take an existing _< commit>_ object, and reuse the log message and the authorship information (including the timestamp) when creating the commit. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--ccommit)`-c` _< commit>_ 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---reedit-messagecommit)`--reedit-message=`_< commit>_ 
    
Like `-C`, but with `-c` the editor is invoked, so that the user can further edit the commit message. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---fixupamendrewordcommit)`--fixup=`[(`amend`|`reword`)`:`]_< commit>_ 
    
Create a new commit which "fixes up" _< commit>_ when applied with `git` `rebase` `--autosquash`. Plain `--fixup=`_< commit>_ creates a "fixup!" commit which changes the content of _< commit>_ but leaves its log message untouched. `--fixup=amend:`_< commit>_ is similar but creates an "amend!" commit which also replaces the log message of _< commit>_ with the log message of the "amend!" commit. `--fixup=reword:`_< commit>_ creates an "amend!" commit which replaces the log message of _< commit>_ with its own log message but makes no changes to the content of _< commit>_.
The commit created by plain `--fixup=`_< commit>_ has a title composed of "fixup!" followed by the title of _< commit>_, and is recognized specially by `git` `rebase` `--autosquash`. The `-m` option may be used to supplement the log message of the created commit, but the additional commentary will be thrown away once the "fixup!" commit is squashed into _< commit>_ by `git` `rebase` `--autosquash`.
The commit created by `--fixup=amend:`_< commit>_ is similar but its title is instead prefixed with "amend!". The log message of _< commit>_ is copied into the log message of the "amend!" commit and opened in an editor so it can be refined. When `git` `rebase` `--autosquash` squashes the "amend!" commit into _< commit>_, the log message of _< commit>_ is replaced by the refined log message from the "amend!" commit. It is an error for the "amend!" commit’s log message to be empty unless `--allow-empty-message` is specified.
`--fixup=reword:`_< commit>_ is shorthand for `--fixup=amend:`_< commit>_ `--only`. It creates an "amend!" commit with only a log message (ignoring any changes staged in the index). When squashed by `git` `rebase` `--autosquash`, it replaces the log message of _< commit>_ without making any other changes.
Neither "fixup!" nor "amend!" commits change authorship of _< commit>_ when applied by `git` `rebase` `--autosquash`. See [git-rebase[1]](https://git-scm.com/docs/git-rebase) for details. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---squashcommit)`--squash=`_< commit>_ 
    
Construct a commit message for use with `git` `rebase` `--autosquash`. The commit message title is taken from the specified commit with a prefix of "squash! ". Can be used with additional commit message options (`-m`/`-c`/`-C`/`-F`). See [git-rebase[1]](https://git-scm.com/docs/git-rebase) for details. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---reset-author)`--reset-author` 
    
When used with `-C`/`-c`/`--amend` options, or when committing after a conflicting cherry-pick, declare that the authorship of the resulting commit now belongs to the committer. This also renews the author timestamp. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---short)`--short` 
    
When doing a dry-run, give the output in the short-format. See [git-status[1]](https://git-scm.com/docs/git-status) for details. Implies `--dry-run`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---branch)`--branch` 
    
Show the branch and tracking info even in short-format. See [git-status[1]](https://git-scm.com/docs/git-status) for details. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---porcelain)`--porcelain` 
    
When doing a dry-run, give the output in a porcelain-ready format. See [git-status[1]](https://git-scm.com/docs/git-status) for details. Implies `--dry-run`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---long)`--long` 
    
When doing a dry-run, give the output in the long-format. This is the default output of [git-status[1]](https://git-scm.com/docs/git-status). Implies `--dry-run`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--z)`-z` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---null)`--null` 
    
When showing `short` or `porcelain` [git-status[1]](https://git-scm.com/docs/git-status) output, print the filename verbatim and terminate the entries with _NUL_ , instead of _LF_. If no format is given, implies the `--porcelain` output format. Without the `-z` option, filenames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--Ffile)`-F` _< file>_ 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---filefile)`--file=`_< file>_ 
    
Take the commit message from _< file>_. Use _-_ to read the message from the standard input. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---authorauthor)`--author=`_< author>_ 
    
Override the commit author. Specify an explicit author using the standard _A U Thor <author@example.com>_ format. Otherwise _< author>_ is assumed to be a pattern and is used to search for an existing commit by that author (i.e. `git` `rev-list` `--all` `-i` `--author=`_< author>_); the commit author is then copied from the first such commit found. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---datedate)`--date=`_< date>_ 
    
Override the author date used in the commit. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--mmsg)`-m` _< msg>_ 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---messagemsg)`--message=`_< msg>_ 
    
Use _< msg>_ as the commit message. If multiple `-m` options are given, their values are concatenated as separate paragraphs.
The `-m` option is mutually exclusive with `-c`, `-C`, and `-F`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--tfile)`-t` _< file>_ 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---templatefile)`--template=`_< file>_ 
    
When editing the commit message, start the editor with the contents in _< file>_. The `commit.template` configuration variable is often used to give this option implicitly to the command. This mechanism can be used by projects that want to guide participants with some hints on what to write in the message in what order. If the user exits the editor without editing the message, the commit is aborted. This has no effect when a message is given by other means, e.g. with the `-m` or `-F` options. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--s)`-s` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff)`--signoff` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---no-signoff)`--no-signoff` 
    
Add a `Signed-off-by` trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you’re committing. For example, it may certify that the committer has the rights to submit the work under the project’s license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See <https://developercertificate.org> for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you’re contributing to understand how the signoffs are used in that project.
The `--no-signoff` option can be used to countermand an earlier `--signoff` option on the command line.
Git does not (and will not) have a configuration variable to enable the `--signoff` command line option by default; see the `commit.signoff` entry in [gitfaq[7]](https://git-scm.com/docs/gitfaq) for more details. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---trailertokenvalue)`--trailer` _< token>_[(`=`|`:`)_< value>_] 
    
Specify a (_< token>_, _< value>_) pair that should be applied as a trailer. (e.g. _git commit --trailer "Signed-off-by:C O Mitter \_ _< committer@example.com>" --trailer "Helped-by:C O Mitter \ _ _< committer@example.com>"_ will add the `Signed-off-by` trailer and the `Helped-by` trailer to the commit message.) The `trailer.*` configuration variables ([git-interpret-trailers[1]](https://git-scm.com/docs/git-interpret-trailers)) can be used to define if a duplicated trailer is omitted, where in the run of trailers each trailer would appear, and other details. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--n)`-n` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---verify)`--verify` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---no-verify)`--no-verify` 
    
Bypass the `pre-commit` and `commit-msg` hooks. See also [githooks[5]](https://git-scm.com/docs/githooks). 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---allow-empty)`--allow-empty` 
    
Usually recording a commit that has the exact same tree as its sole parent commit is a mistake, and the command prevents you from making such a commit. This option bypasses the safety, and is primarily for use by foreign SCM interface scripts. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---allow-empty-message)`--allow-empty-message` 
    
Create a commit with an empty commit message without using plumbing commands like [git-commit-tree[1]](https://git-scm.com/docs/git-commit-tree). Like `--allow-empty`, this command is primarily for use by foreign SCM interface scripts. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---cleanupmode)`--cleanup=`_< mode>_ 
    
Determine how the supplied commit message should be cleaned up before committing. The _< mode>_ can be `strip`, `whitespace`, `verbatim`, `scissors` or `default`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-strip)`strip` 
    
Strip leading and trailing empty lines, trailing whitespace, commentary and collapse consecutive empty lines. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-whitespace)`whitespace` 
    
Same as `strip` except #commentary is not removed. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-verbatim)`verbatim` 
    
Do not change the message at all. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-scissors)`scissors` 
    
Same as `whitespace` except that everything from (and including) the line found below is truncated, if the message is to be edited. "`#`" can be customized with `core.commentChar`.
```
# ------------------------ >8 ------------------------
```


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-default)`default` 
    
Same as `strip` if the message is to be edited. Otherwise `whitespace`.
The default can be changed by the `commit.cleanup` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--e)`-e` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---edit)`--edit` 
    
Let the user further edit the message taken from _< file>_ with `-F` _< file>_, command line with `-m` _< message>_, and from _< commit>_ with `-C` _< commit>_. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---no-edit)`--no-edit` 
    
Use the selected commit message without launching an editor. For example, `git` `commit` `--amend` `--no-edit` amends a commit without changing its commit message. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend)`--amend` 
    
Replace the tip of the current branch by creating a new commit. The recorded tree is prepared as usual (including the effect of the `-i` and `-o` options and explicit pathspec), and the message from the original commit is used as the starting point, instead of an empty message, when no other message is specified from the command line via options such as `-m`, `-F`, `-c`, etc. The new commit has the same parents and author as the current one (the `--reset-author` option can countermand this).
It is a rough equivalent for:
```
	$ git reset --soft HEAD^
	$ ... do something else to come up with the right tree ...
	$ git commit -c ORIG_HEAD
```

but can be used to amend a merge commit.
You should understand the implications of rewriting history if you amend a commit that has already been published. (See the "RECOVERING FROM UPSTREAM REBASE" section in [git-rebase[1]](https://git-scm.com/docs/git-rebase).) 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---no-post-rewrite)`--no-post-rewrite` 
    
Bypass the `post-rewrite` hook. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--i)`-i` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---include)`--include` 
    
Before making a commit out of staged contents so far, stage the contents of paths given on the command line as well. This is usually not what you want unless you are concluding a conflicted merge. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--o)`-o` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---only)`--only` 
    
Make a commit by taking the updated working tree contents of the paths specified on the command line, disregarding any contents that have been staged for other paths. This is the default mode of operation of `git` `commit` if any paths are given on the command line, in which case this option can be omitted. If this option is specified together with `--amend`, then no paths need to be specified, which can be used to amend the last commit without committing changes that have already been staged. If used together with `--allow-empty` paths are also not required, and an empty commit will be created. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---pathspec-from-filefile)`--pathspec-from-file=`_< file>_ 
    
Pass pathspec in _< file>_ instead of commandline args. If _< file>_ is exactly `-` then standard input is used. Pathspec elements are separated by _LF_ or _CR_ /_LF_. Pathspec elements can be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). See also `--pathspec-file-nul` and global `--literal-pathspecs`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---pathspec-file-nul)`--pathspec-file-nul` 
    
Only meaningful with `--pathspec-from-file`. Pathspec elements are separated with _NUL_ character and all other characters are taken literally (including newlines and quotes). 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--umode)`-u`[_< mode>_] 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---untracked-filesmode)`--untracked-files`[`=`_< mode>_] 
    
Show untracked files.
The _< mode>_ parameter is optional (defaults to `all`), and is used to specify the handling of untracked files; when `-u` is not used, the default is `normal`, i.e. show untracked files and directories.
The possible options are: 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-no)`no` 
    
Show no untracked files 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-normal)`normal` 
    
Shows untracked files and directories 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-all)`all` 
    
Also shows individual files in untracked directories.
All usual spellings for Boolean value `true` are taken as `normal` and `false` as `no`. The default can be changed using the `status.showUntrackedFiles` configuration variable documented in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--v)`-v` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---verbose)`--verbose` 
    
Show unified diff between the `HEAD` commit and what would be committed at the bottom of the commit message template to help the user describe the commit by reminding what changes the commit has. Note that this diff output doesn’t have its lines prefixed with `#`. This diff will not be a part of the commit message. See the `commit.verbose` configuration variable in [git-config[1]](https://git-scm.com/docs/git-config).
If specified twice, show in addition the unified diff between what would be committed and the worktree files, i.e. the unstaged changes to tracked files. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--q)`-q` 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---quiet)`--quiet` 
    
Suppress commit summary message. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---dry-run)`--dry-run` 
    
Do not create a commit, but show a list of paths that are to be committed, paths with local changes that will be left uncommitted and paths that are untracked. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---status)`--status` 
    
Include the output of [git-status[1]](https://git-scm.com/docs/git-status) in the commit message template when using an editor to prepare the commit message. Defaults to on, but can be used to override configuration variable `commit.status`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---no-status)`--no-status` 
    
Do not include the output of [git-status[1]](https://git-scm.com/docs/git-status) in the commit message template when using an editor to prepare the default commit message. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--Skey-id)`-S`[_< key-id>_] 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---gpg-signkey-id)`--gpg-sign`[`=`_< key-id>_] 


[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---no-gpg-sign)`--no-gpg-sign` 
    
GPG-sign commits. The _< key-id>_ is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---)`--` 
    
Do not interpret any more arguments as options. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-pathspec)_< pathspec>_... 
    
When _< pathspec>_ is given on the command line, commit the contents of the files that match the pathspec without recording the changes already added to the index. The contents of these files are also staged for the next commit on top of what have been staged before.
For more details, see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary).
##  [](https://git-scm.com/docs/git-commit#_examples)EXAMPLES
When recording your own work, the contents of modified files in your working tree are temporarily stored to a staging area called the "index" with `git` `add`. A file can be reverted back, only in the index but not in the working tree, to that of the last commit with `git` `restore` `--staged` _< file>_, which effectively reverts `git` `add` and prevents the changes to this file from participating in the next commit. After building the state to be committed incrementally with these commands, `git` `commit` (without any pathname parameter) is used to record what has been staged so far. This is the most basic form of the command. An example:
```
$ edit hello.c
$ git rm goodbye.c
$ git add hello.c
$ git commit
```

Instead of staging files after each individual change, you can tell `git` `commit` to notice the changes to the files whose contents are tracked in your working tree and do corresponding `git` `add` and `git` `rm` for you. That is, this example does the same as the earlier example if there is no other change in your working tree:
```
$ edit hello.c
$ rm goodbye.c
$ git commit -a
```

The command `git` `commit` `-a` first looks at your working tree, notices that you have modified `hello.c` and removed `goodbye.c`, and performs necessary `git` `add` and `git` `rm` for you.
After staging changes to many files, you can alter the order the changes are recorded in, by giving pathnames to `git` `commit`. When pathnames are given, the command makes a commit that only records the changes made to the named paths:
```
$ edit hello.c hello.h
$ git add hello.c hello.h
$ edit Makefile
$ git commit Makefile
```

This makes a commit that records the modification to `Makefile`. The changes staged for `hello.c` and `hello.h` are not included in the resulting commit. However, their changes are not lost — they are still staged and merely held back. After the above sequence, if you do:
```
$ git commit
```

this second commit would record the changes to `hello.c` and `hello.h` as expected.
After a merge (initiated by `git` `merge` or `git` `pull`) stops because of conflicts, cleanly merged paths are already staged to be committed for you, and paths that conflicted are left in unmerged state. You would have to first check which paths are conflicting with `git` `status` and after fixing them manually in your working tree, you would stage the result as usual with `git` `add`:
```
$ git status | grep unmerged
unmerged: hello.c
$ edit hello.c
$ git add hello.c
```

After resolving conflicts and staging the result, `git` `ls-files` `-u` would stop mentioning the conflicted path. When you are done, run `git` `commit` to finally record the merge:
```
$ git commit
```

As with the case to record your own changes, you can use `-a` option to save typing. One difference is that during a merge resolution, you cannot use `git` `commit` with pathnames to alter the order the changes are committed, because the merge should be recorded as a single commit. In fact, the command refuses to run when given pathnames (but see `-i` option).
##  [](https://git-scm.com/docs/git-commit#_commit_information)COMMIT INFORMATION
Author and committer information is taken from the following environment variables, if set:
  * `GIT_AUTHOR_NAME`
  * `GIT_AUTHOR_EMAIL`
  * `GIT_AUTHOR_DATE`
  * `GIT_COMMITTER_NAME`
  * `GIT_COMMITTER_EMAIL`
  * `GIT_COMMITTER_DATE`


(nb "<", ">" and "\n"s are stripped)
The author and committer names are by convention some form of a personal name (that is, the name by which other humans refer to you), although Git does not enforce or require any particular form. Arbitrary Unicode may be used, subject to the constraints listed above. This name has no effect on authentication; for that, see the `credential.username` variable in [git-config[1]](https://git-scm.com/docs/git-config).
In case (some of) these environment variables are not set, the information is taken from the configuration items `user.name` and `user.email`, or, if not present, the environment variable `EMAIL`, or, if that is not set, system user name and the hostname used for outgoing mail (taken from `/etc/mailname` and falling back to the fully qualified hostname when that file does not exist).
The `author.name` and `committer.name` and their corresponding email options override `user.name` and `user.email` if set and are overridden themselves by the environment variables.
The typical usage is to set just the `user.name` and `user.email` variables; the other options are provided for more complex use cases.
##  [](https://git-scm.com/docs/git-commit#_date_formats)DATE FORMATS
The `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables support the following date formats: 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-Gitinternalformat)Git internal format 
    
It is _< unix-timestamp>_ _< time-zone-offset>_, where _< unix-timestamp>_ is the number of seconds since the UNIX epoch. _< time-zone-offset>_ is a positive or negative offset from UTC. For example CET (which is 1 hour ahead of UTC) is `+0100`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-RFC2822)RFC 2822 
    
The standard date format as described by RFC 2822, for example `Thu,` `07` `Apr` `2005` `22:13:13` `+0200`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-ISO8601)ISO 8601 
    
Time and date specified by the ISO 8601 standard, for example `2005-04-07T22:13:13`. The parser accepts a space instead of the `T` character as well. Fractional parts of a second will be ignored, for example `2005-04-07T22:13:13.019` will be treated as `2005-04-07T22:13:13`.
Note |  In addition, the date part is accepted in the following formats: `YYYY.MM.DD`, `MM/DD/YYYY` and `DD.MM.YYYY`.   
---|---  
In addition to recognizing all date formats above, the `--date` option will also try to make sense of other, more human-centric date formats, such as relative dates like "yesterday" or "last Friday at noon".
##  [](https://git-scm.com/docs/git-commit#_discussion)DISCUSSION
Though not required, it’s a good idea to begin the commit message with a single short (no more than 50 characters) line summarizing the change, followed by a blank line and then a more thorough description. The text up to the first blank line in a commit message is treated as the commit title, and that title is used throughout Git. For example, [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) turns a commit into email, and it uses the title on the Subject line and the rest of the commit in the body.
Git is to some extent character encoding agnostic.
  * The contents of the blob objects are uninterpreted sequences of bytes. There is no encoding translation at the core level.
  * Path names are encoded in UTF-8 normalization form C. This applies to tree objects, the index file, ref names, as well as path names in command line arguments, environment variables and config files (`.git/config` (see [git-config[1]](https://git-scm.com/docs/git-config)), [gitignore[5]](https://git-scm.com/docs/gitignore), [gitattributes[5]](https://git-scm.com/docs/gitattributes) and [gitmodules[5]](https://git-scm.com/docs/gitmodules)).
Note that Git at the core level treats path names simply as sequences of non-NUL bytes, there are no path name encoding conversions (except on Mac and Windows). Therefore, using non-ASCII path names will mostly work even on platforms and file systems that use legacy extended ASCII encodings. However, repositories created on such systems will not work properly on UTF-8-based systems (e.g. Linux, Mac, Windows) and vice versa. Additionally, many Git-based tools simply assume path names to be UTF-8 and will fail to display other encodings correctly.
  * Commit log messages are typically encoded in UTF-8, but other extended ASCII encodings are also supported. This includes ISO-8859-x, CP125x and many others, but _not_ UTF-16/32, EBCDIC and CJK multi-byte encodings (GBK, Shift-JIS, Big5, EUC-x, CP9xx etc.).


Although we encourage that the commit log messages are encoded in UTF-8, both the core and Git Porcelain are designed not to force UTF-8 on projects. If all participants of a particular project find it more convenient to use legacy encodings, Git does not forbid it. However, there are a few things to keep in mind.
  1. `git` `commit` and `git` `commit-tree` issue a warning if the commit log message given to it does not look like a valid UTF-8 string, unless you explicitly say your project uses a legacy encoding. The way to say this is to have `i18n.commitEncoding` in `.git/config` file, like this:
```
[i18n]
	commitEncoding = ISO-8859-1
```

Commit objects created with the above setting record the value of `i18n.commitEncoding` in their `encoding` header. This is to help other people who look at them later. Lack of this header implies that the commit log message is encoded in UTF-8.
  2. `git` `log`, `git` `show`, `git` `blame` and friends look at the `encoding` header of a commit object, and try to re-code the log message into UTF-8 unless otherwise specified. You can specify the desired output encoding with `i18n.logOutputEncoding` in `.git/config` file, like this:
```
[i18n]
	logOutputEncoding = ISO-8859-1
```

If you do not have this configuration variable, the value of `i18n.commitEncoding` is used instead.


Note that we deliberately chose not to re-code the commit log message when a commit is made to force UTF-8 at the commit object level, because re-coding to UTF-8 is not necessarily a reversible operation.
##  [](https://git-scm.com/docs/git-commit#_environment_and_configuration_variables)ENVIRONMENT AND CONFIGURATION VARIABLES
The editor used to edit the commit log message will be chosen from the `GIT_EDITOR` environment variable, the `core.editor` configuration variable, the `VISUAL` environment variable, or the `EDITOR` environment variable (in that order). See [git-var[1]](https://git-scm.com/docs/git-var) for details.
Everything above this line in this section isn’t included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content that follows is the same as what’s found there: 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-commitcleanup)`commit.cleanup` 
    
This setting overrides the default of the `--cleanup` option in `git` `commit`. Changing the default can be useful when you always want to keep lines that begin with the comment character (`core.commentChar`, default `#`) in your log message, in which case you would do `git` `config` `commit.cleanup` `whitespace` (note that you will have to remove the help lines that begin with the comment character in the commit log template yourself, if you do this). 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-commitgpgSign)`commit.gpgSign` 
    
A boolean to specify whether all commits should be GPG signed. Use of this option when doing operations such as rebase can result in a large number of commits being signed. It may be convenient to use an agent to avoid typing your GPG passphrase several times. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-commitstatus)`commit.status` 
    
A boolean to enable/disable inclusion of status information in the commit message template when using an editor to prepare the commit message. Defaults to `true`. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-committemplate)`commit.template` 
    
Specify the pathname of a file to use as the template for new commit messages. 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-commitverbose)`commit.verbose` 
    
A boolean or int to specify the level of verbosity with `git` `commit`. 
##  [](https://git-scm.com/docs/git-commit#_hooks)HOOKS
This command can run `commit-msg`, `prepare-commit-msg`, `pre-commit`, `post-commit` and `post-rewrite` hooks. See [githooks[5]](https://git-scm.com/docs/githooks) for more information.
##  [](https://git-scm.com/docs/git-commit#_files)FILES 

[](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt-GITDIRCOMMITEDITMSG)`$GIT_DIR/COMMIT_EDITMSG` 
    
This file contains the commit message of a commit in progress. If `git` `commit` exits due to an error before creating a commit, any commit message that has been provided by the user (e.g., in an editor session) will be available in this file, but will be overwritten by the next invocation of `git` `commit`.
##  [](https://git-scm.com/docs/git-commit#_see_also)SEE ALSO
[git-add[1]](https://git-scm.com/docs/git-add), [git-rm[1]](https://git-scm.com/docs/git-rm), [git-mv[1]](https://git-scm.com/docs/git-mv), [git-merge[1]](https://git-scm.com/docs/git-merge), [git-commit-tree[1]](https://git-scm.com/docs/git-commit-tree)
##  [](https://git-scm.com/docs/git-commit#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### commit
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
