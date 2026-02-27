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
    * [NAME](https://git-scm.com/docs/git-pull#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-pull#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-pull#_description)
    * [OPTIONS](https://git-scm.com/docs/git-pull#_options)
    * [GIT URLS](https://git-scm.com/docs/git-pull#_git_urls)
    * [REMOTES](https://git-scm.com/docs/git-pull#_remotes)
    * [UPSTREAM BRANCHES](https://git-scm.com/docs/git-pull#UPSTREAM-BRANCHES)
    * [MERGE STRATEGIES](https://git-scm.com/docs/git-pull#_merge_strategies)
    * [DEFAULT BEHAVIOUR](https://git-scm.com/docs/git-pull#DEFAULT-BEHAVIOUR)
    * [EXAMPLES](https://git-scm.com/docs/git-pull#_examples)
    * [SECURITY](https://git-scm.com/docs/git-pull#_security)
    * [BUGS](https://git-scm.com/docs/git-pull#_bugs)
    * [SEE ALSO](https://git-scm.com/docs/git-pull#_see_also)
    * [GIT](https://git-scm.com/docs/git-pull#_git)


[ English ▾](https://git-scm.com/docs/git-pull)
Localized versions of **git-pull** manual
  1. [English ](https://git-scm.com/docs/git-pull)
  2. [Français ](https://git-scm.com/docs/git-pull/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-pull/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-pull/sv)
  5. [українська мова ](https://git-scm.com/docs/git-pull/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-pull/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-pull)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-pull) git-pull last updated in 2.53.0
Changes in the **git-pull** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-pull/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-pull/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-pull/2.51.1)
  5. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-pull/2.51.0)
  6. 2.50.1 no changes
  7. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-pull/2.50.0)
  8. 2.49.1 no changes
  9. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-pull/2.49.0)
  10. 2.48.1 → 2.48.2 no changes
  11. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-pull/2.48.0)
  12. 2.47.2 → 2.47.3 no changes
  13. [2.47.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-25_ ](https://git-scm.com/docs/git-pull/2.47.1)
  14. 2.46.3 → 2.47.0 no changes
  15. [2.46.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-23_ ](https://git-scm.com/docs/git-pull/2.46.2)
  16. 2.45.1 → 2.46.1 no changes
  17. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-pull/2.45.0)
  18. 2.44.1 → 2.44.4 no changes
  19. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-pull/2.44.0)
  20. 2.43.2 → 2.43.7 no changes
  21. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-pull/2.43.1)
  22. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-pull/2.43.0)
  23. 2.42.1 → 2.42.4 no changes
  24. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-pull/2.42.0)
  25. 2.41.1 → 2.41.3 no changes
  26. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-pull/2.41.0)
  27. 2.40.1 → 2.40.4 no changes
  28. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-pull/2.40.0)
  29. 2.36.1 → 2.39.5 no changes
  30. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-pull/2.36.0)
  31. 2.35.1 → 2.35.8 no changes
  32. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-pull/2.35.0)
  33. 2.34.1 → 2.34.8 no changes
  34. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-pull/2.34.0)
  35. 2.33.2 → 2.33.8 no changes
  36. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git-pull/2.33.1)
  37. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-pull/2.33.0)
  38. 2.32.1 → 2.32.7 no changes
  39. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-pull/2.32.0)
  40. 2.31.1 → 2.31.8 no changes
  41. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-pull/2.31.0)
  42. 2.30.1 → 2.30.9 no changes
  43. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-pull/2.30.0)
  44. 2.29.1 → 2.29.3 no changes
  45. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-pull/2.29.0)
  46. 2.27.1 → 2.28.1 no changes
  47. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-pull/2.27.0)
  48. 2.25.2 → 2.26.3 no changes
  49. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-pull/2.25.1)
  50. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-pull/2.25.0)
  51. 2.24.1 → 2.24.4 no changes
  52. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-pull/2.24.0)
  53. 2.23.1 → 2.23.4 no changes
  54. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-pull/2.23.0)
  55. 2.22.2 → 2.22.5 no changes
  56. [2.22.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-11_ ](https://git-scm.com/docs/git-pull/2.22.1)
  57. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-pull/2.22.0)
  58. 2.20.1 → 2.21.4 no changes
  59. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-pull/2.20.0)
  60. 2.19.1 → 2.19.6 no changes
  61. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-pull/2.19.0)
  62. 2.18.1 → 2.18.5 no changes
  63. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-pull/2.18.0)
  64. 2.17.1 → 2.17.6 no changes
  65. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-pull/2.17.0)
  66. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-pull/2.16.6)
  67. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-pull/2.15.4)
  68. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-pull/2.14.6)
  69. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-pull/2.13.7)
  70. 2.12.5 no changes
  71. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-pull/2.11.4)
  72. 2.10.5 no changes
  73. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-pull/2.9.5)
  74. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-pull/2.8.6)
  75. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-pull/2.7.6)
  76. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-pull/2.6.7)
  77. 2.5.6 no changes
  78. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-pull/2.4.12)
  79. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-pull/2.3.10)
  80. 2.2.3 no changes
  81. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-pull/2.1.4)
  82. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-pull/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-pull#_name)NAME
git-pull - Fetch from and integrate with another repository or a local branch
##  [](https://git-scm.com/docs/git-pull#_synopsis)SYNOPSIS
```
git pull [_<options>_] [_<repository>_ [_<refspec>_…​]]
```

