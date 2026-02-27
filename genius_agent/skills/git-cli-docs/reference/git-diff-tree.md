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
    * [NAME](https://git-scm.com/docs/git-diff-tree#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-diff-tree#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-diff-tree#_description)
    * [OPTIONS](https://git-scm.com/docs/git-diff-tree#_options)
    * [PRETTY FORMATS](https://git-scm.com/docs/git-diff-tree#_pretty_formats)
    * [Raw output format](https://git-scm.com/docs/git-diff-tree#_raw_output_format)
    * [diff format for merges](https://git-scm.com/docs/git-diff-tree#_diff_format_for_merges)
    * [Generating patch text with -p](https://git-scm.com/docs/git-diff-tree#generate_patch_text_with_p)
    * [Combined diff format](https://git-scm.com/docs/git-diff-tree#_combined_diff_format)
    * [other diff formats](https://git-scm.com/docs/git-diff-tree#_other_diff_formats)
    * [GIT](https://git-scm.com/docs/git-diff-tree#_git)


[ English ▾](https://git-scm.com/docs/git-diff-tree)
Localized versions of **git-diff-tree** manual
  1. [English ](https://git-scm.com/docs/git-diff-tree)
  2. [Français ](https://git-scm.com/docs/git-diff-tree/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-diff-tree/pt_BR)
  4. [Русский ](https://git-scm.com/docs/git-diff-tree/ru)
  5. [Svenska ](https://git-scm.com/docs/git-diff-tree/sv)
  6. [українська мова ](https://git-scm.com/docs/git-diff-tree/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-diff-tree/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-diff-tree)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-diff-tree) git-diff-tree last updated in 2.53.0
Changes in the **git-diff-tree** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-diff-tree/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-diff-tree/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-diff-tree/2.51.1)
  5. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-diff-tree/2.51.0)
  6. 2.49.1 → 2.50.1 no changes
  7. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-diff-tree/2.49.0)
  8. 2.48.1 → 2.48.2 no changes
  9. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-diff-tree/2.48.0)
  10. 2.46.2 → 2.47.3 no changes
  11. [2.46.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-13_ ](https://git-scm.com/docs/git-diff-tree/2.46.1)
  12. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-diff-tree/2.46.0)
  13. 2.45.4 no changes
  14. [2.45.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-diff-tree/2.45.3)
  15. 2.45.1 → 2.45.2 no changes
  16. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-diff-tree/2.45.0)
  17. 2.44.1 → 2.44.4 no changes
  18. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-diff-tree/2.44.0)
  19. 2.43.1 → 2.43.7 no changes
  20. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-diff-tree/2.43.0)
  21. 2.42.2 → 2.42.4 no changes
  22. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-diff-tree/2.42.1)
  23. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-diff-tree/2.42.0)
  24. 2.41.1 → 2.41.3 no changes
  25. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-diff-tree/2.41.0)
  26. 2.40.1 → 2.40.4 no changes
  27. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-diff-tree/2.40.0)
  28. 2.37.3 → 2.39.5 no changes
  29. [2.37.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-08-11_ ](https://git-scm.com/docs/git-diff-tree/2.37.2)
  30. 2.36.1 → 2.37.1 no changes
  31. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-diff-tree/2.36.0)
  32. 2.35.1 → 2.35.8 no changes
  33. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-diff-tree/2.35.0)
  34. 2.34.1 → 2.34.8 no changes
  35. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-diff-tree/2.34.0)
  36. 2.33.3 → 2.33.8 no changes
  37. [2.33.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-diff-tree/2.33.2)
  38. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git-diff-tree/2.33.1)
  39. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-diff-tree/2.33.0)
  40. 2.32.1 → 2.32.7 no changes
  41. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-diff-tree/2.32.0)
  42. 2.31.1 → 2.31.8 no changes
  43. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-diff-tree/2.31.0)
  44. 2.30.1 → 2.30.9 no changes
  45. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-diff-tree/2.30.0)
  46. 2.29.1 → 2.29.3 no changes
  47. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-diff-tree/2.29.0)
  48. 2.28.1 no changes
  49. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-diff-tree/2.28.0)
  50. 2.27.1 no changes
  51. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-diff-tree/2.27.0)
  52. 2.26.1 → 2.26.3 no changes
  53. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-diff-tree/2.26.0)
  54. 2.25.2 → 2.25.5 no changes
  55. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-diff-tree/2.25.1)
  56. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-diff-tree/2.25.0)
  57. 2.24.1 → 2.24.4 no changes
  58. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-diff-tree/2.24.0)
  59. 2.22.1 → 2.23.4 no changes
  60. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-diff-tree/2.22.0)
  61. 2.21.1 → 2.21.4 no changes
  62. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-diff-tree/2.21.0)
  63. 2.20.1 → 2.20.5 no changes
  64. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-diff-tree/2.20.0)
  65. 2.19.1 → 2.19.6 no changes
  66. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-diff-tree/2.19.0)
  67. 2.18.1 → 2.18.5 no changes
  68. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-diff-tree/2.18.0)
  69. 2.17.1 → 2.17.6 no changes
  70. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-diff-tree/2.17.0)
  71. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-diff-tree/2.16.6)
  72. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-diff-tree/2.15.4)
  73. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-diff-tree/2.14.6)
  74. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-diff-tree/2.13.7)
  75. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-diff-tree/2.12.5)
  76. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-diff-tree/2.11.4)
  77. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-diff-tree/2.10.5)
  78. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-diff-tree/2.9.5)
  79. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-diff-tree/2.8.6)
  80. 2.7.6 no changes
  81. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-diff-tree/2.6.7)
  82. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-diff-tree/2.5.6)
  83. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-diff-tree/2.4.12)
  84. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-diff-tree/2.3.10)
  85. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-diff-tree/2.2.3)
  86. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-diff-tree/2.1.4)
  87. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-diff-tree/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-diff-tree#_name)NAME
git-diff-tree - Compares the content and mode of blobs found via two tree objects
##  [](https://git-scm.com/docs/git-diff-tree#_synopsis)SYNOPSIS
```
_git diff-tree_ [--stdin] [-m] [-s] [-v] [--no-commit-id] [--pretty]
	      [-t] [-r] [-c | --cc] [--combined-all-paths] [--root] [--merge-base]
	      [<common-diff-options>] <tree-ish> [<tree-ish>] [<path>…​]
```

##  [](https://git-scm.com/docs/git-diff-tree#_description)DESCRIPTION
Compare the content and mode of blobs found via two tree objects.
If there is only one <tree-ish> given, the commit is compared with its parents (see --stdin below).
Note that _git diff-tree_ can use the tree encapsulated in a commit object.
##  [](https://git-scm.com/docs/git-diff-tree#_options)OPTIONS 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--p)`-p` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--u)`-u` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---patch)`--patch` 
    
