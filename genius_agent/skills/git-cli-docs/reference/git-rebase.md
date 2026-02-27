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
    * [NAME](https://git-scm.com/docs/git-rebase#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-rebase#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-rebase#_description)
    * [TRANSPLANTING A TOPIC BRANCH WITH --ONTO](https://git-scm.com/docs/git-rebase#_transplanting_a_topic_branch_with_onto)
    * [MODE OPTIONS](https://git-scm.com/docs/git-rebase#_mode_options)
    * [OPTIONS](https://git-scm.com/docs/git-rebase#_options)
    * [INCOMPATIBLE OPTIONS](https://git-scm.com/docs/git-rebase#_incompatible_options)
    * [BEHAVIORAL DIFFERENCES](https://git-scm.com/docs/git-rebase#_behavioral_differences)
    * [MERGE STRATEGIES](https://git-scm.com/docs/git-rebase#_merge_strategies)
    * [NOTES](https://git-scm.com/docs/git-rebase#_notes)
    * [INTERACTIVE MODE](https://git-scm.com/docs/git-rebase#_interactive_mode)
    * [SPLITTING COMMITS](https://git-scm.com/docs/git-rebase#_splitting_commits)
    * [RECOVERING FROM UPSTREAM REBASE](https://git-scm.com/docs/git-rebase#_recovering_from_upstream_rebase)
    * [REBASING MERGES](https://git-scm.com/docs/git-rebase#_rebasing_merges)
    * [CONFIGURATION](https://git-scm.com/docs/git-rebase#_configuration)
    * [GIT](https://git-scm.com/docs/git-rebase#_git)


[ English ▾](https://git-scm.com/docs/git-rebase)
Localized versions of **git-rebase** manual
  1. [English ](https://git-scm.com/docs/git-rebase)
  2. [Français ](https://git-scm.com/docs/git-rebase/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-rebase/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-rebase/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-rebase/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-rebase)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-rebase) git-rebase last updated in 2.53.0
Changes in the **git-rebase** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-rebase/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-rebase/2.52.0)
  3. 2.50.1 → 2.51.2 no changes
  4. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-rebase/2.50.0)
  5. 2.49.1 no changes
  6. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-rebase/2.49.0)
  7. 2.46.2 → 2.48.2 no changes
  8. [2.46.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-13_ ](https://git-scm.com/docs/git-rebase/2.46.1)
  9. 2.45.1 → 2.46.0 no changes
  10. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-rebase/2.45.0)
  11. 2.44.1 → 2.44.4 no changes
  12. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-rebase/2.44.0)
  13. 2.43.3 → 2.43.7 no changes
  14. [2.43.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-13_ ](https://git-scm.com/docs/git-rebase/2.43.2)
  15. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-rebase/2.43.1)
  16. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-rebase/2.43.0)
  17. 2.42.2 → 2.42.4 no changes
  18. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-rebase/2.42.1)
  19. 2.41.1 → 2.42.0 no changes
  20. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-rebase/2.41.0)
  21. 2.40.1 → 2.40.4 no changes
  22. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-rebase/2.40.0)
  23. 2.39.4 → 2.39.5 no changes
  24. [2.39.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-04-17_ ](https://git-scm.com/docs/git-rebase/2.39.3)
  25. 2.39.1 → 2.39.2 no changes
  26. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-rebase/2.39.0)
  27. 2.38.1 → 2.38.5 no changes
  28. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-rebase/2.38.0)
  29. 2.37.3 → 2.37.7 no changes
  30. [2.37.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-08-11_ ](https://git-scm.com/docs/git-rebase/2.37.2)
  31. 2.36.3 → 2.37.1 no changes
  32. [2.36.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-rebase/2.36.2)
  33. 2.35.1 → 2.36.1 no changes
  34. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-rebase/2.35.0)
  35. 2.34.1 → 2.34.8 no changes
  36. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-rebase/2.34.0)
  37. 2.33.2 → 2.33.8 no changes
  38. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git-rebase/2.33.1)
  39. 2.32.1 → 2.33.0 no changes
  40. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-rebase/2.32.0)
  41. 2.31.1 → 2.31.8 no changes
  42. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-rebase/2.31.0)
  43. 2.30.1 → 2.30.9 no changes
  44. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-rebase/2.30.0)
  45. 2.29.1 → 2.29.3 no changes
  46. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-rebase/2.29.0)
  47. 2.28.1 no changes
  48. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-rebase/2.28.0)
  49. 2.27.1 no changes
  50. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-rebase/2.27.0)
  51. 2.26.1 → 2.26.3 no changes
  52. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-rebase/2.26.0)
  53. 2.25.1 → 2.25.5 no changes
  54. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-rebase/2.25.0)
  55. 2.24.1 → 2.24.4 no changes
  56. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-rebase/2.24.0)
  57. 2.23.1 → 2.23.4 no changes
  58. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-rebase/2.23.0)
  59. 2.22.1 → 2.22.5 no changes
  60. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-rebase/2.22.0)
  61. 2.21.1 → 2.21.4 no changes
  62. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-rebase/2.21.0)
  63. 2.20.1 → 2.20.5 no changes
  64. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-rebase/2.20.0)
  65. 2.19.3 → 2.19.6 no changes
  66. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-rebase/2.19.2)
  67. 2.19.1 no changes
  68. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-rebase/2.19.0)
  69. 2.18.1 → 2.18.5 no changes
  70. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-rebase/2.18.0)
  71. 2.17.1 → 2.17.6 no changes
  72. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-rebase/2.17.0)
  73. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-rebase/2.16.6)
  74. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-rebase/2.15.4)
  75. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-rebase/2.14.6)
  76. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-rebase/2.13.7)
  77. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-rebase/2.12.5)
  78. 2.10.5 → 2.11.4 no changes
  79. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-rebase/2.9.5)
  80. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-rebase/2.8.6)
  81. 2.7.6 no changes
  82. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-rebase/2.6.7)
  83. 2.5.6 no changes
  84. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-rebase/2.4.12)
  85. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-rebase/2.3.10)
  86. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-rebase/2.2.3)
  87. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-rebase/2.1.4)
  88. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-rebase/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-rebase#_name)NAME
git-rebase - Reapply commits on top of another base tip
##  [](https://git-scm.com/docs/git-rebase#_synopsis)SYNOPSIS
```
_git rebase_ [-i | --interactive] [<options>] [--exec <cmd>]
	[--onto <newbase> | --keep-base] [<upstream> [<branch>]]
_git rebase_ [-i | --interactive] [<options>] [--exec <cmd>] [--onto <newbase>]
	--root [<branch>]
_git rebase_ (--continue|--skip|--abort|--quit|--edit-todo|--show-current-patch)
```

##  [](https://git-scm.com/docs/git-rebase#_description)DESCRIPTION
Transplant a series of commits onto a different starting point. You can also use `git` `rebase` to reorder or combine commits: see INTERACTIVE MODE below for how to do that.
For example, imagine that you have been working on the `topic` branch in this history, and you want to "catch up" to the work done on the `master` branch.
```
          A---B---C topic
         /
    D---E---F---G master
```

