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
    * [NAME](https://git-scm.com/docs/git-log#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-log#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-log#_description)
    * [OPTIONS](https://git-scm.com/docs/git-log#_options)
    * [PRETTY FORMATS](https://git-scm.com/docs/git-log#_pretty_formats)
    * [DIFF FORMATTING](https://git-scm.com/docs/git-log#_diff_formatting)
    * [Generating patch text with -p](https://git-scm.com/docs/git-log#generate_patch_text_with_p)
    * [Combined diff format](https://git-scm.com/docs/git-log#_combined_diff_format)
    * [EXAMPLES](https://git-scm.com/docs/git-log#_examples)
    * [DISCUSSION](https://git-scm.com/docs/git-log#_discussion)
    * [CONFIGURATION](https://git-scm.com/docs/git-log#_configuration)
    * [GIT](https://git-scm.com/docs/git-log#_git)


[ English ▾](https://git-scm.com/docs/git-log)
Localized versions of **git-log** manual
  1. [English ](https://git-scm.com/docs/git-log)
  2. [Français ](https://git-scm.com/docs/git-log/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-log/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-log/sv)
  5. [українська мова ](https://git-scm.com/docs/git-log/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-log/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-log)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-log) git-log last updated in 2.53.0
Changes in the **git-log** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-log/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-log/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-log/2.51.1)
  5. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-log/2.51.0)
  6. 2.50.1 no changes
  7. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-log/2.50.0)
  8. 2.49.1 no changes
  9. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-log/2.49.0)
  10. 2.48.1 → 2.48.2 no changes
  11. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-log/2.48.0)
  12. 2.46.1 → 2.47.3 no changes
  13. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-log/2.46.0)
  14. 2.45.4 no changes
  15. [2.45.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-log/2.45.3)
  16. 2.45.1 → 2.45.2 no changes
  17. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-log/2.45.0)
  18. 2.44.1 → 2.44.4 no changes
  19. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-log/2.44.0)
  20. 2.43.3 → 2.43.7 no changes
  21. [2.43.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-13_ ](https://git-scm.com/docs/git-log/2.43.2)
  22. 2.43.1 no changes
  23. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-log/2.43.0)
  24. 2.42.2 → 2.42.4 no changes
  25. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-log/2.42.1)
  26. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-log/2.42.0)
  27. 2.41.1 → 2.41.3 no changes
  28. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-log/2.41.0)
  29. 2.40.1 → 2.40.4 no changes
  30. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-log/2.40.0)
  31. 2.39.1 → 2.39.5 no changes
  32. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-log/2.39.0)
  33. 2.38.3 → 2.38.5 no changes
  34. [2.38.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-11_ ](https://git-scm.com/docs/git-log/2.38.2)
  35. 2.38.1 no changes
  36. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-log/2.38.0)
  37. 2.37.1 → 2.37.7 no changes
  38. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-log/2.37.0)
  39. 2.36.1 → 2.36.6 no changes
  40. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-log/2.36.0)
  41. 2.35.1 → 2.35.8 no changes
  42. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-log/2.35.0)
  43. 2.33.3 → 2.34.8 no changes
  44. [2.33.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-log/2.33.2)
  45. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git-log/2.33.1)
  46. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-log/2.33.0)
  47. 2.32.1 → 2.32.7 no changes
  48. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-log/2.32.0)
  49. 2.31.1 → 2.31.8 no changes
  50. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-log/2.31.0)
  51. 2.30.1 → 2.30.9 no changes
  52. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-log/2.30.0)
  53. 2.29.1 → 2.29.3 no changes
  54. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-log/2.29.0)
  55. 2.28.1 no changes
  56. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-log/2.28.0)
  57. 2.27.1 no changes
  58. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-log/2.27.0)
  59. 2.26.1 → 2.26.3 no changes
  60. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-log/2.26.0)
  61. 2.25.2 → 2.25.5 no changes
  62. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-log/2.25.1)
  63. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-log/2.25.0)
  64. 2.24.1 → 2.24.4 no changes
  65. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-log/2.24.0)
  66. 2.23.1 → 2.23.4 no changes
  67. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-log/2.23.0)
  68. 2.22.1 → 2.22.5 no changes
  69. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-log/2.22.0)
  70. 2.21.1 → 2.21.4 no changes
  71. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-log/2.21.0)
  72. 2.20.1 → 2.20.5 no changes
  73. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-log/2.20.0)
  74. 2.19.3 → 2.19.6 no changes
  75. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-log/2.19.2)
  76. 2.19.1 no changes
  77. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-log/2.19.0)
  78. 2.18.1 → 2.18.5 no changes
  79. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-log/2.18.0)
  80. 2.17.1 → 2.17.6 no changes
  81. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-log/2.17.0)
  82. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-log/2.16.6)
  83. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-log/2.15.4)
  84. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-log/2.14.6)
  85. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-log/2.13.7)
  86. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-log/2.12.5)
  87. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-log/2.11.4)
  88. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-log/2.10.5)
  89. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-log/2.9.5)
  90. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-log/2.8.6)
  91. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-log/2.7.6)
  92. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-log/2.6.7)
  93. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-log/2.5.6)
  94. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-log/2.4.12)
  95. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-log/2.3.10)
  96. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-log/2.2.3)
  97. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-log/2.1.4)
  98. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-log/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-log#_name)NAME
git-log - Show commit logs
##  [](https://git-scm.com/docs/git-log#_synopsis)SYNOPSIS
```
git log [_<options>_] [_<revision-range>_] [[--] _<path>_…​]
```

##  [](https://git-scm.com/docs/git-log#_description)DESCRIPTION
Shows the commit logs.
List commits that are reachable by following the `parent` links from the given commit(s), but exclude commits that are reachable from the one(s) given with a _^_ in front of them. The output is given in reverse chronological order by default.
You can think of this as a set operation. Commits reachable from any of the commits given on the command line form a set, and then commits reachable from any of the ones given with _^_ in front are subtracted from that set. The remaining commits are what comes out in the command’s output. Various other options and paths parameters can be used to further limit the result.
Thus, the following command:
```
$ git log foo bar ^baz
```

means "list all the commits which are reachable from _foo_ or _bar_ , but not from _baz_ ".
A special notation "_< commit1>_`..`_< commit2>_" can be used as a short-hand for "`^`_< commit1>_ _< commit2>_". For example, either of the following may be used interchangeably:
```
$ git log origin..HEAD
$ git log HEAD ^origin
```

Another special notation is "_< commit1>_`...`_< commit2>_" which is useful for merges. The resulting set of commits is the symmetric difference between the two operands. The following two commands are equivalent:
```
$ git log A B --not $(git merge-base --all A B)
$ git log A...B
```

The command takes options applicable to the [git-rev-list[1]](https://git-scm.com/docs/git-rev-list) command to control what is shown and how, and options applicable to the [git-diff[1]](https://git-scm.com/docs/git-diff) command to control how the changes each commit introduces are shown.
##  [](https://git-scm.com/docs/git-log#_options)OPTIONS 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---follow)`--follow` 
    
Continue listing the history of a file beyond renames (works only for a single file). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-decorate)`--no-decorate` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---decorateshortfullautono)`--decorate`[`=`(`short`|`full`|`auto`|`no`)] 
    
Print out the ref names of any commits that are shown. Possible values are:
```
`short`;; the ref name prefixes `refs/heads/`, `refs/tags/` and
	`refs/remotes/` are not printed.
`full`;; the full ref name (including prefix) is printed.
`auto`:: if the output is going to a terminal, the ref names
	are shown as if `short` were given, otherwise no ref names are
	shown.
```

The option `--decorate` is short-hand for `--decorate=short`. Default to configuration value of `log.decorate` if configured, otherwise, `auto`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---decorate-refspattern)`--decorate-refs=`_< pattern>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---decorate-refs-excludepattern)`--decorate-refs-exclude=`_< pattern>_ 
    
For each candidate reference, do not use it for decoration if it matches any of the _< pattern>_ parameters given to `--decorate-refs-exclude` or if it doesn’t match any of the _< pattern>_ parameters given to `--decorate-refs`. The `log.excludeDecoration` config option allows excluding refs from the decorations, but an explicit `--decorate-refs` pattern will override a match in `log.excludeDecoration`.
If none of these options or config settings are given, then references are used as decoration if they match `HEAD`, `refs/heads/`, `refs/remotes/`, `refs/stash/`, or `refs/tags/`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---clear-decorations)`--clear-decorations` 
    
When specified, this option clears all previous `--decorate-refs` or `--decorate-refs-exclude` options and relaxes the default decoration filter to include all references. This option is assumed if the config value `log.initialDecorationSet` is set to `all`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---source)`--source` 
    
Print out the ref name given on the command line by which each commit was reached. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---mailmap)`--mailmap` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-mailmap)`--no-mailmap` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---use-mailmap)`--use-mailmap` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-use-mailmap)`--no-use-mailmap` 
    
Use mailmap file to map author and committer names and email addresses to canonical real names and email addresses. See [git-shortlog[1]](https://git-scm.com/docs/git-shortlog). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---full-diff)`--full-diff` 
    
Without this flag, `git` `log` `-p` _< path>_... shows commits that touch the specified paths, and diffs about the same specified paths. With this, the full diff is shown for commits that touch the specified paths; this means that "_< path>_..." limits only commits, and doesn’t limit diff for those commits.
Note that this affects all diff-based output types, e.g. those produced by `--stat`, etc. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---log-size)`--log-size` 
    
Include a line `log` `size` _< number>_ in the output for each commit, where _< number>_ is the length of that commit’s message in bytes. Intended to speed up tools that read log messages from `git` `log` output by allowing them to allocate space in advance. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Lstartendfile)`-L`_< start>_`,`_< end>_`:`_< file>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Lfuncnamefile)`-L:`_< funcname>_`:`_< file>_ 
    
Trace the evolution of the line range given by _< start>_`,`_< end>_, or by the function name regex _< funcname>_, within the _< file>_. You may not give any pathspec limiters. This is currently limited to a walk starting from a single revision, i.e., you may only give zero or one positive revision arguments, and _< start>_ and _< end>_ (or _< funcname>_) must exist in the starting revision. You can specify this option more than once. Implies `--patch`. Patch output can be suppressed using `--no-patch`, but other diff formats (namely `--raw`, `--numstat`, `--shortstat`, `--dirstat`, `--summary`, `--name-only`, `--name-status`, `--check`) are not currently implemented.
_< start>_ and _< end>_ can take one of these forms:
  * _< number>_
If _< start>_ or _< end>_ is a number, it specifies an absolute line number (lines count from 1).
  * `/`_< regex>_`/`
This form will use the first line matching the given POSIX _< regex>_. If _< start>_ is a regex, it will search from the end of the previous `-L` range, if any, otherwise from the start of file. If _< start>_ is `^/`_< regex>_`/`, it will search from the start of file. If _< end>_ is a regex, it will search starting at the line given by _< start>_.
  * `+`_< offset>_ or `-`_< offset>_
This is only valid for _< end>_ and will specify a number of lines before or after the line given by _< start>_.


If `:`_< funcname>_ is given in place of _< start>_ and _< end>_, it is a regular expression that denotes the range from the first funcname line that matches _< funcname>_, up to the next funcname line. `:`_< funcname>_ searches from the end of the previous `-L` range, if any, otherwise from the start of file. `^:`_< funcname>_ searches from the start of file. The function names are determined in the same way as `git` `diff` works out patch hunk headers (see _Defining a custom hunk-header_ in [gitattributes[5]](https://git-scm.com/docs/gitattributes)). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-revision-range)_< revision-range>_ 
    
Show only commits in the specified revision range. When no _< revision-range>_ is specified, it defaults to `HEAD` (i.e. the whole history leading to the current commit). `origin..HEAD` specifies all the commits reachable from the current commit (i.e. `HEAD`), but not from `origin`. For a complete list of ways to spell _< revision-range>_, see the _Specifying Ranges_ section of [gitrevisions[7]](https://git-scm.com/docs/gitrevisions). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---path)[`--`] _< path>_... 
    
Show only commits that are enough to explain how the files that match the specified paths came to be. See _History Simplification_ below for details and other simplification modes.
Paths may need to be prefixed with `--` to separate them from options or the revision range, when confusion arises.
###  [](https://git-scm.com/docs/git-log#_commit_limiting)Commit Limiting
Besides specifying a range of commits that should be listed using the special notations explained in the description, additional commit limiting may be applied.
Using more options generally further limits the output (e.g. `--since=`_< date1>_ limits to commits newer than _< date1>_, and using it with `--grep=`_< pattern>_ further limits to commits whose log message has a line that matches _< pattern>_), unless otherwise noted.
Note that these are applied before commit ordering and formatting options, such as `--reverse`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--number)`-`_< number>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--nnumber)`-n` _< number>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---max-countnumber)`--max-count=`_< number>_ 
    
Limit the output to _< number>_ commits. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---skipnumber)`--skip=`_< number>_ 
    
Skip _< number>_ commits before starting to show the commit output. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---sincedate)`--since=`_< date>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---afterdate)`--after=`_< date>_ 
    
Show commits more recent than _< date>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---since-as-filterdate)`--since-as-filter=`_< date>_ 
    
Show all commits more recent than _< date>_. This visits all commits in the range, rather than stopping at the first commit which is older than _< date>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---untildate)`--until=`_< date>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---beforedate)`--before=`_< date>_ 
    
Show commits older than _< date>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---authorpattern)`--author=`_< pattern>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---committerpattern)`--committer=`_< pattern>_ 
    