Generate patch (see [Generating patch text with -p](https://git-scm.com/docs/git-diff-tree#generate_patch_text_with_p)). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--s)`-s` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-patch)`--no-patch` 
    
Suppress all output from the diff machinery. Useful for commands like `git` `show` that show the patch by default to squelch their output, or to cancel the effect of options like `--patch`, `--stat` earlier on the command line in an alias. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context instead of the usual three. Implies `--patch`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---outputfile)`--output=`_< file>_ 
    
Output to a specific file instead of stdout. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---output-indicator-newchar)`--output-indicator-new=`_< char>_ 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---output-indicator-oldchar)`--output-indicator-old=`_< char>_ 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---output-indicator-contextchar)`--output-indicator-context=`_< char>_ 
    
Specify the character used to indicate new, old or context lines in the generated patch. Normally they are `+`, `-` and ' ' respectively. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---raw)`--raw` 
    
Generate the diff in raw format. This is the default. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---patch-with-raw)`--patch-with-raw` 
    
Synonym for `-p` `--raw`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---indent-heuristic)`--indent-heuristic` 
    
Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-indent-heuristic)`--no-indent-heuristic` 
    
Disable the indent heuristic. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---minimal)`--minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---patience)`--patience` 
    
Generate a diff using the "patience diff" algorithm. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---histogram)`--histogram` 
    
Generate a diff using the "histogram diff" algorithm. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---anchoredtext)`--anchored=`_< text>_ 
    
Generate a diff using the "anchored diff" algorithm.
This option may be specified more than once.
If a line exists in both the source and destination, exists only once, and starts with _< text>_, this algorithm attempts to prevent it from appearing as a deletion or addition in the output. It uses the "patience diff" algorithm internally. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---diff-algorithmpatienceminimalhistogrammyers)`--diff-algorithm=`(`patience`|`minimal`|`histogram`|`myers`) 
    
Choose a diff algorithm. The variants are as follows: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-default)`default` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-myers)`myers` 
    
The basic greedy diff algorithm. Currently, this is the default. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-minimal)`minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-patience)`patience` 
    
Use "patience diff" algorithm when generating patches. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-histogram)`histogram` 
    
This algorithm extends the patience algorithm to "support low-occurrence common elements".
For instance, if you configured the `diff.algorithm` variable to a non-default value and want to use the default one, then you have to use `--diff-algorithm=default` option. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---statwidthname-widthcount)`--stat`[`=`_< width>_[`,`_< name-width>_[`,`_< count>_]]] 
    
Generate a diffstat. By default, as much space as necessary will be used for the filename part, and the rest for the graph part. Maximum width defaults to terminal width, or 80 columns if not connected to a terminal, and can be overridden by _< width>_. The width of the filename part can be limited by giving another width _< name-width>_ after a comma or by setting `diff.statNameWidth=`_< name-width>_. The width of the graph part can be limited by using `--stat-graph-width=`_< graph-width>_ or by setting `diff.statGraphWidth=`_< graph-width>_. Using `--stat` or `--stat-graph-width` affects all commands generating a stat graph, while setting `diff.statNameWidth` or `diff.statGraphWidth` does not affect `git` `format-patch`. By giving a third parameter _< count>_, you can limit the output to the first _< count>_ lines, followed by ... if there are more.
These parameters can also be set individually with `--stat-width=`_< width>_, `--stat-name-width=`_< name-width>_ and `--stat-count=`_< count>_. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---compact-summary)`--compact-summary` 
    
Output a condensed summary of extended header information such as file creations or deletions ("new" or "gone", optionally `+l` if it’s a symlink) and mode changes (`+x` or `-x` for adding or removing executable bit respectively) in diffstat. The information is put between the filename part and the graph part. Implies `--stat`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---numstat)`--numstat` 
    
Similar to `--stat`, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine friendly. For binary files, outputs two `-` instead of saying `0` `0`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---shortstat)`--shortstat` 
    
Output only the last line of the `--stat` format containing total number of modified files, as well as number of added and deleted lines. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Xparam)`-X` [_< param>_`,...`] 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---dirstatparam)`--dirstat`[`=`_< param>_`,...`] 
    
Output the distribution of relative amount of changes for each sub-directory. The behavior of `--dirstat` can be customized by passing it a comma separated list of parameters. The defaults are controlled by the `diff.dirstat` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). The following parameters are available: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-changes)`changes` 
    
Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-lines)`lines` 
    
Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive `--dirstat` behavior than the `changes` behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other `--*stat` options. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-files)`files` 
    
Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest `--dirstat` behavior, since it does not have to look at the file contents at all. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cumulative)`cumulative` 
    
Count changes in a child directory for the parent directory as well. Note that when using `cumulative`, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the `noncumulative` parameter. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-limit)_< limit>_ 
    
An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.
Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: `--dirstat=files,10,cumulative`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---cumulative)`--cumulative` 
    
Synonym for `--dirstat=cumulative`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---dirstat-by-fileparam)`--dirstat-by-file`[`=`_< param>_`,...`] 
    
Synonym for `--dirstat=files,`_< param>_`,...`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---summary)`--summary` 
    
Output a condensed summary of extended header information such as creations, renames and mode changes. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---patch-with-stat)`--patch-with-stat` 
    
Synonym for `-p` `--stat`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--z)`-z` 
    
When `--raw`, `--numstat`, `--name-only` or `--name-status` has been given, do not munge pathnames and use NULs as output field terminators.
Without this option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---name-only)`--name-only` 
    
Show only the name of each changed file in the post-image tree. The file names are often encoded in UTF-8. For more information see the discussion about encoding in the [git-log[1]](https://git-scm.com/docs/git-log) manual page. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---name-status)`--name-status` 
    
Show only the name(s) and status of each changed file. See the description of the `--diff-filter` option on what the status letters mean. Just like `--name-only` the file names are often encoded in UTF-8. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---submoduleformat)`--submodule`[`=`_< format>_] 
    
Specify how differences in submodules are shown. When specifying `--submodule=short` the `short` format is used. This format just shows the names of the commits at the beginning and end of the range. When `--submodule` or `--submodule=log` is specified, the `log` format is used. This format lists the commits in the range like [git-submodule[1]](https://git-scm.com/docs/git-submodule) `summary` does. When `--submodule=diff` is specified, the `diff` format is used. This format shows an inline diff of the changes in the submodule contents between the commit range. Defaults to `diff.submodule` or the `short` format if the config option is unset. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---colorwhen)`--color`[`=`_< when>_] 
    
Show colored diff. `--color` (i.e. without `=`_< when>_) is the same as `--color=always`. _< when>_ can be one of `always`, `never`, or `auto`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-color)`--no-color` 
    
Turn off colored diff. It is the same as `--color=never`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---color-movedmode)`--color-moved`[`=`_< mode>_] 
    
Moved lines of code are colored differently. The _< mode>_ defaults to `no` if the option is not given and to `zebra` if the option with no mode is given. The mode must be one of: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-no)`no` 
    
Moved lines are not highlighted. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-default-1)`default` 
    
Is a synonym for `zebra`. This may change to a more sensible mode in the future. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-plain)`plain` 
    
