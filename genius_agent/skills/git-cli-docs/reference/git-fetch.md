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
    * [NAME](https://git-scm.com/docs/git-fetch#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-fetch#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-fetch#_description)
    * [OPTIONS](https://git-scm.com/docs/git-fetch#_options)
    * [GIT URLS](https://git-scm.com/docs/git-fetch#_git_urls)
    * [REMOTES](https://git-scm.com/docs/git-fetch#_remotes)
    * [UPSTREAM BRANCHES](https://git-scm.com/docs/git-fetch#UPSTREAM-BRANCHES)
    * [CONFIGURED REMOTE-TRACKING BRANCHES](https://git-scm.com/docs/git-fetch#CRTB)
    * [PRUNING](https://git-scm.com/docs/git-fetch#_pruning)
    * [OUTPUT](https://git-scm.com/docs/git-fetch#_output)
    * [EXAMPLES](https://git-scm.com/docs/git-fetch#_examples)
    * [SECURITY](https://git-scm.com/docs/git-fetch#_security)
    * [CONFIGURATION](https://git-scm.com/docs/git-fetch#_configuration)
    * [BUGS](https://git-scm.com/docs/git-fetch#_bugs)
    * [SEE ALSO](https://git-scm.com/docs/git-fetch#_see_also)
    * [GIT](https://git-scm.com/docs/git-fetch#_git)


[ English ▾](https://git-scm.com/docs/git-fetch)
Localized versions of **git-fetch** manual
  1. [English ](https://git-scm.com/docs/git-fetch)
  2. [Français ](https://git-scm.com/docs/git-fetch/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-fetch/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-fetch/sv)
  5. [українська мова ](https://git-scm.com/docs/git-fetch/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-fetch/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-fetch)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-fetch) git-fetch last updated in 2.53.0
Changes in the **git-fetch** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-fetch/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-fetch/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-fetch/2.51.1)
  5. 2.48.1 → 2.51.0 no changes
  6. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-fetch/2.48.0)
  7. 2.47.2 → 2.47.3 no changes
  8. [2.47.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-25_ ](https://git-scm.com/docs/git-fetch/2.47.1)
  9. 2.46.3 → 2.47.0 no changes
  10. [2.46.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-23_ ](https://git-scm.com/docs/git-fetch/2.46.2)
  11. 2.45.1 → 2.46.1 no changes
  12. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-fetch/2.45.0)
  13. 2.44.1 → 2.44.4 no changes
  14. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-fetch/2.44.0)
  15. 2.43.1 → 2.43.7 no changes
  16. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-fetch/2.43.0)
  17. 2.42.1 → 2.42.4 no changes
  18. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-fetch/2.42.0)
  19. 2.41.1 → 2.41.3 no changes
  20. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-fetch/2.41.0)
  21. 2.40.1 → 2.40.4 no changes
  22. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-fetch/2.40.0)
  23. 2.38.1 → 2.39.5 no changes
  24. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-fetch/2.38.0)
  25. 2.36.1 → 2.37.7 no changes
  26. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-fetch/2.36.0)
  27. 2.35.1 → 2.35.8 no changes
  28. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-fetch/2.35.0)
  29. 2.33.1 → 2.34.8 no changes
  30. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-fetch/2.33.0)
  31. 2.32.1 → 2.32.7 no changes
  32. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-fetch/2.32.0)
  33. 2.31.1 → 2.31.8 no changes
  34. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-fetch/2.31.0)
  35. 2.29.1 → 2.30.9 no changes
  36. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-fetch/2.29.0)
  37. 2.28.1 no changes
  38. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-fetch/2.28.0)
  39. 2.27.1 no changes
  40. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-fetch/2.27.0)
  41. 2.25.2 → 2.26.3 no changes
  42. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-fetch/2.25.1)
  43. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-fetch/2.25.0)
  44. 2.24.1 → 2.24.4 no changes
  45. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-fetch/2.24.0)
  46. 2.23.1 → 2.23.4 no changes
  47. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-fetch/2.23.0)
  48. 2.22.1 → 2.22.5 no changes
  49. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-fetch/2.22.0)
  50. 2.21.1 → 2.21.4 no changes
  51. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-fetch/2.21.0)
  52. 2.20.1 → 2.20.5 no changes
  53. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-fetch/2.20.0)
  54. 2.19.1 → 2.19.6 no changes
  55. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-fetch/2.19.0)
  56. 2.18.1 → 2.18.5 no changes
  57. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-fetch/2.18.0)
  58. 2.17.1 → 2.17.6 no changes
  59. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-fetch/2.17.0)
  60. 2.15.4 → 2.16.6 no changes
  61. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-fetch/2.14.6)
  62. 2.12.5 → 2.13.7 no changes
  63. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-fetch/2.11.4)
  64. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-fetch/2.10.5)
  65. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-fetch/2.9.5)
  66. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-fetch/2.8.6)
  67. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-fetch/2.7.6)
  68. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-fetch/2.6.7)
  69. 2.5.6 no changes
  70. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-fetch/2.4.12)
  71. 2.2.3 → 2.3.10 no changes
  72. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-fetch/2.1.4)
  73. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-fetch/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-fetch#_name)NAME
