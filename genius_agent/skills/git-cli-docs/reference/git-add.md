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
    * [NAME](https://git-scm.com/docs/git-add#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-add#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-add#_description)
    * [OPTIONS](https://git-scm.com/docs/git-add#_options)
    * [EXAMPLES](https://git-scm.com/docs/git-add#_examples)
    * [INTERACTIVE MODE](https://git-scm.com/docs/git-add#_interactive_mode)
    * [EDITING PATCHES](https://git-scm.com/docs/git-add#_editing_patches)
    * [CONFIGURATION](https://git-scm.com/docs/git-add#_configuration)
    * [SEE ALSO](https://git-scm.com/docs/git-add#_see_also)
    * [GIT](https://git-scm.com/docs/git-add#_git)


[ English ▾](https://git-scm.com/docs/git-add)
Localized versions of **git-add** manual
  1. [English ](https://git-scm.com/docs/git-add)
  2. [Deutsch ](https://git-scm.com/docs/git-add/de)
  3. [Español ](https://git-scm.com/docs/git-add/es)
  4. [Français ](https://git-scm.com/docs/git-add/fr)
  5. [Íslenska ](https://git-scm.com/docs/git-add/is)
  6. [日本語 ](https://git-scm.com/docs/git-add/ja)
  7. [Português (Brasil) ](https://git-scm.com/docs/git-add/pt_BR)
  8. [Română ](https://git-scm.com/docs/git-add/ro)
  9. [Русский ](https://git-scm.com/docs/git-add/ru)
  10. [Svenska ](https://git-scm.com/docs/git-add/sv)
  11. [українська мова ](https://git-scm.com/docs/git-add/uk)
  12. [简体中文 ](https://git-scm.com/docs/git-add/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-add)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-add) git-add last updated in 2.52.0
Changes in the **git-add** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-add/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-add/2.51.0)
  5. 2.48.1 → 2.50.1 no changes
  6. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-add/2.48.0)
  7. 2.46.1 → 2.47.3 no changes
  8. 2.46.0 no changes
  9. 2.45.1 → 2.45.4 no changes
  10. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-add/2.45.0)
  11. 2.43.2 → 2.44.4 no changes
  12. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-add/2.43.1)
  13. 2.40.1 → 2.43.0 no changes
  14. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-add/2.40.0)
  15. 2.38.1 → 2.39.5 no changes
  16. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-add/2.38.0)
  17. 2.37.4 → 2.37.7 no changes
  18. [2.37.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-08-30_ ](https://git-scm.com/docs/git-add/2.37.3)
  19. 2.34.1 → 2.37.2 no changes
  20. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-add/2.34.0)
  21. 2.25.1 → 2.33.8 no changes
  22. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-add/2.25.0)
  23. 2.22.1 → 2.24.4 no changes
  24. 2.22.0 no changes
  25. 2.21.1 → 2.21.4 no changes
  26. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-add/2.21.0)
  27. 2.18.1 → 2.20.5 no changes
  28. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-add/2.18.0)
  29. 2.17.0 → 2.17.6 no changes
  30. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-add/2.16.6)
  31. 2.15.4 no changes
  32. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-add/2.14.6)
  33. 2.11.4 → 2.13.7 no changes
  34. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-add/2.10.5)
  35. 2.8.6 → 2.9.5 no changes
  36. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-add/2.7.6)
  37. 2.5.6 → 2.6.7 no changes
  38. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-add/2.4.12)
  39. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-add/2.3.10)
  40. 2.1.4 → 2.2.3 no changes
  41. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-add/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-add#_name)NAME
git-add - Add file contents to the index
##  [](https://git-scm.com/docs/git-add#_synopsis)SYNOPSIS
```
git add [--verbose | -v] [--dry-run | -n] [--force | -f] [--interactive | -i] [--patch | -p]
	[--edit | -e] [--[no-]all | -A | --[no-]ignore-removal | [--update | -u]] [--sparse]
	[--intent-to-add | -N] [--refresh] [--ignore-errors] [--ignore-missing] [--renormalize]
	[--chmod=(+|-)x] [--pathspec-from-file=_<file>_ [--pathspec-file-nul]]
	[--] [_<pathspec>_…​]
```

##  [](https://git-scm.com/docs/git-add#_description)DESCRIPTION
Add contents of new or changed files to the index. The "index" (also known as the "staging area") is what you use to prepare the contents of the next commit.
When you run `git` `commit` without any other arguments, it will only commit staged changes. For example, if you’ve edited `file.c` and want to commit your changes to that file, you can run:
```
git add file.c
git commit
```

You can also add only part of your changes to a file with `git` `add` `-p`.
This command can be performed multiple times before a commit. It only adds the content of the specified file(s) at the time the add command is run; if you want subsequent changes included in the next commit, then you must run `git` `add` again to add the new content to the index.
The `git` `status` command can be used to obtain a summary of which files have changes that are staged for the next commit.
The `git` `add` command will not add ignored files by default. You can use the `--force` option to add ignored files. If you specify the exact filename of an ignored file, `git` `add` will fail with a list of ignored files. Otherwise it will silently ignore the file.
Please see [git-commit[1]](https://git-scm.com/docs/git-commit) for alternative ways to add content to a commit.
##  [](https://git-scm.com/docs/git-add#_options)OPTIONS 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-pathspec)_< pathspec>_... 
    
Files to add content from. Fileglobs (e.g. `*.c`) can be given to add all matching files. Also a leading directory name (e.g. `dir` to add `dir/file1` and `dir/file2`) can be given to update the index to match the current state of the directory as a whole (e.g. specifying `dir` will record not just a file `dir/file1` modified in the working tree, a file `dir/file2` added to the working tree, but also a file `dir/file3` removed from the working tree). Note that older versions of Git used to ignore removed files; use `--no-all` option if you want to add modified or new files but ignore removed ones.
For more details about the _< pathspec>_ syntax, see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--n)`-n` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---dry-run)`--dry-run` 
    
Don’t actually add the file(s), just show if they exist and/or will be ignored. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--v)`-v` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---verbose)`--verbose` 
    
Be verbose. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--f)`-f` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---force)`--force` 
    
Allow adding otherwise ignored files. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---sparse)`--sparse` 
    