Any line that is added in one location and was removed in another location will be colored with `color.diff.newMoved`. Similarly `color.diff.oldMoved` will be used for removed lines that are added somewhere else in the diff. This mode picks up any moved line, but it is not very useful in a review to determine if a block of code was moved without permutation. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-blocks)`blocks` 
    
Blocks of moved text of at least 20 alphanumeric characters are detected greedily. The detected blocks are painted using either the `color.diff.`(`old`|`new`)`Moved` color. Adjacent blocks cannot be told apart. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-zebra)`zebra` 
    
Blocks of moved text are detected as in `blocks` mode. The blocks are painted using either the `color.diff.`(`old`|`new`)`Moved` color or `color.diff.`(`old`|`new`)`MovedAlternative`. The change between the two colors indicates that a new block was detected. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-dimmed-zebra)`dimmed-zebra` 
    
Similar to `zebra`, but additional dimming of uninteresting parts of moved code is performed. The bordering lines of two adjacent blocks are considered interesting, the rest is uninteresting. `dimmed_zebra` is a deprecated synonym. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-color-moved)`--no-color-moved` 
    
Turn off move detection. This can be used to override configuration settings. It is the same as `--color-moved=no`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---color-moved-wsmode)`--color-moved-ws=`_< mode>_`,...` 
    
This configures how whitespace is ignored when performing the move detection for `--color-moved`. These modes can be given as a comma separated list: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-no-1)`no` 
    
Do not ignore whitespace when performing move detection. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ignore-space-at-eol)`ignore-space-at-eol` 
    
Ignore changes in whitespace at EOL. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ignore-space-change)`ignore-space-change` 
    
Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ignore-all-space)`ignore-all-space` 
    
Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-allow-indentation-change)`allow-indentation-change` 
    
Initially ignore any whitespace in the move detection, then group the moved code blocks only into a block if the change in whitespace is the same per line. This is incompatible with the other modes. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-color-moved-ws)`--no-color-moved-ws` 
    
Do not ignore whitespace when performing move detection. This can be used to override configuration settings. It is the same as `--color-moved-ws=no`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---word-diffmode)`--word-diff`[`=`_< mode>_] 
    
By default, words are delimited by whitespace; see `--word-diff-regex` below. The _< mode>_ defaults to `plain`, and must be one of: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-color)`color` 
    
Highlight changed words using only colors. Implies `--color`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-plain-1)`plain` 
    
Show words as [`-removed-`] and `{`added`}`. Makes no attempts to escape the delimiters if they appear in the input, so the output may be ambiguous. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-porcelain)`porcelain` 
    
Use a special line-based format intended for script consumption. Added/removed/unchanged runs are printed in the usual unified diff format, starting with a `+`/`-`/` ` character at the beginning of the line and extending to the end of the line. Newlines in the input are represented by a tilde `~` on a line of its own. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-none)`none` 
    
Disable word diff again.
Note that despite the name of the first mode, color is used to highlight the changed parts in all modes if enabled. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---word-diff-regexregex)`--word-diff-regex=`_< regex>_ 
    
Use _< regex>_ to decide what a word is, instead of considering runs of non-whitespace to be a word. Also implies `--word-diff` unless it was already enabled.
Every non-overlapping match of the _< regex>_ is considered a word. Anything between these matches is considered whitespace and ignored(!) for the purposes of finding differences. You may want to append |[`^`[`:space:`]] to your regular expression to make sure that it matches all non-whitespace characters. A match that contains a newline is silently truncated(!) at the newline.
For example, `--word-diff-regex=.` will treat each character as a word and, correspondingly, show differences character by character.
The regex can also be set via a diff driver or configuration option, see [gitattributes[5]](https://git-scm.com/docs/gitattributes) or [git-config[1]](https://git-scm.com/docs/git-config). Giving it explicitly overrides any diff driver or configuration setting. Diff drivers override configuration settings. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---color-wordsregex)`--color-words`[`=`_< regex>_] 
    
Equivalent to `--word-diff=color` plus (if a regex was specified) `--word-diff-regex=`_< regex>_. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-renames)`--no-renames` 
    
Turn off rename detection, even when the configuration file gives the default to do so. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---rename-empty)`--rename-empty` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-rename-empty)`--no-rename-empty` 
    
Whether to use empty blobs as rename source. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---check)`--check` 
    
Warn if changes introduce conflict markers or whitespace errors. What are considered whitespace errors is controlled by `core.whitespace` configuration. By default, trailing whitespaces (including lines that consist solely of whitespaces) and a space character that is immediately followed by a tab character inside the initial indent of the line are considered whitespace errors. Exits with non-zero status if problems are found. Not compatible with `--exit-code`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ws-error-highlightkind)`--ws-error-highlight=`_< kind>_ 
    
Highlight whitespace errors in the `context`, `old` or `new` lines of the diff. Multiple values are separated by comma, `none` resets previous values, `default` reset the list to `new` and `all` is a shorthand for `old,new,context`. When this option is not given, and the configuration variable `diff.wsErrorHighlight` is not set, only whitespace errors in `new` lines are highlighted. The whitespace errors are colored with `color.diff.whitespace`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---full-index)`--full-index` 
    
Instead of the first handful of characters, show the full pre- and post-image blob object names on the "index" line when generating patch format output. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---binary)`--binary` 
    
In addition to `--full-index`, output a binary diff that can be applied with `git-apply`. Implies `--patch`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---abbrevn)`--abbrev`[`=`_< n>_] 
    
Instead of showing the full 40-byte hexadecimal object name in diff-raw format output and diff-tree header lines, show the shortest prefix that is at least _< n>_ hexdigits long that uniquely refers the object. In diff-patch output format, `--full-index` takes higher precedence, i.e. if `--full-index` is specified, full blob names will be shown regardless of `--abbrev`. Non default number of digits can be specified with `--abbrev=`_< n>_. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Bnm)`-B`[_< n>_][`/`_< m>_] 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---break-rewritesnm)`--break-rewrites`[`=`[_< n>_][`/`_< m>_]] 
    
Break complete rewrite changes into pairs of delete and create. This serves two purposes:
It affects the way a change that amounts to a total rewrite of a file not as a series of deletion and insertion mixed together with a very few lines that happen to match textually as the context, but as a single deletion of everything old followed by a single insertion of everything new, and the number _< m>_ controls this aspect of the `-B` option (defaults to 60%). `-B/70%` specifies that less than 30% of the original should remain in the result for Git to consider it a total rewrite (i.e. otherwise the resulting patch will be a series of deletion and insertion mixed together with context lines).
When used with `-M`, a totally-rewritten file is also considered as the source of a rename (usually `-M` only considers a file that disappeared as the source of a rename), and the number _< n>_ controls this aspect of the `-B` option (defaults to 50%). `-B20%` specifies that a change with addition and deletion compared to 20% or more of the file’s size are eligible for being picked up as a possible source of a rename to another file. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Mn)`-M`[_< n>_] 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---find-renamesn)`--find-renames`[`=`_< n>_] 
    
