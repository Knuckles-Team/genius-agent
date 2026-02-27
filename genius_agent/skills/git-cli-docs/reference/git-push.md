[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --everything-is-local
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
    * [NAME](https://git-scm.com/docs/git-push#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-push#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-push#_description)
    * [OPTIONS](https://git-scm.com/docs/git-push#OPTIONS)
    * [GIT URLS](https://git-scm.com/docs/git-push#_git_urls)
    * [REMOTES](https://git-scm.com/docs/git-push#_remotes)
    * [UPSTREAM BRANCHES](https://git-scm.com/docs/git-push#UPSTREAM-BRANCHES)
    * [OUTPUT](https://git-scm.com/docs/git-push#_output)
    * [PUSH RULES](https://git-scm.com/docs/git-push#_push_rules)
    * [NOTE ABOUT FAST-FORWARDS](https://git-scm.com/docs/git-push#_note_about_fast_forwards)
    * [EXAMPLES](https://git-scm.com/docs/git-push#_examples)
    * [SECURITY](https://git-scm.com/docs/git-push#_security)
    * [CONFIGURATION](https://git-scm.com/docs/git-push#CONFIGURATION)
    * [GIT](https://git-scm.com/docs/git-push#_git)


[ English ▾](https://git-scm.com/docs/git-push)
Localized versions of **git-push** manual
  1. [English ](https://git-scm.com/docs/git-push)
  2. [Français ](https://git-scm.com/docs/git-push/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-push/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-push/sv)
  5. [українська мова ](https://git-scm.com/docs/git-push/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-push/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-push)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-push) git-push last updated in 2.53.0
Changes in the **git-push** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-push/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-push/2.52.0)
  3. 2.48.1 → 2.51.2 no changes
  4. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-push/2.48.0)
  5. 2.45.1 → 2.47.3 no changes
  6. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-push/2.45.0)
  7. 2.44.1 → 2.44.4 no changes
  8. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-push/2.44.0)
  9. 2.43.1 → 2.43.7 no changes
  10. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-push/2.43.0)
  11. 2.42.2 → 2.42.4 no changes
  12. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-push/2.42.1)
  13. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-push/2.42.0)
  14. 2.41.1 → 2.41.3 no changes
  15. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-push/2.41.0)
  16. 2.40.1 → 2.40.4 no changes
  17. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-push/2.40.0)
  18. 2.39.1 → 2.39.5 no changes
  19. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-push/2.39.0)
  20. 2.38.1 → 2.38.5 no changes
  21. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-push/2.38.0)
  22. 2.35.1 → 2.37.7 no changes
  23. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-push/2.35.0)
  24. 2.33.1 → 2.34.8 no changes
  25. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-push/2.33.0)
  26. 2.32.1 → 2.32.7 no changes
  27. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-push/2.32.0)
  28. 2.30.1 → 2.31.8 no changes
  29. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-push/2.30.0)
  30. 2.25.1 → 2.29.3 no changes
  31. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-push/2.25.0)
  32. 2.23.1 → 2.24.4 no changes
  33. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-push/2.23.0)
  34. 2.22.1 → 2.22.5 no changes
  35. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-push/2.22.0)
  36. 2.21.1 → 2.21.4 no changes
  37. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-push/2.21.0)
  38. 2.20.1 → 2.20.5 no changes
  39. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-push/2.20.0)
  40. 2.18.1 → 2.19.6 no changes
  41. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-push/2.18.0)
  42. 2.17.0 → 2.17.6 no changes
  43. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-push/2.16.6)
  44. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-push/2.15.4)
  45. 2.14.6 no changes
  46. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-push/2.13.7)
  47. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-push/2.12.5)
  48. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-push/2.11.4)
  49. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-push/2.10.5)
  50. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-push/2.9.5)
  51. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-push/2.8.6)
  52. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-push/2.7.6)
  53. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-push/2.6.7)
  54. 2.5.6 no changes
  55. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-push/2.4.12)
  56. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-push/2.3.10)
  57. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-push/2.2.3)
  58. 2.1.4 no changes
  59. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-push/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-push#_name)NAME
git-push - Update remote refs along with associated objects
##  [](https://git-scm.com/docs/git-push#_synopsis)SYNOPSIS
```
git push [--all | --branches | --mirror | --tags] [--follow-tags] [--atomic] [-n | --dry-run] [--receive-pack=_<git-receive-pack>_]
	 [--repo=_<repository>_] [-f | --force] [-d | --delete] [--prune] [-q | --quiet] [-v | --verbose]
	 [-u | --set-upstream] [-o _<string>_ | --push-option=_<string>_]
	 [--[no-]signed | --signed=(true|false|if-asked)]
	 [--force-with-lease[=_<refname>_[:_<expect>_]] [--force-if-includes]]
	 [--no-verify] [_<repository>_ [_<refspec>_…​]]
```