You want to transplant the commits you made on `topic` since it diverged from `master` (i.e. A, B, and C), on top of the current `master`. You can do this by running `git` `rebase` `master` while the `topic` branch is checked out. If you want to rebase `topic` while on another branch, `git` `rebase` `master` `topic` is a shortcut for _git checkout topic && git rebase master_.
```
                  A'--B'--C' topic
                 /
    D---E---F---G master
```

If there is a merge conflict during this process, `git` `rebase` will stop at the first problematic commit and leave conflict markers. If this happens, you can do one of these things:
  1. Resolve the conflict. You can use `git` `diff` to find the markers (<<<<<<) and make edits to resolve the conflict. For each file you edit, you need to tell Git that the conflict has been resolved. You can mark the conflict as resolved with `git` `add` _< filename>_. After resolving all of the conflicts, you can continue the rebasing process with
```
git rebase --continue
```

  2. Stop the `git` `rebase` and return your branch to its original state with
```
git rebase --abort
```

  3. Skip the commit that caused the merge conflict with
```
git rebase --skip
```



If you don’t specify an _< upstream>_ to rebase onto, the upstream configured in `branch.`_< name>_`.remote` and `branch.`_< name>_`.merge` options will be used (see [git-config[1]](https://git-scm.com/docs/git-config) for details) and the `--fork-point` option is assumed. If you are currently not on any branch or if the current branch does not have a configured upstream, the rebase will abort.
Here is a simplified description of what `git` `rebase` _< upstream>_ does:
  1. Make a list of all commits on your current branch since it branched off from _< upstream>_ that do not have an equivalent commit in _< upstream>_.
  2. Check out _< upstream>_ with the equivalent of `git` `checkout` `--detach` _< upstream>_.
  3. Replay the commits, one by one, in order. This is similar to running `git` `cherry-pick` _< commit>_ for each commit. See REBASING MERGES for how merges are handled.
  4. Update your branch to point to the final commit with the equivalent of `git` `checkout` `-B` _< branch>_.


Note |  When starting the rebase, `ORIG_HEAD` is set to point to the commit at the tip of the to-be-rebased branch. However, `ORIG_HEAD` is not guaranteed to still point to that commit at the end of the rebase if other commands that change `ORIG_HEAD` (like `git` `reset`) are used during the rebase. The previous branch tip, however, is accessible using the reflog of the current branch (i.e. `@{1}`, see [gitrevisions[7]](https://git-scm.com/docs/gitrevisions)).   
---|---  
##  [](https://git-scm.com/docs/git-rebase#_transplanting_a_topic_branch_with_onto)TRANSPLANTING A TOPIC BRANCH WITH --ONTO
Here is how you would transplant a topic branch based on one branch to another, to pretend that you forked the topic branch from the latter branch, using `rebase` `--onto`.
First let’s assume your _topic_ is based on branch _next_. For example, a feature developed in _topic_ depends on some functionality which is found in _next_.
```
    o---o---o---o---o  master
         \
          o---o---o---o---o  next
                           \
                            o---o---o  topic
```

We want to make _topic_ forked from branch _master_ ; for example, because the functionality on which _topic_ depends was merged into the more stable _master_ branch. We want our tree to look like this:
```
    o---o---o---o---o  master
        |            \
        |             o'--o'--o'  topic
         \
          o---o---o---o---o  next
```

We can get this using the following command:
```
git rebase --onto master next topic
```

Another example of --onto option is to rebase part of a branch. If we have the following situation:
```
                            H---I---J topicB
                           /
                  E---F---G  topicA
                 /
    A---B---C---D  master
```

then the command
```
git rebase --onto master topicA topicB
```

would result in:
```
                 H'--I'--J'  topicB
                /
                | E---F---G  topicA
                |/
    A---B---C---D  master
```

This is useful when topicB does not depend on topicA.
A range of commits could also be removed with rebase. If we have the following situation:
```
    E---F---G---H---I---J  topicA
```

then the command
```
git rebase --onto topicA~5 topicA~3 topicA
```

would result in the removal of commits F and G:
```
    E---H'---I'---J'  topicA
```

This is useful if F and G were flawed in some way, or should not be part of topicA. Note that the argument to `--onto` and the _< upstream>_ parameter can be any valid commit-ish.
##  [](https://git-scm.com/docs/git-rebase#_mode_options)MODE OPTIONS
The options in this section cannot be used with any other option, including not with each other: 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---continue)--continue 
    
Restart the rebasing process after having resolved a merge conflict. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---skip)--skip 
    
Restart the rebasing process by skipping the current patch. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---abort)--abort 
    
Abort the rebase operation and reset HEAD to the original branch. If _< branch>_ was provided when the rebase operation was started, then `HEAD` will be reset to _< branch>_. Otherwise `HEAD` will be reset to where it was when the rebase operation was started. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---quit)--quit 
    
Abort the rebase operation but `HEAD` is not reset back to the original branch. The index and working tree are also left unchanged as a result. If a temporary stash entry was created using `--autostash`, it will be saved to the stash list. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---edit-todo)--edit-todo 
    
Edit the todo list during an interactive rebase. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---show-current-patch)--show-current-patch 
    
Show the current patch in an interactive rebase or when rebase is stopped because of conflicts. This is the equivalent of `git` `show` `REBASE_HEAD`.
##  [](https://git-scm.com/docs/git-rebase#_options)OPTIONS 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---ontonewbase)--onto <newbase> 
    
Starting point at which to create the new commits. If the `--onto` option is not specified, the starting point is _< upstream>_. May be any valid commit, and not just an existing branch name.
As a special case, you may use "A...B" as a shortcut for the merge base of A and B if there is exactly one merge base. You can leave out at most one of A and B, in which case it defaults to HEAD.
See TRANSPLANTING A TOPIC BRANCH WITH --ONTO above for examples. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---keep-base)--keep-base 
    
Set the starting point at which to create the new commits to the merge base of _< upstream>_ and _< branch>_. Running `git` `rebase` `--keep-base` _< upstream>_ _< branch>_ is equivalent to running `git` `rebase` `--reapply-cherry-picks` `--no-fork-point` `--onto` _< upstream>_`...`_< branch>_ _< upstream>_ _< branch>_.
This option is useful in the case where one is developing a feature on top of an upstream branch. While the feature is being worked on, the upstream branch may advance and it may not be the best idea to keep rebasing on top of the upstream but to keep the base commit as-is. As the base commit is unchanged this option implies `--reapply-cherry-picks` to avoid losing commits.
Although both this option and `--fork-point` find the merge base between _< upstream>_ and _< branch>_, this option uses the merge base as the _starting point_ on which new commits will be created, whereas `--fork-point` uses the merge base to determine the _set of commits_ which will be rebased.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-upstream)<upstream> 
    
Upstream branch to compare against. May be any valid commit, not just an existing branch name. Defaults to the configured upstream for the current branch. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-branch)<branch> 
    
Working branch; defaults to `HEAD`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---apply)--apply 
    
Use applying strategies to rebase (calling `git-am` internally). This option may become a no-op in the future once the merge backend handles everything the apply one does.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---emptydropkeepstop)--empty=(drop|keep|stop) 
    
How to handle commits that are not empty to start and are not clean cherry-picks of any upstream commit, but which become empty after rebasing (because they contain a subset of already upstream changes): 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-drop)`drop` 
    
The commit will be dropped. This is the default behavior. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-keep)`keep` 
    