##  [](https://git-scm.com/docs/git-pull#_description)DESCRIPTION
Integrate changes from a remote repository into the current branch.
First, `git` `pull` runs `git` `fetch` with the same arguments (excluding merge options) to fetch remote branch(es). Then it decides which remote branch to integrate: if you run `git` `pull` with no arguments this defaults to the [upstream](https://git-scm.com/docs/git-pull#UPSTREAM-BRANCHES) for the current branch. Then it integrates that branch into the current branch.
There are 4 main options for integrating the remote branch:
  1. `git` `pull` `--ff-only` will only do "fast-forward" updates: it fails if your local branch has diverged from the remote branch. This is the default.
  2. `git` `pull` `--rebase` runs `git` `rebase`
  3. `git` `pull` `--no-rebase` runs `git` `merge`.
  4. `git` `pull` `--squash` runs `git` `merge` `--squash`


You can also set the configuration options `pull.rebase`, `pull.squash`, or `pull.ff` with your preferred behaviour.
If there’s a merge conflict during the merge or rebase that you don’t want to handle, you can safely abort it with `git` `merge` `--abort` or `git` `rebase` `--abort`.
##  [](https://git-scm.com/docs/git-pull#_options)OPTIONS 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-repository)_< repository>_ 
    
The "remote" repository to pull from. This can be either a URL (see the section [GIT URLS](https://git-scm.com/docs/git-pull#URLS) below) or the name of a remote (see the section [REMOTES](https://git-scm.com/docs/git-pull#REMOTES) below).
Defaults to the configured upstream for the current branch, or `origin`. See [UPSTREAM BRANCHES](https://git-scm.com/docs/git-pull#UPSTREAM-BRANCHES) below for more on how to configure upstreams. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-refspec)_< refspec>_ 
    
Which branch or other reference(s) to fetch and integrate into the current branch, for example `main` in `git` `pull` `origin` `main`. Defaults to the configured upstream for the current branch.
This can be a branch, tag, or other collection of reference(s). See [_< refspec>_](https://git-scm.com/docs/git-pull#fetch-refspec) below under "Options related to fetching" for the full syntax, and [DEFAULT BEHAVIOUR](https://git-scm.com/docs/git-pull#DEFAULT-BEHAVIOUR) below for how `git` `pull` uses this argument to determine which remote branch to integrate. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--q)`-q` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---quiet)`--quiet` 
    
This is passed to both underlying git-fetch to squelch reporting of during transfer, and underlying git-merge to squelch output during merging. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--v)`-v` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---verbose)`--verbose` 
    
Pass `--verbose` to git-fetch and git-merge. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---recurse-submodulesyeson-demandno)`--recurse-submodules`[`=`(`yes`|`on-demand`|`no`)] 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-recurse-submodules)`--no-recurse-submodules` 
    
This option controls if new commits of populated submodules should be fetched, and if the working trees of active submodules should be updated, too (see [git-fetch[1]](https://git-scm.com/docs/git-fetch), [git-config[1]](https://git-scm.com/docs/git-config) and [gitmodules[5]](https://git-scm.com/docs/gitmodules)).
If the checkout is done via rebase, local submodule commits are rebased as well.
If the update is done via merge, the submodule conflicts are resolved and checked out.
###  [](https://git-scm.com/docs/git-pull#_options_related_to_merging)Options related to merging 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---commit)`--commit` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-commit)`--no-commit` 
    
Perform the merge and commit the result. This option can be used to override `--no-commit`. Only useful when merging.
With `--no-commit` perform the merge and stop just before creating a merge commit, to give the user a chance to inspect and further tweak the merge result before committing.
Note that fast-forward updates do not create a merge commit and therefore there is no way to stop those merges with `--no-commit`. Thus, if you want to ensure your branch is not changed or updated by the merge command, use `--no-ff` with `--no-commit`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---edit)`--edit` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--e)`-e` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-edit)`--no-edit` 
    
Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain and justify the merge. The `--no-edit` option can be used to accept the auto-generated message (this is generally discouraged).
Older scripts may depend on the historical behaviour of not allowing the user to edit the merge log message. They will see an editor opened when they run `git` `merge`. To make it easier to adjust such scripts to the updated behaviour, the environment variable `GIT_MERGE_AUTOEDIT` can be set to `no` at the beginning of them. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---cleanupmode)`--cleanup=`_< mode>_ 
    
This option determines how the merge message will be cleaned up before committing. See [git-commit[1]](https://git-scm.com/docs/git-commit) for more details. In addition, if the _< mode>_ is given a value of `scissors`, scissors will be appended to `MERGE_MSG` before being passed on to the commit machinery in the case of a merge conflict. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---ff-only)`--ff-only` 
    
Only update to the new history if there is no divergent local history. This is the default when no method for reconciling divergent histories is provided (via the `--rebase` flags). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---ff)`--ff` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-ff)`--no-ff` 
    
When merging rather than rebasing, specifies how a merge is handled when the merged-in history is already a descendant of the current history. If merging is requested, `--ff` is the default unless merging an annotated (and possibly signed) tag that is not stored in its natural place in the `refs/tags/` hierarchy, in which case `--no-ff` is assumed.
With `--ff`, when possible resolve the merge as a fast-forward (only update the branch pointer to match the merged branch; do not create a merge commit). When not possible (when the merged-in history is not a descendant of the current history), create a merge commit.
With `--no-ff`, create a merge commit in all cases, even when the merge could instead be resolved as a fast-forward. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--Skey-id)`-S`[_< key-id>_] 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---gpg-signkey-id)`--gpg-sign`[`=`_< key-id>_] 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-gpg-sign)`--no-gpg-sign` 
    
GPG-sign the resulting merge commit. The _< key-id>_ argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---logn)`--log`[`=`_< n>_] 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-log)`--no-log` 
    
In addition to branch names, populate the log message with one-line descriptions from at most _< n>_ actual commits that are being merged. See also [git-fmt-merge-msg[1]](https://git-scm.com/docs/git-fmt-merge-msg). Only useful when merging.
With `--no-log` do not list one-line descriptions from the actual commits being merged. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---signoff)`--signoff` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-signoff)`--no-signoff` 
    