##  [](https://git-scm.com/docs/git-push#_description)DESCRIPTION
Updates one or more branches, tags, or other references in a remote repository from your local repository, and sends all necessary data that isn’t already on the remote.
The simplest way to push is `git` `push` _< remote>_ _< branch>_. `git` `push` `origin` `main` will push the local `main` branch to the `main` branch on the remote named `origin`.
The _< repository>_ argument defaults to the upstream for the current branch, or `origin` if there’s no configured upstream.
To decide which branches, tags, or other refs to push, Git uses (in order of precedence):
  1. The _< refspec>_ argument(s) (for example `main` in `git` `push` `origin` `main`) or the `--all`, `--mirror`, or `--tags` options
  2. The `remote.`_< name>_`.push` configuration for the repository being pushed to
  3. The `push.default` configuration. The default is `push.default=simple`, which will push to a branch with the same name as the current branch. See the [CONFIGURATION](https://git-scm.com/docs/git-push#CONFIGURATION) section below for more on `push.default`.


`git` `push` may fail if you haven’t set an upstream for the current branch, depending on what `push.default` is set to. See the [UPSTREAM BRANCHES](https://git-scm.com/docs/git-push#UPSTREAM-BRANCHES) section below for more on how to set and use upstreams.
You can make interesting things happen to a repository every time you push into it, by setting up _hooks_ there. See documentation for [git-receive-pack[1]](https://git-scm.com/docs/git-receive-pack).
##  [](https://git-scm.com/docs/git-push#OPTIONS)OPTIONS 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-repository)_< repository>_ 
    
The "remote" repository that is the destination of a push operation. This parameter can be either a URL (see the section [GIT URLS](https://git-scm.com/docs/git-push#URLS) below) or the name of a remote (see the section [REMOTES](https://git-scm.com/docs/git-push#REMOTES) below). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-refspec)_< refspec>_... 
    
Specify what destination ref to update with what source object.
The format for a refspec is [`+`]_< src>_[`:`_< dst>_], for example `main`, `main:other`, or `HEAD^:refs/heads/main`.
The _< src>_ is often the name of the local branch to push, but it can be any arbitrary "SHA-1 expression" (see [gitrevisions[7]](https://git-scm.com/docs/gitrevisions)).
The _< dst>_ determines what ref to update on the remote side. It must be the name of a branch, tag, or other ref, not an arbitrary expression.
The `+` is optional and does the same thing as `--force`.
You can write a refspec using the fully expanded form (for example `refs/heads/main:refs/heads/main`) which specifies the exact source and destination, or with a shorter form (for example `main` or `main:other`). Here are the rules for how refspecs are expanded, as well as various other special refspec forms:
  * _< src>_ without a `:`_< dst>_ means to update the same ref as the _< src>_, unless the `remote.`_< repository>_`.push` configuration specifies a different _< dst>_. For example, if `main` is a branch, then the refspec `main` expands to `main:refs/heads/main`.
  * If _< dst>_ unambiguously refers to a ref on the <repository> remote, then expand it to that ref. For example, if `v1.0` is a tag on the remote, then `HEAD:v1.0` expands to `HEAD:refs/tags/v1.0`.
  * If _< src>_ resolves to a ref starting with `refs/heads/` or `refs/tags/`, then prepend that to <dst>. For example, if `main` is a branch, then `main:other` expands to `main:refs/heads/other`
  * The special refspec `:` (or `+:` to allow non-fast-forward updates) directs Git to push "matching" branches: for every branch that exists on the local side, the remote side is updated if a branch of the same name already exists on the remote side.
  * _< src>_ may contain a `*` to indicate a simple pattern match. This works like a glob that matches any ref matching the pattern. There must be only one `*` in both the _< src>_ and _< dst>_. It will map refs to the destination by replacing the * with the contents matched from the source. For example, `refs/heads/*:refs/heads/*` will push all branches.
  * A refspec starting with `^` is a negative refspec. This specifies refs to exclude. A ref will be considered to match if it matches at least one positive refspec, and does not match any negative refspec. Negative refspecs can be pattern refspecs. They must only contain a _< src>_. Fully spelled out hex object names are also not supported. For example, `git` `push` `origin` `refs/heads/*'` `^refs/heads/dev-*'` will push all branches except for those starting with `dev-`
  * If _< src>_ is empty, it deletes the _< dst>_ ref from the remote repository. For example, `git` `push` `origin` `:dev` will delete the `dev` branch.
  * `tag` _< tag>_ expands to `refs/tags/`_< tag>_`:refs/tags/`_< tag>_. This is technically a special syntax for `git` `push` and not a refspec, since in `git` `push` `origin` `tag` `v1.0` the arguments `tag` and `v1.0` are separate.
  * If the refspec can’t be expanded unambiguously, error out with an error indicating what was tried, and depending on the `advice.pushUnqualifiedRefname` configuration (see [git-config[1]](https://git-scm.com/docs/git-config)) suggest what refs/ namespace you may have wanted to push to.


Not all updates are allowed: see PUSH RULES below for the details. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---all)`--all` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---branches)`--branches` 
    
Push all branches (i.e. refs under `refs/heads/`); cannot be used with other <refspec>. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---prune)`--prune` 
    
Remove remote branches that don’t have a local counterpart. For example a remote branch `tmp` will be removed if a local branch with the same name doesn’t exist any more. This also respects refspecs, e.g. `git` `push` `--prune` `remote` `refs/heads/*:refs/tmp/*` would make sure that remote `refs/tmp/foo` will be removed if `refs/heads/foo` doesn’t exist. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---mirror)`--mirror` 
    
Instead of naming each ref to push, specifies that all refs under `refs/` (which includes but is not limited to `refs/heads/`, `refs/remotes/`, and `refs/tags/`) be mirrored to the remote repository. Newly created local refs will be pushed to the remote end, locally updated refs will be force updated on the remote end, and deleted refs will be removed from the remote end. This is the default if the configuration option `remote.`_< remote>_`.mirror` is set. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--n)`-n` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---dry-run)`--dry-run` 
    
Do everything except actually send the updates. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---porcelain)`--porcelain` 
    
Produce machine-readable output. The output status line for each ref will be tab-separated and sent to stdout instead of stderr. The full symbolic names of the refs will be given. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--d)`-d` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---delete)`--delete` 
    