Allow updating index entries outside of the sparse-checkout cone. Normally, `git` `add` refuses to update index entries whose paths do not fit within the sparse-checkout cone, since those files might be removed from the working tree without warning. See [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) for more details. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--i)`-i` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---interactive)`--interactive` 
    
Add modified contents in the working tree interactively to the index. Optional path arguments may be supplied to limit operation to a subset of the working tree. See “Interactive mode” for details. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--p)`-p` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---patch)`--patch` 
    
Interactively choose hunks of patch between the index and the work tree and add them to the index. This gives the user a chance to review the difference before adding modified contents to the index.
This effectively runs `add` `--interactive`, but bypasses the initial command menu and directly jumps to the `patch` subcommand. See “Interactive mode” for details. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context. Defaults to `diff.context` or 3 if the config option is unset. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---inter-hunk-contextn)`--inter-hunk-context=`_< n>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--e)`-e` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---edit)`--edit` 
    
Open the diff vs. the index in an editor and let the user edit it. After the editor was closed, adjust the hunk headers and apply the patch to the index.
The intent of this option is to pick and choose lines of the patch to apply, or even to modify the contents of lines to be staged. This can be quicker and more flexible than using the interactive hunk selector. However, it is easy to confuse oneself and create a patch that does not apply to the index. See EDITING PATCHES below. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--u)`-u` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---update)`--update` 
    
Update the index just where it already has an entry matching _< pathspec>_. This removes as well as modifies index entries to match the working tree, but adds no new files.
If no _< pathspec>_ is given when `-u` option is used, all tracked files in the entire working tree are updated (old versions of Git used to limit the update to the current directory and its subdirectories). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--A)`-A` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---all)`--all` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---no-ignore-removal)`--no-ignore-removal` 
    
Update the index not only where the working tree has a file matching _< pathspec>_ but also where the index already has an entry. This adds, modifies, and removes index entries to match the working tree.
If no _< pathspec>_ is given when `-A` option is used, all files in the entire working tree are updated (old versions of Git used to limit the update to the current directory and its subdirectories). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---no-all)`--no-all` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---ignore-removal)`--ignore-removal` 
    
Update the index by adding new files that are unknown to the index and files modified in the working tree, but ignore files that have been removed from the working tree. This option is a no-op when no _< pathspec>_ is used.
This option is primarily to help users who are used to older versions of Git, whose `git` `add` _< pathspec>_... was a synonym for `git` `add` `--no-all` _< pathspec>_..., i.e. ignored removed files. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt--N)`-N` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---intent-to-add)`--intent-to-add` 
    
Record only the fact that the path will be added later. An entry for the path is placed in the index with no content. This is useful for, among other things, showing the unstaged content of such files with `git` `diff` and committing them with `git` `commit` `-a`. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---refresh)`--refresh` 
    
Don’t add the file(s), but only refresh their stat() information in the index. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---ignore-errors)`--ignore-errors` 
    