The commit will be kept. This option is implied when `--exec` is specified unless `-i`/`--interactive` is also specified. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-stop)`stop` 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ask)`ask` 
    
The rebase will halt when the commit is applied, allowing you to choose whether to drop it, edit files more, or just commit the empty changes. This option is implied when `-i`/`--interactive` is specified. `ask` is a deprecated synonym of `stop`.
Note that commits which start empty are kept (unless `--no-keep-empty` is specified), and commits which are clean cherry-picks (as determined by `git` `log` `--cherry-mark` ...) are detected and dropped as a preliminary step (unless `--reapply-cherry-picks` or `--keep-base` is passed).
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-keep-empty)--no-keep-empty 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---keep-empty)--keep-empty 
    
Do not keep commits that start empty before the rebase (i.e. that do not change anything from its parent) in the result. The default is to keep commits which start empty, since creating such commits requires passing the `--allow-empty` override flag to `git` `commit`, signifying that a user is very intentionally creating such a commit and thus wants to keep it.
Usage of this flag will probably be rare, since you can get rid of commits that start empty by just firing up an interactive rebase and removing the lines corresponding to the commits you don’t want. This flag exists as a convenient shortcut, such as for cases where external tools generate many empty commits and you want them all removed.
For commits which do not start empty but become empty after rebasing, see the `--empty` flag.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---reapply-cherry-picks)--reapply-cherry-picks 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-reapply-cherry-picks)--no-reapply-cherry-picks 
    
Reapply all clean cherry-picks of any upstream commit instead of preemptively dropping them. (If these commits then become empty after rebasing, because they contain a subset of already upstream changes, the behavior towards them is controlled by the `--empty` flag.)
In the absence of `--keep-base` (or if `--no-reapply-cherry-picks` is given), these commits will be automatically dropped. Because this necessitates reading all upstream commits, this can be expensive in repositories with a large number of upstream commits that need to be read. When using the _merge_ backend, warnings will be issued for each dropped commit (unless `--quiet` is given). Advice will also be issued unless `advice.skippedCherryPicks` is set to false (see [git-config[1]](https://git-scm.com/docs/git-config)).
`--reapply-cherry-picks` allows rebase to forgo reading all upstream commits, potentially improving performance.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---allow-empty-message)--allow-empty-message 
    
No-op. Rebasing commits with an empty message used to fail and this option would override that behavior, allowing commits with empty messages to be rebased. Now commits with an empty message do not cause rebasing to halt.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--m)-m 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---merge)--merge 
    
Using merging strategies to rebase (default).
Note that a rebase merge works by replaying each commit from the working branch on top of the _< upstream>_ branch. Because of this, when a merge conflict happens, the side reported as _ours_ is the so-far rebased series, starting with _< upstream>_, and _theirs_ is the working branch. In other words, the sides are swapped.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--sstrategy)-s <strategy> 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---strategystrategy)--strategy=<strategy> 
    
Use the given merge strategy, instead of the default `ort`. This implies `--merge`.
Because `git` `rebase` replays each commit from the working branch on top of the _< upstream>_ branch using the given strategy, using the `ours` strategy simply empties all patches from the _< branch>_, which makes little sense.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--Xstrategy-option)-X <strategy-option> 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---strategy-optionstrategy-option)--strategy-option=<strategy-option> 
    
Pass the <strategy-option> through to the merge strategy. This implies `--merge` and, if no strategy has been specified, `-s` `ort`. Note the reversal of _ours_ and _theirs_ as noted above for the `-m` option.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---rerere-autoupdate)`--rerere-autoupdate` 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-rerere-autoupdate)`--no-rerere-autoupdate` 
    
After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update the index with the result of resolution. `--no-rerere-autoupdate` is a good way to double-check what `rerere` did and catch potential mismerges, before committing the result to the index with a separate `git` `add`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--Skeyid)-S[<keyid>] 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---gpg-signkeyid)--gpg-sign[=<keyid>] 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-gpg-sign)--no-gpg-sign 
    
GPG-sign commits. The `keyid` argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand both `commit.gpgSign` configuration variable, and earlier `--gpg-sign`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--q)-q 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---quiet)--quiet 
    
Be quiet. Implies `--no-stat`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--v)-v 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---verbose)--verbose 
    
Be verbose. Implies `--stat`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---stat)--stat 
    
Show a diffstat of what changed upstream since the last rebase. The diffstat is also controlled by the configuration option rebase.stat. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--n)-n 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-stat)--no-stat 
    
Do not show a diffstat as part of the rebase process. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-verify)--no-verify 
    
This option bypasses the pre-rebase hook. See also [githooks[5]](https://git-scm.com/docs/githooks). 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---verify)--verify 
    
Allows the pre-rebase hook to run, which is the default. This option can be used to override `--no-verify`. See also [githooks[5]](https://git-scm.com/docs/githooks). 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--Cn)-C<n> 
    
Ensure at least _< n>_ lines of surrounding context match before and after each change. When fewer lines of surrounding context exist they all must match. By default no context is ever ignored. Implies `--apply`.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-ff)--no-ff 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---force-rebase)--force-rebase 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--f)-f 
    
Individually replay all rebased commits instead of fast-forwarding over the unchanged ones. This ensures that the entire history of the rebased branch is composed of new commits.
You may find this helpful after reverting a topic branch merge, as this option recreates the topic branch with fresh commits so it can be remerged successfully without needing to "revert the reversion" (see the [revert-a-faulty-merge How-To](https://git-scm.com/docs/howto/revert-a-faulty-merge) for details). 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---fork-point)--fork-point 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-fork-point)--no-fork-point 
    
Use reflog to find a better common ancestor between _< upstream>_ and _< branch>_ when calculating which commits have been introduced by _< branch>_.
When `--fork-point` is active, _fork_point_ will be used instead of _< upstream>_ to calculate the set of commits to rebase, where _fork_point_ is the result of `git` `merge-base` `--fork-point` _< upstream>_ _< branch>_ command (see [git-merge-base[1]](https://git-scm.com/docs/git-merge-base)). If _fork_point_ ends up being empty, the _< upstream>_ will be used as a fallback.
If _< upstream>_ or `--keep-base` is given on the command line, then the default is `--no-fork-point`, otherwise the default is `--fork-point`. See also `rebase.forkpoint` in [git-config[1]](https://git-scm.com/docs/git-config).
If your branch was based on _< upstream>_ but _< upstream>_ was rewound and your branch contains commits which were dropped, this option can be used with `--keep-base` in order to drop those commits from your branch.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---ignore-whitespace)--ignore-whitespace 
    
Ignore whitespace differences when trying to reconcile differences. Currently, each backend implements an approximation of this behavior: 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-applybackend)apply backend 
    
When applying a patch, ignore changes in whitespace in context lines. Unfortunately, this means that if the "old" lines being replaced by the patch differ only in whitespace from the existing file, you will get a merge conflict instead of a successful patch application. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-mergebackend)merge backend 
    
Treat lines with only whitespace changes as unchanged when merging. Unfortunately, this means that any patch hunks that were intended to modify whitespace and nothing else will be dropped, even if the other side had no changes that conflicted. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---whitespaceoption)--whitespace=<option> 
    
This flag is passed to the `git` `apply` program (see [git-apply[1]](https://git-scm.com/docs/git-apply)) that applies the patch. Implies `--apply`.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---committer-date-is-author-date)--committer-date-is-author-date 
    
Instead of using the current time as the committer date, use the author date of the commit being rebased as the committer date. This option implies `--force-rebase`.
Warning |  The history walking machinery assumes that commits have non-decreasing commit timestamps. You should consider if you really need to use this option. Then you should only use this option to override the committer date when rebasing commits on top of a base which commit is older (in terms of the commit date) than the oldest commit you are applying (in terms of the author date).   
---|--- 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---ignore-date)--ignore-date 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---reset-author-date)--reset-author-date 
      
Instead of using the author date of the original commit, use the current time as the author date of the rebased commit. This option implies `--force-rebase`.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---signoff)--signoff 
    
