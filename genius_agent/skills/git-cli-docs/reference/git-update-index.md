[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --distributed-is-the-new-centralized
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
    * [NAME](https://git-scm.com/docs/git-update-index#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-update-index#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-update-index#_description)
    * [OPTIONS](https://git-scm.com/docs/git-update-index#_options)
    * [USING --REFRESH](https://git-scm.com/docs/git-update-index#_using_refresh)
    * [USING --CACHEINFO OR --INFO-ONLY](https://git-scm.com/docs/git-update-index#_using_cacheinfo_or_info_only)
    * [USING --INDEX-INFO](https://git-scm.com/docs/git-update-index#_using_index_info)
    * [USING “ASSUME UNCHANGED” BIT](https://git-scm.com/docs/git-update-index#_using_assume_unchanged_bit)
    * [EXAMPLES](https://git-scm.com/docs/git-update-index#_examples)
    * [SKIP-WORKTREE BIT](https://git-scm.com/docs/git-update-index#_skip_worktree_bit)
    * [SPLIT INDEX](https://git-scm.com/docs/git-update-index#_split_index)
    * [UNTRACKED CACHE](https://git-scm.com/docs/git-update-index#_untracked_cache)
    * [FILE SYSTEM MONITOR](https://git-scm.com/docs/git-update-index#_file_system_monitor)
    * [CONFIGURATION](https://git-scm.com/docs/git-update-index#_configuration)
    * [NOTES](https://git-scm.com/docs/git-update-index#_notes)
    * [SEE ALSO](https://git-scm.com/docs/git-update-index#_see_also)
    * [GIT](https://git-scm.com/docs/git-update-index#_git)


[ English ▾](https://git-scm.com/docs/git-update-index)
Localized versions of **git-update-index** manual
  1. [English ](https://git-scm.com/docs/git-update-index)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-update-index/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-update-index/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-update-index/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-update-index)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-update-index) git-update-index last updated in 2.52.0
Changes in the **git-update-index** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-update-index/2.52.0)
  3. 2.45.4 → 2.51.2 no changes
  4. [2.45.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-update-index/2.45.3)
  5. 2.43.1 → 2.45.2 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-update-index/2.43.0)
  7. 2.38.1 → 2.42.4 no changes
  8. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-update-index/2.38.0)
  9. 2.36.1 → 2.37.7 no changes
  10. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-update-index/2.36.0)
  11. 2.30.2 → 2.35.8 no changes
  12. [2.30.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-02-08_ ](https://git-scm.com/docs/git-update-index/2.30.1)
  13. 2.25.2 → 2.30.0 no changes
  14. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-update-index/2.25.1)
  15. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-update-index/2.25.0)
  16. 2.19.1 → 2.24.4 no changes
  17. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-update-index/2.19.0)
  18. 2.18.1 → 2.18.5 no changes
  19. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-update-index/2.18.0)
  20. 2.17.1 → 2.17.6 no changes
  21. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-update-index/2.17.0)
  22. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-update-index/2.16.6)
  23. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-update-index/2.15.4)
  24. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-update-index/2.14.6)
  25. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-update-index/2.13.7)
  26. 2.10.5 → 2.12.5 no changes
  27. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-update-index/2.9.5)
  28. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-update-index/2.8.6)
  29. 2.7.6 no changes
  30. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-update-index/2.6.7)
  31. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-update-index/2.5.6)
  32. 2.4.12 no changes
  33. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-update-index/2.3.10)
  34. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-update-index/2.2.3)
  35. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-update-index/2.1.4)
  36. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-update-index/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-update-index#_name)NAME
git-update-index - Register file contents in the working tree to the index
##  [](https://git-scm.com/docs/git-update-index#_synopsis)SYNOPSIS
```
_git update-index_
	     [--add] [--remove | --force-remove] [--replace]
	     [--refresh] [-q] [--unmerged] [--ignore-missing]
	     [(--cacheinfo <mode>,<object>,<file>)…​]
	     [--chmod=(+|-)x]
	     [--[no-]assume-unchanged]
	     [--[no-]skip-worktree]
	     [--[no-]ignore-skip-worktree-entries]
	     [--[no-]fsmonitor-valid]
	     [--ignore-submodules]
	     [--[no-]split-index]
	     [--[no-|test-|force-]untracked-cache]
	     [--[no-]fsmonitor]
	     [--really-refresh] [--unresolve] [--again | -g]
	     [--info-only] [--index-info]
	     [-z] [--stdin] [--index-version <n>]
	     [--show-index-version]
	     [--verbose]
	     [--] [<file>…​]
```