git-fetch - Download objects and refs from another repository
##  [](https://git-scm.com/docs/git-fetch#_synopsis)SYNOPSIS
```
git fetch [_<options>_] [_<repository>_ [_<refspec>_…​]]
git fetch [_<options>_] _<group>_
git fetch --multiple [_<options>_] [(_<repository>_|_<group>_)…​]
git fetch --all [_<options>_]
```

##  [](https://git-scm.com/docs/git-fetch#_description)DESCRIPTION
Fetch branches and/or tags (collectively, "refs") from one or more other repositories, along with the objects necessary to complete their histories. Remote-tracking branches are updated (see the description of _< refspec>_ below for ways to control this behavior).
By default, any tag that points into the histories being fetched is also fetched; the effect is to fetch tags that point at branches that you are interested in. This default behavior can be changed by using the `--tags` or `--no-tags` options or by configuring `remote.`_< name>_`.tagOpt`. By using a refspec that fetches tags explicitly, you can fetch tags that do not point into branches you are interested in as well.
`git` `fetch` can fetch from either a single named repository or URL, or from several repositories at once if _< group>_ is given and there is a `remotes.`_< group>_ entry in the configuration file. (See [git-config[1]](https://git-scm.com/docs/git-config)).
When no remote is specified, by default the `origin` remote will be used, unless there’s an upstream branch configured for the current branch.
The names of refs that are fetched, together with the object names they point at, are written to `.git/FETCH_HEAD`. This information may be used by scripts or other git commands, such as [git-pull[1]](https://git-scm.com/docs/git-pull).
##  [](https://git-scm.com/docs/git-fetch#_options)OPTIONS 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---all)`--all` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-all)`--no-all` 
    
Fetch all remotes, except for the ones that has the `remote.`_< name>_`.skipFetchAll` configuration variable set. This overrides the configuration variable `fetch.all`. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--a)`-a` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---append)`--append` 
    
Append ref names and object names of fetched refs to the existing contents of `.git/FETCH_HEAD`. Without this option old data in `.git/FETCH_HEAD` will be overwritten. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---atomic)`--atomic` 
    
Use an atomic transaction to update local refs. Either all refs are updated, or on error, no refs are updated. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---depthdepth)`--depth=`_< depth>_ 
    
Limit fetching to the specified number of commits from the tip of each remote branch history. If fetching to a _shallow_ repository created by `git` `clone` with `--depth=`_< depth>_ option (see [git-clone[1]](https://git-scm.com/docs/git-clone)), deepen or shorten the history to the specified number of commits. Tags for the deepened commits are not fetched. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---deependepth)`--deepen=`_< depth>_ 
    
Similar to `--depth`, except it specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---shallow-sincedate)`--shallow-since=`_< date>_ 
    
Deepen or shorten the history of a shallow repository to include all reachable commits after _< date>_. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---shallow-excluderef)`--shallow-exclude=`_< ref>_ 
    
Deepen or shorten the history of a shallow repository to exclude commits reachable from a specified remote branch or tag. This option can be specified multiple times. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---unshallow)`--unshallow` 
    
If the source repository is complete, convert a shallow repository to a complete one, removing all the limitations imposed by shallow repositories.
If the source repository is shallow, fetch as much as possible so that the current repository has the same history as the source repository. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---update-shallow)`--update-shallow` 
    
By default when fetching from a shallow repository, `git` `fetch` refuses refs that require updating `.git/shallow`. This option updates `.git/shallow` and accepts such refs. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---negotiation-tipcommitglob)`--negotiation-tip=`(_< commit>_|_< glob>_) 
    
By default, Git will report, to the server, commits reachable from all local refs to find common commits in an attempt to reduce the size of the to-be-received packfile. If specified, Git will only report commits reachable from the given tips. This is useful to speed up fetches when the user knows which local ref is likely to have commits in common with the upstream ref being fetched.
This option may be specified more than once; if so, Git will report commits reachable from any of the given commits.
The argument to this option may be a glob on ref names, a ref, or the (possibly abbreviated) SHA-1 of a commit. Specifying a glob is equivalent to specifying this option multiple times, one for each matching ref name.
See also the `fetch.negotiationAlgorithm` and `push.negotiate` configuration variables documented in [git-config[1]](https://git-scm.com/docs/git-config), and the `--negotiate-only` option below. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---negotiate-only)`--negotiate-only` 
    
Do not fetch anything from the server, and instead print the ancestors of the provided `--negotiation-tip=` arguments, which we have in common with the server.
This is incompatible with `--recurse-submodules=`(`yes`|`on-demand`). Internally this is used to implement the `push.negotiate` option, see [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---dry-run)`--dry-run` 
    
Show what would be done, without making any changes. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---porcelain)`--porcelain` 
    