Detect renames. If _< n>_ is specified, it is a threshold on the similarity index (i.e. amount of addition/deletions compared to the file’s size). For example, `-M90%` means Git should consider a delete/add pair to be a rename if more than 90% of the file hasn’t changed. Without a `%` sign, the number is to be read as a fraction, with a decimal point before it. I.e., `-M5` becomes 0.5, and is thus the same as `-M50%`. Similarly, `-M05` is the same as `-M5%`. To limit detection to exact renames, use `-M100%`. The default similarity index is 50%. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Cn)`-C`[_< n>_] 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---find-copiesn)`--find-copies`[`=`_< n>_] 
    
Detect copies as well as renames. See also `--find-copies-harder`. If _< n>_ is specified, it has the same meaning as for `-M`_< n>_. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---find-copies-harder)`--find-copies-harder` 
    
For performance reasons, by default, `-C` option finds copies only if the original file of the copy was modified in the same changeset. This flag makes the command inspect unmodified files as candidates for the source of copy. This is a very expensive operation for large projects, so use it with caution. Giving more than one `-C` option has the same effect. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--D)`-D` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---irreversible-delete)`--irreversible-delete` 
    
Omit the preimage for deletes, i.e. print only the header but not the diff between the preimage and `/dev/null`. The resulting patch is not meant to be applied with `patch` or `git` `apply`; this is solely for people who want to just concentrate on reviewing the text after the change. In addition, the output obviously lacks enough information to apply such a patch in reverse, even manually, hence the name of the option.
When used together with `-B`, omit also the preimage in the deletion part of a delete/create pair. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--lnum)`-l`_< num>_ 
    
The `-M` and `-C` options involve some preliminary steps that can detect subsets of renames/copies cheaply, followed by an exhaustive fallback portion that compares all remaining unpaired destinations to all relevant sources. (For renames, only remaining unpaired sources are relevant; for copies, all original sources are relevant.) For N sources and destinations, this exhaustive check is O(N^2). This option prevents the exhaustive portion of rename/copy detection from running if the number of source/destination files involved exceeds the specified number. Defaults to `diff.renameLimit`. Note that a value of 0 is treated as unlimited. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---diff-filterACDMRTUXB)`--diff-filter=`[(`A`|`C`|`D`|`M`|`R`|`T`|`U`|`X`|`B`)`...`[`*`]] 
    
Select only files that are Added (`A`), Copied (`C`), Deleted (`D`), Modified (`M`), Renamed (`R`), have their type (i.e. regular file, symlink, submodule, …​) changed (`T`), are Unmerged (`U`), are Unknown (`X`), or have had their pairing Broken (`B`). Any combination of the filter characters (including none) can be used. When `*` (All-or-none) is added to the combination, all paths are selected if there is any file that matches other criteria in the comparison; if there is no file that matches other criteria, nothing is selected.
Also, these upper-case letters can be downcased to exclude. E.g. `--diff-filter=ad` excludes added and deleted paths.
Note that not all diffs can feature all types. For instance, copied and renamed entries cannot appear if detection for those types is disabled. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Sstring)`-S`_< string>_ 
    
Look for differences that change the number of occurrences of the specified _< string>_ (i.e. addition/deletion) in a file. Intended for the scripter’s use.
It is useful when you’re looking for an exact block of code (like a struct), and want to know the history of that block since it first came into being: use the feature iteratively to feed the interesting block in the preimage back into `-S`, and keep going until you get the very first version of the block.
Binary files are searched as well. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Gregex)`-G`_< regex>_ 
    
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

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---find-objectobject-id)`--find-object=`_< object-id>_ 
    
Look for differences that change the number of occurrences of the specified object. Similar to `-S`, just the argument is different in that it doesn’t search for a specific string but for a specific object id.
The object can be a blob or a submodule commit. It implies the `-t` option in `git-log` to also find trees. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---pickaxe-all)`--pickaxe-all` 
    
When `-S` or `-G` finds a change, show all the changes in that changeset, not just the files that contain the change in _< string>_. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---pickaxe-regex)`--pickaxe-regex` 
    
Treat the _< string>_ given to `-S` as an extended POSIX regular expression to match. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Oorderfile)`-O`_< orderfile>_ 
    
Control the order in which files appear in the output. This overrides the `diff.orderFile` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). To cancel `diff.orderFile`, use `-O/dev/null`.
The output order is determined by the order of glob patterns in _< orderfile>_. All files with pathnames that match the first pattern are output first, all files with pathnames that match the second pattern (but not the first) are output next, and so on. All files with pathnames that do not match any pattern are output last, as if there was an implicit match-all pattern at the end of the file. If multiple pathnames have the same rank (they match the same pattern but no earlier patterns), their output order relative to each other is the normal order.
_< orderfile>_ is parsed as follows:
  * Blank lines are ignored, so they can be used as separators for readability.
  * Lines starting with a hash ("`#`") are ignored, so they can be used for comments. Add a backslash ("_\_ ") to the beginning of the pattern if it starts with a hash.
  * Each other line contains a single pattern.


Patterns have the same syntax and semantics as patterns used for `fnmatch`(3) without the `FNM_PATHNAME` flag, except a pathname also matches a pattern if removing any number of the final pathname components matches the pattern. For example, the pattern "`foo*bar`" matches "`fooasdfbar`" and "`foo/bar/baz/asdf`" but not "`foobarx`". 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---skip-tofile)`--skip-to=`_< file>_ 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---rotate-tofile)`--rotate-to=`_< file>_ 
    
Discard the files before the named _< file>_ from the output (i.e. _skip to_), or move them to the end of the output (i.e. _rotate to_). These options were invented primarily for the use of the `git` `difftool` command, and may not be very useful otherwise. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--R)`-R` 
    
Swap two inputs; that is, show differences from index or on-disk file to tree contents. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---relativepath)`--relative`[`=`_< path>_] 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-relative)`--no-relative` 
    
When run from a subdirectory of the project, it can be told to exclude changes outside the directory and show pathnames relative to it with this option. When you are not in a subdirectory (e.g. in a bare repository), you can name which subdirectory to make the output relative to by giving a _< path>_ as an argument. `--no-relative` can be used to countermand both `diff.relative` config option and previous `--relative`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--a)`-a` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---text)`--text` 
    
Treat all files as text. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ignore-cr-at-eol)`--ignore-cr-at-eol` 
    
Ignore carriage-return at the end of line when doing a comparison. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ignore-space-at-eol)`--ignore-space-at-eol` 
    
Ignore changes in whitespace at EOL. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--b)`-b` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ignore-space-change)`--ignore-space-change` 
    
Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--w)`-w` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ignore-all-space)`--ignore-all-space` 
    
Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ignore-blank-lines)`--ignore-blank-lines` 
    
Ignore changes whose lines are all blank. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--Iregex)`-I`_< regex>_ 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ignore-matching-linesregex)`--ignore-matching-lines=`_< regex>_ 
    
Ignore changes whose all lines match _< regex>_. This option may be specified more than once. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---inter-hunk-contextnumber)`--inter-hunk-context=`_< number>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--W)`-W` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---function-context)`--function-context` 
    