Add a `Signed-off-by` trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you’re committing. For example, it may certify that the committer has the rights to submit the work under the project’s license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See <https://developercertificate.org> for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you’re contributing to understand how the signoffs are used in that project.
The `--no-signoff` option can be used to countermand an earlier `--signoff` option on the command line.
Git does not (and will not) have a configuration variable to enable the `--signoff` command line option by default; see the `commit.signoff` entry in [gitfaq[7]](https://git-scm.com/docs/gitfaq) for more details. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---stat)`--stat` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--n)`-n` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-stat)`--no-stat` 
    
Show a diffstat at the end of the merge. The diffstat is also controlled by the configuration option merge.stat.
With `-n` or `--no-stat` do not show a diffstat at the end of the merge. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---compact-summary)`--compact-summary` 
    
Show a compact-summary at the end of the merge. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---squash)`--squash` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-squash)`--no-squash` 
    
Produce the working tree and index state as if a real merge happened (except for the merge information), but do not actually make a commit, move the `HEAD`, or record `$GIT_DIR/MERGE_HEAD` (to cause the next `git` `commit` command to create a merge commit). This allows you to create a single commit on top of the current branch whose effect is the same as merging another branch (or more in case of an octopus).
With `--no-squash` perform the merge and commit the result. This option can be used to override `--squash`.
With `--squash`, `--commit` is not allowed, and will fail.
Only useful when merging. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---verify)`--verify` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-verify)`--no-verify` 
    
By default, the pre-merge and commit-msg hooks are run. When `--no-verify` is given, these are bypassed. See also [githooks[5]](https://git-scm.com/docs/githooks). Only useful when merging. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--sstrategy)`-s` _< strategy>_ 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---strategystrategy)`--strategy=`_< strategy>_ 
    
Use the given merge strategy; can be supplied more than once to specify them in the order they should be tried. If there is no `-s` option, a built-in list of strategies is used instead (`ort` when merging a single head, `octopus` otherwise). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--Xoption)`-X` _< option>_ 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---strategy-optionoption)`--strategy-option=`_< option>_ 
    
Pass merge strategy specific option through to the merge strategy. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---verify-signatures)`--verify-signatures` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-verify-signatures)`--no-verify-signatures` 
    
Verify that the tip commit of the side branch being merged is signed with a valid key, i.e. a key that has a valid uid: in the default trust model, this means the signing key has been signed by a trusted key. If the tip commit of the side branch is not signed with a valid key, the merge is aborted.
Only useful when merging. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---summary)`--summary` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-summary)`--no-summary` 
    
Synonyms to `--stat` and `--no-stat`; these are deprecated and will be removed in the future. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---autostash)`--autostash` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-autostash)`--no-autostash` 
    
Automatically create a temporary stash entry before the operation begins, record it in the ref `MERGE_AUTOSTASH` and apply it after the operation ends. This means that you can run the operation on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---allow-unrelated-histories)`--allow-unrelated-histories` 
    
By default, `git` `merge` command refuses to merge histories that do not share a common ancestor. This option can be used to override this safety when merging histories of two projects that started their lives independently. As that is a very rare occasion, no configuration variable to enable this by default exists or will be added.
Only useful when merging. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--r)`-r` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---rebasetruemergesfalseinteractive)`--rebase`[`=`(`true`|`merges`|`false`|`interactive`)] 
     

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-true)`true` 
    
rebase the current branch on top of the upstream branch after fetching. If there is a remote-tracking branch corresponding to the upstream branch and the upstream branch was rebased since last fetched, the rebase uses that information to avoid rebasing non-local changes. This is the default. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-merges)`merges` 
    
rebase using `git` `rebase` `--rebase-merges` so that the local merge commits are included in the rebase (see [git-rebase[1]](https://git-scm.com/docs/git-rebase) for details). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-false)`false` 
    
merge the upstream branch into the current branch. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-interactive)`interactive` 
    
enable the interactive mode of rebase.
See `pull.rebase`, `branch.`_< name>_`.rebase` and `branch.autoSetupRebase` in [git-config[1]](https://git-scm.com/docs/git-config) if you want to make `git` `pull` always use `--rebase` instead of merging.
+
Note |  This is a potentially _dangerous_ mode of operation. It rewrites history, which does not bode well when you published that history already. Do **not** use this option unless you have read [git-rebase[1]](https://git-scm.com/docs/git-rebase) carefully.   
---|--- 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-rebase)`--no-rebase` 
      
This is shorthand for `--rebase=false`.
###  [](https://git-scm.com/docs/git-pull#_options_related_to_fetching)Options related to fetching 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---all)`--all` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-all)`--no-all` 
    
Fetch all remotes, except for the ones that has the `remote.`_< name>_`.skipFetchAll` configuration variable set. This overrides the configuration variable `fetch.all`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--a)`-a` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---append)`--append` 
    
Append ref names and object names of fetched refs to the existing contents of `.git/FETCH_HEAD`. Without this option old data in `.git/FETCH_HEAD` will be overwritten. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---atomic)`--atomic` 
    
Use an atomic transaction to update local refs. Either all refs are updated, or on error, no refs are updated. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---depthdepth)`--depth=`_< depth>_ 
    
Limit fetching to the specified number of commits from the tip of each remote branch history. If fetching to a _shallow_ repository created by `git` `clone` with `--depth=`_< depth>_ option (see [git-clone[1]](https://git-scm.com/docs/git-clone)), deepen or shorten the history to the specified number of commits. Tags for the deepened commits are not fetched. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---deependepth)`--deepen=`_< depth>_ 
    
Similar to `--depth`, except it specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---shallow-sincedate)`--shallow-since=`_< date>_ 
    
Deepen or shorten the history of a shallow repository to include all reachable commits after _< date>_. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---shallow-excluderef)`--shallow-exclude=`_< ref>_ 
    
Deepen or shorten the history of a shallow repository to exclude commits reachable from a specified remote branch or tag. This option can be specified multiple times. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---unshallow)`--unshallow` 
    
If the source repository is complete, convert a shallow repository to a complete one, removing all the limitations imposed by shallow repositories.
If the source repository is shallow, fetch as much as possible so that the current repository has the same history as the source repository. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---update-shallow)`--update-shallow` 
    