Print the output to standard output in an easy-to-parse format for scripts. See section OUTPUT in [git-fetch[1]](https://git-scm.com/docs/git-fetch) for details.
This is incompatible with `--recurse-submodules=`(`yes`|`on-demand`) and takes precedence over the `fetch.output` config option. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---write-fetch-head)`--write-fetch-head` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-write-fetch-head)`--no-write-fetch-head` 
    
Write the list of remote refs fetched in the `FETCH_HEAD` file directly under `$GIT_DIR`. This is the default. Passing `--no-write-fetch-head` from the command line tells Git not to write the file. Under `--dry-run` option, the file is never written. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--f)`-f` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---force)`--force` 
    
When `git` `fetch` is used with _< src>_`:`_< dst>_ refspec, it may refuse to update the local branch as discussed in the _< refspec>_ part below. This option overrides that check. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--k)`-k` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---keep)`--keep` 
    
Keep downloaded pack. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---multiple)`--multiple` 
    
Allow several _< repository>_ and _< group>_ arguments to be specified. No _< refspec>_s may be specified. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---auto-maintenance)`--auto-maintenance` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-auto-maintenance)`--no-auto-maintenance` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---auto-gc)`--auto-gc` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-auto-gc)`--no-auto-gc` 
    
Run `git` `maintenance` `run` `--auto` at the end to perform automatic repository maintenance if needed. This is enabled by default. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---write-commit-graph)`--write-commit-graph` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-write-commit-graph)`--no-write-commit-graph` 
    
Write a commit-graph after fetching. This overrides the config setting `fetch.writeCommitGraph`. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---prefetch)`--prefetch` 
    
Modify the configured refspec to place all refs into the `refs/prefetch/` namespace. See the `prefetch` task in [git-maintenance[1]](https://git-scm.com/docs/git-maintenance). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--p)`-p` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---prune)`--prune` 
    
Before fetching, remove any remote-tracking references that no longer exist on the remote. Tags are not subject to pruning if they are fetched only because of the default tag auto-following or due to a `--tags` option. However, if tags are fetched due to an explicit refspec (either on the command line or in the remote configuration, for example if the remote was cloned with the `--mirror` option), then they are also subject to pruning. Supplying `--prune-tags` is a shorthand for providing the tag refspec.
See the PRUNING section below for more details. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--P)`-P` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---prune-tags)`--prune-tags` 
    
Before fetching, remove any local tags that no longer exist on the remote if `--prune` is enabled. This option should be used more carefully, unlike `--prune` it will remove any local references (local tags) that have been created. This option is a shorthand for providing the explicit tag refspec along with `--prune`, see the discussion about that in its documentation.
See the PRUNING section below for more details. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--n)`-n` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-tags)`--no-tags` 
    
By default, tags that point at objects that are downloaded from the remote repository are fetched and stored locally. This option disables this automatic tag following. The default behavior for a remote may be specified with the `remote.`_< name>_`.tagOpt` setting. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---refetch)`--refetch` 
    
Instead of negotiating with the server to avoid transferring commits and associated objects that are already present locally, this option fetches all objects as a fresh clone would. Use this to reapply a partial clone filter from configuration or using `--filter=` when the filter definition has changed. Automatic post-fetch maintenance will perform object database pack consolidation to remove any duplicate objects. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---refmaprefspec)`--refmap=`_< refspec>_ 
    
When fetching refs listed on the command line, use the specified refspec (can be given more than once) to map the refs to remote-tracking branches, instead of the values of `remote.`_< name>_`.fetch` configuration variables for the remote repository. Providing an empty _< refspec>_ to the `--refmap` option causes Git to ignore the configured refspecs and rely entirely on the refspecs supplied as command-line arguments. See section on "Configured Remote-tracking Branches" for details. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--t)`-t` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---tags)`--tags` 
    
Fetch all tags from the remote (i.e., fetch remote tags `refs/tags/*` into local tags with the same name), in addition to whatever else would otherwise be fetched. Using this option alone does not subject tags to pruning, even if `--prune` is used (though tags may be pruned anyway if they are also the destination of an explicit refspec; see `--prune`). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---recurse-submodulesyeson-demandno)`--recurse-submodules`[`=`(`yes`|`on-demand`|`no`)] 
    
