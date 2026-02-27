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
    * [NAME](https://git-scm.com/docs/git-svn#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-svn#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-svn#_description)
    * [COMMANDS](https://git-scm.com/docs/git-svn#_commands)
    * [OPTIONS](https://git-scm.com/docs/git-svn#_options)
    * [ADVANCED OPTIONS](https://git-scm.com/docs/git-svn#_advanced_options)
    * [CONFIG FILE-ONLY OPTIONS](https://git-scm.com/docs/git-svn#_config_file_only_options)
    * [BASIC EXAMPLES](https://git-scm.com/docs/git-svn#_basic_examples)
    * [REBASE VS. PULL/MERGE](https://git-scm.com/docs/git-svn#_rebase_vs_pullmerge)
    * [MERGE TRACKING](https://git-scm.com/docs/git-svn#_merge_tracking)
    * [HANDLING OF SVN BRANCHES](https://git-scm.com/docs/git-svn#_handling_of_svn_branches)
    * [CAVEATS](https://git-scm.com/docs/git-svn#_caveats)
    * [CONFIGURATION](https://git-scm.com/docs/git-svn#_configuration)
    * [FILES](https://git-scm.com/docs/git-svn#_files)
    * [BUGS](https://git-scm.com/docs/git-svn#_bugs)
    * [SEE ALSO](https://git-scm.com/docs/git-svn#_see_also)
    * [GIT](https://git-scm.com/docs/git-svn#_git)


[ English ▾](https://git-scm.com/docs/git-svn)
Localized versions of **git-svn** manual
  1. [English ](https://git-scm.com/docs/git-svn)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-svn/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-svn/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-svn/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-svn)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-svn) git-svn last updated in 2.52.0
Changes in the **git-svn** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-svn/2.52.0)
  3. 2.47.1 → 2.51.2 no changes
  4. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git-svn/2.47.0)
  5. 2.44.1 → 2.46.4 no changes
  6. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-svn/2.44.0)
  7. 2.35.1 → 2.43.7 no changes
  8. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-svn/2.35.0)
  9. 2.34.1 → 2.34.8 no changes
  10. 2.34.0 no changes
  11. 2.32.1 → 2.33.8 no changes
  12. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-svn/2.32.0)
  13. 2.30.1 → 2.31.8 no changes
  14. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-svn/2.30.0)
  15. 2.25.1 → 2.29.3 no changes
  16. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-svn/2.25.0)
  17. 2.24.1 → 2.24.4 no changes
  18. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-svn/2.24.0)
  19. 2.22.1 → 2.23.4 no changes
  20. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-svn/2.22.0)
  21. 2.19.1 → 2.21.4 no changes
  22. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-svn/2.19.0)
  23. 2.18.1 → 2.18.5 no changes
  24. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-svn/2.18.0)
  25. 2.16.6 → 2.17.6 no changes
  26. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-svn/2.15.4)
  27. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-svn/2.14.6)
  28. 2.12.5 → 2.13.7 no changes
  29. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-svn/2.11.4)
  30. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-svn/2.10.5)
  31. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-svn/2.9.5)
  32. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-svn/2.8.6)
  33. 2.6.7 → 2.7.6 no changes
  34. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-svn/2.5.6)
  35. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-svn/2.4.12)
  36. 2.3.10 no changes
  37. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-svn/2.2.3)
  38. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-svn/2.1.4)
  39. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-svn/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-svn#_name)NAME
git-svn - Bidirectional operation between a Subversion repository and Git
##  [](https://git-scm.com/docs/git-svn#_synopsis)SYNOPSIS
```
_git svn_ <command> [<options>] [<arguments>]
```

##  [](https://git-scm.com/docs/git-svn#_description)DESCRIPTION
_git svn_ is a simple conduit for changesets between Subversion and Git. It provides a bidirectional flow of changes between a Subversion and a Git repository.
_git svn_ can track a standard Subversion repository, following the common "trunk/branches/tags" layout, with the --stdlayout option. It can also follow branches and tags in any layout with the -T/-t/-b options (see options to _init_ below, and also the _clone_ command).
Once tracking a Subversion repository (with any of the above methods), the Git repository can be updated from Subversion by the _fetch_ command and Subversion updated from Git by the _dcommit_ command.
##  [](https://git-scm.com/docs/git-svn#_commands)COMMANDS 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-init)_init_ 
    
Initializes an empty Git repository with additional metadata directories for _git svn_. The Subversion URL may be specified as a command-line argument, or as full URL arguments to -T/-t/-b. Optionally, the target directory to operate on can be specified as a second argument. Normally this command initializes the current directory. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--Ttrunk-subdir)-T<trunk-subdir> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---trunktrunk-subdir)--trunk=<trunk-subdir> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--ttags-subdir)-t<tags-subdir> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---tagstags-subdir)--tags=<tags-subdir> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--bbranches-subdir)-b<branches-subdir> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---branchesbranches-subdir)--branches=<branches-subdir> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--s)-s 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---stdlayout)--stdlayout 
    
These are optional command-line options for init. Each of these flags can point to a relative repository path (--tags=project/tags) or a full url (--tags=https://foo.org/project/tags). You can specify more than one --tags and/or --branches options, in case your Subversion repository places tags or branches under multiple paths. The option --stdlayout is a shorthand way of setting trunk,tags,branches as the relative paths, which is the Subversion default. If any of the other options are given as well, they take precedence. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---no-metadata)--no-metadata 
    
Set the _noMetadata_ option in the [svn-remote] config. This option is not recommended, please read the _svn.noMetadata_ section of this manpage before using this option. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---use-svm-props)--use-svm-props 
    
Set the _useSvmProps_ option in the [svn-remote] config. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---use-svnsync-props)--use-svnsync-props 
    
Set the _useSvnsyncProps_ option in the [svn-remote] config. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---rewrite-rootURL)--rewrite-root=<URL> 
    