All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---tags)`--tags` 
    
All refs under `refs/tags` are pushed, in addition to refspecs explicitly listed on the command line. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---follow-tags)`--follow-tags` 
    
Push all the refs that would be pushed without this option, and also push annotated tags in `refs/tags` that are missing from the remote but are pointing at commit-ish that are reachable from the refs being pushed. This can also be specified with configuration variable `push.followTags`. For more information, see `push.followTags` in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---signed)`--signed` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-signed)`--no-signed` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---signedtruefalseif-asked)`--signed=`(`true`|`false`|`if-asked`) 
    
GPG-sign the push request to update refs on the receiving side, to allow it to be checked by the hooks and/or be logged. Possible values are: 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-false)`false` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-signed-1)`--no-signed` 
    
no signing will be attempted. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-true)`true` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---signed-1)`--signed` 
    
the push will fail if the server does not support signed pushes. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-if-asked)`if-asked` 
    
sign if and only if the server supports signed pushes. The push will also fail if the actual call to `gpg` `--sign` fails. See [git-receive-pack[1]](https://git-scm.com/docs/git-receive-pack) for the details on the receiving end. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---atomic)`--atomic` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-atomic)`--no-atomic` 
    
Use an atomic transaction on the remote side if available. Either all refs are updated, or on error, no refs are updated. If the server does not support atomic pushes the push will fail. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--ooption)`-o` _< option>_ 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---push-optionoption)`--push-option=`_< option>_ 
    
Transmit the given string to the server, which passes them to the pre-receive as well as the post-receive hook. The given string must not contain a _NUL_ or _LF_ character. When multiple `--push-option=`_< option>_ are given, they are all sent to the other side in the order listed on the command line. When no `--push-option=`_< option>_ is given from the command line, the values of configuration variable `push.pushOption` are used instead. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---receive-packgit-receive-pack)`--receive-pack=`_< git-receive-pack>_ 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---execgit-receive-pack)`--exec=`_< git-receive-pack>_ 
    
Path to the _git-receive-pack_ program on the remote end. Sometimes useful when pushing to a remote repository over ssh, and you do not have the program in a directory on the default `$PATH`. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force-with-lease)`--force-with-lease` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-force-with-lease)`--no-force-with-lease` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force-with-leaserefname)`--force-with-lease=`_< refname>_ 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force-with-leaserefnameexpect)`--force-with-lease=`_< refname>_`:`_< expect>_ 
    
Usually, `git` `push` refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it.
This option overrides this restriction if the current value of the remote ref is the expected value. `git` `push` fails otherwise.
Imagine that you have to rebase what you have already published. You will have to bypass the "must fast-forward" rule in order to replace the history you originally published with the rebased history. If somebody else built on top of your original history while you are rebasing, the tip of the branch at the remote may advance with their commit, and blindly pushing with `--force` will lose their work.
This option allows you to say that you expect the history you are updating is what you rebased and want to replace. If the remote ref still points at the commit you specified, you can be sure that no other people did anything to the ref. It is like taking a "lease" on the ref without explicitly locking it, and the remote ref is updated only if the "lease" is still valid.
`--force-with-lease` alone, without specifying the details, will protect all remote refs that are going to be updated by requiring their current value to be the same as the remote-tracking branch we have for them.
`--force-with-lease=`_< refname>_, without specifying the expected value, will protect _< refname>_ (alone), if it is going to be updated, by requiring its current value to be the same as the remote-tracking branch we have for it.
`--force-with-lease=`_< refname>_`:`_< expect>_ will protect _< refname>_ (alone), if it is going to be updated, by requiring its current value to be the same as the specified value _< expect>_ (which is allowed to be different from the remote-tracking branch we have for the refname, or we do not even have to have such a remote-tracking branch when this form is used). If _< expect>_ is the empty string, then the named ref must not already exist.
Note that all forms other than `--force-with-lease=`_< refname>_`:`_< expect>_ that specifies the expected current value of the ref explicitly are still experimental and their semantics may change as we gain experience with this feature.
`--no-force-with-lease` will cancel all the previous `--force-with-lease` on the command line.
A general note on safety: supplying this option without an expected value, i.e. as `--force-with-lease` or `--force-with-lease=`_< refname>_ interacts very badly with anything that implicitly runs `git` `fetch` on the remote to be pushed to in the background, e.g. `git` `fetch` `origin` on your repository in a cronjob.
The protection it offers over `--force` is ensuring that subsequent changes your work wasn’t based on aren’t clobbered, but this is trivially defeated if some background process is updating refs in the background. We don’t have anything except the remote tracking info to go by as a heuristic for refs you’re expected to have seen & are willing to clobber.
If your editor or some other system is running `git` `fetch` in the background for you a way to mitigate this is to simply set up another remote:
```
git remote add origin-push $(git config remote.origin.url)
git fetch origin-push
```