Control if and under what conditions new commits of submodules should be fetched too. When recursing through submodules, `git` `fetch` always attempts to fetch "changed" submodules, that is, a submodule that has commits that are referenced by a newly fetched superproject commit but are missing in the local submodule clone. A changed submodule can be fetched as long as it is present locally e.g. in `$GIT_DIR/modules/` (see [gitsubmodules[7]](https://git-scm.com/docs/gitsubmodules)); if the upstream adds a new submodule, that submodule cannot be fetched until it is cloned e.g. by `git` `submodule` `update`.
When set to `on-demand`, only changed submodules are fetched. When set to `yes`, all populated submodules are fetched and submodules that are both unpopulated and changed are fetched. When set to `no`, submodules are never fetched.
When unspecified, this uses the value of `fetch.recurseSubmodules` if it is set (see [git-config[1]](https://git-scm.com/docs/git-config)), defaulting to `on-demand` if unset. When this option is used without any value, it defaults to `yes`. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--jn)`-j` _< n>_ 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---jobsn)`--jobs=`_< n>_ 
    
Parallelize all forms of fetching up to _< n>_ jobs at a time.
If the `--multiple` option was specified, the different remotes will be fetched in parallel. If multiple submodules are fetched, they will be fetched in parallel. To control them independently, use the config settings `fetch.parallel` and `submodule.fetchJobs` (see [git-config[1]](https://git-scm.com/docs/git-config)).
Typically, parallel recursive and multi-remote fetches will be faster. By default fetches are performed sequentially, not in parallel. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-recurse-submodules)`--no-recurse-submodules` 
    
Disable recursive fetching of submodules (this has the same effect as using the `--recurse-submodules=no` option). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---set-upstream)`--set-upstream` 
    
If the remote is fetched successfully, add upstream (tracking) reference, used by argument-less [git-pull[1]](https://git-scm.com/docs/git-pull) and other commands. For more information, see `branch.`_< name>_`.merge` and `branch.`_< name>_`.remote` in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---submodule-prefixpath)`--submodule-prefix=`_< path>_ 
    
Prepend _< path>_ to paths printed in informative messages such as "Fetching submodule foo". This option is used internally when recursing over submodules. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---recurse-submodules-defaultyeson-demand)`--recurse-submodules-default=`(`yes`|`on-demand`) 
    
This option is used internally to temporarily provide a non-negative default value for the `--recurse-submodules` option. All other methods of configuring fetch’s submodule recursion (such as settings in [gitmodules[5]](https://git-scm.com/docs/gitmodules) and [git-config[1]](https://git-scm.com/docs/git-config)) override this option, as does specifying `--`[`no-`]`recurse-submodules` directly. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--u)`-u` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---update-head-ok)`--update-head-ok` 
    
By default `git` `fetch` refuses to update the head which corresponds to the current branch. This flag disables the check. This is purely for the internal use for `git` `pull` to communicate with `git` `fetch`, and unless you are implementing your own Porcelain you are not supposed to use it. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---upload-packupload-pack)`--upload-pack` _< upload-pack>_ 
    
When given, and the repository to fetch from is handled by `git` `fetch-pack`, `--exec=`_< upload-pack>_ is passed to the command to specify non-default path for the command run on the other end. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--q)`-q` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---quiet)`--quiet` 
    
Pass `--quiet` to `git-fetch-pack` and silence any other internally used git commands. Progress is not reported to the standard error stream. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--v)`-v` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---verbose)`--verbose` 
    
Be verbose. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---progress)`--progress` 
    
Progress status is reported on the standard error stream by default when it is attached to a terminal, unless `-q` is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--ooption)`-o` _< option>_ 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---server-optionoption)`--server-option=`_< option>_ 
    
Transmit the given string to the server when communicating using protocol version 2. The given string must not contain a _NUL_ or _LF_ character. The server’s handling of server options, including unknown ones, is server-specific. When multiple `--server-option=`_< option>_ are given, they are all sent to the other side in the order listed on the command line. When no `--server-option=`_< option>_ is given from the command line, the values of configuration variable `remote.`_< name>_`.serverOption` are used instead. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---show-forced-updates)`--show-forced-updates` 
    
By default, git checks if a branch is force-updated during fetch. This can be disabled through `fetch.showForcedUpdates`, but the `--show-forced-updates` option guarantees this check occurs. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---no-show-forced-updates)`--no-show-forced-updates` 
    
By default, git checks if a branch is force-updated during fetch. Pass `--no-show-forced-updates` or set `fetch.showForcedUpdates` to false to skip this check for performance reasons. If used during `git-pull` the `--ff-only` option will still check for forced updates before attempting a fast-forward update. See [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--4)`-4` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---ipv4)`--ipv4` 
    
Use IPv4 addresses only, ignoring IPv6 addresses. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--6)`-6` 


[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---ipv6)`--ipv6` 
    
Use IPv6 addresses only, ignoring IPv4 addresses. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-repository)_< repository>_ 
    
