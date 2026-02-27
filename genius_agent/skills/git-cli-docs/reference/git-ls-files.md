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
    * [NAME](https://git-scm.com/docs/git-ls-files#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-ls-files#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-ls-files#_description)
    * [OPTIONS](https://git-scm.com/docs/git-ls-files#_options)
    * [OUTPUT](https://git-scm.com/docs/git-ls-files#_output)
    * [FIELD NAMES](https://git-scm.com/docs/git-ls-files#_field_names)
    * [EXCLUDE PATTERNS](https://git-scm.com/docs/git-ls-files#_exclude_patterns)
    * [SEE ALSO](https://git-scm.com/docs/git-ls-files#_see_also)
    * [GIT](https://git-scm.com/docs/git-ls-files#_git)


[ English ▾](https://git-scm.com/docs/git-ls-files)
Localized versions of **git-ls-files** manual
  1. [English ](https://git-scm.com/docs/git-ls-files)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-ls-files/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-ls-files/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-ls-files/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-ls-files)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-ls-files) git-ls-files last updated in 2.46.1
Changes in the **git-ls-files** manual
  1. 2.46.2 → 2.53.0 no changes
  2. [2.46.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-13_ ](https://git-scm.com/docs/git-ls-files/2.46.1)
  3. 2.44.1 → 2.46.0 no changes
  4. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-ls-files/2.44.0)
  5. 2.43.1 → 2.43.7 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-ls-files/2.43.0)
  7. 2.42.1 → 2.42.4 no changes
  8. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-ls-files/2.42.0)
  9. 2.40.1 → 2.41.3 no changes
  10. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-ls-files/2.40.0)
  11. 2.39.1 → 2.39.5 no changes
  12. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-ls-files/2.39.0)
  13. 2.38.1 → 2.38.5 no changes
  14. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-ls-files/2.38.0)
  15. 2.36.1 → 2.37.7 no changes
  16. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-ls-files/2.36.0)
  17. 2.35.1 → 2.35.8 no changes
  18. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-ls-files/2.35.0)
  19. 2.31.1 → 2.34.8 no changes
  20. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-ls-files/2.31.0)
  21. 2.30.2 → 2.30.9 no changes
  22. [2.30.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-02-08_ ](https://git-scm.com/docs/git-ls-files/2.30.1)
  23. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-ls-files/2.30.0)
  24. 2.27.1 → 2.29.3 no changes
  25. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-ls-files/2.27.0)
  26. 2.22.1 → 2.26.3 no changes
  27. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-ls-files/2.22.0)
  28. 2.18.1 → 2.21.4 no changes
  29. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-ls-files/2.18.0)
  30. 2.17.0 → 2.17.6 no changes
  31. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-ls-files/2.16.6)
  32. 2.14.6 → 2.15.4 no changes
  33. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-ls-files/2.13.7)
  34. 2.12.5 no changes
  35. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-ls-files/2.11.4)
  36. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-ls-files/2.10.5)
  37. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-ls-files/2.9.5)
  38. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-ls-files/2.8.6)
  39. 2.2.3 → 2.7.6 no changes
  40. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-ls-files/2.1.4)
  41. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-ls-files/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-ls-files#_name)NAME
git-ls-files - Show information about files in the index and the working tree
##  [](https://git-scm.com/docs/git-ls-files#_synopsis)SYNOPSIS
```
_git ls-files_ [-z] [-t] [-v] [-f]
		[-c|--cached] [-d|--deleted] [-o|--others] [-i|--ignored]
		[-s|--stage] [-u|--unmerged] [-k|--killed] [-m|--modified]
		[--resolve-undo]
		[--directory [--no-empty-directory]] [--eol]
		[--deduplicate]
		[-x <pattern>|--exclude=<pattern>]
		[-X <file>|--exclude-from=<file>]
		[--exclude-per-directory=<file>]
		[--exclude-standard]
		[--error-unmatch] [--with-tree=<tree-ish>]
		[--full-name] [--recurse-submodules]
		[--abbrev[=<n>]] [--format=<format>] [--] [<file>…​]
```

