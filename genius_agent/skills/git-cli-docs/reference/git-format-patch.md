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
    * [NAME](https://git-scm.com/docs/git-format-patch#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-format-patch#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-format-patch#_description)
    * [OPTIONS](https://git-scm.com/docs/git-format-patch#_options)
    * [CONFIGURATION](https://git-scm.com/docs/git-format-patch#_configuration)
    * [DISCUSSION](https://git-scm.com/docs/git-format-patch#_discussion)
    * [MUA-SPECIFIC HINTS](https://git-scm.com/docs/git-format-patch#_mua_specific_hints)
    * [BASE TREE INFORMATION](https://git-scm.com/docs/git-format-patch#_base_tree_information)
    * [EXAMPLES](https://git-scm.com/docs/git-format-patch#_examples)
    * [CAVEATS](https://git-scm.com/docs/git-format-patch#_caveats)
    * [SEE ALSO](https://git-scm.com/docs/git-format-patch#_see_also)
    * [GIT](https://git-scm.com/docs/git-format-patch#_git)


[ English ▾](https://git-scm.com/docs/git-format-patch)
Localized versions of **git-format-patch** manual
  1. [English ](https://git-scm.com/docs/git-format-patch)
  2. [Français ](https://git-scm.com/docs/git-format-patch/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-format-patch/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-format-patch/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-format-patch/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-format-patch)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-format-patch) git-format-patch last updated in 2.53.0
Changes in the **git-format-patch** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-format-patch/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-format-patch/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-format-patch/2.51.1)
  5. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-format-patch/2.51.0)
  6. 2.48.1 → 2.50.1 no changes
  7. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-format-patch/2.48.0)
  8. 2.46.1 → 2.47.3 no changes
  9. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-format-patch/2.46.0)
  10. 2.45.4 no changes
  11. [2.45.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-format-patch/2.45.3)
  12. 2.45.1 → 2.45.2 no changes
  13. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-format-patch/2.45.0)
  14. 2.44.1 → 2.44.4 no changes
  15. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-format-patch/2.44.0)
  16. 2.43.2 → 2.43.7 no changes
  17. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-format-patch/2.43.1)
  18. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-format-patch/2.43.0)
  19. 2.42.2 → 2.42.4 no changes
  20. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-format-patch/2.42.1)
  21. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-format-patch/2.42.0)
  22. 2.41.1 → 2.41.3 no changes
  23. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-format-patch/2.41.0)
  24. 2.40.1 → 2.40.4 no changes
  25. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-format-patch/2.40.0)
  26. 2.38.1 → 2.39.5 no changes
  27. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-format-patch/2.38.0)
  28. 2.36.1 → 2.37.7 no changes
  29. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-format-patch/2.36.0)
  30. 2.35.1 → 2.35.8 no changes
  31. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-format-patch/2.35.0)
  32. 2.34.1 → 2.34.8 no changes
  33. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-format-patch/2.34.0)
  34. 2.33.1 → 2.33.8 no changes
  35. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-format-patch/2.33.0)
  36. 2.32.1 → 2.32.7 no changes
  37. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-format-patch/2.32.0)
  38. 2.31.1 → 2.31.8 no changes
  39. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-format-patch/2.31.0)
  40. 2.30.1 → 2.30.9 no changes
  41. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-format-patch/2.30.0)
  42. 2.29.1 → 2.29.3 no changes
  43. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-format-patch/2.29.0)
  44. 2.28.1 no changes
  45. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-format-patch/2.28.0)
  46. 2.27.1 no changes
  47. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-format-patch/2.27.0)
  48. 2.25.2 → 2.26.3 no changes
  49. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-format-patch/2.25.1)
  50. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-format-patch/2.25.0)
  51. 2.24.1 → 2.24.4 no changes
  52. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-format-patch/2.24.0)
  53. 2.23.1 → 2.23.4 no changes
  54. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-format-patch/2.23.0)
  55. 2.22.1 → 2.22.5 no changes
  56. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-format-patch/2.22.0)
  57. 2.21.1 → 2.21.4 no changes
  58. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-format-patch/2.21.0)
  59. 2.20.1 → 2.20.5 no changes
  60. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-format-patch/2.20.0)
  61. 2.19.1 → 2.19.6 no changes
  62. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-format-patch/2.19.0)
  63. 2.18.1 → 2.18.5 no changes
  64. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-format-patch/2.18.0)
  65. 2.17.1 → 2.17.6 no changes
  66. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-format-patch/2.17.0)
  67. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-format-patch/2.16.6)
  68. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-format-patch/2.15.4)
  69. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-format-patch/2.14.6)
  70. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-format-patch/2.13.7)
  71. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-format-patch/2.12.5)
  72. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-format-patch/2.11.4)
  73. 2.10.5 no changes
  74. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-format-patch/2.9.5)
  75. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-format-patch/2.8.6)
  76. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-format-patch/2.7.6)
  77. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-format-patch/2.6.7)
  78. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-format-patch/2.5.6)
  79. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-format-patch/2.4.12)
  80. 2.2.3 → 2.3.10 no changes
  81. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-format-patch/2.1.4)
  82. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-format-patch/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-format-patch#_name)NAME
git-format-patch - Prepare patches for e-mail submission
##  [](https://git-scm.com/docs/git-format-patch#_synopsis)SYNOPSIS
```
_git format-patch_ [-k] [(-o|--output-directory) <dir> | --stdout]
		   [--no-thread | --thread[=<style>]]
		   [(--attach|--inline)[=<boundary>] | --no-attach]
		   [-s | --signoff]
		   [--signature=<signature> | --no-signature]
		   [--signature-file=<file>]
		   [-n | --numbered | -N | --no-numbered]
		   [--start-number <n>] [--numbered-files]
		   [--in-reply-to=<message-id>] [--suffix=.<sfx>]
		   [--ignore-if-in-upstream] [--always]
		   [--cover-from-description=<mode>]
		   [--rfc[=<rfc>]] [--subject-prefix=<subject-prefix>]
		   [(--reroll-count|-v) <n>]
		   [--to=<email>] [--cc=<email>]
		   [--[no-]cover-letter] [--quiet]
		   [--[no-]encode-email-headers]
		   [--no-notes | --notes[=<ref>]]
		   [--interdiff=<previous>]
		   [--range-diff=<previous> [--creation-factor=<percent>]]
		   [--filename-max-length=<n>]
		   [--progress]
		   [<common-diff-options>]
		   [ <since> | <revision-range> ]
```