Limit the commits output to ones with author/committer header lines that match the _< pattern>_ regular expression. With more than one `--author=`_< pattern>_, commits whose author matches any of the _< pattern>_ are chosen (similarly for multiple `--committer=`_< pattern>_). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---grep-reflogpattern)`--grep-reflog=`_< pattern>_ 
    
Limit the commits output to ones with reflog entries that match the _< pattern>_ regular expression. With more than one `--grep-reflog`, commits whose reflog message matches any of the given patterns are chosen. It is an error to use this option unless `--walk-reflogs` is in use. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---greppattern)`--grep=`_< pattern>_ 
    
Limit the commits output to ones with a log message that matches the _< pattern>_ regular expression. With more than one `--grep=`_< pattern>_, commits whose message matches any of the _< pattern>_ are chosen (but see `--all-match`).
When `--notes` is in effect, the message from the notes is matched as if it were part of the log message. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---all-match)`--all-match` 
    
Limit the commits output to ones that match all given `--grep`, instead of ones that match at least one. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---invert-grep)`--invert-grep` 
    
Limit the commits output to ones with a log message that do not match the _< pattern>_ specified with `--grep=`_< pattern>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--i)`-i` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---regexp-ignore-case)`--regexp-ignore-case` 
    
Match the regular expression limiting patterns without regard to letter case. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---basic-regexp)`--basic-regexp` 
    
Consider the limiting patterns to be basic regular expressions; this is the default. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--E)`-E` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---extended-regexp)`--extended-regexp` 
    
Consider the limiting patterns to be extended regular expressions instead of the default basic regular expressions. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--F)`-F` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---fixed-strings)`--fixed-strings` 
    
Consider the limiting patterns to be fixed strings (don’t interpret pattern as a regular expression). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--P)`-P` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---perl-regexp)`--perl-regexp` 
    
Consider the limiting patterns to be Perl-compatible regular expressions.
Support for these types of regular expressions is an optional compile-time dependency. If Git wasn’t compiled with support for them providing this option will cause it to die. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---remove-empty)`--remove-empty` 
    
Stop when a given path disappears from the tree. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---merges)`--merges` 
    
Print only merge commits. This is exactly the same as `--min-parents=2`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-merges)`--no-merges` 
    
Do not print commits with more than one parent. This is exactly the same as `--max-parents=1`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---min-parentsnumber)`--min-parents=`_< number>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---max-parentsnumber)`--max-parents=`_< number>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-min-parents)`--no-min-parents` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-max-parents)`--no-max-parents` 
    
Show only commits which have at least (or at most) that many parent commits. In particular, `--max-parents=1` is the same as `--no-merges`, `--min-parents=2` is the same as `--merges`. `--max-parents=0` gives all root commits and `--min-parents=3` all octopus merges.
`--no-min-parents` and `--no-max-parents` reset these limits (to no limit) again. Equivalent forms are `--min-parents=0` (any commit has 0 or more parents) and `--max-parents=-1` (negative numbers denote no upper limit). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---first-parent)`--first-parent` 
    
When finding commits to include, follow only the first parent commit upon seeing a merge commit. This option can give a better overview when viewing the evolution of a particular topic branch, because merges into a topic branch tend to be only about adjusting to updated upstream from time to time, and this option allows you to ignore the individual commits brought in to your history by such a merge.
This option also changes default diff format for merge commits to `first-parent`, see `--diff-merges=first-parent` for details. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---exclude-first-parent-only)`--exclude-first-parent-only` 
    
When finding commits to exclude (with a _^_), follow only the first parent commit upon seeing a merge commit. This can be used to find the set of changes in a topic branch from the point where it diverged from the remote branch, given that arbitrary merges can be valid topic branch changes. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---not)`--not` 
    
Reverses the meaning of the _^_ prefix (or lack thereof) for all following revision specifiers, up to the next `--not`. When used on the command line before --stdin, the revisions passed through stdin will not be affected by it. Conversely, when passed via standard input, the revisions passed on the command line will not be affected by it. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---all)`--all` 
    
Pretend as if all the refs in `refs/`, along with `HEAD`, are listed on the command line as _< commit>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---branchespattern)`--branches`[`=`_< pattern>_] 
    