##  [](https://git-scm.com/docs/git-ls-files#_description)DESCRIPTION
This command merges the file listing in the index with the actual working directory list, and shows different combinations of the two.
Several flags can be used to determine which files are shown, and each file may be printed multiple times if there are multiple entries in the index or if multiple statuses are applicable for the relevant file selection options.
##  [](https://git-scm.com/docs/git-ls-files#_options)OPTIONS 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--c)-c 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---cached)--cached 
    
Show all files cached in Git’s index, i.e. all tracked files. (This is the default if no -c/-s/-d/-o/-u/-k/-m/--resolve-undo options are specified.) 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--d)-d 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---deleted)--deleted 
    
Show files with an unstaged deletion 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--m)-m 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---modified)--modified 
    
Show files with an unstaged modification (note that an unstaged deletion also counts as an unstaged modification) 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--o)-o 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---others)--others 
    
Show other (i.e. untracked) files in the output 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--i)-i 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---ignored)--ignored 
    
Show only ignored files in the output. Must be used with either an explicit _-c_ or _-o_. When showing files in the index (i.e. when used with _-c_), print only those files matching an exclude pattern. When showing "other" files (i.e. when used with _-o_), show only those matched by an exclude pattern. Standard ignore rules are not automatically activated; therefore, at least one of the `--exclude*` options is required. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--s)-s 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---stage)--stage 
    
Show staged contents' mode bits, object name and stage number in the output. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---directory)--directory 
    
If a whole directory is classified as "other", show just its name (with a trailing slash) and not its whole contents. Has no effect without -o/--others. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---no-empty-directory)--no-empty-directory 
    
Do not list empty directories. Has no effect without --directory. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--u)-u 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---unmerged)--unmerged 
    
Show information about unmerged files in the output, but do not show any other tracked files (forces --stage, overrides --cached). 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--k)-k 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---killed)--killed 
    
Show untracked files on the filesystem that need to be removed due to file/directory conflicts for tracked files to be able to be written to the filesystem. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---resolve-undo)--resolve-undo 
    
Show files having resolve-undo information in the index together with their resolve-undo information. (resolve-undo information is what is used to implement "git checkout -m $PATH", i.e. to recreate merge conflicts that were accidentally resolved) 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--z)-z 
    
\0 line termination on output and do not quote filenames. See OUTPUT below for more information. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---deduplicate)--deduplicate 
    
When only filenames are shown, suppress duplicates that may come from having multiple stages during a merge, or giving `--deleted` and `--modified` option at the same time. When any of the `-t`, `--unmerged`, or `--stage` option is in use, this option has no effect. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--xpattern)-x <pattern> 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---excludepattern)--exclude=<pattern> 
    
Skip untracked files matching pattern. Note that pattern is a shell wildcard pattern. See EXCLUDE PATTERNS below for more information. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--Xfile)-X <file> 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---exclude-fromfile)--exclude-from=<file> 
    
Read exclude patterns from <file>; 1 per line. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---exclude-per-directoryfile)--exclude-per-directory=<file> 
    
Read additional exclude patterns that apply only to the directory and its subdirectories in <file>. If you are trying to emulate the way Porcelain commands work, using the `--exclude-standard` option instead is easier and more thorough. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---exclude-standard)--exclude-standard 
    
Add the standard Git exclusions: .git/info/exclude, .gitignore in each directory, and the user’s global exclusion file. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---error-unmatch)--error-unmatch 
    
If any <file> does not appear in the index, treat this as an error (return 1). 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---with-treetree-ish)--with-tree=<tree-ish> 
    
When using --error-unmatch to expand the user supplied <file> (i.e. path pattern) arguments to paths, pretend that paths which were removed in the index since the named <tree-ish> are still present. Using this option with `-s` or `-u` options does not make any sense. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--t)-t 
    