By default when fetching from a shallow repository, `git` `fetch` refuses refs that require updating `.git/shallow`. This option updates `.git/shallow` and accepts such refs. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---negotiation-tipcommitglob)`--negotiation-tip=`(_< commit>_|_< glob>_) 
    
By default, Git will report, to the server, commits reachable from all local refs to find common commits in an attempt to reduce the size of the to-be-received packfile. If specified, Git will only report commits reachable from the given tips. This is useful to speed up fetches when the user knows which local ref is likely to have commits in common with the upstream ref being fetched.
This option may be specified more than once; if so, Git will report commits reachable from any of the given commits.
The argument to this option may be a glob on ref names, a ref, or the (possibly abbreviated) SHA-1 of a commit. Specifying a glob is equivalent to specifying this option multiple times, one for each matching ref name.
See also the `fetch.negotiationAlgorithm` and `push.negotiate` configuration variables documented in [git-config[1]](https://git-scm.com/docs/git-config), and the `--negotiate-only` option below. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---negotiate-only)`--negotiate-only` 
    
Do not fetch anything from the server, and instead print the ancestors of the provided `--negotiation-tip=` arguments, which we have in common with the server.
This is incompatible with `--recurse-submodules=`(`yes`|`on-demand`). Internally this is used to implement the `push.negotiate` option, see [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---dry-run)`--dry-run` 
    
Show what would be done, without making any changes. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---porcelain)`--porcelain` 
    
Print the output to standard output in an easy-to-parse format for scripts. See section OUTPUT in [git-fetch[1]](https://git-scm.com/docs/git-fetch) for details.
This is incompatible with `--recurse-submodules=`(`yes`|`on-demand`) and takes precedence over the `fetch.output` config option. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--f)`-f` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---force)`--force` 
    
When `git` `fetch` is used with _< src>_`:`_< dst>_ refspec, it may refuse to update the local branch as discussed in the _< refspec>_ part of the [git-fetch[1]](https://git-scm.com/docs/git-fetch) documentation. This option overrides that check. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--k)`-k` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---keep)`--keep` 
    
Keep downloaded pack. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---prefetch)`--prefetch` 
    
Modify the configured refspec to place all refs into the `refs/prefetch/` namespace. See the `prefetch` task in [git-maintenance[1]](https://git-scm.com/docs/git-maintenance). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--p)`-p` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---prune)`--prune` 
    
Before fetching, remove any remote-tracking references that no longer exist on the remote. Tags are not subject to pruning if they are fetched only because of the default tag auto-following or due to a `--tags` option. However, if tags are fetched due to an explicit refspec (either on the command line or in the remote configuration, for example if the remote was cloned with the `--mirror` option), then they are also subject to pruning. Supplying `--prune-tags` is a shorthand for providing the tag refspec. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-tags)`--no-tags` 
    
By default, tags that point at objects that are downloaded from the remote repository are fetched and stored locally. This option disables this automatic tag following. The default behavior for a remote may be specified with the `remote.`_< name>_`.tagOpt` setting. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---refmaprefspec)`--refmap=`_< refspec>_ 
    
When fetching refs listed on the command line, use the specified refspec (can be given more than once) to map the refs to remote-tracking branches, instead of the values of `remote.`_< name>_`.fetch` configuration variables for the remote repository. Providing an empty _< refspec>_ to the `--refmap` option causes Git to ignore the configured refspecs and rely entirely on the refspecs supplied as command-line arguments. See section on "Configured Remote-tracking Branches" for details. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--t)`-t` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---tags)`--tags` 
    
Fetch all tags from the remote (i.e., fetch remote tags `refs/tags/*` into local tags with the same name), in addition to whatever else would otherwise be fetched. Using this option alone does not subject tags to pruning, even if `--prune` is used (though tags may be pruned anyway if they are also the destination of an explicit refspec; see `--prune`). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--jn)`-j` _< n>_ 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---jobsn)`--jobs=`_< n>_ 
    
Parallelize all forms of fetching up to _< n>_ jobs at a time.
If the `--multiple` option was specified, the different remotes will be fetched in parallel. If multiple submodules are fetched, they will be fetched in parallel. To control them independently, use the config settings `fetch.parallel` and `submodule.fetchJobs` (see [git-config[1]](https://git-scm.com/docs/git-config)).
Typically, parallel recursive and multi-remote fetches will be faster. By default fetches are performed sequentially, not in parallel. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---set-upstream)`--set-upstream` 
    
If the remote is fetched successfully, add upstream (tracking) reference, used by argument-less [git-pull[1]](https://git-scm.com/docs/git-pull) and other commands. For more information, see `branch.`_< name>_`.merge` and `branch.`_< name>_`.remote` in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---upload-packupload-pack)`--upload-pack` _< upload-pack>_ 
    
When given, and the repository to fetch from is handled by `git` `fetch-pack`, `--exec=`_< upload-pack>_ is passed to the command to specify non-default path for the command run on the other end. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---progress)`--progress` 
    
Progress status is reported on the standard error stream by default when it is attached to a terminal, unless `-q` is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--ooption)`-o` _< option>_ 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---server-optionoption)`--server-option=`_< option>_ 
    
Transmit the given string to the server when communicating using protocol version 2. The given string must not contain a _NUL_ or _LF_ character. The server’s handling of server options, including unknown ones, is server-specific. When multiple `--server-option=`_< option>_ are given, they are all sent to the other side in the order listed on the command line. When no `--server-option=`_< option>_ is given from the command line, the values of configuration variable `remote.`_< name>_`.serverOption` are used instead. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---show-forced-updates)`--show-forced-updates` 
    
By default, git checks if a branch is force-updated during fetch. This can be disabled through `fetch.showForcedUpdates`, but the `--show-forced-updates` option guarantees this check occurs. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---no-show-forced-updates)`--no-show-forced-updates` 
    