Show whole function as context lines for each change. The function names are determined in the same way as `git` `diff` works out patch hunk headers (see "Defining a custom hunk-header" in [gitattributes[5]](https://git-scm.com/docs/gitattributes)). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---exit-code)`--exit-code` 
    
Make the program exit with codes similar to `diff`(1). That is, it exits with 1 if there were differences and 0 means no differences. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---quiet)`--quiet` 
    
Disable all output of the program. Implies `--exit-code`. Disables execution of external diff helpers whose exit code is not trusted, i.e. their respective configuration option `diff.trustExitCode` or `diff.`_< driver>_`.trustExitCode` or environment variable `GIT_EXTERNAL_DIFF_TRUST_EXIT_CODE` is false. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ext-diff)`--ext-diff` 
    
Allow an external diff helper to be executed. If you set an external diff driver with [gitattributes[5]](https://git-scm.com/docs/gitattributes), you need to use this option with [git-log[1]](https://git-scm.com/docs/git-log) and friends. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-ext-diff)`--no-ext-diff` 
    
Disallow external diff drivers. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---textconv)`--textconv` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-textconv)`--no-textconv` 
    
Allow (or disallow) external text conversion filters to be run when comparing binary files. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. Because textconv filters are typically a one-way conversion, the resulting diff is suitable for human consumption, but cannot be applied. For this reason, textconv filters are enabled by default only for [git-diff[1]](https://git-scm.com/docs/git-diff) and [git-log[1]](https://git-scm.com/docs/git-log), but not for [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) or diff plumbing commands. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ignore-submodulesnoneuntrackeddirtyall)`--ignore-submodules`[`=`(`none`|`untracked`|`dirty`|`all`)] 
    
Ignore changes to submodules in the diff generation. `all` is the default. Using `none` will consider the submodule modified when it either contains untracked or modified files or its `HEAD` differs from the commit recorded in the superproject and can be used to override any settings of the `ignore` option in [git-config[1]](https://git-scm.com/docs/git-config) or [gitmodules[5]](https://git-scm.com/docs/gitmodules). When `untracked` is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using `dirty` ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior until 1.7.0). Using `all` hides all changes to submodules. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---src-prefixprefix)`--src-prefix=`_< prefix>_ 
    
Show the given source _< prefix>_ instead of "a/". 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---dst-prefixprefix)`--dst-prefix=`_< prefix>_ 
    
Show the given destination _< prefix>_ instead of "b/". 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-prefix)`--no-prefix` 
    
Do not show any source or destination prefix. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---default-prefix)`--default-prefix` 
    
Use the default source and destination prefixes ("a/" and "b/"). This overrides configuration variables such as `diff.noprefix`, `diff.srcPrefix`, `diff.dstPrefix`, and `diff.mnemonicPrefix` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---line-prefixprefix)`--line-prefix=`_< prefix>_ 
    
Prepend an additional _< prefix>_ to every line of output. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---ita-invisible-in-index)`--ita-invisible-in-index` 
    
By default entries added by `git` `add` `-N` appear as an existing empty file in `git` `diff` and a new file in `git` `diff` `--cached`. This option makes the entry appear as a new file in `git` `diff` and non-existent in `git` `diff` `--cached`. This option could be reverted with `--ita-visible-in-index`. Both options are experimental and could be removed in future. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---max-depthdepth)--max-depth=<depth> 
    
For each pathspec given on command line, descend at most _< depth>_ levels of directories. A value of `-1` means no limit. Cannot be combined with wildcards in the pathspec. Given a tree containing `foo/bar/baz`, the following list shows the matches generated by each set of options:
  * `--max-depth=0` `--` `foo`: `foo`
  * `--max-depth=1` `--` `foo`: `foo/bar`
  * `--max-depth=1` `--` `foo/bar`: `foo/bar/baz`
  * `--max-depth=1` `--` `foo` `foo/bar`: `foo/bar/baz`
  * `--max-depth=2` `--` `foo`: `foo/bar/baz`


If no pathspec is given, the depth is measured as if all top-level entries were specified. Note that this is different than measuring from the root, in that `--max-depth=0` would still return `foo`. This allows you to still limit depth while asking for a subset of the top-level entries.
Note that this option is only supported for diffs between tree objects, not against the index or working tree.
For more detailed explanation on these common options, see also [gitdiffcore[7]](https://git-scm.com/docs/gitdiffcore). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-tree-ish)<tree-ish> 
    
The id of a tree object. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-path)<path>…​ 
    
If provided, the results are limited to a subset of files matching one of the provided pathspecs. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--r)-r 
    
Recurse into sub-trees. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--t)-t 
    
Show tree entry itself as well as subtrees. Implies -r. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---root)--root 
    
When `--root` is specified the initial commit will be shown as a big creation event. This is equivalent to a diff against the NULL tree. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---merge-base)--merge-base 
    
Instead of comparing the <tree-ish>s directly, use the merge base between the two <tree-ish>s as the "before" side. There must be two <tree-ish>s given and they must both be commits. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---stdin)--stdin 
    
When `--stdin` is specified, the command does not take <tree-ish> arguments from the command line. Instead, it reads lines containing either two <tree>, one <commit>, or a list of <commit> from its standard input. (Use a single space as separator.)
When two trees are given, it compares the first tree with the second. When a single commit is given, it compares the commit with its parents. The remaining commits, when given, are used as if they are parents of the first commit.
When comparing two trees, the ID of both trees (separated by a space and terminated by a newline) is printed before the difference. When comparing commits, the ID of the first (or only) commit, followed by a newline, is printed.
The following flags further affect the behavior when comparing commits (but not trees). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--m)-m 
    
By default, _git diff-tree --stdin_ does not show differences for merge commits. With this flag, it shows differences to that commit from all of its parents. See also `-c`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--s-1)-s 
    
By default, _git diff-tree --stdin_ shows differences, either in machine-readable form (without `-p`) or in patch form (with `-p`). This output can be suppressed. It is only useful with the `-v` flag. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--v)-v 
    
This flag causes _git diff-tree --stdin_ to also show the commit message before the differences. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---prettyformat)`--pretty`[`=`_< format>_] 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---formatformat)`--format=`_< format>_ 
    
Pretty-print the contents of the commit logs in a given format, where _< format>_ can be one of `oneline`, `short`, `medium`, `full`, `fuller`, `reference`, `email`, `raw`, `format:`_< string>_ and `tformat:`_< string>_. When _< format>_ is none of the above, and has `%`_< placeholder>_ in it, it acts as if `--pretty=tformat:`_< format>_ were given.
See the "PRETTY FORMATS" section for some additional details for each format. When `=`_< format>_ part is omitted, it defaults to `medium`.
Note |  you can specify the default pretty format in the repository configuration (see [git-config[1]](https://git-scm.com/docs/git-config)).   
---|--- 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---abbrev-commit)`--abbrev-commit` 
      
Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely. `--abbrev=`_< n>_ (which also modifies diff output, if it is displayed) option can be used to specify the minimum length of the prefix.
This should make `--pretty=oneline` a whole lot more readable for people using 80-column terminals. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-abbrev-commit)`--no-abbrev-commit` 
    