Now when the background process runs `git` `fetch` `origin` the references on `origin-push` won’t be updated, and thus commands like:
```
git push --force-with-lease origin-push
```

Will fail unless you manually run `git` `fetch` `origin-push`. This method is of course entirely defeated by something that runs `git` `fetch` `--all`, in that case you’d need to either disable it or do something more tedious like:
```
git fetch              # update 'master' from remote
git tag base master    # mark our base point
git rebase -i master   # rewrite some commits
git push --force-with-lease=master:base master:master
```

I.e. create a `base` tag for versions of the upstream code that you’ve seen and are willing to overwrite, then rewrite history, and finally force push changes to `master` if the remote version is still at `base`, regardless of what your local `remotes/origin/master` has been updated to in the background.
Alternatively, specifying `--force-if-includes` as an ancillary option along with `--force-with-lease`[`=`_< refname>_] (i.e., without saying what exact commit the ref on the remote side must be pointing at, or which refs on the remote side are being protected) at the time of "push" will verify if updates from the remote-tracking refs that may have been implicitly updated in the background are integrated locally before allowing a forced update. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--f)`-f` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force)`--force` 
    
Usually, `git` `push` will refuse to update a branch that is not an ancestor of the commit being pushed.
This flag disables that check, the other safety checks in PUSH RULES below, and the checks in `--force-with-lease`. It can cause the remote repository to lose commits; use it with care.
Note that `--force` applies to all the refs that are pushed, hence using it with `push.default` set to `matching` or with multiple push destinations configured with `remote.`_< name>_`.push` may overwrite refs other than the current branch (including local refs that are strictly behind their remote counterpart). To force a push to only one branch, use a `+` in front of the refspec to push (e.g `git` `push` `origin` `+master` to force a push to the `master` branch). See the _< refspec>_... section above for details. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---force-if-includes)`--force-if-includes` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-force-if-includes)`--no-force-if-includes` 
    
Force an update only if the tip of the remote-tracking ref has been integrated locally.
This option enables a check that verifies if the tip of the remote-tracking ref is reachable from one of the "reflog" entries of the local branch based in it for a rewrite. The check ensures that any updates from the remote have been incorporated locally by rejecting the forced update if that is not the case.
If the option is passed without specifying `--force-with-lease`, or specified along with `--force-with-lease=`_< refname>_`:`_< expect>_, it is a "no-op".
Specifying `--no-force-if-includes` disables this behavior. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---reporepository)`--repo=`_< repository>_ 
    
This option is equivalent to the _< repository>_ argument. If both are specified, the command-line argument takes precedence. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--u)`-u` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---set-upstream)`--set-upstream` 
    
For every branch that is up to date or successfully pushed, add upstream (tracking) reference, used by argument-less [git-pull[1]](https://git-scm.com/docs/git-pull) and other commands. For more information, see `branch.`_< name>_`.merge` in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---thin)`--thin` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-thin)`--no-thin` 
    
These options are passed to [git-send-pack[1]](https://git-scm.com/docs/git-send-pack). A thin transfer significantly reduces the amount of sent data when the sender and receiver share many of the same objects in common. The default is `--thin`. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--q)`-q` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---quiet)`--quiet` 
    
Suppress all output, including the listing of updated refs, unless an error occurs. Progress is not reported to the standard error stream. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--v)`-v` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---verbose)`--verbose` 
    
Run verbosely. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---progress)`--progress` 
    
Progress status is reported on the standard error stream by default when it is attached to a terminal, unless `-q` is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-recurse-submodules)`--no-recurse-submodules` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---recurse-submodulescheckon-demandonlyno)`--recurse-submodules=`(`check`|`on-demand`|`only`|`no`) 
    
May be used to make sure all submodule commits used by the revisions to be pushed are available on a remote-tracking branch. Possible values are: 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-check)`check` 
    