If some files could not be added because of errors indexing them, do not abort the operation, but continue adding the others. The command shall still exit with non-zero status. The configuration variable `add.ignoreErrors` can be set to true to make this the default behaviour. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---ignore-missing)`--ignore-missing` 
    
This option can only be used together with `--dry-run`. By using this option the user can check if any of the given files would be ignored, no matter if they are already present in the work tree or not. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---no-warn-embedded-repo)`--no-warn-embedded-repo` 
    
By default, `git` `add` will warn when adding an embedded repository to the index without using `git` `submodule` `add` to create an entry in `.gitmodules`. This option will suppress the warning (e.g., if you are manually performing operations on submodules). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---renormalize)`--renormalize` 
    
Apply the "clean" process freshly to all tracked files to forcibly add them again to the index. This is useful after changing `core.autocrlf` configuration or the `text` attribute in order to correct files added with wrong _CRLF/LF_ line endings. This option implies `-u`. Lone CR characters are untouched, thus while a _CRLF_ cleans to _LF_ , a _CRCRLF_ sequence is only partially cleaned to _CRLF_. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---chmod-x)`--chmod=`(`+`|`-`)`x` 
    
Override the executable bit of the added files. The executable bit is only changed in the index, the files on disk are left unchanged. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---pathspec-from-filefile)`--pathspec-from-file=`_< file>_ 
    
Pathspec is passed in _< file>_ instead of commandline args. If _< file>_ is exactly `-` then standard input is used. Pathspec elements are separated by _LF_ or _CR/LF_. Pathspec elements can be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). See also `--pathspec-file-nul` and global `--literal-pathspecs`. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---pathspec-file-nul)`--pathspec-file-nul` 
    
Only meaningful with `--pathspec-from-file`. Pathspec elements are separated with _NUL_ character and all other characters are taken literally (including newlines and quotes). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt---)`--` 
    
This option can be used to separate command-line options from the list of files, (useful when filenames might be mistaken for command-line options).
##  [](https://git-scm.com/docs/git-add#_examples)EXAMPLES
  * Adds content from all `*.txt` files under `Documentation` directory and its subdirectories:
```
$ git add Documentation/\*.txt
```

Note that the asterisk `*` is quoted from the shell in this example; this lets the command include the files from subdirectories of `Documentation/` directory.
  * Considers adding content from all `git-*.sh` scripts:
```
$ git add git-*.sh
```

Because this example lets the shell expand the asterisk (i.e. you are listing the files explicitly), it does not consider `subdir/git-foo.sh`.


##  [](https://git-scm.com/docs/git-add#_interactive_mode)INTERACTIVE MODE
When the command enters the interactive mode, it shows the output of the _status_ subcommand, and then goes into its interactive command loop.
The command loop shows the list of subcommands available, and gives a prompt "What now> ". In general, when the prompt ends with a single _>_ , you can pick only one of the choices given and type return, like this:
```
    *** Commands ***
      1: status       2: update       3: revert       4: add untracked
      5: patch        6: diff         7: quit         8: help
    What now> 1
```

You also could say `s` or `sta` or `status` above as long as the choice is unique.
The main command loop has 6 subcommands (plus help and quit). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-status)status 
    
This shows the change between `HEAD` and index (i.e. what will be committed if you say `git` `commit`), and between index and working tree files (i.e. what you could stage further before `git` `commit` using `git` `add`) for each path. A sample output looks like this:
```
              staged     unstaged path
     1:       binary      nothing foo.png
     2:     +403/-35        +1/-1 add-interactive.c
```

It shows that `foo.png` has differences from `HEAD` (but that is binary so line count cannot be shown) and there is no difference between indexed copy and the working tree version (if the working tree version were also different, _binary_ would have been shown in place of _nothing_). The other file, `add-interactive.c`, has 403 lines added and 35 lines deleted if you commit what is in the index, but working tree file has further modifications (one addition and one deletion). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-update)update 
    
This shows the status information and issues an "Update>>" prompt. When the prompt ends with double _> >_, you can make more than one selection, concatenated with whitespace or comma. Also you can say ranges. E.g. "2-5 7,9" to choose 2,3,4,5,7,9 from the list. If the second number in a range is omitted, all remaining patches are taken. E.g. "7-" to choose 7,8,9 from the list. You can say _*_ to choose everything.
What you chose are then highlighted with _*_ , like this:
```
           staged     unstaged path
  1:       binary      nothing foo.png
* 2:     +403/-35        +1/-1 add-interactive.c
```

To remove selection, prefix the input with `-` like this:
```
Update>> -2
```

After making the selection, answer with an empty line to stage the contents of working tree files for selected paths in the index. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-revert)revert 
    