Pretend as if all the refs in `refs/heads` are listed on the command line as _< commit>_. If _< pattern>_ is given, limit branches to ones matching given shell glob. If _< pattern>_ lacks _?_ , _*_ , or _[_ , _/*_ at the end is implied. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---tagspattern)`--tags`[`=`_< pattern>_] 
    
Pretend as if all the refs in `refs/tags` are listed on the command line as _< commit>_. If _< pattern>_ is given, limit tags to ones matching given shell glob. If pattern lacks _?_ , _*_ , or _[_ , _/*_ at the end is implied. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---remotespattern)`--remotes`[`=`_< pattern>_] 
    
Pretend as if all the refs in `refs/remotes` are listed on the command line as _< commit>_. If _< pattern>_ is given, limit remote-tracking branches to ones matching given shell glob. If pattern lacks _?_ , _*_ , or _[_ , _/*_ at the end is implied. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---globglob-pattern)`--glob=`_< glob-pattern>_ 
    
Pretend as if all the refs matching shell glob _< glob-pattern>_ are listed on the command line as _< commit>_. Leading _refs/_ , is automatically prepended if missing. If pattern lacks _?_ , _*_ , or _[_ , _/*_ at the end is implied. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---excludeglob-pattern)`--exclude=`_< glob-pattern>_ 
    
Do not include refs matching _< glob-pattern>_ that the next `--all`, `--branches`, `--tags`, `--remotes`, or `--glob` would otherwise consider. Repetitions of this option accumulate exclusion patterns up to the next `--all`, `--branches`, `--tags`, `--remotes`, or `--glob` option (other options or arguments do not clear accumulated patterns).
The patterns given should not begin with `refs/heads`, `refs/tags`, or `refs/remotes` when applied to `--branches`, `--tags`, or `--remotes`, respectively, and they must begin with `refs/` when applied to `--glob` or `--all`. If a trailing _/*_ is intended, it must be given explicitly. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---exclude-hiddenfetchreceiveuploadpack)`--exclude-hidden=`(`fetch`|`receive`|`uploadpack`) 
    
Do not include refs that would be hidden by `git-fetch`, `git-receive-pack` or `git-upload-pack` by consulting the appropriate `fetch.hideRefs`, `receive.hideRefs` or `uploadpack.hideRefs` configuration along with `transfer.hideRefs` (see [git-config[1]](https://git-scm.com/docs/git-config)). This option affects the next pseudo-ref option `--all` or `--glob` and is cleared after processing them. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---reflog)`--reflog` 
    
Pretend as if all objects mentioned by reflogs are listed on the command line as _< commit>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---alternate-refs)`--alternate-refs` 
    
Pretend as if all objects mentioned as ref tips of alternate repositories were listed on the command line. An alternate repository is any repository whose object directory is specified in `objects/info/alternates`. The set of included objects may be modified by `core.alternateRefsCommand`, etc. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---single-worktree)`--single-worktree` 
    
By default, all working trees will be examined by the following options when there are more than one (see [git-worktree[1]](https://git-scm.com/docs/git-worktree)): `--all`, `--reflog` and `--indexed-objects`. This option forces them to examine the current working tree only. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-missing)`--ignore-missing` 
    
Upon seeing an invalid object name in the input, pretend as if the bad input was not given. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---bisect)`--bisect` 
    
Pretend as if the bad bisection ref `refs/bisect/bad` was listed and as if it was followed by `--not` and the good bisection refs `refs/bisect/good-*` on the command line. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---stdin)`--stdin` 
    
In addition to getting arguments from the command line, read them from standard input as well. This accepts commits and pseudo-options like `--all` and `--glob=`. When a `--` separator is seen, the following input is treated as paths and used to limit the result. Flags like `--not` which are read via standard input are only respected for arguments passed in the same way and will not influence any subsequent command line arguments. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---cherry-mark)`--cherry-mark` 
    
Like `--cherry-pick` (see below) but mark equivalent commits with `=` rather than omitting them, and inequivalent ones with `+`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---cherry-pick)`--cherry-pick` 
    
Omit any commit that introduces the same change as another commit on the “other side” when the set of commits are limited with symmetric difference.
For example, if you have two branches, `A` and `B`, a usual way to list all commits on only one side of them is with `--left-right` (see the example below in the description of the `--left-right` option). However, it shows the commits that were cherry-picked from the other branch (for example, “3rd on b” may be cherry-picked from branch A). With this option, such pairs of commits are excluded from the output. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---left-only)`--left-only` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---right-only)`--right-only` 
    
List only commits on the respective side of a symmetric difference, i.e. only those which would be marked _<_ resp. _>_ by `--left-right`.
For example, `--cherry-pick` `--right-only` `A...B` omits those commits from `B` which are in `A` or are patch-equivalent to a commit in `A`. In other words, this lists the `+` commits from `git` `cherry` `A` `B`. More precisely, `--cherry-pick` `--right-only` `--no-merges` gives the exact list. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---cherry)`--cherry` 
    
A synonym for `--right-only` `--cherry-mark` `--no-merges`; useful to limit the output to the commits on our side and mark those that have been applied to the other side of a forked history with `git` `log` `--cherry` `upstream...mybranch`, similar to `git` `cherry` `upstream` `mybranch`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--g)`-g` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---walk-reflogs)`--walk-reflogs` 
    
Instead of walking the commit ancestry chain, walk reflog entries from the most recent one to older ones. When this option is used you cannot specify commits to exclude (that is, `^`_< commit>_, _< commit1>_`..`_< commit2>_, and _< commit1>_`...`_< commit2>_ notations cannot be used).
With `--pretty` format other than `oneline` and `reference` (for obvious reasons), this causes the output to have two extra lines of information taken from the reflog. The reflog designator in the output may be shown as `ref@{`_< Nth>_`}` (where _< Nth>_ is the reverse-chronological index in the reflog) or as `ref@{`_< timestamp>_`}` (with the _< timestamp>_ for that entry), depending on a few rules:
  1. If the starting point is specified as `ref@{`_< Nth>_`}`, show the index format.
  2. If the starting point was specified as `ref@{now}`, show the timestamp format.
  3. If neither was used, but `--date` was given on the command line, show the timestamp in the format requested by `--date`.
  4. Otherwise, show the index format.


Under `--pretty=oneline`, the commit message is prefixed with this information on the same line. This option cannot be combined with `--reverse`. See also [git-reflog[1]](https://git-scm.com/docs/git-reflog).
Under `--pretty=reference`, this information will not be shown at all. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---merge)`--merge` 
    
Show commits touching conflicted paths in the range `HEAD...`_< other>_, where _< other>_ is the first existing pseudoref in `MERGE_HEAD`, `CHERRY_PICK_HEAD`, `REVERT_HEAD` or `REBASE_HEAD`. Only works when the index has unmerged entries. This option can be used to show relevant commits when resolving conflicts from a 3-way merge. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---boundary)`--boundary` 
    
Output excluded boundary commits. Boundary commits are prefixed with `-`.
###  [](https://git-scm.com/docs/git-log#_history_simplification)History Simplification
Sometimes you are only interested in parts of the history, for example the commits modifying a particular <path>. But there are two parts of _History Simplification_ , one part is selecting the commits and the other is how to do it, as there are various strategies to simplify the history.
The following options select the commits to be shown: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-paths)_< paths>_ 
    
Commits modifying the given <paths> are selected. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---simplify-by-decoration)`--simplify-by-decoration` 
    
Commits that are referred by some branch or tag are selected.
Note that extra commits can be shown to give a meaningful history.
The following options affect the way the simplification is performed: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-Defaultmode)`Default` `mode` 
    
Simplifies the history to the simplest history explaining the final state of the tree. Simplest because it prunes some side branches if the end result is the same (i.e. merging branches with the same content) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---show-pulls)`--show-pulls` 
    
Include all commits from the default mode, but also any merge commits that are not TREESAME to the first parent but are TREESAME to a later parent. This mode is helpful for showing the merge commits that "first introduced" a change to a branch. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---full-history)`--full-history` 
    
Same as the default mode, but does not prune some history. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dense)`--dense` 
    
Only the selected commits are shown, plus some to have a meaningful history. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---sparse)`--sparse` 
    
All commits in the simplified history are shown. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---simplify-merges)`--simplify-merges` 
    
Additional option to `--full-history` to remove some needless merges from the resulting history, as there are no selected commits contributing to this merge. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ancestry-pathcommit)`--ancestry-path`[`=`_< commit>_] 
    
When given a range of commits to display (e.g. _< commit1>_`..`_< commit2>_ or _< commit2>_ `^`_< commit1>_), and a commit _< commit>_ in that range, only display commits in that range that are ancestors of _< commit>_, descendants of _< commit>_, or _< commit>_ itself. If no commit is specified, use _< commit1>_ (the excluded part of the range) as _< commit>_. Can be passed multiple times; if so, a commit is included if it is any of the commits given or if it is an ancestor or descendant of one of them.
A more detailed explanation follows.
Suppose you specified `foo` as the _< paths>_. We shall call commits that modify `foo` !TREESAME, and the rest TREESAME. (In a diff filtered for `foo`, they look different and equal, respectively.)
In the following, we will always refer to the same example history to illustrate the differences between simplification settings. We assume that you are filtering for a file `foo` in this commit graph:
```
	  .-A---M---N---O---P---Q
	 /     /   /   /   /   /
	I     B   C   D   E   Y
	 \   /   /   /   /   /
	  `-------------'   X
```

The horizontal line of history A---Q is taken to be the first parent of each merge. The commits are:
  * `I` is the initial commit, in which `foo` exists with contents `asdf`, and a file `quux` exists with contents `quux`. Initial commits are compared to an empty tree, so `I` is !TREESAME.
  * In `A`, `foo` contains just `foo`.
  * `B` contains the same change as `A`. Its merge `M` is trivial and hence TREESAME to all parents.
  * `C` does not change `foo`, but its merge `N` changes it to `foobar`, so it is not TREESAME to any parent.
  * `D` sets `foo` to `baz`. Its merge `O` combines the strings from `N` and `D` to `foobarbaz`; i.e., it is not TREESAME to any parent.
  * `E` changes `quux` to `xyzzy`, and its merge `P` combines the strings to `quux` `xyzzy`. `P` is TREESAME to `O`, but not to `E`.
  * `X` is an independent root commit that added a new file `side`, and `Y` modified it. `Y` is TREESAME to `X`. Its merge `Q` added `side` to `P`, and `Q` is TREESAME to `P`, but not to `Y`.


`rev-list` walks backwards through history, including or excluding commits based on whether `--full-history` and/or parent rewriting (via `--parents` or `--children`) are used. The following settings are available. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-Defaultmode-1)Default mode 
    
Commits are included if they are not TREESAME to any parent (though this can be changed, see `--sparse` below). If the commit was a merge, and it was TREESAME to one parent, follow only that parent. (Even if there are several TREESAME parents, follow only one of them.) Otherwise, follow all parents.
This results in:
```
	  .-A---N---O
	 /     /   /
	I---------D
```

Note how the rule to only follow the TREESAME parent, if one is available, removed `B` from consideration entirely. `C` was considered via `N`, but is TREESAME. Root commits are compared to an empty tree, so `I` is !TREESAME.
Parent/child relations are only visible with `--parents`, but that does not affect the commits selected in default mode, so we have shown the parent lines. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---full-historywithoutparentrewriting)`--full-history` without parent rewriting 
    
This mode differs from the default in one point: always follow all parents of a merge, even if it is TREESAME to one of them. Even if more than one side of the merge has commits that are included, this does not imply that the merge itself is! In the example, we get
```
	I  A  B  N  D  O  P  Q
```

`M` was excluded because it is TREESAME to both parents. `E`, `C` and `B` were all walked, but only `B` was !TREESAME, so the others do not appear.
Note that without parent rewriting, it is not really possible to talk about the parent/child relationships between the commits, so we show them disconnected. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---full-historywithparentrewriting)`--full-history` with parent rewriting 
    
Ordinary commits are only included if they are !TREESAME (though this can be changed, see `--sparse` below).
Merges are always included. However, their parent list is rewritten: Along each parent, prune away commits that are not included themselves. This results in
```
	  .-A---M---N---O---P---Q
	 /     /   /   /   /
	I     B   /   D   /
	 \   /   /   /   /
	  `-------------'
```

Compare to `--full-history` without rewriting above. Note that `E` was pruned away because it is TREESAME, but the parent list of P was rewritten to contain `E`'s parent `I`. The same happened for `C` and `N`, and `X`, `Y` and `Q`.
In addition to the above settings, you can change whether TREESAME affects inclusion: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dense-1)`--dense` 
    
Commits that are walked are included if they are not TREESAME to any parent. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---sparse-1)`--sparse` 
    
All commits that are walked are included.
Note that without `--full-history`, this still simplifies merges: if one of the parents is TREESAME, we follow only that one, so the other sides of the merge are never walked. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---simplify-merges-1)`--simplify-merges` 
    
First, build a history graph in the same way that `--full-history` with parent rewriting does (see above).
Then simplify each commit `C` to its replacement `C'` in the final history according to the following rules:
  * Set `C'` to `C`.
  * Replace each parent `P` of `C'` with its simplification `P'`. In the process, drop parents that are ancestors of other parents or that are root commits TREESAME to an empty tree, and remove duplicates, but take care to never drop all parents that we are TREESAME to.
  * If after this parent rewriting, `C'` is a root or merge commit (has zero or >1 parents), a boundary commit, or !TREESAME, it remains. Otherwise, it is replaced with its only parent.


The effect of this is best shown by way of comparing to `--full-history` with parent rewriting. The example turns into:
```
	  .-A---M---N---O
	 /     /       /
	I     B       D
	 \   /       /
	  `---------'
```

Note the major differences in `N`, `P`, and `Q` over `--full-history`:
  * `N`'s parent list had `I` removed, because it is an ancestor of the other parent `M`. Still, `N` remained because it is !TREESAME.
  * `P`'s parent list similarly had `I` removed. `P` was then removed completely, because it had one parent and is TREESAME.
  * `Q`'s parent list had `Y` simplified to `X`. `X` was then removed, because it was a TREESAME root. `Q` was then removed completely, because it had one parent and is TREESAME.


There is another simplification mode available: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ancestry-pathcommit-1)`--ancestry-path`[`=`_< commit>_] 
    
Limit the displayed commits to those which are an ancestor of _< commit>_, or which are a descendant of _< commit>_, or are _< commit>_ itself.
As an example use case, consider the following commit history:
```
	    D---E-------F
	   /     \       \
	  B---C---G---H---I---J
	 /                     \
	A-------K---------------L--M
```

A regular _D..M_ computes the set of commits that are ancestors of `M`, but excludes the ones that are ancestors of `D`. This is useful to see what happened to the history leading to `M` since `D`, in the sense that "what does `M` have that did not exist in `D`". The result in this example would be all the commits, except `A` and `B` (and `D` itself, of course).
When we want to find out what commits in `M` are contaminated with the bug introduced by `D` and need fixing, however, we might want to view only the subset of `D..M` that are actually descendants of `D`, i.e. excluding `C` and `K`. This is exactly what the `--ancestry-path` option does. Applied to the `D..M` range, it results in:
```
		E-------F
		 \       \
		  G---H---I---J
			       \
				L--M
```

We can also use `--ancestry-path=D` instead of `--ancestry-path` which means the same thing when applied to the `D..M` range but is just more explicit.
If we instead are interested in a given topic within this range, and all commits affected by that topic, we may only want to view the subset of `D..M` which contain that topic in their ancestry path. So, using `--ancestry-path=H` `D..M` for example would result in:
```
		E
		 \
	      C---G---H---I---J
			       \
				L--M
```

Whereas `--ancestry-path=K` `D..M` would result in
```
		K---------------L--M
```

Before discussing another option, `--show-pulls`, we need to create a new example history.
A common problem users face when looking at simplified history is that a commit they know changed a file somehow does not appear in the file’s simplified history. Let’s demonstrate a new example and show how options such as `--full-history` and `--simplify-merges` works in that case:
```
	  .-A---M-----C--N---O---P
	 /     / \  \  \/   /   /
	I     B   \  R-'`-Z'   /
	 \   /     \/         /
	  \ /      /\        /
	   `---X--'  `---Y--'
```

For this example, suppose `I` created `file.txt` which was modified by `A`, `B`, and `X` in different ways. The single-parent commits `C`, `Z`, and `Y` do not change `file.txt`. The merge commit `M` was created by resolving the merge conflict to include both changes from `A` and `B` and hence is not TREESAME to either. The merge commit `R`, however, was created by ignoring the contents of `file.txt` at `M` and taking only the contents of `file.txt` at `X`. Hence, `R` is TREESAME to `X` but not `M`. Finally, the natural merge resolution to create `N` is to take the contents of `file.txt` at `R`, so `N` is TREESAME to `R` but not `C`. The merge commits `O` and `P` are TREESAME to their first parents, but not to their second parents, `Z` and `Y` respectively.
When using the default mode, `N` and `R` both have a TREESAME parent, so those edges are walked and the others are ignored. The resulting history graph is:
```
	I---X
```

When using `--full-history`, Git walks every edge. This will discover the commits `A` and `B` and the merge `M`, but also will reveal the merge commits `O` and `P`. With parent rewriting, the resulting graph is:
```
	  .-A---M--------N---O---P
	 /     / \  \  \/   /   /
	I     B   \  R-'`--'   /
	 \   /     \/         /
	  \ /      /\        /
	   `---X--'  `------'
```

Here, the merge commits `O` and `P` contribute extra noise, as they did not actually contribute a change to `file.txt`. They only merged a topic that was based on an older version of `file.txt`. This is a common issue in repositories using a workflow where many contributors work in parallel and merge their topic branches along a single trunk: many unrelated merges appear in the `--full-history` results.
When using the `--simplify-merges` option, the commits `O` and `P` disappear from the results. This is because the rewritten second parents of `O` and `P` are reachable from their first parents. Those edges are removed and then the commits look like single-parent commits that are TREESAME to their parent. This also happens to the commit `N`, resulting in a history view as follows:
```
	  .-A---M--.
	 /     /    \
	I     B      R
	 \   /      /
	  \ /      /
	   `---X--'
```

In this view, we see all of the important single-parent changes from `A`, `B`, and `X`. We also see the carefully-resolved merge `M` and the not-so-carefully-resolved merge `R`. This is usually enough information to determine why the commits `A` and `B` "disappeared" from history in the default view. However, there are a few issues with this approach.
The first issue is performance. Unlike any previous option, the `--simplify-merges` option requires walking the entire commit history before returning a single result. This can make the option difficult to use for very large repositories.
The second issue is one of auditing. When many contributors are working on the same repository, it is important which merge commits introduced a change into an important branch. The problematic merge `R` above is not likely to be the merge commit that was used to merge into an important branch. Instead, the merge `N` was used to merge `R` and `X` into the important branch. This commit may have information about why the change `X` came to override the changes from `A` and `B` in its commit message. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---show-pulls-1)`--show-pulls` 
    
In addition to the commits shown in the default history, show each merge commit that is not TREESAME to its first parent but is TREESAME to a later parent.
When a merge commit is included by `--show-pulls`, the merge is treated as if it "pulled" the change from another branch. When using `--show-pulls` on this example (and no other options) the resulting graph is:
```
	I---X---R---N
```

Here, the merge commits `R` and `N` are included because they pulled the commits `X` and `R` into the base branch, respectively. These merges are the reason the commits `A` and `B` do not appear in the default history.
When `--show-pulls` is paired with `--simplify-merges`, the graph includes all of the necessary information:
```
	  .-A---M--.   N
	 /     /    \ /
	I     B      R
	 \   /      /
	  \ /      /
	   `---X--'
```

Notice that since `M` is reachable from `R`, the edge from `N` to `M` was simplified away. However, `N` still appears in the history as an important commit because it "pulled" the change `R` into the main branch.
The `--simplify-by-decoration` option allows you to view only the big picture of the topology of the history, by omitting commits that are not referenced by tags. Commits are marked as !TREESAME (in other words, kept after history simplification rules described above) if (1) they are referenced by tags, or (2) they change the contents of the paths given on the command line. All other commits are marked as TREESAME (subject to be simplified away).
###  [](https://git-scm.com/docs/git-log#_commit_ordering)Commit Ordering
By default, the commits are shown in reverse chronological order. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---date-order)`--date-order` 
    
Show no parents before all of its children are shown, but otherwise show commits in the commit timestamp order. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---author-date-order)`--author-date-order` 
    
Show no parents before all of its children are shown, but otherwise show commits in the author timestamp order. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---topo-order)`--topo-order` 
    
Show no parents before all of its children are shown, and avoid showing commits on multiple lines of history intermixed.
For example, in a commit history like this:
```
    ---1----2----4----7
	\	       \
	 3----5----6----8---
```

where the numbers denote the order of commit timestamps, `git` `rev-list` and friends with `--date-order` show the commits in the timestamp order: 8 7 6 5 4 3 2 1.
With `--topo-order`, they would show 8 6 5 3 7 4 2 1 (or 8 7 4 2 6 5 3 1); some older commits are shown before newer ones in order to avoid showing the commits from two parallel development track mixed together. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---reverse)`--reverse` 
    
Output the commits chosen to be shown (see _Commit Limiting_ section above) in reverse order. Cannot be combined with `--walk-reflogs`.
###  [](https://git-scm.com/docs/git-log#_object_traversal)Object Traversal
These options are mostly targeted for packing of Git repositories. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-walksortedunsorted)`--no-walk`[`=`(`sorted`|`unsorted`)] 
    
Only show the given commits, but do not traverse their ancestors. This has no effect if a range is specified. If the argument `unsorted` is given, the commits are shown in the order they were given on the command line. Otherwise (if `sorted` or no argument was given), the commits are shown in reverse chronological order by commit time. Cannot be combined with `--graph`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---do-walk)`--do-walk` 
    
Overrides a previous `--no-walk`.
###  [](https://git-scm.com/docs/git-log#_commit_formatting)Commit Formatting 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---prettyformat)`--pretty`[`=`_< format>_] 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---formatformat)`--format=`_< format>_ 
    
Pretty-print the contents of the commit logs in a given format, where _< format>_ can be one of `oneline`, `short`, `medium`, `full`, `fuller`, `reference`, `email`, `raw`, `format:`_< string>_ and `tformat:`_< string>_. When _< format>_ is none of the above, and has `%`_< placeholder>_ in it, it acts as if `--pretty=tformat:`_< format>_ were given.
See the "PRETTY FORMATS" section for some additional details for each format. When `=`_< format>_ part is omitted, it defaults to `medium`.
Note |  you can specify the default pretty format in the repository configuration (see [git-config[1]](https://git-scm.com/docs/git-config)).   
---|--- 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---abbrev-commit)`--abbrev-commit` 
      
Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely. `--abbrev=`_< n>_ (which also modifies diff output, if it is displayed) option can be used to specify the minimum length of the prefix.
This should make `--pretty=oneline` a whole lot more readable for people using 80-column terminals. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-abbrev-commit)`--no-abbrev-commit` 
    
Show the full 40-byte hexadecimal commit object name. This negates `--abbrev-commit`, either explicit or implied by other options such as `--oneline`. It also overrides the `log.abbrevCommit` variable. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---oneline)`--oneline` 
    
This is a shorthand for `--pretty=oneline` `--abbrev-commit` used together. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---encodingencoding)`--encoding=`_< encoding>_ 
    
Commit objects record the character encoding used for the log message in their encoding header; this option can be used to tell the command to re-code the commit log message in the encoding preferred by the user. For non plumbing commands this defaults to UTF-8. Note that if an object claims to be encoded in `X` and we are outputting in `X`, we will output the object verbatim; this means that invalid sequences in the original commit may be copied to the output. Likewise, if iconv(3) fails to convert the commit, we will quietly output the original object verbatim. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---expand-tabsn)`--expand-tabs=`_< n>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---expand-tabs)`--expand-tabs` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-expand-tabs)`--no-expand-tabs` 
    
Perform a tab expansion (replace each tab with enough spaces to fill to the next display column that is a multiple of _< n>_) in the log message before showing it in the output. `--expand-tabs` is a short-hand for `--expand-tabs=8`, and `--no-expand-tabs` is a short-hand for `--expand-tabs=0`, which disables tab expansion.
By default, tabs are expanded in pretty formats that indent the log message by 4 spaces (i.e. `medium`, which is the default, `full`, and `fuller`). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---notesref)`--notes`[`=`_< ref>_] 
    
Show the notes (see [git-notes[1]](https://git-scm.com/docs/git-notes)) that annotate the commit, when showing the commit log message. This is the default for `git` `log`, `git` `show` and `git` `whatchanged` commands when there is no `--pretty`, `--format`, or `--oneline` option given on the command line.
By default, the notes shown are from the notes refs listed in the `core.notesRef` and `notes.displayRef` variables (or corresponding environment overrides). See [git-config[1]](https://git-scm.com/docs/git-config) for more details.
With an optional _< ref>_ argument, use the ref to find the notes to display. The ref can specify the full refname when it begins with `refs/notes/`; when it begins with `notes/`, `refs/` and otherwise `refs/notes/` is prefixed to form the full name of the ref.
Multiple `--notes` options can be combined to control which notes are being displayed. Examples: "`--notes=foo`" will show only notes from `refs/notes/foo`; "`--notes=foo` `--notes`" will show both notes from "refs/notes/foo" and from the default notes ref(s). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-notes)`--no-notes` 
    
Do not show notes. This negates the above `--notes` option, by resetting the list of notes refs from which notes are shown. Options are parsed in the order given on the command line, so e.g. "`--notes` `--notes=foo` `--no-notes` `--notes=bar`" will only show notes from `refs/notes/bar`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---show-notes-by-default)`--show-notes-by-default` 
    
Show the default notes unless options for displaying specific notes are given. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---show-notesref)`--show-notes`[`=`_< ref>_] 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---standard-notes)`--standard-notes` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-standard-notes)`--no-standard-notes` 
    
These options are deprecated. Use the above `--notes`/`--no-notes` options instead. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---show-signature)`--show-signature` 
    
Check the validity of a signed commit object by passing the signature to `gpg` `--verify` and show the output. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---relative-date)`--relative-date` 
    
Synonym for `--date=relative`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dateformat)`--date=`_< format>_ 
    
Only takes effect for dates shown in human-readable format, such as when using `--pretty`. `log.date` config variable sets a default value for the log command’s `--date` option. By default, dates are shown in the original time zone (either committer’s or author’s). If `-local` is appended to the format (e.g., `iso-local`), the user’s local time zone is used instead.
`--date=relative` shows dates relative to the current time, e.g. “2 hours ago”. The `-local` option has no effect for `--date=relative`.
`--date=local` is an alias for `--date=default-local`.
`--date=iso` (or `--date=iso8601`) shows timestamps in a ISO 8601-like format. The differences to the strict ISO 8601 format are:
  * a space instead of the `T` date/time delimiter
  * a space between time and time zone
  * no colon between hours and minutes of the time zone


`--date=iso-strict` (or `--date=iso8601-strict`) shows timestamps in strict ISO 8601 format.
`--date=rfc` (or `--date=rfc2822`) shows timestamps in RFC 2822 format, often found in email messages.
`--date=short` shows only the date, but not the time, in `YYYY-MM-DD` format.
`--date=raw` shows the date as seconds since the epoch (1970-01-01 00:00:00 UTC), followed by a space, and then the timezone as an offset from UTC (a `+` or `-` with four digits; the first two are hours, and the second two are minutes). I.e., as if the timestamp were formatted with `strftime`(`"%s` `%z"`)). Note that the `-local` option does not affect the seconds-since-epoch value (which is always measured in UTC), but does switch the accompanying timezone value.
`--date=human` shows the timezone if the timezone does not match the current time-zone, and doesn’t print the whole date if that matches (ie skip printing year for dates that are "this year", but also skip the whole date itself if it’s in the last few days and we can just say what weekday it was). For older dates the hour and minute is also omitted.
`--date=unix` shows the date as a Unix epoch timestamp (seconds since 1970). As with `--raw`, this is always in UTC and therefore `-local` has no effect.
`--date=format:`_< format>_ feeds the _< format>_ to your system `strftime`, except for `%s`, `%z`, and `%Z`, which are handled internally. Use `--date=format:%c` to show the date in your system locale’s preferred format. See the `strftime`(3) manual for a complete list of format placeholders. When using `-local`, the correct syntax is `--date=format-local:`_< format>_.
`--date=default` is the default format, and is based on ctime(3) output. It shows a single line with three-letter day of the week, three-letter month, day-of-month, hour-minute-seconds in "HH:MM:SS" format, followed by 4-digit year, plus timezone information, unless the local time zone is used, e.g. `Thu` `Jan` `1` `00:00:00` `1970` `+0000`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---parents)`--parents` 
    
Print also the parents of the commit (in the form "commit parent…​"). Also enables parent rewriting, see _History Simplification_ above. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---children)`--children` 
    
Print also the children of the commit (in the form "commit child…​"). Also enables parent rewriting, see _History Simplification_ above. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---left-right)`--left-right` 
    
Mark which side of a symmetric difference a commit is reachable from. Commits from the left side are prefixed with _<_ and those from the right with _>_. If combined with `--boundary`, those commits are prefixed with `-`.
For example, if you have this topology:
```
	     y---b---b  branch B
	    / \ /
	   /   .
	  /   / \
	 o---x---a---a  branch A
```

you would get an output like this:
```
	$ git rev-list --left-right --boundary --pretty=oneline A...B

	>bbbbbbb... 3rd on b
	>bbbbbbb... 2nd on b
	<aaaaaaa... 3rd on a
	<aaaaaaa... 2nd on a
	-yyyyyyy... 1st on b
	-xxxxxxx... 1st on a
```


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---graph)`--graph` 
    
Draw a text-based graphical representation of the commit history on the left hand side of the output. This may cause extra lines to be printed in between commits, in order for the graph history to be drawn properly. Cannot be combined with `--no-walk`.
This enables parent rewriting, see _History Simplification_ above.
This implies the `--topo-order` option by default, but the `--date-order` option may also be specified. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---show-linear-breakbarrier)`--show-linear-break`[`=`_< barrier>_] 
    
When `--graph` is not used, all history branches are flattened which can make it hard to see that the two consecutive commits do not belong to a linear branch. This option puts a barrier in between them in that case. If _< barrier>_ is specified, it is the string that will be shown instead of the default one.
##  [](https://git-scm.com/docs/git-log#_pretty_formats)PRETTY FORMATS
If the commit is a merge, and if the pretty-format is not `oneline`, `email` or `raw`, an additional line is inserted before the `Author:` line. This line begins with "Merge: " and the hashes of ancestral commits are printed, separated by spaces. Note that the listed commits may not necessarily be the list of the _direct_ parent commits if you have limited your view of history: for example, if you are only interested in changes related to a certain directory or file.
There are several built-in formats, and you can define additional formats by setting a pretty.<name> config option to either another format name, or a `format:` string, as described below (see [git-config[1]](https://git-scm.com/docs/git-config)). Here are the details of the built-in formats:
  * `oneline`
```
<hash> <title-line>
```

This is designed to be as compact as possible.
  * `short`
```
commit <hash>
Author: <author>
```

```
<title-line>
```

  * `medium`
```
commit <hash>
Author: <author>
Date:   <author-date>
```

```
<title-line>
```

```
<full-commit-message>
```

  * `full`
```
commit <hash>
Author: <author>
Commit: <committer>
```

```
<title-line>
```

```
<full-commit-message>
```

  * `fuller`
```
commit <hash>
Author:     <author>
AuthorDate: <author-date>
Commit:     <committer>
CommitDate: <committer-date>
```

```
<title-line>
```

```
<full-commit-message>
```

  * `reference`
```
<abbrev-hash> (<title-line>, <short-author-date>)
```

This format is used to refer to another commit in a commit message and is the same as `--pretty='format:%C`(`auto`)`%h` (`%s,` `%ad`). By default, the date is formatted with `--date=short` unless another `--date` option is explicitly specified. As with any `format:` with format placeholders, its output is not affected by other options like `--decorate` and `--walk-reflogs`.
  * `email`
```
From <hash> <date>
From: <author>
Date: <author-date>
Subject: [PATCH] <title-line>
```

```
<full-commit-message>
```

  * `mboxrd`
Like `email`, but lines in the commit message starting with "From " (preceded by zero or more ">") are quoted with ">" so they aren’t confused as starting a new commit.
  * `raw`
The `raw` format shows the entire commit exactly as stored in the commit object. Notably, the hashes are displayed in full, regardless of whether `--abbrev` or `--no-abbrev` are used, and _parents_ information show the true parent commits, without taking grafts or history simplification into account. Note that this format affects the way commits are displayed, but not the way the diff is shown e.g. with `git` `log` `--raw`. To get full object names in a raw diff format, use `--no-abbrev`.
  * `format:`_< format-string>_
The `format:`_< format-string>_ format allows you to specify which information you want to show. It works a little bit like printf format, with the notable exception that you get a newline with `%n` instead of _\n_.
E.g, _format:"The author of %h was %an, %ar%nThe title was >>%s<<%n"_ would show something like this:
```
The author of fe6e0ee was Junio C Hamano, 23 hours ago
The title was >>t4119: test autocomputing -p<n> for traditional diff input.<<
```

The placeholders are:
    * Placeholders that expand to a single literal character: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-n)`%n` 
    
newline 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-)`%%` 
    
a raw `%` 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-x00)`%x00` 
    
`%x` followed by two hexadecimal digits is replaced with a byte with the hexadecimal digits' value (we will call this "literal formatting code" in the rest of this document).
    * Placeholders that affect formatting of later placeholders: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-Cred)`%Cred` 
    
switch color to red 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-Cgreen)`%Cgreen` 
    
switch color to green 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-Cblue)`%Cblue` 
    
switch color to blue 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-Creset)`%Creset` 
    
reset color 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-Cspec)`%C`(_< spec>_) 
    
color specification, as described under Values in the "CONFIGURATION FILE" section of [git-config[1]](https://git-scm.com/docs/git-config). By default, colors are shown only when enabled for log output (by `color.diff`, `color.ui`, or `--color`, and respecting the `auto` settings of the former if we are going to a terminal). `%C`(`auto,`_< spec>_) is accepted as a historical synonym for the default (e.g., `%C`(`auto,red`)). Specifying `%C`(`always,`_< spec>_) will show the colors even when color is not otherwise enabled (though consider just using `--color=always` to enable color for the whole output, including this format and anything else git might color). `auto` alone (i.e. `%C`(`auto`)) will turn on auto coloring on the next placeholders until the color is switched again. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-m)`%m` 
    
left (_<_), right (_>_) or boundary (`-`) mark 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-wwi1i2)`%w`([_< w>_[`,`_< i1>_[`,`_< i2>_]]]) 
    
switch line wrapping, like the `-w` option of [git-shortlog[1]](https://git-scm.com/docs/git-shortlog). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ntruncltruncmtrunc)_% <(__< n>_[`,`(`trunc`|`ltrunc`|`mtrunc`)]) 
    
make the next placeholder take at least N column widths, padding spaces on the right if necessary. Optionally truncate (with ellipsis `..`) at the left (ltrunc) `..ft`, the middle (mtrunc) `mi..le`, or the end (trunc) `rig..`, if the output is longer than _< n>_ columns. Note 1: that truncating only works correctly with _< n>_ >= 2. Note 2: spaces around the _< n>_ and _< m>_ (see below) values are optional. Note 3: Emojis and other wide characters will take two display columns, which may over-run column boundaries. Note 4: decomposed character combining marks may be misplaced at padding boundaries. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-m-1)_% <|(__< m>_ ) 
    
make the next placeholder take at least until _< m>_ th display column, padding spaces on the right if necessary. Use negative _< m>_ values for column positions measured from the right hand edge of the terminal window. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-n-1)_% >(__< n>_) 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-m-1-1)_% >|(__< m>_) 
    
similar to _% <(__< n>_), _% <|(__< m>_) respectively, but padding spaces on the left 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-n-1-1)_% >>(__< n>_) 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-m-1-1-1)_% >>|(__< m>_) 
    
similar to _% >(__< n>_), _% >|(__< m>_) respectively, except that if the next placeholder takes more spaces than given and there are spaces on its left, use those spaces 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-n-1-1-1)_% ><(__< n>_) 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-m-1-1-1-1)_% ><|(__< m>_) 
    
similar to _% <(__< n>_), _% <|(__< m>_) respectively, but padding both sides (i.e. the text is centered)
    * Placeholders that expand to information extracted from the commit: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-H)`%H` 
    
commit hash 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-h)`%h` 
    
abbreviated commit hash 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-T)`%T` 
    
tree hash 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-t)`%t` 
    
abbreviated tree hash 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-P)`%P` 
    
parent hashes 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-p)`%p` 
    
abbreviated parent hashes 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-an)`%an` 
    
author name 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-aN)`%aN` 
    
author name (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ae)`%ae` 
    
author email 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-aE)`%aE` 
    
author email (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-al)`%al` 
    
author email local-part (the part before the `@` sign) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-aL)`%aL` 
    
author local-part (see `%al`) respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ad)`%ad` 
    
author date (format respects --date= option) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-aD)`%aD` 
    
author date, RFC2822 style 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ar)`%ar` 
    
author date, relative 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-at)`%at` 
    
author date, UNIX timestamp 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ai)`%ai` 
    
author date, ISO 8601-like format 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-aI)`%aI` 
    
author date, strict ISO 8601 format 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-as)`%as` 
    
author date, short format (`YYYY-MM-DD`) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ah)`%ah` 
    
author date, human style (like the `--date=human` option of [git-rev-list[1]](https://git-scm.com/docs/git-rev-list)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cn)`%cn` 
    
committer name 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cN)`%cN` 
    
committer name (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ce)`%ce` 
    
committer email 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cE)`%cE` 
    
committer email (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cl)`%cl` 
    
committer email local-part (the part before the `@` sign) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cL)`%cL` 
    
committer local-part (see `%cl`) respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cd)`%cd` 
    
committer date (format respects --date= option) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cD)`%cD` 
    
committer date, RFC2822 style 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cr)`%cr` 
    
committer date, relative 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ct)`%ct` 
    
committer date, UNIX timestamp 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ci)`%ci` 
    
committer date, ISO 8601-like format 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cI)`%cI` 
    
committer date, strict ISO 8601 format 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cs)`%cs` 
    
committer date, short format (`YYYY-MM-DD`) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ch)`%ch` 
    
committer date, human style (like the `--date=human` option of [git-rev-list[1]](https://git-scm.com/docs/git-rev-list)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-d)`%d` 
    
ref names, like the --decorate option of [git-log[1]](https://git-scm.com/docs/git-log) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-D)`%D` 
    
ref names without the " (", ")" wrapping. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-decorateoption)`%`(`decorate`[`:`_< option>_`,...`]) 
    
ref names with custom decorations. The `decorate` string may be followed by a colon and zero or more comma-separated options. Option values may contain literal formatting codes. These must be used for commas (`%x2C`) and closing parentheses (`%x29`), due to their role in the option syntax.
      * `prefix=`_< value>_: Shown before the list of ref names. Defaults to " (".
      * `suffix=`_< value>_: Shown after the list of ref names. Defaults to ")".
      * `separator=`_< value>_: Shown between ref names. Defaults to "`,` ".
      * `pointer=`_< value>_: Shown between HEAD and the branch it points to, if any. Defaults to "  _→_ ".
      * `tag=`_< value>_: Shown before tag names. Defaults to "`tag:` ".
For example, to produce decorations with no wrapping or tag annotations, and spaces as separators:
`%`(`decorate:prefix=,suffix=,tag=,separator=` ) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-describeoption)`%`(`describe`[`:`_< option>_`,...`]) 
    
human-readable name, like [git-describe[1]](https://git-scm.com/docs/git-describe); empty string for undescribable commits. The `describe` string may be followed by a colon and zero or more comma-separated options. Descriptions can be inconsistent when tags are added or removed at the same time.
    * `tags`[`=`_< bool-value>_]: Instead of only considering annotated tags, consider lightweight tags as well.
    * `abbrev=`_< number>_: Instead of using the default number of hexadecimal digits (which will vary according to the number of objects in the repository with a default of 7) of the abbreviated object name, use <number> digits, or as many digits as needed to form a unique object name.
    * `match=`_< pattern>_: Only consider tags matching the given `glob`(`7`) _< pattern>_, excluding the `refs/tags/` prefix.
    * `exclude=`_< pattern>_: Do not consider tags matching the given `glob`(`7`) _< pattern>_, excluding the `refs/tags/` prefix. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-S)`%S` 
    
ref name given on the command line by which the commit was reached (like `git` `log` `--source`), only works with `git` `log` 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-e)`%e` 
    
encoding 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-s)`%s` 
    
subject 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-f)`%f` 
    
sanitized subject line, suitable for a filename 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-b)`%b` 
    
body 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-B)`%B` 
    
raw body (unwrapped subject and body) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-N)`%N` 
    
commit notes 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-GG)`%GG` 
    
raw verification message from GPG for a signed commit 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-G)_%G?_ 
    
show "G" for a good (valid) signature, "B" for a bad signature, "U" for a good signature with unknown validity, "X" for a good signature that has expired, "Y" for a good signature made by an expired key, "R" for a good signature made by a revoked key, "E" if the signature cannot be checked (e.g. missing key) and "N" for no signature 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-GS)`%GS` 
    
show the name of the signer for a signed commit 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-GK)`%GK` 
    
show the key used to sign a signed commit 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-GF)`%GF` 
    
show the fingerprint of the key used to sign a signed commit 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-GP)`%GP` 
    
show the fingerprint of the primary key whose subkey was used to sign a signed commit 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-GT)`%GT` 
    
show the trust level for the key used to sign a signed commit 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gD)`%gD` 
    
reflog selector, e.g., `refs/stash@{1}` or `refs/stash@{2` `minutes` `ago}`; the format follows the rules described for the `-g` option. The portion before the `@` is the refname as given on the command line (so `git` `log` `-g` `refs/heads/master` would yield `refs/heads/master@{0}`). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gd)`%gd` 
    
shortened reflog selector; same as `%gD`, but the refname portion is shortened for human readability (so `refs/heads/master` becomes just `master`). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gn)`%gn` 
    
reflog identity name 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gN)`%gN` 
    
reflog identity name (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ge)`%ge` 
    
reflog identity email 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gE)`%gE` 
    
reflog identity email (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gs)`%gs` 
    
reflog subject 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-trailersoption)`%`(`trailers`[`:`_< option>_`,...`]) 
    
display the trailers of the body as interpreted by [git-interpret-trailers[1]](https://git-scm.com/docs/git-interpret-trailers). The `trailers` string may be followed by a colon and zero or more comma-separated options. If any option is provided multiple times, the last occurrence wins.
    * `key=`_< key>_: only show trailers with specified <key>. Matching is done case-insensitively and trailing colon is optional. If option is given multiple times trailer lines matching any of the keys are shown. This option automatically enables the `only` option so that non-trailer lines in the trailer block are hidden. If that is not desired it can be disabled with `only=false`. E.g., `%`(`trailers:key=Reviewed-by`) shows trailer lines with key `Reviewed-by`.
    * `only`[`=`_< bool>_]: select whether non-trailer lines from the trailer block should be included.
    * `separator=`_< sep>_: specify the separator inserted between trailer lines. Defaults to a line feed character. The string <sep> may contain the literal formatting codes described above. To use comma as separator one must use `%x2C` as it would otherwise be parsed as next option. E.g., `%`(`trailers:key=Ticket,separator=%x2C` ) shows all trailer lines whose key is "Ticket" separated by a comma and a space.
    * `unfold`[`=`_< bool>_]: make it behave as if interpret-trailer’s `--unfold` option was given. E.g., `%`(`trailers:only,unfold=true`) unfolds and shows all trailer lines.
    * `keyonly`[`=`_< bool>_]: only show the key part of the trailer.
    * `valueonly`[`=`_< bool>_]: only show the value part of the trailer.
    * `key_value_separator=`_< sep>_: specify the separator inserted between the key and value of each trailer. Defaults to ": ". Otherwise it shares the same semantics as `separator=`_< sep>_ above.


Note |  Some placeholders may depend on other options given to the revision traversal engine. For example, the `%g*` reflog options will insert an empty string unless we are traversing reflog entries (e.g., by `git` `log` `-g`). The `%d` and `%D` placeholders will use the "short" decoration format if `--decorate` was not already provided on the command line.   
---|---  
The boolean options accept an optional value [`=`_< bool-value>_]. The values taken by `--type=bool` [git-config[1]](https://git-scm.com/docs/git-config), like `yes` and `off`, are all accepted. Giving a boolean option without `=`_< value>_ is equivalent to giving it with `=true`.
If you add a `+` (plus sign) after `%` of a placeholder, a line-feed is inserted immediately before the expansion if and only if the placeholder expands to a non-empty string.
If you add a `-` (minus sign) after `%` of a placeholder, all consecutive line-feeds immediately preceding the expansion are deleted if and only if the placeholder expands to an empty string.
If you add a `%` of a placeholder, a space is inserted immediately before the expansion if and only if the placeholder expands to a non-empty string.
  * `tformat:`
The `tformat:` format works exactly like `format:`, except that it provides "terminator" semantics instead of "separator" semantics. In other words, each commit has the message terminator character (usually a newline) appended, rather than a separator placed between entries. This means that the final entry of a single-line format will be properly terminated with a new line, just as the "oneline" format does. For example:
```
$ git log -2 --pretty=format:%h 4da45bef \
  | perl -pe '$_ .= " -- NO NEWLINE\n" unless /\n/'
4da45be
7134973 -- NO NEWLINE

$ git log -2 --pretty=tformat:%h 4da45bef \
  | perl -pe '$_ .= " -- NO NEWLINE\n" unless /\n/'
4da45be
7134973
```

In addition, any unrecognized string that has a `%` in it is interpreted as if it has `tformat:` in front of it. For example, these two are equivalent:
```
$ git log -2 --pretty=tformat:%h 4da45bef
$ git log -2 --pretty=%h 4da45bef
```



##  [](https://git-scm.com/docs/git-log#_diff_formatting)DIFF FORMATTING
By default, `git` `log` does not generate any diff output. The options below can be used to show the changes made by each commit.
Note that unless one of `--diff-merges` variants (including short `-m`, `-c`, `--cc`, and `--dd` options) is explicitly given, merge commits will not show a diff, even if a diff format like `--patch` is selected, nor will they match search options like `-S`. The exception is when `--first-parent` is in use, in which case `first-parent` is the default format for merge commits. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--p)`-p` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--u)`-u` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---patch)`--patch` 
    
Generate patch (see [Generating patch text with -p](https://git-scm.com/docs/git-log#generate_patch_text_with_p)). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--s)`-s` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-patch)`--no-patch` 
    
Suppress all output from the diff machinery. Useful for commands like `git` `show` that show the patch by default to squelch their output, or to cancel the effect of options like `--patch`, `--stat` earlier on the command line in an alias. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--m)`-m` 
    
Show diffs for merge commits in the default format. This is similar to `--diff-merges=on`, except `-m` will produce no output unless `-p` is given as well. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--c)`-c` 
    
Produce combined diff output for merge commits. Shortcut for `--diff-merges=combined` `-p`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---cc)`--cc` 
    
Produce dense combined diff output for merge commits. Shortcut for `--diff-merges=dense-combined` `-p`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dd)`--dd` 
    
Produce diff with respect to first parent for both merge and regular commits. Shortcut for `--diff-merges=first-parent` `-p`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---remerge-diff)`--remerge-diff` 
    
Produce remerge-diff output for merge commits. Shortcut for `--diff-merges=remerge` `-p`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-diff-merges)`--no-diff-merges` 
    
Synonym for `--diff-merges=off`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---diff-mergesformat)`--diff-merges=`_< format>_ 
    
Specify diff format to be used for merge commits. Default is `off` unless `--first-parent` is in use, in which case `first-parent` is the default.
The following formats are supported: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-off)`off` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-none)`none` 
    
Disable output of diffs for merge commits. Useful to override implied value. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-on)`on` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-m-1-1-1-1-1)`m` 
    
Make diff output for merge commits to be shown in the default format. The default format can be changed using `log.diffMerges` configuration variable, whose default value is `separate`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-first-parent)`first-parent` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-1)`1` 
    
Show full diff with respect to first parent. This is the same format as `--patch` produces for non-merge commits. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-separate)`separate` 
    
Show full diff with respect to each of parents. Separate log entry and diff is generated for each parent. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-combined)`combined` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-c)`c` 
    
Show differences from each of the parents to the merge result simultaneously instead of showing pairwise diff between a parent and the result one at a time. Furthermore, it lists only files which were modified from all parents. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-dense-combined)`dense-combined` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cc)`cc` 
    
Further compress output produced by `--diff-merges=combined` by omitting uninteresting hunks whose contents in the parents have only two variants and the merge result picks one of them without modification. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-remerge)`remerge` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-r)`r` 
    
Remerge two-parent merge commits to create a temporary tree object—​potentially containing files with conflict markers and such. A diff is then shown between that temporary tree and the actual merge commit.
The output emitted when this option is used is subject to change, and so is its interaction with other options (unless explicitly documented). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---combined-all-paths)`--combined-all-paths` 
    
Cause combined diffs (used for merge commits) to list the name of the file from all parents. It thus only has effect when `--diff-merges=`[`dense-`]`combined` is in use, and is likely only useful if filename changes are detected (i.e. when either rename or copy detection have been requested). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context instead of the usual three. Implies `--patch`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---outputfile)`--output=`_< file>_ 
    
Output to a specific file instead of stdout. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---output-indicator-newchar)`--output-indicator-new=`_< char>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---output-indicator-oldchar)`--output-indicator-old=`_< char>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---output-indicator-contextchar)`--output-indicator-context=`_< char>_ 
    
Specify the character used to indicate new, old or context lines in the generated patch. Normally they are `+`, `-` and ' ' respectively. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---raw)`--raw` 
    
For each commit, show a summary of changes using the raw diff format. See the "RAW OUTPUT FORMAT" section of [git-diff[1]](https://git-scm.com/docs/git-diff). This is different from showing the log itself in raw format, which you can achieve with `--format=raw`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---patch-with-raw)`--patch-with-raw` 
    
Synonym for `-p` `--raw`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--t)`-t` 
    
Show the tree objects in the diff output. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---indent-heuristic)`--indent-heuristic` 
    
Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-indent-heuristic)`--no-indent-heuristic` 
    
Disable the indent heuristic. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---minimal)`--minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---patience)`--patience` 
    
Generate a diff using the "patience diff" algorithm. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---histogram)`--histogram` 
    
Generate a diff using the "histogram diff" algorithm. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---anchoredtext)`--anchored=`_< text>_ 
    
Generate a diff using the "anchored diff" algorithm.
This option may be specified more than once.
If a line exists in both the source and destination, exists only once, and starts with _< text>_, this algorithm attempts to prevent it from appearing as a deletion or addition in the output. It uses the "patience diff" algorithm internally. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---diff-algorithmpatienceminimalhistogrammyers)`--diff-algorithm=`(`patience`|`minimal`|`histogram`|`myers`) 
    
Choose a diff algorithm. The variants are as follows: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-default)`default` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-myers)`myers` 
    
The basic greedy diff algorithm. Currently, this is the default. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-minimal)`minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-patience)`patience` 
    
Use "patience diff" algorithm when generating patches. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-histogram)`histogram` 
    
This algorithm extends the patience algorithm to "support low-occurrence common elements".
For instance, if you configured the `diff.algorithm` variable to a non-default value and want to use the default one, then you have to use `--diff-algorithm=default` option. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---statwidthname-widthcount)`--stat`[`=`_< width>_[`,`_< name-width>_[`,`_< count>_]]] 
    
Generate a diffstat. By default, as much space as necessary will be used for the filename part, and the rest for the graph part. Maximum width defaults to terminal width, or 80 columns if not connected to a terminal, and can be overridden by _< width>_. The width of the filename part can be limited by giving another width _< name-width>_ after a comma or by setting `diff.statNameWidth=`_< name-width>_. The width of the graph part can be limited by using `--stat-graph-width=`_< graph-width>_ or by setting `diff.statGraphWidth=`_< graph-width>_. Using `--stat` or `--stat-graph-width` affects all commands generating a stat graph, while setting `diff.statNameWidth` or `diff.statGraphWidth` does not affect `git` `format-patch`. By giving a third parameter _< count>_, you can limit the output to the first _< count>_ lines, followed by ... if there are more.
These parameters can also be set individually with `--stat-width=`_< width>_, `--stat-name-width=`_< name-width>_ and `--stat-count=`_< count>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---compact-summary)`--compact-summary` 
    
Output a condensed summary of extended header information such as file creations or deletions ("new" or "gone", optionally `+l` if it’s a symlink) and mode changes (`+x` or `-x` for adding or removing executable bit respectively) in diffstat. The information is put between the filename part and the graph part. Implies `--stat`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---numstat)`--numstat` 
    
Similar to `--stat`, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine friendly. For binary files, outputs two `-` instead of saying `0` `0`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---shortstat)`--shortstat` 
    
Output only the last line of the `--stat` format containing total number of modified files, as well as number of added and deleted lines. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Xparam)`-X` [_< param>_`,...`] 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dirstatparam)`--dirstat`[`=`_< param>_`,...`] 
    
Output the distribution of relative amount of changes for each sub-directory. The behavior of `--dirstat` can be customized by passing it a comma separated list of parameters. The defaults are controlled by the `diff.dirstat` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). The following parameters are available: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-changes)`changes` 
    
Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-lines)`lines` 
    
Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive `--dirstat` behavior than the `changes` behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other `--*stat` options. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-files)`files` 
    
Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest `--dirstat` behavior, since it does not have to look at the file contents at all. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-cumulative)`cumulative` 
    
Count changes in a child directory for the parent directory as well. Note that when using `cumulative`, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the `noncumulative` parameter. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-limit)_< limit>_ 
    
An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.
Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: `--dirstat=files,10,cumulative`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---cumulative)`--cumulative` 
    
Synonym for `--dirstat=cumulative`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dirstat-by-fileparam)`--dirstat-by-file`[`=`_< param>_`,...`] 
    
Synonym for `--dirstat=files,`_< param>_`,...`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---summary)`--summary` 
    
Output a condensed summary of extended header information such as creations, renames and mode changes. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---patch-with-stat)`--patch-with-stat` 
    
Synonym for `-p` `--stat`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--z)`-z` 
    
Separate the commits with _NUL_ s instead of newlines.
Also, when `--raw` or `--numstat` has been given, do not munge pathnames and use _NUL_ s as output field terminators.
Without this option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---name-only)`--name-only` 
    
Show only the name of each changed file in the post-image tree. The file names are often encoded in UTF-8. For more information see the discussion about encoding in the [git-log[1]](https://git-scm.com/docs/git-log) manual page. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---name-status)`--name-status` 
    
Show only the name(s) and status of each changed file. See the description of the `--diff-filter` option on what the status letters mean. Just like `--name-only` the file names are often encoded in UTF-8. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---submoduleformat)`--submodule`[`=`_< format>_] 
    
Specify how differences in submodules are shown. When specifying `--submodule=short` the `short` format is used. This format just shows the names of the commits at the beginning and end of the range. When `--submodule` or `--submodule=log` is specified, the `log` format is used. This format lists the commits in the range like [git-submodule[1]](https://git-scm.com/docs/git-submodule) `summary` does. When `--submodule=diff` is specified, the `diff` format is used. This format shows an inline diff of the changes in the submodule contents between the commit range. Defaults to `diff.submodule` or the `short` format if the config option is unset. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---colorwhen)`--color`[`=`_< when>_] 
    
Show colored diff. `--color` (i.e. without `=`_< when>_) is the same as `--color=always`. _< when>_ can be one of `always`, `never`, or `auto`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-color)`--no-color` 
    
Turn off colored diff. It is the same as `--color=never`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---color-movedmode)`--color-moved`[`=`_< mode>_] 
    
Moved lines of code are colored differently. The _< mode>_ defaults to `no` if the option is not given and to `zebra` if the option with no mode is given. The mode must be one of: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-no)`no` 
    
Moved lines are not highlighted. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-default-1)`default` 
    
Is a synonym for `zebra`. This may change to a more sensible mode in the future. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-plain)`plain` 
    
Any line that is added in one location and was removed in another location will be colored with `color.diff.newMoved`. Similarly `color.diff.oldMoved` will be used for removed lines that are added somewhere else in the diff. This mode picks up any moved line, but it is not very useful in a review to determine if a block of code was moved without permutation. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-blocks)`blocks` 
    
Blocks of moved text of at least 20 alphanumeric characters are detected greedily. The detected blocks are painted using either the `color.diff.`(`old`|`new`)`Moved` color. Adjacent blocks cannot be told apart. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-zebra)`zebra` 
    
Blocks of moved text are detected as in `blocks` mode. The blocks are painted using either the `color.diff.`(`old`|`new`)`Moved` color or `color.diff.`(`old`|`new`)`MovedAlternative`. The change between the two colors indicates that a new block was detected. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-dimmed-zebra)`dimmed-zebra` 
    
Similar to `zebra`, but additional dimming of uninteresting parts of moved code is performed. The bordering lines of two adjacent blocks are considered interesting, the rest is uninteresting. `dimmed_zebra` is a deprecated synonym. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-color-moved)`--no-color-moved` 
    
Turn off move detection. This can be used to override configuration settings. It is the same as `--color-moved=no`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---color-moved-wsmode)`--color-moved-ws=`_< mode>_`,...` 
    
This configures how whitespace is ignored when performing the move detection for `--color-moved`. These modes can be given as a comma separated list: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-no-1)`no` 
    
Do not ignore whitespace when performing move detection. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ignore-space-at-eol)`ignore-space-at-eol` 
    
Ignore changes in whitespace at EOL. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ignore-space-change)`ignore-space-change` 
    
Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-ignore-all-space)`ignore-all-space` 
    
Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-allow-indentation-change)`allow-indentation-change` 
    
Initially ignore any whitespace in the move detection, then group the moved code blocks only into a block if the change in whitespace is the same per line. This is incompatible with the other modes. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-color-moved-ws)`--no-color-moved-ws` 
    
Do not ignore whitespace when performing move detection. This can be used to override configuration settings. It is the same as `--color-moved-ws=no`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---word-diffmode)`--word-diff`[`=`_< mode>_] 
    
By default, words are delimited by whitespace; see `--word-diff-regex` below. The _< mode>_ defaults to `plain`, and must be one of: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-color)`color` 
    
Highlight changed words using only colors. Implies `--color`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-plain-1)`plain` 
    
Show words as [`-removed-`] and `{`added`}`. Makes no attempts to escape the delimiters if they appear in the input, so the output may be ambiguous. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-porcelain)`porcelain` 
    
Use a special line-based format intended for script consumption. Added/removed/unchanged runs are printed in the usual unified diff format, starting with a `+`/`-`/` ` character at the beginning of the line and extending to the end of the line. Newlines in the input are represented by a tilde `~` on a line of its own. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-none-1)`none` 
    
Disable word diff again.
Note that despite the name of the first mode, color is used to highlight the changed parts in all modes if enabled. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---word-diff-regexregex)`--word-diff-regex=`_< regex>_ 
    
Use _< regex>_ to decide what a word is, instead of considering runs of non-whitespace to be a word. Also implies `--word-diff` unless it was already enabled.
Every non-overlapping match of the _< regex>_ is considered a word. Anything between these matches is considered whitespace and ignored(!) for the purposes of finding differences. You may want to append |[`^`[`:space:`]] to your regular expression to make sure that it matches all non-whitespace characters. A match that contains a newline is silently truncated(!) at the newline.
For example, `--word-diff-regex=.` will treat each character as a word and, correspondingly, show differences character by character.
The regex can also be set via a diff driver or configuration option, see [gitattributes[5]](https://git-scm.com/docs/gitattributes) or [git-config[1]](https://git-scm.com/docs/git-config). Giving it explicitly overrides any diff driver or configuration setting. Diff drivers override configuration settings. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---color-wordsregex)`--color-words`[`=`_< regex>_] 
    
Equivalent to `--word-diff=color` plus (if a regex was specified) `--word-diff-regex=`_< regex>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-renames)`--no-renames` 
    
Turn off rename detection, even when the configuration file gives the default to do so. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---rename-empty)`--rename-empty` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-rename-empty)`--no-rename-empty` 
    
Whether to use empty blobs as rename source. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---check)`--check` 
    
Warn if changes introduce conflict markers or whitespace errors. What are considered whitespace errors is controlled by `core.whitespace` configuration. By default, trailing whitespaces (including lines that consist solely of whitespaces) and a space character that is immediately followed by a tab character inside the initial indent of the line are considered whitespace errors. Exits with non-zero status if problems are found. Not compatible with `--exit-code`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ws-error-highlightkind)`--ws-error-highlight=`_< kind>_ 
    
Highlight whitespace errors in the `context`, `old` or `new` lines of the diff. Multiple values are separated by comma, `none` resets previous values, `default` reset the list to `new` and `all` is a shorthand for `old,new,context`. When this option is not given, and the configuration variable `diff.wsErrorHighlight` is not set, only whitespace errors in `new` lines are highlighted. The whitespace errors are colored with `color.diff.whitespace`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---full-index)`--full-index` 
    
Instead of the first handful of characters, show the full pre- and post-image blob object names on the "index" line when generating patch format output. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---binary)`--binary` 
    
In addition to `--full-index`, output a binary diff that can be applied with `git-apply`. Implies `--patch`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---abbrevn)`--abbrev`[`=`_< n>_] 
    
Instead of showing the full 40-byte hexadecimal object name in diff-raw format output and diff-tree header lines, show the shortest prefix that is at least _< n>_ hexdigits long that uniquely refers the object. In diff-patch output format, `--full-index` takes higher precedence, i.e. if `--full-index` is specified, full blob names will be shown regardless of `--abbrev`. Non default number of digits can be specified with `--abbrev=`_< n>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Bnm)`-B`[_< n>_][`/`_< m>_] 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---break-rewritesnm)`--break-rewrites`[`=`[_< n>_][`/`_< m>_]] 
    
Break complete rewrite changes into pairs of delete and create. This serves two purposes:
It affects the way a change that amounts to a total rewrite of a file not as a series of deletion and insertion mixed together with a very few lines that happen to match textually as the context, but as a single deletion of everything old followed by a single insertion of everything new, and the number _< m>_ controls this aspect of the `-B` option (defaults to 60%). `-B/70%` specifies that less than 30% of the original should remain in the result for Git to consider it a total rewrite (i.e. otherwise the resulting patch will be a series of deletion and insertion mixed together with context lines).
When used with `-M`, a totally-rewritten file is also considered as the source of a rename (usually `-M` only considers a file that disappeared as the source of a rename), and the number _< n>_ controls this aspect of the `-B` option (defaults to 50%). `-B20%` specifies that a change with addition and deletion compared to 20% or more of the file’s size are eligible for being picked up as a possible source of a rename to another file. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Mn)`-M`[_< n>_] 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---find-renamesn)`--find-renames`[`=`_< n>_] 
    
If generating diffs, detect and report renames for each commit. For following files across renames while traversing history, see `--follow`. If _< n>_ is specified, it is a threshold on the similarity index (i.e. amount of addition/deletions compared to the file’s size). For example, `-M90%` means Git should consider a delete/add pair to be a rename if more than 90% of the file hasn’t changed. Without a `%` sign, the number is to be read as a fraction, with a decimal point before it. I.e., `-M5` becomes 0.5, and is thus the same as `-M50%`. Similarly, `-M05` is the same as `-M5%`. To limit detection to exact renames, use `-M100%`. The default similarity index is 50%. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Cn)`-C`[_< n>_] 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---find-copiesn)`--find-copies`[`=`_< n>_] 
    
Detect copies as well as renames. See also `--find-copies-harder`. If _< n>_ is specified, it has the same meaning as for `-M`_< n>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---find-copies-harder)`--find-copies-harder` 
    
For performance reasons, by default, `-C` option finds copies only if the original file of the copy was modified in the same changeset. This flag makes the command inspect unmodified files as candidates for the source of copy. This is a very expensive operation for large projects, so use it with caution. Giving more than one `-C` option has the same effect. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--D)`-D` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---irreversible-delete)`--irreversible-delete` 
    
Omit the preimage for deletes, i.e. print only the header but not the diff between the preimage and `/dev/null`. The resulting patch is not meant to be applied with `patch` or `git` `apply`; this is solely for people who want to just concentrate on reviewing the text after the change. In addition, the output obviously lacks enough information to apply such a patch in reverse, even manually, hence the name of the option.
When used together with `-B`, omit also the preimage in the deletion part of a delete/create pair. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--lnum)`-l`_< num>_ 
    
The `-M` and `-C` options involve some preliminary steps that can detect subsets of renames/copies cheaply, followed by an exhaustive fallback portion that compares all remaining unpaired destinations to all relevant sources. (For renames, only remaining unpaired sources are relevant; for copies, all original sources are relevant.) For N sources and destinations, this exhaustive check is O(N^2). This option prevents the exhaustive portion of rename/copy detection from running if the number of source/destination files involved exceeds the specified number. Defaults to `diff.renameLimit`. Note that a value of 0 is treated as unlimited. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---diff-filterACDMRTUXB)`--diff-filter=`[(`A`|`C`|`D`|`M`|`R`|`T`|`U`|`X`|`B`)`...`[`*`]] 
    
Select only files that are Added (`A`), Copied (`C`), Deleted (`D`), Modified (`M`), Renamed (`R`), have their type (i.e. regular file, symlink, submodule, …​) changed (`T`), are Unmerged (`U`), are Unknown (`X`), or have had their pairing Broken (`B`). Any combination of the filter characters (including none) can be used. When `*` (All-or-none) is added to the combination, all paths are selected if there is any file that matches other criteria in the comparison; if there is no file that matches other criteria, nothing is selected.
Also, these upper-case letters can be downcased to exclude. E.g. `--diff-filter=ad` excludes added and deleted paths.
Note that not all diffs can feature all types. For instance, copied and renamed entries cannot appear if detection for those types is disabled. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Sstring)`-S`_< string>_ 
    
Look for differences that change the number of occurrences of the specified _< string>_ (i.e. addition/deletion) in a file. Intended for the scripter’s use.
It is useful when you’re looking for an exact block of code (like a struct), and want to know the history of that block since it first came into being: use the feature iteratively to feed the interesting block in the preimage back into `-S`, and keep going until you get the very first version of the block.
Binary files are searched as well. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Gregex)`-G`_< regex>_ 
    
Look for differences whose patch text contains added/removed lines that match _< regex>_.
To illustrate the difference between `-S`_< regex>_ `--pickaxe-regex` and `-G`_< regex>_, consider a commit with the following diff in the same file:
```
+    return frotz(nitfol, two->ptr, 1, 0);
...
-    hit = frotz(nitfol, mf2.ptr, 1, 0);
```

While _git log -G"frotz\\(nitfol"_ will show this commit, _git log_ _-S"frotz\\(nitfol" --pickaxe-regex_ will not (because the number of occurrences of that string did not change).
Unless `--text` is supplied patches of binary files without a textconv filter will be ignored.
See the _pickaxe_ entry in [gitdiffcore[7]](https://git-scm.com/docs/gitdiffcore) for more information. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---find-objectobject-id)`--find-object=`_< object-id>_ 
    
Look for differences that change the number of occurrences of the specified object. Similar to `-S`, just the argument is different in that it doesn’t search for a specific string but for a specific object id.
The object can be a blob or a submodule commit. It implies the `-t` option in `git-log` to also find trees. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---pickaxe-all)`--pickaxe-all` 
    
When `-S` or `-G` finds a change, show all the changes in that changeset, not just the files that contain the change in _< string>_. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---pickaxe-regex)`--pickaxe-regex` 
    
Treat the _< string>_ given to `-S` as an extended POSIX regular expression to match. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Oorderfile)`-O`_< orderfile>_ 
    
Control the order in which files appear in the output. This overrides the `diff.orderFile` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). To cancel `diff.orderFile`, use `-O/dev/null`.
The output order is determined by the order of glob patterns in _< orderfile>_. All files with pathnames that match the first pattern are output first, all files with pathnames that match the second pattern (but not the first) are output next, and so on. All files with pathnames that do not match any pattern are output last, as if there was an implicit match-all pattern at the end of the file. If multiple pathnames have the same rank (they match the same pattern but no earlier patterns), their output order relative to each other is the normal order.
_< orderfile>_ is parsed as follows:
  * Blank lines are ignored, so they can be used as separators for readability.
  * Lines starting with a hash ("`#`") are ignored, so they can be used for comments. Add a backslash ("_\_ ") to the beginning of the pattern if it starts with a hash.
  * Each other line contains a single pattern.


Patterns have the same syntax and semantics as patterns used for `fnmatch`(3) without the `FNM_PATHNAME` flag, except a pathname also matches a pattern if removing any number of the final pathname components matches the pattern. For example, the pattern "`foo*bar`" matches "`fooasdfbar`" and "`foo/bar/baz/asdf`" but not "`foobarx`". 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---skip-tofile)`--skip-to=`_< file>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---rotate-tofile)`--rotate-to=`_< file>_ 
    
Discard the files before the named _< file>_ from the output (i.e. _skip to_), or move them to the end of the output (i.e. _rotate to_). These options were invented primarily for the use of the `git` `difftool` command, and may not be very useful otherwise. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--R)`-R` 
    
Swap two inputs; that is, show differences from index or on-disk file to tree contents. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---relativepath)`--relative`[`=`_< path>_] 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-relative)`--no-relative` 
    
When run from a subdirectory of the project, it can be told to exclude changes outside the directory and show pathnames relative to it with this option. When you are not in a subdirectory (e.g. in a bare repository), you can name which subdirectory to make the output relative to by giving a _< path>_ as an argument. `--no-relative` can be used to countermand both `diff.relative` config option and previous `--relative`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--a)`-a` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---text)`--text` 
    
Treat all files as text. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-cr-at-eol)`--ignore-cr-at-eol` 
    
Ignore carriage-return at the end of line when doing a comparison. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-space-at-eol)`--ignore-space-at-eol` 
    
Ignore changes in whitespace at EOL. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--b)`-b` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-space-change)`--ignore-space-change` 
    
Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--w)`-w` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-all-space)`--ignore-all-space` 
    
Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-blank-lines)`--ignore-blank-lines` 
    
Ignore changes whose lines are all blank. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--Iregex)`-I`_< regex>_ 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-matching-linesregex)`--ignore-matching-lines=`_< regex>_ 
    
Ignore changes whose all lines match _< regex>_. This option may be specified more than once. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---inter-hunk-contextnumber)`--inter-hunk-context=`_< number>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt--W)`-W` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---function-context)`--function-context` 
    
Show whole function as context lines for each change. The function names are determined in the same way as `git` `diff` works out patch hunk headers (see "Defining a custom hunk-header" in [gitattributes[5]](https://git-scm.com/docs/gitattributes)). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ext-diff)`--ext-diff` 
    
Allow an external diff helper to be executed. If you set an external diff driver with [gitattributes[5]](https://git-scm.com/docs/gitattributes), you need to use this option with [git-log[1]](https://git-scm.com/docs/git-log) and friends. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-ext-diff)`--no-ext-diff` 
    
Disallow external diff drivers. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---textconv)`--textconv` 


[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-textconv)`--no-textconv` 
    
Allow (or disallow) external text conversion filters to be run when comparing binary files. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. Because textconv filters are typically a one-way conversion, the resulting diff is suitable for human consumption, but cannot be applied. For this reason, textconv filters are enabled by default only for [git-diff[1]](https://git-scm.com/docs/git-diff) and [git-log[1]](https://git-scm.com/docs/git-log), but not for [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) or diff plumbing commands. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ignore-submodulesnoneuntrackeddirtyall)`--ignore-submodules`[`=`(`none`|`untracked`|`dirty`|`all`)] 
    
Ignore changes to submodules in the diff generation. `all` is the default. Using `none` will consider the submodule modified when it either contains untracked or modified files or its `HEAD` differs from the commit recorded in the superproject and can be used to override any settings of the `ignore` option in [git-config[1]](https://git-scm.com/docs/git-config) or [gitmodules[5]](https://git-scm.com/docs/gitmodules). When `untracked` is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using `dirty` ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior until 1.7.0). Using `all` hides all changes to submodules. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---src-prefixprefix)`--src-prefix=`_< prefix>_ 
    
Show the given source _< prefix>_ instead of "a/". 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---dst-prefixprefix)`--dst-prefix=`_< prefix>_ 
    
Show the given destination _< prefix>_ instead of "b/". 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---no-prefix)`--no-prefix` 
    
Do not show any source or destination prefix. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---default-prefix)`--default-prefix` 
    
Use the default source and destination prefixes ("a/" and "b/"). This overrides configuration variables such as `diff.noprefix`, `diff.srcPrefix`, `diff.dstPrefix`, and `diff.mnemonicPrefix` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---line-prefixprefix)`--line-prefix=`_< prefix>_ 
    
Prepend an additional _< prefix>_ to every line of output. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---ita-invisible-in-index)`--ita-invisible-in-index` 
    
By default entries added by `git` `add` `-N` appear as an existing empty file in `git` `diff` and a new file in `git` `diff` `--cached`. This option makes the entry appear as a new file in `git` `diff` and non-existent in `git` `diff` `--cached`. This option could be reverted with `--ita-visible-in-index`. Both options are experimental and could be removed in future. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt---max-depthdepth)--max-depth=<depth> 
    
For each pathspec given on command line, descend at most _< depth>_ levels of directories. A value of `-1` means no limit. Cannot be combined with wildcards in the pathspec. Given a tree containing `foo/bar/baz`, the following list shows the matches generated by each set of options:
  * `--max-depth=0` `--` `foo`: `foo`
  * `--max-depth=1` `--` `foo`: `foo/bar`
  * `--max-depth=1` `--` `foo/bar`: `foo/bar/baz`
  * `--max-depth=1` `--` `foo` `foo/bar`: `foo/bar/baz`
  * `--max-depth=2` `--` `foo`: `foo/bar/baz`


If no pathspec is given, the depth is measured as if all top-level entries were specified. Note that this is different than measuring from the root, in that `--max-depth=0` would still return `foo`. This allows you to still limit depth while asking for a subset of the top-level entries.
Note that this option is only supported for diffs between tree objects, not against the index or working tree.
For more detailed explanation on these common options, see also [gitdiffcore[7]](https://git-scm.com/docs/gitdiffcore).
##  [](https://git-scm.com/docs/git-log#generate_patch_text_with_p)Generating patch text with -p
Running [git-diff[1]](https://git-scm.com/docs/git-diff), [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), [git-diff-index[1]](https://git-scm.com/docs/git-diff-index), [git-diff-tree[1]](https://git-scm.com/docs/git-diff-tree), or [git-diff-files[1]](https://git-scm.com/docs/git-diff-files) with the `-p` option produces patch text. You can customize the creation of patch text via the `GIT_EXTERNAL_DIFF` and the `GIT_DIFF_OPTS` environment variables (see [git[1]](https://git-scm.com/docs/git)), and the `diff` attribute (see [gitattributes[5]](https://git-scm.com/docs/gitattributes)).
What the `-p` option produces is slightly different from the traditional diff format:
  1. It is preceded by a "git diff" header that looks like this:
```
diff --git a/file1 b/file2
```

The `a/` and `b/` filenames are the same unless rename/copy is involved. Especially, even for a creation or a deletion, `/dev/null` is _not_ used in place of the `a/` or `b/` filenames.
When a rename/copy is involved, `file1` and `file2` show the name of the source file of the rename/copy and the name of the file that the rename/copy produces, respectively.
  2. It is followed by one or more extended header lines:
```
old mode _<mode>_
new mode _<mode>_
deleted file mode _<mode>_
new file mode _<mode>_
copy from _<path>_
copy to _<path>_
rename from _<path>_
rename to _<path>_
similarity index _<number>_
dissimilarity index _<number>_
index _<hash>_.._<hash>_ _<mode>_
```

File modes _< mode>_ are printed as 6-digit octal numbers including the file type and file permission bits.
Path names in extended headers do not include the `a/` and `b/` prefixes.
The similarity index is the percentage of unchanged lines, and the dissimilarity index is the percentage of changed lines. It is a rounded down integer, followed by a percent sign. The similarity index value of 100% is thus reserved for two equal files, while 100% dissimilarity means that no line from the old file made it into the new one.
The index line includes the blob object names before and after the change. The _< mode>_ is included if the file mode does not change; otherwise, separate lines indicate the old and the new mode.
  3. Pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)).
  4. All the `file1` files in the output refer to files before the commit, and all the `file2` files refer to files after the commit. It is incorrect to apply each change to each file sequentially. For example, this patch will swap a and b:
```
diff --git a/a b/b
rename from a
rename to b
diff --git a/b b/a
rename from b
rename to a
```

  5. Hunk headers mention the name of the function to which the hunk applies. See "Defining a custom hunk-header" in [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details of how to tailor this to specific languages.


##  [](https://git-scm.com/docs/git-log#_combined_diff_format)Combined diff format
Any diff-generating command can take the `-c` or `--cc` option to produce a _combined diff_ when showing a merge. This is the default format when showing merges with [git-diff[1]](https://git-scm.com/docs/git-diff) or [git-show[1]](https://git-scm.com/docs/git-show). Note also that you can give suitable `--diff-merges` option to any of these commands to force generation of diffs in a specific format.
A "combined diff" format looks like this:
```
diff --combined describe.c
index fabadb8,cc95eb0..4866510
--- a/describe.c
+++ b/describe.c
@@@ -98,20 -98,12 +98,20 @@@
	return (a_date > b_date) ? -1 : (a_date == b_date) ? 0 : 1;
  }

- static void describe(char *arg)
 -static void describe(struct commit *cmit, int last_one)
++static void describe(char *arg, int last_one)
  {
 +	unsigned char sha1[20];
 +	struct commit *cmit;
	struct commit_list *list;
	static int initialized = 0;
	struct commit_name *n;

 +	if (get_sha1(arg, sha1) < 0)
 +		usage(describe_usage);
 +	cmit = lookup_commit_reference(sha1);
 +	if (!cmit)
 +		usage(describe_usage);
 +
	if (!initialized) {
		initialized = 1;
		for_each_ref(get_name);
```

  1. It is preceded by a "git diff" header, that looks like this (when the `-c` option is used):
```
diff --combined file
```

or like this (when the `--cc` option is used):
```
diff --cc file
```

  2. It is followed by one or more extended header lines (this example shows a merge with two parents):
```
index _<hash>_,_<hash>_.._<hash>_
mode _<mode>_,_<mode>_.._<mode>_
new file mode _<mode>_
deleted file mode _<mode>_,_<mode>_
```

The `mode` _< mode>_`,`_< mode>_`..`_< mode>_ line appears only if at least one of the <mode> is different from the rest. Extended headers with information about detected content movement (renames and copying detection) are designed to work with the diff of two _< tree-ish>_ and are not used by combined diff format.
  3. It is followed by a two-line from-file/to-file header:
```
--- a/file
+++ b/file
```

Similar to the two-line header for the traditional _unified_ diff format, `/dev/null` is used to signal created or deleted files.
However, if the --combined-all-paths option is provided, instead of a two-line from-file/to-file, you get an N+1 line from-file/to-file header, where N is the number of parents in the merge commit:
```
--- a/file
--- a/file
--- a/file
+++ b/file
```

This extended format can be useful if rename or copy detection is active, to allow you to see the original name of the file in different parents.
  4. Chunk header format is modified to prevent people from accidentally feeding it to `patch` `-p1`. Combined diff format was created for review of merge commit changes, and was not meant to be applied. The change is similar to the change in the extended _index_ header:
```
@@@ <from-file-range> <from-file-range> <to-file-range> @@@
```

There are (number of parents + 1) `@` characters in the chunk header for combined diff format.


Unlike the traditional _unified_ diff format, which shows two files A and B with a single column that has `-` (minus — appears in A but removed in B), `+` (plus — missing in A but added to B), or `"` `"` (space — unchanged) prefix, this format compares two or more files file1, file2,…​ with one file X, and shows how X differs from each of fileN. One column for each of fileN is prepended to the output line to note how X’s line is different from it.
A `-` character in the column N means that the line appears in fileN but it does not appear in the result. A `+` character in the column N means that the line appears in the result, and fileN does not have that line (in other words, the line was added, from the point of view of that parent).
In the above example output, the function signature was changed from both files (hence two `-` removals from both file1 and file2, plus `++` to mean one line that was added does not appear in either file1 or file2). Also, eight other lines are the same from file1 but do not appear in file2 (hence prefixed with `+`).
When shown by `git` `diff-tree` `-c`, it compares the parents of a merge commit with the merge result (i.e. file1..fileN are the parents). When shown by `git` `diff-files` `-c`, it compares the two unresolved merge parents with the working tree file (i.e. file1 is stage 2 aka "our version", file2 is stage 3 aka "their version").
##  [](https://git-scm.com/docs/git-log#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog--no-merges)`git` `log` `--no-merges` 
    
Show the whole commit history, but skip any merges 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlogv2612includescsidriversscsi)`git` `log` `v2.6.12..` `include/scsi` `drivers/scsi` 
    
Show all commits since version _v2.6.12_ that changed any file in the `include/scsi` or `drivers/scsi` subdirectories 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog--since2weeksago--gitk)`git` `log` `--since="2` `weeks` `ago"` `--` `gitk` 
    
Show the changes during the last two weeks to the file `gitk`. The `--` is necessary to avoid confusion with the **branch** named `gitk` 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog--name-statusreleasetest)`git` `log` `--name-status` `release..test` 
    
Show the commits that are in the "`test`" branch but not yet in the "`release`" branch, along with the list of paths each commit modifies. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog--followbuiltinrev-listc)`git` `log` `--follow` `builtin/rev-list.c` 
    
Shows the commits that changed `builtin/rev-list.c`, including those commits that occurred before the file was given its present name. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog--branches--not--remotesorigin)`git` `log` `--branches` `--not` `--remotes=origin` 
    
Shows all commits that are in any of local branches but not in any of remote-tracking branches for `origin` (what you have that origin doesn’t). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlogmaster--not--remotesmaster)`git` `log` `master` `--not` `--remotes=*/master` 
    
Shows all commits that are in local master but not in any remote repository master branches. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog-p-m--first-parent)`git` `log` `-p` `-m` `--first-parent` 
    
Shows the history including change diffs, but only from the “main branch” perspective, skipping commits that come from merged branches, and showing full diffs of changes introduced by the merges. This makes sense only when following a strict policy of merging all topic branches when staying on a single integration branch. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog-Lintmainmainc)`git` `log` `-L` `/int` `main/',/^}/:main.c` 
    
Shows how the function `main`() in the file `main.c` evolved over time. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-gitlog-3)`git` `log` `-3` 
    