##  [](https://git-scm.com/docs/git-update-index#_description)DESCRIPTION
Modifies the index. Each file mentioned is updated into the index and any _unmerged_ or _needs updating_ state is cleared.
See also [git-add[1]](https://git-scm.com/docs/git-add) for a more user-friendly way to do some of the most common operations on the index.
The way _git update-index_ handles files it is told about can be modified using the various options:
##  [](https://git-scm.com/docs/git-update-index#_options)OPTIONS 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---add)--add 
    
If a specified file isn’t in the index already then it’s added. Default behaviour is to ignore new files. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---remove)--remove 
    
If a specified file is in the index but is missing then it’s removed. Default behavior is to ignore removed files. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---refresh)--refresh 
    
Looks at the current index and checks to see if merges or updates are needed by checking stat() information. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt--q)-q 
    
Quiet. If --refresh finds that the index needs an update, the default behavior is to error out. This option makes _git update-index_ continue anyway. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---ignore-submodules)--ignore-submodules 
    
Do not try to update submodules. This option is only respected when passed before --refresh. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---unmerged)--unmerged 
    
If --refresh finds unmerged changes in the index, the default behavior is to error out. This option makes _git update-index_ continue anyway. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---ignore-missing)--ignore-missing 
    
Ignores missing files during a --refresh 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---cacheinfomodeobjectpath)--cacheinfo <mode>,<object>,<path> 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---cacheinfomodeobjectpath-1)--cacheinfo <mode> <object> <path> 
    
Directly insert the specified info into the index. For backward compatibility, you can also give these three arguments as three separate parameters, but new users are encouraged to use a single-parameter form. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---index-info)--index-info 
    
Read index information from stdin. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---chmod-x)--chmod=(+|-)x 
    
Set the execute permissions on the updated files. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---assume-unchanged)--assume-unchanged 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-assume-unchanged)--no-assume-unchanged 
    
When this flag is specified, the object names recorded for the paths are not updated. Instead, this option sets/unsets the "assume unchanged" bit for the paths. When the "assume unchanged" bit is on, the user promises not to change the file and allows Git to assume that the working tree file matches what is recorded in the index. If you want to change the working tree file, you need to unset the bit to tell Git. This is sometimes helpful when working with a big project on a filesystem that has a very slow lstat(2) system call (e.g. cifs).
Git will fail (gracefully) in case it needs to modify this file in the index e.g. when merging in a commit; thus, in case the assumed-untracked file is changed upstream, you will need to handle the situation manually. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---really-refresh)--really-refresh 
    
Like `--refresh`, but checks stat information unconditionally, without regard to the "assume unchanged" setting. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---skip-worktree)--skip-worktree 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-skip-worktree)--no-skip-worktree 
    
When one of these flags is specified, the object names recorded for the paths are not updated. Instead, these options set and unset the "skip-worktree" bit for the paths. See section "Skip-worktree bit" below for more information. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---ignore-skip-worktree-entries)--ignore-skip-worktree-entries 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-ignore-skip-worktree-entries)--no-ignore-skip-worktree-entries 
    
Do not remove skip-worktree (AKA "index-only") entries even when the `--remove` option was specified. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---fsmonitor-valid)--fsmonitor-valid 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-fsmonitor-valid)--no-fsmonitor-valid 
    
When one of these flags is specified, the object names recorded for the paths are not updated. Instead, these options set and unset the "fsmonitor valid" bit for the paths. See section "File System Monitor" below for more information. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt--g)-g 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---again)--again 
    
Runs _git update-index_ itself on the paths whose index entries are different from those of the `HEAD` commit. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---unresolve)--unresolve 
    
Restores the _unmerged_ or _needs updating_ state of a file during a merge if it was cleared by accident. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---info-only)--info-only 
    
Do not create objects in the object database for all <file> arguments that follow this flag; just insert their object IDs into the index. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---force-remove)--force-remove 
    
Remove the file from the index even when the working directory still has such a file. (Implies --remove.) 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---replace)--replace 
    