##  [](https://git-scm.com/docs/git-format-patch#_description)DESCRIPTION
Prepare each non-merge commit with its "patch" in one "message" per commit, formatted to resemble a UNIX mailbox. The output of this command is convenient for e-mail submission or for use with _git am_.
A "message" generated by the command consists of three parts:
  * A brief metadata header that begins with `From` _< commit>_ with a fixed `Mon` `Sep` `17` `00:00:00` `2001` datestamp to help programs like "file(1)" to recognize that the file is an output from this command, fields that record the author identity, the author date, and the title of the change (taken from the first paragraph of the commit log message).
  * The second and subsequent paragraphs of the commit log message.
  * The "patch", which is the "diff -p --stat" output (see [git-diff[1]](https://git-scm.com/docs/git-diff)) between the commit and its parent.


The log message and the patch are separated by a line with a three-dash line.
There are two ways to specify which commits to operate on.
  1. A single commit, <since>, specifies that the commits leading to the tip of the current branch that are not in the history that leads to the <since> to be output.
  2. Generic <revision-range> expression (see "SPECIFYING REVISIONS" section in [gitrevisions[7]](https://git-scm.com/docs/gitrevisions)) means the commits in the specified range.


The first rule takes precedence in the case of a single <commit>. To apply the second rule, i.e., format everything since the beginning of history up until <commit>, use the `--root` option: `git` `format-patch` `--root` _< commit>_. If you want to format only <commit> itself, you can do this with `git` `format-patch` `-1` _< commit>_.
By default, each output file is numbered sequentially from 1, and uses the first line of the commit message (massaged for pathname safety) as the filename. With the `--numbered-files` option, the output file names will only be numbers, without the first line of the commit appended. The names of the output files are printed to standard output, unless the `--stdout` option is specified.
If `-o` is specified, output files are created in <dir>. Otherwise they are created in the current working directory. The default path can be set with the `format.outputDirectory` configuration option. The `-o` option takes precedence over `format.outputDirectory`. To store patches in the current working directory even when `format.outputDirectory` points elsewhere, use `-o` `.`. All directory components will be created.
By default, the subject of a single patch is "[PATCH] " followed by the concatenation of lines from the commit message up to the first blank line (see the DISCUSSION section of [git-commit[1]](https://git-scm.com/docs/git-commit)).
When multiple patches are output, the subject prefix will instead be "[PATCH n/m] ". To force 1/1 to be added for a single patch, use `-n`. To omit patch numbers from the subject, use `-N`.
If given `--thread`, `git-format-patch` will generate `In-Reply-To` and `References` headers to make the second and subsequent patch mails appear as replies to the first mail; this also generates a `Message-ID` header to reference.
##  [](https://git-scm.com/docs/git-format-patch#_options)OPTIONS 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--p)-p 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-stat)--no-stat 
    
Generate plain patches without any diffstats. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context instead of the usual three. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---outputfile)`--output=`_< file>_ 
    
Output to a specific file instead of stdout. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---output-indicator-newchar)`--output-indicator-new=`_< char>_ 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---output-indicator-oldchar)`--output-indicator-old=`_< char>_ 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---output-indicator-contextchar)`--output-indicator-context=`_< char>_ 
    
Specify the character used to indicate new, old or context lines in the generated patch. Normally they are `+`, `-` and ' ' respectively. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---indent-heuristic)`--indent-heuristic` 
    
Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-indent-heuristic)`--no-indent-heuristic` 
    
Disable the indent heuristic. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---minimal)`--minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---patience)`--patience` 
    
Generate a diff using the "patience diff" algorithm. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---histogram)`--histogram` 
    
Generate a diff using the "histogram diff" algorithm. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---anchoredtext)`--anchored=`_< text>_ 
    
Generate a diff using the "anchored diff" algorithm.
This option may be specified more than once.
If a line exists in both the source and destination, exists only once, and starts with _< text>_, this algorithm attempts to prevent it from appearing as a deletion or addition in the output. It uses the "patience diff" algorithm internally. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---diff-algorithmpatienceminimalhistogrammyers)`--diff-algorithm=`(`patience`|`minimal`|`histogram`|`myers`) 
    
Choose a diff algorithm. The variants are as follows: 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-default)`default` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-myers)`myers` 
    
The basic greedy diff algorithm. Currently, this is the default. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-minimal)`minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-patience)`patience` 
    
Use "patience diff" algorithm when generating patches. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-histogram)`histogram` 
    
This algorithm extends the patience algorithm to "support low-occurrence common elements".
For instance, if you configured the `diff.algorithm` variable to a non-default value and want to use the default one, then you have to use `--diff-algorithm=default` option. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---statwidthname-widthcount)`--stat`[`=`_< width>_[`,`_< name-width>_[`,`_< count>_]]] 
    
Generate a diffstat. By default, as much space as necessary will be used for the filename part, and the rest for the graph part. Maximum width defaults to terminal width, or 80 columns if not connected to a terminal, and can be overridden by _< width>_. The width of the filename part can be limited by giving another width _< name-width>_ after a comma or by setting `diff.statNameWidth=`_< name-width>_. The width of the graph part can be limited by using `--stat-graph-width=`_< graph-width>_ or by setting `diff.statGraphWidth=`_< graph-width>_. Using `--stat` or `--stat-graph-width` affects all commands generating a stat graph, while setting `diff.statNameWidth` or `diff.statGraphWidth` does not affect `git` `format-patch`. By giving a third parameter _< count>_, you can limit the output to the first _< count>_ lines, followed by ... if there are more.
These parameters can also be set individually with `--stat-width=`_< width>_, `--stat-name-width=`_< name-width>_ and `--stat-count=`_< count>_. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---compact-summary)`--compact-summary` 
    