Show the full 40-byte hexadecimal commit object name. This negates `--abbrev-commit`, either explicit or implied by other options such as `--oneline`. It also overrides the `log.abbrevCommit` variable. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---oneline)`--oneline` 
    
This is a shorthand for `--pretty=oneline` `--abbrev-commit` used together. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---encodingencoding)`--encoding=`_< encoding>_ 
    
Commit objects record the character encoding used for the log message in their encoding header; this option can be used to tell the command to re-code the commit log message in the encoding preferred by the user. For non plumbing commands this defaults to UTF-8. Note that if an object claims to be encoded in `X` and we are outputting in `X`, we will output the object verbatim; this means that invalid sequences in the original commit may be copied to the output. Likewise, if iconv(3) fails to convert the commit, we will quietly output the original object verbatim. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---expand-tabsn)`--expand-tabs=`_< n>_ 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---expand-tabs)`--expand-tabs` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-expand-tabs)`--no-expand-tabs` 
    
Perform a tab expansion (replace each tab with enough spaces to fill to the next display column that is a multiple of _< n>_) in the log message before showing it in the output. `--expand-tabs` is a short-hand for `--expand-tabs=8`, and `--no-expand-tabs` is a short-hand for `--expand-tabs=0`, which disables tab expansion.
By default, tabs are expanded in pretty formats that indent the log message by 4 spaces (i.e. `medium`, which is the default, `full`, and `fuller`). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---notesref)`--notes`[`=`_< ref>_] 
    
Show the notes (see [git-notes[1]](https://git-scm.com/docs/git-notes)) that annotate the commit, when showing the commit log message. This is the default for `git` `log`, `git` `show` and `git` `whatchanged` commands when there is no `--pretty`, `--format`, or `--oneline` option given on the command line.
By default, the notes shown are from the notes refs listed in the `core.notesRef` and `notes.displayRef` variables (or corresponding environment overrides). See [git-config[1]](https://git-scm.com/docs/git-config) for more details.
With an optional _< ref>_ argument, use the ref to find the notes to display. The ref can specify the full refname when it begins with `refs/notes/`; when it begins with `notes/`, `refs/` and otherwise `refs/notes/` is prefixed to form the full name of the ref.
Multiple `--notes` options can be combined to control which notes are being displayed. Examples: "`--notes=foo`" will show only notes from `refs/notes/foo`; "`--notes=foo` `--notes`" will show both notes from "refs/notes/foo" and from the default notes ref(s). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-notes)`--no-notes` 
    
Do not show notes. This negates the above `--notes` option, by resetting the list of notes refs from which notes are shown. Options are parsed in the order given on the command line, so e.g. "`--notes` `--notes=foo` `--no-notes` `--notes=bar`" will only show notes from `refs/notes/bar`. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---show-notes-by-default)`--show-notes-by-default` 
    
Show the default notes unless options for displaying specific notes are given. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---show-notesref)`--show-notes`[`=`_< ref>_] 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---standard-notes)`--standard-notes` 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-standard-notes)`--no-standard-notes` 
    
These options are deprecated. Use the above `--notes`/`--no-notes` options instead. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---show-signature)`--show-signature` 
    
Check the validity of a signed commit object by passing the signature to `gpg` `--verify` and show the output. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---no-commit-id)--no-commit-id 
    
_git diff-tree_ outputs a line with the commit ID when applicable. This flag suppresses the commit ID output. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt--c)-c 
    
This flag changes the way a merge commit is displayed (which means it is useful only when the command is given one <tree-ish>, or `--stdin`). It shows the differences from each of the parents to the merge result simultaneously instead of showing pairwise diff between a parent and the result one at a time (which is what the `-m` option does). Furthermore, it lists only files which were modified from all parents. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---cc)--cc 
    
This flag changes the way a merge commit patch is displayed, in a similar way to the `-c` option. It implies the `-c` and `-p` options and further compresses the patch output by omitting uninteresting hunks whose contents in the parents have only two variants and the merge result picks one of them without modification. When all hunks are uninteresting, the commit itself and the commit log message are not shown, just like in any other "empty diff" case. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---combined-all-paths)--combined-all-paths 
    
This flag causes combined diffs (used for merge commits) to list the name of the file from all parents. It thus only has effect when -c or --cc are specified, and is likely only useful if filename changes are detected (i.e. when either rename or copy detection have been requested). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt---always)--always 
    
Show the commit itself and the commit log message even if the diff itself is empty.
##  [](https://git-scm.com/docs/git-diff-tree#_pretty_formats)PRETTY FORMATS
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

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-n)`%n` 
    
newline 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-)`%%` 
    
a raw `%` 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-x00)`%x00` 
    
`%x` followed by two hexadecimal digits is replaced with a byte with the hexadecimal digits' value (we will call this "literal formatting code" in the rest of this document).
    * Placeholders that affect formatting of later placeholders: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-Cred)`%Cred` 
    
switch color to red 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-Cgreen)`%Cgreen` 
    
switch color to green 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-Cblue)`%Cblue` 
    
switch color to blue 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-Creset)`%Creset` 
    
reset color 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-Cspec)`%C`(_< spec>_) 
    
color specification, as described under Values in the "CONFIGURATION FILE" section of [git-config[1]](https://git-scm.com/docs/git-config). By default, colors are shown only when enabled for log output (by `color.diff`, `color.ui`, or `--color`, and respecting the `auto` settings of the former if we are going to a terminal). `%C`(`auto,`_< spec>_) is accepted as a historical synonym for the default (e.g., `%C`(`auto,red`)). Specifying `%C`(`always,`_< spec>_) will show the colors even when color is not otherwise enabled (though consider just using `--color=always` to enable color for the whole output, including this format and anything else git might color). `auto` alone (i.e. `%C`(`auto`)) will turn on auto coloring on the next placeholders until the color is switched again. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-m)`%m` 
    
left (_<_), right (_>_) or boundary (`-`) mark 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-wwi1i2)`%w`([_< w>_[`,`_< i1>_[`,`_< i2>_]]]) 
    
switch line wrapping, like the `-w` option of [git-shortlog[1]](https://git-scm.com/docs/git-shortlog). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ntruncltruncmtrunc)_% <(__< n>_[`,`(`trunc`|`ltrunc`|`mtrunc`)]) 
    
make the next placeholder take at least N column widths, padding spaces on the right if necessary. Optionally truncate (with ellipsis `..`) at the left (ltrunc) `..ft`, the middle (mtrunc) `mi..le`, or the end (trunc) `rig..`, if the output is longer than _< n>_ columns. Note 1: that truncating only works correctly with _< n>_ >= 2. Note 2: spaces around the _< n>_ and _< m>_ (see below) values are optional. Note 3: Emojis and other wide characters will take two display columns, which may over-run column boundaries. Note 4: decomposed character combining marks may be misplaced at padding boundaries. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-m-1)_% <|(__< m>_ ) 
    