By default, when a file `path` exists in the index, _git update-index_ refuses an attempt to add `path/file`. Similarly if a file `path/file` exists, a file `path` cannot be added. With --replace flag, existing entries that conflict with the entry being added are automatically removed with warning messages. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---stdin)--stdin 
    
Instead of taking a list of paths from the command line, read a list of paths from the standard input. Paths are separated by LF (i.e. one path per line) by default. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---verbose)--verbose 
    
Report what is being added and removed from the index. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---index-versionn)--index-version <n> 
    
Write the resulting index out in the named on-disk format version. Supported versions are 2, 3, and 4. The current default version is 2 or 3, depending on whether extra features are used, such as `git` `add` `-N`. With `--verbose`, also report the version the index file uses before and after this command.
Version 4 performs a simple pathname compression that reduces index size by 30%-50% on large repositories, which results in faster load time. Git supports it since version 1.8.0, released in October 2012, and support for it was added to libgit2 in 2016 and to JGit in 2020. Older versions of this manual page called it "relatively young", but it should be considered mature technology these days. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---show-index-version)--show-index-version 
    
Report the index format version used by the on-disk index file. See `--index-version` above. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt--z)-z 
    
Only meaningful with `--stdin` or `--index-info`; paths are separated with NUL character instead of LF. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---split-index)--split-index 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-split-index)--no-split-index 
    
Enable or disable split index mode. If split-index mode is already enabled and `--split-index` is given again, all changes in $GIT_DIR/index are pushed back to the shared index file.
These options take effect whatever the value of the `core.splitIndex` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). But a warning is emitted when the change goes against the configured value, as the configured value will take effect next time the index is read and this will remove the intended effect of the option. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---untracked-cache)--untracked-cache 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-untracked-cache)--no-untracked-cache 
    
Enable or disable untracked cache feature. Please use `--test-untracked-cache` before enabling it.
These options take effect whatever the value of the `core.untrackedCache` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). But a warning is emitted when the change goes against the configured value, as the configured value will take effect next time the index is read and this will remove the intended effect of the option. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---test-untracked-cache)--test-untracked-cache 
    
Only perform tests on the working directory to make sure untracked cache can be used. You have to manually enable untracked cache using `--untracked-cache` or `--force-untracked-cache` or the `core.untrackedCache` configuration variable afterwards if you really want to use it. If a test fails the exit code is 1 and a message explains what is not working as needed, otherwise the exit code is 0 and OK is printed. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---force-untracked-cache)--force-untracked-cache 
    
Same as `--untracked-cache`. Provided for backwards compatibility with older versions of Git where `--untracked-cache` used to imply `--test-untracked-cache` but this option would enable the extension unconditionally. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---fsmonitor)--fsmonitor 


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---no-fsmonitor)--no-fsmonitor 
    
Enable or disable files system monitor feature. These options take effect whatever the value of the `core.fsmonitor` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). But a warning is emitted when the change goes against the configured value, as the configured value will take effect next time the index is read and this will remove the intended effect of the option. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---)-- 
    
Do not interpret any more arguments as options. 

[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt-file)<file> 
    
Files to act on. Note that files beginning with _._ are discarded. This includes `./file` and `dir/./file`. If you don’t want this, then use cleaner names. The same applies to directories ending _/_ and paths with _//_
##  [](https://git-scm.com/docs/git-update-index#_using_refresh)USING --REFRESH
`--refresh` does not calculate a new sha1 file or bring the index up to date for mode/content changes. But what it **does** do is to "re-match" the stat information of a file with the index, so that you can refresh the index for a file that hasn’t been changed but where the stat entry is out of date.
For example, you’d want to do this after doing a _git read-tree_ , to link up the stat index details with the proper files.
##  [](https://git-scm.com/docs/git-update-index#_using_cacheinfo_or_info_only)USING --CACHEINFO OR --INFO-ONLY
`--cacheinfo` is used to register a file that is not in the current working directory. This is useful for minimum-checkout merging.
To pretend you have a file at path with mode and sha1, say:
```
$ git update-index --add --cacheinfo <mode>,<sha1>,<path>
```