Set the _rewriteRoot_ option in the [svn-remote] config. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---rewrite-uuidUUID)--rewrite-uuid=<UUID> 
    
Set the _rewriteUUID_ option in the [svn-remote] config. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---usernameuser)--username=<user> 
    
For transports that SVN handles authentication for (http, https, and plain svn), specify the username. For other transports (e.g. `svn+ssh://`), you must include the username in the URL, e.g. `svn+ssh://foo@svn.bar.com/project` 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---prefixprefix)--prefix=<prefix> 
    
This allows one to specify a prefix which is prepended to the names of remotes if trunk/branches/tags are specified. The prefix does not automatically include a trailing slash, so be sure you include one in the argument if that is what you want. If --branches/-b is specified, the prefix must include a trailing slash. Setting a prefix (with a trailing slash) is strongly encouraged in any case, as your SVN-tracking refs will then be located at "refs/remotes/$prefix/**", which is compatible with Git’s own remote-tracking ref layout (refs/remotes/$remote/**). Setting a prefix is also useful if you wish to track multiple projects that share a common repository. By default, the prefix is set to _origin/_.
Note |  Before Git v2.0, the default prefix was "" (no prefix). This meant that SVN-tracking refs were put at "refs/remotes/*", which is incompatible with how Git’s own remote-tracking refs are organized. If you still want the old default, you can get it by passing `--prefix` `""` on the command line (`--prefix=""` may not work if your Perl’s Getopt::Long is < v2.37).   
---|--- 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---ignore-refsregex)--ignore-refs=<regex> 
      
When passed to _init_ or _clone_ this regular expression will be preserved as a config key. See _fetch_ for a description of `--ignore-refs`. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---ignore-pathsregex)--ignore-paths=<regex> 
    
When passed to _init_ or _clone_ this regular expression will be preserved as a config key. See _fetch_ for a description of `--ignore-paths`. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---include-pathsregex)--include-paths=<regex> 
    
When passed to _init_ or _clone_ this regular expression will be preserved as a config key. See _fetch_ for a description of `--include-paths`. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---no-minimize-url)--no-minimize-url 
    
When tracking multiple directories (using --stdlayout, --branches, or --tags options), git svn will attempt to connect to the root (or highest allowed level) of the Subversion repository. This default allows better tracking of history if entire projects are moved within a repository, but may cause issues on repositories where read access restrictions are in place. Passing `--no-minimize-url` will allow git svn to accept URLs as-is without attempting to connect to a higher level directory. This option is off by default when only one URL/branch is tracked (it would do little good). 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-fetch)_fetch_ 
    
Fetch unfetched revisions from the Subversion remote we are tracking. The name of the [svn-remote "…​"] section in the $GIT_DIR/config file may be specified as an optional command-line argument.
This automatically updates the rev_map if needed (see _$GIT_DIR/svn/**/.rev_map.*_ in the FILES section below for details). 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---localtime)--localtime 
    
Store Git commit times in the local time zone instead of UTC. This makes _git log_ (even without --date=local) show the same times that `svn` `log` would in the local time zone.
This doesn’t interfere with interoperating with the Subversion repository you cloned from, but if you wish for your local Git repository to be able to interoperate with someone else’s local Git repository, either don’t use this option or you should both use it in the same local time zone. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---parent)--parent 
    
Fetch only from the SVN parent of the current HEAD. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---ignore-refsregex-1)--ignore-refs=<regex> 
    
Ignore refs for branches or tags matching the Perl regular expression. A "negative look-ahead assertion" like _^refs/remotes/origin/(?!tags/wanted-tag|wanted-branch).*$_ can be used to allow only certain refs.
```
config key: svn-remote.<name>.ignore-refs
```

If the ignore-refs configuration key is set, and the command-line option is also given, both regular expressions will be used. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---ignore-pathsregex-1)--ignore-paths=<regex> 
    
This allows one to specify a Perl regular expression that will cause skipping of all matching paths from checkout from SVN. The `--ignore-paths` option should match for every _fetch_ (including automatic fetches due to _clone_ , _dcommit_ , _rebase_ , etc) on a given repository.
```
config key: svn-remote.<name>.ignore-paths
```

If the ignore-paths configuration key is set, and the command-line option is also given, both regular expressions will be used.
Examples: 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-Skipdocdirectoryforeveryfetch)Skip "doc*" directory for every fetch 
    
```
--ignore-paths="^doc"
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-Skipbranchesandtagsoffirstleveldirectories)Skip "branches" and "tags" of first level directories 
    
```
--ignore-paths="^[^/]+/(?:branches|tags)"
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---include-pathsregex-1)--include-paths=<regex> 
    