Git will verify that all submodule commits that changed in the revisions to be pushed are available on at least one remote of the submodule. If any commits are missing the push will be aborted and exit with non-zero status. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-on-demand)`on-demand` 
    
all submodules that changed in the revisions to be pushed will be pushed. If `on-demand` was not able to push all necessary revisions it will also be aborted and exit with non-zero status. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-only)`only` 
    
all submodules will be pushed while the superproject is left unpushed. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-no)`no` 
    
override the `push.recurseSubmodules` configuration variable when no submodule recursion is required. Similar to using `--no-recurse-submodules`.
When using `on-demand` or `only`, if a submodule has a `push.recurseSubmodules=`(`on-demand`|`only`) or `submodule.recurse` configuration, further recursion will occur. In this case, `only` is treated as `on-demand`. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---verify)`--verify` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-verify)`--no-verify` 
    
Toggle the pre-push hook (see [githooks[5]](https://git-scm.com/docs/githooks)). The default is `--verify`, giving the hook a chance to prevent the push. With `--no-verify`, the hook is bypassed completely. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--4)`-4` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---ipv4)`--ipv4` 
    
Use IPv4 addresses only, ignoring IPv6 addresses. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--6)`-6` 


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt---ipv6)`--ipv6` 
    
Use IPv6 addresses only, ignoring IPv4 addresses.
##  [](https://git-scm.com/docs/git-push#_git_urls)GIT URLS
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
##  [](https://git-scm.com/docs/git-push#_remotes)REMOTES
The name of one of the following can be used instead of a URL as _< repository>_ argument:
  * a remote in the Git configuration file: `$GIT_DIR/config`,
  * a file in the `$GIT_DIR/remotes` directory, or
  * a file in the `$GIT_DIR/branches` directory.


All of these also allow you to omit the refspec from the command line because they each contain a refspec which git will use by default.
###  [](https://git-scm.com/docs/git-push#_named_remote_in_configuration_file)Named remote in configuration file
You can choose to provide the name of a remote which you had previously configured using [git-remote[1]](https://git-scm.com/docs/git-remote), [git-config[1]](https://git-scm.com/docs/git-config) or even by a manual edit to the `$GIT_DIR/config` file. The URL of this remote will be used to access the repository. The refspec of this remote will be used by default when you do not provide a refspec on the command line. The entry in the config file would appear like this:
```
	[remote "<name>"]
		url = <URL>
		pushurl = <pushurl>
		push = <refspec>
		fetch = <refspec>
```

The _< pushurl>_ is used for pushes only. It is optional and defaults to _< URL>_. Pushing to a remote affects all defined pushurls or all defined urls if no pushurls are defined. Fetch, however, will only fetch from the first defined url if multiple urls are defined.
###  [](https://git-scm.com/docs/git-push#_named_file_in_git_dirremotes)Named file in `$GIT_DIR/remotes`
You can choose to provide the name of a file in `$GIT_DIR/remotes`. The URL in this file will be used to access the repository. The refspec in this file will be used as default when you do not provide a refspec on the command line. This file should have the following format:
```
	URL: one of the above URL formats
	Push: <refspec>
	Pull: <refspec>
```

`Push:` lines are used by `git` `push` and `Pull:` lines are used by `git` `pull` and `git` `fetch`. Multiple `Push:` and `Pull:` lines may be specified for additional branch mappings.
###  [](https://git-scm.com/docs/git-push#_named_file_in_git_dirbranches)Named file in `$GIT_DIR/branches`
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

##  [](https://git-scm.com/docs/git-push#UPSTREAM-BRANCHES)UPSTREAM BRANCHES
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
##  [](https://git-scm.com/docs/git-push#_output)OUTPUT
The output of "git push" depends on the transport method used; this section describes the output when pushing over the Git protocol (either locally or via ssh).
The status of the push is output in tabular form, with each line representing the status of a single ref. Each line is of the form:
```
 <flag> <summary> <from> -> <to> (<reason>)
```

If `--porcelain` is used, then each line of the output is of the form:
```
 <flag> \t <from>:<to> \t <summary> (<reason>)
```

The status of up-to-date refs is shown only if `--porcelain` or `--verbose` option is used. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-flag)_< flag>_ 
    
A single character indicating the status of the ref: 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-space)(space) 
    
for a successfully pushed fast-forward; 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-)`+` 
    
for a successful forced update; 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--)`-` 
    
for a successfully deleted ref; 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--1)`*` 
    
for a successfully pushed new ref; 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--1-1)`!` 
    
for a ref that was rejected or failed to push; and 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt--1-1-1)`=` 
    
for a ref that was up to date and did not need pushing. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-summary)_< summary>_ 
    
For a successfully pushed ref, the summary shows the old and new values of the ref in a form suitable for using as an argument to `git` `log` (this is _< old>_`..`_< new>_ in most cases, and _< old>_`...`_< new>_ for forced non-fast-forward updates).
For a failed update, more details are given: 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-rejected)rejected 
    