Show status tags together with filenames. Note that for scripting purposes, [git-status[1]](https://git-scm.com/docs/git-status) `--porcelain` and [git-diff-files[1]](https://git-scm.com/docs/git-diff-files) `--name-status` are almost always superior alternatives; users should look at [git-status[1]](https://git-scm.com/docs/git-status) `--short` or [git-diff[1]](https://git-scm.com/docs/git-diff) `--name-status` for more user-friendly alternatives.
This option provides a reason for showing each filename, in the form of a status tag (which is followed by a space and then the filename). The status tags are all single characters from the following list: 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-H)H 
    
tracked file that is not either unmerged or skip-worktree 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-S)S 
    
tracked file that is skip-worktree 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-M)M 
    
tracked file that is unmerged 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-R)R 
    
tracked file with unstaged removal/deletion 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-C)C 
    
tracked file with unstaged modification/change 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-K)K 
    
untracked paths which are part of file/directory conflicts which prevent checking out tracked files 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-)? 
    
untracked file 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-U)U 
    
file with resolve-undo information 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--v)-v 
    
Similar to `-t`, but use lowercase letters for files that are marked as _assume unchanged_ (see [git-update-index[1]](https://git-scm.com/docs/git-update-index)). 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt--f)-f 
    
Similar to `-t`, but use lowercase letters for files that are marked as _fsmonitor valid_ (see [git-update-index[1]](https://git-scm.com/docs/git-update-index)). 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---full-name)--full-name 
    
When run from a subdirectory, the command usually outputs paths relative to the current directory. This option forces paths to be output relative to the project top directory. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---recurse-submodules)--recurse-submodules 
    
Recursively calls ls-files on each active submodule in the repository. Currently there is only support for the --cached and --stage modes. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---abbrevn)--abbrev[=<n>] 
    
Instead of showing the full 40-byte hexadecimal object lines, show the shortest prefix that is at least _< n>_ hexdigits long that uniquely refers the object. Non default number of digits can be specified with --abbrev=<n>. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---debug)--debug 
    
After each line that describes a file, add more data about its cache entry. This is intended to show as much information as possible for manual inspection; the exact format may change at any time. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---eol)--eol 
    
Show <eolinfo> and <eolattr> of files. <eolinfo> is the file content identification used by Git when the "text" attribute is "auto" (or not set and core.autocrlf is not false). <eolinfo> is either "-text", "none", "lf", "crlf", "mixed" or "".
"" means the file is not a regular file, it is not in the index or not accessible in the working tree.
<eolattr> is the attribute that is used when checking out or committing, it is either "", "-text", "text", "text=auto", "text eol=lf", "text eol=crlf". Since Git 2.10 "text=auto eol=lf" and "text=auto eol=crlf" are supported.
Both the <eolinfo> in the index ("i/<eolinfo>") and in the working tree ("w/<eolinfo>") are shown for regular files, followed by the ("attr/<eolattr>"). 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---sparse)--sparse 
    
If the index is sparse, show the sparse directories without expanding to the contained files. Sparse directories will be shown with a trailing slash, such as "x/" for a sparse directory "x". 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---formatformat)--format=<format> 
    
A string that interpolates `%`(`fieldname`) from the result being shown. It also interpolates `%%` to `%`, and `%xXX` where `XX` are hex digits interpolates to character with hex code `XX`; for example `%x00` interpolates to _\0_ (NUL), `%x09` to _\t_ (TAB) and %x0a to _\n_ (LF). --format cannot be combined with `-s`, `-o`, `-k`, `-t`, `--resolve-undo` and `--eol`. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---)-- 
    
Do not interpret any more arguments as options. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-file)<file> 
    
Files to show. If no files are given all files which match the other specified criteria are shown.
##  [](https://git-scm.com/docs/git-ls-files#_output)OUTPUT
_git ls-files_ just outputs the filenames unless `--stage` is specified in which case it outputs:
```
[<tag> ]<mode> <object> <stage> <file>
```