Limits the number of commits to show to 3.
##  [](https://git-scm.com/docs/git-log#_discussion)DISCUSSION
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
##  [](https://git-scm.com/docs/git-log#_configuration)CONFIGURATION
See [git-config[1]](https://git-scm.com/docs/git-config) for core variables and [git-diff[1]](https://git-scm.com/docs/git-diff) for settings related to diff generation. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-formatpretty)`format.pretty` 
    
Default for the `--format` option. (See _Pretty Formats_ above.) Defaults to `medium`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-i18nlogOutputEncoding)`i18n.logOutputEncoding` 
    
Encoding to use when displaying logs. (See _Discussion_ above.) Defaults to the value of `i18n.commitEncoding` if set, and UTF-8 otherwise.
Everything above this line in this section isn’t included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content that follows is the same as what’s found there: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logabbrevCommit)`log.abbrevCommit` 
    
If `true`, make [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), and [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged) assume `--abbrev-commit`. You may override this option with `--no-abbrev-commit`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logdate)`log.date` 
    
Set the default date-time mode for the `log` command. Setting a value for log.date is similar to using `git` `log`'s `--date` option. See [git-log[1]](https://git-scm.com/docs/git-log) for details.
If the format is set to "auto:foo" and the pager is in use, format "foo" will be used for the date format. Otherwise, "default" will be used. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logdecorate)`log.decorate` 
    