Git did not try to send the ref at all, typically because it is not a fast-forward and you did not force the update. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-remoterejected)remote rejected 
    
The remote end refused the update. Usually caused by a hook on the remote side, or because the remote repository has one of the following safety options in effect: `receive.denyCurrentBranch` (for pushes to the checked out branch), `receive.denyNonFastForwards` (for forced non-fast-forward updates), `receive.denyDeletes` or `receive.denyDeleteCurrent`. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-remotefailure)remote failure 
    
The remote end did not report the successful update of the ref, perhaps because of a temporary error on the remote side, a break in the network connection, or other transient error. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-from)from 
    
The name of the local ref being pushed, minus its `refs/`_< type>_`/` prefix. In the case of deletion, the name of the local ref is omitted. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-to)to 
    
The name of the remote ref being updated, minus its `refs/`_< type>_`/` prefix. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-reason)reason 
    
A human-readable explanation. In the case of successfully pushed refs, no explanation is needed. For a failed ref, the reason for failure is described.
##  [](https://git-scm.com/docs/git-push#_push_rules)PUSH RULES
As a safety feature, the `git` `push` command only allows certain kinds of updates to prevent you from accidentally losing data on the remote.
Because branches and tags are intended to be used differently, the safety rules for pushing to a branch are different from the rules for pushing to a tag. In the following rules "update" means any modifications except deletions and creations. Deletions and creations are always allowed, except when forbidden by configuration or hooks.
  1. If the push destination is a **branch** (`refs/heads/*`): only fast-forward updates are allowed, which means the destination must be an ancestor of the source commit. The source must be a commit.
  2. If the push destination is a **tag** (`refs/tags/*`): all updates will be rejected. The source can be any object.
  3. If the push destination is not a branch or tag:
     * If the source is a tree or blob object, any updates will be rejected
     * If the source is a tag or commit object, any fast-forward update is allowed, even in cases where what’s being fast-forwarded is not a commit, but a tag object which happens to point to a new commit which is a fast-forward of the commit the last tag (or commit) it’s replacing. Replacing a tag with an entirely different tag is also allowed, if it points to the same commit, as well as pushing a peeled tag, i.e. pushing the commit that existing tag object points to, or a new tag object which an existing commit points to.


You can override these rules by passing `--force` or by adding the optional leading `+` to a refspec. The only exceptions are that no amount of forcing will make a branch accept a non-commit object, and forcing won’t make the remote repository accept a push that it’s configured to deny.
Hooks and configuration can also override or amend these rules, see e.g. `receive.denyNonFastForwards` and `receive.denyDeletes` in [git-config[1]](https://git-scm.com/docs/git-config) and `pre-receive` and `update` in [githooks[5]](https://git-scm.com/docs/githooks).
##  [](https://git-scm.com/docs/git-push#_note_about_fast_forwards)NOTE ABOUT FAST-FORWARDS
When an update changes a branch (or more in general, a ref) that used to point at commit A to point at another commit B, it is called a fast-forward update if and only if B is a descendant of A.
In a fast-forward update from A to B, the set of commits that the original commit A built on top of is a subset of the commits the new commit B builds on top of. Hence, it does not lose any history.
In contrast, a non-fast-forward update will lose history. For example, suppose you and somebody else started at the same commit X, and you built a history leading to commit B while the other person built a history leading to commit A. The history looks like this:
```
      B
     /
 ---X---A
```

Further suppose that the other person already pushed changes leading to A back to the original repository from which you two obtained the original commit X.
The push done by the other person updated the branch that used to point at commit X to point at commit A. It is a fast-forward.
But if you try to push, you will attempt to update the branch (that now points at A) with commit B. This does _not_ fast-forward. If you did so, the changes introduced by commit A will be lost, because everybody will now start building on top of B.
The command by default does not allow an update that is not a fast-forward to prevent such loss of history.
If you do not want to lose your work (history from X to B) or the work by the other person (history from X to A), you would need to first fetch the history from the repository, create a history that contains changes done by both parties, and push the result back.
You can perform "git pull", resolve potential conflicts, and "git push" the result. A "git pull" will create a merge commit C between commits A and B.
```
      B---C
     /   /
 ---X---A
```

Updating A with the resulting merge commit will fast-forward and your push will be accepted.
Alternatively, you can rebase your change between X and B on top of A, with `git` `pull` `--rebase`, and push the result back. The rebase will create a new commit D that builds the change between X and B on top of A.
```
      B   D
     /   /
 ---X---A
```

Again, updating A with this commit will fast-forward and your push will be accepted.
There is another common situation where you may encounter non-fast-forward rejection when you try to push, and it is possible even when you are pushing into a repository nobody else pushes into. After you push commit A yourself (in the first picture in this section), replace it with `git` `commit` `--amend` to produce commit B, and you try to push it out, because forgot that you have pushed A out already. In such a case, and only if you are certain that nobody in the meantime fetched your earlier commit A (and started building on top of it), you can run `git` `push` `--force` to overwrite it. In other words, `git` `push` `--force` is a method reserved for a case where you do mean to lose history.
##  [](https://git-scm.com/docs/git-push#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpush)`git` `push` 
    
Works like `git` `push` _< remote>_, where <remote> is the current branch’s remote (or `origin`, if no remote is configured for the current branch). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushorigin)`git` `push` `origin` 
    