_git ls-files --eol_ will show i/<eolinfo><SPACES>w/<eolinfo><SPACES>attr/<eolattr><SPACE*><TAB><file>
_git ls-files --unmerged_ and _git ls-files --stage_ can be used to examine detailed information on unmerged paths.
For an unmerged path, instead of recording a single mode/SHA-1 pair, the index records up to three such pairs; one from tree O in stage 1, A in stage 2, and B in stage 3. This information can be used by the user (or the porcelain) to see what should eventually be recorded at the path. (see [git-read-tree[1]](https://git-scm.com/docs/git-read-tree) for more information on state)
Without the `-z` option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). Using `-z` the filename is output verbatim and the line is terminated by a NUL byte.
It is possible to print in a custom format by using the `--format` option, which is able to interpolate different fields using a `%`(`fieldname`) notation. For example, if you only care about the "objectname" and "path" fields, you can execute with a specific "--format" like
```
git ls-files --format='%(objectname) %(path)'
```

##  [](https://git-scm.com/docs/git-ls-files#_field_names)FIELD NAMES
The way each path is shown can be customized by using the `--format=`_< format>_ option, where the %(fieldname) in the <format> string for various aspects of the index entry are interpolated. The following "fieldname" are understood: 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-objectmode)objectmode 
    
The mode of the file which is recorded in the index. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-objecttype)objecttype 
    
The object type of the file which is recorded in the index. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-objectname)objectname 
    
The name of the file which is recorded in the index. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-objectsizepadded)objectsize[:padded] 
    
The object size of the file which is recorded in the index ("-" if the object is a `commit` or `tree`). It also supports a padded format of size with "%(objectsize:padded)". 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-stage)stage 
    
The stage of the file which is recorded in the index. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-eolinfoindex)eolinfo:index 


[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-eolinfoworktree)eolinfo:worktree 
    
The <eolinfo> (see the description of the `--eol` option) of the contents in the index or in the worktree for the path. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-eolattr)eolattr 
    
The <eolattr> (see the description of the `--eol` option) that applies to the path. 

[](https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt-path)path 
    
The pathname of the file which is recorded in the index.
##  [](https://git-scm.com/docs/git-ls-files#_exclude_patterns)EXCLUDE PATTERNS
_git ls-files_ can use a list of "exclude patterns" when traversing the directory tree and finding files to show when the flags --others or --ignored are specified. [gitignore[5]](https://git-scm.com/docs/gitignore) specifies the format of exclude patterns.
These exclude patterns can be specified from the following places, in order:
  1. The command-line flag --exclude=<pattern> specifies a single pattern. Patterns are ordered in the same order they appear in the command line.
  2. The command-line flag --exclude-from=<file> specifies a file containing a list of patterns. Patterns are ordered in the same order they appear in the file.
  3. The command-line flag --exclude-per-directory=<name> specifies a name of the file in each directory _git ls-files_ examines, normally `.gitignore`. Files in deeper directories take precedence. Patterns are ordered in the same order they appear in the files.


A pattern specified on the command line with --exclude or read from the file specified with --exclude-from is relative to the top of the directory tree. A pattern read from a file specified by --exclude-per-directory is relative to the directory that the pattern file appears in.
Generally, you should be able to use `--exclude-standard` when you want the exclude rules applied the same way as what Porcelain commands do. To emulate what `--exclude-standard` specifies, you can give `--exclude-per-directory=.gitignore`, and then specify:
  1. The file specified by the `core.excludesfile` configuration variable, if exists, or the `$XDG_CONFIG_HOME/git/ignore` file.
  2. The `$GIT_DIR/info/exclude` file.


via the `--exclude-from=` option.
##  [](https://git-scm.com/docs/git-ls-files#_see_also)SEE ALSO
[git-read-tree[1]](https://git-scm.com/docs/git-read-tree), [gitignore[5]](https://git-scm.com/docs/gitignore)
##  [](https://git-scm.com/docs/git-ls-files#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### ls-files
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