Output a condensed summary of extended header information such as file creations or deletions ("new" or "gone", optionally `+l` if it’s a symlink) and mode changes (`+x` or `-x` for adding or removing executable bit respectively) in diffstat. The information is put between the filename part and the graph part. Implies `--stat`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---numstat)`--numstat` 
    
Similar to `--stat`, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine friendly. For binary files, outputs two `-` instead of saying `0` `0`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---shortstat)`--shortstat` 
    
Output only the last line of the `--stat` format containing total number of modified files, as well as number of added and deleted lines. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--Xparam)`-X` [_< param>_`,...`] 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---dirstatparam)`--dirstat`[`=`_< param>_`,...`] 
    
Output the distribution of relative amount of changes for each sub-directory. The behavior of `--dirstat` can be customized by passing it a comma separated list of parameters. The defaults are controlled by the `diff.dirstat` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). The following parameters are available: 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-changes)`changes` 
    
Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-lines)`lines` 
    
Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive `--dirstat` behavior than the `changes` behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other `--*stat` options. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-files)`files` 
    
Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest `--dirstat` behavior, since it does not have to look at the file contents at all. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-cumulative)`cumulative` 
    
Count changes in a child directory for the parent directory as well. Note that when using `cumulative`, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the `noncumulative` parameter. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt-limit)_< limit>_ 
    
An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.
Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: `--dirstat=files,10,cumulative`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---cumulative)`--cumulative` 
    
Synonym for `--dirstat=cumulative`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---dirstat-by-fileparam)`--dirstat-by-file`[`=`_< param>_`,...`] 
    
Synonym for `--dirstat=files,`_< param>_`,...`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---summary)`--summary` 
    
Output a condensed summary of extended header information such as creations, renames and mode changes. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-renames)`--no-renames` 
    
Turn off rename detection, even when the configuration file gives the default to do so. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---rename-empty)`--rename-empty` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-rename-empty)`--no-rename-empty` 
    
Whether to use empty blobs as rename source. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---full-index)`--full-index` 
    
Instead of the first handful of characters, show the full pre- and post-image blob object names on the "index" line when generating patch format output. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---binary)`--binary` 
    
In addition to `--full-index`, output a binary diff that can be applied with `git-apply`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---abbrevn)`--abbrev`[`=`_< n>_] 
    
Instead of showing the full 40-byte hexadecimal object name in diff-raw format output and diff-tree header lines, show the shortest prefix that is at least _< n>_ hexdigits long that uniquely refers the object. In diff-patch output format, `--full-index` takes higher precedence, i.e. if `--full-index` is specified, full blob names will be shown regardless of `--abbrev`. Non default number of digits can be specified with `--abbrev=`_< n>_. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--Bnm)`-B`[_< n>_][`/`_< m>_] 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---break-rewritesnm)`--break-rewrites`[`=`[_< n>_][`/`_< m>_]] 
    
Break complete rewrite changes into pairs of delete and create. This serves two purposes:
It affects the way a change that amounts to a total rewrite of a file not as a series of deletion and insertion mixed together with a very few lines that happen to match textually as the context, but as a single deletion of everything old followed by a single insertion of everything new, and the number _< m>_ controls this aspect of the `-B` option (defaults to 60%). `-B/70%` specifies that less than 30% of the original should remain in the result for Git to consider it a total rewrite (i.e. otherwise the resulting patch will be a series of deletion and insertion mixed together with context lines).
When used with `-M`, a totally-rewritten file is also considered as the source of a rename (usually `-M` only considers a file that disappeared as the source of a rename), and the number _< n>_ controls this aspect of the `-B` option (defaults to 50%). `-B20%` specifies that a change with addition and deletion compared to 20% or more of the file’s size are eligible for being picked up as a possible source of a rename to another file. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--Mn)`-M`[_< n>_] 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---find-renamesn)`--find-renames`[`=`_< n>_] 
    
Detect renames. If _< n>_ is specified, it is a threshold on the similarity index (i.e. amount of addition/deletions compared to the file’s size). For example, `-M90%` means Git should consider a delete/add pair to be a rename if more than 90% of the file hasn’t changed. Without a `%` sign, the number is to be read as a fraction, with a decimal point before it. I.e., `-M5` becomes 0.5, and is thus the same as `-M50%`. Similarly, `-M05` is the same as `-M5%`. To limit detection to exact renames, use `-M100%`. The default similarity index is 50%. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--Cn)`-C`[_< n>_] 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---find-copiesn)`--find-copies`[`=`_< n>_] 
    
Detect copies as well as renames. See also `--find-copies-harder`. If _< n>_ is specified, it has the same meaning as for `-M`_< n>_. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---find-copies-harder)`--find-copies-harder` 
    
For performance reasons, by default, `-C` option finds copies only if the original file of the copy was modified in the same changeset. This flag makes the command inspect unmodified files as candidates for the source of copy. This is a very expensive operation for large projects, so use it with caution. Giving more than one `-C` option has the same effect. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--D)`-D` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---irreversible-delete)`--irreversible-delete` 
    
Omit the preimage for deletes, i.e. print only the header but not the diff between the preimage and `/dev/null`. The resulting patch is not meant to be applied with `patch` or `git` `apply`; this is solely for people who want to just concentrate on reviewing the text after the change. In addition, the output obviously lacks enough information to apply such a patch in reverse, even manually, hence the name of the option.
When used together with `-B`, omit also the preimage in the deletion part of a delete/create pair. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--lnum)`-l`_< num>_ 
    
The `-M` and `-C` options involve some preliminary steps that can detect subsets of renames/copies cheaply, followed by an exhaustive fallback portion that compares all remaining unpaired destinations to all relevant sources. (For renames, only remaining unpaired sources are relevant; for copies, all original sources are relevant.) For N sources and destinations, this exhaustive check is O(N^2). This option prevents the exhaustive portion of rename/copy detection from running if the number of source/destination files involved exceeds the specified number. Defaults to `diff.renameLimit`. Note that a value of 0 is treated as unlimited. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--Oorderfile)`-O`_< orderfile>_ 
    