Add a `Signed-off-by` trailer to all the rebased commits. Note that if `--interactive` is given then only commits marked to be picked, edited or reworded will have the trailer added.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--i)-i 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---interactive)--interactive 
    
Make a list of the commits which are about to be rebased. Let the user edit that list before rebasing. This mode can also be used to split commits (see SPLITTING COMMITS below).
The commit list format can be changed by setting the configuration option rebase.instructionFormat. A customized instruction format will automatically have the commit hash prepended to the format.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--r)-r 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---rebase-mergesrebase-cousinsno-rebase-cousins)--rebase-merges[=(rebase-cousins|no-rebase-cousins)] 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-rebase-merges)--no-rebase-merges 
    
By default, a rebase will simply drop merge commits from the todo list, and put the rebased commits into a single, linear branch. With `--rebase-merges`, the rebase will instead try to preserve the branching structure within the commits that are to be rebased, by recreating the merge commits. Any resolved merge conflicts or manual amendments in these merge commits will have to be resolved/re-applied manually. `--no-rebase-merges` can be used to countermand both the `rebase.rebaseMerges` config option and a previous `--rebase-merges`.
When rebasing merges, there are two modes: `rebase-cousins` and `no-rebase-cousins`. If the mode is not specified, it defaults to `no-rebase-cousins`. In `no-rebase-cousins` mode, commits which do not have _< upstream>_ as direct ancestor will keep their original branch point, i.e. commits that would be excluded by [git-log[1]](https://git-scm.com/docs/git-log)'s `--ancestry-path` option will keep their original ancestry by default. In `rebase-cousins` mode, such commits are instead rebased onto _< upstream>_ (or _< onto>_, if specified).
It is currently only possible to recreate the merge commits using the `ort` merge strategy; different merge strategies can be used only via explicit `exec` `git` `merge` `-s` _< strategy>_ [...] commands.
See also REBASING MERGES and INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--xcmd)-x <cmd> 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---execcmd)--exec <cmd> 
    
Append "exec <cmd>" after each line creating a commit in the final history. _< cmd>_ will be interpreted as one or more shell commands. Any command that fails will interrupt the rebase, with exit code 1.
You may execute several commands by either using one instance of `--exec` with several commands:
```
git rebase -i --exec "cmd1 && cmd2 && ..."
```

or by giving more than one `--exec`:
```
git rebase -i --exec "cmd1" --exec "cmd2" --exec ...
```

If `--autosquash` is used, `exec` lines will not be appended for the intermediate commits, and will only appear at the end of each squash/fixup series.
This uses the `--interactive` machinery internally, but it can be run without an explicit `--interactive`.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---root)--root 
    
Rebase all commits reachable from _< branch>_, instead of limiting them with an _< upstream>_. This allows you to rebase the root commit(s) on a branch.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---autosquash)--autosquash 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-autosquash)--no-autosquash 
    
Automatically squash commits with specially formatted messages into previous commits being rebased. If a commit message starts with "squash! ", "fixup! " or "amend! ", the remainder of the title is taken as a commit specifier, which matches a previous commit if it matches the title or the hash of that commit. If no commit matches fully, matches of the specifier with the start of commit titles are considered.
In the rebase todo list, the actions of squash, fixup and amend commits are changed from `pick` to `squash`, `fixup` or `fixup` `-C`, respectively, and they are moved right after the commit they modify. The `--interactive` option can be used to review and edit the todo list before proceeding.
The recommended way to create commits with squash markers is by using the `--squash`, `--fixup`, `--fixup=amend:` or `--fixup=reword:` options of [git-commit[1]](https://git-scm.com/docs/git-commit), which take the target commit as an argument and automatically fill in the title of the new commit from that.
Setting configuration variable `rebase.autoSquash` to true enables auto-squashing by default for interactive rebase. The `--no-autosquash` option can be used to override that setting.
See also INCOMPATIBLE OPTIONS below. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---autostash)--autostash 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-autostash)--no-autostash 
    
Automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---reschedule-failed-exec)--reschedule-failed-exec 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-reschedule-failed-exec)--no-reschedule-failed-exec 
    
Automatically reschedule `exec` commands that failed. This only makes sense in interactive mode (or when an `--exec` option was provided).
This option applies once a rebase is started. It is preserved for the whole rebase based on, in order, the command line option provided to the initial `git` `rebase`, the `rebase.rescheduleFailedExec` configuration (see [git-config[1]](https://git-scm.com/docs/git-config) or "CONFIGURATION" below), or it defaults to false.
Recording this option for the whole rebase is a convenience feature. Otherwise an explicit `--no-reschedule-failed-exec` at the start would be overridden by the presence of a `rebase.rescheduleFailedExec=true` configuration when `git` `rebase` `--continue` is invoked. Currently, you cannot pass `--`[`no-`]`reschedule-failed-exec` to `git` `rebase` `--continue`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---update-refs)--update-refs 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt---no-update-refs)--no-update-refs 
    
Automatically force-update any branches that point to commits that are being rebased. Any branches that are checked out in a worktree are not updated in this way.
If the configuration variable `rebase.updateRefs` is set, then this option can be used to override and disable this setting.
See also INCOMPATIBLE OPTIONS below.
##  [](https://git-scm.com/docs/git-rebase#_incompatible_options)INCOMPATIBLE OPTIONS
The following options:
  * --apply
  * --whitespace
  * -C


are incompatible with the following options:
  * --merge
  * --strategy
  * --strategy-option
  * --autosquash
  * --rebase-merges
  * --interactive
  * --exec
  * --no-keep-empty
  * --empty=
  * --[no-]reapply-cherry-picks when used without --keep-base
  * --update-refs
  * --root when used without --onto


In addition, the following pairs of options are incompatible:
  * --keep-base and --onto
  * --keep-base and --root
  * --fork-point and --root