This allows one to specify a Perl regular expression that will cause the inclusion of only matching paths from checkout from SVN. The `--include-paths` option should match for every _fetch_ (including automatic fetches due to _clone_ , _dcommit_ , _rebase_ , etc) on a given repository. `--ignore-paths` takes precedence over `--include-paths`.
```
config key: svn-remote.<name>.include-paths
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---log-window-sizen)--log-window-size=<n> 
    
Fetch <n> log entries per request when scanning Subversion history. The default is 100. For very large Subversion repositories, larger values may be needed for _clone_ /_fetch_ to complete in reasonable time. But overly large values may lead to higher memory usage and request timeouts. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-clone)_clone_ 
    
Runs _init_ and _fetch_. It will automatically create a directory based on the basename of the URL passed to it; or if a second argument is passed; it will create a directory and work within that. It accepts all arguments that the _init_ and _fetch_ commands accept; with the exception of `--fetch-all` and `--parent`. After a repository is cloned, the _fetch_ command will be able to update revisions without affecting the working tree; and the _rebase_ command will be able to update the working tree with the latest changes. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---preserve-empty-dirs)--preserve-empty-dirs 
    
Create a placeholder file in the local Git repository for each empty directory fetched from Subversion. This includes directories that become empty by removing all entries in the Subversion repository (but not the directory itself). The placeholder files are also tracked and removed when no longer necessary. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---placeholder-filenamefilename)--placeholder-filename=<filename> 
    
Set the name of placeholder files created by --preserve-empty-dirs. Default: ".gitignore" 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-rebase)_rebase_ 
    
This fetches revisions from the SVN parent of the current HEAD and rebases the current (uncommitted to SVN) work against it.
This works similarly to `svn` `update` or _git pull_ except that it preserves linear history with _git rebase_ instead of _git merge_ for ease of dcommitting with _git svn_.
This accepts all options that _git svn fetch_ and _git rebase_ accept. However, `--fetch-all` only fetches from the current [svn-remote], and not all [svn-remote] definitions.
Like _git rebase_ ; this requires that the working tree be clean and have no uncommitted changes.
This automatically updates the rev_map if needed (see _$GIT_DIR/svn/**/.rev_map.*_ in the FILES section below for details). 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--l)-l 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---local)--local 
    
Do not fetch remotely; only run _git rebase_ against the last fetched commit from the upstream SVN. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-dcommit)_dcommit_ 
    
Commit each diff from the current branch directly to the SVN repository, and then rebase or reset (depending on whether or not there is a diff between SVN and head). This will create a revision in SVN for each commit in Git.
When an optional Git branch name (or a Git commit object name) is specified as an argument, the subcommand works on the specified branch, not on the current branch.
Use of _dcommit_ is preferred to _set-tree_ (below). 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---no-rebase)--no-rebase 
    
After committing, do not rebase or reset. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---commit-urlURL)--commit-url <URL> 
    
Commit to this SVN URL (the full path). This is intended to allow existing _git svn_ repositories created with one transport method (e.g. `svn://` or `http://` for anonymous read) to be reused if a user is later given access to an alternate transport method (e.g. `svn+ssh://` or `https://`) for commit.
```
config key: svn-remote.<name>.commiturl
config key: svn.commiturl (overwrites all svn-remote.<name>.commiturl options)
```

Note that the SVN URL of the commiturl config key includes the SVN branch. If you rather want to set the commit URL for an entire SVN repository use svn-remote.<name>.pushurl instead.
Using this option for any other purpose (don’t ask) is very strongly discouraged. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---mergeinfomergeinfo)--mergeinfo=<mergeinfo> 
    
Add the given merge information during the dcommit (e.g. `--mergeinfo="/branches/foo:1-10"`). All svn server versions can store this information (as a property), and svn clients starting from version 1.5 can make use of it. To specify merge information from multiple branches, use a single space character between the branches (`--mergeinfo="/branches/foo:1-10` `/branches/bar:3,5-6,8"`)
```
config key: svn.pushmergeinfo
```

This option will cause git-svn to attempt to automatically populate the svn:mergeinfo property in the SVN repository when possible. Currently, this can only be done when dcommitting non-fast-forward merges where all parents but the first have already been pushed into SVN. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---interactive)--interactive 
    
Ask the user to confirm that a patch set should actually be sent to SVN. For each patch, one may answer "yes" (accept this patch), "no" (discard this patch), "all" (accept all patches), or "quit".
_git svn dcommit_ returns immediately if answer is "no" or "quit", without committing anything to SVN. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-branch)_branch_ 
    
Create a branch in the SVN repository. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--m)-m 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---message)--message 
    
Allows to specify the commit message. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--t)-t 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---tag)--tag 
    
Create a tag by using the tags_subdir instead of the branches_subdir specified during git svn init. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--dpath)-d<path> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---destinationpath)--destination=<path> 
    
If more than one --branches (or --tags) option was given to the _init_ or _clone_ command, you must provide the location of the branch (or tag) you wish to create in the SVN repository. <path> specifies which path to use to create the branch or tag and should match the pattern on the left-hand side of one of the configured branches or tags refspecs. You can see these refspecs with the commands
```
git config --get-all svn-remote.<name>.branches
git config --get-all svn-remote.<name>.tags
```

where <name> is the name of the SVN repository as specified by the -R option to _init_ (or "svn" by default). 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---username)--username 
    
Specify the SVN username to perform the commit as. This option overrides the _username_ configuration property. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---commit-url)--commit-url 
    