Control the order in which files appear in the output. This overrides the `diff.orderFile` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). To cancel `diff.orderFile`, use `-O/dev/null`.
The output order is determined by the order of glob patterns in _< orderfile>_. All files with pathnames that match the first pattern are output first, all files with pathnames that match the second pattern (but not the first) are output next, and so on. All files with pathnames that do not match any pattern are output last, as if there was an implicit match-all pattern at the end of the file. If multiple pathnames have the same rank (they match the same pattern but no earlier patterns), their output order relative to each other is the normal order.
_< orderfile>_ is parsed as follows:
  * Blank lines are ignored, so they can be used as separators for readability.
  * Lines starting with a hash ("`#`") are ignored, so they can be used for comments. Add a backslash ("_\_ ") to the beginning of the pattern if it starts with a hash.
  * Each other line contains a single pattern.


Patterns have the same syntax and semantics as patterns used for `fnmatch`(3) without the `FNM_PATHNAME` flag, except a pathname also matches a pattern if removing any number of the final pathname components matches the pattern. For example, the pattern "`foo*bar`" matches "`fooasdfbar`" and "`foo/bar/baz/asdf`" but not "`foobarx`". 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---skip-tofile)`--skip-to=`_< file>_ 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---rotate-tofile)`--rotate-to=`_< file>_ 
    
Discard the files before the named _< file>_ from the output (i.e. _skip to_), or move them to the end of the output (i.e. _rotate to_). These options were invented primarily for the use of the `git` `difftool` command, and may not be very useful otherwise. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---relativepath)`--relative`[`=`_< path>_] 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-relative)`--no-relative` 
    
When run from a subdirectory of the project, it can be told to exclude changes outside the directory and show pathnames relative to it with this option. When you are not in a subdirectory (e.g. in a bare repository), you can name which subdirectory to make the output relative to by giving a _< path>_ as an argument. `--no-relative` can be used to countermand both `diff.relative` config option and previous `--relative`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--a)`-a` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---text)`--text` 
    
Treat all files as text. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-cr-at-eol)`--ignore-cr-at-eol` 
    
Ignore carriage-return at the end of line when doing a comparison. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-space-at-eol)`--ignore-space-at-eol` 
    
Ignore changes in whitespace at EOL. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--b)`-b` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-space-change)`--ignore-space-change` 
    
Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--w)`-w` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-all-space)`--ignore-all-space` 
    
Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-blank-lines)`--ignore-blank-lines` 
    
Ignore changes whose lines are all blank. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--Iregex)`-I`_< regex>_ 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-matching-linesregex)`--ignore-matching-lines=`_< regex>_ 
    
Ignore changes whose all lines match _< regex>_. This option may be specified more than once. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---inter-hunk-contextnumber)`--inter-hunk-context=`_< number>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--W)`-W` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---function-context)`--function-context` 
    
Show whole function as context lines for each change. The function names are determined in the same way as `git` `diff` works out patch hunk headers (see "Defining a custom hunk-header" in [gitattributes[5]](https://git-scm.com/docs/gitattributes)). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ext-diff)`--ext-diff` 
    
Allow an external diff helper to be executed. If you set an external diff driver with [gitattributes[5]](https://git-scm.com/docs/gitattributes), you need to use this option with [git-log[1]](https://git-scm.com/docs/git-log) and friends. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-ext-diff)`--no-ext-diff` 
    
Disallow external diff drivers. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---textconv)`--textconv` 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-textconv)`--no-textconv` 
    
Allow (or disallow) external text conversion filters to be run when comparing binary files. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. Because textconv filters are typically a one-way conversion, the resulting diff is suitable for human consumption, but cannot be applied. For this reason, textconv filters are enabled by default only for [git-diff[1]](https://git-scm.com/docs/git-diff) and [git-log[1]](https://git-scm.com/docs/git-log), but not for [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) or diff plumbing commands. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-submodulesnoneuntrackeddirtyall)`--ignore-submodules`[`=`(`none`|`untracked`|`dirty`|`all`)] 
    
Ignore changes to submodules in the diff generation. `all` is the default. Using `none` will consider the submodule modified when it either contains untracked or modified files or its `HEAD` differs from the commit recorded in the superproject and can be used to override any settings of the `ignore` option in [git-config[1]](https://git-scm.com/docs/git-config) or [gitmodules[5]](https://git-scm.com/docs/gitmodules). When `untracked` is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using `dirty` ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior until 1.7.0). Using `all` hides all changes to submodules. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---src-prefixprefix)`--src-prefix=`_< prefix>_ 
    
Show the given source _< prefix>_ instead of "a/". 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---dst-prefixprefix)`--dst-prefix=`_< prefix>_ 
    
Show the given destination _< prefix>_ instead of "b/". 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-prefix)`--no-prefix` 
    
Do not show any source or destination prefix. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---default-prefix)`--default-prefix` 
    
Use the default source and destination prefixes ("a/" and "b/"). This overrides configuration variables such as `diff.noprefix`, `diff.srcPrefix`, `diff.dstPrefix`, and `diff.mnemonicPrefix` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---line-prefixprefix)`--line-prefix=`_< prefix>_ 
    
Prepend an additional _< prefix>_ to every line of output. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ita-invisible-in-index)`--ita-invisible-in-index` 
    
By default entries added by `git` `add` `-N` appear as an existing empty file in `git` `diff` and a new file in `git` `diff` `--cached`. This option makes the entry appear as a new file in `git` `diff` and non-existent in `git` `diff` `--cached`. This option could be reverted with `--ita-visible-in-index`. Both options are experimental and could be removed in future. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---max-depthdepth)--max-depth=<depth> 
    
For each pathspec given on command line, descend at most _< depth>_ levels of directories. A value of `-1` means no limit. Cannot be combined with wildcards in the pathspec. Given a tree containing `foo/bar/baz`, the following list shows the matches generated by each set of options:
  * `--max-depth=0` `--` `foo`: `foo`
  * `--max-depth=1` `--` `foo`: `foo/bar`
  * `--max-depth=1` `--` `foo/bar`: `foo/bar/baz`
  * `--max-depth=1` `--` `foo` `foo/bar`: `foo/bar/baz`
  * `--max-depth=2` `--` `foo`: `foo/bar/baz`