By default, git checks if a branch is force-updated during fetch. Pass `--no-show-forced-updates` or set `fetch.showForcedUpdates` to false to skip this check for performance reasons. If used during `git-pull` the `--ff-only` option will still check for forced updates before attempting a fast-forward update. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--4)`-4` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---ipv4)`--ipv4` 
    
Use IPv4 addresses only, ignoring IPv6 addresses. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt--6)`-6` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---ipv6)`--ipv6` 
    
Use IPv6 addresses only, ignoring IPv4 addresses. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-repository-1)_< repository>_ 
    
The "remote" repository that is the source of a fetch or pull operation. This parameter can be either a URL (see the section [GIT URLS](https://git-scm.com/docs/git-pull#URLS) below) or the name of a remote (see the section [REMOTES](https://git-scm.com/docs/git-pull#REMOTES) below). 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-refspec-1)_< refspec>_ 
    
Specifies which refs to fetch and which local refs to update. When no _< refspec>_s appear on the command line, the refs to fetch are read from `remote.`_< repository>_`.fetch` variables instead (see the section "CONFIGURED REMOTE-TRACKING BRANCHES" in [git-fetch[1]](https://git-scm.com/docs/git-fetch)).
The format of a _< refspec>_ parameter is an optional plus `+`, followed by the source _< src>_, followed by a colon `:`, followed by the destination _< dst>_. The colon can be omitted when _< dst>_ is empty. _< src>_ is typically a ref, or a glob pattern with a single `*` that is used to match a set of refs, but it can also be a fully spelled hex object name.
A _< refspec>_ may contain a `*` in its _< src>_ to indicate a simple pattern match. Such a refspec functions like a glob that matches any ref with the pattern. A pattern _< refspec>_ must have one and only one `*` in both the _< src>_ and _< dst>_. It will map refs to the destination by replacing the `*` with the contents matched from the source.
If a refspec is prefixed by `^`, it will be interpreted as a negative refspec. Rather than specifying which refs to fetch or which local refs to update, such a refspec will instead specify refs to exclude. A ref will be considered to match if it matches at least one positive refspec, and does not match any negative refspec. Negative refspecs can be useful to restrict the scope of a pattern refspec so that it will not include specific refs. Negative refspecs can themselves be pattern refspecs. However, they may only contain a _< src>_ and do not specify a _< dst>_. Fully spelled out hex object names are also not supported.
`tag` _< tag>_ means the same as `refs/tags/`_< tag>_`:refs/tags/`_< tag>_; it requests fetching everything up to the given tag.
The remote ref that matches _< src>_ is fetched, and if _< dst>_ is not an empty string, an attempt is made to update the local ref that matches it.
Whether that update is allowed without `--force` depends on the ref namespace it’s being fetched to, the type of object being fetched, and whether the update is considered to be a fast-forward. Generally, the same rules apply for fetching as when pushing, see the _< refspec>_... section of [git-push[1]](https://git-scm.com/docs/git-push) for what those are. Exceptions to those rules particular to `git` `fetch` are noted below.
Until Git version 2.20, and unlike when pushing with [git-push[1]](https://git-scm.com/docs/git-push), any updates to `refs/tags/*` would be accepted without `+` in the refspec (or `--force`). When fetching, we promiscuously considered all tag updates from a remote to be forced fetches. Since Git version 2.20, fetching to update `refs/tags/*` works the same way as when pushing. I.e. any updates will be rejected without `+` in the refspec (or `--force`).
Unlike when pushing with [git-push[1]](https://git-scm.com/docs/git-push), any updates outside of `refs/{tags,heads}/*` will be accepted without `+` in the refspec (or `--force`), whether that’s swapping e.g. a tree object for a blob, or a commit for another commit that doesn’t have the previous commit as an ancestor etc.
Unlike when pushing with [git-push[1]](https://git-scm.com/docs/git-push), there is no configuration which’ll amend these rules, and nothing like a `pre-fetch` hook analogous to the `pre-receive` hook.
As with pushing with [git-push[1]](https://git-scm.com/docs/git-push), all of the rules described above about what’s not allowed as an update can be overridden by adding an optional leading `+` to a refspec (or using the `--force` command line option). The only exception to this is that no amount of forcing will make the `refs/heads/*` namespace accept a non-commit object.
Note |  When the remote branch you want to fetch is known to be rewound and rebased regularly, it is expected that its new tip will not be a descendant of its previous tip (as stored in your remote-tracking branch the last time you fetched). You would want to use the `+` sign to indicate non-fast-forward updates will be needed for such branches. There is no way to determine or declare that a branch will be made available in a repository with this behavior; the pulling user simply must know this is the expected usage pattern for a branch.   
---|---  
Note |  There is a difference between listing multiple _< refspec>_ directly on `git` `pull` command line and having multiple `remote.`_< repository>_`.fetch` entries in your configuration for a _< repository>_ and running a `git` `pull` command without any explicit _< refspec>_ parameters. _< refspec>_s listed explicitly on the command line are always merged into the current branch after fetching. In other words, if you list more than one remote ref, `git` `pull` will create an Octopus merge. On the other hand, if you do not list any explicit _< refspec>_ parameter on the command line, `git` `pull` will fetch all the _< refspec>_s it finds in the `remote.`_< repository>_`.fetch` configuration and merge only the first _< refspec>_ found into the current branch. This is because making an Octopus from remote refs is rarely done, while keeping track of multiple remote heads in one-go by fetching more than one is often useful.   
---|---  
##  [](https://git-scm.com/docs/git-pull#_git_urls)GIT URLS
In general, URLs contain information about the transport protocol, the address of the remote server, and the path to the repository. Depending on the transport protocol, some of this information may be absent.
Git supports ssh, git, http, and https protocols (in addition, ftp and ftps can be used for fetching, but this is inefficient and deprecated; do not use them).
The native transport (i.e. `git://` URL) does no authentication and should be used with caution on unsecured networks.
The following syntaxes may be used with them:
  * `ssh://`[_< user>_`@`]_< host>_[`:`_< port>_]`/`_< path-to-git-repo>_
  * `git://`_< host>_[`:`_< port>_]`/`_< path-to-git-repo>_
  * `http`[`s`]`://`_< host>_[`:`_< port>_]`/`_< path-to-git-repo>_
  * `ftp`[`s`]`://`_< host>_[`:`_< port>_]`/`_< path-to-git-repo>_


An alternative scp-like syntax may also be used with the ssh protocol:
  * [_< user>_`@`]_< host>_`:/`_< path-to-git-repo>_


This syntax is only recognized if there are no slashes before the first colon. This helps differentiate a local path that contains a colon. For example the local path `foo:bar` could be specified as an absolute path or `./foo:bar` to avoid being misinterpreted as an ssh url.
The ssh and git protocols additionally support `~`_< username>_ expansion:
  * `ssh://`[_< user>_`@`]_< host>_[`:`_< port>_]`/~`_< user>_`/`_< path-to-git-repo>_
  * `git://`_< host>_[`:`_< port>_]`/~`_< user>_`/`_< path-to-git-repo>_
  * [_< user>_`@`]_< host>_`:~`_< user>_`/`_< path-to-git-repo>_


For local repositories, also supported by Git natively, the following syntaxes may be used:
  * `/path/to/repo.git/`
  * `file:///path/to/repo.git/`


These two syntaxes are mostly equivalent, except when cloning, when the former implies `--local` option. See [git-clone[1]](https://git-scm.com/docs/git-clone) for details.
`git` `clone`, `git` `fetch` and `git` `pull`, but not `git` `push`, will also accept a suitable bundle file. See [git-bundle[1]](https://git-scm.com/docs/git-bundle).
When Git doesn’t know how to handle a certain transport protocol, it attempts to use the `remote-`_< transport>_ remote helper, if one exists. To explicitly request a remote helper, the following syntax may be used:
  * _< transport>_`::`_< address>_


where _< address>_ may be a path, a server and path, or an arbitrary URL-like string recognized by the specific remote helper being invoked. See [gitremote-helpers[7]](https://git-scm.com/docs/gitremote-helpers) for details.
If there are a large number of similarly-named remote repositories and you want to use a different format for them (such that the URLs you use will be rewritten into URLs that work), you can create a configuration section of the form:
```
	[url "_<actual-url-base>_"]
		insteadOf = _<other-url-base>_
```

For example, with this:
```
	[url "git://git.host.xz/"]
		insteadOf = host.xz:/path/to/
		insteadOf = work:
```

a URL like "work:repo.git" or like "host.xz:/path/to/repo.git" will be rewritten in any context that takes a URL to be "git://git.host.xz/repo.git".
If you want to rewrite URLs for push only, you can create a configuration section of the form:
```
	[url "_<actual-url-base>_"]
		pushInsteadOf = _<other-url-base>_
```

For example, with this:
```
	[url "ssh://example.org/"]
		pushInsteadOf = git://example.org/
```

a URL like "git://example.org/path/to/repo.git" will be rewritten to "ssh://example.org/path/to/repo.git" for pushes, but pulls will still use the original URL.
##  [](https://git-scm.com/docs/git-pull#_remotes)REMOTES
The name of one of the following can be used instead of a URL as _< repository>_ argument:
  * a remote in the Git configuration file: `$GIT_DIR/config`,
  * a file in the `$GIT_DIR/remotes` directory, or
  * a file in the `$GIT_DIR/branches` directory.


All of these also allow you to omit the refspec from the command line because they each contain a refspec which git will use by default.
###  [](https://git-scm.com/docs/git-pull#_named_remote_in_configuration_file)Named remote in configuration file
You can choose to provide the name of a remote which you had previously configured using [git-remote[1]](https://git-scm.com/docs/git-remote), [git-config[1]](https://git-scm.com/docs/git-config) or even by a manual edit to the `$GIT_DIR/config` file. The URL of this remote will be used to access the repository. The refspec of this remote will be used by default when you do not provide a refspec on the command line. The entry in the config file would appear like this:
```
	[remote "<name>"]
		url = <URL>
		pushurl = <pushurl>
		push = <refspec>
		fetch = <refspec>
```

The _< pushurl>_ is used for pushes only. It is optional and defaults to _< URL>_. Pushing to a remote affects all defined pushurls or all defined urls if no pushurls are defined. Fetch, however, will only fetch from the first defined url if multiple urls are defined.
###  [](https://git-scm.com/docs/git-pull#_named_file_in_git_dirremotes)Named file in `$GIT_DIR/remotes`
You can choose to provide the name of a file in `$GIT_DIR/remotes`. The URL in this file will be used to access the repository. The refspec in this file will be used as default when you do not provide a refspec on the command line. This file should have the following format:
```
	URL: one of the above URL formats
	Push: <refspec>
	Pull: <refspec>
```

`Push:` lines are used by `git` `push` and `Pull:` lines are used by `git` `pull` and `git` `fetch`. Multiple `Push:` and `Pull:` lines may be specified for additional branch mappings.
###  [](https://git-scm.com/docs/git-pull#_named_file_in_git_dirbranches)Named file in `$GIT_DIR/branches`
You can choose to provide the name of a file in `$GIT_DIR/branches`. The URL in this file will be used to access the repository. This file should have the following format:
```
	<URL>#<head>
```

_< URL>_ is required; `#`_< head>_ is optional.
Depending on the operation, git will use one of the following refspecs, if you don’t provide one on the command line. _< branch>_ is the name of this file in `$GIT_DIR/branches` and _< head>_ defaults to `master`.
git fetch uses:
```
	refs/heads/<head>:refs/heads/<branch>
```

git push uses:
```
	HEAD:refs/heads/<head>
```

##  [](https://git-scm.com/docs/git-pull#UPSTREAM-BRANCHES)UPSTREAM BRANCHES
Branches in Git can optionally have an upstream remote branch. Git defaults to using the upstream branch for remote operations, for example:
  * It’s the default for `git` `pull` or `git` `fetch` with no arguments.
  * It’s the default for `git` `push` with no arguments, with some exceptions. For example, you can use the `branch.`_< name>_`.pushRemote` option to push to a different remote than you pull from, and by default with `push.default=simple` the upstream branch you configure must have the same name.
  * Various commands, including `git` `checkout` and `git` `status`, will show you how many commits have been added to your current branch and the upstream since you forked from it, for example "Your branch and _origin/main_ have diverged, and have 2 and 3 different commits each respectively".


The upstream is stored in `.git/config`, in the "`remote`" and "`merge`" fields. For example, if `main`'s upstream is `origin/main`:
```
[branch "main"]
   remote = origin
   merge = refs/heads/main
```

You can set an upstream branch explicitly with `git` `push` `--set-upstream` _< remote>_ _< branch>_ but Git will often automatically set the upstream for you, for example:
  * When you clone a repository, Git will automatically set the upstream for the default branch.
  * If you have the `push.autoSetupRemote` configuration option set, `git` `push` will automatically set the upstream the first time you push a branch.
  * Checking out a remote-tracking branch with `git` `checkout` _< branch>_ will automatically create a local branch with that name and set the upstream to the remote branch.


Note |  Upstream branches are sometimes referred to as "tracking information", as in "set the branch’s tracking information".   
---|---  
##  [](https://git-scm.com/docs/git-pull#_merge_strategies)MERGE STRATEGIES
The merge mechanism (`git` `merge` and `git` `pull` commands) allows the backend _merge strategies_ to be chosen with `-s` option. Some strategies can also take their own options, which can be passed by giving `-X`_< option>_ arguments to `git` `merge` and/or `git` `pull`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-ort)`ort` 
    
This is the default merge strategy when pulling or merging one branch. This strategy can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this strategy can detect and handle merges involving renames. It does not make use of detected copies. The name for this algorithm is an acronym ("Ostensibly Recursive’s Twin") and came from the fact that it was written as a replacement for the previous default algorithm, `recursive`.
In the case where the path is a submodule, if the submodule commit used on one side of the merge is a descendant of the submodule commit used on the other side of the merge, Git attempts to fast-forward to the descendant. Otherwise, Git will treat this case as a conflict, suggesting as a resolution a submodule commit that is descendant of the conflicting ones, if one exists.
The `ort` strategy can take the following options: 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-ours)`ours` 
    
This option forces conflicting hunks to be auto-resolved cleanly by favoring _our_ version. Changes from the other tree that do not conflict with our side are reflected in the merge result. For a binary file, the entire contents are taken from our side.
This should not be confused with the `ours` merge strategy, which does not even look at what the other tree contains at all. It discards everything the other tree did, declaring _our_ history contains all that happened in it. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-theirs)`theirs` 
    
This is the opposite of `ours`; note that, unlike `ours`, there is no `theirs` merge strategy to confuse this merge option with. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-ignore-space-change)`ignore-space-change` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-ignore-all-space)`ignore-all-space` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-ignore-space-at-eol)`ignore-space-at-eol` 


[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-ignore-cr-at-eol)`ignore-cr-at-eol` 
    
Treats lines with the indicated type of whitespace change as unchanged for the sake of a three-way merge. Whitespace changes mixed with other changes to a line are not ignored. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `-b`, `-w`, `--ignore-space-at-eol`, and `--ignore-cr-at-eol`.
  * If _their_ version only introduces whitespace changes to a line, _our_ version is used;
  * If _our_ version introduces whitespace changes but _their_ version includes a substantial change, _their_ version is used;
  * Otherwise, the merge proceeds in the usual way.



[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-renormalize)`renormalize` 
    
This runs a virtual check-out and check-in of all three stages of any file which needs a three-way merge. This option is meant to be used when merging branches with different clean filters or end-of-line normalization rules. See "Merging branches with differing checkin/checkout attributes" in [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-no-renormalize)`no-renormalize` 
    
Disables the `renormalize` option. This overrides the `merge.renormalize` configuration variable. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-find-renamesn)`find-renames`[`=`_< n>_] 
    
Turn on rename detection, optionally setting the similarity threshold. This is the default. This overrides the `merge.renames` configuration variable. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--find-renames`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-rename-thresholdn)`rename-threshold=`_< n>_ 
    
Deprecated synonym for `find-renames=`_< n>_. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-no-renames)`no-renames` 
    
Turn off rename detection. This overrides the `merge.renames` configuration variable. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--no-renames`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-histogram)`histogram` 
    
Deprecated synonym for `diff-algorithm=histogram`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-patience)`patience` 
    
Deprecated synonym for `diff-algorithm=patience`. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-diff-algorithmhistogramminimalmyerspatience)`diff-algorithm=`(`histogram`|`minimal`|`myers`|`patience`) 
    
Use a different diff algorithm while merging, which can help avoid mismerges that occur due to unimportant matching lines (such as braces from distinct functions). See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--diff-algorithm`. Note that `ort` defaults to `diff-algorithm=histogram`, while regular diffs currently default to the `diff.algorithm` config setting. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-subtreepath)`subtree`[`=`_< path>_] 
    
This option is a more advanced form of _subtree_ strategy, where the strategy makes a guess on how two trees must be shifted to match with each other when merging. Instead, the specified path is prefixed (or stripped from the beginning) to make the shape of two trees to match. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-recursive)`recursive` 
    
This is now a synonym for `ort`. It was an alternative implementation until v2.49.0, but was redirected to mean `ort` in v2.50.0. The previous recursive strategy was the default strategy for resolving two heads from Git v0.99.9k until v2.33.0. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-resolve)`resolve` 
    
This can only resolve two heads (i.e. the current branch and another branch you pulled from) using a 3-way merge algorithm. It tries to carefully detect criss-cross merge ambiguities. It does not handle renames. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-octopus)`octopus` 
    
This resolves cases with more than two heads, but refuses to do a complex merge that needs manual resolution. It is primarily meant to be used for bundling topic branch heads together. This is the default merge strategy when pulling or merging more than one branch. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-ours-1)`ours` 
    
This resolves any number of heads, but the resulting tree of the merge is always that of the current branch head, effectively ignoring all changes from all other branches. It is meant to be used to supersede old development history of side branches. Note that this is different from the `-Xours` option to the `ort` merge strategy. 

[](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt-subtree)`subtree` 
    
This is a modified `ort` strategy. When merging trees A and B, if B corresponds to a subtree of A, B is first adjusted to match the tree structure of A, instead of reading the trees at the same level. This adjustment is also done to the common ancestor tree.
With the strategies that use 3-way merge (including the default, `ort`), if a change is made on both branches, but later reverted on one of the branches, that change will be present in the merged result; some people find this behavior confusing. It occurs because only the heads and the merge base are considered when performing a merge, not the individual commits. The merge algorithm therefore considers the reverted change as no change at all, and substitutes the changed version instead.
##  [](https://git-scm.com/docs/git-pull#DEFAULT-BEHAVIOUR)DEFAULT BEHAVIOUR
Often people use `git` `pull` without giving any parameter. Traditionally, this has been equivalent to saying `git` `pull` `origin`. However, when configuration `branch.`_< name>_`.remote` is present while on branch _< name>_, that value is used instead of `origin`.
In order to determine what URL to use to fetch from, the value of the configuration `remote.`_< origin>_`.url` is consulted and if there is not any such variable, the value on the `URL:` line in `$GIT_DIR/remotes/`_< origin>_ is used.
In order to determine what remote branches to fetch (and optionally store in the remote-tracking branches) when the command is run without any refspec parameters on the command line, values of the configuration variable `remote.`_< origin>_`.fetch` are consulted, and if there aren’t any, `$GIT_DIR/remotes/`_< origin>_ is consulted and its `Pull:` lines are used. In addition to the refspec formats described in the OPTIONS section, you can have a globbing refspec that looks like this:
```
refs/heads/*:refs/remotes/origin/*
```

A globbing refspec must have a non-empty RHS (i.e. must store what were fetched in remote-tracking branches), and its LHS and RHS must end with `/*`. The above specifies that all remote branches are tracked using remote-tracking branches in `refs/remotes/origin/` hierarchy under the same name.
The rule to determine which remote branch to merge after fetching is a bit involved, in order not to break backward compatibility.
If explicit refspecs were given on the command line of `git` `pull`, they are all merged.
When no refspec was given on the command line, then `git` `pull` uses the refspec from the configuration or `$GIT_DIR/remotes/`_< origin>_. In such cases, the following rules apply:
  1. If `branch.`_< name>_`.merge` configuration for the current branch _< name>_ exists, that is the name of the branch at the remote site that is merged.
  2. If the refspec is a globbing one, nothing is merged.
  3. Otherwise the remote branch of the first refspec is merged.


##  [](https://git-scm.com/docs/git-pull#_examples)EXAMPLES
  * Update the remote-tracking branches for the repository you cloned from, then merge one of them into your current branch:
```
$ git pull
$ git pull origin
```

Normally the branch merged in is the `HEAD` of the remote repository, but the choice is determined by the `branch.`_< name>_`.remote` and `branch.`_< name>_`.merge` options; see [git-config[1]](https://git-scm.com/docs/git-config) for details.
  * Merge into the current branch the remote branch `next`:
```
$ git pull origin next
```

This leaves a copy of `next` temporarily in `FETCH_HEAD`, and updates the remote-tracking branch `origin/next`. The same can be done by invoking fetch and merge:
```
$ git fetch origin
$ git merge origin/next
```



If you tried a pull which resulted in complex conflicts and would want to start over, you can recover with `git` `reset`.
##  [](https://git-scm.com/docs/git-pull#_security)SECURITY
The fetch and push protocols are not designed to prevent one side from stealing data from the other repository that was not intended to be shared. If you have private data that you need to protect from a malicious peer, your best option is to store it in another repository. This applies to both clients and servers. In particular, namespaces on a server are not effective for read access control; you should only grant read access to a namespace to clients that you would trust with read access to the entire repository.
The known attack vectors are as follows:
  1. The victim sends "have" lines advertising the IDs of objects it has that are not explicitly intended to be shared but can be used to optimize the transfer if the peer also has them. The attacker chooses an object ID X to steal and sends a ref to X, but isn’t required to send the content of X because the victim already has it. Now the victim believes that the attacker has X, and it sends the content of X back to the attacker later. (This attack is most straightforward for a client to perform on a server, by creating a ref to X in the namespace the client has access to and then fetching it. The most likely way for a server to perform it on a client is to "merge" X into a public branch and hope that the user does additional work on this branch and pushes it back to the server without noticing the merge.)
  2. As in #1, the attacker chooses an object ID X to steal. The victim sends an object Y that the attacker already has, and the attacker falsely claims to have X and not Y, so the victim sends Y as a delta against X. The delta reveals regions of X that are similar to Y to the attacker.


##  [](https://git-scm.com/docs/git-pull#_bugs)BUGS
Using `--recurse-submodules` can only fetch new commits in already checked out submodules right now. When e.g. upstream added a new submodule in the just fetched commits of the superproject the submodule itself cannot be fetched, making it impossible to check out that submodule later without having to do a fetch again. This is expected to be fixed in a future Git version.
##  [](https://git-scm.com/docs/git-pull#_see_also)SEE ALSO
[git-fetch[1]](https://git-scm.com/docs/git-fetch), [git-merge[1]](https://git-scm.com/docs/git-merge), [git-config[1]](https://git-scm.com/docs/git-config)
##  [](https://git-scm.com/docs/git-pull#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### pull
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