The "remote" repository that is the source of a fetch or pull operation. This parameter can be either a URL (see the section [GIT URLS](https://git-scm.com/docs/git-fetch#URLS) below) or the name of a remote (see the section [REMOTES](https://git-scm.com/docs/git-fetch#REMOTES) below). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-group)_< group>_ 
    
A name referring to a list of repositories as the value of `remotes.`_< group>_ in the configuration file. (See [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-refspec)_< refspec>_ 
    
Specifies which refs to fetch and which local refs to update. When no _< refspec>_s appear on the command line, the refs to fetch are read from `remote.`_< repository>_`.fetch` variables instead (see [CONFIGURED REMOTE-TRACKING BRANCHES](https://git-scm.com/docs/git-fetch#CRTB) below).
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

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---stdin)`--stdin` 
      
Read refspecs, one per line, from stdin in addition to those provided as arguments. The "tag _< name>_" format is not supported.
##  [](https://git-scm.com/docs/git-fetch#_git_urls)GIT URLS
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
##  [](https://git-scm.com/docs/git-fetch#_remotes)REMOTES
The name of one of the following can be used instead of a URL as _< repository>_ argument:
  * a remote in the Git configuration file: `$GIT_DIR/config`,
  * a file in the `$GIT_DIR/remotes` directory, or
  * a file in the `$GIT_DIR/branches` directory.


All of these also allow you to omit the refspec from the command line because they each contain a refspec which git will use by default.
###  [](https://git-scm.com/docs/git-fetch#_named_remote_in_configuration_file)Named remote in configuration file
You can choose to provide the name of a remote which you had previously configured using [git-remote[1]](https://git-scm.com/docs/git-remote), [git-config[1]](https://git-scm.com/docs/git-config) or even by a manual edit to the `$GIT_DIR/config` file. The URL of this remote will be used to access the repository. The refspec of this remote will be used by default when you do not provide a refspec on the command line. The entry in the config file would appear like this:
```
	[remote "<name>"]
		url = <URL>
		pushurl = <pushurl>
		push = <refspec>
		fetch = <refspec>
```

The _< pushurl>_ is used for pushes only. It is optional and defaults to _< URL>_. Pushing to a remote affects all defined pushurls or all defined urls if no pushurls are defined. Fetch, however, will only fetch from the first defined url if multiple urls are defined.
###  [](https://git-scm.com/docs/git-fetch#_named_file_in_git_dirremotes)Named file in `$GIT_DIR/remotes`
You can choose to provide the name of a file in `$GIT_DIR/remotes`. The URL in this file will be used to access the repository. The refspec in this file will be used as default when you do not provide a refspec on the command line. This file should have the following format:
```
	URL: one of the above URL formats
	Push: <refspec>
	Pull: <refspec>
```

`Push:` lines are used by `git` `push` and `Pull:` lines are used by `git` `pull` and `git` `fetch`. Multiple `Push:` and `Pull:` lines may be specified for additional branch mappings.
###  [](https://git-scm.com/docs/git-fetch#_named_file_in_git_dirbranches)Named file in `$GIT_DIR/branches`
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

##  [](https://git-scm.com/docs/git-fetch#UPSTREAM-BRANCHES)UPSTREAM BRANCHES
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
##  [](https://git-scm.com/docs/git-fetch#CRTB)CONFIGURED REMOTE-TRACKING BRANCHES
You often interact with the same remote repository by regularly and repeatedly fetching from it. In order to keep track of the progress of such a remote repository, `git` `fetch` allows you to configure `remote.`_< repository>_`.fetch` configuration variables.
Typically such a variable may look like this:
```
[remote "origin"]
	fetch = +refs/heads/*:refs/remotes/origin/*
```

This configuration is used in two ways:
  * When `git` `fetch` is run without specifying what branches and/or tags to fetch on the command line, e.g. `git` `fetch` `origin` or `git` `fetch`, `remote.`_< repository>_`.fetch` values are used as the refspecs—​they specify which refs to fetch and which local refs to update. The example above will fetch all branches that exist in the `origin` (i.e. any ref that matches the left-hand side of the value, `refs/heads/*`) and update the corresponding remote-tracking branches in the `refs/remotes/origin/*` hierarchy.
  * When `git` `fetch` is run with explicit branches and/or tags to fetch on the command line, e.g. `git` `fetch` `origin` `master`, the _< refspec>s_ given on the command line determine what are to be fetched (e.g. `master` in the example, which is a short-hand for `master:`, which in turn means "fetch the `master` branch but I do not explicitly say what remote-tracking branch to update with it from the command line"), and the example command will fetch _only_ the `master` branch. The `remote.`_< repository>_`.fetch` values determine which remote-tracking branch, if any, is updated. When used in this way, the `remote.`_< repository>_`.fetch` values do not have any effect in deciding _what_ gets fetched (i.e. the values are not used as refspecs when the command-line lists refspecs); they are only used to decide _where_ the refs that are fetched are stored by acting as a mapping.


The latter use of the `remote.`_< repository>_`.fetch` values can be overridden by giving the `--refmap=`_< refspec>_ parameter(s) on the command line.
##  [](https://git-scm.com/docs/git-fetch#_pruning)PRUNING
Git has a default disposition of keeping data unless it’s explicitly thrown away; this extends to holding onto local references to branches on remotes that have themselves deleted those branches.
If left to accumulate, these stale references might make performance worse on big and busy repos that have a lot of branch churn, and e.g. make the output of commands like `git` `branch` `-a` `--contains` _< commit>_ needlessly verbose, as well as impacting anything else that’ll work with the complete set of known references.
These remote-tracking references can be deleted as a one-off with either of:
```
# While fetching
$ git fetch --prune <name>

# Only prune, don't fetch
$ git remote prune <name>
```

To prune references as part of your normal workflow without needing to remember to run that, set `fetch.prune` globally, or `remote.`_< name>_`.prune` per-remote in the config. See [git-config[1]](https://git-scm.com/docs/git-config).
Here’s where things get tricky and more specific. The pruning feature doesn’t actually care about branches, instead it’ll prune local ←→ remote-references as a function of the refspec of the remote (see _< refspec>_ and [CONFIGURED REMOTE-TRACKING BRANCHES](https://git-scm.com/docs/git-fetch#CRTB) above).
Therefore if the refspec for the remote includes e.g. `refs/tags/*:refs/tags/*`, or you manually run e.g. `git` `fetch` `--prune` _< name>_ `"refs/tags/*:refs/tags/*"` it won’t be stale remote tracking branches that are deleted, but any local tag that doesn’t exist on the remote.
This might not be what you expect, i.e. you want to prune remote _< name>_, but also explicitly fetch tags from it, so when you fetch from it you delete all your local tags, most of which may not have come from the _< name>_ remote in the first place.
So be careful when using this with a refspec like `refs/tags/*:refs/tags/*`, or any other refspec which might map references from multiple remotes to the same local namespace.
Since keeping up-to-date with both branches and tags on the remote is a common use-case the `--prune-tags` option can be supplied along with `--prune` to prune local tags that don’t exist on the remote, and force-update those tags that differ. Tag pruning can also be enabled with `fetch.pruneTags` or `remote.`_< name>_`.pruneTags` in the config. See [git-config[1]](https://git-scm.com/docs/git-config).
The `--prune-tags` option is equivalent to having `refs/tags/*:refs/tags/*` declared in the refspecs of the remote. This can lead to some seemingly strange interactions:
```
# These both fetch tags
$ git fetch --no-tags origin 'refs/tags/*:refs/tags/*'
$ git fetch --no-tags --prune-tags origin
```

The reason it doesn’t error out when provided without `--prune` or its config versions is for flexibility of the configured versions, and to maintain a 1=1 mapping between what the command line flags do, and what the configuration versions do.
It’s reasonable to e.g. configure `fetch.pruneTags=true` in `~/.gitconfig` to have tags pruned whenever `git` `fetch` `--prune` is run, without making every invocation of `git` `fetch` without `--prune` an error.
Pruning tags with `--prune-tags` also works when fetching a URL instead of a named remote. These will all prune tags not found on origin:
```
$ git fetch origin --prune --prune-tags
$ git fetch origin --prune 'refs/tags/*:refs/tags/*'
$ git fetch <url-of-origin> --prune --prune-tags
$ git fetch <url-of-origin> --prune 'refs/tags/*:refs/tags/*'
```

##  [](https://git-scm.com/docs/git-fetch#_output)OUTPUT
The output of "git fetch" depends on the transport method used; this section describes the output when fetching over the Git protocol (either locally or via ssh) and Smart HTTP protocol.
The status of the fetch is output in tabular form, with each line representing the status of a single ref. Each line is of the form:
```
 <flag> <summary> <from> -> <to> [<reason>]
```

When using `--porcelain`, the output format is intended to be machine-parseable. In contrast to the human-readable output formats it thus prints to standard output instead of standard error. Each line is of the form:
```
<flag> <old-object-id> <new-object-id> <local-reference>
```

The status of up-to-date refs is shown only if the `--verbose` option is used.
In compact output mode, specified with configuration variable fetch.output, if either entire _< from>_ or _< to>_ is found in the other string, it will be substituted with `*` in the other string. For example, _master - > origin/master_ becomes _master - > origin/*_. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-flag)flag 
    
A single character indicating the status of the ref: 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-space)(space) 
    
for a successfully fetched fast-forward; 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-)`+` 
    
for a successful forced update; 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--)`-` 
    
for a successfully pruned ref; 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-t)`t` 
    
for a successful tag update; 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--1)`*` 
    
for a successfully fetched new ref; 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--1-1)`!` 
    
for a ref that was rejected or failed to update; and 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt--1-1-1)`=` 
    
for a ref that was up to date and did not need fetching. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-summary)summary 
    
For a successfully fetched ref, the summary shows the old and new values of the ref in a form suitable for using as an argument to `git` `log` (this is _< old>_`..`_< new>_ in most cases, and _< old>_`...`_< new>_ for forced non-fast-forward updates). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-from)from 
    
The name of the remote ref being fetched from, minus its `refs/`_< type>_`/` prefix. In the case of deletion, the name of the remote ref is "(none)". 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-to)to 
    
The name of the local ref being updated, minus its `refs/`_< type>_`/` prefix. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-reason)reason 
    
A human-readable explanation. In the case of successfully fetched refs, no explanation is needed. For a failed ref, the reason for failure is described.
##  [](https://git-scm.com/docs/git-fetch#_examples)EXAMPLES
  * Update the remote-tracking branches:
```
$ git fetch origin
```

The above command copies all branches from the remote `refs/heads/` namespace and stores them to the local `refs/remotes/origin/` namespace, unless the `remote.`_< repository>_`.fetch` option is used to specify a non-default refspec.
  * Using refspecs explicitly:
```
$ git fetch origin +seen:seen maint:tmp
```

This updates (or creates, as necessary) branches `seen` and `tmp` in the local repository by fetching from the branches (respectively) `seen` and `maint` from the remote repository.
The `seen` branch will be updated even if it does not fast-forward, because it is prefixed with a plus sign; `tmp` will not be.
  * Peek at a remote’s branch, without configuring the remote in your local repository:
```
$ git fetch git://git.kernel.org/pub/scm/git/git.git maint
$ git log FETCH_HEAD
```

The first command fetches the `maint` branch from the repository at `git://git.kernel.org/pub/scm/git/git.git` and the second command uses `FETCH_HEAD` to examine the branch with [git-log[1]](https://git-scm.com/docs/git-log). The fetched objects will eventually be removed by git’s built-in housekeeping (see [git-gc[1]](https://git-scm.com/docs/git-gc)).


##  [](https://git-scm.com/docs/git-fetch#_security)SECURITY
The fetch and push protocols are not designed to prevent one side from stealing data from the other repository that was not intended to be shared. If you have private data that you need to protect from a malicious peer, your best option is to store it in another repository. This applies to both clients and servers. In particular, namespaces on a server are not effective for read access control; you should only grant read access to a namespace to clients that you would trust with read access to the entire repository.
The known attack vectors are as follows:
  1. The victim sends "have" lines advertising the IDs of objects it has that are not explicitly intended to be shared but can be used to optimize the transfer if the peer also has them. The attacker chooses an object ID X to steal and sends a ref to X, but isn’t required to send the content of X because the victim already has it. Now the victim believes that the attacker has X, and it sends the content of X back to the attacker later. (This attack is most straightforward for a client to perform on a server, by creating a ref to X in the namespace the client has access to and then fetching it. The most likely way for a server to perform it on a client is to "merge" X into a public branch and hope that the user does additional work on this branch and pushes it back to the server without noticing the merge.)
  2. As in #1, the attacker chooses an object ID X to steal. The victim sends an object Y that the attacker already has, and the attacker falsely claims to have X and not Y, so the victim sends Y as a delta against X. The delta reveals regions of X that are similar to Y to the attacker.


##  [](https://git-scm.com/docs/git-fetch#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchrecurseSubmodules)`fetch.recurseSubmodules` 
    
This option controls whether `git` `fetch` (and the underlying fetch in `git` `pull`) will recursively fetch into populated submodules. This option can be set either to a boolean value or to `on-demand`. Setting it to a boolean changes the behavior of fetch and pull to recurse unconditionally into submodules when set to true or to not recurse at all when set to false. When set to `on-demand`, fetch and pull will only recurse into a populated submodule when its superproject retrieves a commit that updates the submodule’s reference. Defaults to `on-demand`, or to the value of `submodule.recurse` if set. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchfsckObjects)`fetch.fsckObjects` 
    
If it is set to true, git-fetch-pack will check all fetched objects. See `transfer.fsckObjects` for what’s checked. Defaults to `false`. If not set, the value of `transfer.fsckObjects` is used instead. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchfsckmsg-id)`fetch.fsck.`_< msg-id>_ 
    
Acts like `fsck.`_< msg-id>_, but is used by [git-fetch-pack[1]](https://git-scm.com/docs/git-fetch-pack) instead of [git-fsck[1]](https://git-scm.com/docs/git-fsck). See the `fsck.`_< msg-id>_ documentation for details. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchfsckskipList)`fetch.fsck.skipList` 
    
Acts like `fsck.skipList`, but is used by [git-fetch-pack[1]](https://git-scm.com/docs/git-fetch-pack) instead of [git-fsck[1]](https://git-scm.com/docs/git-fsck). See the `fsck.skipList` documentation for details. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchunpackLimit)`fetch.unpackLimit` 
    
If the number of objects fetched over the Git native transfer is below this limit, then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchprune)`fetch.prune` 
    
If true, fetch will automatically behave as if the `--prune` option was given on the command line. See also `remote.`_< name>_`.prune` and the PRUNING section of [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchpruneTags)`fetch.pruneTags` 
    
If true, fetch will automatically behave as if the `refs/tags/*:refs/tags/*` refspec was provided when pruning, if not set already. This allows for setting both this option and `fetch.prune` to maintain a 1=1 mapping to upstream refs. See also `remote.`_< name>_`.pruneTags` and the PRUNING section of [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchall)`fetch.all` 
    
If true, fetch will attempt to update all available remotes. This behavior can be overridden by passing `--no-all` or by explicitly specifying one or more remote(s) to fetch from. Defaults to `false`. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchoutput)`fetch.output` 
    
Control how ref update status is printed. Valid values are `full` and `compact`. Default value is `full`. See the OUTPUT section in [git-fetch[1]](https://git-scm.com/docs/git-fetch) for details. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchnegotiationAlgorithm)`fetch.negotiationAlgorithm` 
    
Control how information about the commits in the local repository is sent when negotiating the contents of the packfile to be sent by the server. Set to `consecutive` to use an algorithm that walks over consecutive commits checking each one. Set to `skipping` to use an algorithm that skips commits in an effort to converge faster, but may result in a larger-than-necessary packfile; or set to `noop` to not send any information at all, which will almost certainly result in a larger-than-necessary packfile, but will skip the negotiation step. Set to `default` to override settings made previously and use the default behaviour. The default is normally `consecutive`, but if `feature.experimental` is `true`, then the default is `skipping`. Unknown values will cause `git` `fetch` to error out.
See also the `--negotiate-only` and `--negotiation-tip` options to [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchshowForcedUpdates)`fetch.showForcedUpdates` 
    
Set to `false` to enable `--no-show-forced-updates` in [git-fetch[1]](https://git-scm.com/docs/git-fetch) and [git-pull[1]](https://git-scm.com/docs/git-pull) commands. Defaults to `true`. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchparallel)`fetch.parallel` 
    
Specifies the maximal number of fetch operations to be run in parallel at a time (submodules, or remotes when the `--multiple` option of [git-fetch[1]](https://git-scm.com/docs/git-fetch) is in effect).
A value of 0 will give some reasonable default. If unset, it defaults to 1.
For submodules, this setting can be overridden using the `submodule.fetchJobs` config setting. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchwriteCommitGraph)`fetch.writeCommitGraph` 
    
Set to true to write a commit-graph after every `git` `fetch` command that downloads a pack-file from a remote. Using the `--split` option, most executions will create a very small commit-graph file on top of the existing commit-graph file(s). Occasionally, these files will merge and the write may take longer. Having an updated commit-graph file helps performance of many Git commands, including `git` `merge-base`, `git` `push` `-f`, and `git` `log` `--graph`. Defaults to `false`. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchbundleURI)`fetch.bundleURI` 
    
This value stores a URI for downloading Git object data from a bundle URI before performing an incremental fetch from the origin Git server. This is similar to how the `--bundle-uri` option behaves in [git-clone[1]](https://git-scm.com/docs/git-clone). `git` `clone` `--bundle-uri` will set the `fetch.bundleURI` value if the supplied bundle URI contains a bundle list that is organized for incremental fetches.
If you modify this value and your repository has a `fetch.bundleCreationToken` value, then remove that `fetch.bundleCreationToken` value before fetching from the new bundle URI. 

[](https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt-fetchbundleCreationToken)`fetch.bundleCreationToken` 
    
When using `fetch.bundleURI` to fetch incrementally from a bundle list that uses the "`creationToken`" heuristic, this config value stores the maximum `creationToken` value of the downloaded bundles. This value is used to prevent downloading bundles in the future if the advertised `creationToken` is not strictly larger than this value.
The creation token values are chosen by the provider serving the specific bundle URI. If you modify the URI at `fetch.bundleURI`, then be sure to remove the value for the `fetch.bundleCreationToken` value before fetching.
##  [](https://git-scm.com/docs/git-fetch#_bugs)BUGS
Using `--recurse-submodules` can only fetch new commits in submodules that are present locally e.g. in `$GIT_DIR/modules/`. If the upstream adds a new submodule, that submodule cannot be fetched until it is cloned e.g. by `git` `submodule` `update`. This is expected to be fixed in a future Git version.
##  [](https://git-scm.com/docs/git-fetch#_see_also)SEE ALSO
[git-pull[1]](https://git-scm.com/docs/git-pull)
##  [](https://git-scm.com/docs/git-fetch#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### fetch
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