If no pathspec is given, the depth is measured as if all top-level entries were specified. Note that this is different than measuring from the root, in that `--max-depth=0` would still return `foo`. This allows you to still limit depth while asking for a subset of the top-level entries.
Note that this option is only supported for diffs between tree objects, not against the index or working tree.
For more detailed explanation on these common options, see also [gitdiffcore[7]](https://git-scm.com/docs/gitdiffcore). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--n)-<n> 
    
Prepare patches from the topmost <n> commits. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--odir)-o <dir> 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---output-directorydir)--output-directory <dir> 
    
Use <dir> to store the resulting files, instead of the current working directory. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--n-1)-n 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---numbered)--numbered 
    
Name output in _[PATCH n/m]_ format, even with a single patch. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--N)-N 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-numbered)--no-numbered 
    
Name output in _[PATCH]_ format. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---start-numbern)--start-number <n> 
    
Start numbering the patches at <n> instead of 1. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---numbered-files)--numbered-files 
    
Output file names will be a simple number sequence without the default first line of the commit appended. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--k)-k 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---keep-subject)--keep-subject 
    
Do not strip/add _[PATCH]_ from the first line of the commit log message. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--s)-s 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---signoff)--signoff 
    
Add a `Signed-off-by` trailer to the commit message, using the committer identity of yourself. See the signoff option in [git-commit[1]](https://git-scm.com/docs/git-commit) for more information. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---stdout)--stdout 
    
Print all commits to the standard output in mbox format, instead of creating a file for each one. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---attachboundary)--attach[=<boundary>] 
    
Create multipart/mixed attachment, the first part of which is the commit message and the patch itself in the second part, with `Content-Disposition:` `attachment`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-attach)--no-attach 
    
Disable the creation of an attachment, overriding the configuration setting. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---inlineboundary)--inline[=<boundary>] 
    
Create multipart/mixed attachment, the first part of which is the commit message and the patch itself in the second part, with `Content-Disposition:` `inline`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---threadstyle)--thread[=<style>] 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-thread)--no-thread 
    
Controls addition of `In-Reply-To` and `References` headers to make the second and subsequent mails appear as replies to the first. Also controls generation of the `Message-ID` header to reference.
The optional <style> argument can be either `shallow` or `deep`. _shallow_ threading makes every mail a reply to the head of the series, where the head is chosen from the cover letter, the `--in-reply-to`, and the first patch mail, in this order. _deep_ threading makes every mail a reply to the previous one.
The default is `--no-thread`, unless the `format.thread` configuration is set. `--thread` without an argument is equivalent to `--thread=shallow`.
Beware that the default for _git send-email_ is to thread emails itself. If you want `git` `format-patch` to take care of threading, you will want to ensure that threading is disabled for `git` `send-email`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---in-reply-tomessage-id)--in-reply-to=<message-id> 
    
Make the first mail (or all the mails with `--no-thread`) appear as a reply to the given <message-id>, which avoids breaking threads to provide a new patch series. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ignore-if-in-upstream)--ignore-if-in-upstream 
    
Do not include a patch that matches a commit in <until>..<since>. This will examine all patches reachable from <since> but not from <until> and compare them with the patches being generated, and any patch that matches is ignored. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---always)--always 
    
Include patches for commits that do not introduce any change, which are omitted by default. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---cover-from-descriptionmode)--cover-from-description=<mode> 
    
Controls which parts of the cover letter will be automatically populated using the branch’s description.
If _< mode>_ is `message` or `default`, the cover letter subject will be populated with placeholder text. The body of the cover letter will be populated with the branch’s description. This is the default mode when no configuration nor command line option is specified.
If _< mode>_ is `subject`, the first paragraph of the branch description will populate the cover letter subject. The remainder of the description will populate the body of the cover letter.
If _< mode>_ is `auto`, if the first paragraph of the branch description is greater than 100 bytes, then the mode will be `message`, otherwise `subject` will be used.
If _< mode>_ is `none`, both the cover letter subject and body will be populated with placeholder text. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---description-filefile)--description-file=<file> 
    
Use the contents of <file> instead of the branch’s description for generating the cover letter. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---subject-prefixsubject-prefix)--subject-prefix=<subject-prefix> 
    
Instead of the standard _[PATCH]_ prefix in the subject line, instead use _[ <subject-prefix>]_. This can be used to name a patch series, and can be combined with the `--numbered` option.
The configuration variable `format.subjectPrefix` may also be used to configure a subject prefix to apply to a given repository for all patches. This is often useful on mailing lists which receive patches for several repositories and can be used to disambiguate the patches (with a value of e.g. "PATCH my-project"). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---filename-max-lengthn)--filename-max-length=<n> 
    
Instead of the standard 64 bytes, chomp the generated output filenames at around _< n>_ bytes (too short a value will be silently raised to a reasonable length). Defaults to the value of the `format.filenameMaxLength` configuration variable, or 64 if unconfigured. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---rfcrfc)--rfc[=<rfc>] 
    
Prepends the string _< rfc>_ (defaults to "RFC") to the subject prefix. As the subject prefix defaults to "PATCH", you’ll get "RFC PATCH" by default.
RFC means "Request For Comments"; use this when sending an experimental patch for discussion rather than application. "--rfc=WIP" may also be a useful way to indicate that a patch is not complete yet ("WIP" stands for "Work In Progress").
If the convention of the receiving community for a particular extra string is to have it _after_ the subject prefix, the string _< rfc>_ can be prefixed with a dash ("`-`") to signal that the rest of the _< rfc>_ string should be appended to the subject prefix instead, e.g., `--rfc='-`(`WIP`) results in "PATCH (WIP)". 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--vn)-v <n> 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---reroll-countn)--reroll-count=<n> 
    
Mark the series as the <n>-th iteration of the topic. The output filenames have `v`_< n>_ prepended to them, and the subject prefix ("PATCH" by default, but configurable via the `--subject-prefix` option) has ` v<n>` appended to it. E.g. `--reroll-count=4` may produce `v4-0001-add-makefile.patch` file that has "Subject: [PATCH v4 1/20] Add makefile" in it. _< n>_ does not have to be an integer (e.g. "--reroll-count=4.4", or "--reroll-count=4rev2" are allowed), but the downside of using such a reroll-count is that the range-diff/interdiff with the previous version does not state exactly which version the new iteration is compared against. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---toemail)--to=<email> 
    