##  [](https://git-scm.com/docs/git-rebase#_behavioral_differences)BEHAVIORAL DIFFERENCES
`git` `rebase` has two primary backends: _apply_ and _merge_. (The _apply_ backend used to be known as the _am_ backend, but the name led to confusion as it looks like a verb instead of a noun. Also, the _merge_ backend used to be known as the interactive backend, but it is now used for non-interactive cases as well. Both were renamed based on lower-level functionality that underpinned each.) There are some subtle differences in how these two backends behave:
###  [](https://git-scm.com/docs/git-rebase#_empty_commits)Empty commits
The _apply_ backend unfortunately drops intentionally empty commits, i.e. commits that started empty, though these are rare in practice. It also drops commits that become empty and has no option for controlling this behavior.
The _merge_ backend keeps intentionally empty commits by default (though with `-i` they are marked as empty in the todo list editor, or they can be dropped automatically with `--no-keep-empty`).
Similar to the apply backend, by default the merge backend drops commits that become empty unless `-i`/`--interactive` is specified (in which case it stops and asks the user what to do). The merge backend also has an `--empty=`(`drop`|`keep`|`stop`) option for changing the behavior of handling commits that become empty.
###  [](https://git-scm.com/docs/git-rebase#_directory_rename_detection)Directory rename detection
Due to the lack of accurate tree information (arising from constructing fake ancestors with the limited information available in patches), directory rename detection is disabled in the _apply_ backend. Disabled directory rename detection means that if one side of history renames a directory and the other adds new files to the old directory, then the new files will be left behind in the old directory without any warning at the time of rebasing that you may want to move these files into the new directory.
Directory rename detection works with the _merge_ backend to provide you warnings in such cases.
###  [](https://git-scm.com/docs/git-rebase#_context)Context
The _apply_ backend works by creating a sequence of patches (by calling `format-patch` internally), and then applying the patches in sequence (calling `am` internally). Patches are composed of multiple hunks, each with line numbers, a context region, and the actual changes. The line numbers have to be taken with some offset, since the other side will likely have inserted or deleted lines earlier in the file. The context region is meant to help find how to adjust the line numbers in order to apply the changes to the right lines. However, if multiple areas of the code have the same surrounding lines of context, the wrong one can be picked. There are real-world cases where this has caused commits to be reapplied incorrectly with no conflicts reported. Setting `diff.context` to a larger value may prevent such types of problems, but increases the chance of spurious conflicts (since it will require more lines of matching context to apply).
The _merge_ backend works with a full copy of each relevant file, insulating it from these types of problems.
###  [](https://git-scm.com/docs/git-rebase#_labelling_of_conflicts_markers)Labelling of conflicts markers
When there are content conflicts, the merge machinery tries to annotate each side’s conflict markers with the commits where the content came from. Since the _apply_ backend drops the original information about the rebased commits and their parents (and instead generates new fake commits based off limited information in the generated patches), those commits cannot be identified; instead it has to fall back to a commit summary. Also, when `merge.conflictStyle` is set to `diff3` or `zdiff3`, the _apply_ backend will use "constructed merge base" to label the content from the merge base, and thus provide no information about the merge base commit whatsoever.
The _merge_ backend works with the full commits on both sides of history and thus has no such limitations.
###  [](https://git-scm.com/docs/git-rebase#_hooks)Hooks
The _apply_ backend has not traditionally called the post-commit hook, while the _merge_ backend has. Both have called the post-checkout hook, though the _merge_ backend has squelched its output. Further, both backends only call the post-checkout hook with the starting point commit of the rebase, not the intermediate commits nor the final commit. In each case, the calling of these hooks was by accident of implementation rather than by design (both backends were originally implemented as shell scripts and happened to invoke other commands like `git` `checkout` or `git` `commit` that would call the hooks). Both backends should have the same behavior, though it is not entirely clear which, if any, is correct. We will likely make rebase stop calling either of these hooks in the future.
###  [](https://git-scm.com/docs/git-rebase#_interruptability)Interruptability
The _apply_ backend has safety problems with an ill-timed interrupt; if the user presses Ctrl-C at the wrong time to try to abort the rebase, the rebase can enter a state where it cannot be aborted with a subsequent `git` `rebase` `--abort`. The _merge_ backend does not appear to suffer from the same shortcoming. (See <https://lore.kernel.org/git/20200207132152.GC2868@szeder.dev/> for details.)
###  [](https://git-scm.com/docs/git-rebase#_commit_rewording)Commit Rewording
When a conflict occurs while rebasing, rebase stops and asks the user to resolve. Since the user may need to make notable changes while resolving conflicts, after conflicts are resolved and the user has run `git` `rebase` `--continue`, the rebase should open an editor and ask the user to update the commit message. The _merge_ backend does this, while the _apply_ backend blindly applies the original commit message.
###  [](https://git-scm.com/docs/git-rebase#_miscellaneous_differences)Miscellaneous differences
There are a few more behavioral differences that most folks would probably consider inconsequential but which are mentioned for completeness:
  * Reflog: The two backends will use different wording when describing the changes made in the reflog, though both will make use of the word "rebase".
  * Progress, informational, and error messages: The two backends provide slightly different progress and informational messages. Also, the apply backend writes error messages (such as "Your files would be overwritten…​") to stdout, while the merge backend writes them to stderr.
  * State directories: The two backends keep their state in different directories under `.git/`


##  [](https://git-scm.com/docs/git-rebase#_merge_strategies)MERGE STRATEGIES
The merge mechanism (`git` `merge` and `git` `pull` commands) allows the backend _merge strategies_ to be chosen with `-s` option. Some strategies can also take their own options, which can be passed by giving `-X`_< option>_ arguments to `git` `merge` and/or `git` `pull`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ort)`ort` 
    
This is the default merge strategy when pulling or merging one branch. This strategy can only resolve two heads using a 3-way merge algorithm. When there is more than one common ancestor that can be used for 3-way merge, it creates a merged tree of the common ancestors and uses that as the reference tree for the 3-way merge. This has been reported to result in fewer merge conflicts without causing mismerges by tests done on actual merge commits taken from Linux 2.6 kernel development history. Additionally this strategy can detect and handle merges involving renames. It does not make use of detected copies. The name for this algorithm is an acronym ("Ostensibly Recursive’s Twin") and came from the fact that it was written as a replacement for the previous default algorithm, `recursive`.
In the case where the path is a submodule, if the submodule commit used on one side of the merge is a descendant of the submodule commit used on the other side of the merge, Git attempts to fast-forward to the descendant. Otherwise, Git will treat this case as a conflict, suggesting as a resolution a submodule commit that is descendant of the conflicting ones, if one exists.
The `ort` strategy can take the following options: 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ours)`ours` 
    
This option forces conflicting hunks to be auto-resolved cleanly by favoring _our_ version. Changes from the other tree that do not conflict with our side are reflected in the merge result. For a binary file, the entire contents are taken from our side.
This should not be confused with the `ours` merge strategy, which does not even look at what the other tree contains at all. It discards everything the other tree did, declaring _our_ history contains all that happened in it. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-theirs)`theirs` 
    
This is the opposite of `ours`; note that, unlike `ours`, there is no `theirs` merge strategy to confuse this merge option with. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ignore-space-change)`ignore-space-change` 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ignore-all-space)`ignore-all-space` 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ignore-space-at-eol)`ignore-space-at-eol` 


[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ignore-cr-at-eol)`ignore-cr-at-eol` 
    
Treats lines with the indicated type of whitespace change as unchanged for the sake of a three-way merge. Whitespace changes mixed with other changes to a line are not ignored. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `-b`, `-w`, `--ignore-space-at-eol`, and `--ignore-cr-at-eol`.
  * If _their_ version only introduces whitespace changes to a line, _our_ version is used;
  * If _our_ version introduces whitespace changes but _their_ version includes a substantial change, _their_ version is used;
  * Otherwise, the merge proceeds in the usual way.