Use the specified URL to connect to the destination Subversion repository. This is useful in cases where the source SVN repository is read-only. This option overrides configuration property _commiturl_.
```
git config --get-all svn-remote.<name>.commiturl
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---parents)--parents 
    
Create parent folders. This parameter is equivalent to the parameter --parents on svn cp commands and is useful for non-standard repository layouts. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-tag)_tag_ 
    
Create a tag in the SVN repository. This is a shorthand for _branch -t_. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-log)_log_ 
    
This should make it easy to look up svn log messages when svn users refer to -r/--revision numbers.
The following features from ‘svn log’ are supported: 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--rnn)-r <n>[:<n>] 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---revisionnn)--revision=<n>[:<n>] 
    
is supported, non-numeric args are not: HEAD, NEXT, BASE, PREV, etc …​ 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--v)-v 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---verbose)--verbose 
    
it’s not completely compatible with the --verbose output in svn log, but reasonably close. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---limitn)--limit=<n> 
    
is NOT the same as --max-count, doesn’t count merged/excluded commits 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---incremental)--incremental 
    
supported
New features: 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---show-commit)--show-commit 
    
shows the Git commit sha1, as well 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---oneline)--oneline 
    
our version of --pretty=oneline
Note |  SVN itself only stores times in UTC and nothing else. The regular svn client converts the UTC time to the local time (or based on the TZ= environment). This command has the same behaviour.   
---|---  
Any other arguments are passed directly to _git log_ 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-blame)_blame_ 
    
Show what revision and author last modified each line of a file. The output of this mode is format-compatible with the output of ‘svn blame’ by default. Like the SVN blame command, local uncommitted changes in the working tree are ignored; the version of the file in the HEAD revision is annotated. Unknown arguments are passed directly to _git blame_. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---git-format)--git-format 
    
Produce output in the same format as _git blame_ , but with SVN revision numbers instead of Git commit hashes. In this mode, changes that haven’t been committed to SVN (including local working-copy edits) are shown as revision 0. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-find-rev)_find-rev_ 
    
When given an SVN revision number of the form _rN_ , returns the corresponding Git commit hash (this can optionally be followed by a tree-ish to specify which branch should be searched). When given a tree-ish, returns the corresponding SVN revision number. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--B)-B 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---before)--before 
    
Don’t require an exact match if given an SVN revision, instead find the commit corresponding to the state of the SVN repository (on the current branch) at the specified revision. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--A)-A 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---after)--after 
    
Don’t require an exact match if given an SVN revision; if there is not an exact match return the closest match searching forward in the history. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-set-tree)_set-tree_ 
    
You should consider using _dcommit_ instead of this command. Commit specified commit or tree objects to SVN. This relies on your imported fetch data being up to date. This makes absolutely no attempts to do patching when committing to SVN, it simply overwrites files with those specified in the tree or commit. All merging is assumed to have taken place independently of _git svn_ functions. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-create-ignore)_create-ignore_ 
    
Recursively finds the svn:ignore and svn:global-ignores properties on directories and creates matching .gitignore files. The resulting files are staged to be committed, but are not committed. Use -r/--revision to refer to a specific revision. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-show-ignore)_show-ignore_ 
    
Recursively finds and lists the svn:ignore and svn:global-ignores properties on directories. The output is suitable for appending to the $GIT_DIR/info/exclude file. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-mkdirs)_mkdirs_ 
    
Attempts to recreate empty directories that core Git cannot track based on information in $GIT_DIR/svn/<refname>/unhandled.log files. Empty directories are automatically recreated when using "git svn clone" and "git svn rebase", so "mkdirs" is intended for use after commands like "git checkout" or "git reset". (See the svn-remote.<name>.automkdirs config file option for more information.) 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-commit-diff)_commit-diff_ 
    
Commits the diff of two tree-ish arguments from the command-line. This command does not rely on being inside a `git` `svn` `init`-ed repository. This command takes three arguments, (a) the original tree to diff against, (b) the new tree result, (c) the URL of the target Subversion repository. The final argument (URL) may be omitted if you are working from a _git svn_ -aware repository (that has been `init`-ed with _git svn_). The -r<revision> option is required for this.
The commit message is supplied either directly with the `-m` or `-F` option, or indirectly from the tag or commit when the second tree-ish denotes such an object, or it is requested by invoking an editor (see `--edit` option below). 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--mmsg)-m <msg> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---messagemsg)--message=<msg> 
    
Use the given `msg` as the commit message. This option disables the `--edit` option. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--Ffilename)-F <filename> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---filefilename)--file=<filename> 
    
Take the commit message from the given file. This option disables the `--edit` option. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-info)_info_ 
    
Shows information about a file or directory similar to what ‘svn info’ provides. Does not currently support a -r/--revision argument. Use the --url option to output only the value of the _URL:_ field. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-proplist)_proplist_ 
    
Lists the properties stored in the Subversion repository about a given file or directory. Use -r/--revision to refer to a specific Subversion revision. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-propget)_propget_ 
    
Gets the Subversion property given as the first argument, for a file. A specific revision can be specified with -r/--revision. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-propset)_propset_ 
    
Sets the Subversion property given as the first argument, to the value given as the second argument for the file given as the third argument.
Example:
```
git svn propset svn:keywords "FreeBSD=%H" devel/py-tipper/Makefile
```

This will set the property _svn:keywords_ to _FreeBSD=%H_ for the file _devel/py-tipper/Makefile_. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-show-externals)_show-externals_ 
    
Shows the Subversion externals. Use -r/--revision to specify a specific revision. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-gc)_gc_ 
    
Compress $GIT_DIR/svn/<refname>/unhandled.log files and remove $GIT_DIR/svn/<refname>/index files. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-reset)_reset_ 
    
Undoes the effects of _fetch_ back to the specified revision. This allows you to re-_fetch_ an SVN revision. Normally the contents of an SVN revision should never change and _reset_ should not be necessary. However, if SVN permissions change, or if you alter your --ignore-paths option, a _fetch_ may fail with "not found in commit" (file not previously visible) or "checksum mismatch" (missed a modification). If the problem file cannot be ignored forever (with --ignore-paths) the only way to repair the repo is to use _reset_.
Only the rev_map and refs/remotes/git-svn are changed (see _$GIT_DIR/svn/**/.rev_map.*_ in the FILES section below for details). Follow _reset_ with a _fetch_ and then _git reset_ or _git rebase_ to move local branches onto the new tree. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--rn)-r <n> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---revisionn)--revision=<n> 
    
Specify the most recent revision to keep. All later revisions are discarded. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--p)-p 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---parent-1)--parent 
    
Discard the specified revision as well, keeping the nearest parent instead. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-Example)Example: 
    
Assume you have local changes in "master", but you need to refetch "r2".
```
    r1---r2---r3 remotes/git-svn
                \
                 A---B master
```

Fix the ignore-paths or SVN permissions problem that caused "r2" to be incomplete in the first place. Then:
```
git svn reset -r2 -p
git svn fetch
```

```
    r1---r2'--r3' remotes/git-svn
      \
       r2---r3---A---B master
```

Then fixup "master" with _git rebase_. Do NOT use _git merge_ or your history will not be compatible with a future _dcommit_!
```
git rebase --onto remotes/git-svn A^ master
```

```
    r1---r2'--r3' remotes/git-svn
                \
                 A'--B' master