Without additional configuration, pushes the current branch to the configured upstream (`branch.`_< name>_`.merge` configuration variable) if it has the same name as the current branch, and errors out without pushing otherwise.
The default behavior of this command when no _< refspec>_ is given can be configured by setting the `push` option of the remote, or the `push.default` configuration variable.
For example, to default to pushing only the current branch to `origin` use `git` `config` `remote.origin.push` `HEAD`. Any valid _< refspec>_ (like the ones in the examples below) can be configured as the default for `git` `push` `origin`. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushorigin-1)`git` `push` `origin` `:` 
    
Push "matching" branches to `origin`. See _< refspec>_ in the [OPTIONS](https://git-scm.com/docs/git-push#OPTIONS) section above for a description of "matching" branches. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushoriginmaster)`git` `push` `origin` `master` 
    
Find a ref that matches `master` in the source repository (most likely, it would find `refs/heads/master`), and update the same ref (e.g. `refs/heads/master`) in `origin` repository with it. If `master` did not exist remotely, it would be created. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushoriginHEAD)`git` `push` `origin` `HEAD` 
    
A handy way to push the current branch to the same name on the remote. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushmothershipmastersatellitemasterdevsatellitedev)`git` `push` `mothership` `master:satellite/master` `dev:satellite/dev` 
    
Use the source ref that matches `master` (e.g. `refs/heads/master`) to update the ref that matches `satellite/master` (most probably `refs/remotes/satellite/master`) in the `mothership` repository; do the same for `dev` and `satellite/dev`.
See the section describing _< refspec>_... above for a discussion of the matching semantics.
This is to emulate `git` `fetch` run on the `mothership` using `git` `push` that is run in the opposite direction in order to integrate the work done on `satellite`, and is often necessary when you can only make connection in one way (i.e. satellite can ssh into mothership but mothership cannot initiate connection to satellite because the latter is behind a firewall or does not run sshd).
After running this `git` `push` on the `satellite` machine, you would ssh into the `mothership` and run `git` `merge` there to complete the emulation of `git` `pull` that were run on `mothership` to pull changes made on `satellite`. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushoriginHEADmaster)`git` `push` `origin` `HEAD:master` 
    
Push the current branch to the remote ref matching `master` in the `origin` repository. This form is convenient to push the current branch without thinking about its local name. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushoriginmasterrefsheadsexperimental)`git` `push` `origin` `master:refs/heads/experimental` 
    
Create the branch `experimental` in the `origin` repository by copying the current `master` branch. This form is only needed to create a new branch or tag in the remote repository when the local name and the remote name are different; otherwise, the ref name on its own will work. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushoriginexperimental)`git` `push` `origin` `:experimental` 
    
Find a ref that matches `experimental` in the `origin` repository (e.g. `refs/heads/experimental`), and delete it. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-gitpushorigindevmaster)`git` `push` `origin` `+dev:master` 
    
Update the origin repository’s master branch with the dev branch, allowing non-fast-forward updates. **This can leave unreferenced commits dangling in the origin repository.** Consider the following situation, where a fast-forward is not possible:
```
	    o---o---o---A---B  origin/master
		     \
		      X---Y---Z  dev
```

The above command would change the origin repository to
```
		      A---B  (unnamed branch)
		     /
	    o---o---o---X---Y---Z  master
```

Commits A and B would no longer belong to a branch with a symbolic name, and so would be unreachable. As such, these commits would be removed by a `git` `gc` command on the origin repository.
##  [](https://git-scm.com/docs/git-push#_security)SECURITY
The fetch and push protocols are not designed to prevent one side from stealing data from the other repository that was not intended to be shared. If you have private data that you need to protect from a malicious peer, your best option is to store it in another repository. This applies to both clients and servers. In particular, namespaces on a server are not effective for read access control; you should only grant read access to a namespace to clients that you would trust with read access to the entire repository.
The known attack vectors are as follows:
  1. The victim sends "have" lines advertising the IDs of objects it has that are not explicitly intended to be shared but can be used to optimize the transfer if the peer also has them. The attacker chooses an object ID X to steal and sends a ref to X, but isn’t required to send the content of X because the victim already has it. Now the victim believes that the attacker has X, and it sends the content of X back to the attacker later. (This attack is most straightforward for a client to perform on a server, by creating a ref to X in the namespace the client has access to and then fetching it. The most likely way for a server to perform it on a client is to "merge" X into a public branch and hope that the user does additional work on this branch and pushes it back to the server without noticing the merge.)
  2. As in #1, the attacker chooses an object ID X to steal. The victim sends an object Y that the attacker already has, and the attacker falsely claims to have X and not Y, so the victim sends Y as a delta against X. The delta reveals regions of X that are similar to Y to the attacker.