[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-renormalize)`renormalize` 
    
This runs a virtual check-out and check-in of all three stages of any file which needs a three-way merge. This option is meant to be used when merging branches with different clean filters or end-of-line normalization rules. See "Merging branches with differing checkin/checkout attributes" in [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-no-renormalize)`no-renormalize` 
    
Disables the `renormalize` option. This overrides the `merge.renormalize` configuration variable. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-find-renamesn)`find-renames`[`=`_< n>_] 
    
Turn on rename detection, optionally setting the similarity threshold. This is the default. This overrides the `merge.renames` configuration variable. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--find-renames`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rename-thresholdn)`rename-threshold=`_< n>_ 
    
Deprecated synonym for `find-renames=`_< n>_. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-no-renames)`no-renames` 
    
Turn off rename detection. This overrides the `merge.renames` configuration variable. See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--no-renames`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-histogram)`histogram` 
    
Deprecated synonym for `diff-algorithm=histogram`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-patience)`patience` 
    
Deprecated synonym for `diff-algorithm=patience`. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-diff-algorithmhistogramminimalmyerspatience)`diff-algorithm=`(`histogram`|`minimal`|`myers`|`patience`) 
    
Use a different diff algorithm while merging, which can help avoid mismerges that occur due to unimportant matching lines (such as braces from distinct functions). See also [git-diff[1]](https://git-scm.com/docs/git-diff) `--diff-algorithm`. Note that `ort` defaults to `diff-algorithm=histogram`, while regular diffs currently default to the `diff.algorithm` config setting. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-subtreepath)`subtree`[`=`_< path>_] 
    
This option is a more advanced form of _subtree_ strategy, where the strategy makes a guess on how two trees must be shifted to match with each other when merging. Instead, the specified path is prefixed (or stripped from the beginning) to make the shape of two trees to match. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-recursive)`recursive` 
    
This is now a synonym for `ort`. It was an alternative implementation until v2.49.0, but was redirected to mean `ort` in v2.50.0. The previous recursive strategy was the default strategy for resolving two heads from Git v0.99.9k until v2.33.0. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-resolve)`resolve` 
    
This can only resolve two heads (i.e. the current branch and another branch you pulled from) using a 3-way merge algorithm. It tries to carefully detect criss-cross merge ambiguities. It does not handle renames. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-octopus)`octopus` 
    
This resolves cases with more than two heads, but refuses to do a complex merge that needs manual resolution. It is primarily meant to be used for bundling topic branch heads together. This is the default merge strategy when pulling or merging more than one branch. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-ours-1)`ours` 
    
This resolves any number of heads, but the resulting tree of the merge is always that of the current branch head, effectively ignoring all changes from all other branches. It is meant to be used to supersede old development history of side branches. Note that this is different from the `-Xours` option to the `ort` merge strategy. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-subtree)`subtree` 
    
This is a modified `ort` strategy. When merging trees A and B, if B corresponds to a subtree of A, B is first adjusted to match the tree structure of A, instead of reading the trees at the same level. This adjustment is also done to the common ancestor tree.
With the strategies that use 3-way merge (including the default, `ort`), if a change is made on both branches, but later reverted on one of the branches, that change will be present in the merged result; some people find this behavior confusing. It occurs because only the heads and the merge base are considered when performing a merge, not the individual commits. The merge algorithm therefore considers the reverted change as no change at all, and substitutes the changed version instead.
##  [](https://git-scm.com/docs/git-rebase#_notes)NOTES
You should understand the implications of using `git` `rebase` on a repository that you share. See also RECOVERING FROM UPSTREAM REBASE below.
When the rebase is run, it will first execute a `pre-rebase` hook if one exists. You can use this hook to do sanity checks and reject the rebase if it isn’t appropriate. Please see the template `pre-rebase` hook script for an example.
Upon completion, _< branch>_ will be the current branch.
##  [](https://git-scm.com/docs/git-rebase#_interactive_mode)INTERACTIVE MODE
Rebasing interactively means that you have a chance to edit the commits which are rebased. You can reorder the commits, and you can remove them (weeding out bad or otherwise unwanted patches).
The interactive mode is meant for this type of workflow:
  1. have a wonderful idea
  2. hack on the code
  3. prepare a series for submission
  4. submit


where point 2. consists of several instances of
a) regular use
  1. finish something worthy of a commit
  2. commit


b) independent fixup
  1. realize that something does not work
  2. fix that
  3. commit it


Sometimes the thing fixed in b.2. cannot be amended to the not-quite perfect commit it fixes, because that commit is buried deeply in a patch series. That is exactly what interactive rebase is for: use it after plenty of "a"s and "b"s, by rearranging and editing commits, and squashing multiple commits into one.
Start it with the last commit you want to retain as-is:
```
git rebase -i <after-this-commit>
```

An editor will be fired up with all the commits in your current branch (ignoring merge commits), which come after the given commit. You can reorder the commits in this list to your heart’s content, and you can remove them. The list looks more or less like this:
```
pick deadbee The oneline of this commit
pick fa1afe1 The oneline of the next commit
...
```

The oneline descriptions are purely for your pleasure; _git rebase_ will not look at them but at the commit names ("deadbee" and "fa1afe1" in this example), so do not delete or edit the names.
By replacing the command "pick" with the command "edit", you can tell `git` `rebase` to stop after applying that commit, so that you can edit the files and/or the commit message, amend the commit, and continue rebasing.
To interrupt the rebase (just like an "edit" command would do, but without cherry-picking any commit first), use the "break" command.
If you just want to edit the commit message for a commit, replace the command "pick" with the command "reword".
To drop a commit, replace the command "pick" with "drop", or just delete the matching line.
If you want to fold two or more commits into one, replace the command "pick" for the second and subsequent commits with "squash" or "fixup". If the commits had different authors, the folded commit will be attributed to the author of the first commit. The suggested commit message for the folded commit is the concatenation of the first commit’s message with those identified by "squash" commands, omitting the messages of commits identified by "fixup" commands, unless "fixup -c" is used. In that case the suggested commit message is only the message of the "fixup -c" commit, and an editor is opened allowing you to edit the message. The contents (patch) of the "fixup -c" commit are still incorporated into the folded commit. If there is more than one "fixup -c" commit, the message from the final one is used. You can also use "fixup -C" to get the same behavior as "fixup -c" except without opening an editor.
`git` `rebase` will stop when "pick" has been replaced with "edit" or when a command fails due to merge errors. When you are done editing and/or resolving conflicts you can continue with `git` `rebase` `--continue`.
For example, if you want to reorder the last 5 commits, such that what was `HEAD~4` becomes the new `HEAD`. To achieve that, you would call `git` `rebase` like this:
```
$ git rebase -i HEAD~5
```

And move the first patch to the end of the list.
You might want to recreate merge commits, e.g. if you have a history like this:
```
           X
            \
         A---M---B
        /
---o---O---P---Q
```

Suppose you want to rebase the side branch starting at "A" to "Q". Make sure that the current `HEAD` is "B", and call
```
$ git rebase -i -r --onto Q O
```