make the next placeholder take at least until _< m>_ th display column, padding spaces on the right if necessary. Use negative _< m>_ values for column positions measured from the right hand edge of the terminal window. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-n-1)_% >(__< n>_) 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-m-1-1)_% >|(__< m>_) 
    
similar to _% <(__< n>_), _% <|(__< m>_) respectively, but padding spaces on the left 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-n-1-1)_% >>(__< n>_) 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-m-1-1-1)_% >>|(__< m>_) 
    
similar to _% >(__< n>_), _% >|(__< m>_) respectively, except that if the next placeholder takes more spaces than given and there are spaces on its left, use those spaces 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-n-1-1-1)_% ><(__< n>_) 


[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-m-1-1-1-1)_% ><|(__< m>_) 
    
similar to _% <(__< n>_), _% <|(__< m>_) respectively, but padding both sides (i.e. the text is centered)
    * Placeholders that expand to information extracted from the commit: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-H)`%H` 
    
commit hash 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-h)`%h` 
    
abbreviated commit hash 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-T)`%T` 
    
tree hash 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-t)`%t` 
    
abbreviated tree hash 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-P)`%P` 
    
parent hashes 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-p)`%p` 
    
abbreviated parent hashes 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-an)`%an` 
    
author name 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-aN)`%aN` 
    
author name (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ae)`%ae` 
    
author email 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-aE)`%aE` 
    
author email (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-al)`%al` 
    
author email local-part (the part before the `@` sign) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-aL)`%aL` 
    
author local-part (see `%al`) respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ad)`%ad` 
    
author date (format respects --date= option) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-aD)`%aD` 
    
author date, RFC2822 style 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ar)`%ar` 
    
author date, relative 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-at)`%at` 
    
author date, UNIX timestamp 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ai)`%ai` 
    
author date, ISO 8601-like format 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-aI)`%aI` 
    
author date, strict ISO 8601 format 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-as)`%as` 
    
author date, short format (`YYYY-MM-DD`) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ah)`%ah` 
    
author date, human style (like the `--date=human` option of [git-rev-list[1]](https://git-scm.com/docs/git-rev-list)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cn)`%cn` 
    
committer name 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cN)`%cN` 
    
committer name (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ce)`%ce` 
    
committer email 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cE)`%cE` 
    
committer email (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cl)`%cl` 
    
committer email local-part (the part before the `@` sign) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cL)`%cL` 
    
committer local-part (see `%cl`) respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cd)`%cd` 
    
committer date (format respects --date= option) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cD)`%cD` 
    
committer date, RFC2822 style 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cr)`%cr` 
    
committer date, relative 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ct)`%ct` 
    
committer date, UNIX timestamp 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ci)`%ci` 
    
committer date, ISO 8601-like format 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cI)`%cI` 
    
committer date, strict ISO 8601 format 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-cs)`%cs` 
    
committer date, short format (`YYYY-MM-DD`) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ch)`%ch` 
    
committer date, human style (like the `--date=human` option of [git-rev-list[1]](https://git-scm.com/docs/git-rev-list)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-d)`%d` 
    
ref names, like the --decorate option of [git-log[1]](https://git-scm.com/docs/git-log) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-D)`%D` 
    
ref names without the " (", ")" wrapping. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-decorateoption)`%`(`decorate`[`:`_< option>_`,...`]) 
    
ref names with custom decorations. The `decorate` string may be followed by a colon and zero or more comma-separated options. Option values may contain literal formatting codes. These must be used for commas (`%x2C`) and closing parentheses (`%x29`), due to their role in the option syntax.
      * `prefix=`_< value>_: Shown before the list of ref names. Defaults to " (".
      * `suffix=`_< value>_: Shown after the list of ref names. Defaults to ")".
      * `separator=`_< value>_: Shown between ref names. Defaults to "`,` ".
      * `pointer=`_< value>_: Shown between HEAD and the branch it points to, if any. Defaults to "  _→_ ".
      * `tag=`_< value>_: Shown before tag names. Defaults to "`tag:` ".
For example, to produce decorations with no wrapping or tag annotations, and spaces as separators:
`%`(`decorate:prefix=,suffix=,tag=,separator=` ) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-describeoption)`%`(`describe`[`:`_< option>_`,...`]) 
    
human-readable name, like [git-describe[1]](https://git-scm.com/docs/git-describe); empty string for undescribable commits. The `describe` string may be followed by a colon and zero or more comma-separated options. Descriptions can be inconsistent when tags are added or removed at the same time.
    * `tags`[`=`_< bool-value>_]: Instead of only considering annotated tags, consider lightweight tags as well.
    * `abbrev=`_< number>_: Instead of using the default number of hexadecimal digits (which will vary according to the number of objects in the repository with a default of 7) of the abbreviated object name, use <number> digits, or as many digits as needed to form a unique object name.
    * `match=`_< pattern>_: Only consider tags matching the given `glob`(`7`) _< pattern>_, excluding the `refs/tags/` prefix.
    * `exclude=`_< pattern>_: Do not consider tags matching the given `glob`(`7`) _< pattern>_, excluding the `refs/tags/` prefix. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-S)`%S` 
    
ref name given on the command line by which the commit was reached (like `git` `log` `--source`), only works with `git` `log` 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-e)`%e` 
    
encoding 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-s)`%s` 
    
subject 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-f)`%f` 
    
sanitized subject line, suitable for a filename 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-b)`%b` 
    
body 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-B)`%B` 
    
raw body (unwrapped subject and body) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-N)`%N` 
    
commit notes 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-GG)`%GG` 
    
raw verification message from GPG for a signed commit 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-G)_%G?_ 
    
show "G" for a good (valid) signature, "B" for a bad signature, "U" for a good signature with unknown validity, "X" for a good signature that has expired, "Y" for a good signature made by an expired key, "R" for a good signature made by a revoked key, "E" if the signature cannot be checked (e.g. missing key) and "N" for no signature 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-GS)`%GS` 
    
show the name of the signer for a signed commit 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-GK)`%GK` 
    
show the key used to sign a signed commit 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-GF)`%GF` 
    
show the fingerprint of the key used to sign a signed commit 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-GP)`%GP` 
    
show the fingerprint of the primary key whose subkey was used to sign a signed commit 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-GT)`%GT` 
    
show the trust level for the key used to sign a signed commit 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-gD)`%gD` 
    
reflog selector, e.g., `refs/stash@{1}` or `refs/stash@{2` `minutes` `ago}`; the format follows the rules described for the `-g` option. The portion before the `@` is the refname as given on the command line (so `git` `log` `-g` `refs/heads/master` would yield `refs/heads/master@{0}`). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-gd)`%gd` 
    
shortened reflog selector; same as `%gD`, but the refname portion is shortened for human readability (so `refs/heads/master` becomes just `master`). 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-gn)`%gn` 
    
reflog identity name 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-gN)`%gN` 
    
reflog identity name (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-ge)`%ge` 
    
reflog identity email 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-gE)`%gE` 
    