This has a very similar UI to _update_ , and the staged information for selected paths are reverted to that of the HEAD version. Reverting new paths makes them untracked. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-adduntracked)add untracked 
    
This has a very similar UI to _update_ and _revert_ , and lets you add untracked paths to the index. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-patch)patch 
    
This lets you choose one path out of a _status_ like selection. After choosing the path, it presents the diff between the index and the working tree file and asks you if you want to stage the change of each hunk. You can select one of the following options and type return:
```
y - stage this hunk
n - do not stage this hunk
q - quit; do not stage this hunk or any of the remaining ones
a - stage this hunk and all later hunks in the file
d - do not stage this hunk or any of the later hunks in the file
g - select a hunk to go to
/ - search for a hunk matching the given regex
j - go to the next undecided hunk, roll over at the bottom
J - go to the next hunk, roll over at the bottom
k - go to the previous undecided hunk, roll over at the top
K - go to the previous hunk, roll over at the top
s - split the current hunk into smaller hunks
e - manually edit the current hunk
p - print the current hunk
P - print the current hunk using the pager
? - print help
```

After deciding the fate for all hunks, if there is any hunk that was chosen, the index is updated with the selected hunks.
You can omit having to type return here, by setting the configuration variable `interactive.singleKey` to `true`. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-diff)diff 
    
This lets you review what will be committed (i.e. between `HEAD` and index).
##  [](https://git-scm.com/docs/git-add#_editing_patches)EDITING PATCHES
Invoking `git` `add` `-e` or selecting `e` from the interactive hunk selector will open a patch in your editor; after the editor exits, the result is applied to the index. You are free to make arbitrary changes to the patch, but note that some changes may have confusing results, or even result in a patch that cannot be applied. If you want to abort the operation entirely (i.e., stage nothing new in the index), simply delete all lines of the patch. The list below describes some common things you may see in a patch, and which editing operations make sense on them. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-addedcontent)added content 
    
Added content is represented by lines beginning with "+". You can prevent staging any addition lines by deleting them. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-removedcontent)removed content 
    
Removed content is represented by lines beginning with "-". You can prevent staging their removal by converting the "-" to a " " (space). 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-modifiedcontent)modified content 
    
Modified content is represented by "-" lines (removing the old content) followed by "+" lines (adding the replacement content). You can prevent staging the modification by converting "-" lines to " ", and removing "+" lines. Beware that modifying only half of the pair is likely to introduce confusing changes to the index.
There are also more complex operations that can be performed. But beware that because the patch is applied only to the index and not the working tree, the working tree will appear to "undo" the change in the index. For example, introducing a new line into the index that is in neither the `HEAD` nor the working tree will stage the new line for commit, but the line will appear to be reverted in the working tree.
Avoid using these constructs, or do so with extreme caution. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-removinguntouchedcontent)removing untouched content 
    
Content which does not differ between the index and working tree may be shown on context lines, beginning with a " " (space). You can stage context lines for removal by converting the space to a "-". The resulting working tree file will appear to re-add the content. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-modifyingexistingcontent)modifying existing content 
    
One can also modify context lines by staging them for removal (by converting " " to "-") and adding a "+" line with the new content. Similarly, one can modify "+" lines for existing additions or modifications. In all cases, the new modification will appear reverted in the working tree. 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-newcontent)new content 
    
You may also add new content that does not exist in the patch; simply add new lines, each starting with "+". The addition will appear reverted in the working tree.
There are also several operations which should be avoided entirely, as they will make the patch impossible to apply:
  * adding context (" ") or removal ("-") lines
  * deleting context or removal lines
  * modifying the contents of context or removal lines


##  [](https://git-scm.com/docs/git-add#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-addignoreErrors)`add.ignoreErrors` 


[](https://git-scm.com/docs/git-add#Documentation/git-add.txt-addignore-errorsdeprecated)`add.ignore-errors` (deprecated) 
    
Tells `git` `add` to continue adding files when some files cannot be added due to indexing errors. Equivalent to the `--ignore-errors` option. `add.ignore-errors` is deprecated, as it does not follow the usual naming convention for configuration variables.
##  [](https://git-scm.com/docs/git-add#_see_also)SEE ALSO
[git-status[1]](https://git-scm.com/docs/git-status) [git-rm[1]](https://git-scm.com/docs/git-rm) [git-reset[1]](https://git-scm.com/docs/git-reset) [git-mv[1]](https://git-scm.com/docs/git-mv) [git-commit[1]](https://git-scm.com/docs/git-commit) [git-update-index[1]](https://git-scm.com/docs/git-update-index)
##  [](https://git-scm.com/docs/git-add#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### add
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