Reordering and editing commits usually creates untested intermediate steps. You may want to check that your history editing did not break anything by running a test, or at least recompiling at intermediate points in history by using the "exec" command (shortcut "x"). You may do so by creating a todo list like this one:
```
pick deadbee Implement feature XXX
fixup f1a5c00 Fix to feature XXX
exec make
pick c0ffeee The oneline of the next commit
edit deadbab The oneline of the commit after
exec cd subdir; make test
...
```

The interactive rebase will stop when a command fails (i.e. exits with non-0 status) to give you an opportunity to fix the problem. You can continue with `git` `rebase` `--continue`.
The "exec" command launches the command in a shell (the default one, usually /bin/sh), so you can use shell features (like "cd", ">", ";" …​). The command is run from the root of the working tree.
```
$ git rebase -i --exec "make test"
```

This command lets you check that intermediate commits are compilable. The todo list becomes like that:
```
pick 5928aea one
exec make test
pick 04d0fda two
exec make test
pick ba46169 three
exec make test
pick f4593f9 four
exec make test
```

##  [](https://git-scm.com/docs/git-rebase#_splitting_commits)SPLITTING COMMITS
In interactive mode, you can mark commits with the action "edit". However, this does not necessarily mean that `git` `rebase` expects the result of this edit to be exactly one commit. Indeed, you can undo the commit, or you can add other commits. This can be used to split a commit into two:
  * Start an interactive rebase with `git` `rebase` `-i` _< commit>_`^`, where _< commit>_ is the commit you want to split. In fact, any commit range will do, as long as it contains that commit.
  * Mark the commit you want to split with the action "edit".
  * When it comes to editing that commit, execute `git` `reset` `HEAD^`. The effect is that the `HEAD` is rewound by one, and the index follows suit. However, the working tree stays the same.
  * Now add the changes to the index that you want to have in the first commit. You can use `git` `add` (possibly interactively) or `git` `gui` (or both) to do that.
  * Commit the now-current index with whatever commit message is appropriate now.
  * Repeat the last two steps until your working tree is clean.
  * Continue the rebase with `git` `rebase` `--continue`.


If you are not absolutely sure that the intermediate revisions are consistent (they compile, pass the testsuite, etc.) you should use `git` `stash` to stash away the not-yet-committed changes after each commit, test, and amend the commit if fixes are necessary.
##  [](https://git-scm.com/docs/git-rebase#_recovering_from_upstream_rebase)RECOVERING FROM UPSTREAM REBASE
Rebasing (or any other form of rewriting) a branch that others have based work on is a bad idea: anyone downstream of it is forced to manually fix their history. This section explains how to do the fix from the downstream’s point of view. The real fix, however, would be to avoid rebasing the upstream in the first place.
To illustrate, suppose you are in a situation where someone develops a _subsystem_ branch, and you are working on a _topic_ that is dependent on this _subsystem_. You might end up with a history like the following:
```
    o---o---o---o---o---o---o---o  master
	 \
	  o---o---o---o---o  subsystem
			   \
			    *---*---*  topic
```

If _subsystem_ is rebased against _master_ , the following happens:
```
    o---o---o---o---o---o---o---o  master
	 \			 \
	  o---o---o---o---o	  o'--o'--o'--o'--o'  subsystem
			   \
			    *---*---*  topic
```

If you now continue development as usual, and eventually merge _topic_ to _subsystem_ , the commits from _subsystem_ will remain duplicated forever:
```
    o---o---o---o---o---o---o---o  master
	 \			 \
	  o---o---o---o---o	  o'--o'--o'--o'--o'--M	 subsystem
			   \			     /
			    *---*---*-..........-*--*  topic
```

Such duplicates are generally frowned upon because they clutter up history, making it harder to follow. To clean things up, you need to transplant the commits on _topic_ to the new _subsystem_ tip, i.e., rebase _topic_. This becomes a ripple effect: anyone downstream from _topic_ is forced to rebase too, and so on!
There are two kinds of fixes, discussed in the following subsections: 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-EasycaseThechangesareliterallythesame)Easy case: The changes are literally the same. 
    
This happens if the _subsystem_ rebase was a simple rebase and had no conflicts. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-HardcaseThechangesarenotthesame)Hard case: The changes are not the same. 
    