reflog identity email (respecting .mailmap, see [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) or [git-blame[1]](https://git-scm.com/docs/git-blame)) 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-gs)`%gs` 
    
reflog subject 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-trailersoption)`%`(`trailers`[`:`_< option>_`,...`]) 
    
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



##  [](https://git-scm.com/docs/git-diff-tree#_raw_output_format)Raw output format
The raw output format from `git-diff-index`, `git-diff-tree`, `git-diff-files` and `git` `diff` `--raw` are very similar.
These commands all compare two sets of things; what is compared differs: 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-git-diff-indextree-ish)`git-diff-index` _< tree-ish>_ 
    
compares the _< tree-ish>_ and the files on the filesystem. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-git-diff-index--cachedtree-ish)`git-diff-index` `--cached` _< tree-ish>_ 
    
compares the _< tree-ish>_ and the index. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-git-diff-tree-rtree-ish-1tree-ish-2pattern)`git-diff-tree` [`-r`] _< tree-ish-1>_ _< tree-ish-2>_ [_< pattern>_...] 
    
compares the trees named by the two arguments. 

[](https://git-scm.com/docs/git-diff-tree#Documentation/git-diff-tree.txt-git-diff-filespattern)`git-diff-files` [_< pattern>_...] 
    
compares the index and the files on the filesystem.
The `git-diff-tree` command begins its output by printing the hash of what is being compared. After that, all the commands print one output line per changed file.
An output line is formatted this way:
```
in-place edit  :100644 100644 bcd1234 0123456 M file0
copy-edit      :100644 100644 abcd123 1234567 C68 file1 file2
rename-edit    :100644 100644 abcd123 1234567 R86 file1 file3
create         :000000 100644 0000000 1234567 A file4
delete         :100644 000000 1234567 0000000 D file5
unmerged       :000000 000000 0000000 0000000 U file6
```

That is, from the left to the right:
  1. a colon.
  2. mode for "src"; 000000 if creation or unmerged.
  3. a space.
  4. mode for "dst"; 000000 if deletion or unmerged.
  5. a space.
  6. sha1 for "src"; 0{40} if creation or unmerged.
  7. a space.
  8. sha1 for "dst"; 0{40} if deletion, unmerged or "work tree out of sync with the index".
  9. a space.
  10. status, followed by optional "score" number.
  11. a tab or a NUL when `-z` option is used.
  12. path for "src"
  13. a tab or a NUL when `-z` option is used; only exists for C or R.
  14. path for "dst"; only exists for C or R.
  15. an LF or a NUL when `-z` option is used, to terminate the record.


Possible status letters are:
  * `A`: addition of a file
  * `C`: copy of a file into a new one
  * `D`: deletion of a file
  * `M`: modification of the contents or mode of a file
  * `R`: renaming of a file
  * `T`: change in the type of the file (regular file, symbolic link or submodule)
  * `U`: file is unmerged (you must complete the merge before it can be committed)
  * `X`: "unknown" change type (most probably a bug, please report it)


Status letters `C` and `R` are always followed by a score (denoting the percentage of similarity between the source and target of the move or copy). Status letter `M` may be followed by a score (denoting the percentage of dissimilarity) for file rewrites.
The sha1 for "dst" is shown as all 0’s if a file on the filesystem is out of sync with the index.
Example:
```
:100644 100644 5be4a4a 0000000 M file.c
```

Without the `-z` option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). Using `-z` the filename is output verbatim and the line is terminated by a NUL byte.
##  [](https://git-scm.com/docs/git-diff-tree#_diff_format_for_merges)diff format for merges
`git-diff-tree`, `git-diff-files` and `git-diff` `--raw` can take `-c` or `--cc` option to generate diff output also for merge commits. The output differs from the format described above in the following way:
  1. there is a colon for each parent
  2. there are more "src" modes and "src" sha1
  3. status is concatenated status characters for each parent
  4. no optional "score" number
  5. tab-separated pathname(s) of the file


For `-c` and `--cc`, only the destination or final path is shown even if the file was renamed on any side of history. With `--combined-all-paths`, the name of the path in each parent is shown followed by the name of the path in the merge commit.
Examples for `-c` and `--cc` without `--combined-all-paths`:
```
::100644 100644 100644 fabadb8 cc95eb0 4866510 MM	desc.c
::100755 100755 100755 52b7a2d 6d1ac04 d2ac7d7 RM	bar.sh
::100644 100644 100644 e07d6c5 9042e82 ee91881 RR	phooey.c
```

Examples when `--combined-all-paths` added to either `-c` or `--cc`:
```
::100644 100644 100644 fabadb8 cc95eb0 4866510 MM	desc.c	desc.c	desc.c
::100755 100755 100755 52b7a2d 6d1ac04 d2ac7d7 RM	foo.sh	bar.sh	bar.sh
::100644 100644 100644 e07d6c5 9042e82 ee91881 RR	fooey.c	fuey.c	phooey.c
```

Note that _combined diff_ lists only files which were modified from all parents.
##  [](https://git-scm.com/docs/git-diff-tree#generate_patch_text_with_p)Generating patch text with -p
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


##  [](https://git-scm.com/docs/git-diff-tree#_combined_diff_format)Combined diff format
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
##  [](https://git-scm.com/docs/git-diff-tree#_other_diff_formats)other diff formats
The `--summary` option describes newly added, deleted, renamed and copied files. The `--stat` option adds `diffstat`(1) graph to the output. These options can be combined with other options, such as `-p`, and are meant for human consumption.
When showing a change that involves a rename or a copy, `--stat` output formats the pathnames compactly by combining common prefix and suffix of the pathnames. For example, a change that moves `arch/i386/Makefile` to `arch/x86/Makefile` while modifying 4 lines will be shown like this:
```
arch/{i386 => x86}/Makefile    |   4 +--
```

The `--numstat` option gives the diffstat(1) information but is designed for easier machine consumption. An entry in `--numstat` output looks like this:
```
1	2	README
3	1	arch/{i386 => x86}/Makefile
```

That is, from left to right:
  1. the number of added lines;
  2. a tab;
  3. the number of deleted lines;
  4. a tab;
  5. pathname (possibly with rename/copy information);
  6. a newline.


When `-z` output option is in effect, the output is formatted this way:
```
1	2	README NUL
3	1	NUL arch/i386/Makefile NUL arch/x86/Makefile NUL
```

That is:
  1. the number of added lines;
  2. a tab;
  3. the number of deleted lines;
  4. a tab;
  5. a NUL (only exists if renamed/copied);
  6. pathname in preimage;
  7. a NUL (only exists if renamed/copied);
  8. pathname in postimage (only exists if renamed/copied);
  9. a NUL.


The extra `NUL` before the preimage path in renamed case is to allow scripts that read the output to tell if the current record being read is a single-path record or a rename/copy record without reading ahead. After reading added and deleted lines, reading up to `NUL` would yield the pathname, but if that is `NUL`, the record will show two paths.
##  [](https://git-scm.com/docs/git-diff-tree#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### diff-tree
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