`--info-only` is used to register files without placing them in the object database. This is useful for status-only repositories.
Both `--cacheinfo` and `--info-only` behave similarly: the index is updated but the object database isn’t. `--cacheinfo` is useful when the object is in the database but the file isn’t available locally. `--info-only` is useful when the file is available, but you do not wish to update the object database.
##  [](https://git-scm.com/docs/git-update-index#_using_index_info)USING --INDEX-INFO
`--index-info` is a more powerful mechanism that lets you feed multiple entry definitions from the standard input, and designed specifically for scripts. It can take inputs of three formats:
  1. mode SP type SP sha1 TAB path
This format is to stuff `git` `ls-tree` output into the index.
  2. mode SP sha1 SP stage TAB path
This format is to put higher order stages into the index file and matches _git ls-files --stage_ output.
  3. mode SP sha1 TAB path
This format is no longer produced by any Git command, but is and will continue to be supported by `update-index` `--index-info`.


To place a higher stage entry to the index, the path should first be removed by feeding a mode=0 entry for the path, and then feeding necessary input lines in the third format.
For example, starting with this index:
```
$ git ls-files -s
100644 8a1218a1024a212bb3db30becd860315f9f3ac52 0       frotz
```

you can feed the following input to `--index-info`:
```
$ git update-index --index-info
0 0000000000000000000000000000000000000000	frotz
100644 8a1218a1024a212bb3db30becd860315f9f3ac52 1	frotz
100755 8a1218a1024a212bb3db30becd860315f9f3ac52 2	frotz
```

The first line of the input feeds 0 as the mode to remove the path; the SHA-1 does not matter as long as it is well formatted. Then the second and third line feeds stage 1 and stage 2 entries for that path. After the above, we would end up with this:
```
$ git ls-files -s
100644 8a1218a1024a212bb3db30becd860315f9f3ac52 1	frotz
100755 8a1218a1024a212bb3db30becd860315f9f3ac52 2	frotz
```