```

##  [](https://git-scm.com/docs/git-svn#_options)OPTIONS 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---sharedfalsetrueumaskgroupallworldeverybody)--shared[=(false|true|umask|group|all|world|everybody)] 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---templatetemplate-directory)--template=<template-directory> 
    
Only used with the _init_ command. These are passed directly to _git init_. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--rarg)-r <arg> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---revisionarg)--revision <arg> 
    
Used with the _fetch_ command.
This allows revision ranges for partial/cauterized history to be supported. $NUMBER, $NUMBER1:$NUMBER2 (numeric ranges), $NUMBER:HEAD, and BASE:$NUMBER are all supported.
This can allow you to make partial mirrors when running fetch; but is generally not recommended because history will be skipped and lost. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--)- 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---stdin)--stdin 
    
Only used with the _set-tree_ command.
Read a list of commits from stdin and commit them in reverse order. Only the leading sha1 is read from each line, so _git rev-list --pretty=oneline_ output can be used. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---rmdir)--rmdir 
    
Only used with the _dcommit_ , _set-tree_ and _commit-diff_ commands.
Remove directories from the SVN tree if there are no files left behind. SVN can version empty directories, and they are not removed by default if there are no files left in them. Git cannot version empty directories. Enabling this flag will make the commit to SVN act like Git.
```
config key: svn.rmdir
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--e)-e 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---edit)--edit 
    
Only used with the _dcommit_ , _set-tree_ and _commit-diff_ commands.
Edit the commit message before committing to SVN. This is off by default for objects that are commits, and forced on when committing tree objects.
```
config key: svn.edit
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--lnum)-l<num> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---find-copies-harder)--find-copies-harder 
    
Only used with the _dcommit_ , _set-tree_ and _commit-diff_ commands.
They are both passed directly to _git diff-tree_ ; see [git-diff-tree[1]](https://git-scm.com/docs/git-diff-tree) for more information.
```
config key: svn.l
config key: svn.findcopiesharder
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--Afilename)-A<filename> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---authors-filefilename)--authors-file=<filename> 
    
Syntax is compatible with the file used by _git cvsimport_ but an empty email address can be supplied with _< >_:
```
	loginname = Joe User <user@example.com>
```

If this option is specified and _git svn_ encounters an SVN committer name that does not exist in the authors-file, _git svn_ will abort operation. The user will then have to add the appropriate entry. Re-running the previous _git svn_ command after the authors-file is modified should continue operation.
```
config key: svn.authorsfile
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---authors-progfilename)--authors-prog=<filename> 
    
If this option is specified, for each SVN committer name that does not exist in the authors file, the given file is executed with the committer name as the first argument. The program is expected to return a single line of the form "Name <email>" or "Name <>", which will be treated as if included in the authors file.
Due to historical reasons a relative _filename_ is first searched relative to the current directory for _init_ and _clone_ and relative to the root of the working tree for _fetch_. If _filename_ is not found, it is searched like any other command in _$PATH_.
```
config key: svn.authorsProg
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--q)-q 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---quiet)--quiet 
    
Make _git svn_ less verbose. Specify a second time to make it even less verbose. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--m-1)-m 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---merge)--merge 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--sstrategy)-s<strategy> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---strategystrategy)--strategy=<strategy> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--p-1)-p 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---rebase-merges)--rebase-merges 
    
These are only used with the _dcommit_ and _rebase_ commands.
Passed directly to _git rebase_ when using _dcommit_ if a _git reset_ cannot be used (see _dcommit_). 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--n)-n 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---dry-run)--dry-run 
    
This can be used with the _dcommit_ , _rebase_ , _branch_ and _tag_ commands.
For _dcommit_ , print out the series of Git arguments that would show which diffs would be committed to SVN.
For _rebase_ , display the local branch associated with the upstream svn repository associated with the current branch and the URL of svn repository that will be fetched from.
For _branch_ and _tag_ , display the urls that will be used for copying when creating the branch or tag. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---use-log-author)--use-log-author 
    
When retrieving svn commits into Git (as part of _fetch_ , _rebase_ , or _dcommit_ operations), look for the first `From:` line or `Signed-off-by` trailer in the log message and use that as the author string.
```
config key: svn.useLogAuthor
```


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---add-author-from)--add-author-from 
    
When committing to svn from Git (as part of _set-tree_ or _dcommit_ operations), if the existing log message doesn’t already have a `From:` or `Signed-off-by` trailer, append a `From:` line based on the Git commit’s author string. If you use this, then `--use-log-author` will retrieve a valid author string for all commits.
```
config key: svn.addAuthorFrom
```

##  [](https://git-scm.com/docs/git-svn#_advanced_options)ADVANCED OPTIONS 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--iGITSVNID)-i<GIT_SVN_ID> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---idGITSVNID)--id <GIT_SVN_ID> 
    
This sets GIT_SVN_ID (instead of using the environment). This allows the user to override the default refname to fetch from when tracking a single URL. The _log_ and _dcommit_ commands no longer require this switch as an argument. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt--Rremote-name)-R<remote-name> 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---svn-remoteremote-name)--svn-remote <remote-name> 
    
Specify the [svn-remote "<remote-name>"] section to use, this allows SVN multiple repositories to be tracked. Default: "svn" 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt---follow-parent)--follow-parent 
    
This option is only relevant if we are tracking branches (using one of the repository layout options --trunk, --tags, --branches, --stdlayout). For each tracked branch, try to find out where its revision was copied from, and set a suitable parent in the first Git commit for the branch. This is especially helpful when we’re tracking a directory that has been moved around within the repository. If this feature is disabled, the branches created by _git svn_ will all be linear and not share any history, meaning that there will be no information on where branches were branched off or merged. However, following long/convoluted histories can take a long time, so disabling this feature may speed up the cloning process. This feature is enabled by default, use --no-follow-parent to disable it.
```
config key: svn.followparent
```