Add a `To:` header to the email headers. This is in addition to any configured headers, and may be used multiple times. The negated form `--no-to` discards all `To:` headers added so far (from config or command line). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---ccemail)--cc=<email> 
    
Add a `Cc:` header to the email headers. This is in addition to any configured headers, and may be used multiple times. The negated form `--no-cc` discards all `Cc:` headers added so far (from config or command line). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---from)--from 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---fromident)--from=<ident> 
    
Use `ident` in the `From:` header of each commit email. If the author ident of the commit is not textually identical to the provided `ident`, place a `From:` header in the body of the message with the original author. If no `ident` is given, use the committer ident.
Note that this option is only useful if you are actually sending the emails and want to identify yourself as the sender, but retain the original author (and `git` `am` will correctly pick up the in-body header). Note also that `git` `send-email` already handles this transformation for you, and this option should not be used if you are feeding the result to `git` `send-email`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---force-in-body-from)--force-in-body-from 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-force-in-body-from)--no-force-in-body-from 
    
With the e-mail sender specified via the `--from` option, by default, an in-body "From:" to identify the real author of the commit is added at the top of the commit log message if the sender is different from the author. With this option, the in-body "From:" is added even when the sender and the author have the same name and address, which may help if the mailing list software mangles the sender’s identity. Defaults to the value of the `format.forceInBodyFrom` configuration variable. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---add-headerheader)--add-header=<header> 
    
Add an arbitrary header to the email headers. This is in addition to any configured headers, and may be used multiple times. For example, `--add-header="Organization:` `git-foo"`. The negated form `--no-add-header` discards **all** (`To:`, `Cc:`, and custom) headers added so far from config or command line. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---cover-letter)--cover-letter 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-cover-letter)--no-cover-letter 
    
In addition to the patches, generate a cover letter file containing the branch description, shortlog and the overall diffstat. You can fill in a description in the file before sending it out. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---encode-email-headers)--encode-email-headers 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-encode-email-headers)--no-encode-email-headers 
    
Encode email headers that have non-ASCII characters with "Q-encoding" (described in RFC 2047), instead of outputting the headers verbatim. Defaults to the value of the `format.encodeEmailHeaders` configuration variable. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---interdiffprevious)--interdiff=<previous> 
    
As a reviewer aid, insert an interdiff into the cover letter, or as commentary of the lone patch of a 1-patch series, showing the differences between the previous version of the patch series and the series currently being formatted. `previous` is a single revision naming the tip of the previous series which shares a common base with the series being formatted (for example `git` `format-patch` `--cover-letter` `--interdiff=feature/v1` `-3` `feature/v2`). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---range-diffprevious)--range-diff=<previous> 
    
As a reviewer aid, insert a range-diff (see [git-range-diff[1]](https://git-scm.com/docs/git-range-diff)) into the cover letter, or as commentary of the lone patch of a 1-patch series, showing the differences between the previous version of the patch series and the series currently being formatted. `previous` can be a single revision naming the tip of the previous series if it shares a common base with the series being formatted (for example `git` `format-patch` `--cover-letter` `--range-diff=feature/v1` `-3` `feature/v2`), or a revision range if the two versions of the series are disjoint (for example `git` `format-patch` `--cover-letter` `--range-diff=feature/v1~3..feature/v1` `-3` `feature/v2`).
Note that diff options passed to the command affect how the primary product of `format-patch` is generated, and they are not passed to the underlying `range-diff` machinery used to generate the cover-letter material (this may change in the future). 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---creation-factorpercent)--creation-factor=<percent> 
    
Used with `--range-diff`, tweak the heuristic which matches up commits between the previous and current series of patches by adjusting the creation/deletion cost fudge factor. See [git-range-diff[1]](https://git-scm.com/docs/git-range-diff)) for details.
Defaults to 999 (the [git-range-diff[1]](https://git-scm.com/docs/git-range-diff) uses 60), as the use case is to show comparison with an older iteration of the same topic and the tool should find more correspondence between the two sets of patches. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---notesref)--notes[=<ref>] 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-notes)--no-notes 
    
Append the notes (see [git-notes[1]](https://git-scm.com/docs/git-notes)) for the commit after the three-dash line.
The expected use case of this is to write supporting explanation for the commit that does not belong to the commit log message proper, and include it with the patch submission. While one can simply write these explanations after `format-patch` has run but before sending, keeping them as Git notes allows them to be maintained between versions of the patch series (but see the discussion of the `notes.rewrite` configuration options in [git-notes[1]](https://git-scm.com/docs/git-notes) to use this workflow).
The default is `--no-notes`, unless the `format.notes` configuration is set. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---signaturesignature)--signature=<signature> 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-signature)--no-signature 
    
Add a signature to each message produced. Per RFC 3676 the signature is separated from the body by a line with '-- ' on it. If the signature option is omitted the signature defaults to the Git version number. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---signature-filefile)--signature-file=<file> 
    
Works just like --signature except the signature is read from a file. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---suffixsfx)--suffix=.<sfx> 
    
Instead of using `.patch` as the suffix for generated filenames, use specified suffix. A common alternative is `--suffix=.txt`. Leaving this empty will remove the `.patch` suffix.
Note that the leading character does not have to be a dot; for example, you can use `--suffix=-patch` to get `0001-description-of-my-change-patch`. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt--q)-q 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---quiet)--quiet 
    
Do not print the names of the generated files to standard output. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-binary)--no-binary 
    
Do not output contents of changes in binary files, instead display a notice that those files changed. Patches generated using this option cannot be applied properly, but they are still useful for code review. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---zero-commit)--zero-commit 
    
Output an all-zero hash in each patch’s From header instead of the hash of the commit. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---no-base)--no-base 


[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---basecommit)--base[=<commit>] 
    
Record the base tree information to identify the state the patch series applies to. See the BASE TREE INFORMATION section below for details. If <commit> is "auto", a base commit is automatically chosen. The `--no-base` option overrides a `format.useAutoBase` configuration. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---root)--root 
    
Treat the revision argument as a <revision-range>, even if it is just a single commit (that would normally be treated as a <since>). Note that root commits included in the specified range are always formatted as creation patches, independently of this flag. 