Print out the ref names of any commits that are shown by the log command. Possible values are: 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-short)`short` 
    
the ref name prefixes `refs/heads/`, `refs/tags/` and `refs/remotes/` are not printed. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-full)`full` 
    
the full ref name (including prefix) are printed. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-auto)`auto` 
    
if the output is going to a terminal, the ref names are shown as if `short` were given, otherwise no ref names are shown.
This is the same as the `--decorate` option of the `git` `log`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-loginitialDecorationSet)`log.initialDecorationSet` 
    
By default, `git` `log` only shows decorations for certain known ref namespaces. If _all_ is specified, then show all refs as decorations. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logexcludeDecoration)`log.excludeDecoration` 
    
Exclude the specified patterns from the log decorations. This is similar to the `--decorate-refs-exclude` command-line option, but the config option can be overridden by the `--decorate-refs` option. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logdiffMerges)`log.diffMerges` 
    
Set diff format to be used when `--diff-merges=on` is specified, see `--diff-merges` in [git-log[1]](https://git-scm.com/docs/git-log) for details. Defaults to `separate`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logfollow)`log.follow` 
    
If `true`, `git` `log` will act as if the `--follow` option was used when a single <path> is given. This has the same limitations as `--follow`, i.e. it cannot be used to follow multiple files and does not work well on non-linear history. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-loggraphColors)`log.graphColors` 
    