##  [](https://git-scm.com/docs/git-push#CONFIGURATION)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushautoSetupRemote)`push.autoSetupRemote` 
    
If set to `true` assume `--set-upstream` on default push when no upstream tracking exists for the current branch; this option takes effect with `push.default` options `simple`, `upstream`, and `current`. It is useful if by default you want new branches to be pushed to the default remote (like the behavior of `push.default=current`) and you also want the upstream tracking to be set. Workflows most likely to benefit from this option are `simple` central workflows where all branches are expected to have the same name on the remote. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushdefault)`push.default` 
    
Defines the action `git` `push` should take if no refspec is given (whether from the command-line, config, or elsewhere). Different values are well-suited for specific workflows; for instance, in a purely central workflow (i.e. the fetch source is equal to the push destination), `upstream` is probably what you want. Possible values are: 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-nothing)`nothing` 
    
do not push anything (error out) unless a refspec is given. This is primarily meant for people who want to avoid mistakes by always being explicit. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-current)`current` 
    
push the current branch to update a branch with the same name on the receiving end. Works in both central and non-central workflows. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-upstream)`upstream` 
    
push the current branch back to the branch whose changes are usually integrated into the current branch (which is called `@{upstream}`). This mode only makes sense if you are pushing to the same repository you would normally pull from (i.e. central workflow). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-tracking)`tracking` 
    
this is a deprecated synonym for `upstream`. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-simple)`simple` 
    
push the current branch with the same name on the remote.
If you are working on a centralized workflow (pushing to the same repository you pull from, which is typically `origin`), then you need to configure an upstream branch with the same name.
This mode is the default since Git 2.0, and is the safest option suited for beginners. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-matching)`matching` 
    
push all branches having the same name on both ends. This makes the repository you are pushing to remember the set of branches that will be pushed out (e.g. if you always push `maint` and `master` there and no other branches, the repository you push to will have these two branches, and your local `maint` and `master` will be pushed there).
To use this mode effectively, you have to make sure _all_ the branches you would push out are ready to be pushed out before running `git` `push`, as the whole point of this mode is to allow you to push all of the branches in one go. If you usually finish work on only one branch and push out the result, while other branches are unfinished, this mode is not for you. Also this mode is not suitable for pushing into a shared central repository, as other people may add new branches there, or update the tip of existing branches outside your control.
This used to be the default, but not since Git 2.0 (`simple` is the new default). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushfollowTags)`push.followTags` 
    
If set to true, enable `--follow-tags` option by default. You may override this configuration at time of push by specifying `--no-follow-tags`. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushgpgSign)`push.gpgSign` 
    
May be set to a boolean value, or the string `if-asked`. A true value causes all pushes to be GPG signed, as if `--signed` is passed to [git-push[1]](https://git-scm.com/docs/git-push). The string `if-asked` causes pushes to be signed if the server supports it, as if `--signed=if-asked` is passed to `git` `push`. A false value may override a value from a lower-priority config file. An explicit command-line flag always overrides this config option. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushpushOption)`push.pushOption` 
    
When no `--push-option=`_< option>_ argument is given from the command line, `git` `push` behaves as if each _< option>_ of this variable is given as `--push-option=`_< option>_.
This is a multi-valued variable, and an empty value can be used in a higher priority configuration file (e.g. `.git/config` in a repository) to clear the values inherited from a lower priority configuration files (e.g. `$HOME/.gitconfig`).
```
Example:

/etc/gitconfig
  push.pushoption = a
  push.pushoption = b

~/.gitconfig
  push.pushoption = c

repo/.git/config
  push.pushoption =
  push.pushoption = b

This will result in only b (a and c are cleared).
```


[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushrecurseSubmodules)`push.recurseSubmodules` 
    
May be `check`, `on-demand`, `only`, or `no`, with the same behavior as that of `push` `--recurse-submodules`. If not set, `no` is used by default, unless `submodule.recurse` is set (in which case a `true` value means `on-demand`). 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushuseForceIfIncludes)`push.useForceIfIncludes` 
    
If set to `true`, it is equivalent to specifying `--force-if-includes` as an option to [git-push[1]](https://git-scm.com/docs/git-push) in the command line. Adding `--no-force-if-includes` at the time of push overrides this configuration setting. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushnegotiate)`push.negotiate` 
    
If set to `true`, attempt to reduce the size of the packfile sent by rounds of negotiation in which the client and the server attempt to find commits in common. If `false`, Git will rely solely on the server’s ref advertisement to find commits in common. 

[](https://git-scm.com/docs/git-push#Documentation/git-push.txt-pushuseBitmaps)`push.useBitmaps` 
    
If set to `false`, disable use of bitmaps for `git` `push` even if `pack.useBitmaps` is `true`, without preventing other git operations from using bitmaps. Default is `true`.
##  [](https://git-scm.com/docs/git-push#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### push
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