##  [](https://git-scm.com/docs/git-update-index#_using_assume_unchanged_bit)USING “ASSUME UNCHANGED” BIT
Many operations in Git depend on your filesystem to have an efficient `lstat`(`2`) implementation, so that `st_mtime` information for working tree files can be cheaply checked to see if the file contents have changed from the version recorded in the index file. Unfortunately, some filesystems have inefficient `lstat`(`2`). If your filesystem is one of them, you can set "assume unchanged" bit to paths you have not changed to cause Git not to do this check. Note that setting this bit on a path does not mean Git will check the contents of the file to see if it has changed — it makes Git to omit any checking and assume it has **not** changed. When you make changes to working tree files, you have to explicitly tell Git about it by dropping "assume unchanged" bit, either before or after you modify them.
In order to set "assume unchanged" bit, use `--assume-unchanged` option. To unset, use `--no-assume-unchanged`. To see which files have the "assume unchanged" bit set, use `git` `ls-files` `-v` (see [git-ls-files[1]](https://git-scm.com/docs/git-ls-files)).
The command looks at `core.ignorestat` configuration variable. When this is true, paths updated with `git` `update-index` `paths...` and paths updated with other Git commands that update both index and working tree (e.g. _git apply --index_ , _git checkout-index -u_ , and _git read-tree -u_) are automatically marked as "assume unchanged". Note that "assume unchanged" bit is **not** set if `git` `update-index` `--refresh` finds the working tree file matches the index (use `git` `update-index` `--really-refresh` if you want to mark them as "assume unchanged").
Sometimes users confuse the assume-unchanged bit with the skip-worktree bit. See the final paragraph in the "Skip-worktree bit" section below for an explanation of the differences.
##  [](https://git-scm.com/docs/git-update-index#_examples)EXAMPLES
To update and refresh only the files already checked out:
```
$ git checkout-index -n -f -a && git update-index --ignore-missing --refresh
```


[](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt-Onaninefficientfilesystemwithcoreignorestatset)On an inefficient filesystem with `core.ignorestat` set 
    
```
$ git update-index --really-refresh              **(1)**
$ git update-index --no-assume-unchanged foo.c   **(2)**
$ git diff --name-only                           **(3)**
$ edit foo.c
$ git diff --name-only                           **(4)**
M foo.c
$ git update-index foo.c                         **(5)**
$ git diff --name-only                           **(6)**
$ edit foo.c
$ git diff --name-only                           **(7)**
$ git update-index --no-assume-unchanged foo.c   **(8)**
$ git diff --name-only                           **(9)**
M foo.c
```

  1. forces lstat(2) to set "assume unchanged" bits for paths that match index.
  2. mark the path to be edited.
  3. this does lstat(2) and finds index matches the path.
  4. this does lstat(2) and finds index does **not** match the path.
  5. registering the new version to index sets "assume unchanged" bit.
  6. and it is assumed unchanged.
  7. even after you edit it.
  8. you can tell about the change after the fact.
  9. now it checks with lstat(2) and finds it has been changed.


##  [](https://git-scm.com/docs/git-update-index#_skip_worktree_bit)SKIP-WORKTREE BIT
Skip-worktree bit can be defined in one (long) sentence: Tell git to avoid writing the file to the working directory when reasonably possible, and treat the file as unchanged when it is not present in the working directory.
Note that not all git commands will pay attention to this bit, and some only partially support it.
The update-index flags and the read-tree capabilities relating to the skip-worktree bit predated the introduction of the [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) command, which provides a much easier way to configure and handle the skip-worktree bits. If you want to reduce your working tree to only deal with a subset of the files in the repository, we strongly encourage the use of [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) in preference to the low-level update-index and read-tree primitives.
The primary purpose of the skip-worktree bit is to enable sparse checkouts, i.e. to have working directories with only a subset of paths present. When the skip-worktree bit is set, Git commands (such as `switch`, `pull`, `merge`) will avoid writing these files. However, these commands will sometimes write these files anyway in important cases such as conflicts during a merge or rebase. Git commands will also avoid treating the lack of such files as an intentional deletion; for example `git` `add` `-u` will not stage a deletion for these files and `git` `commit` `-a` will not make a commit deleting them either.
Although this bit looks similar to assume-unchanged bit, its goal is different. The assume-unchanged bit is for leaving the file in the working tree but having Git omit checking it for changes and presuming that the file has not been changed (though if it can determine without stat’ing the file that it has changed, it is free to record the changes). skip-worktree tells Git to ignore the absence of the file, avoid updating it when possible with commands that normally update much of the working directory (e.g. `checkout`, `switch`, `pull`, etc.), and not have its absence be recorded in commits. Note that in sparse checkouts (setup by `git` `sparse-checkout` or by configuring core.sparseCheckout to true), if a file is marked as skip-worktree in the index but is found in the working tree, Git will clear the skip-worktree bit for that file.
##  [](https://git-scm.com/docs/git-update-index#_split_index)SPLIT INDEX
This mode is designed for repositories with very large indexes, and aims at reducing the time it takes to repeatedly write these indexes.
In this mode, the index is split into two files, $GIT_DIR/index and $GIT_DIR/sharedindex.<SHA-1>. Changes are accumulated in $GIT_DIR/index, the split index, while the shared index file contains all index entries and stays unchanged.
All changes in the split index are pushed back to the shared index file when the number of entries in the split index reaches a level specified by the splitIndex.maxPercentChange config variable (see [git-config[1]](https://git-scm.com/docs/git-config)).
Each time a new shared index file is created, the old shared index files are deleted if their modification time is older than what is specified by the splitIndex.sharedIndexExpire config variable (see [git-config[1]](https://git-scm.com/docs/git-config)).
To avoid deleting a shared index file that is still used, its modification time is updated to the current time every time a new split index based on the shared index file is either created or read from.
##  [](https://git-scm.com/docs/git-update-index#_untracked_cache)UNTRACKED CACHE
This cache is meant to speed up commands that involve determining untracked files such as `git` `status`.
This feature works by recording the mtime of the working tree directories and then omitting reading directories and stat calls against files in those directories whose mtime hasn’t changed. For this to work the underlying operating system and file system must change the `st_mtime` field of directories if files in the directory are added, modified or deleted.
You can test whether the filesystem supports that with the `--test-untracked-cache` option. The `--untracked-cache` option used to implicitly perform that test in older versions of Git, but that’s no longer the case.
If you want to enable (or disable) this feature, it is easier to use the `core.untrackedCache` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)) than using the `--untracked-cache` option to `git` `update-index` in each repository, especially if you want to do so across all repositories you use, because you can set the configuration variable to `true` (or `false`) in your `$HOME/.gitconfig` just once and have it affect all repositories you touch.
When the `core.untrackedCache` configuration variable is changed, the untracked cache is added to or removed from the index the next time a command reads the index; while when `--`[`no-`|`force-`]`untracked-cache` are used, the untracked cache is immediately added to or removed from the index.
Before 2.17, the untracked cache had a bug where replacing a directory with a symlink to another directory could cause it to incorrectly show files tracked by git as untracked. See the "status: add a failing test showing a core.untrackedCache bug" commit to git.git. A workaround for that is (and this might work for other undiscovered bugs in the future):
```
$ git -c core.untrackedCache=false status
```

This bug has also been shown to affect non-symlink cases of replacing a directory with a file when it comes to the internal structures of the untracked cache, but no case has been reported where this resulted in wrong "git status" output.
There are also cases where existing indexes written by git versions before 2.17 will reference directories that don’t exist anymore, potentially causing many "could not open directory" warnings to be printed on "git status". These are new warnings for existing issues that were previously silently discarded.
As with the bug described above the solution is to one-off do a "git status" run with `core.untrackedCache=false` to flush out the leftover bad data.
##  [](https://git-scm.com/docs/git-update-index#_file_system_monitor)FILE SYSTEM MONITOR
This feature is intended to speed up git operations for repos that have large working directories.
It enables git to work together with a file system monitor (see [git-fsmonitor--daemon[1]](https://git-scm.com/docs/git-fsmonitor--daemon) and the "fsmonitor-watchman" section of [githooks[5]](https://git-scm.com/docs/githooks)) that can inform it as to what files have been modified. This enables git to avoid having to lstat() every file to find modified files.
When used in conjunction with the untracked cache, it can further improve performance by avoiding the cost of scanning the entire working directory looking for new files.
If you want to enable (or disable) this feature, it is easier to use the `core.fsmonitor` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)) than using the `--fsmonitor` option to `git` `update-index` in each repository, especially if you want to do so across all repositories you use, because you can set the configuration variable in your `$HOME/.gitconfig` just once and have it affect all repositories you touch.
When the `core.fsmonitor` configuration variable is changed, the file system monitor is added to or removed from the index the next time a command reads the index. When `--`[`no-`]`fsmonitor` are used, the file system monitor is immediately added to or removed from the index.
##  [](https://git-scm.com/docs/git-update-index#_configuration)CONFIGURATION
The command honors `core.filemode` configuration variable. If your repository is on a filesystem whose executable bits are unreliable, this should be set to _false_ (see [git-config[1]](https://git-scm.com/docs/git-config)). This causes the command to ignore differences in file modes recorded in the index and the file mode on the filesystem if they differ only on executable bit. On such an unfortunate filesystem, you may need to use _git update-index --chmod=_.
Quite similarly, if `core.symlinks` configuration variable is set to _false_ (see [git-config[1]](https://git-scm.com/docs/git-config)), symbolic links are checked out as plain files, and this command does not modify a recorded file mode from symbolic link to regular file.
The command looks at `core.ignorestat` configuration variable. See _Using "assume unchanged" bit_ section above.
The command also looks at `core.trustctime` configuration variable. It can be useful when the inode change time is regularly modified by something outside Git (file system crawlers and backup systems use ctime for marking files processed) (see [git-config[1]](https://git-scm.com/docs/git-config)).
The untracked cache extension can be enabled by the `core.untrackedCache` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)).
##  [](https://git-scm.com/docs/git-update-index#_notes)NOTES
Users often try to use the assume-unchanged and skip-worktree bits to tell Git to ignore changes to files that are tracked. This does not work as expected, since Git may still check working tree files against the index when performing certain operations. In general, Git does not provide a way to ignore changes to tracked files, so alternate solutions are recommended.
For example, if the file you want to change is some sort of config file, the repository can include a sample config file that can then be copied into the ignored name and modified. The repository can even include a script to treat the sample file as a template, modifying and copying it automatically.
##  [](https://git-scm.com/docs/git-update-index#_see_also)SEE ALSO
[git-config[1]](https://git-scm.com/docs/git-config), [git-add[1]](https://git-scm.com/docs/git-add), [git-ls-files[1]](https://git-scm.com/docs/git-ls-files)
##  [](https://git-scm.com/docs/git-update-index#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### update-index
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