##  [](https://git-scm.com/docs/git-svn#_config_file_only_options)CONFIG FILE-ONLY OPTIONS 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svnnoMetadata)svn.noMetadata 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svn-remotenamenoMetadata)svn-remote.<name>.noMetadata 
    
This gets rid of the _git-svn-id:_ lines at the end of every commit.
This option can only be used for one-shot imports as _git svn_ will not be able to fetch again without metadata. Additionally, if you lose your _$GIT_DIR/svn/**/.rev_map.*_ files, _git svn_ will not be able to rebuild them.
The _git svn log_ command will not work on repositories using this, either. Using this conflicts with the _useSvmProps_ option for (hopefully) obvious reasons.
This option is NOT recommended as it makes it difficult to track down old references to SVN revision numbers in existing documentation, bug reports, and archives. If you plan to eventually migrate from SVN to Git and are certain about dropping SVN history, consider [git-filter-repo](https://github.com/newren/git-filter-repo) instead. filter-repo also allows reformatting of metadata for ease-of-reading and rewriting authorship info for non-"svn.authorsFile" users. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svnuseSvmProps)svn.useSvmProps 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svn-remotenameuseSvmProps)svn-remote.<name>.useSvmProps 
    
This allows _git svn_ to re-map repository URLs and UUIDs from mirrors created using SVN::Mirror (or svk) for metadata.
If an SVN revision has a property, "svm:headrev", it is likely that the revision was created by SVN::Mirror (also used by SVK). The property contains a repository UUID and a revision. We want to make it look like we are mirroring the original URL, so introduce a helper function that returns the original identity URL and UUID, and use it when generating metadata in commit messages. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svnuseSvnsyncProps)svn.useSvnsyncProps 


[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svn-remotenameuseSvnsyncprops)svn-remote.<name>.useSvnsyncprops 
    
Similar to the useSvmProps option; this is for users of the svnsync(1) command distributed with SVN 1.4.x and later. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svn-remotenamerewriteRoot)svn-remote.<name>.rewriteRoot 
    
This allows users to create repositories from alternate URLs. For example, an administrator could run _git svn_ on the server locally (accessing via file://) but wish to distribute the repository with a public http:// or svn:// URL in the metadata so users of it will see the public URL. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svn-remotenamerewriteUUID)svn-remote.<name>.rewriteUUID 
    
Similar to the useSvmProps option; this is for users who need to remap the UUID manually. This may be useful in situations where the original UUID is not available via either useSvmProps or useSvnsyncProps. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svn-remotenamepushurl)svn-remote.<name>.pushurl 
    
Similar to Git’s `remote.`_< name>_`.pushurl`, this key is designed to be used in cases where _url_ points to an SVN repository via a read-only transport, to provide an alternate read/write transport. It is assumed that both keys point to the same repository. Unlike _commiturl_ , _pushurl_ is a base path. If either _commiturl_ or _pushurl_ could be used, _commiturl_ takes precedence. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svnbrokenSymlinkWorkaround)svn.brokenSymlinkWorkaround 
    
This disables potentially expensive checks to workaround broken symlinks checked into SVN by broken clients. Set this option to "false" if you track a SVN repository with many empty blobs that are not symlinks. This option may be changed while _git svn_ is running and take effect on the next revision fetched. If unset, _git svn_ assumes this option to be "true". 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svnpathnameencoding)svn.pathnameencoding 
    
This instructs git svn to recode pathnames to a given encoding. It can be used by windows users and by those who work in non-utf8 locales to avoid corrupted file names with non-ASCII characters. Valid encodings are the ones supported by Perl’s Encode module. 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-svn-remotenameautomkdirs)svn-remote.<name>.automkdirs 
    
Normally, the "git svn clone" and "git svn rebase" commands attempt to recreate empty directories that are in the Subversion repository. If this option is set to "false", then empty directories will only be created if the "git svn mkdirs" command is run explicitly. If unset, _git svn_ assumes this option to be "true".
Since the noMetadata, rewriteRoot, rewriteUUID, useSvnsyncProps and useSvmProps options all affect the metadata generated and used by _git svn_ ; they **must** be set in the configuration file before any history is imported and these settings should never be changed once they are set.
Additionally, only one of these options can be used per svn-remote section because they affect the _git-svn-id:_ metadata line, except for rewriteRoot and rewriteUUID which can be used together.
##  [](https://git-scm.com/docs/git-svn#_basic_examples)BASIC EXAMPLES
Tracking and contributing to the trunk of a Subversion-managed project (ignoring tags and branches):
```
# Clone a repo (like git clone):
	git svn clone http://svn.example.com/project/trunk
# Enter the newly cloned directory:
	cd trunk
# You should be on master branch, double-check with 'git branch'
	git branch
# Do some work and commit locally to Git:
	git commit ...
# Something is committed to SVN, rebase your local changes against the
# latest changes in SVN:
	git svn rebase
# Now commit your changes (that were committed previously using Git) to SVN,
# as well as automatically updating your working HEAD:
	git svn dcommit
# Append svn:ignore and svn:global-ignores settings to the default Git exclude file:
	git svn show-ignore >> .git/info/exclude
```

Tracking and contributing to an entire Subversion-managed project (complete with a trunk, tags and branches):
```
# Clone a repo with standard SVN directory layout (like git clone):
	git svn clone http://svn.example.com/project --stdlayout --prefix svn/
# Or, if the repo uses a non-standard directory layout:
	git svn clone http://svn.example.com/project -T tr -b branch -t tag --prefix svn/
# View all branches and tags you have cloned:
	git branch -r
# Create a new branch in SVN
	git svn branch waldo
# Reset your master to trunk (or any other branch, replacing 'trunk'
# with the appropriate name):
	git reset --hard svn/trunk
# You may only dcommit to one branch/tag/trunk at a time.  The usage
# of dcommit/rebase/show-ignore should be the same as above.
```