[](https://git-scm.com/docs/git-format-patch#Documentation/git-format-patch.txt---progress)--progress 
    
Show progress reports on stderr as patches are generated.
##  [](https://git-scm.com/docs/git-format-patch#_configuration)CONFIGURATION
You can specify extra mail header lines to be added to each message, defaults for the subject prefix and file suffix, number patches when outputting more than one patch, add "To:" or "Cc:" headers, configure attachments, change the patch output directory, and sign off patches with configuration variables.
```
[format]
	headers = "Organization: git-foo\n"
	subjectPrefix = CHANGE
	suffix = .txt
	numbered = auto
	to = <email>
	cc = <email>
	attach [ = mime-boundary-string ]
	signOff = true
	outputDirectory = <directory>
	coverLetter = auto
	coverFromDescription = auto
```

##  [](https://git-scm.com/docs/git-format-patch#_discussion)DISCUSSION
The patch produced by _git format-patch_ is in UNIX mailbox format, with a fixed "magic" time stamp to indicate that the file is output from format-patch rather than a real mailbox, like so:
```
From 8f72bad1baf19a53459661343e21d6491c3908d3 Mon Sep 17 00:00:00 2001
From: Tony Luck <tony.luck@intel.com>
Date: Tue, 13 Jul 2010 11:42:54 -0700
Subject: [PATCH] =?UTF-8?q?[IA64]=20Put=20ia64=20config=20files=20on=20the=20?=
 =?UTF-8?q?Uwe=20Kleine-K=C3=B6nig=20diet?=
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit

arch/arm config files were slimmed down using a python script
(See commit c2330e286f68f1c408b4aa6515ba49d57f05beae comment)

Do the same for ia64 so we can have sleek & trim looking
...
```

Typically it will be placed in a MUA’s drafts folder, edited to add timely commentary that should not go in the changelog after the three dashes, and then sent as a message whose body, in our example, starts with "arch/arm config files were…​". On the receiving end, readers can save interesting patches in a UNIX mailbox and apply them with [git-am[1]](https://git-scm.com/docs/git-am).
When a patch is part of an ongoing discussion, the patch generated by _git format-patch_ can be tweaked to take advantage of the _git am --scissors_ feature. After your response to the discussion comes a line that consists solely of "_-- >8 --_" (scissors and perforation), followed by the patch with unnecessary header fields removed:
```
...
> So we should do such-and-such.

Makes sense to me.  How about this patch?

-- >8 --
Subject: [IA64] Put ia64 config files on the Uwe Kleine-König diet

arch/arm config files were slimmed down using a python script
...
```

When sending a patch this way, most often you are sending your own patch, so in addition to the "`From` `$SHA1` `$magic_timestamp`" marker you should omit `From:` and `Date:` lines from the patch file. The patch title is likely to be different from the subject of the discussion the patch is in response to, so it is likely that you would want to keep the Subject: line, like the example above.
###  [](https://git-scm.com/docs/git-format-patch#_checking_for_patch_corruption)Checking for patch corruption
Many mailers if not set up properly will corrupt whitespace. Here are two common types of corruption:
  * Empty context lines that do not have _any_ whitespace.
  * Non-empty context lines that have one extra whitespace at the beginning.


One way to test if your MUA is set up correctly is:
  * Send the patch to yourself, exactly the way you would, except with To: and Cc: lines that do not contain the list and maintainer address.
  * Save that patch to a file in UNIX mailbox format. Call it a.patch, say.
  * Apply it:
```
$ git fetch <project> master:test-apply
$ git switch test-apply
$ git restore --source=HEAD --staged --worktree :/
$ git am a.patch
```



If it does not apply correctly, there can be various reasons.
  * The patch itself does not apply cleanly. That is _bad_ but does not have much to do with your MUA. You might want to rebase the patch with [git-rebase[1]](https://git-scm.com/docs/git-rebase) before regenerating it in this case.
  * The MUA corrupted your patch; "am" would complain that the patch does not apply. Look in the .git/rebase-apply/ subdirectory and see what _patch_ file contains and check for the common corruption patterns mentioned above.
  * While at it, check the _info_ and _final-commit_ files as well. If what is in _final-commit_ is not exactly what you would want to see in the commit log message, it is very likely that the receiver would end up hand editing the log message when applying your patch. Things like "Hi, this is my first patch.\n" in the patch e-mail should come after the three-dash line that signals the end of the commit message.


##  [](https://git-scm.com/docs/git-format-patch#_mua_specific_hints)MUA-SPECIFIC HINTS
Here are some hints on how to successfully submit patches inline using various mailers.
###  [](https://git-scm.com/docs/git-format-patch#_gmail)GMail
GMail does not have any way to turn off line wrapping in the web interface, so it will mangle any emails that you send. You can however use "git send-email" and send your patches through the GMail SMTP server, or use any IMAP email client to connect to the google IMAP server and forward the emails through that.
For hints on using _git send-email_ to send your patches through the GMail SMTP server, see the EXAMPLE section of [git-send-email[1]](https://git-scm.com/docs/git-send-email).
For hints on submission using the IMAP interface, see the EXAMPLE section of [git-imap-send[1]](https://git-scm.com/docs/git-imap-send).
###  [](https://git-scm.com/docs/git-format-patch#_thunderbird)Thunderbird
By default, Thunderbird will both wrap emails as well as flag them as being _format=flowed_ , both of which will make the resulting email unusable by Git.
There are three different approaches: use an add-on to turn off line wraps, configure Thunderbird to not mangle patches, or use an external editor to keep Thunderbird from mangling the patches.
####  [](https://git-scm.com/docs/git-format-patch#_approach_1_add_on)Approach #1 (add-on)
Install the Toggle Line Wrap add-on that is available from <https://addons.thunderbird.net/thunderbird/addon/toggle-line-wrap> It adds a button "Line Wrap" to the composer’s toolbar that you can tick off. Now you can compose the message as you otherwise do (cut + paste, _git format-patch_ | _git imap-send_ , etc), but you have to insert line breaks manually in any text that you type.
As a bonus feature, the add-on can detect patch text in the composer and warns when line wrapping has not yet been turned off.
The add-on requires a few tweaks of the advanced configuration (about:config). These are listed on the download page.
####  [](https://git-scm.com/docs/git-format-patch#_approach_2_configuration)Approach #2 (configuration)
Three steps:
  1. Configure your mail server composition as plain text: Edit…​Account Settings…​Composition & Addressing, uncheck "Compose Messages in HTML".
  2. Configure your general composition window to not wrap.
In Thunderbird 2: Edit..Preferences..Composition, wrap plain text messages at 0
In Thunderbird 3: Edit..Preferences..Advanced..Config Editor. Search for "mail.wrap_long_lines". Toggle it to make sure it is set to `false`. Also, search for "mailnews.wraplength" and set the value to 0.
  3. Disable the use of format=flowed: Edit..Preferences..Advanced..Config Editor. Search for "mailnews.send_plaintext_flowed". Toggle it to make sure it is set to `false`.


After that is done, you should be able to compose email as you otherwise would (cut + paste, _git format-patch_ | _git imap-send_ , etc), and the patches will not be mangled.
####  [](https://git-scm.com/docs/git-format-patch#_approach_3_external_editor)Approach #3 (external editor)
The following Thunderbird extensions are needed: AboutConfig from <https://mjg.github.io/AboutConfig/> and External Editor from [https://globs.org/articles.php?lng=en&pg=8](https://globs.org/articles.php?lng=en&pg=8)
  1. Prepare the patch as a text file using your method of choice.
  2. Before opening a compose window, use Edit→Account Settings to uncheck the "Compose messages in HTML format" setting in the "Composition & Addressing" panel of the account to be used to send the patch.
  3. In the main Thunderbird window, _before_ you open the compose window for the patch, use Tools→about:config to set the following to the indicated values:
```
	mailnews.send_plaintext_flowed  => false
	mailnews.wraplength             => 0
```

  4. Open a compose window and click the external editor icon.
  5. In the external editor window, read in the patch file and exit the editor normally.


Side note: it may be possible to do step 2 with about:config and the following settings but no one’s tried yet.
```
	mail.html_compose                       => false
	mail.identity.default.compose_html      => false
	mail.identity.id?.compose_html          => false
```

There is a script in contrib/thunderbird-patch-inline which can help you include patches with Thunderbird in an easy way. To use it, do the steps above and then use the script as the external editor.
###  [](https://git-scm.com/docs/git-format-patch#_kmail)KMail
This should help you to submit patches inline using KMail.
  1. Prepare the patch as a text file.
  2. Click on New Mail.
  3. Go under "Options" in the Composer window and be sure that "Word wrap" is not set.
  4. Use Message → Insert file…​ and insert the patch.
  5. Back in the compose window: add whatever other text you wish to the message, complete the addressing and subject fields, and press send.


##  [](https://git-scm.com/docs/git-format-patch#_base_tree_information)BASE TREE INFORMATION
The base tree information block is used for maintainers or third party testers to know the exact state the patch series applies to. It consists of the _base commit_ , which is a well-known commit that is part of the stable part of the project history everybody else works off of, and zero or more _prerequisite patches_ , which are well-known patches in flight that is not yet part of the _base commit_ that need to be applied on top of _base commit_ in topological order before the patches can be applied.
The _base commit_ is shown as "base-commit: " followed by the 40-hex of the commit object name. A _prerequisite patch_ is shown as "prerequisite-patch-id: " followed by the 40-hex _patch id_ , which can be obtained by passing the patch through the `git` `patch-id` `--stable` command.
Imagine that on top of the public commit P, you applied well-known patches X, Y and Z from somebody else, and then built your three-patch series A, B, C, the history would be like:
```
---P---X---Y---Z---A---B---C
```

With `git` `format-patch` `--base=P` `-3` `C` (or variants thereof, e.g. with `--cover-letter` or using `Z..C` instead of `-3` `C` to specify the range), the base tree information block is shown at the end of the first message the command outputs (either the first patch, or the cover letter), like this:
```
base-commit: P
prerequisite-patch-id: X
prerequisite-patch-id: Y
prerequisite-patch-id: Z
```

For non-linear topology, such as
```
---P---X---A---M---C
    \         /
     Y---Z---B
```

You can also use `git` `format-patch` `--base=P` `-3` `C` to generate patches for A, B and C, and the identifiers for P, X, Y, Z are appended at the end of the first message.
If set `--base=auto` in cmdline, it will automatically compute the base commit as the merge base of tip commit of the remote-tracking branch and revision-range specified in cmdline. For a local branch, you need to make it to track a remote branch by `git` `branch` `--set-upstream-to` before using this option.
##  [](https://git-scm.com/docs/git-format-patch#_examples)EXAMPLES
  * Extract commits between revisions R1 and R2, and apply them on top of the current branch using _git am_ to cherry-pick them:
```
$ git format-patch -k --stdout R1..R2 | git am -3 -k
```

  * Extract all commits which are in the current branch but not in the origin branch:
```
$ git format-patch origin
```

For each commit a separate file is created in the current directory.
  * Extract all commits that lead to _origin_ since the inception of the project:
```
$ git format-patch --root origin
```

  * The same as the previous one:
```
$ git format-patch -M -B origin
```

Additionally, it detects and handles renames and complete rewrites intelligently to produce a renaming patch. A renaming patch reduces the amount of text output, and generally makes it easier to review. Note that non-Git "patch" programs won’t understand renaming patches, so use it only when you know the recipient uses Git to apply your patch.
  * Extract three topmost commits from the current branch and format them as e-mailable patches:
```
$ git format-patch -3
```



##  [](https://git-scm.com/docs/git-format-patch#_caveats)CAVEATS
Note that `format-patch` will omit merge commits from the output, even if they are part of the requested range. A simple "patch" does not include enough information for the receiving end to reproduce the same merge commit.
##  [](https://git-scm.com/docs/git-format-patch#_see_also)SEE ALSO
[git-am[1]](https://git-scm.com/docs/git-am), [git-send-email[1]](https://git-scm.com/docs/git-send-email)
##  [](https://git-scm.com/docs/git-format-patch#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### format-patch
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