A list of colors, separated by commas, that can be used to draw history lines in `git` `log` `--graph`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logshowRoot)`log.showRoot` 
    
If true, the initial commit will be shown as a big creation event. This is equivalent to a diff against an empty tree. Tools like [git-log[1]](https://git-scm.com/docs/git-log) or [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged), which normally hide the root commit will now show it. True by default. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logshowSignature)`log.showSignature` 
    
If true, makes [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), and [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged) assume `--show-signature`. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-logmailmap)`log.mailmap` 
    
If true, makes [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), and [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged) assume `--use-mailmap`, otherwise assume `--no-use-mailmap`. True by default. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-notesmergeStrategy)`notes.mergeStrategy` 
    
Which merge strategy to choose by default when resolving notes conflicts. Must be one of `manual`, `ours`, `theirs`, `union`, or `cat_sort_uniq`. Defaults to `manual`. See the "NOTES MERGE STRATEGIES" section of [git-notes[1]](https://git-scm.com/docs/git-notes) for more information on each strategy.
This setting can be overridden by passing the `--strategy` option to [git-notes[1]](https://git-scm.com/docs/git-notes). 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-notesnamemergeStrategy)`notes.`_< name>_`.mergeStrategy` 
    
Which merge strategy to choose when doing a notes merge into `refs/notes/`_< name>_. This overrides the more general `notes.mergeStrategy`. See the "NOTES MERGE STRATEGIES" section in [git-notes[1]](https://git-scm.com/docs/git-notes) for more information on the available strategies. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-notesdisplayRef)`notes.displayRef` 
    
Which ref (or refs, if a glob or specified more than once), in addition to the default set by `core.notesRef` or `GIT_NOTES_REF`, to read notes from when showing commit messages with the `git` `log` family of commands.
This setting can be overridden with the `GIT_NOTES_DISPLAY_REF` environment variable, which must be a colon separated list of refs or globs.
A warning will be issued for refs that do not exist, but a glob that does not match any refs is silently ignored.
This setting can be disabled by the `--no-notes` option to the [git-log[1]](https://git-scm.com/docs/git-log) family of commands, or by the `--notes=`_< ref>_ option accepted by those commands.
The effective value of `core.notesRef` (possibly overridden by `GIT_NOTES_REF`) is also implicitly added to the list of refs to be displayed. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-notesrewritecommand)`notes.rewrite.`_< command>_ 
    
When rewriting commits with _< command>_ (currently `amend` or `rebase`), if this variable is `false`, git will not copy notes from the original to the rewritten commit. Defaults to `true`. See also `notes.rewriteRef` below.
This setting can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable, which must be a colon separated list of refs or globs. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-notesrewriteMode)`notes.rewriteMode` 
    
When copying notes during a rewrite (see the `notes.rewrite.`_< command>_ option), determines what to do if the target commit already has a note. Must be one of `overwrite`, `concatenate`, `cat_sort_uniq`, or `ignore`. Defaults to `concatenate`.
This setting can be overridden with the `GIT_NOTES_REWRITE_MODE` environment variable. 

[](https://git-scm.com/docs/git-log#Documentation/git-log.txt-notesrewriteRef)`notes.rewriteRef` 
    
When copying notes during a rewrite, specifies the (fully qualified) ref whose notes should be copied. May be a glob, in which case notes in all matching refs will be copied. You may also specify this configuration several times.
Does not have a default value; you must configure this variable to enable note rewriting. Set it to `refs/notes/commits` to enable rewriting for the default commit notes.
Can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable. See `notes.rewrite.`_< command>_ above for a further description of its format.
##  [](https://git-scm.com/docs/git-log#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### log
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