The initial _git svn clone_ can be quite time-consuming (especially for large Subversion repositories). If multiple people (or one person with multiple machines) want to use _git svn_ to interact with the same Subversion repository, you can do the initial _git svn clone_ to a repository on a server and have each person clone that repository with _git clone_ :
```
# Do the initial import on a server
	ssh server "cd /pub && git svn clone http://svn.example.com/project [options...]"
# Clone locally - make sure the refs/remotes/ space matches the server
	mkdir project
	cd project
	git init
	git remote add origin server:/pub/project
	git config --replace-all remote.origin.fetch '+refs/remotes/*:refs/remotes/*'
	git fetch
# Prevent fetch/pull from remote Git server in the future,
# we only want to use git svn for future updates
	git config --remove-section remote.origin
# Create a local branch from one of the branches just fetched
	git checkout -b master FETCH_HEAD
# Initialize 'git svn' locally (be sure to use the same URL and
# --stdlayout/-T/-b/-t/--prefix options as were used on server)
	git svn init http://svn.example.com/project [options...]
# Pull the latest changes from Subversion
	git svn rebase
```

##  [](https://git-scm.com/docs/git-svn#_rebase_vs_pullmerge)REBASE VS. PULL/MERGE
Prefer to use _git svn rebase_ or _git rebase_ , rather than _git pull_ or _git merge_ to synchronize unintegrated commits with a _git svn_ branch. Doing so will keep the history of unintegrated commits linear with respect to the upstream SVN repository and allow the use of the preferred _git svn dcommit_ subcommand to push unintegrated commits back into SVN.
Originally, _git svn_ recommended that developers pulled or merged from the _git svn_ branch. This was because the author favored `git` `svn` `set-tree` `B` to commit a single head rather than the `git` `svn` `set-tree` `A..B` notation to commit multiple commits. Use of _git pull_ or _git merge_ with `git` `svn` `set-tree` `A..B` will cause non-linear history to be flattened when committing into SVN and this can lead to merge commits unexpectedly reversing previous commits in SVN.
##  [](https://git-scm.com/docs/git-svn#_merge_tracking)MERGE TRACKING
While _git svn_ can track copy history (including branches and tags) for repositories adopting a standard layout, it cannot yet represent merge history that happened inside git back upstream to SVN users. Therefore it is advised that users keep history as linear as possible inside Git to ease compatibility with SVN (see the CAVEATS section below).
##  [](https://git-scm.com/docs/git-svn#_handling_of_svn_branches)HANDLING OF SVN BRANCHES
If _git svn_ is configured to fetch branches (and --follow-branches is in effect), it sometimes creates multiple Git branches for one SVN branch, where the additional branches have names of the form _branchname@nnn_ (with nnn an SVN revision number). These additional branches are created if _git svn_ cannot find a parent commit for the first commit in an SVN branch, to connect the branch to the history of the other branches.
Normally, the first commit in an SVN branch consists of a copy operation. _git svn_ will read this commit to get the SVN revision the branch was created from. It will then try to find the Git commit that corresponds to this SVN revision, and use that as the parent of the branch. However, it is possible that there is no suitable Git commit to serve as parent. This will happen, among other reasons, if the SVN branch is a copy of a revision that was not fetched by _git svn_ (e.g. because it is an old revision that was skipped with `--revision`), or if in SVN a directory was copied that is not tracked by _git svn_ (such as a branch that is not tracked at all, or a subdirectory of a tracked branch). In these cases, _git svn_ will still create a Git branch, but instead of using an existing Git commit as the parent of the branch, it will read the SVN history of the directory the branch was copied from and create appropriate Git commits. This is indicated by the message "Initializing parent: <branchname>".
Additionally, it will create a special branch named _< branchname>@<SVN-Revision>_, where <SVN-Revision> is the SVN revision number the branch was copied from. This branch will point to the newly created parent commit of the branch. If in SVN the branch was deleted and later recreated from a different version, there will be multiple such branches with an _@_.
Note that this may mean that multiple Git commits are created for a single SVN revision.
An example: in an SVN repository with a standard trunk/tags/branches layout, a directory trunk/sub is created in r.100. In r.200, trunk/sub is branched by copying it to branches/. _git svn clone -s_ will then create a branch _sub_. It will also create new Git commits for r.100 through r.199 and use these as the history of branch _sub_. Thus there will be two Git commits for each revision from r.100 to r.199 (one containing trunk/, one containing trunk/sub/). Finally, it will create a branch _sub@200_ pointing to the new parent commit of branch _sub_ (i.e. the commit for r.200 and trunk/sub/).
##  [](https://git-scm.com/docs/git-svn#_caveats)CAVEATS
For the sake of simplicity and interoperating with Subversion, it is recommended that all _git svn_ users clone, fetch and dcommit directly from the SVN server, and avoid all _git clone_ /_pull_ /_merge_ /_push_ operations between Git repositories and branches. The recommended method of exchanging code between Git branches and users is _git format-patch_ and _git am_ , or just 'dcommit’ing to the SVN repository.
Running _git merge_ or _git pull_ is NOT recommended on a branch you plan to _dcommit_ from because Subversion users cannot see any merges you’ve made. Furthermore, if you merge or pull from a Git branch that is a mirror of an SVN branch, _dcommit_ may commit to the wrong branch.
If you do merge, note the following rule: _git svn dcommit_ will attempt to commit on top of the SVN commit named in
```
git log --grep=^git-svn-id: --first-parent -1
```