This happens if the _subsystem_ rebase had conflicts, or used `--interactive` to omit, edit, squash, or fixup commits; or if the upstream used one of `commit` `--amend`, `reset`, or a full history rewriting command like [`filter-repo`](https://github.com/newren/git-filter-repo).
###  [](https://git-scm.com/docs/git-rebase#_the_easy_case)The easy case
Only works if the changes (patch IDs based on the diff contents) on _subsystem_ are literally the same before and after the rebase _subsystem_ did.
In that case, the fix is easy because _git rebase_ knows to skip changes that are already present in the new upstream (unless `--reapply-cherry-picks` is given). So if you say (assuming you’re on _topic_)
```
    $ git rebase subsystem
```

you will end up with the fixed history
```
    o---o---o---o---o---o---o---o  master
				 \
				  o'--o'--o'--o'--o'  subsystem
						   \
						    *---*---*  topic
```

###  [](https://git-scm.com/docs/git-rebase#_the_hard_case)The hard case
Things get more complicated if the _subsystem_ changes do not exactly correspond to the ones before the rebase.
Note |  While an "easy case recovery" sometimes appears to be successful even in the hard case, it may have unintended consequences. For example, a commit that was removed via `git` `rebase` `--interactive` will be **resurrected**!   
---|---  
The idea is to manually tell `git` `rebase` "where the old _subsystem_ ended and your _topic_ began", that is, what the old merge base between them was. You will have to find a way to name the last commit of the old _subsystem_ , for example:
  * With the _subsystem_ reflog: after `git` `fetch`, the old tip of _subsystem_ is at `subsystem@{1}`. Subsequent fetches will increase the number. (See [git-reflog[1]](https://git-scm.com/docs/git-reflog).)
  * Relative to the tip of _topic_ : knowing that your _topic_ has three commits, the old tip of _subsystem_ must be `topic~3`.


You can then transplant the old `subsystem..topic` to the new tip by saying (for the reflog case, and assuming you are on _topic_ already):
```
    $ git rebase --onto subsystem subsystem@{1}
```

The ripple effect of a "hard case" recovery is especially bad: _everyone_ downstream from _topic_ will now have to perform a "hard case" recovery too!
##  [](https://git-scm.com/docs/git-rebase#_rebasing_merges)REBASING MERGES
The interactive rebase command was originally designed to handle individual patch series. As such, it makes sense to exclude merge commits from the todo list, as the developer may have merged the then-current `master` while working on the branch, only to rebase all the commits onto `master` eventually (skipping the merge commits).
However, there are legitimate reasons why a developer may want to recreate merge commits: to keep the branch structure (or "commit topology") when working on multiple, inter-related branches.
In the following example, the developer works on a topic branch that refactors the way buttons are defined, and on another topic branch that uses that refactoring to implement a "Report a bug" button. The output of `git` `log` `--graph` `--format=%s` `-5` may look like this:
```
*   Merge branch 'report-a-bug'
|\
| * Add the feedback button
* | Merge branch 'refactor-button'
|\ \
| |/
| * Use the Button class for all buttons
| * Extract a generic Button class from the DownloadButton one
```

The developer might want to rebase those commits to a newer `master` while keeping the branch topology, for example when the first topic branch is expected to be integrated into `master` much earlier than the second one, say, to resolve merge conflicts with changes to the DownloadButton class that made it into `master`.
This rebase can be performed using the `--rebase-merges` option. It will generate a todo list looking like this:
```
label onto

# Branch: refactor-button
reset onto
pick 123456 Extract a generic Button class from the DownloadButton one
pick 654321 Use the Button class for all buttons
label refactor-button

# Branch: report-a-bug
reset refactor-button # Use the Button class for all buttons
pick abcdef Add the feedback button
label report-a-bug

reset onto
merge -C a1b2c3 refactor-button # Merge 'refactor-button'
merge -C 6f5e4d report-a-bug # Merge 'report-a-bug'
```

In contrast to a regular interactive rebase, there are `label`, `reset` and `merge` commands in addition to `pick` ones.
The `label` command associates a label with the current HEAD when that command is executed. These labels are created as worktree-local refs (`refs/rewritten/`_< label>_) that will be deleted when the rebase finishes. That way, rebase operations in multiple worktrees linked to the same repository do not interfere with one another. If the `label` command fails, it is rescheduled immediately, with a helpful message how to proceed.
The `reset` command resets the HEAD, index and worktree to the specified revision. It is similar to an `exec` `git` `reset` `--hard` _< label>_, but refuses to overwrite untracked files. If the `reset` command fails, it is rescheduled immediately, with a helpful message how to edit the todo list (this typically happens when a `reset` command was inserted into the todo list manually and contains a typo).
The `merge` command will merge the specified revision(s) into whatever is HEAD at that time. With `-C` _< original-commit>_, the commit message of the specified merge commit will be used. When the `-C` is changed to a lower-case `-c`, the message will be opened in an editor after a successful merge so that the user can edit the message.
If a `merge` command fails for any reason other than merge conflicts (i.e. when the merge operation did not even start), it is rescheduled immediately.
By default, the `merge` command will use the `ort` merge strategy for regular merges, and `octopus` for octopus merges. One can specify a default strategy for all merges using the `--strategy` argument when invoking rebase, or can override specific merges in the interactive list of commands by using an `exec` command to call `git` `merge` explicitly with a `--strategy` argument. Note that when calling `git` `merge` explicitly like this, you can make use of the fact that the labels are worktree-local refs (the ref `refs/rewritten/onto` would correspond to the label `onto`, for example) in order to refer to the branches you want to merge.
Note: the first command (`label` `onto`) labels the revision onto which the commits are rebased; The name `onto` is just a convention, as a nod to the `--onto` option.
It is also possible to introduce completely new merge commits from scratch by adding a command of the form `merge` _< merge-head>_. This form will generate a tentative commit message and always open an editor to let the user edit it. This can be useful e.g. when a topic branch turns out to address more than a single concern and wants to be split into two or even more topic branches. Consider this todo list:
```
pick 192837 Switch from GNU Makefiles to CMake
pick 5a6c7e Document the switch to CMake
pick 918273 Fix detection of OpenSSL in CMake
pick afbecd http: add support for TLS v1.3
pick fdbaec Fix detection of cURL in CMake on Windows
```

The one commit in this list that is not related to CMake may very well have been motivated by working on fixing all those bugs introduced by switching to CMake, but it addresses a different concern. To split this branch into two topic branches, the todo list could be edited like this:
```
label onto

pick afbecd http: add support for TLS v1.3
label tlsv1.3

reset onto
pick 192837 Switch from GNU Makefiles to CMake
pick 918273 Fix detection of OpenSSL in CMake
pick fdbaec Fix detection of cURL in CMake on Windows
pick 5a6c7e Document the switch to CMake
label cmake

reset onto
merge tlsv1.3
merge cmake
```

##  [](https://git-scm.com/docs/git-rebase#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebasebackend)rebase.backend 
    
Default backend to use for rebasing. Possible choices are _apply_ or _merge_. In the future, if the merge backend gains all remaining capabilities of the apply backend, this setting may become unused. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebasestat)rebase.stat 
    
Whether to show a diffstat of what changed upstream since the last rebase. False by default. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaseautoSquash)rebase.autoSquash 
    
If set to true, enable the `--autosquash` option of [git-rebase[1]](https://git-scm.com/docs/git-rebase) by default for interactive mode. This can be overridden with the `--no-autosquash` option. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaseautoStash)rebase.autoStash 
    
When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts. This option can be overridden by the `--no-autostash` and `--autostash` options of [git-rebase[1]](https://git-scm.com/docs/git-rebase). Defaults to false. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaseupdateRefs)rebase.updateRefs 
    
If set to true enable `--update-refs` option by default. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebasemissingCommitsCheck)rebase.missingCommitsCheck 
    
If set to "warn", git rebase -i will print a warning if some commits are removed (e.g. a line was deleted), however the rebase will still proceed. If set to "error", it will print the previous warning and stop the rebase, _git rebase --edit-todo_ can then be used to correct the error. If set to "ignore", no checking is done. To drop a commit without warning or error, use the `drop` command in the todo list. Defaults to "ignore". 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaseinstructionFormat)rebase.instructionFormat 
    
A format string, as specified in [git-log[1]](https://git-scm.com/docs/git-log), to be used for the todo list during an interactive rebase. The format will automatically have the commit hash prepended to the format. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaseabbreviateCommands)rebase.abbreviateCommands 
    
If set to true, `git` `rebase` will use abbreviated command names in the todo list resulting in something like this:
```
	p deadbee The oneline of the commit
	p fa1afe1 The oneline of the next commit
	...
```

instead of:
```
	pick deadbee The oneline of the commit
	pick fa1afe1 The oneline of the next commit
	...
```

Defaults to false. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaserescheduleFailedExec)rebase.rescheduleFailedExec 
    
Automatically reschedule `exec` commands that failed. This only makes sense in interactive mode (or when an `--exec` option was provided). This is the same as specifying the `--reschedule-failed-exec` option. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaseforkPoint)rebase.forkPoint 
    
If set to false set `--no-fork-point` option by default. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebaserebaseMerges)rebase.rebaseMerges 
    
Whether and how to set the `--rebase-merges` option by default. Can be `rebase-cousins`, `no-rebase-cousins`, or a boolean. Setting to true or to `no-rebase-cousins` is equivalent to `--rebase-merges=no-rebase-cousins`, setting to `rebase-cousins` is equivalent to `--rebase-merges=rebase-cousins`, and setting to false is equivalent to `--no-rebase-merges`. Passing `--rebase-merges` on the command line, with or without an argument, overrides any `rebase.rebaseMerges` configuration. 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-rebasemaxLabelLength)rebase.maxLabelLength 
    
When generating label names from commit subjects, truncate the names to this length. By default, the names are truncated to a little less than `NAME_MAX` (to allow e.g. `.lock` files to be written for the corresponding loose refs). 

[](https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt-sequenceeditor)sequence.editor 
    
Text editor used by `git` `rebase` `-i` for editing the rebase instruction file. The value is meant to be interpreted by the shell when it is used. It can be overridden by the `GIT_SEQUENCE_EDITOR` environment variable. When not configured, the default commit message editor is used instead.
##  [](https://git-scm.com/docs/git-rebase#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### rebase
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