You _must_ therefore ensure that the most recent commit of the branch you want to dcommit to is the _first_ parent of the merge. Chaos will ensue otherwise, especially if the first parent is an older commit on the same SVN branch.
_git clone_ does not clone branches under the refs/remotes/ hierarchy or any _git svn_ metadata, or config. So repositories created and managed with using _git svn_ should use _rsync_ for cloning, if cloning is to be done at all.
Since _dcommit_ uses rebase internally, any Git branches you _git push_ to before _dcommit_ on will require forcing an overwrite of the existing ref on the remote repository. This is generally considered bad practice, see the [git-push[1]](https://git-scm.com/docs/git-push) documentation for details.
Do not use the --amend option of [git-commit[1]](https://git-scm.com/docs/git-commit) on a change you’ve already dcommitted. It is considered bad practice to --amend commits you’ve already pushed to a remote repository for other users, and dcommit with SVN is analogous to that.
When cloning an SVN repository, if none of the options for describing the repository layout is used (--trunk, --tags, --branches, --stdlayout), _git svn clone_ will create a Git repository with completely linear history, where branches and tags appear as separate directories in the working copy. While this is the easiest way to get a copy of a complete repository, for projects with many branches it will lead to a working copy many times larger than just the trunk. Thus for projects using the standard directory structure (trunk/branches/tags), it is recommended to clone with option `--stdlayout`. If the project uses a non-standard structure, and/or if branches and tags are not required, it is easiest to only clone one directory (typically trunk), without giving any repository layout options. If the full history with branches and tags is required, the options `--trunk` / `--branches` / `--tags` must be used.
When using multiple --branches or --tags, _git svn_ does not automatically handle name collisions (for example, if two branches from different paths have the same name, or if a branch and a tag have the same name). In these cases, use _init_ to set up your Git repository then, before your first _fetch_ , edit the $GIT_DIR/config file so that the branches and tags are associated with different name spaces. For example:
```
branches = stable/*:refs/remotes/svn/stable/*
branches = debug/*:refs/remotes/svn/debug/*
```

##  [](https://git-scm.com/docs/git-svn#_configuration)CONFIGURATION
_git svn_ stores [svn-remote] configuration information in the repository $GIT_DIR/config file. It is similar the core Git [remote] sections except _fetch_ keys do not accept glob arguments; but they are instead handled by the _branches_ and _tags_ keys. Since some SVN repositories are oddly configured with multiple projects glob expansions such those listed below are allowed:
```
[svn-remote "project-a"]
	url = http://server.org/svn
	fetch = trunk/project-a:refs/remotes/project-a/trunk
	branches = branches/*/project-a:refs/remotes/project-a/branches/*
	branches = branches/release_*:refs/remotes/project-a/branches/release_*
	branches = branches/re*se:refs/remotes/project-a/branches/*
	tags = tags/*/project-a:refs/remotes/project-a/tags/*
```

Keep in mind that the `*` (asterisk) wildcard of the local ref (right of the `:`) **must** be the farthest right path component; however the remote wildcard may be anywhere as long as it’s an independent path component (surrounded by `/` or EOL). This type of configuration is not automatically created by _init_ and should be manually entered with a text-editor or using _git config_.
Also note that only one asterisk is allowed per word. For example:
```
branches = branches/re*se:refs/remotes/project-a/branches/*
```

will match branches _release_ , _rese_ , _re123se_ , however
```
branches = branches/re*s*e:refs/remotes/project-a/branches/*
```

will produce an error.
It is also possible to fetch a subset of branches or tags by using a comma-separated list of names within braces. For example:
```
[svn-remote "huge-project"]
	url = http://server.org/svn
	fetch = trunk/src:refs/remotes/trunk
	branches = branches/{red,green}/src:refs/remotes/project-a/branches/*
	tags = tags/{1.0,2.0}/src:refs/remotes/project-a/tags/*
```

Multiple fetch, branches, and tags keys are supported:
```
[svn-remote "messy-repo"]
	url = http://server.org/svn
	fetch = trunk/project-a:refs/remotes/project-a/trunk
	fetch = branches/demos/june-project-a-demo:refs/remotes/project-a/demos/june-demo
	branches = branches/server/*:refs/remotes/project-a/branches/*
	branches = branches/demos/2011/*:refs/remotes/project-a/2011-demos/*
	tags = tags/server/*:refs/remotes/project-a/tags/*
```

Creating a branch in such a configuration requires disambiguating which location to use using the -d or --destination flag:
```
$ git svn branch -d branches/server release-2-3-0
```

Note that git-svn keeps track of the highest revision in which a branch or tag has appeared. If the subset of branches or tags is changed after fetching, then $GIT_DIR/svn/.metadata must be manually edited to remove (or reset) branches-maxRev and/or tags-maxRev as appropriate.
##  [](https://git-scm.com/docs/git-svn#_files)FILES 

[](https://git-scm.com/docs/git-svn#Documentation/git-svn.txt-GITDIRsvnrevmap)$GIT_DIR/svn/**/.rev_map.* 
    
Mapping between Subversion revision numbers and Git commit names. In a repository where the noMetadata option is not set, this can be rebuilt from the git-svn-id: lines that are at the end of every commit (see the _svn.noMetadata_ section above for details).
_git svn fetch_ and _git svn rebase_ automatically update the rev_map if it is missing or not up to date. _git svn reset_ automatically rewinds it.
##  [](https://git-scm.com/docs/git-svn#_bugs)BUGS
We ignore all SVN properties except svn:executable. Any unhandled properties are logged to $GIT_DIR/svn/<refname>/unhandled.log
Renamed and copied directories are not detected by Git and hence not tracked when committing to SVN. I do not plan on adding support for this as it’s quite difficult and time-consuming to get working for all the possible corner cases (Git doesn’t do it, either). Committing renamed and copied files is fully supported if they’re similar enough for Git to detect them.
In SVN, it is possible (though discouraged) to commit changes to a tag (because a tag is just a directory copy, thus technically the same as a branch). When cloning an SVN repository, _git svn_ cannot know if such a commit to a tag will happen in the future. Thus it acts conservatively and imports all SVN tags as branches, prefixing the tag name with _tags/_.
##  [](https://git-scm.com/docs/git-svn#_see_also)SEE ALSO
[git-rebase[1]](https://git-scm.com/docs/git-rebase)
##  [](https://git-scm.com/docs/git-svn#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### svn
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
