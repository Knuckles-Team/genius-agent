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
    * [NAME](https://git-scm.com/docs/git-config#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-config#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-config#_description)
    * [COMMANDS](https://git-scm.com/docs/git-config#_commands)
    * [OPTIONS](https://git-scm.com/docs/git-config#OPTIONS)
    * [DEPRECATED MODES](https://git-scm.com/docs/git-config#_deprecated_modes)
    * [CONFIGURATION](https://git-scm.com/docs/git-config#_configuration)
    * [FILES](https://git-scm.com/docs/git-config#FILES)
    * [SCOPES](https://git-scm.com/docs/git-config#SCOPES)
    * [ENVIRONMENT](https://git-scm.com/docs/git-config#ENVIRONMENT)
    * [EXAMPLES](https://git-scm.com/docs/git-config#EXAMPLES)
    * [CONFIGURATION FILE](https://git-scm.com/docs/git-config#_configuration_file)
    * [BUGS](https://git-scm.com/docs/git-config#_bugs)
    * [GIT](https://git-scm.com/docs/git-config#_git)


[ English ▾](https://git-scm.com/docs/git-config)
Localized versions of **git-config** manual
  1. [English ](https://git-scm.com/docs/git-config)
  2. [Deutsch ](https://git-scm.com/docs/git-config/de)
  3. [Français ](https://git-scm.com/docs/git-config/fr)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-config/pt_BR)
  5. [Svenska ](https://git-scm.com/docs/git-config/sv)
  6. [українська мова ](https://git-scm.com/docs/git-config/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-config/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-config)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-config) git-config last updated in 2.53.0
Changes in the **git-config** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-config/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-config/2.52.0)
  3. [2.51.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-27_ ](https://git-scm.com/docs/git-config/2.51.2)
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-config/2.51.1)
  5. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-config/2.51.0)
  6. 2.50.1 no changes
  7. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-config/2.50.0)
  8. 2.49.1 no changes
  9. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-config/2.49.0)
  10. 2.48.2 no changes
  11. [2.48.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-13_ ](https://git-scm.com/docs/git-config/2.48.1)
  12. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-config/2.48.0)
  13. 2.47.3 no changes
  14. [2.47.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.47.2)
  15. [2.47.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-25_ ](https://git-scm.com/docs/git-config/2.47.1)
  16. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git-config/2.47.0)
  17. 2.46.4 no changes
  18. [2.46.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.46.3)
  19. [2.46.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-23_ ](https://git-scm.com/docs/git-config/2.46.2)
  20. [2.46.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-09-13_ ](https://git-scm.com/docs/git-config/2.46.1)
  21. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-config/2.46.0)
  22. 2.45.4 no changes
  23. [2.45.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.45.3)
  24. 2.45.1 → 2.45.2 no changes
  25. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-config/2.45.0)
  26. 2.44.4 no changes
  27. [2.44.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.44.3)
  28. 2.44.1 → 2.44.2 no changes
  29. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-config/2.44.0)
  30. 2.43.7 no changes
  31. [2.43.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.43.6)
  32. 2.43.2 → 2.43.5 no changes
  33. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git-config/2.43.1)
  34. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-config/2.43.0)
  35. [2.42.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.42.4)
  36. 2.42.2 → 2.42.3 no changes
  37. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git-config/2.42.1)
  38. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-config/2.42.0)
  39. [2.41.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.41.3)
  40. 2.41.1 → 2.41.2 no changes
  41. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-config/2.41.0)
  42. [2.40.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-config/2.40.4)
  43. 2.40.1 → 2.40.3 no changes
  44. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-config/2.40.0)
  45. 2.39.1 → 2.39.5 no changes
  46. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-config/2.39.0)
  47. 2.38.3 → 2.38.5 no changes
  48. [2.38.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-11_ ](https://git-scm.com/docs/git-config/2.38.2)
  49. [2.38.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-07_ ](https://git-scm.com/docs/git-config/2.38.1)
  50. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-config/2.38.0)
  51. 2.37.5 → 2.37.7 no changes
  52. [2.37.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.37.4)
  53. 2.37.3 no changes
  54. [2.37.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-08-11_ ](https://git-scm.com/docs/git-config/2.37.2)
  55. 2.37.1 no changes
  56. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-config/2.37.0)
  57. 2.36.4 → 2.36.6 no changes
  58. [2.36.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.36.3)
  59. [2.36.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-config/2.36.2)
  60. 2.36.1 no changes
  61. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-config/2.36.0)
  62. 2.35.6 → 2.35.8 no changes
  63. [2.35.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.35.5)
  64. [2.35.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-config/2.35.4)
  65. [2.35.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-13_ ](https://git-scm.com/docs/git-config/2.35.3)
  66. [2.35.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-config/2.35.2)
  67. 2.35.1 no changes
  68. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-config/2.35.0)
  69. 2.34.6 → 2.34.8 no changes
  70. [2.34.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.34.5)
  71. [2.34.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-config/2.34.4)
  72. [2.34.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-13_ ](https://git-scm.com/docs/git-config/2.34.3)
  73. [2.34.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-config/2.34.2)
  74. 2.34.1 no changes
  75. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-config/2.34.0)
  76. 2.33.6 → 2.33.8 no changes
  77. [2.33.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.33.5)
  78. [2.33.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-config/2.33.4)
  79. [2.33.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-13_ ](https://git-scm.com/docs/git-config/2.33.3)
  80. [2.33.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-config/2.33.2)
  81. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git-config/2.33.1)
  82. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-config/2.33.0)
  83. 2.32.5 → 2.32.7 no changes
  84. [2.32.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.32.4)
  85. [2.32.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-config/2.32.3)
  86. [2.32.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-13_ ](https://git-scm.com/docs/git-config/2.32.2)
  87. [2.32.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-config/2.32.1)
  88. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-config/2.32.0)
  89. 2.31.6 → 2.31.8 no changes
  90. [2.31.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.31.5)
  91. [2.31.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-config/2.31.4)
  92. [2.31.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-13_ ](https://git-scm.com/docs/git-config/2.31.3)
  93. [2.31.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-config/2.31.2)
  94. [2.31.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-26_ ](https://git-scm.com/docs/git-config/2.31.1)
  95. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-config/2.31.0)
  96. 2.30.7 → 2.30.9 no changes
  97. [2.30.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-06_ ](https://git-scm.com/docs/git-config/2.30.6)
  98. [2.30.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-23_ ](https://git-scm.com/docs/git-config/2.30.5)
  99. [2.30.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-13_ ](https://git-scm.com/docs/git-config/2.30.4)
  100. [2.30.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git-config/2.30.3)
  101. 2.30.2 no changes
  102. [2.30.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-02-08_ ](https://git-scm.com/docs/git-config/2.30.1)
  103. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-config/2.30.0)
  104. 2.29.1 → 2.29.3 no changes
  105. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-config/2.29.0)
  106. 2.28.1 no changes
  107. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-config/2.28.0)
  108. 2.27.1 no changes
  109. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-config/2.27.0)
  110. 2.26.1 → 2.26.3 no changes
  111. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git-config/2.26.0)
  112. 2.25.3 → 2.25.5 no changes
  113. [2.25.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-17_ ](https://git-scm.com/docs/git-config/2.25.2)
  114. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git-config/2.25.1)
  115. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-config/2.25.0)
  116. 2.24.1 → 2.24.4 no changes
  117. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-config/2.24.0)
  118. 2.23.1 → 2.23.4 no changes
  119. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-config/2.23.0)
  120. 2.22.2 → 2.22.5 no changes
  121. [2.22.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-11_ ](https://git-scm.com/docs/git-config/2.22.1)
  122. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-config/2.22.0)
  123. 2.21.1 → 2.21.4 no changes
  124. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-config/2.21.0)
  125. 2.20.1 → 2.20.5 no changes
  126. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-config/2.20.0)
  127. 2.19.3 → 2.19.6 no changes
  128. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-config/2.19.2)
  129. 2.19.1 no changes
  130. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-config/2.19.0)
  131. 2.18.1 → 2.18.5 no changes
  132. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-config/2.18.0)
  133. 2.17.1 → 2.17.6 no changes
  134. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git-config/2.17.0)
  135. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-config/2.16.6)
  136. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-config/2.15.4)
  137. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-config/2.14.6)
  138. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-config/2.13.7)
  139. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-config/2.12.5)
  140. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-config/2.11.4)
  141. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-config/2.10.5)
  142. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-config/2.9.5)
  143. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-config/2.8.6)
  144. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-config/2.7.6)
  145. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-config/2.6.7)
  146. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-config/2.5.6)
  147. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-config/2.4.12)
  148. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-config/2.3.10)
  149. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-config/2.2.3)
  150. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-config/2.1.4)
  151. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-config/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-config#_name)NAME
git-config - Get and set repository or global options
##  [](https://git-scm.com/docs/git-config#_synopsis)SYNOPSIS
```
_git config list_ [<file-option>] [<display-option>] [--includes]
_git config get_ [<file-option>] [<display-option>] [--includes] [--all] [--regexp] [--value=<pattern>] [--fixed-value] [--default=<default>] [--url=<url>] <name>
_git config set_ [<file-option>] [--type=<type>] [--all] [--value=<pattern>] [--fixed-value] <name> <value>
_git config unset_ [<file-option>] [--all] [--value=<pattern>] [--fixed-value] <name>
_git config rename-section_ [<file-option>] <old-name> <new-name>
_git config remove-section_ [<file-option>] <name>
_git config edit_ [<file-option>]
_git config_ [<file-option>] --get-colorbool <name> [<stdout-is-tty>]
```

##  [](https://git-scm.com/docs/git-config#_description)DESCRIPTION
You can query/set/replace/unset options with this command. The name is actually the section and the key separated by a dot, and the value will be escaped.
Multiple lines can be added to an option by using the `--append` option. If you want to update or unset an option which can occur on multiple lines, `--value=`_< pattern>_ (which is an extended regular expression, unless the `--fixed-value` option is given) needs to be given. Only the existing values that match the pattern are updated or unset. If you want to handle the lines that do **not** match the pattern, just prepend a single exclamation mark in front (see also [EXAMPLES](https://git-scm.com/docs/git-config#EXAMPLES)), but note that this only works when the `--fixed-value` option is not in use.
The `--type=`_< type>_ option instructs _git config_ to ensure that incoming and outgoing values are canonicalize-able under the given <type>. If no `--type=`_< type>_ is given, no canonicalization will be performed. Callers may unset an existing `--type` specifier with `--no-type`.
When reading, the values are read from the system, global and repository local configuration files by default, and options `--system`, `--global`, `--local`, `--worktree` and `--file` _< filename>_ can be used to tell the command to read from only that location (see [FILES](https://git-scm.com/docs/git-config#FILES)).
When writing, the new value is written to the repository local configuration file by default, and options `--system`, `--global`, `--worktree`, `--file` _< filename>_ can be used to tell the command to write to that location (you can say `--local` but that is the default).
This command will fail with non-zero status upon error. Some exit codes are:
  * The section or key is invalid (ret=1),
  * no section or name was provided (ret=2),
  * the config file is invalid (ret=3),
  * the config file cannot be written (ret=4),
  * you try to unset an option which does not exist (ret=5),
  * you try to unset/set an option for which multiple lines match (ret=5), or
  * you try to use an invalid regexp (ret=6).


On success, the command returns the exit code 0.
A list of all available configuration variables can be obtained using the `git` `help` `--config` command.
##  [](https://git-scm.com/docs/git-config#_commands)COMMANDS 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-list)list 
    
List all variables set in config file, along with their values. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-get)get 
    
Emits the value of the specified key. If key is present multiple times in the configuration, emits the last value. If `--all` is specified, emits all values associated with key. Returns error code 1 if key is not present. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-set)set 
    
Set value for one or more config options. By default, this command refuses to write multi-valued config options. Passing `--all` will replace all multi-valued config options with the new value, whereas `--value=` will replace all config options whose values match the given pattern. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-unset)unset 
    
Unset value for one or more config options. By default, this command refuses to unset multi-valued keys. Passing `--all` will unset all multi-valued config options, whereas `--value` will unset all config options whose values match the given pattern. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rename-section)rename-section 
    
Rename the given section to a new name. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remove-section)remove-section 
    
Remove the given section from the configuration file. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-edit)edit 
    
Opens an editor to modify the specified config file; either `--system`, `--global`, `--local` (default), `--worktree`, or `--file` _< config-file>_.
##  [](https://git-scm.com/docs/git-config#OPTIONS)OPTIONS 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---replace-all)--replace-all 
    
Default behavior is to replace at most one line. This replaces all lines matching the key (and optionally `--value=`_< pattern>_). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---append)--append 
    
Adds a new line to the option without altering any existing values. This is the same as providing _--value=^$_ in `set`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---commentmessage)--comment <message> 
    
Append a comment at the end of new or modified lines.
If _< message>_ begins with one or more whitespaces followed by "", it is used as-is. If it begins with "", a space is prepended before it is used. Otherwise, a string " # " (a space followed by a hash followed by a space) is prepended to it. And the resulting string is placed immediately after the value defined for the variable. The _< message>_ must not contain linefeed characters (no multi-line comments are permitted). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---all)--all 
    
With `get`, return all values for a multi-valued key. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---regexp)--regexp 
    
With `get`, interpret the name as a regular expression. Regular expression matching is currently case-sensitive and done against a canonicalized version of the key in which section and variable names are lowercased, but subsection names are not. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---urlURL)--url=<URL> 
    
When given a two-part <name> as <section>.<key>, the value for <section>.<URL>.<key> whose <URL> part matches the best to the given URL is returned (if no such key exists, the value for <section>.<key> is used as a fallback). When given just the <section> as name, do so for all the keys in the section and list them. Returns error code 1 if no value is found. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---global)--global 
    
For writing options: write to global `~/.gitconfig` file rather than the repository `.git/config`, write to `$XDG_CONFIG_HOME/git/config` file if this file exists and the `~/.gitconfig` file doesn’t.
For reading options: read only from global `~/.gitconfig` and from `$XDG_CONFIG_HOME/git/config` rather than from all available files.
See also [FILES](https://git-scm.com/docs/git-config#FILES). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---system)--system 
    
For writing options: write to system-wide `$`(`prefix`)`/etc/gitconfig` rather than the repository `.git/config`.
For reading options: read only from system-wide `$`(`prefix`)`/etc/gitconfig` rather than from all available files.
See also [FILES](https://git-scm.com/docs/git-config#FILES). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---local)--local 
    
For writing options: write to the repository `.git/config` file. This is the default behavior.
For reading options: read only from the repository `.git/config` rather than from all available files.
See also [FILES](https://git-scm.com/docs/git-config#FILES). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---worktree)--worktree 
    
Similar to `--local` except that `$GIT_DIR/config.worktree` is read from or written to if `extensions.worktreeConfig` is enabled. If not it’s the same as `--local`. Note that `$GIT_DIR` is equal to `$GIT_COMMON_DIR` for the main working tree, but is of the form `$GIT_DIR/worktrees/`_< id>_`/` for other working trees. See [git-worktree[1]](https://git-scm.com/docs/git-worktree) to learn how to enable `extensions.worktreeConfig`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt--fconfig-file)-f <config-file> 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---fileconfig-file)--file <config-file> 
    
For writing options: write to the specified file rather than the repository `.git/config`.
For reading options: read only from the specified file rather than from all available files.
See also [FILES](https://git-scm.com/docs/git-config#FILES). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---blobblob)--blob <blob> 
    
Similar to `--file` but use the given blob instead of a file. E.g. you can use _master:.gitmodules_ to read values from the file _.gitmodules_ in the master branch. See "SPECIFYING REVISIONS" section in [gitrevisions[7]](https://git-scm.com/docs/gitrevisions) for a more complete list of ways to spell blob names. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---valuepattern)`--value=`_< pattern>_ 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---no-value)`--no-value` 
    
With `get`, `set`, and `unset`, match only against _< pattern>_. The pattern is an extended regular expression unless `--fixed-value` is given.
Use `--no-value` to unset _< pattern>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---fixed-value)--fixed-value 
    
When used with `--value=`_< pattern>_, treat _< pattern>_ as an exact string instead of a regular expression. This will restrict the name/value pairs that are matched to only those where the value is exactly equal to _< pattern>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---typetype)--type <type> 
    
_git config_ will ensure that any input or output is valid under the given type constraint(s), and will canonicalize outgoing values in _< type>_'s canonical form.
Valid _< type>_'s include:
  * _bool_ : canonicalize values `true`, `yes`,`on`, and positive numbers as "true", and values `false`, `no`, `off` and `0` as "false".
  * _int_ : canonicalize values as simple decimal numbers. An optional suffix of _k_ , _m_ , or _g_ will cause the value to be multiplied by 1024, 1048576, or 1073741824 upon input.
  * _bool-or-int_ : canonicalize according to either _bool_ or _int_ , as described above.
  * _path_ : canonicalize by expanding a leading `~` to the value of `$HOME` and `~user` to the home directory for the specified user. This specifier has no effect when setting the value (but you can use `git` `config` `section.variable` `~/` from the command line to let your shell do the expansion.)
  * _expiry-date_ : canonicalize by converting from a fixed or relative date-string to a timestamp. This specifier has no effect when setting the value.
  * _color_ : When getting a value, canonicalize by converting to an ANSI color escape sequence. When setting a value, a sanity-check is performed to ensure that the given value is canonicalize-able as an ANSI color, but it is written as-is.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---bool)--bool 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---int)--int 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---bool-or-int)--bool-or-int 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---path)--path 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---expiry-date)--expiry-date 
    
Historical options for selecting a type specifier. Prefer instead `--type` (see above). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---no-type)--no-type 
    
Un-sets the previously set type specifier (if one was previously set). This option requests that _git config_ not canonicalize the retrieved variable. `--no-type` has no effect without `--type=`_< type>_ or `--`_< type>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt--z)-z 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---null)--null 
    
For all options that output values and/or keys, always end values with the null character (instead of a newline). Use newline instead as a delimiter between key and value. This allows for secure parsing of the output without getting confused e.g. by values that contain line breaks. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---name-only)--name-only 
    
Output only the names of config variables for `list` or `get`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---show-names)`--show-names` 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---no-show-names)`--no-show-names` 
    
With `get`, show config keys in addition to their values. The default is `--no-show-names` unless `--url` is given and there are no subsections in _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---show-origin)--show-origin 
    
Augment the output of all queried config options with the origin type (file, standard input, blob, command line) and the actual origin (config file path, ref, or blob id if applicable). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---show-scope)--show-scope 
    
Similar to `--show-origin` in that it augments the output of all queried config options with the scope of that value (worktree, local, global, system, command). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---get-colorboolnamestdout-is-tty)--get-colorbool <name> [<stdout-is-tty>] 
    
Find the color setting for _< name>_ (e.g. `color.diff`) and output "true" or "false". _< stdout-is-tty>_ should be either "true" or "false", and is taken into account when configuration says "auto". If _< stdout-is-tty>_ is missing, then checks the standard output of the command itself, and exits with status 0 if color is to be used, or exits with status 1 otherwise. When the color setting for `name` is undefined, the command uses `color.ui` as fallback. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---includes)--includes 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---no-includes)--no-includes 
    
Respect `include.*` directives in config files when looking up values. Defaults to `off` when a specific file is given (e.g., using `--file`, `--global`, etc) and `on` when searching all config files. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---defaultvalue)--default <value> 
    
When using `get`, and the requested variable is not found, behave as if <value> were the value assigned to that variable.
##  [](https://git-scm.com/docs/git-config#_deprecated_modes)DEPRECATED MODES
The following modes have been deprecated in favor of subcommands. It is recommended to migrate to the new syntax. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitconfigname)_git config <name>_ 
    
Replaced by `git` `config` `get` _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitconfignamevaluevalue-pattern)_git config <name> <value> [<value-pattern>]_ 
    
Replaced by `git` `config` `set` [`--value=`_< pattern>_] _< name>_ _< value>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt--l)-l 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---list)--list 
    
Replaced by `git` `config` `list`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---getnamevalue-pattern)--get <name> [<value-pattern>] 
    
Replaced by `git` `config` `get` [`--value=`_< pattern>_] _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---get-allnamevalue-pattern)--get-all <name> [<value-pattern>] 
    
Replaced by `git` `config` `get` [`--value=`_< pattern>_] `--all` _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---get-regexpname-regexp)--get-regexp <name-regexp> 
    
Replaced by `git` `config` `get` `--all` `--show-names` `--regexp` _< name-regexp>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---get-urlmatchnameURL)--get-urlmatch <name> <URL> 
    
Replaced by `git` `config` `get` `--url=`_< URL>_ _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---get-colornamedefault)--get-color <name> [<default>] 
    
Replaced by `git` `config` `get` `--type=color` [`--default=`_< default>_] _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---addnamevalue)--add <name> <value> 
    
Replaced by `git` `config` `set` `--append` _< name>_ _< value>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---unsetnamevalue-pattern)--unset <name> [<value-pattern>] 
    
Replaced by `git` `config` `unset` [`--value=`_< pattern>_] _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---unset-allnamevalue-pattern)--unset-all <name> [<value-pattern>] 
    
Replaced by `git` `config` `unset` [`--value=`_< pattern>_] `--all` _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---rename-sectionold-namenew-name)--rename-section <old-name> <new-name> 
    
Replaced by `git` `config` `rename-section` _< old-name>_ _< new-name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---remove-sectionname)--remove-section <name> 
    
Replaced by `git` `config` `remove-section` _< name>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt--e)-e 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt---edit)--edit 
    
Replaced by `git` `config` `edit`.
##  [](https://git-scm.com/docs/git-config#_configuration)CONFIGURATION
`pager.config` is only respected when listing configuration, i.e., when using `list` or `get` which may return multiple results. The default is to use a pager.
##  [](https://git-scm.com/docs/git-config#FILES)FILES
By default, _git config_ will read configuration options from multiple files: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-prefixetcgitconfig)$(prefix)/etc/gitconfig 
    
System-wide configuration file. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-XDGCONFIGHOMEgitconfig)$XDG_CONFIG_HOME/git/config 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitconfig)~/.gitconfig 
    
User-specific configuration files. When the XDG_CONFIG_HOME environment variable is not set or empty, $HOME/.config/ is used as $XDG_CONFIG_HOME.
These are also called "global" configuration files. If both files exist, both files are read in the order given above. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITDIRconfig)$GIT_DIR/config 
    
Repository specific configuration file. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITDIRconfigworktree)$GIT_DIR/config.worktree 
    
This is optional and is only searched when `extensions.worktreeConfig` is present in $GIT_DIR/config.
You may also provide additional configuration parameters when running any git command by using the `-c` option. See [git[1]](https://git-scm.com/docs/git) for details.
Options will be read from all of these files that are available. If the global or the system-wide configuration files are missing or unreadable they will be ignored. If the repository configuration file is missing or unreadable, _git config_ will exit with a non-zero error code. An error message is produced if the file is unreadable, but not if it is missing.
The files are read in the order given above, with last value found taking precedence over values read earlier. When multiple values are taken then all values of a key from all files will be used.
By default, options are only written to the repository specific configuration file. Note that this also affects options like `set` and `unset`. **_git config_ will only ever change one file at a time**.
You can limit which configuration sources are read from or written to by specifying the path of a file with the `--file` option, or by specifying a configuration scope with `--system`, `--global`, `--local`, or `--worktree`. For more, see [OPTIONS](https://git-scm.com/docs/git-config#OPTIONS) above.
##  [](https://git-scm.com/docs/git-config#SCOPES)SCOPES
Each configuration source falls within a configuration scope. The scopes are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-system)system 
    
$(prefix)/etc/gitconfig 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-global)global 
    
$XDG_CONFIG_HOME/git/config
~/.gitconfig 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-local)local 
    
$GIT_DIR/config 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-worktree)worktree 
    
$GIT_DIR/config.worktree 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-command)command 
    
GIT_CONFIG_{COUNT,KEY,VALUE} environment variables (see [ENVIRONMENT](https://git-scm.com/docs/git-config#ENVIRONMENT) below)
the `-c` option
With the exception of _command_ , each scope corresponds to a command line option: `--system`, `--global`, `--local`, `--worktree`.
When reading options, specifying a scope will only read options from the files within that scope. When writing options, specifying a scope will write to the files within that scope (instead of the repository specific configuration file). See [OPTIONS](https://git-scm.com/docs/git-config#OPTIONS) above for a complete description.
Most configuration options are respected regardless of the scope it is defined in, but some options are only respected in certain scopes. See the respective option’s documentation for the full details.
###  [](https://git-scm.com/docs/git-config#_protected_configuration)Protected configuration
Protected configuration refers to the _system_ , _global_ , and _command_ scopes. For security reasons, certain options are only respected when they are specified in protected configuration, and ignored otherwise.
Git treats these scopes as if they are controlled by the user or a trusted administrator. This is because an attacker who controls these scopes can do substantial harm without using Git, so it is assumed that the user’s environment protects these scopes against attackers.
##  [](https://git-scm.com/docs/git-config#ENVIRONMENT)ENVIRONMENT 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIGGLOBAL)GIT_CONFIG_GLOBAL 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIGSYSTEM)GIT_CONFIG_SYSTEM 
    
Take the configuration from the given files instead from global or system-level configuration. See [git[1]](https://git-scm.com/docs/git) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIGNOSYSTEM)GIT_CONFIG_NOSYSTEM 
    
Whether to skip reading settings from the system-wide $(prefix)/etc/gitconfig file. See [git[1]](https://git-scm.com/docs/git) for details.
See also [FILES](https://git-scm.com/docs/git-config#FILES). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIGCOUNT)GIT_CONFIG_COUNT 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIGKEYn)GIT_CONFIG_KEY_<n> 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIGVALUEn)GIT_CONFIG_VALUE_<n> 
    
If GIT_CONFIG_COUNT is set to a positive number, all environment pairs GIT_CONFIG_KEY_<n> and GIT_CONFIG_VALUE_<n> up to that number will be added to the process’s runtime configuration. The config pairs are zero-indexed. Any missing key or value is treated as an error. An empty GIT_CONFIG_COUNT is treated the same as GIT_CONFIG_COUNT=0, namely no pairs are processed. These environment variables will override values in configuration files, but will be overridden by any explicit options passed via `git` `-c`.
This is useful for cases where you want to spawn multiple git commands with a common configuration but cannot depend on a configuration file, for example when writing scripts. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-GITCONFIG)GIT_CONFIG 
    
If no `--file` option is provided to `git` `config`, use the file given by `GIT_CONFIG` as if it were provided via `--file`. This variable has no effect on other Git commands, and is mostly for historical compatibility; there is generally no reason to use it instead of the `--file` option.
##  [](https://git-scm.com/docs/git-config#EXAMPLES)EXAMPLES
Given a .git/config like this:
```
#
# This is the config file, and
# a '#' or ';' character indicates
# a comment
#

; core variables
[core]
	; Don't trust file modes
	filemode = false

; Our diff algorithm
[diff]
	external = /usr/local/bin/diff-wrapper
	renames = true

; Proxy settings
[core]
	gitproxy=proxy-command for kernel.org
	gitproxy=default-proxy ; for all the rest

; HTTP
[http]
	sslVerify
[http "https://weak.example.com"]
	sslVerify = false
	cookieFile = /tmp/cookie.txt
```

you can set the filemode to true with
```
% git config set core.filemode true
```

The hypothetical proxy command entries actually have a postfix to discern what URL they apply to. Here is how to change the entry for kernel.org to "ssh".
```
% git config set --value='for kernel.org$' core.gitproxy '"ssh" for kernel.org'
```

This makes sure that only the key/value pair for kernel.org is replaced.
To delete the entry for renames, do
```
% git config unset diff.renames
```

If you want to delete an entry for a multivar (like core.gitproxy above), you have to provide a regex matching the value of exactly one line.
To query the value for a given key, do
```
% git config get core.filemode
```

or, to query a multivar:
```
% git config get --value="for kernel.org$" core.gitproxy
```

If you want to know all the values for a multivar, do:
```
% git config get --all --show-names core.gitproxy
```

If you like to live dangerously, you can replace **all** core.gitproxy by a new one with
```
% git config set --all core.gitproxy ssh
```

However, if you really only want to replace the line for the default proxy, i.e. the one without a "for …​" postfix, do something like this:
```
% git config set --value='! for ' core.gitproxy ssh
```

To actually match only values with an exclamation mark, you have to
```
% git config set --value='[!]' section.key value
```

To add a new proxy, without altering any of the existing ones, use
```
% git config set --append core.gitproxy '"proxy-command" for example.com'
```

An example to use customized color from the configuration in your script:
```
#!/bin/sh
WS=$(git config get --type=color --default="blue reverse" color.diff.whitespace)
RESET=$(git config get --type=color --default="reset" "")
echo "${WS}your whitespace color or blue reverse${RESET}"
```

For URLs in `https://weak.example.com`, `http.sslVerify` is set to false, while it is set to `true` for all others:
```
% git config get --type=bool --url=https://good.example.com http.sslverify
true
% git config get --type=bool --url=https://weak.example.com http.sslverify
false
% git config get --url=https://weak.example.com http
http.cookieFile /tmp/cookie.txt
http.sslverify false
```

##  [](https://git-scm.com/docs/git-config#_configuration_file)CONFIGURATION FILE
The Git configuration file contains a number of variables that affect the Git commands' behavior. The files `.git/config` and optionally `config.worktree` (see the "CONFIGURATION FILE" section of [git-worktree[1]](https://git-scm.com/docs/git-worktree)) in each repository are used to store the configuration for that repository, and `$HOME/.gitconfig` is used to store a per-user configuration as fallback values for the `.git/config` file. The file `/etc/gitconfig` can be used to store a system-wide default configuration.
The configuration variables are used by both the Git plumbing and the porcelain commands. The variables are divided into sections, wherein the fully qualified variable name of the variable itself is the last dot-separated segment and the section name is everything before the last dot. The variable names are case-insensitive, allow only alphanumeric characters and `-`, and must start with an alphabetic character. Some variables may appear multiple times; we say then that the variable is multivalued.
###  [](https://git-scm.com/docs/git-config#_syntax)Syntax
The syntax is fairly flexible and permissive. Whitespace characters, which in this context are the space character (SP) and the horizontal tabulation (HT), are mostly ignored. The _#_ and _;_ characters begin comments to the end of line. Blank lines are ignored.
The file consists of sections and variables. A section begins with the name of the section in square brackets and continues until the next section begins. Section names are case-insensitive. Only alphanumeric characters, `-` and `.` are allowed in section names. Each variable must belong to some section, which means that there must be a section header before the first setting of a variable.
Sections can be further divided into subsections. To begin a subsection put its name in double quotes, separated by space from the section name, in the section header, like in the example below:
```
	[section "subsection"]
```

Subsection names are case sensitive and can contain any characters except newline and the null byte. Doublequote `"` and backslash can be included by escaping them as _\"_ and _\\\_ , respectively. Backslashes preceding other characters are dropped when reading; for example, _\t_ is read as `t` and _\0_ is read as `0`. Section headers cannot span multiple lines. Variables may belong directly to a section or to a given subsection. You can have [`section`] if you have [`section` `"subsection"`], but you don’t need to.
There is also a deprecated [`section.subsection`] syntax. With this syntax, the subsection name is converted to lower-case and is also compared case sensitively. These subsection names follow the same restrictions as section names.
All the other lines (and the remainder of the line after the section header) are recognized as setting variables, in the form _name = value_ (or just _name_ , which is a short-hand to say that the variable is the boolean "true"). The variable names are case-insensitive, allow only alphanumeric characters and `-`, and must start with an alphabetic character.
Whitespace characters surrounding `name`, `=` and `value` are discarded. Internal whitespace characters within _value_ are retained verbatim. Comments starting with either `#` or _;_ and extending to the end of line are discarded. A line that defines a value can be continued to the next line by ending it with a backslash (_\_); the backslash and the end-of-line characters are discarded.
If `value` needs to contain leading or trailing whitespace characters, it must be enclosed in double quotation marks (`"`). Inside double quotation marks, double quote (`"`) and backslash (_\_) characters must be escaped: use _\"_ for `"` and _\\\_ for _\_.
The following escape sequences (beside _\"_ and _\\\_) are recognized: _\n_ for newline character (NL), _\t_ for horizontal tabulation (HT, TAB) and _\b_ for backspace (BS). Other char escape sequences (including octal escape sequences) are invalid.
###  [](https://git-scm.com/docs/git-config#_includes)Includes
The `include` and `includeIf` sections allow you to include config directives from another source. These sections behave identically to each other with the exception that `includeIf` sections may be ignored if their condition does not evaluate to true; see "Conditional includes" below.
You can include a config file from another by setting the special `include.path` (or `includeIf.*.path`) variable to the name of the file to be included. The variable takes a pathname as its value, and is subject to tilde expansion. These variables can be given multiple times.
The contents of the included file are inserted immediately, as if they had been found at the location of the include directive. If the value of the variable is a relative path, the path is considered to be relative to the configuration file in which the include directive was found. See below for examples.
###  [](https://git-scm.com/docs/git-config#_conditional_includes)Conditional includes
You can conditionally include a config file from another by setting an `includeIf.`_< condition>_`.path` variable to the name of the file to be included.
The condition starts with a keyword followed by a colon and some data whose format and meaning depends on the keyword. Supported keywords are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitdir)`gitdir` 
    
The data that follows the keyword `gitdir` and a colon is used as a glob pattern. If the location of the .git directory matches the pattern, the include condition is met.
The .git location may be auto-discovered, or come from `$GIT_DIR` environment variable. If the repository is auto-discovered via a .git file (e.g. from submodules, or a linked worktree), the .git location would be the final location where the .git directory is, not where the .git file is.
The pattern can contain standard globbing wildcards and two additional ones, `**/` and `/**`, that can match multiple path components. Please refer to [gitignore[5]](https://git-scm.com/docs/gitignore) for details. For convenience:
  * If the pattern starts with `~/`, `~` will be substituted with the content of the environment variable `HOME`.
  * If the pattern starts with `./`, it is replaced with the directory containing the current config file.
  * If the pattern does not start with either `~/`, `./` or `/`, `**/` will be automatically prepended. For example, the pattern `foo/bar` becomes `**/foo/bar` and would match `/any/path/to/foo/bar`.
  * If the pattern ends with `/`, `**` will be automatically added. For example, the pattern `foo/` becomes `foo/**`. In other words, it matches "foo" and everything inside, recursively.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitdiri)`gitdir/i` 
    
This is the same as `gitdir` except that matching is done case-insensitively (e.g. on case-insensitive file systems) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-onbranch)`onbranch` 
    
The data that follows the keyword `onbranch` and a colon is taken to be a pattern with standard globbing wildcards and two additional ones, `**/` and `/**`, that can match multiple path components. If we are in a worktree where the name of the branch that is currently checked out matches the pattern, the include condition is met.
If the pattern ends with `/`, `**` will be automatically added. For example, the pattern `foo/` becomes `foo/**`. In other words, it matches all branches that begin with `foo/`. This is useful if your branches are organized hierarchically and you would like to apply a configuration to all the branches in that hierarchy. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-hasconfigremoteurl)`hasconfig:remote.*.url` 
    
The data that follows this keyword and a colon is taken to be a pattern with standard globbing wildcards and two additional ones, `**/` and `/**`, that can match multiple components. The first time this keyword is seen, the rest of the config files will be scanned for remote URLs (without applying any values). If there exists at least one remote URL that matches this pattern, the include condition is met.
Files included by this option (directly or indirectly) are not allowed to contain remote URLs.
Note that unlike other includeIf conditions, resolving this condition relies on information that is not yet known at the point of reading the condition. A typical use case is this option being present as a system-level or global-level config, and the remote URL being in a local-level config; hence the need to scan ahead when resolving this condition. In order to avoid the chicken-and-egg problem in which potentially-included files can affect whether such files are potentially included, Git breaks the cycle by prohibiting these files from affecting the resolution of these conditions (thus, prohibiting them from declaring remote URLs).
As for the naming of this keyword, it is for forwards compatibility with a naming scheme that supports more variable-based include conditions, but currently Git only supports the exact keyword described above.
A few more notes on matching via `gitdir` and `gitdir/i`:
  * Symlinks in `$GIT_DIR` are not resolved before matching.
  * Both the symlink & realpath versions of paths will be matched outside of `$GIT_DIR`. E.g. if ~/git is a symlink to /mnt/storage/git, both `gitdir:~/git` and `gitdir:/mnt/storage/git` will match.
This was not the case in the initial release of this feature in v2.13.0, which only matched the realpath version. Configuration that wants to be compatible with the initial release of this feature needs to either specify only the realpath version, or both versions.
  * Note that "../" is not special and will match literally, which is unlikely what you want.


###  [](https://git-scm.com/docs/git-config#_example)Example
```
# Core variables
[core]
	; Don't trust file modes
	filemode = false

# Our diff algorithm
[diff]
	external = /usr/local/bin/diff-wrapper
	renames = true

[branch "devel"]
	remote = origin
	merge = refs/heads/devel

# Proxy settings
[core]
	gitProxy="ssh" for "kernel.org"
	gitProxy=default-proxy ; for the rest

[include]
	path = /path/to/foo.inc ; include by absolute path
	path = foo.inc ; find "foo.inc" relative to the current file
	path = ~/foo.inc ; find "foo.inc" in your `$HOME` directory

; include if $GIT_DIR is /path/to/foo/.git
[includeIf "gitdir:/path/to/foo/.git"]
	path = /path/to/foo.inc

; include for all repositories inside /path/to/group
[includeIf "gitdir:/path/to/group/"]
	path = /path/to/foo.inc

; include for all repositories inside $HOME/to/group
[includeIf "gitdir:~/to/group/"]
	path = /path/to/foo.inc

; relative paths are always relative to the including
; file (if the condition is true); their location is not
; affected by the condition
[includeIf "gitdir:/path/to/group/"]
	path = foo.inc

; include only if we are in a worktree where foo-branch is
; currently checked out
[includeIf "onbranch:foo-branch"]
	path = foo.inc

; include only if a remote with the given URL exists (note
; that such a URL may be provided later in a file or in a
; file read after this file is read, as seen in this example)
[includeIf "hasconfig:remote.*.url:https://example.com/**"]
	path = foo.inc
[remote "origin"]
	url = https://example.com/git
```

###  [](https://git-scm.com/docs/git-config#_values)Values
Values of many variables are treated as a simple string, but there are variables that take values of specific types and there are rules as to how to spell them. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-boolean)boolean 
    
When a variable is said to take a boolean value, many synonyms are accepted for _true_ and _false_ ; these are all case-insensitive. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-true)true 
    
Boolean true literals are `yes`, `on`, `true`, and `1`. Also, a variable defined without `=` _< value>_ is taken as true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-false)false 
    
Boolean false literals are `no`, `off`, `false`, `0` and the empty string.
When converting a value to its canonical form using the `--type=bool` type specifier, _git config_ will ensure that the output is "true" or "false" (spelled in lowercase). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-integer)integer 
    
The value for many variables that specify various sizes can be suffixed with `k`, `M`,…​ to mean "scale the number by 1024", "by 1024x1024", etc. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-color)color 
    
The value for a variable that takes a color is a list of colors (at most two, one for foreground and one for background) and attributes (as many as you want), separated by spaces.
The basic colors accepted are `normal`, `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white` and `default`. The first color given is the foreground; the second is the background. All the basic colors except `normal` and `default` have a bright variant that can be specified by prefixing the color with `bright`, like `brightred`.
The color `normal` makes no change to the color. It is the same as an empty string, but can be used as the foreground color when specifying a background color alone (for example, "normal red").
The color `default` explicitly resets the color to the terminal default, for example to specify a cleared background. Although it varies between terminals, this is usually not the same as setting to "white black".
Colors may also be given as numbers between 0 and 255; these use ANSI 256-color mode (but note that not all terminals may support this). If your terminal supports it, you may also specify 24-bit RGB values as hex, like `#ff0ab3`, or 12-bit RGB values like `#f1b`, which is equivalent to the 24-bit color `#ff11bb`.
The accepted attributes are `bold`, `dim`, `ul`, `blink`, `reverse`, `italic`, and `strike` (for crossed-out or "strikethrough" letters). The position of any attributes with respect to the colors (before, after, or in between), doesn’t matter. Specific attributes may be turned off by prefixing them with `no` or `no-` (e.g., `noreverse`, `no-ul`, etc).
The pseudo-attribute `reset` resets all colors and attributes before applying the specified coloring. For example, `reset` `green` will result in a green foreground and default background without any active attributes.
An empty color string produces no color effect at all. This can be used to avoid coloring specific elements without disabling color entirely.
For git’s pre-defined color slots, the attributes are meant to be reset at the beginning of each item in the colored output. So setting `color.decorate.branch` to `black` will paint that branch name in a plain `black`, even if the previous thing on the same output line (e.g. opening parenthesis before the list of branch names in `log` `--decorate` output) is set to be painted with `bold` or some other attribute. However, custom log formats may do more complicated and layered coloring, and the negated forms may be useful there. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pathname)pathname 
    
A variable that takes a pathname value can be given a string that begins with "`~/`" or "`~user/`", and the usual tilde expansion happens to such a string: `~/` is expanded to the value of `$HOME`, and `~user/` to the specified user’s home directory.
If a path starts with `%`(`prefix`)`/`, the remainder is interpreted as a path relative to Git’s "runtime prefix", i.e. relative to the location where Git itself was installed. For example, `%`(`prefix`)`/bin/` refers to the directory in which the Git executable itself lives. If Git was compiled without runtime prefix support, the compiled-in prefix will be substituted instead. In the unlikely event that a literal path needs to be specified that should _not_ be expanded, it needs to be prefixed by `./`, like so: `./%`(`prefix`)`/bin`.
If prefixed with `:`(`optional`), the configuration variable is treated as if it does not exist, if the named path does not exist.
###  [](https://git-scm.com/docs/git-config#_variables)Variables
Note that this list is non-comprehensive and not necessarily complete. For command-specific variables, you will find a more detailed description in the appropriate manual page.
Other git-related tools may and do use their own variables. When inventing new variables for use in your own tool, make sure their names do not conflict with those that are used by Git itself and other popular tools, and describe them in your documentation. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-addignoreErrors)`add.ignoreErrors` 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-addignore-errorsdeprecated)`add.ignore-errors` (deprecated) 
    
Tells `git` `add` to continue adding files when some files cannot be added due to indexing errors. Equivalent to the `--ignore-errors` option of [git-add[1]](https://git-scm.com/docs/git-add). `add.ignore-errors` is deprecated, as it does not follow the usual naming convention for configuration variables. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-advice)advice.* 
    
These variables control various optional help messages designed to aid new users. When left unconfigured, Git will give the message alongside instructions on how to squelch it. You can tell Git that you have understood the issue and no longer need a specific help message by setting the corresponding variable to `false`.
As they are intended to help human users, these messages are output to the standard error. When tools that run Git as a subprocess find them disruptive, they can set `GIT_ADVICE=0` in the environment to squelch all advice messages. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-addEmbeddedRepo)addEmbeddedRepo 
    
Shown when the user accidentally adds one git repo inside of another. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-addEmptyPathspec)addEmptyPathspec 
    
Shown when the user runs `git` `add` without providing the pathspec parameter. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-addIgnoredFile)addIgnoredFile 
    
Shown when the user attempts to add an ignored file to the index. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-amWorkDir)amWorkDir 
    
Shown when [git-am[1]](https://git-scm.com/docs/git-am) fails to apply a patch file, to tell the user the location of the file. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-ambiguousFetchRefspec)ambiguousFetchRefspec 
    
Shown when a fetch refspec for multiple remotes maps to the same remote-tracking branch namespace and causes branch tracking set-up to fail. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-checkoutAmbiguousRemoteBranchName)checkoutAmbiguousRemoteBranchName 
    
Shown when the argument to [git-checkout[1]](https://git-scm.com/docs/git-checkout) and [git-switch[1]](https://git-scm.com/docs/git-switch) ambiguously resolves to a remote tracking branch on more than one remote in situations where an unambiguous argument would have otherwise caused a remote-tracking branch to be checked out. See the `checkout.defaultRemote` configuration variable for how to set a given remote to be used by default in some situations where this advice would be printed. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitBeforeMerge)commitBeforeMerge 
    
Shown when [git-merge[1]](https://git-scm.com/docs/git-merge) refuses to merge to avoid overwriting local changes. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-detachedHead)detachedHead 
    
Shown when the user uses [git-switch[1]](https://git-scm.com/docs/git-switch) or [git-checkout[1]](https://git-scm.com/docs/git-checkout) to move to the detached HEAD state, to tell the user how to create a local branch after the fact. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diverging)diverging 
    
Shown when a fast-forward is not possible. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchShowForcedUpdates)fetchShowForcedUpdates 
    
Shown when [git-fetch[1]](https://git-scm.com/docs/git-fetch) takes a long time to calculate forced updates after ref updates, or to warn that the check is disabled. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-forceDeleteBranch)forceDeleteBranch 
    
Shown when the user tries to delete a not fully merged branch without the force option set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-ignoredHook)ignoredHook 
    
Shown when a hook is ignored because the hook is not set as executable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-implicitIdentity)implicitIdentity 
    
Shown when the user’s information is guessed from the system username and domain name, to tell the user how to set their identity configuration. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeConflict)mergeConflict 
    
Shown when various commands stop because of conflicts. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-nestedTag)nestedTag 
    
Shown when a user attempts to recursively tag a tag object. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushAlreadyExists)pushAlreadyExists 
    
Shown when [git-push[1]](https://git-scm.com/docs/git-push) rejects an update that does not qualify for fast-forwarding (e.g., a tag.) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushFetchFirst)pushFetchFirst 
    
Shown when [git-push[1]](https://git-scm.com/docs/git-push) rejects an update that tries to overwrite a remote ref that points at an object we do not have. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushNeedsForce)pushNeedsForce 
    
Shown when [git-push[1]](https://git-scm.com/docs/git-push) rejects an update that tries to overwrite a remote ref that points at an object that is not a commit-ish, or make the remote ref point at an object that is not a commit-ish. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushNonFFCurrent)pushNonFFCurrent 
    
Shown when [git-push[1]](https://git-scm.com/docs/git-push) fails due to a non-fast-forward update to the current branch. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushNonFFMatching)pushNonFFMatching 
    
Shown when the user ran [git-push[1]](https://git-scm.com/docs/git-push) and pushed "matching refs" explicitly (i.e. used `:`, or specified a refspec that isn’t the current branch) and it resulted in a non-fast-forward error. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushRefNeedsUpdate)pushRefNeedsUpdate 
    
Shown when [git-push[1]](https://git-scm.com/docs/git-push) rejects a forced update of a branch when its remote-tracking ref has updates that we do not have locally. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushUnqualifiedRefname)pushUnqualifiedRefname 
    
Shown when [git-push[1]](https://git-scm.com/docs/git-push) gives up trying to guess based on the source and destination refs what remote ref namespace the source belongs in, but where we can still suggest that the user push to either `refs/heads/*` or `refs/tags/*` based on the type of the source object. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushUpdateRejected)pushUpdateRejected 
    
Set this variable to `false` if you want to disable `pushNonFFCurrent`, `pushNonFFMatching`, `pushAlreadyExists`, `pushFetchFirst`, `pushNeedsForce`, and `pushRefNeedsUpdate` simultaneously. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseTodoError)rebaseTodoError 
    
Shown when there is an error after editing the rebase todo list. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-refSyntax)refSyntax 
    
Shown when the user provides an illegal ref name, to tell the user about the ref syntax documentation. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-resetNoRefresh)resetNoRefresh 
    
Shown when [git-reset[1]](https://git-scm.com/docs/git-reset) takes more than 2 seconds to refresh the index after reset, to tell the user that they can use the `--no-refresh` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-resolveConflict)resolveConflict 
    
Shown by various commands when conflicts prevent the operation from being performed. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rmHints)rmHints 
    
Shown on failure in the output of [git-rm[1]](https://git-scm.com/docs/git-rm), to give directions on how to proceed from the current state. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sequencerInUse)sequencerInUse 
    
Shown when a sequencer command is already in progress. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-skippedCherryPicks)skippedCherryPicks 
    
Shown when [git-rebase[1]](https://git-scm.com/docs/git-rebase) skips a commit that has already been cherry-picked onto the upstream branch. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sparseIndexExpanded)sparseIndexExpanded 
    
Shown when a sparse index is expanded to a full index, which is likely due to an unexpected set of files existing outside of the sparse-checkout. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusAheadBehind)statusAheadBehind 
    
Shown when [git-status[1]](https://git-scm.com/docs/git-status) computes the ahead/behind counts for a local ref compared to its remote tracking ref, and that calculation takes longer than expected. Will not appear if `status.aheadBehind` is false or the option `--no-ahead-behind` is given. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusHints)statusHints 
    
Show directions on how to proceed from the current state in the output of [git-status[1]](https://git-scm.com/docs/git-status), in the template shown when writing commit messages in [git-commit[1]](https://git-scm.com/docs/git-commit), and in the help message shown by [git-switch[1]](https://git-scm.com/docs/git-switch) or [git-checkout[1]](https://git-scm.com/docs/git-checkout) when switching branches. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusUoption)statusUoption 
    
Shown when [git-status[1]](https://git-scm.com/docs/git-status) takes more than 2 seconds to enumerate untracked files, to tell the user that they can use the `-u` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submoduleAlternateErrorStrategyDie)submoduleAlternateErrorStrategyDie 
    
Shown when a submodule.alternateErrorStrategy option configured to "die" causes a fatal error. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submoduleMergeConflict)submoduleMergeConflict 
    
Advice shown when a non-trivial submodule merge conflict is encountered. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulesNotUpdated)submodulesNotUpdated 
    
Shown when a user runs a submodule command that fails because `git` `submodule` `update` `--init` was not run. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-suggestDetachingHead)suggestDetachingHead 
    
Shown when [git-switch[1]](https://git-scm.com/docs/git-switch) refuses to detach HEAD without the explicit `--detach` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-updateSparsePath)updateSparsePath 
    
Shown when either [git-add[1]](https://git-scm.com/docs/git-add) or [git-rm[1]](https://git-scm.com/docs/git-rm) is asked to update index entries outside the current sparse checkout. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-waitingForEditor)waitingForEditor 
    
Shown when Git is waiting for editor input. Relevant when e.g. the editor is not launched inside the terminal. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-worktreeAddOrphan)worktreeAddOrphan 
    
Shown when the user tries to create a worktree from an invalid reference, to tell the user how to create a new unborn branch instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-alias)alias.* 
    
Command aliases for the [git[1]](https://git-scm.com/docs/git) command wrapper - e.g. after defining `alias.last` `=` `cat-file` `commit` `HEAD`, the invocation `git` `last` is equivalent to `git` `cat-file` `commit` `HEAD`. To avoid confusion and troubles with script usage, aliases that hide existing Git commands are ignored except for deprecated commands. Arguments are split by spaces, the usual shell quoting and escaping are supported. A quote pair or a backslash can be used to quote them.
Note that the first word of an alias does not necessarily have to be a command. It can be a command-line option that will be passed into the invocation of `git`. In particular, this is useful when used with `-c` to pass in one-time configurations or `-p` to force pagination. For example, `loud-rebase` `=` `-c` `commit.verbose=true` `rebase` can be defined such that running `git` `loud-rebase` would be equivalent to `git` `-c` `commit.verbose=true` `rebase`. Also, `ps` `=` `-p` `status` would be a helpful alias since `git` `ps` would paginate the output of `git` `status` where the original command does not.
If the alias expansion is prefixed with an exclamation point, it will be treated as a shell command. For example, defining `alias.new` `=` `!gitk` `--all` `--not` `ORIG_HEAD`, the invocation `git` `new` is equivalent to running the shell command `gitk` `--all` `--not` `ORIG_HEAD`. Note:
  * Shell commands will be executed from the top-level directory of a repository, which may not necessarily be the current directory.
  * `GIT_PREFIX` is set as returned by running `git` `rev-parse` `--show-prefix` from the original current directory. See [git-rev-parse[1]](https://git-scm.com/docs/git-rev-parse).
  * Shell command aliases always receive any extra arguments provided to the Git command-line as positional arguments.
    * Care should be taken if your shell alias is a "one-liner" script with multiple commands (e.g. in a pipeline), references multiple arguments, or is otherwise not able to handle positional arguments added at the end. For example: `alias.cmd` `=` `"!echo` `$1` | `grep` `$2"` called as `git` `cmd` `1` `2` will be executed as _echo $1 | grep $2 1 2_ , which is not what you want.
    * A convenient way to deal with this is to write your script operations in an inline function that is then called with any arguments from the command-line. For example _alias.cmd = "!c() {_ _echo $1 | grep $2 ; }; c"_ will correctly execute the prior example.
    * Setting `GIT_TRACE=1` can help you debug the command being run for your alias.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-amkeepcr)am.keepcr 
    
If true, git-am will call git-mailsplit for patches in mbox format with parameter `--keep-cr`. In this case git-mailsplit will not remove _\r_ from lines ending with _\r\n_. Can be overridden by giving `--no-keep-cr` from the command line. See [git-am[1]](https://git-scm.com/docs/git-am), [git-mailsplit[1]](https://git-scm.com/docs/git-mailsplit). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-amthreeWay)am.threeWay 
    
By default, `git` `am` will fail if the patch does not apply cleanly. When set to true, this setting tells `git` `am` to fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally (equivalent to giving the `--3way` option from the command line). Defaults to `false`. See [git-am[1]](https://git-scm.com/docs/git-am). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-applyignoreWhitespace)apply.ignoreWhitespace 
    
When set to _change_ , tells _git apply_ to ignore changes in whitespace, in the same way as the `--ignore-space-change` option. When set to one of: no, none, never, false, it tells _git apply_ to respect all whitespace differences. See [git-apply[1]](https://git-scm.com/docs/git-apply). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-applywhitespace)apply.whitespace 
    
Tells _git apply_ how to handle whitespace, in the same way as the `--whitespace` option. See [git-apply[1]](https://git-scm.com/docs/git-apply). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-attrtree)attr.tree 
    
A reference to a tree in the repository from which to read attributes, instead of the `.gitattributes` file in the working tree. If the value does not resolve to a valid tree object, an empty tree is used instead. When the `GIT_ATTR_SOURCE` environment variable or `--attr-source` command line option are used, this configuration variable has no effect.
Note |  The configuration options in `bitmapPseudoMerge.*` are considered EXPERIMENTAL and may be subject to change or be removed entirely in the future. For more information about the pseudo-merge bitmap feature, see the "Pseudo-merge bitmaps" section of [gitpacking[7]](https://git-scm.com/docs/gitpacking).   
---|--- 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bitmapPseudoMergenamepattern)bitmapPseudoMerge.<name>.pattern 
      
Regular expression used to match reference names. Commits pointed to by references matching this pattern (and meeting the below criteria, like `bitmapPseudoMerge.`_< name>_`.sampleRate` and `bitmapPseudoMerge.`_< name>_`.threshold`) will be considered for inclusion in a pseudo-merge bitmap.
Commits are grouped into pseudo-merge groups based on whether or not any reference(s) that point at a given commit match the pattern, which is an extended regular expression.
Within a pseudo-merge group, commits may be further grouped into sub-groups based on the capture groups in the pattern. These sub-groupings are formed from the regular expressions by concatenating any capture groups from the regular expression, with a _-_ dash in between.
For example, if the pattern is `refs/tags/`, then all tags (provided they meet the below criteria) will be considered candidates for the same pseudo-merge group. However, if the pattern is instead `refs/remotes/`([`0-9`])`+/tags/`, then tags from different remotes will be grouped into separate pseudo-merge groups, based on the remote number. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bitmapPseudoMergenamedecay)bitmapPseudoMerge.<name>.decay 
    
Determines the rate at which consecutive pseudo-merge bitmap groups decrease in size. Must be non-negative. This parameter can be thought of as `k` in the function `f`(`n`) `=` `C` `*` `n^-k`, where `f`(`n`) is the size of the `n`th group.
Setting the decay rate equal to `0` will cause all groups to be the same size. Setting the decay rate equal to `1` will cause the `n``th` `group` `to` `be` `1/n` the size of the initial group. Higher values of the decay rate cause consecutive groups to shrink at an increasing rate. The default is `1`.
If all groups are the same size, it is possible that groups containing newer commits will be able to be used less often than earlier groups, since it is more likely that the references pointing at newer commits will be updated more often than a reference pointing at an old commit. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bitmapPseudoMergenamesampleRate)bitmapPseudoMerge.<name>.sampleRate 
    
Determines the proportion of non-bitmapped commits (among reference tips) which are selected for inclusion in an unstable pseudo-merge bitmap. Must be between `0` and `1` (inclusive). The default is `1`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bitmapPseudoMergenamethreshold)bitmapPseudoMerge.<name>.threshold 
    
Determines the minimum age of non-bitmapped commits (among reference tips, as above) which are candidates for inclusion in an unstable pseudo-merge bitmap. The default is `1.week.ago`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bitmapPseudoMergenamemaxMerges)bitmapPseudoMerge.<name>.maxMerges 
    
Determines the maximum number of pseudo-merge commits among which commits may be distributed.
For pseudo-merge groups whose pattern does not contain any capture groups, this setting is applied for all commits matching the regular expression. For patterns that have one or more capture groups, this setting is applied for each distinct capture group.
For example, if your capture group is `refs/tags/`, then this setting will distribute all tags into a maximum of `maxMerges` pseudo-merge commits. However, if your capture group is, say, `refs/remotes/`([`0-9`]`+`)`/tags/`, then this setting will be applied to each remote’s set of tags individually.
Must be non-negative. The default value is 64. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bitmapPseudoMergenamestableThreshold)bitmapPseudoMerge.<name>.stableThreshold 
    
Determines the minimum age of commits (among reference tips, as above, however stable commits are still considered candidates even when they have been covered by a bitmap) which are candidates for a stable a pseudo-merge bitmap. The default is `1.month.ago`.
Setting this threshold to a smaller value (e.g., 1.week.ago) will cause more stable groups to be generated (which impose a one-time generation cost) but those groups will likely become stale over time. Using a larger value incurs the opposite penalty (fewer stable groups which are more useful). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bitmapPseudoMergenamestableSize)bitmapPseudoMerge.<name>.stableSize 
    
Determines the size (in number of commits) of a stable psuedo-merge bitmap. The default is `512`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blameblankBoundary)blame.blankBoundary 
    
Show blank commit object name for boundary commits in [git-blame[1]](https://git-scm.com/docs/git-blame). This option defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blamecoloring)blame.coloring 
    
This determines the coloring scheme to be applied to blame output. It can be _repeatedLines_ , _highlightRecent_ , or _none_ which is the default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blamedate)blame.date 
    
Specifies the format used to output dates in [git-blame[1]](https://git-scm.com/docs/git-blame). If unset the iso format is used. For supported values, see the discussion of the `--date` option at [git-log[1]](https://git-scm.com/docs/git-log). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blameshowEmail)blame.showEmail 
    
Show the author email instead of author name in [git-blame[1]](https://git-scm.com/docs/git-blame). This option defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blameshowRoot)blame.showRoot 
    
Do not treat root commits as boundaries in [git-blame[1]](https://git-scm.com/docs/git-blame). This option defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blameignoreRevsFile)blame.ignoreRevsFile 
    
Ignore revisions listed in the file, one unabbreviated object name per line, in [git-blame[1]](https://git-scm.com/docs/git-blame). Whitespace and comments beginning with `#` are ignored. This option may be repeated multiple times. Empty file names will reset the list of ignored revisions. This option will be handled before the command line option `--ignore-revs-file`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blamemarkUnblamableLines)blame.markUnblamableLines 
    
Mark lines that were changed by an ignored revision that we could not attribute to another commit with a _*_ in the output of [git-blame[1]](https://git-scm.com/docs/git-blame). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-blamemarkIgnoredLines)blame.markIgnoredLines 
    
Mark lines that were changed by an ignored revision that we attributed to another commit with a _?_ in the output of [git-blame[1]](https://git-scm.com/docs/git-blame). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchautoSetupMerge)`branch.autoSetupMerge` 
    
Tells `git` `branch`, `git` `switch` and `git` `checkout` to set up new branches so that [git-pull[1]](https://git-scm.com/docs/git-pull) will appropriately merge from the starting point branch. Note that even if this option is not set, this behavior can be chosen per-branch using the `--track` and `--no-track` options. This option defaults to `true`. The valid settings are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-false-1)`false` 
    
no automatic setup is done 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-true-1)`true` 
    
automatic setup is done when the starting point is a remote-tracking branch 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-always)`always` 
    
automatic setup is done when the starting point is either a local branch or remote-tracking branch 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-inherit)`inherit` 
    
if the starting point has a tracking configuration, it is copied to the new branch 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-simple)`simple` 
    
automatic setup is done only when the starting point is a remote-tracking branch and the new branch has the same name as the remote branch. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchautoSetupRebase)`branch.autoSetupRebase` 
    
When a new branch is created with `git` `branch`, `git` `switch` or `git` `checkout` that tracks another branch, this variable tells Git to set up pull to rebase instead of merge (see `branch.`_< name>_`.rebase`). The valid settings are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-never)`never` 
    
rebase is never automatically set to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-local-1)`local` 
    
rebase is set to true for tracked branches of other local branches. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remote)`remote` 
    
rebase is set to true for tracked branches of remote-tracking branches. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-always-1)`always` 
    
rebase will be set to true for all tracking branches.
See `branch.autoSetupMerge` for details on how to set up a branch to track another branch. This option defaults to `never`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchsort)`branch.sort` 
    
This variable controls the sort ordering of branches when displayed by [git-branch[1]](https://git-scm.com/docs/git-branch). Without the `--sort=`_< value>_ option provided, the value of this variable will be used as the default. See [git-for-each-ref[1]](https://git-scm.com/docs/git-for-each-ref) field names for valid values. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchnameremote)`branch.`_< name>_`.remote` 
    
When on branch _< name>_, it tells `git` `fetch` and `git` `push` which remote to fetch from or push to. The remote to push to may be overridden with `remote.pushDefault` (for all branches). The remote to push to, for the current branch, may be further overridden by `branch.`_< name>_`.pushRemote`. If no remote is configured, or if you are not on any branch and there is more than one remote defined in the repository, it defaults to `origin` for fetching and `remote.pushDefault` for pushing. Additionally, `.` (a period) is the current local repository (a dot-repository), see `branch.`_< name>_`.merge`'s final note below. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchnamepushRemote)`branch.`_< name>_`.pushRemote` 
    
When on branch _< name>_, it overrides `branch.`_< name>_`.remote` for pushing. It also overrides `remote.pushDefault` for pushing from branch _< name>_. When you pull from one place (e.g. your upstream) and push to another place (e.g. your own publishing repository), you would want to set `remote.pushDefault` to specify the remote to push to for all branches, and use this option to override it for a specific branch. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchnamemerge)`branch.`_< name>_`.merge` 
    
Defines, together with `branch.`_< name>_`.remote`, the upstream branch for the given branch. It tells `git` `fetch`/`git` `pull`/`git` `rebase` which branch to merge and can also affect `git` `push` (see `push.default`). When in branch _< name>_, it tells `git` `fetch` the default refspec to be marked for merging in `FETCH_HEAD`. The value is handled like the remote part of a refspec, and must match a ref which is fetched from the remote given by `branch.`_< name>_`.remote`. The merge information is used by `git` `pull` (which first calls `git` `fetch`) to lookup the default branch for merging. Without this option, `git` `pull` defaults to merge the first refspec fetched. Specify multiple values to get an octopus merge. If you wish to setup `git` `pull` so that it merges into _< name>_ from another branch in the local repository, you can point `branch.`_< name>_`.merge` to the desired branch, and use the relative path setting `.` (a period) for `branch.`_< name>_`.remote`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchnamemergeOptions)`branch.`_< name>_`.mergeOptions` 
    
Sets default options for merging into branch _< name>_. The syntax and supported options are the same as those of [git-merge[1]](https://git-scm.com/docs/git-merge), but option values containing whitespace characters are currently not supported. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchnamerebase)`branch.`_< name>_`.rebase` 
    
When true, rebase the branch _< name>_ on top of the fetched branch, instead of merging the default branch from the default remote when `git` `pull` is run. See `pull.rebase` for doing this in a non branch-specific manner.
When `merges` (or just `m`), pass the `--rebase-merges` option to `git` `rebase` so that the local merge commits are included in the rebase (see [git-rebase[1]](https://git-scm.com/docs/git-rebase) for details).
When the value is `interactive` (or just `i`), the rebase is run in interactive mode.
**NOTE** : this is a possibly dangerous operation; do **not** use it unless you understand the implications (see [git-rebase[1]](https://git-scm.com/docs/git-rebase) for details). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-branchnamedescription)`branch.`_< name>_`.description` 
    
Branch description, can be edited with `git` `branch` `--edit-description`. Branch description is automatically added to the `format-patch` cover letter or `request-pull` summary. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-browsertoolcmd)browser.<tool>.cmd 
    
Specify the command to invoke the specified browser. The specified command is evaluated in shell with the URLs passed as arguments. (See [git-web--browse[1]](https://git-scm.com/docs/git-web--browse).) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-browsertoolpath)browser.<tool>.path 
    
Override the path for the given tool that may be used to browse HTML help (see `-w` option in [git-help[1]](https://git-scm.com/docs/git-help)) or a working repository in gitweb (see [git-instaweb[1]](https://git-scm.com/docs/git-instaweb)). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bundle)bundle.* 
    
The `bundle.*` keys may appear in a bundle list file found via the `git` `clone` `--bundle-uri` option. These keys currently have no effect if placed in a repository config file, though this will change in the future. See [the bundle URI design document](https://git-scm.com/docs/bundle-uri) for more details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bundleversion)bundle.version 
    
This integer value advertises the version of the bundle list format used by the bundle list. Currently, the only accepted value is `1`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bundlemode)bundle.mode 
    
This string value should be either `all` or `any`. This value describes whether all of the advertised bundles are required to unbundle a complete understanding of the bundled information (`all`) or if any one of the listed bundle URIs is sufficient (`any`). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bundleheuristic)bundle.heuristic 
    
If this string-valued key exists, then the bundle list is designed to work well with incremental `git` `fetch` commands. The heuristic signals that there are additional keys available for each bundle that help determine which subset of bundles the client should download. The only value currently understood is `creationToken`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bundleid)bundle.<id>.* 
    
The `bundle.`_< id>_`.*` keys are used to describe a single item in the bundle list, grouped under _< id>_ for identification purposes. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-bundleiduri)bundle.<id>.uri 
    
This string value defines the URI by which Git can reach the contents of this _< id>_. This URI may be a bundle file or another bundle list. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-checkoutdefaultRemote)`checkout.defaultRemote` 
    
When you run `git` `checkout` _< something>_ or `git` `switch` _< something>_ and only have one remote, it may implicitly fall back on checking out and tracking e.g. `origin/`_< something>_. This stops working as soon as you have more than one remote with a _< something>_ reference. This setting allows for setting the name of a preferred remote that should always win when it comes to disambiguation. The typical use-case is to set this to `origin`.
Currently this is used by [git-switch[1]](https://git-scm.com/docs/git-switch) and [git-checkout[1]](https://git-scm.com/docs/git-checkout) when `git` `checkout` _< something>_ or `git` `switch` _< something>_ will checkout the _< something>_ branch on another remote, and by [git-worktree[1]](https://git-scm.com/docs/git-worktree) when `git` `worktree` `add` refers to a remote branch. This setting might be used for other checkout-like commands or functionality in the future. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-checkoutguess)`checkout.guess` 
    
Provides the default value for the `--guess` or `--no-guess` option in `git` `checkout` and `git` `switch`. See [git-switch[1]](https://git-scm.com/docs/git-switch) and [git-checkout[1]](https://git-scm.com/docs/git-checkout). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-checkoutworkers)`checkout.workers` 
    
The number of parallel workers to use when updating the working tree. The default is one, i.e. sequential execution. If set to a value less than one, Git will use as many workers as the number of logical cores available. This setting and `checkout.thresholdForParallelism` affect all commands that perform checkout. E.g. checkout, clone, reset, sparse-checkout, etc.
Note |  Parallel checkout usually delivers better performance for repositories located on SSDs or over NFS. For repositories on spinning disks and/or machines with a small number of cores, the default sequential checkout often performs better. The size and compression level of a repository might also influence how well the parallel version performs.   
---|--- 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-checkoutthresholdForParallelism)`checkout.thresholdForParallelism` 
      
When running parallel checkout with a small number of files, the cost of subprocess spawning and inter-process communication might outweigh the parallelization gains. This setting allows you to define the minimum number of files for which parallel checkout should be attempted. The default is 100. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-cleanrequireForce)clean.requireForce 
    
A boolean to make git-clean refuse to delete files unless -f is given. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-clonedefaultRemoteName)`clone.defaultRemoteName` 
    
The name of the remote to create when cloning a repository. Defaults to `origin`. It can be overridden by passing the `--origin` command-line option to [git-clone[1]](https://git-scm.com/docs/git-clone). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-clonerejectShallow)`clone.rejectShallow` 
    
Reject cloning a repository if it is a shallow one; this can be overridden by passing the `--reject-shallow` option on the command line. See [git-clone[1]](https://git-scm.com/docs/git-clone). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-clonefilterSubmodules)`clone.filterSubmodules` 
    
If a partial clone filter is provided (see `--filter` in [git-rev-list[1]](https://git-scm.com/docs/git-rev-list)) and `--recurse-submodules` is used, also apply the filter to submodules. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coloradvice)color.advice 
    
A boolean to enable/disable color in hints (e.g. when a push failed, see `advice.*` for a list). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the error output goes to a terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coloradvicehint)color.advice.hint 
    
Use customized color for hints. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorblamehighlightRecent)color.blame.highlightRecent 
    
Specify the line annotation color for `git` `blame` `--color-by-age` depending upon the age of the line.
This setting should be set to a comma-separated list of color and date settings, starting and ending with a color, the dates should be set from oldest to newest. The metadata will be colored with the specified colors if the line was introduced before the given timestamp, overwriting older timestamped colors.
Instead of an absolute timestamp relative timestamps work as well, e.g. `2.weeks.ago` is valid to address anything older than 2 weeks.
It defaults to `blue,12` `month` `ago,white,1` `month` `ago,red`, which colors everything older than one year blue, recent changes between one month and one year old are kept white, and lines introduced within the last month are colored red. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorblamerepeatedLines)color.blame.repeatedLines 
    
Use the specified color to colorize line annotations for `git` `blame` `--color-lines`, if they come from the same commit as the preceding line. Defaults to cyan. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorbranch)color.branch 
    
A boolean to enable/disable color in the output of [git-branch[1]](https://git-scm.com/docs/git-branch). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the output is to a terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorbranchslot)color.branch.<slot> 
    
Use customized color for branch coloration. _< slot>_ is one of `current` (the current branch), `local` (a local branch), `remote` (a remote-tracking branch in refs/remotes/), `upstream` (upstream tracking branch), `plain` (other refs). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colordiff)color.diff 
    
Whether to use ANSI escape sequences to add color to patches. If this is set to `always`, [git-diff[1]](https://git-scm.com/docs/git-diff), [git-log[1]](https://git-scm.com/docs/git-log), and [git-show[1]](https://git-scm.com/docs/git-show) will use color for all patches. If it is set to `true` or `auto`, those commands will only use color when output is to the terminal. If unset, then the value of `color.ui` is used (`auto` by default).
This does not affect [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) or the _git-diff-*_ plumbing commands. Can be overridden on the command line with the `--color`[`=`_< when>_] option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colordiffslot)color.diff.<slot> 
    
Use customized color for diff colorization. _< slot>_ specifies which part of the patch to use the specified color, and is one of `context` (context text - `plain` is a historical synonym), `meta` (metainformation), `frag` (hunk header), _func_ (function in hunk header), `old` (removed lines), `new` (added lines), `commit` (commit headers), `whitespace` (highlighting whitespace errors), `oldMoved` (deleted lines), `newMoved` (added lines), `oldMovedDimmed`, `oldMovedAlternative`, `oldMovedAlternativeDimmed`, `newMovedDimmed`, `newMovedAlternative` `newMovedAlternativeDimmed` (See the _< mode>_ setting of _--color-moved_ in [git-diff[1]](https://git-scm.com/docs/git-diff) for details), `contextDimmed`, `oldDimmed`, `newDimmed`, `contextBold`, `oldBold`, and `newBold` (see [git-range-diff[1]](https://git-scm.com/docs/git-range-diff) for details). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colordecorateslot)color.decorate.<slot> 
    
Use customized color for _git log --decorate_ output. _< slot>_ is one of `branch`, `remoteBranch`, `tag`, `stash` or `HEAD` for local branches, remote-tracking branches, tags, stash and HEAD, respectively and `grafted` for grafted commits. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorgrep)color.grep 
    
When set to `always`, always highlight matches. When `false` (or `never`), never. When set to `true` or `auto`, use color only when the output is written to the terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorgrepslot)color.grep.<slot> 
    
Use customized color for grep colorization. _< slot>_ specifies which part of the line to use the specified color, and is one of 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-context)`context` 
    
non-matching text in context lines (when using `-A`, `-B`, or `-C`) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-filename)`filename` 
    
filename prefix (when not using `-h`) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-function)`function` 
    
function name lines (when using `-p`) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-lineNumber)`lineNumber` 
    
line number prefix (when using `-n`) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-column)`column` 
    
column number prefix (when using `--column`) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-match)`match` 
    
matching text (same as setting `matchContext` and `matchSelected`) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-matchContext)`matchContext` 
    
matching text in context lines 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-matchSelected)`matchSelected` 
    
matching text in selected lines. Also, used to customize the following [git-log[1]](https://git-scm.com/docs/git-log) subcommands: `--grep`, `--author`, and `--committer`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-selected)`selected` 
    
non-matching text in selected lines. Also, used to customize the following [git-log[1]](https://git-scm.com/docs/git-log) subcommands: `--grep`, `--author` and `--committer`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-separator)`separator` 
    
separators between fields on a line (`:`, `-`, and `=`) and between hunks (`--`) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorinteractive)color.interactive 
    
When set to `always`, always use colors for interactive prompts and displays (such as those used by "git-add --interactive" and "git-clean --interactive"). When false (or `never`), never. When set to `true` or `auto`, use colors only when the output is to the terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorinteractiveslot)color.interactive.<slot> 
    
Use customized color for _git add --interactive_ and _git clean --interactive_ output. _< slot>_ may be `prompt`, `header`, `help` or `error`, for four distinct types of normal output from interactive commands. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorpager)color.pager 
    
A boolean to specify whether `auto` color modes should colorize output going to the pager. Defaults to true; set this to false if your pager does not understand ANSI color codes. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorpush)color.push 
    
A boolean to enable/disable color in push errors. May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the error output goes to a terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorpusherror)color.push.error 
    
Use customized color for push errors. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorremote)color.remote 
    
If set, keywords at the start of the line are highlighted. The keywords are "error", "warning", "hint" and "success", and are matched case-insensitively. May be set to `always`, `false` (or `never`) or `auto` (or `true`). If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorremoteslot)color.remote.<slot> 
    
Use customized color for each remote keyword. _< slot>_ may be `hint`, `warning`, `success` or `error` which match the corresponding keyword. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorshowBranch)color.showBranch 
    
A boolean to enable/disable color in the output of [git-show-branch[1]](https://git-scm.com/docs/git-show-branch). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the output is to a terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorstatus)color.status 
    
A boolean to enable/disable color in the output of [git-status[1]](https://git-scm.com/docs/git-status). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the output is to a terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorstatusslot)color.status.<slot> 
    
Use customized color for status colorization. _< slot>_ is one of `header` (the header text of the status message), `added` or `updated` (files which are added but not committed), `changed` (files which are changed but not added in the index), `untracked` (files which are not tracked by Git), `branch` (the current branch), `nobranch` (the color the _no branch_ warning is shown in, defaulting to red), `localBranch` or `remoteBranch` (the local and remote branch names, respectively, when branch and tracking information is displayed in the status short-format), or `unmerged` (files which have unmerged changes). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colortransport)color.transport 
    
A boolean to enable/disable color when pushes are rejected. May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the error output goes to a terminal. If unset, then the value of `color.ui` is used (`auto` by default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colortransportrejected)color.transport.rejected 
    
Use customized color when a push was rejected. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-colorui)color.ui 
    
This variable determines the default value for variables such as `color.diff` and `color.grep` that control the use of color per command family. Its scope will expand as more commands learn configuration to set a default for the `--color` option. Set it to `false` or `never` if you prefer Git commands not to use color unless enabled explicitly with some other configuration or the `--color` option. Set it to `always` if you want all output not intended for machine consumption to use color, to `true` or `auto` (this is the default since Git 1.8.4) if you want such output to use color when written to the terminal. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-columnui)column.ui 
    
Specify whether supported commands should output in columns. This variable consists of a list of tokens separated by spaces or commas:
These options control when the feature should be enabled (defaults to _never_): 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-always-1-1)`always` 
    
always show in columns 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-never-1)`never` 
    
never show in columns 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-auto)`auto` 
    
show in columns if the output is to the terminal
These options control layout (defaults to _column_). Setting any of these implies _always_ if none of _always_ , _never_ , or _auto_ are specified. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-column-1)`column` 
    
fill columns before rows 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-row)`row` 
    
fill rows before columns 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-plain)`plain` 
    
show in one column
Finally, these options can be combined with a layout option (defaults to _nodense_): 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-dense)`dense` 
    
make unequal size columns to utilize more space 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-nodense)`nodense` 
    
make equal size columns 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-columnbranch)column.branch 
    
Specify whether to output branch listing in `git` `branch` in columns. See `column.ui` for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-columnclean)column.clean 
    
Specify the layout when listing items in `git` `clean` `-i`, which always shows files and directories in columns. See `column.ui` for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-columnstatus)column.status 
    
Specify whether to output untracked files in `git` `status` in columns. See `column.ui` for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-columntag)column.tag 
    
Specify whether to output tag listings in `git` `tag` in columns. See `column.ui` for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitcleanup)`commit.cleanup` 
    
This setting overrides the default of the `--cleanup` option in `git` `commit`. See [git-commit[1]](https://git-scm.com/docs/git-commit) for details. Changing the default can be useful when you always want to keep lines that begin with the comment character (`core.commentChar`, default `#`) in your log message, in which case you would do `git` `config` `commit.cleanup` `whitespace` (note that you will have to remove the help lines that begin with the comment character in the commit log template yourself, if you do this). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitgpgSign)`commit.gpgSign` 
    
A boolean to specify whether all commits should be GPG signed. Use of this option when doing operations such as rebase can result in a large number of commits being signed. It may be convenient to use an agent to avoid typing your GPG passphrase several times. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitstatus)`commit.status` 
    
A boolean to enable/disable inclusion of status information in the commit message template when using an editor to prepare the commit message. Defaults to `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-committemplate)`commit.template` 
    
Specify the pathname of a file to use as the template for new commit messages. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitverbose)`commit.verbose` 
    
A boolean or int to specify the level of verbosity with `git` `commit`. See [git-commit[1]](https://git-scm.com/docs/git-commit) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitGraphgenerationVersion)commitGraph.generationVersion 
    
Specifies the type of generation number version to use when writing or reading the commit-graph file. If version 1 is specified, then the corrected commit dates will not be written or read. Defaults to 2. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitGraphmaxNewFilters)commitGraph.maxNewFilters 
    
Specifies the default value for the `--max-new-filters` option of `git` `commit-graph` `write` (c.f., [git-commit-graph[1]](https://git-scm.com/docs/git-commit-graph)). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitGraphchangedPaths)commitGraph.changedPaths 
    
If true, then `git` `commit-graph` `write` will compute and write changed-path Bloom filters by default, equivalent to passing `--changed-paths`. If false or unset, changed-paths Bloom filters will be written during `git` `commit-graph` `write` only if the filters already exist in the current commit-graph file. This matches the default behavior of `git` `commit-graph` `write` without any `--`[`no-`]`changed-paths` option. To rewrite a commit-graph file without any filters, use the `--no-changed-paths` option. Command-line option `--`[`no-`]`changed-paths` always takes precedence over this configuration. Defaults to unset. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitGraphreadChangedPaths)commitGraph.readChangedPaths 
    
Deprecated. Equivalent to commitGraph.changedPathsVersion=-1 if true, and commitGraph.changedPathsVersion=0 if false. (If commitGraph.changedPathVersion is also set, commitGraph.changedPathsVersion takes precedence.) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-commitGraphchangedPathsVersion)commitGraph.changedPathsVersion 
    
Specifies the version of the changed-path Bloom filters that Git will read and write. May be -1, 0, 1, or 2. Note that values greater than 1 may be incompatible with older versions of Git which do not yet understand those versions. Use caution when operating in a mixed-version environment.
Defaults to -1.
If -1, Git will use the version of the changed-path Bloom filters in the repository, defaulting to 1 if there are none.
If 0, Git will not read any Bloom filters, and will write version 1 Bloom filters when instructed to write.
If 1, Git will only read version 1 Bloom filters, and will write version 1 Bloom filters.
If 2, Git will only read version 2 Bloom filters, and will write version 2 Bloom filters.
See [git-commit-graph[1]](https://git-scm.com/docs/git-commit-graph) for more information. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-completioncommands)completion.commands 
    
This is only used by git-completion.bash to add or remove commands from the list of completed commands. Normally only porcelain commands and a few select others are completed. You can add more commands, separated by space, in this variable. Prefixing the command with _-_ will remove it from the existing list. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefileMode)core.fileMode 
    
Tells Git if the executable bit of files in the working tree is to be honored.
Some filesystems lose the executable bit when a file that is marked as executable is checked out, or checks out a non-executable file with executable bit on. [git-clone[1]](https://git-scm.com/docs/git-clone) or [git-init[1]](https://git-scm.com/docs/git-init) probe the filesystem to see if it handles the executable bit correctly and this variable is automatically set as necessary.
A repository, however, may be on a filesystem that handles the filemode correctly, and this variable is set to _true_ when created, but later may be made accessible from another environment that loses the filemode (e.g. exporting ext4 via CIFS mount, visiting a Cygwin created repository with Git for Windows or Eclipse). In such a case it may be necessary to set this variable to _false_. See [git-update-index[1]](https://git-scm.com/docs/git-update-index).
The default is true (when core.filemode is not specified in the config file). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corehideDotFiles)core.hideDotFiles 
    
(Windows-only) If true, mark newly-created directories and files whose name starts with a dot as hidden. If _dotGitOnly_ , only the `.git/` directory is hidden, but no other files starting with a dot. The default mode is _dotGitOnly_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreignoreCase)core.ignoreCase 
    
Internal variable which enables various workarounds to enable Git to work better on filesystems that are not case sensitive, like APFS, HFS+, FAT, NTFS, etc. For example, if a directory listing finds "makefile" when Git expects "Makefile", Git will assume it is really the same file, and continue to remember it as "Makefile".
The default is false, except [git-clone[1]](https://git-scm.com/docs/git-clone) or [git-init[1]](https://git-scm.com/docs/git-init) will probe and set core.ignoreCase true if appropriate when the repository is created.
Git relies on the proper configuration of this variable for your operating and file system. Modifying this value may result in unexpected behavior. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreprecomposeUnicode)core.precomposeUnicode 
    
This option is only used by Mac OS implementation of Git. When core.precomposeUnicode=true, Git reverts the unicode decomposition of filenames done by Mac OS. This is useful when sharing a repository between Mac OS and Linux or Windows. (Git for Windows 1.7.10 or higher is needed, or Git under cygwin 1.7). When false, file names are handled fully transparent by Git, which is backward compatible with older versions of Git. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreprotectHFS)core.protectHFS 
    
If set to true, do not allow checkout of paths that would be considered equivalent to `.git` on an HFS+ filesystem. Defaults to `true` on Mac OS, and `false` elsewhere. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreprotectNTFS)core.protectNTFS 
    
If set to true, do not allow checkout of paths that would cause problems with the NTFS filesystem, e.g. conflict with 8.3 "short" names. Defaults to `true` on Windows, and `false` elsewhere. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefsmonitor)core.fsmonitor 
    
If set to true, enable the built-in file system monitor daemon for this working directory ([git-fsmonitor--daemon[1]](https://git-scm.com/docs/git-fsmonitor--daemon)).
Like hook-based file system monitors, the built-in file system monitor can speed up Git commands that need to refresh the Git index (e.g. `git` `status`) in a working directory with many files. The built-in monitor eliminates the need to install and maintain an external third-party tool.
The built-in file system monitor is currently available only on a limited set of supported platforms. Currently, this includes Windows and MacOS.
Otherwise, this variable contains the pathname of the "fsmonitor" hook command.
This hook command is used to identify all files that may have changed since the requested date/time. This information is used to speed up git by avoiding unnecessary scanning of files that have not changed.
See the "fsmonitor-watchman" section of [githooks[5]](https://git-scm.com/docs/githooks).
Note that if you concurrently use multiple versions of Git, such as one version on the command line and another version in an IDE tool, that the definition of `core.fsmonitor` was extended to allow boolean values in addition to hook pathnames. Git versions 2.35.1 and prior will not understand the boolean values and will consider the "true" or "false" values as hook pathnames to be invoked. Git versions 2.26 thru 2.35.1 default to hook protocol V2 and will fall back to no fsmonitor (full scan). Git versions prior to 2.26 default to hook protocol V1 and will silently assume there were no changes to report (no scan), so status commands may report incomplete results. For this reason, it is best to upgrade all of your Git versions before using the built-in file system monitor. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefsmonitorHookVersion)core.fsmonitorHookVersion 
    
Sets the protocol version to be used when invoking the "fsmonitor" hook.
There are currently versions 1 and 2. When this is not set, version 2 will be tried first and if it fails then version 1 will be tried. Version 1 uses a timestamp as input to determine which files have changes since that time but some monitors like Watchman have race conditions when used with a timestamp. Version 2 uses an opaque string so that the monitor can return something that can be used to determine what files have changed without race conditions. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coretrustctime)core.trustctime 
    
If false, the ctime differences between the index and the working tree are ignored; useful when the inode change time is regularly modified by something outside Git (file system crawlers and some backup systems). See [git-update-index[1]](https://git-scm.com/docs/git-update-index). True by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresplitIndex)core.splitIndex 
    
If true, the split-index feature of the index will be used. See [git-update-index[1]](https://git-scm.com/docs/git-update-index). False by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreuntrackedCache)core.untrackedCache 
    
Determines what to do about the untracked cache feature of the index. It will be kept, if this variable is unset or set to `keep`. It will automatically be added if set to `true`. And it will automatically be removed, if set to `false`. Before setting it to `true`, you should check that mtime is working properly on your system. See [git-update-index[1]](https://git-scm.com/docs/git-update-index). `keep` by default, unless `feature.manyFiles` is enabled which sets this setting to `true` by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecheckStat)core.checkStat 
    
When missing or is set to `default`, many fields in the stat structure are checked to detect if a file has been modified since Git looked at it. When this configuration variable is set to `minimal`, sub-second part of mtime and ctime, the uid and gid of the owner of the file, the inode number (and the device number, if Git was compiled to use it), are excluded from the check among these fields, leaving only the whole-second part of mtime (and ctime, if `core.trustCtime` is set) and the filesize to be checked.
There are implementations of Git that do not leave usable values in some fields (e.g. JGit); by excluding these fields from the comparison, the `minimal` mode may help interoperability when the same repository is used by these other systems at the same time. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corequotePath)core.quotePath 
    
Commands that output paths (e.g. _ls-files_ , _diff_), will quote "unusual" characters in the pathname by enclosing the pathname in double-quotes and escaping those characters with backslashes in the same way C escapes control characters (e.g. _\t_ for TAB, _\n_ for LF, _\\\_ for backslash) or bytes with values larger than 0x80 (e.g. octal _\302\265_ for "micro" in UTF-8). If this variable is set to false, bytes higher than 0x80 are not considered "unusual" any more. Double-quotes, backslash and control characters are always escaped regardless of the setting of this variable. A simple space character is not considered "unusual". Many commands can output pathnames completely verbatim using the `-z` option. The default value is true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreeol)core.eol 
    
Sets the line ending type to use in the working directory for files that are marked as text (either by having the `text` attribute set, or by having `text=auto` and Git auto-detecting the contents as text). Alternatives are _lf_ , _crlf_ and _native_ , which uses the platform’s native line ending. The default value is `native`. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for more information on end-of-line conversion. Note that this value is ignored if `core.autocrlf` is set to `true` or `input`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresafecrlf)core.safecrlf 
    
If true, makes Git check if converting `CRLF` is reversible when end-of-line conversion is active. Git will verify if a command modifies a file in the work tree either directly or indirectly. For example, committing a file followed by checking out the same file should yield the original file in the work tree. If this is not the case for the current setting of `core.autocrlf`, Git will reject the file. The variable can be set to "warn", in which case Git will only warn about an irreversible conversion but continue the operation.
CRLF conversion bears a slight chance of corrupting data. When it is enabled, Git will convert CRLF to LF during commit and LF to CRLF during checkout. A file that contains a mixture of LF and CRLF before the commit cannot be recreated by Git. For text files this is the right thing to do: it corrects line endings such that we have only LF line endings in the repository. But for binary files that are accidentally classified as text the conversion can corrupt data.
If you recognize such corruption early you can easily fix it by setting the conversion type explicitly in .gitattributes. Right after committing you still have the original file in your work tree and this file is not yet corrupted. You can explicitly tell Git that this file is binary and Git will handle the file appropriately.
Unfortunately, the desired effect of cleaning up text files with mixed line endings and the undesired effect of corrupting binary files cannot be distinguished. In both cases CRLFs are removed in an irreversible way. For text files this is the right thing to do because CRLFs are line endings, while for binary files converting CRLFs corrupts data.
Note, this safety check does not mean that a checkout will generate a file identical to the original file for a different setting of `core.eol` and `core.autocrlf`, but only for the current one. For example, a text file with `LF` would be accepted with `core.eol=lf` and could later be checked out with `core.eol=crlf`, in which case the resulting file would contain `CRLF`, although the original file contained `LF`. However, in both work trees the line endings would be consistent, that is either all `LF` or all `CRLF`, but never mixed. A file with mixed line endings would be reported by the `core.safecrlf` mechanism. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreautocrlf)core.autocrlf 
    
Setting this variable to "true" is the same as setting the `text` attribute to "auto" on all files and core.eol to "crlf". Set to true if you want to have `CRLF` line endings in your working directory and the repository has LF line endings. This variable can be set to _input_ , in which case no output conversion is performed. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecheckRoundtripEncoding)core.checkRoundtripEncoding 
    
A comma and/or whitespace separated list of encodings that Git performs UTF-8 round trip checks on if they are used in an `working-tree-encoding` attribute (see [gitattributes[5]](https://git-scm.com/docs/gitattributes)). The default value is `SHIFT-JIS`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresymlinks)core.symlinks 
    
If false, symbolic links are checked out as small plain files that contain the link text. [git-update-index[1]](https://git-scm.com/docs/git-update-index) and [git-add[1]](https://git-scm.com/docs/git-add) will not change the recorded type to regular file. Useful on filesystems like FAT that do not support symbolic links.
The default is true, except [git-clone[1]](https://git-scm.com/docs/git-clone) or [git-init[1]](https://git-scm.com/docs/git-init) will probe and set core.symlinks false if appropriate when the repository is created. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coregitProxy)core.gitProxy 
    
A "proxy command" to execute (as _command host port_) instead of establishing direct connection to the remote server when using the Git protocol for fetching. If the variable value is in the "COMMAND for DOMAIN" format, the command is applied only on hostnames ending with the specified domain string. This variable may be set multiple times and is matched in the given order; the first match wins.
Can be overridden by the `GIT_PROXY_COMMAND` environment variable (which always applies universally, without the special "for" handling).
The special string `none` can be used as the proxy command to specify that no proxy be used for a given domain pattern. This is useful for excluding servers inside a firewall from proxy use, while defaulting to a common proxy for external domains. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresshCommand)core.sshCommand 
    
If this variable is set, `git` `fetch` and `git` `push` will use the specified command instead of `ssh` when they need to connect to a remote system. The command is in the same form as the `GIT_SSH_COMMAND` environment variable and is overridden when the environment variable is set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreignoreStat)core.ignoreStat 
    
If true, Git will avoid using lstat() calls to detect if files have changed by setting the "assume-unchanged" bit for those tracked files which it has updated identically in both the index and working tree.
When files are modified outside of Git, the user will need to stage the modified files explicitly (e.g. see _Examples_ section in [git-update-index[1]](https://git-scm.com/docs/git-update-index)). Git will not normally detect changes to those files.
This is useful on systems where lstat() calls are very slow, such as CIFS/Microsoft Windows.
False by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corepreferSymlinkRefs)core.preferSymlinkRefs 
    
Instead of the default "symref" format for HEAD and other symbolic reference files, use symbolic links. This is sometimes needed to work with old scripts that expect HEAD to be a symbolic link.
This configuration is deprecated and will be removed in Git 3.0. Symbolic refs will always be written as textual symrefs. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corealternateRefsCommand)core.alternateRefsCommand 
    
When advertising tips of available history from an alternate, use the shell to execute the specified command instead of [git-for-each-ref[1]](https://git-scm.com/docs/git-for-each-ref). The first argument is the absolute path of the alternate. Output must contain one hex object id per line (i.e., the same as produced by `git` `for-each-ref` `--format='%`(`objectname`)).
Note that you cannot generally put `git` `for-each-ref` directly into the config value, as it does not take a repository path as an argument (but you can wrap the command above in a shell script). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corealternateRefsPrefixes)core.alternateRefsPrefixes 
    
When listing references from an alternate, list only references that begin with the given prefix. Prefixes match as if they were given as arguments to [git-for-each-ref[1]](https://git-scm.com/docs/git-for-each-ref). To list multiple prefixes, separate them with whitespace. If `core.alternateRefsCommand` is set, setting `core.alternateRefsPrefixes` has no effect. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corebare)core.bare 
    
If true this repository is assumed to be _bare_ and has no working directory associated with it. If this is the case a number of commands that require a working directory will be disabled, such as [git-add[1]](https://git-scm.com/docs/git-add) or [git-merge[1]](https://git-scm.com/docs/git-merge).
This setting is automatically guessed by [git-clone[1]](https://git-scm.com/docs/git-clone) or [git-init[1]](https://git-scm.com/docs/git-init) when the repository was created. By default a repository that ends in "/.git" is assumed to be not bare (bare = false), while all other repositories are assumed to be bare (bare = true). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreworktree)core.worktree 
    
Set the path to the root of the working tree. If `GIT_COMMON_DIR` environment variable is set, core.worktree is ignored and not used for determining the root of working tree. This can be overridden by the `GIT_WORK_TREE` environment variable and the `--work-tree` command-line option. The value can be an absolute path or relative to the path to the .git directory, which is either specified by --git-dir or GIT_DIR, or automatically discovered. If --git-dir or GIT_DIR is specified but none of --work-tree, GIT_WORK_TREE and core.worktree is specified, the current working directory is regarded as the top level of your working tree.
Note that this variable is honored even when set in a configuration file in a ".git" subdirectory of a directory and its value differs from the latter directory (e.g. "/path/to/.git/config" has core.worktree set to "/different/path"), which is most likely a misconfiguration. Running Git commands in the "/path/to" directory will still use "/different/path" as the root of the work tree and can cause confusion unless you know what you are doing (e.g. you are creating a read-only snapshot of the same index to a location different from the repository’s usual working tree). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corelogAllRefUpdates)core.logAllRefUpdates 
    
Enable the reflog. Updates to a ref <ref> is logged to the file "`$GIT_DIR/logs/`_< ref>_", by appending the new and old SHA-1, the date/time and the reason of the update, but only when the file exists. If this configuration variable is set to `true`, missing "`$GIT_DIR/logs/`_< ref>_" file is automatically created for branch heads (i.e. under `refs/heads/`), remote refs (i.e. under `refs/remotes/`), note refs (i.e. under `refs/notes/`), and the symbolic ref `HEAD`. If it is set to `always`, then a missing reflog is automatically created for any ref under `refs/`.
This information can be used to determine what commit was the tip of a branch "2 days ago".
This value is true by default in a repository that has a working directory associated with it, and false by default in a bare repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corerepositoryFormatVersion)core.repositoryFormatVersion 
    
Internal variable identifying the repository format and layout version. See [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresharedRepository)core.sharedRepository 
    
When _group_ (or _true_), the repository is made shareable between several users in a group (making sure all the files and objects are group-writable). When _all_ (or _world_ or _everybody_), the repository will be readable by all users, additionally to being group-shareable. When _umask_ (or _false_), Git will use permissions reported by umask(2). When _0xxx_ , where _0xxx_ is an octal number, files in the repository will have this mode value. _0xxx_ will override user’s umask value (whereas the other options will only override requested parts of the user’s umask value). Examples: _0660_ will make the repo read/write-able for the owner and group, but inaccessible to others (equivalent to _group_ unless umask is e.g. _0022_). _0640_ is a repository that is group-readable but not group-writable. See [git-init[1]](https://git-scm.com/docs/git-init). False by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corewarnAmbiguousRefs)core.warnAmbiguousRefs 
    
If true, Git will warn you if the ref name you passed it is ambiguous and might match multiple refs in the repository. True by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecompression)core.compression 
    
An integer -1..9, indicating a default compression level. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If set, this provides a default to other compression variables, such as `core.looseCompression` and `pack.compression`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corelooseCompression)core.looseCompression 
    
An integer -1..9, indicating the compression level for objects that are not in a pack file. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If not set, defaults to core.compression. If that is not set, defaults to 1 (best speed). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corepackedGitWindowSize)core.packedGitWindowSize 
    
Number of bytes of a pack file to map into memory in a single mapping operation. Larger window sizes may allow your system to process a smaller number of large pack files more quickly. Smaller window sizes will negatively affect performance due to increased calls to the operating system’s memory manager, but may improve performance when accessing a large number of large pack files.
Default is 1 MiB if NO_MMAP was set at compile time, otherwise 32 MiB on 32 bit platforms and 1 GiB on 64 bit platforms. This should be reasonable for all users/operating systems. You probably do not need to adjust this value.
Common unit suffixes of _k_ , _m_ , or _g_ are supported. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corepackedGitLimit)core.packedGitLimit 
    
Maximum number of bytes to map simultaneously into memory from pack files. If Git needs to access more than this many bytes at once to complete an operation it will unmap existing regions to reclaim virtual address space within the process.
Default is 256 MiB on 32 bit platforms and 32 TiB (effectively unlimited) on 64 bit platforms. This should be reasonable for all users/operating systems, except on the largest projects. You probably do not need to adjust this value.
Common unit suffixes of _k_ , _m_ , or _g_ are supported. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coredeltaBaseCacheLimit)core.deltaBaseCacheLimit 
    
Maximum number of bytes per thread to reserve for caching base objects that may be referenced by multiple deltified objects. By storing the entire decompressed base objects in a cache Git is able to avoid unpacking and decompressing frequently used base objects multiple times.
Default is 96 MiB on all platforms. This should be reasonable for all users/operating systems, except on the largest projects. You probably do not need to adjust this value.
Common unit suffixes of _k_ , _m_ , or _g_ are supported. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corebigFileThreshold)core.bigFileThreshold 
    
The size of files considered "big", which as discussed below changes the behavior of numerous git commands, as well as how such files are stored within the repository. The default is 512 MiB. Common unit suffixes of _k_ , _m_ , or _g_ are supported.
Files above the configured limit will be:
  * Stored deflated in packfiles, without attempting delta compression.
The default limit is primarily set with this use-case in mind. With it, most projects will have their source code and other text files delta compressed, but not larger binary media files.
Storing large files without delta compression avoids excessive memory usage, at the slight expense of increased disk usage.
  * Will be treated as if they were labeled "binary" (see [gitattributes[5]](https://git-scm.com/docs/gitattributes)). e.g. [git-log[1]](https://git-scm.com/docs/git-log) and [git-diff[1]](https://git-scm.com/docs/git-diff) will not compute diffs for files above this limit.
  * Will generally be streamed when written, which avoids excessive memory usage, at the cost of some fixed overhead. Commands that make use of this include [git-archive[1]](https://git-scm.com/docs/git-archive), [git-fast-import[1]](https://git-scm.com/docs/git-fast-import), [git-index-pack[1]](https://git-scm.com/docs/git-index-pack), [git-unpack-objects[1]](https://git-scm.com/docs/git-unpack-objects) and [git-fsck[1]](https://git-scm.com/docs/git-fsck).



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreexcludesFile)core.excludesFile 
    
Specifies the pathname to the file that contains patterns to describe paths that are not meant to be tracked, in addition to `.gitignore` (per-directory) and `.git/info/exclude`. Defaults to `$XDG_CONFIG_HOME/git/ignore`. If `$XDG_CONFIG_HOME` is either not set or empty, `$HOME/.config/git/ignore` is used instead. See [gitignore[5]](https://git-scm.com/docs/gitignore). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreaskPass)core.askPass 
    
Some commands (e.g. svn and http interfaces) that interactively ask for a password can be told to use an external program given via the value of this variable. Can be overridden by the `GIT_ASKPASS` environment variable. If not set, fall back to the value of the `SSH_ASKPASS` environment variable or, failing that, a simple password prompt. The external program shall be given a suitable prompt as command-line argument and write the password on its STDOUT. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreattributesFile)core.attributesFile 
    
Specifies the pathname to the file that contains attributes (see [gitattributes[5]](https://git-scm.com/docs/gitattributes)), in addition to `.gitattributes` (per-directory) and `.git/info/attributes`. Its default value is `$XDG_CONFIG_HOME/git/attributes`. If `$XDG_CONFIG_HOME` is either not set or empty, `$HOME/.config/git/attributes` is used instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corehooksPath)core.hooksPath 
    
By default Git will look for your hooks in the `$GIT_DIR/hooks` directory. Set this to different path, e.g. `/etc/git/hooks`, and Git will try to find your hooks in that directory, e.g. `/etc/git/hooks/pre-receive` instead of in `$GIT_DIR/hooks/pre-receive`.
The path can be either absolute or relative. A relative path is taken as relative to the directory where the hooks are run (see the "DESCRIPTION" section of [githooks[5]](https://git-scm.com/docs/githooks)).
This configuration variable is useful in cases where you’d like to centrally configure your Git hooks instead of configuring them on a per-repository basis, or as a more flexible and centralized alternative to having an `init.templateDir` where you’ve changed default hooks.
You can also disable all hooks entirely by setting `core.hooksPath` to `/dev/null`. This is usually only advisable for expert users and on a per-command basis using configuration parameters of the form `git` `-c` `core.hooksPath=/dev/null` .... 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreeditor)core.editor 
    
Commands such as `commit` and `tag` that let you edit messages by launching an editor use the value of this variable when it is set, and the environment variable `GIT_EDITOR` is not set. See [git-var[1]](https://git-scm.com/docs/git-var). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecommentChar)core.commentChar 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecommentString)core.commentString 
    
Commands such as `commit` and `tag` that let you edit messages consider a line that begins with this character commented, and removes them after the editor returns (default _#_).
If set to "auto", `git-commit` will select a character that is not the beginning character of any line in existing commit messages. Support for this value is deprecated and will be removed in Git 3.0 due to the following limitations:
  * It is incompatible with adding comments in a commit message template. This includes the conflicts comments added to the commit message by `cherry-pick`, `merge`, `rebase` and `revert`.
  * It is incompatible with adding comments to the commit message in the `prepare-commit-msg` hook.
  * It is incompatible with the `fixup` and `squash` commands when rebasing,
  * It is not respected by `git` `notes`


Note that these two variables are aliases of each other, and in modern versions of Git you are free to use a string (e.g., `//` or _⁑⁕⁑_) with `commentChar`. Versions of Git prior to v2.45.0 will ignore `commentString` but will reject a value of `commentChar` that consists of more than a single ASCII byte. If you plan to use your config with older and newer versions of Git, you may want to specify both:
```
[core]
# single character for older versions
commentChar = "#"
# string for newer versions (which will override commentChar
# because it comes later in the file)
commentString = "//"
```


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefilesRefLockTimeout)core.filesRefLockTimeout 
    
The length of time, in milliseconds, to retry when trying to lock an individual reference. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 100 (i.e., retry for 100ms). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corepackedRefsTimeout)core.packedRefsTimeout 
    
The length of time, in milliseconds, to retry when trying to lock the `packed-refs` file. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 1000 (i.e., retry for 1 second). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corepager)core.pager 
    
Text viewer for use by Git commands (e.g., _less_). The value is meant to be interpreted by the shell. The order of preference is the `$GIT_PAGER` environment variable, then `core.pager` configuration, then `$PAGER`, and then the default chosen at compile time (usually _less_).
When the `LESS` environment variable is unset, Git sets it to `FRX` (if `LESS` environment variable is set, Git does not change it at all). If you want to selectively override Git’s default setting for `LESS`, you can set `core.pager` to e.g. `less` `-S`. This will be passed to the shell by Git, which will translate the final command to `LESS=FRX` `less` `-S`. The environment does not set the `S` option but the command line does, instructing less to truncate long lines. Similarly, setting `core.pager` to `less` `-+F` will deactivate the `F` option specified by the environment from the command-line, deactivating the "quit if one screen" behavior of `less`. One can specifically activate some flags for particular commands: for example, setting `pager.blame` to `less` `-S` enables line truncation only for `git` `blame`.
Likewise, when the `LV` environment variable is unset, Git sets it to `-c`. You can override this setting by exporting `LV` with another value or setting `core.pager` to `lv` `+c`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corewhitespace)core.whitespace 
    
A comma separated list of common whitespace problems to notice. _git diff_ will use `color.diff.whitespace` to highlight them, and _git apply --whitespace=error_ will consider them as errors. You can prefix `-` to disable any of them (e.g. `-trailing-space`):
  * `blank-at-eol` treats trailing whitespaces at the end of the line as an error (enabled by default).
  * `space-before-tab` treats a space character that appears immediately before a tab character in the initial indent part of the line as an error (enabled by default).
  * `indent-with-non-tab` treats a line that is indented with space characters instead of the equivalent tabs as an error (not enabled by default).
  * `tab-in-indent` treats a tab character in the initial indent part of the line as an error (not enabled by default).
  * `blank-at-eof` treats blank lines added at the end of file as an error (enabled by default).
  * `trailing-space` is a short-hand to cover both `blank-at-eol` and `blank-at-eof`.
  * `cr-at-eol` treats a carriage-return at the end of line as part of the line terminator, i.e. with it, `trailing-space` does not trigger if the character before such a carriage-return is not a whitespace (not enabled by default).
  * `incomplete-line` treats the last line of a file that is missing the newline at the end as an error (not enabled by default).
  * `tabwidth=`_< n>_ tells how many character positions a tab occupies; this is relevant for `indent-with-non-tab` and when Git fixes `tab-in-indent` errors. The default tab width is 8. Allowed values are 1 to 63.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefsync)core.fsync 
    
A comma-separated list of components of the repository that should be hardened via the core.fsyncMethod when created or modified. You can disable hardening of any component by prefixing it with a _-_. Items that are not hardened may be lost in the event of an unclean system shutdown. Unless you have special requirements, it is recommended that you leave this option empty or pick one of `committed`, `added`, or `all`.
When this configuration is encountered, the set of components starts with the platform default value, disabled components are removed, and additional components are added. `none` resets the state so that the platform default is ignored.
The empty string resets the fsync configuration to the platform default. The default on most platforms is equivalent to `core.fsync=committed,-loose-object`, which has good performance, but risks losing recent work in the event of an unclean system shutdown.
  * `none` clears the set of fsynced components.
  * `loose-object` hardens objects added to the repo in loose-object form.
  * `pack` hardens objects added to the repo in packfile form.
  * `pack-metadata` hardens packfile bitmaps and indexes.
  * `commit-graph` hardens the commit-graph file.
  * `index` hardens the index when it is modified.
  * `objects` is an aggregate option that is equivalent to `loose-object,pack`.
  * `reference` hardens references modified in the repo.
  * `derived-metadata` is an aggregate option that is equivalent to `pack-metadata,commit-graph`.
  * `committed` is an aggregate option that is currently equivalent to `objects`. This mode sacrifices some performance to ensure that work that is committed to the repository with `git` `commit` or similar commands is hardened.
  * `added` is an aggregate option that is currently equivalent to `committed,index`. This mode sacrifices additional performance to ensure that the results of commands like `git` `add` and similar operations are hardened.
  * `all` is an aggregate option that syncs all individual components above.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefsyncMethod)core.fsyncMethod 
    
A value indicating the strategy Git will use to harden repository data using fsync and related primitives.
  * `fsync` uses the fsync() system call or platform equivalents.
  * `writeout-only` issues pagecache writeback requests, but depending on the filesystem and storage hardware, data added to the repository may not be durable in the event of a system crash. This is the default mode on macOS.
  * `batch` enables a mode that uses writeout-only flushes to stage multiple updates in the disk writeback cache and then does a single full fsync of a dummy file to trigger the disk cache flush at the end of the operation.
Currently `batch` mode only applies to loose-object files. Other repository data is made durable as if `fsync` was specified. This mode is expected to be as safe as `fsync` on macOS for repos stored on HFS+ or APFS filesystems and on Windows for repos stored on NTFS or ReFS filesystems.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corefsyncObjectFiles)core.fsyncObjectFiles 
    
This boolean will enable _fsync()_ when writing object files. This setting is deprecated. Use core.fsync instead.
This setting affects data added to the Git repository in loose-object form. When set to true, Git will issue an fsync or similar system call to flush caches so that loose-objects remain consistent in the face of a unclean system shutdown. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corepreloadIndex)core.preloadIndex 
    
Enable parallel index preload for operations like _git diff_
This can speed up operations like _git diff_ and _git status_ especially on filesystems like NFS that have weak caching semantics and thus relatively high IO latencies. When enabled, Git will do the index comparison to the filesystem data in parallel, allowing overlapping IO’s. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreunsetenvvars)core.unsetenvvars 
    
Windows-only: comma-separated list of environment variables' names that need to be unset before spawning any other process. Defaults to `PERL5LIB` to account for the fact that Git for Windows insists on using its own Perl interpreter. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecreateObject)core.createObject 
    
You can set this to _link_ , in which case a hardlink followed by a delete of the source are used to make sure that object creation will not overwrite existing objects.
On some file system/operating system combinations, this is unreliable. Set this config setting to _rename_ there; however, this will remove the check that makes sure that existing object files will not get overwritten. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corenotesRef)core.notesRef 
    
When showing commit messages, also show notes which are stored in the given ref. The ref must be fully qualified. If the given ref does not exist, it is not an error but means that no notes should be printed.
This setting defaults to "refs/notes/commits", and it can be overridden by the `GIT_NOTES_REF` environment variable. See [git-notes[1]](https://git-scm.com/docs/git-notes). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-corecommitGraph)core.commitGraph 
    
If true, then git will read the commit-graph file (if it exists) to parse the graph structure of commits. Defaults to true. See [git-commit-graph[1]](https://git-scm.com/docs/git-commit-graph) for more information. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreuseReplaceRefs)core.useReplaceRefs 
    
If set to `false`, behave as if the `--no-replace-objects` option was given on the command line. See [git[1]](https://git-scm.com/docs/git) and [git-replace[1]](https://git-scm.com/docs/git-replace) for more information. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coremultiPackIndex)core.multiPackIndex 
    
Use the multi-pack-index file to track multiple packfiles using a single index. See [git-multi-pack-index[1]](https://git-scm.com/docs/git-multi-pack-index) for more information. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresparseCheckout)core.sparseCheckout 
    
Enable "sparse checkout" feature. See [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) for more information. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresparseCheckoutCone)core.sparseCheckoutCone 
    
Enables the "cone mode" of the sparse checkout feature. When the sparse-checkout file contains a limited set of patterns, this mode provides significant performance advantages. The "non-cone mode" can be requested to allow specifying more flexible patterns by setting this variable to _false_. See [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) for more information. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coreabbrev)core.abbrev 
    
Set the length object names are abbreviated to. If unspecified or set to "auto", an appropriate value is computed based on the approximate number of packed objects in your repository, which hopefully is enough for abbreviated object names to stay unique for some time. If set to "no", no abbreviation is made and the object names are shown in their full length. The minimum length is 4. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coremaxTreeDepth)core.maxTreeDepth 
    
The maximum depth Git is willing to recurse while traversing a tree (e.g., "a/b/cde/f" has a depth of 4). This is a fail-safe to allow Git to abort cleanly, and should not generally need to be adjusted. When Git is compiled with MSVC, the default is 512. Otherwise, the default is 2048. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialhelper)credential.helper 
    
Specify an external helper to be called when a username or password credential is needed; the helper may consult external storage to avoid prompting the user for the credentials. This is normally the name of a credential helper with possible arguments, but may also be an absolute path with arguments or, if preceded by `!`, shell commands.
Note that multiple helpers may be defined. See [gitcredentials[7]](https://git-scm.com/docs/gitcredentials) for details and examples. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialinteractive)credential.interactive 
    
By default, Git and any configured credential helpers will ask for user input when new credentials are required. Many of these helpers will succeed based on stored credentials if those credentials are still valid. To avoid the possibility of user interactivity from Git, set `credential.interactive=false`. Some credential helpers respect this option as well. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialuseHttpPath)credential.useHttpPath 
    
When acquiring credentials, consider the "path" component of an http or https URL to be important. Defaults to false. See [gitcredentials[7]](https://git-scm.com/docs/gitcredentials) for more information. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialsanitizePrompt)credential.sanitizePrompt 
    
By default, user names and hosts that are shown as part of the password prompt are not allowed to contain control characters (they will be URL-encoded by default). Configure this setting to `false` to override that behavior. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialprotectProtocol)credential.protectProtocol 
    
By default, Carriage Return characters are not allowed in the protocol that is used when Git talks to a credential helper. This setting allows users to override this default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialusername)credential.username 
    
If no username is set for a network authentication, use this username by default. See credential.<context>.* below, and [gitcredentials[7]](https://git-scm.com/docs/gitcredentials). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialurl)credential.<url>.* 
    
Any of the credential.* options above can be applied selectively to some credentials. For example, "credential.https://example.com.username" would set the default username only for https connections to example.com. See [gitcredentials[7]](https://git-scm.com/docs/gitcredentials) for details on how URLs are matched. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialCacheignoreSIGHUP)credentialCache.ignoreSIGHUP 
    
Tell git-credential-cache—​daemon to ignore SIGHUP, instead of quitting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-credentialStorelockTimeoutMS)credentialStore.lockTimeoutMS 
    
The length of time, in milliseconds, for git-credential-store to retry when trying to lock the credentials file. A value of 0 means not to retry at all; -1 means to try indefinitely. Default is 1000 (i.e., retry for 1s). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffautoRefreshIndex)`diff.autoRefreshIndex` 
    
When using `git` `diff` to compare with work tree files, do not consider stat-only changes as changed. Instead, silently run `git` `update-index` `--refresh` to update the cached stat information for paths whose contents in the work tree match the contents in the index. This option defaults to `true`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdirstat)`diff.dirstat` 
    
A comma separated list of `--dirstat` parameters specifying the default behavior of the `--dirstat` option to [git-diff[1]](https://git-scm.com/docs/git-diff) and friends. The defaults can be overridden on the command line (using `--dirstat=`_< param>_`,...`). The fallback defaults (when not changed by `diff.dirstat`) are `changes,noncumulative,3`. The following parameters are available: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-changes)`changes` 
    
Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-lines)`lines` 
    
Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive `--dirstat` behavior than the `changes` behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other `--*stat` options. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-files)`files` 
    
Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest `--dirstat` behavior, since it does not have to look at the file contents at all. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-cumulative)`cumulative` 
    
Count changes in a child directory for the parent directory as well. Note that when using `cumulative`, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the `noncumulative` parameter. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-limit)_< limit>_ 
    
An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.
Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: `files,10,cumulative`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffstatNameWidth)`diff.statNameWidth` 
    
Limit the width of the filename part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffstatGraphWidth)`diff.statGraphWidth` 
    
Limit the width of the graph part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffcontext)`diff.context` 
    
Generate diffs with _< n>_ lines of context instead of the default of 3. This value is overridden by the `-U` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffinterHunkContext)`diff.interHunkContext` 
    
Show the context between diff hunks, up to the specified number of lines, thereby fusing the hunks that are close to each other. This value serves as the default for the `--inter-hunk-context` command line option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffexternal)`diff.external` 
    
If this config variable is set, diff generation is not performed using the internal diff machinery, but using the given command. Can be overridden with the `GIT_EXTERNAL_DIFF` environment variable. The command is called with parameters as described under "git Diffs" in [git[1]](https://git-scm.com/docs/git). Note: if you want to use an external diff program only on a subset of your files, you might want to use [gitattributes[5]](https://git-scm.com/docs/gitattributes) instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftrustExitCode)`diff.trustExitCode` 
    
If this boolean value is set to `true` then the `diff.external` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code `0` regardless of equality. Any other exit code causes Git to report a fatal error. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffignoreSubmodules)`diff.ignoreSubmodules` 
    
Sets the default value of `--ignore-submodules`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`. `git` `checkout` and `git` `switch` also honor this setting when reporting uncommitted changes. Setting it to `all` disables the submodule summary normally shown by `git` `commit` and `git` `status` when `status.submoduleSummary` is set unless it is overridden by using the `--ignore-submodules` command-line option. The `git` `submodule` commands are not affected by this setting. By default this is set to untracked so that any untracked submodules are ignored. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffmnemonicPrefix)`diff.mnemonicPrefix` 
    
If set, `git` `diff` uses a prefix pair that is different from the standard `a/` and `b/` depending on what is being compared. When this configuration is in effect, reverse diff output also swaps the order of the prefixes: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitdiff)`git` `diff` 
    
compares the (i)ndex and the (w)ork tree; 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitdiffHEAD)`git` `diff` `HEAD` 
    
compares a (c)ommit and the (w)ork tree; 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitdiff--cached)`git` `diff` `--cached` 
    
compares a (c)ommit and the (i)ndex; 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitdiffHEADfile1file2)`git` `diff` `HEAD:`_< file1>_ _< file2>_ 
    
compares an (o)bject and a (w)ork tree entity; 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitdiff--no-indexab)`git` `diff` `--no-index` _< a>_ _< b>_ 
    
compares two non-git things _< a>_ and _< b>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffnoPrefix)`diff.noPrefix` 
    
If set, `git` `diff` does not show any source or destination prefix. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffsrcPrefix)`diff.srcPrefix` 
    
If set, `git` `diff` uses this source prefix. Defaults to `a/`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdstPrefix)`diff.dstPrefix` 
    
If set, `git` `diff` uses this destination prefix. Defaults to `b/`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffrelative)`diff.relative` 
    
If set to `true`, `git` `diff` does not show changes outside of the directory and show pathnames relative to the current directory. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difforderFile)`diff.orderFile` 
    
File indicating how to order files within a diff. See the `-O` option to [git-diff[1]](https://git-scm.com/docs/git-diff) for details. If `diff.orderFile` is a relative pathname, it is treated as relative to the top of the working tree. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffrenameLimit)`diff.renameLimit` 
    
The number of files to consider in the exhaustive portion of copy/rename detection; equivalent to the `git` `diff` option `-l`. If not set, the default value is currently 1000. This setting has no effect if rename detection is turned off. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffrenames)`diff.renames` 
    
Whether and how Git detects renames. If set to `false`, rename detection is disabled. If set to `true`, basic rename detection is enabled. If set to `copies` or `copy`, Git will detect copies, as well. Defaults to `true`. Note that this affects only `git` `diff` Porcelain like [git-diff[1]](https://git-scm.com/docs/git-diff) and [git-log[1]](https://git-scm.com/docs/git-log), and not lower level commands such as [git-diff-files[1]](https://git-scm.com/docs/git-diff-files). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffsuppressBlankEmpty)`diff.suppressBlankEmpty` 
    
A boolean to inhibit the standard behavior of printing a space before each empty output line. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffsubmodule)`diff.submodule` 
    
Specify the format in which differences in submodules are shown. The `short` format just shows the names of the commits at the beginning and end of the range. The `log` format lists the commits in the range like [git-submodule[1]](https://git-scm.com/docs/git-submodule) `summary` does. The `diff` format shows an inline diff of the changed contents of the submodule. Defaults to `short`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffwordRegex)`diff.wordRegex` 
    
A POSIX Extended Regular Expression used to determine what is a "word" when performing word-by-word difference calculations. Character sequences that match the regular expression are "words", all other characters are **ignorable** whitespace. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdrivercommand)`diff.`_< driver>_`.command` 
    
The custom diff driver command. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdrivertrustExitCode)`diff.`_< driver>_`.trustExitCode` 
    
If this boolean value is set to `true` then the `diff.`_< driver>_`.command` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code 0 regardless of equality. Any other exit code causes Git to report a fatal error. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdriverxfuncname)`diff.`_< driver>_`.xfuncname` 
    
The regular expression that the diff driver should use to recognize the hunk header. A built-in pattern may also be used. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdriverbinary)`diff.`_< driver>_`.binary` 
    
Set this option to `true` to make the diff driver treat files as binary. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdrivertextconv)`diff.`_< driver>_`.textconv` 
    
The command that the diff driver should call to generate the text-converted version of a file. The result of the conversion is used to generate a human-readable diff. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdriverwordRegex)`diff.`_< driver>_`.wordRegex` 
    
The regular expression that the diff driver should use to split words in a line. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffdrivercachetextconv)`diff.`_< driver>_`.cachetextconv` 
    
Set this option to `true` to make the diff driver cache the text conversion outputs. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffindentHeuristic)`diff.indentHeuristic` 
    
Set this option to `false` to disable the default heuristics that shift diff hunk boundaries to make patches easier to read. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffalgorithm)`diff.algorithm` 
    
Choose a diff algorithm. The variants are as follows: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-default)`default` 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-myers)`myers` 
    
The basic greedy diff algorithm. Currently, this is the default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-minimal)`minimal` 
    
Spend extra time to make sure the smallest possible diff is produced. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-patience)`patience` 
    
Use "patience diff" algorithm when generating patches. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-histogram)`histogram` 
    
This algorithm extends the patience algorithm to "support low-occurrence common elements". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffwsErrorHighlight)`diff.wsErrorHighlight` 
    
Highlight whitespace errors in the `context`, `old` or `new` lines of the diff. Multiple values are separated by comma, `none` resets previous values, `default` reset the list to `new` and `all` is a shorthand for `old,new,context`. The whitespace errors are colored with `color.diff.whitespace`. The command line option `--ws-error-highlight=`_< kind>_ overrides this setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffcolorMoved)`diff.colorMoved` 
    
If set to either a valid _< mode>_ or a `true` value, moved lines in a diff are colored differently. For details of valid modes see `--color-moved` in [git-diff[1]](https://git-scm.com/docs/git-diff). If simply set to `true` the default color mode will be used. When set to `false`, moved lines are not colored. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffcolorMovedWS)`diff.colorMovedWS` 
    
When moved lines are colored using e.g. the `diff.colorMoved` setting, this option controls the mode how spaces are treated. For details of valid modes see `--color-moved-ws` in [git-diff[1]](https://git-scm.com/docs/git-diff). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftool)diff.tool 
    
Controls which diff tool is used by [git-difftool[1]](https://git-scm.com/docs/git-difftool). This variable overrides the value configured in `merge.tool`. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding difftool.<tool>.cmd variable is defined. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-diffguitool)diff.guitool 
    
Controls which diff tool is used by [git-difftool[1]](https://git-scm.com/docs/git-difftool) when the -g/--gui flag is specified. This variable overrides the value configured in `merge.guitool`. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding difftool.<guitool>.cmd variable is defined.
  * araxis
  * bc
  * codecompare
  * deltawalker
  * diffmerge
  * diffuse
  * ecmerge
  * emerge
  * examdiff
  * guiffy
  * gvimdiff
  * kdiff3
  * kompare
  * meld
  * nvimdiff
  * opendiff
  * p4merge
  * smerge
  * tkdiff
  * vimdiff
  * vscode
  * winmerge
  * xxdiff



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftooltoolcmd)difftool.<tool>.cmd 
    
Specify the command to invoke the specified diff tool. The specified command is evaluated in shell with the following variables available: _LOCAL_ is set to the name of the temporary file containing the contents of the diff pre-image and _REMOTE_ is set to the name of the temporary file containing the contents of the diff post-image.
See the `--tool=`_< tool>_ option in [git-difftool[1]](https://git-scm.com/docs/git-difftool) for more details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftooltoolpath)difftool.<tool>.path 
    
Override the path for the given tool. This is useful in case your tool is not in the PATH. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftooltrustExitCode)difftool.trustExitCode 
    
Exit difftool if the invoked diff tool returns a non-zero exit status.
See the `--trust-exit-code` option in [git-difftool[1]](https://git-scm.com/docs/git-difftool) for more details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftoolprompt)difftool.prompt 
    
Prompt before each invocation of the diff tool. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftoolguiDefault)difftool.guiDefault 
    
Set `true` to use the `diff.guitool` by default (equivalent to specifying the `--gui` argument), or `auto` to select `diff.guitool` or `diff.tool` depending on the presence of a `DISPLAY` environment variable value. The default is `false`, where the `--gui` argument must be provided explicitly for the `diff.guitool` to be used. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-extensions)extensions.* 
    
Unless otherwise stated, is an error to specify an extension if `core.repositoryFormatVersion` is not `1`. See [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-compatObjectFormat)compatObjectFormat 
    
Specify a compatibility hash algorithm to use. The acceptable values are `sha1` and `sha256`. The value specified must be different from the value of `extensions.objectFormat`. This allows client level interoperability between git repositories whose objectFormat matches this compatObjectFormat. In particular when fully implemented the pushes and pulls from a repository in whose objectFormat matches compatObjectFormat. As well as being able to use oids encoded in compatObjectFormat in addition to oids encoded with objectFormat to locally specify objects.
Note that the functionality enabled by this extension is incomplete and subject to change. It currently exists only to allow development and testing of the underlying feature and is not designed to be enabled by end users. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-noop)noop 
    
This extension does not change git’s behavior at all. It is useful only for testing format-1 compatibility.
For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-noop-v1)noop-v1 
    
This extension does not change git’s behavior at all. It is useful only for testing format-1 compatibility. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-objectFormat)objectFormat 
    
Specify the hash algorithm to use. The acceptable values are `sha1` and `sha256`. If not specified, `sha1` is assumed.
Note that this setting should only be set by [git-init[1]](https://git-scm.com/docs/git-init) or [git-clone[1]](https://git-scm.com/docs/git-clone). Trying to change it after initialization will not work and will produce hard-to-diagnose issues. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-partialClone)partialClone 
    
When enabled, indicates that the repo was created with a partial clone (or later performed a partial fetch) and that the remote may have omitted sending certain unwanted objects. Such a remote is called a "promisor remote" and it promises that all such omitted objects can be fetched from it in the future.
The value of this key is the name of the promisor remote.
For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-preciousObjects)preciousObjects 
    
If enabled, indicates that objects in the repository MUST NOT be deleted (e.g., by `git-prune` or `git` `repack` `-d`).
For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-refStorage)refStorage 
    
Specify the ref storage format to use. The acceptable values are:
  * `files` for loose files with packed-refs. This is the default.
  * `reftable` for the reftable format. This format is experimental and its internals are subject to change.


Note that this setting should only be set by [git-init[1]](https://git-scm.com/docs/git-init) or [git-clone[1]](https://git-scm.com/docs/git-clone). Trying to change it after initialization will not work and will produce hard-to-diagnose issues. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-relativeWorktrees)relativeWorktrees 
    
If enabled, indicates at least one worktree has been linked with relative paths. Automatically set if a worktree has been created or repaired with either the `--relative-paths` option or with the `worktree.useRelativePaths` config set to `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-worktreeConfig)worktreeConfig 
    
If enabled, then worktrees will load config settings from the `$GIT_DIR/config.worktree` file in addition to the `$GIT_COMMON_DIR/config` file. Note that `$GIT_COMMON_DIR` and `$GIT_DIR` are the same for the main working tree, while other working trees have `$GIT_DIR` equal to `$GIT_COMMON_DIR/worktrees/`_< id>_`/`. The settings in the `config.worktree` file will override settings from any other config files.
When enabling this extension, you must be careful to move certain values from the common config file to the main working tree’s `config.worktree` file, if present:
  * `core.worktree` must be moved from `$GIT_COMMON_DIR/config` to `$GIT_COMMON_DIR/config.worktree`.
  * If `core.bare` is true, then it must be moved from `$GIT_COMMON_DIR/config` to `$GIT_COMMON_DIR/config.worktree`.


It may also be beneficial to adjust the locations of `core.sparseCheckout` and `core.sparseCheckoutCone` depending on your desire for customizable sparse-checkout settings for each worktree. By default, the `git` `sparse-checkout` builtin enables this extension, assigns these config values on a per-worktree basis, and uses the `$GIT_DIR/info/sparse-checkout` file to specify the sparsity for each worktree independently. See [git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) for more details.
For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fastimportunpackLimit)fastimport.unpackLimit 
    
If the number of objects imported by [git-fast-import[1]](https://git-scm.com/docs/git-fast-import) is below this limit, then the objects will be unpacked into loose object files. However, if the number of imported objects equals or exceeds this limit, then the pack will be stored as a pack. Storing the pack from a fast-import can make the import operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-feature)feature.* 
    
The config settings that start with `feature.` modify the defaults of a group of other config settings. These groups are created by the Git developer community as recommended defaults and are subject to change. In particular, new config options may be added with different defaults. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-featureexperimental)feature.experimental 
    
Enable config options that are new to Git, and are being considered for future defaults. Config settings included here may be added or removed with each release, including minor version updates. These settings may have unintended interactions since they are so new. Please enable this setting if you are interested in providing feedback on experimental features. The new default values are:
  * `fetch.negotiationAlgorithm=skipping` may improve fetch negotiation times by skipping more commits at a time, reducing the number of round trips.
  * `pack.useBitmapBoundaryTraversal=true` may improve bitmap traversal times by walking fewer objects.
  * `pack.allowPackReuse=multi` may improve the time it takes to create a pack by reusing objects from multiple packs instead of just one.
  * `pack.usePathWalk` may speed up packfile creation and make the packfiles be significantly smaller in the presence of certain filename collisions with Git’s default name-hash.
  * `init.defaultRefFormat=reftable` causes newly initialized repositories to use the reftable format for storing references. This new format solves issues with case-insensitive filesystems, compresses better and performs significantly better with many use cases. Refer to Documentation/technical/reftable.adoc for more information on this new storage format.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-featuremanyFiles)feature.manyFiles 
    
Enable config options that optimize for repos with many files in the working directory. With many files, commands such as `git` `status` and `git` `checkout` may be slow and these new defaults improve performance:
  * `index.skipHash=true` speeds up index writes by not computing a trailing checksum. Note that this will cause Git versions earlier than 2.13.0 to refuse to parse the index and Git versions earlier than 2.40.0 will report a corrupted index during `git` `fsck`.
  * `index.version=4` enables path-prefix compression in the index.
  * `core.untrackedCache=true` enables the untracked cache. This setting assumes that mtime is working on your machine.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchrecurseSubmodules)`fetch.recurseSubmodules` 
    
This option controls whether `git` `fetch` (and the underlying fetch in `git` `pull`) will recursively fetch into populated submodules. This option can be set either to a boolean value or to `on-demand`. Setting it to a boolean changes the behavior of fetch and pull to recurse unconditionally into submodules when set to true or to not recurse at all when set to false. When set to `on-demand`, fetch and pull will only recurse into a populated submodule when its superproject retrieves a commit that updates the submodule’s reference. Defaults to `on-demand`, or to the value of `submodule.recurse` if set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchfsckObjects)`fetch.fsckObjects` 
    
If it is set to true, git-fetch-pack will check all fetched objects. See `transfer.fsckObjects` for what’s checked. Defaults to `false`. If not set, the value of `transfer.fsckObjects` is used instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchfsckmsg-id)`fetch.fsck.`_< msg-id>_ 
    
Acts like `fsck.`_< msg-id>_, but is used by [git-fetch-pack[1]](https://git-scm.com/docs/git-fetch-pack) instead of [git-fsck[1]](https://git-scm.com/docs/git-fsck). See the `fsck.`_< msg-id>_ documentation for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchfsckskipList)`fetch.fsck.skipList` 
    
Acts like `fsck.skipList`, but is used by [git-fetch-pack[1]](https://git-scm.com/docs/git-fetch-pack) instead of [git-fsck[1]](https://git-scm.com/docs/git-fsck). See the `fsck.skipList` documentation for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchunpackLimit)`fetch.unpackLimit` 
    
If the number of objects fetched over the Git native transfer is below this limit, then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchprune)`fetch.prune` 
    
If true, fetch will automatically behave as if the `--prune` option was given on the command line. See also `remote.`_< name>_`.prune` and the PRUNING section of [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchpruneTags)`fetch.pruneTags` 
    
If true, fetch will automatically behave as if the `refs/tags/*:refs/tags/*` refspec was provided when pruning, if not set already. This allows for setting both this option and `fetch.prune` to maintain a 1=1 mapping to upstream refs. See also `remote.`_< name>_`.pruneTags` and the PRUNING section of [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchall)`fetch.all` 
    
If true, fetch will attempt to update all available remotes. This behavior can be overridden by passing `--no-all` or by explicitly specifying one or more remote(s) to fetch from. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchoutput)`fetch.output` 
    
Control how ref update status is printed. Valid values are `full` and `compact`. Default value is `full`. See the OUTPUT section in [git-fetch[1]](https://git-scm.com/docs/git-fetch) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchnegotiationAlgorithm)`fetch.negotiationAlgorithm` 
    
Control how information about the commits in the local repository is sent when negotiating the contents of the packfile to be sent by the server. Set to `consecutive` to use an algorithm that walks over consecutive commits checking each one. Set to `skipping` to use an algorithm that skips commits in an effort to converge faster, but may result in a larger-than-necessary packfile; or set to `noop` to not send any information at all, which will almost certainly result in a larger-than-necessary packfile, but will skip the negotiation step. Set to `default` to override settings made previously and use the default behaviour. The default is normally `consecutive`, but if `feature.experimental` is `true`, then the default is `skipping`. Unknown values will cause `git` `fetch` to error out.
See also the `--negotiate-only` and `--negotiation-tip` options to [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchshowForcedUpdates)`fetch.showForcedUpdates` 
    
Set to `false` to enable `--no-show-forced-updates` in [git-fetch[1]](https://git-scm.com/docs/git-fetch) and [git-pull[1]](https://git-scm.com/docs/git-pull) commands. Defaults to `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchparallel)`fetch.parallel` 
    
Specifies the maximal number of fetch operations to be run in parallel at a time (submodules, or remotes when the `--multiple` option of [git-fetch[1]](https://git-scm.com/docs/git-fetch) is in effect).
A value of 0 will give some reasonable default. If unset, it defaults to 1.
For submodules, this setting can be overridden using the `submodule.fetchJobs` config setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchwriteCommitGraph)`fetch.writeCommitGraph` 
    
Set to true to write a commit-graph after every `git` `fetch` command that downloads a pack-file from a remote. Using the `--split` option, most executions will create a very small commit-graph file on top of the existing commit-graph file(s). Occasionally, these files will merge and the write may take longer. Having an updated commit-graph file helps performance of many Git commands, including `git` `merge-base`, `git` `push` `-f`, and `git` `log` `--graph`. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchbundleURI)`fetch.bundleURI` 
    
This value stores a URI for downloading Git object data from a bundle URI before performing an incremental fetch from the origin Git server. This is similar to how the `--bundle-uri` option behaves in [git-clone[1]](https://git-scm.com/docs/git-clone). `git` `clone` `--bundle-uri` will set the `fetch.bundleURI` value if the supplied bundle URI contains a bundle list that is organized for incremental fetches.
If you modify this value and your repository has a `fetch.bundleCreationToken` value, then remove that `fetch.bundleCreationToken` value before fetching from the new bundle URI. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fetchbundleCreationToken)`fetch.bundleCreationToken` 
    
When using `fetch.bundleURI` to fetch incrementally from a bundle list that uses the "`creationToken`" heuristic, this config value stores the maximum `creationToken` value of the downloaded bundles. This value is used to prevent downloading bundles in the future if the advertised `creationToken` is not strictly larger than this value.
The creation token values are chosen by the provider serving the specific bundle URI. If you modify the URI at `fetch.bundleURI`, then be sure to remove the value for the `fetch.bundleCreationToken` value before fetching. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-filterdriverclean)filter.<driver>.clean 
    
The command which is used to convert the content of a worktree file to a blob upon checkin. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-filterdriversmudge)filter.<driver>.smudge 
    
The command which is used to convert the content of a blob object to a worktree file upon checkout. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatattach)format.attach 
    
Enable multipart/mixed attachments as the default for _format-patch_. The value can also be a double quoted string which will enable attachments as the default and set the value as the boundary. See the --attach option in [git-format-patch[1]](https://git-scm.com/docs/git-format-patch). To countermand an earlier value, set it to an empty string. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatfrom)format.from 
    
Provides the default value for the `--from` option to format-patch. Accepts a boolean value, or a name and email address. If false, format-patch defaults to `--no-from`, using commit authors directly in the "From:" field of patch mails. If true, format-patch defaults to `--from`, using your committer identity in the "From:" field of patch mails and including a "From:" field in the body of the patch mail if different. If set to a non-boolean value, format-patch uses that value instead of your committer identity. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatforceInBodyFrom)format.forceInBodyFrom 
    
Provides the default value for the `--`[`no-`]`force-in-body-from` option to format-patch. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatnumbered)format.numbered 
    
A boolean which can enable or disable sequence numbers in patch subjects. It defaults to "auto" which enables it only if there is more than one patch. It can be enabled or disabled for all messages by setting it to "true" or "false". See --numbered option in [git-format-patch[1]](https://git-scm.com/docs/git-format-patch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatheaders)format.headers 
    
Additional email headers to include in a patch to be submitted by mail. See [git-format-patch[1]](https://git-scm.com/docs/git-format-patch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatto)format.to 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatcc)format.cc 
    
Additional recipients to include in a patch to be submitted by mail. See the --to and --cc options in [git-format-patch[1]](https://git-scm.com/docs/git-format-patch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatsubjectPrefix)format.subjectPrefix 
    
The default for format-patch is to output files with the _[PATCH]_ subject prefix. Use this variable to change that prefix. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatcoverFromDescription)format.coverFromDescription 
    
The default mode for format-patch to determine which parts of the cover letter will be populated using the branch’s description. See the `--cover-from-description` option in [git-format-patch[1]](https://git-scm.com/docs/git-format-patch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatsignature)format.signature 
    
The default for format-patch is to output a signature containing the Git version number. Use this variable to change that default. Set this variable to the empty string ("") to suppress signature generation. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatsignatureFile)format.signatureFile 
    
Works just like format.signature except the contents of the file specified by this variable will be used as the signature. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatsuffix)format.suffix 
    
The default for format-patch is to output files with the suffix `.patch`. Use this variable to change that suffix (make sure to include the dot if you want it). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatencodeEmailHeaders)format.encodeEmailHeaders 
    
Encode email headers that have non-ASCII characters with "Q-encoding" (described in RFC 2047) for email transmission. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatpretty)format.pretty 
    
The default pretty format for log/show/whatchanged command. See [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatthread)format.thread 
    
The default threading style for _git format-patch_. Can be a boolean value, or `shallow` or `deep`. `shallow` threading makes every mail a reply to the head of the series, where the head is chosen from the cover letter, the `--in-reply-to`, and the first patch mail, in this order. `deep` threading makes every mail a reply to the previous one. A true boolean value is the same as `shallow`, and a false value disables threading. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatsignOff)format.signOff 
    
A boolean value which lets you enable the `-s/--signoff` option of format-patch by default. **Note:** Adding the `Signed-off-by` trailer to a patch should be a conscious act and means that you certify you have the rights to submit this work under the same open source license. Please see the _SubmittingPatches_ document for further discussion. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatcoverLetter)format.coverLetter 
    
A boolean that controls whether to generate a cover-letter when format-patch is invoked, but in addition can be set to "auto", to generate a cover-letter only when there’s more than one patch. Default is false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatoutputDirectory)format.outputDirectory 
    
Set a custom directory to store the resulting files instead of the current working directory. All directory components will be created. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatfilenameMaxLength)format.filenameMaxLength 
    
The maximum length of the output filenames generated by the `format-patch` command; defaults to 64. Can be overridden by the `--filename-max-length=`_< n>_ command line option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatuseAutoBase)format.useAutoBase 
    
A boolean value which lets you enable the `--base=auto` option of format-patch by default. Can also be set to "whenAble" to allow enabling `--base=auto` if a suitable base is available, but to skip adding base info otherwise without the format dying. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatnotes)format.notes 
    
Provides the default value for the `--notes` option to format-patch. Accepts a boolean value, or a ref which specifies where to get notes. If false, format-patch defaults to `--no-notes`. If true, format-patch defaults to `--notes`. If set to a non-boolean value, format-patch defaults to `--notes=`_< ref>_, where `ref` is the non-boolean value. Defaults to false.
If one wishes to use the ref `refs/notes/true`, please use that literal instead.
This configuration can be specified multiple times in order to allow multiple notes refs to be included. In that case, it will behave similarly to multiple `--`[`no-`]`notes`[`=`] options passed in. That is, a value of `true` will show the default notes, a value of _< ref>_ will also show notes from that notes ref and a value of `false` will negate previous configurations and not show notes.
For example,
```
[format]
	notes = true
	notes = foo
	notes = false
	notes = bar
```

will only show notes from `refs/notes/bar`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatmboxrd)format.mboxrd 
    
A boolean value which enables the robust "mboxrd" format when `--stdout` is in use to escape "^>+From " lines. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-formatnoprefix)format.noprefix 
    
If set, do not show any source or destination prefix in patches. This is equivalent to the `diff.noprefix` option used by `git` `diff` (but which is not respected by `format-patch`). Note that by setting this, the receiver of any patches you generate will have to apply them using the `-p0` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fsckmsg-id)fsck.<msg-id> 
    
During fsck git may find issues with legacy data which wouldn’t be generated by current versions of git, and which wouldn’t be sent over the wire if `transfer.fsckObjects` was set. This feature is intended to support working with legacy repositories containing such data.
Setting `fsck.`_< msg-id>_ will be picked up by [git-fsck[1]](https://git-scm.com/docs/git-fsck), but to accept pushes of such data set `receive.fsck.`_< msg-id>_ instead, or to clone or fetch it set `fetch.fsck.`_< msg-id>_.
The rest of the documentation discusses `fsck.*` for brevity, but the same applies for the corresponding `receive.fsck.*` and `fetch.fsck.*`. variables.
Unlike variables like `color.ui` and `core.editor`, the `receive.fsck.`_< msg-id>_ and `fetch.fsck.`_< msg-id>_ variables will not fall back on the `fsck.`_< msg-id>_ configuration if they aren’t set. To uniformly configure the same fsck settings in different circumstances, all three of them must be set to the same values.
When `fsck.`_< msg-id>_ is set, errors can be switched to warnings and vice versa by configuring the `fsck.`_< msg-id>_ setting where the _< msg-id>_ is the fsck message ID and the value is one of `error`, `warn` or `ignore`. For convenience, fsck prefixes the error/warning with the message ID, e.g. "missingEmail: invalid author/committer line - missing email" means that setting `fsck.missingEmail` `=` `ignore` will hide that issue.
In general, it is better to enumerate existing objects with problems with `fsck.skipList`, instead of listing the kind of breakages these problematic objects share to be ignored, as doing the latter will allow new instances of the same breakages go unnoticed.
Setting an unknown `fsck.`_< msg-id>_ value will cause fsck to die, but doing the same for `receive.fsck.`_< msg-id>_ and `fetch.fsck.`_< msg-id>_ will only cause git to warn.
See the `Fsck` `Messages` section of [git-fsck[1]](https://git-scm.com/docs/git-fsck) for supported values of _< msg-id>_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fsckskipList)fsck.skipList 
    
The path to a list of object names (i.e. one unabbreviated SHA-1 per line) that are known to be broken in a non-fatal way and should be ignored. On versions of Git 2.20 and later, comments (_#_), empty lines, and any leading and trailing whitespace are ignored. Everything but a SHA-1 per line will error out on older versions.
This feature is useful when an established project should be accepted despite early commits containing errors that can be safely ignored, such as invalid committer email addresses. Note: corrupt objects cannot be skipped with this setting.
Like `fsck.`_< msg-id>_ this variable has corresponding `receive.fsck.skipList` and `fetch.fsck.skipList` variants.
Unlike variables like `color.ui` and `core.editor` the `receive.fsck.skipList` and `fetch.fsck.skipList` variables will not fall back on the `fsck.skipList` configuration if they aren’t set. To uniformly configure the same fsck settings in different circumstances, all three of them must be set to the same values.
Older versions of Git (before 2.20) documented that the object names list should be sorted. This was never a requirement; the object names could appear in any order, but when reading the list we tracked whether the list was sorted for the purposes of an internal binary search implementation, which could save itself some work with an already sorted list. Unless you had a humongous list there was no reason to go out of your way to pre-sort the list. After Git version 2.20 a hash implementation is used instead, so there’s now no reason to pre-sort the list. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fsmonitorallowRemote)fsmonitor.allowRemote 
    
By default, the fsmonitor daemon refuses to work with network-mounted repositories. Setting `fsmonitor.allowRemote` to `true` overrides this behavior. Only respected when `core.fsmonitor` is set to `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-fsmonitorsocketDir)fsmonitor.socketDir 
    
This Mac OS-specific option, if set, specifies the directory in which to create the Unix domain socket used for communication between the fsmonitor daemon and various Git commands. The directory must reside on a native Mac OS filesystem. Only respected when `core.fsmonitor` is set to `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcaggressiveDepth)gc.aggressiveDepth 
    
The depth parameter used in the delta compression algorithm used by _git gc --aggressive_. This defaults to 50, which is the default for the `--depth` option when `--aggressive` isn’t in use.
See the documentation for the `--depth` option in [git-repack[1]](https://git-scm.com/docs/git-repack) for more details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcaggressiveWindow)gc.aggressiveWindow 
    
The window size parameter used in the delta compression algorithm used by _git gc --aggressive_. This defaults to 250, which is a much more aggressive window size than the default `--window` of 10.
See the documentation for the `--window` option in [git-repack[1]](https://git-scm.com/docs/git-repack) for more details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcauto)gc.auto 
    
When there are approximately more than this many loose objects in the repository, `git` `gc` `--auto` will pack them. Some Porcelain commands use this command to perform a light-weight garbage collection from time to time. The default value is 6700.
Setting this to 0 disables not only automatic packing based on the number of loose objects, but also any other heuristic `git` `gc` `--auto` will otherwise use to determine if there’s work to do, such as `gc.autoPackLimit`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcautoPackLimit)gc.autoPackLimit 
    
When there are more than this many packs that are not marked with `*.keep` file in the repository, `git` `gc` `--auto` consolidates them into one larger pack. The default value is 50. Setting this to 0 disables it. Setting `gc.auto` to 0 will also disable this.
See the `gc.bigPackThreshold` configuration variable below. When in use, it’ll affect how the auto pack limit works. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcautoDetach)gc.autoDetach 
    
Make `git` `gc` `--auto` return immediately and run in the background if the system supports it. Default is true. This config variable acts as a fallback in case `maintenance.autoDetach` is not set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcbigPackThreshold)gc.bigPackThreshold 
    
If non-zero, all non-cruft packs larger than this limit are kept when `git` `gc` is run. This is very similar to `--keep-largest-pack` except that all non-cruft packs that meet the threshold are kept, not just the largest pack. Defaults to zero. Common unit suffixes of _k_ , _m_ , or _g_ are supported.
Note that if the number of kept packs is more than gc.autoPackLimit, this configuration variable is ignored, all packs except the base pack will be repacked. After this the number of packs should go below gc.autoPackLimit and gc.bigPackThreshold should be respected again.
If the amount of memory estimated for `git` `repack` to run smoothly is not available and `gc.bigPackThreshold` is not set, the largest pack will also be excluded (this is the equivalent of running `git` `gc` with `--keep-largest-pack`). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcwriteCommitGraph)gc.writeCommitGraph 
    
If true, then gc will rewrite the commit-graph file when [git-gc[1]](https://git-scm.com/docs/git-gc) is run. When using `git` `gc` `--auto` the commit-graph will be updated if housekeeping is required. Default is true. See [git-commit-graph[1]](https://git-scm.com/docs/git-commit-graph) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gclogExpiry)gc.logExpiry 
    
If the file gc.log exists, then `git` `gc` `--auto` will print its content and exit with status zero instead of running unless that file is more than _gc.logExpiry_ old. Default is "1.day". See `gc.pruneExpire` for more ways to specify its value. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcpackRefs)gc.packRefs 
    
Running `git` `pack-refs` in a repository renders it unclonable by Git versions prior to 1.5.1.2 over dumb transports such as HTTP. This variable determines whether _git gc_ runs `git` `pack-refs`. This can be set to `notbare` to enable it within all non-bare repos or it can be set to a boolean value. The default is `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gccruftPacks)gc.cruftPacks 
    
Store unreachable objects in a cruft pack (see [git-repack[1]](https://git-scm.com/docs/git-repack)) instead of as loose objects. The default is `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcmaxCruftSize)gc.maxCruftSize 
    
Limit the size of new cruft packs when repacking. When specified in addition to `--max-cruft-size`, the command line option takes priority. See the `--max-cruft-size` option of [git-repack[1]](https://git-scm.com/docs/git-repack). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcpruneExpire)gc.pruneExpire 
    
When _git gc_ is run, it will call _prune --expire 2.weeks.ago_ (and _repack --cruft --cruft-expiration 2.weeks.ago_ if using cruft packs via `gc.cruftPacks` or `--cruft`). Override the grace period with this config variable. The value "now" may be used to disable this grace period and always prune unreachable objects immediately, or "never" may be used to suppress pruning. This feature helps prevent corruption when _git gc_ runs concurrently with another process writing to the repository; see the "NOTES" section of [git-gc[1]](https://git-scm.com/docs/git-gc). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcworktreePruneExpire)gc.worktreePruneExpire 
    
When _git gc_ is run, it calls _git worktree prune --expire 3.months.ago_. This config variable can be used to set a different grace period. The value "now" may be used to disable the grace period and prune `$GIT_DIR/worktrees` immediately, or "never" may be used to suppress pruning. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcreflogExpire)gc.reflogExpire 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcpatternreflogExpire)gc.<pattern>.reflogExpire 
    
_git reflog expire_ removes reflog entries older than this time; defaults to 90 days. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. With "<pattern>" (e.g. "refs/stash") in the middle the setting applies only to the refs that match the <pattern>. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcreflogExpireUnreachable)gc.reflogExpireUnreachable 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcpatternreflogExpireUnreachable)gc.<pattern>.reflogExpireUnreachable 
    
_git reflog expire_ removes reflog entries older than this time and are not reachable from the current tip; defaults to 30 days. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. With "<pattern>" (e.g. "refs/stash") in the middle, the setting applies only to the refs that match the <pattern>.
These types of entries are generally created as a result of using `git` `commit` `--amend` or `git` `rebase` and are the commits prior to the amend or rebase occurring. Since these changes are not part of the current project most users will want to expire them sooner, which is why the default is more aggressive than `gc.reflogExpire`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrecentObjectsHook)gc.recentObjectsHook 
    
When considering whether or not to remove an object (either when generating a cruft pack or storing unreachable objects as loose), use the shell to execute the specified command(s). Interpret their output as object IDs which Git will consider as "recent", regardless of their age. By treating their mtimes as "now", any objects (and their descendants) mentioned in the output will be kept regardless of their true age.
Output must contain exactly one hex object ID per line, and nothing else. Objects which cannot be found in the repository are ignored. Multiple hooks are supported, but all must exit successfully, else the operation (either generating a cruft pack or unpacking unreachable objects) will be halted. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrepackFilter)gc.repackFilter 
    
When repacking, use the specified filter to move certain objects into a separate packfile. See the `--filter=`_< filter-spec>_ option of [git-repack[1]](https://git-scm.com/docs/git-repack). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrepackFilterTo)gc.repackFilterTo 
    
When repacking and using a filter, see `gc.repackFilter`, the specified location will be used to create the packfile containing the filtered out objects. **WARNING:** The specified location should be accessible, using for example the Git alternates mechanism, otherwise the repo could be considered corrupt by Git as it might not be able to access the objects in that packfile. See the `--filter-to=`_< dir>_ option of [git-repack[1]](https://git-scm.com/docs/git-repack) and the `objects/info/alternates` section of [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrerereResolved)gc.rerereResolved 
    
Records of conflicted merge you resolved earlier are kept for this many days when _git rerere gc_ is run. You can also use more human-readable "1.month.ago", etc. The default is 60 days. See [git-rerere[1]](https://git-scm.com/docs/git-rerere). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrerereUnresolved)gc.rerereUnresolved 
    
Records of conflicted merge you have not resolved are kept for this many days when _git rerere gc_ is run. You can also use more human-readable "1.month.ago", etc. The default is 15 days. See [git-rerere[1]](https://git-scm.com/docs/git-rerere). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvscommitMsgAnnotation)gitcvs.commitMsgAnnotation 
    
Append this string to each commit message. Set to empty string to disable this feature. Defaults to "via git-CVS emulator". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsenabled)gitcvs.enabled 
    
Whether the CVS server interface is enabled for this repository. See [git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvslogFile)gitcvs.logFile 
    
Path to a log file where the CVS server interface well…​ logs various stuff. See [git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsusecrlfattr)gitcvs.usecrlfattr 
    
If true, the server will look up the end-of-line conversion attributes for files to determine the `-k` modes to use. If the attributes force Git to treat a file as text, the `-k` mode will be left blank so CVS clients will treat it as text. If they suppress text conversion, the file will be set with _-kb_ mode, which suppresses any newline munging the client might otherwise do. If the attributes do not allow the file type to be determined, then `gitcvs.allBinary` is used. See [gitattributes[5]](https://git-scm.com/docs/gitattributes). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsallBinary)gitcvs.allBinary 
    
This is used if `gitcvs.usecrlfattr` does not resolve the correct _-kb_ mode to use. If true, all unresolved files are sent to the client in mode _-kb_. This causes the client to treat them as binary files, which suppresses any newline munging it otherwise might do. Alternatively, if it is set to "guess", then the contents of the file are examined to decide if it is binary, similar to `core.autocrlf`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsdbName)gitcvs.dbName 
    
Database used by git-cvsserver to cache revision information derived from the Git repository. The exact meaning depends on the used database driver, for SQLite (which is the default driver) this is a filename. Supports variable substitution (see [git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver) for details). May not contain semicolons (_;_). Default: _%Ggitcvs.%m.sqlite_ 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsdbDriver)gitcvs.dbDriver 
    
Used Perl DBI driver. You can specify any available driver for this here, but it might not work. git-cvsserver is tested with _DBD::SQLite_ , reported to work with _DBD::Pg_ , and reported **not** to work with _DBD::mysql_. Experimental feature. May not contain double colons (`:`). Default: _SQLite_. See [git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsdbUser)gitcvs.dbUser 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsdbPass)gitcvs.dbPass 
    
Database user and password. Only useful if setting `gitcvs.dbDriver`, since SQLite has no concept of database users and/or passwords. _gitcvs.dbUser_ supports variable substitution (see [git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver) for details). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitcvsdbTableNamePrefix)gitcvs.dbTableNamePrefix 
    
Database table name prefix. Prepended to the names of any database tables used, allowing a single database to be used for several repositories. Supports variable substitution (see [git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver) for details). Any non-alphabetic characters will be replaced with underscores.
All gitcvs variables except for `gitcvs.usecrlfattr` and `gitcvs.allBinary` can also be specified as _gitcvs. <access_method>.<varname>_ (where _access_method_ is one of "ext" and "pserver") to make them apply only for the given access method. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebcategory)gitweb.category 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebdescription)gitweb.description 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebowner)gitweb.owner 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitweburl)gitweb.url 
    
See [gitweb[1]](https://git-scm.com/docs/gitweb) for description. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebavatar)gitweb.avatar 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebblame)gitweb.blame 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebgrep)gitweb.grep 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebhighlight)gitweb.highlight 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebpatches)gitweb.patches 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebpickaxe)gitweb.pickaxe 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebremoteheads)gitweb.remote_heads 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebshowSizes)gitweb.showSizes 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gitwebsnapshot)gitweb.snapshot 
    
See [gitweb.conf[5]](https://git-scm.com/docs/gitweb.conf) for description. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gpgprogram)gpg.program 
    
Pathname of the program to use instead of "`gpg`" when making or verifying a PGP signature. The program must support the same command-line interface as GPG, namely, to verify a detached signature, "_gpg --verify $signature - <$file_" is run, and the program is expected to signal a good signature by exiting with code 0. To generate an ASCII-armored detached signature, the standard input of "`gpg` `-bsau` `$key`" is fed with the contents to be signed, and the program is expected to send the result to its standard output. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gpgformat)gpg.format 
    
Specifies which key format to use when signing with `--gpg-sign`. Default is "openpgp". Other possible values are "x509", "ssh".
See [gitformat-signature[5]](https://git-scm.com/docs/gitformat-signature) for the signature format, which differs based on the selected `gpg.format`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gpgformatprogram)gpg.<format>.program 
    
Use this to customize the program used for the signing format you chose. (see `gpg.program` and `gpg.format`) `gpg.program` can still be used as a legacy synonym for `gpg.openpgp.program`. The default value for `gpg.x509.program` is "gpgsm" and `gpg.ssh.program` is "ssh-keygen". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gpgminTrustLevel)gpg.minTrustLevel 
    
Specifies a minimum trust level for signature verification. If this option is unset, then signature verification for merge operations requires a key with at least `marginal` trust. Other operations that perform signature verification require a key with at least `undefined` trust. Setting this option overrides the required trust-level for all operations. Supported values, in increasing order of significance:
  * `undefined`
  * `never`
  * `marginal`
  * `fully`
  * `ultimate`



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gpgsshdefaultKeyCommand)gpg.ssh.defaultKeyCommand 
    
This command will be run when user.signingkey is not set and a ssh signature is requested. On successful exit a valid ssh public key prefixed with `key::` is expected in the first line of its output. This allows for a script doing a dynamic lookup of the correct public key when it is impractical to statically configure `user.signingKey`. For example when keys or SSH Certificates are rotated frequently or selection of the right key depends on external factors unknown to git. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gpgsshallowedSignersFile)gpg.ssh.allowedSignersFile 
    
A file containing ssh public keys which you are willing to trust. The file consists of one or more lines of principals followed by an ssh public key. e.g.: `user1@example.com,user2@example.com` `ssh-rsa` `AAAAX1...` See ssh-keygen(1) "ALLOWED SIGNERS" for details. The principal is only used to identify the key and is available when verifying a signature.
SSH has no concept of trust levels like gpg does. To be able to differentiate between valid signatures and trusted signatures the trust level of a signature verification is set to `fully` when the public key is present in the allowedSignersFile. Otherwise the trust level is `undefined` and git verify-commit/tag will fail.
This file can be set to a location outside of the repository and every developer maintains their own trust store. A central repository server could generate this file automatically from ssh keys with push access to verify the code against. In a corporate setting this file is probably generated at a global location from automation that already handles developer ssh keys.
A repository that only allows signed commits can store the file in the repository itself using a path relative to the top-level of the working tree. This way only committers with an already valid key can add or change keys in the keyring.
Since OpensSSH 8.8 this file allows specifying a key lifetime using valid-after & valid-before options. Git will mark signatures as valid if the signing key was valid at the time of the signature’s creation. This allows users to change a signing key without invalidating all previously made signatures.
Using a SSH CA key with the cert-authority option (see ssh-keygen(1) "CERTIFICATES") is also valid. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-gpgsshrevocationFile)gpg.ssh.revocationFile 
    
Either a SSH KRL or a list of revoked public keys (without the principal prefix). See ssh-keygen(1) for details. If a public key is found in this file then it will always be treated as having trust level "never" and signatures will show as invalid. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-greplineNumber)grep.lineNumber 
    
If set to true, enable `-n` option by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-grepcolumn)grep.column 
    
If set to true, enable the `--column` option by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-greppatternType)grep.patternType 
    
Set the default matching behavior. Using a value of _basic_ , _extended_ , _fixed_ , or _perl_ will enable the `--basic-regexp`, `--extended-regexp`, `--fixed-strings`, or `--perl-regexp` option accordingly, while the value _default_ will use the `grep.extendedRegexp` option to choose between _basic_ and _extended_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-grepextendedRegexp)grep.extendedRegexp 
    
If set to true, enable `--extended-regexp` option by default. This option is ignored when the `grep.patternType` option is set to a value other than _default_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-grepthreads)grep.threads 
    
Number of grep worker threads to use. If unset (or set to 0), Git will use as many threads as the number of logical cores available. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-grepfullName)grep.fullName 
    
If set to true, enable `--full-name` option by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-grepfallbackToNoIndex)grep.fallbackToNoIndex 
    
If set to true, fall back to `git` `grep` `--no-index` if `git` `grep` is executed outside of a git repository. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guicommitMsgWidth)gui.commitMsgWidth 
    
Defines how wide the commit message window is in the [git-gui[1]](https://git-scm.com/docs/git-gui). "75" is the default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guidiffContext)gui.diffContext 
    
Specifies how many context lines should be used in calls to diff made by the [git-gui[1]](https://git-scm.com/docs/git-gui). The default is "5". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guidisplayUntracked)gui.displayUntracked 
    
Determines if [git-gui[1]](https://git-scm.com/docs/git-gui) shows untracked files in the file list. The default is "true". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guiencoding)gui.encoding 
    
Specifies the default character encoding to use for displaying of file contents in [git-gui[1]](https://git-scm.com/docs/git-gui) and [gitk[1]](https://git-scm.com/docs/gitk). It can be overridden by setting the _encoding_ attribute for relevant files (see [gitattributes[5]](https://git-scm.com/docs/gitattributes)). If this option is not set, the tools default to the locale encoding. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guimatchTrackingBranch)gui.matchTrackingBranch 
    
Determines if new branches created with [git-gui[1]](https://git-scm.com/docs/git-gui) should default to tracking remote branches with matching names or not. Default: "false". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guinewBranchTemplate)gui.newBranchTemplate 
    
Is used as a suggested name when creating new branches using the [git-gui[1]](https://git-scm.com/docs/git-gui). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guipruneDuringFetch)gui.pruneDuringFetch 
    
"true" if [git-gui[1]](https://git-scm.com/docs/git-gui) should prune remote-tracking branches when performing a fetch. The default value is "false". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitrustmtime)gui.trustmtime 
    
Determines if [git-gui[1]](https://git-scm.com/docs/git-gui) should trust the file modification timestamp or not. By default the timestamps are not trusted. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guispellingDictionary)gui.spellingDictionary 
    
Specifies the dictionary used for spell checking commit messages in the [git-gui[1]](https://git-scm.com/docs/git-gui). When set to "none" spell checking is turned off. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guifastCopyBlame)gui.fastCopyBlame 
    
If true, _git gui blame_ uses `-C` instead of `-C` `-C` for original location detection. It makes blame significantly faster on huge repositories at the expense of less thorough copy detection. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guicopyBlameThreshold)gui.copyBlameThreshold 
    
Specifies the threshold to use in _git gui blame_ original location detection, measured in alphanumeric characters. See the [git-blame[1]](https://git-scm.com/docs/git-blame) manual for more information on copy detection. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guiblamehistoryctx)gui.blamehistoryctx 
    
Specifies the radius of history context in days to show in [gitk[1]](https://git-scm.com/docs/gitk) for the selected commit, when the `Show` `History` `Context` menu item is invoked from _git gui blame_. If this variable is set to zero, the whole history is shown. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guiGCWarning)gui.GCWarning 
    
Determines whether [git-gui[1]](https://git-scm.com/docs/git-gui) should prompt for garbage collection when git detects a large number of loose objects in the repository. The default value is "true". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnamecmd)guitool.<name>.cmd 
    
Specifies the shell command line to execute when the corresponding item of the [git-gui[1]](https://git-scm.com/docs/git-gui) `Tools` menu is invoked. This option is mandatory for every tool. The command is executed from the root of the working directory, and in the environment it receives the name of the tool as `GIT_GUITOOL`, the name of the currently selected file as _FILENAME_ , and the name of the current branch as _CUR_BRANCH_ (if the head is detached, _CUR_BRANCH_ is empty). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnameneedsFile)guitool.<name>.needsFile 
    
Run the tool only if a diff is selected in the GUI. It guarantees that _FILENAME_ is not empty. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnamenoConsole)guitool.<name>.noConsole 
    
Run the command silently, without creating a window to display its output. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnamenoRescan)guitool.<name>.noRescan 
    
Don’t rescan the working directory for changes after the tool finishes execution. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnameconfirm)guitool.<name>.confirm 
    
Show a confirmation dialog before actually running the tool. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnameargPrompt)guitool.<name>.argPrompt 
    
Request a string argument from the user, and pass it to the tool through the `ARGS` environment variable. Since requesting an argument implies confirmation, the _confirm_ option has no effect if this is enabled. If the option is set to _true_ , _yes_ , or _1_ , the dialog uses a built-in generic prompt; otherwise the exact value of the variable is used. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnamerevPrompt)guitool.<name>.revPrompt 
    
Request a single valid revision from the user, and set the `REVISION` environment variable. In other aspects this option is similar to _argPrompt_ , and can be used together with it. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnamerevUnmerged)guitool.<name>.revUnmerged 
    
Show only unmerged branches in the _revPrompt_ subdialog. This is useful for tools similar to merge or rebase, but not for things like checkout or reset. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnametitle)guitool.<name>.title 
    
Specifies the title to use for the prompt dialog. The default is the tool name. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-guitoolnameprompt)guitool.<name>.prompt 
    
Specifies the general prompt string to display at the top of the dialog, before subsections for _argPrompt_ and _revPrompt_. The default value includes the actual command. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpbrowser)help.browser 
    
Specify the browser that will be used to display help in the _web_ format. See [git-help[1]](https://git-scm.com/docs/git-help). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpformat)help.format 
    
Override the default help format used by [git-help[1]](https://git-scm.com/docs/git-help). Values _man_ , _info_ , _web_ and _html_ are supported. _man_ is the default. _web_ and _html_ are the same. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpautoCorrect)help.autoCorrect 
    
If git detects typos and can identify exactly one valid command similar to the error, git will try to suggest the correct command or even run the suggestion automatically. Possible config values are:
  * 0, "false", "off", "no", "show": show the suggested command (default).
  * 1, "true", "on", "yes", "immediate": run the suggested command immediately.
  * positive number > 1: run the suggested command after specified deciseconds (0.1 sec).
  * "never": don’t run or show any suggested command.
  * "prompt": show the suggestion and prompt for confirmation to run the command.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-helphtmlPath)help.htmlPath 
    
Specify the path where the HTML documentation resides. File system paths and URLs are supported. HTML pages will be prefixed with this path when help is displayed in the _web_ format. This defaults to the documentation path of your Git installation. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpproxy)http.proxy 
    
Override the HTTP proxy, normally configured using the _http_proxy_ , _https_proxy_ , and _all_proxy_ environment variables (see `curl`(`1`)). In addition to the syntax understood by curl, it is possible to specify a proxy string with a user name but no password, in which case git will attempt to acquire one in the same way it does for other credentials. See [gitcredentials[7]](https://git-scm.com/docs/gitcredentials) for more information. The syntax thus is _[protocol://][user[:password]@]proxyhost[:port][/path]_. This can be overridden on a per-remote basis; see remote.<name>.proxy
Any proxy, however configured, must be completely transparent and must not modify, transform, or buffer the request or response in any way. Proxies which are not completely transparent are known to cause various forms of breakage with Git. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpproxyAuthMethod)http.proxyAuthMethod 
    
Set the method with which to authenticate against the HTTP proxy. This only takes effect if the configured proxy string contains a user name part (i.e. is of the form _user@host_ or _user@host:port_). This can be overridden on a per-remote basis; see `remote.`_< name>_`.proxyAuthMethod`. Both can be overridden by the `GIT_HTTP_PROXY_AUTHMETHOD` environment variable. Possible values are:
  * `anyauth` - Automatically pick a suitable authentication method. It is assumed that the proxy answers an unauthenticated request with a 407 status code and one or more Proxy-authenticate headers with supported authentication methods. This is the default.
  * `basic` - HTTP Basic authentication
  * `digest` - HTTP Digest authentication; this prevents the password from being transmitted to the proxy in clear text
  * `negotiate` - GSS-Negotiate authentication (compare the --negotiate option of `curl`(`1`))
  * `ntlm` - NTLM authentication (compare the --ntlm option of `curl`(`1`))



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpproxySSLCert)http.proxySSLCert 
    
The pathname of a file that stores a client certificate to use to authenticate with an HTTPS proxy. Can be overridden by the `GIT_PROXY_SSL_CERT` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpproxySSLKey)http.proxySSLKey 
    
The pathname of a file that stores a private key to use to authenticate with an HTTPS proxy. Can be overridden by the `GIT_PROXY_SSL_KEY` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpproxySSLCertPasswordProtected)http.proxySSLCertPasswordProtected 
    
Enable Git’s password prompt for the proxy SSL certificate. Otherwise OpenSSL will prompt the user, possibly many times, if the certificate or private key is encrypted. Can be overridden by the `GIT_PROXY_SSL_CERT_PASSWORD_PROTECTED` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpproxySSLCAInfo)http.proxySSLCAInfo 
    
Pathname to the file containing the certificate bundle that should be used to verify the proxy with when using an HTTPS proxy. Can be overridden by the `GIT_PROXY_SSL_CAINFO` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpemptyAuth)http.emptyAuth 
    
Attempt authentication without seeking a username or password. This can be used to attempt GSS-Negotiate authentication without specifying a username in the URL, as libcurl normally requires a username for authentication. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpproactiveAuth)http.proactiveAuth 
    
Attempt authentication without first making an unauthenticated attempt and receiving a 401 response. This can be used to ensure that all requests are authenticated. If `http.emptyAuth` is set to true, this value has no effect.
If the credential helper used specifies an authentication scheme (i.e., via the `authtype` field), that value will be used; if a username and password is provided without a scheme, then Basic authentication is used. The value of the option determines the scheme requested from the helper. Possible values are:
  * `basic` - Request Basic authentication from the helper.
  * `auto` - Allow the helper to pick an appropriate scheme.
  * `none` - Disable proactive authentication.


Note that TLS should always be used with this configuration, since otherwise it is easy to accidentally expose plaintext credentials if Basic authentication is selected. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpdelegation)http.delegation 
    
Control GSSAPI credential delegation. The delegation is disabled by default in libcurl since version 7.21.7. Set parameter to tell the server what it is allowed to delegate when it comes to user credentials. Used with GSS/kerberos. Possible values are:
  * `none` - Don’t allow any delegation.
  * `policy` - Delegates if and only if the OK-AS-DELEGATE flag is set in the Kerberos service ticket, which is a matter of realm policy.
  * `always` - Unconditionally allow the server to delegate.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpextraHeader)http.extraHeader 
    
Pass an additional HTTP header when communicating with a server. If more than one such entry exists, all of them are added as extra headers. To allow overriding the settings inherited from the system config, an empty value will reset the extra headers to the empty list. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpcookieFile)http.cookieFile 
    
The pathname of a file containing previously stored cookie lines, which should be used in the Git http session, if they match the server. The file format of the file to read cookies from should be plain HTTP headers or the Netscape/Mozilla cookie file format (see `curl`(`1`)). Set it to an empty string, to accept only new cookies from the server and send them back in successive requests within same connection. NOTE that the file specified with http.cookieFile is used only as input unless http.saveCookies is set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsaveCookies)http.saveCookies 
    
If set, store cookies received during requests to the file specified by http.cookieFile. Has no effect if http.cookieFile is unset, or set to an empty string. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpversion)http.version 
    
Use the specified HTTP protocol version when communicating with a server. If you want to force the default. The available and default version depend on libcurl. Currently the possible values of this option are:
  * HTTP/2
  * HTTP/1.1



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpcurloptResolve)http.curloptResolve 
    
Hostname resolution information that will be used first by libcurl when sending HTTP requests. This information should be in one of the following formats:
  * [+]HOST:PORT:ADDRESS[,ADDRESS]
  * -HOST:PORT


The first format redirects all requests to the given `HOST:PORT` to the provided `ADDRESS`(s). The second format clears all previous config values for that `HOST:PORT` combination. To allow easy overriding of all the settings inherited from the system config, an empty value will reset all resolution information to the empty list. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslVersion)http.sslVersion 
    
The SSL version to use when negotiating an SSL connection, if you want to force the default. The available and default version depend on whether libcurl was built against NSS or OpenSSL and the particular configuration of the crypto library in use. Internally this sets the _CURLOPT_SSL_VERSION_ option; see the libcurl documentation for more details on the format of this option and for the ssl version supported. Currently the possible values of this option are:
  * sslv2
  * sslv3
  * tlsv1
  * tlsv1.0
  * tlsv1.1
  * tlsv1.2
  * tlsv1.3


Can be overridden by the `GIT_SSL_VERSION` environment variable. To force git to use libcurl’s default ssl version and ignore any explicit http.sslversion option, set `GIT_SSL_VERSION` to the empty string. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslCipherList)http.sslCipherList 
    
A list of SSL ciphers to use when negotiating an SSL connection. The available ciphers depend on whether libcurl was built against NSS or OpenSSL and the particular configuration of the crypto library in use. Internally this sets the _CURLOPT_SSL_CIPHER_LIST_ option; see the libcurl documentation for more details on the format of this list.
Can be overridden by the `GIT_SSL_CIPHER_LIST` environment variable. To force git to use libcurl’s default cipher list and ignore any explicit http.sslCipherList option, set `GIT_SSL_CIPHER_LIST` to the empty string. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslVerify)http.sslVerify 
    
Whether to verify the SSL certificate when fetching or pushing over HTTPS. Defaults to true. Can be overridden by the `GIT_SSL_NO_VERIFY` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslCert)http.sslCert 
    
File containing the SSL certificate when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_CERT` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslKey)http.sslKey 
    
File containing the SSL private key when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_KEY` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslCertPasswordProtected)http.sslCertPasswordProtected 
    
Enable Git’s password prompt for the SSL certificate. Otherwise OpenSSL will prompt the user, possibly many times, if the certificate or private key is encrypted. Can be overridden by the `GIT_SSL_CERT_PASSWORD_PROTECTED` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslCAInfo)http.sslCAInfo 
    
File containing the certificates to verify the peer with when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_CAINFO` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslCAPath)http.sslCAPath 
    
Path containing files with the CA certificates to verify the peer with when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_CAPATH` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslBackend)http.sslBackend 
    
Name of the SSL backend to use (e.g. "openssl" or "schannel"). This option is ignored if cURL lacks support for choosing the SSL backend at runtime. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslCertType)http.sslCertType 
    
Type of client certificate used when fetching or pushing over HTTPS. "PEM", "DER" are supported when using openssl or gnutls backends. "P12" is supported on "openssl", "schannel", "securetransport", and gnutls 8.11+. See also libcurl `CURLOPT_SSLCERTTYPE`. Can be overridden by the `GIT_SSL_CERT_TYPE` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslKeyType)http.sslKeyType 
    
Type of client private key used when fetching or pushing over HTTPS. (e.g. "PEM", "DER", or "ENG"). Only applicable when using "openssl" backend. "DER" is not supported with openssl. Particularly useful when set to "ENG" for authenticating with PKCS#11 tokens, with a PKCS#11 URL in sslCert option. See also libcurl `CURLOPT_SSLKEYTYPE`. Can be overridden by the `GIT_SSL_KEY_TYPE` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpschannelCheckRevoke)http.schannelCheckRevoke 
    
Used to enforce or disable certificate revocation checks in cURL when http.sslBackend is set to "schannel". Defaults to `true` if unset. Only necessary to disable this if Git consistently errors and the message is about checking the revocation status of a certificate. This option is ignored if cURL lacks support for setting the relevant SSL option at runtime. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpschannelUseSSLCAInfo)http.schannelUseSSLCAInfo 
    
As of cURL v7.60.0, the Secure Channel backend can use the certificate bundle provided via `http.sslCAInfo`, but that would override the Windows Certificate Store. Since this is not desirable by default, Git will tell cURL not to use that bundle by default when the `schannel` backend was configured via `http.sslBackend`, unless `http.schannelUseSSLCAInfo` overrides this behavior. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httppinnedPubkey)http.pinnedPubkey 
    
Public key of the https service. It may either be the filename of a PEM or DER encoded public key file or a string starting with _sha256//_ followed by the base64 encoded sha256 hash of the public key. See also libcurl _CURLOPT_PINNEDPUBLICKEY_. git will exit with an error if this option is set but not supported by cURL. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpsslTry)http.sslTry 
    
Attempt to use AUTH SSL/TLS and encrypted data transfers when connecting via regular FTP protocol. This might be needed if the FTP server requires it for security reasons or you wish to connect securely whenever remote FTP server supports it. Default is false since it might trigger certificate verification errors on misconfigured servers. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpmaxRequests)http.maxRequests 
    
How many HTTP requests to launch in parallel. Can be overridden by the `GIT_HTTP_MAX_REQUESTS` environment variable. Default is 5. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpminSessions)http.minSessions 
    
The number of curl sessions (counted across slots) to be kept across requests. They will not be ended with curl_easy_cleanup() until http_cleanup() is invoked. If USE_CURL_MULTI is not defined, this value will be capped at 1. Defaults to 1. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httppostBuffer)http.postBuffer 
    
Maximum size in bytes of the buffer used by smart HTTP transports when POSTing data to the remote system. For requests larger than this buffer size, HTTP/1.1 and Transfer-Encoding: chunked is used to avoid creating a massive pack file locally. Default is 1 MiB, which is sufficient for most requests.
Note that raising this limit is only effective for disabling chunked transfer encoding and therefore should be used only where the remote server or a proxy only supports HTTP/1.0 or is noncompliant with the HTTP standard. Raising this is not, in general, an effective solution for most push problems, but can increase memory consumption significantly since the entire buffer is allocated even for small pushes. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httplowSpeedLimit)http.lowSpeedLimit 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httplowSpeedTime)http.lowSpeedTime 
    
If the HTTP transfer speed, in bytes per second, is less than _http.lowSpeedLimit_ for longer than _http.lowSpeedTime_ seconds, the transfer is aborted. Can be overridden by the `GIT_HTTP_LOW_SPEED_LIMIT` and `GIT_HTTP_LOW_SPEED_TIME` environment variables. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpkeepAliveIdle)http.keepAliveIdle 
    
Specifies how long in seconds to wait on an idle connection before sending TCP keepalive probes (if supported by the OS). If unset, curl’s default value is used. Can be overridden by the `GIT_HTTP_KEEPALIVE_IDLE` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpkeepAliveInterval)http.keepAliveInterval 
    
Specifies how long in seconds to wait between TCP keepalive probes (if supported by the OS). If unset, curl’s default value is used. Can be overridden by the `GIT_HTTP_KEEPALIVE_INTERVAL` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpkeepAliveCount)http.keepAliveCount 
    
Specifies how many TCP keepalive probes to send before giving up and terminating the connection (if supported by the OS). If unset, curl’s default value is used. Can be overridden by the `GIT_HTTP_KEEPALIVE_COUNT` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpnoEPSV)http.noEPSV 
    
A boolean which disables using of EPSV ftp command by curl. This can be helpful with some "poor" ftp servers which don’t support EPSV mode. Can be overridden by the `GIT_CURL_FTP_NO_EPSV` environment variable. Default is false (curl will use EPSV). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpuserAgent)http.userAgent 
    
The HTTP USER_AGENT string presented to an HTTP server. The default value represents the version of the Git client such as git/1.7.1. This option allows you to override this value to a more common value such as Mozilla/4.0. This may be necessary, for instance, if connecting through a firewall that restricts HTTP connections to a set of common USER_AGENT strings (but not including those like git/1.7.1). Can be overridden by the `GIT_HTTP_USER_AGENT` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpfollowRedirects)http.followRedirects 
    
Whether git should follow HTTP redirects. If set to `true`, git will transparently follow any redirect issued by a server it encounters. If set to `false`, git will treat all redirects as errors. If set to `initial`, git will follow redirects only for the initial request to a remote, but not for subsequent follow-up HTTP requests. Since git uses the redirected URL as the base for the follow-up requests, this is generally sufficient. The default is `initial`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpurl)http.<url>.* 
    
Any of the http.* options above can be applied selectively to some URLs. For a config key to match a URL, each element of the config key is compared to that of the URL, in the following order:
  1. Scheme (e.g., `https` in `https://example.com/`). This field must match exactly between the config key and the URL.
  2. Host/domain name (e.g., `example.com` in `https://example.com/`). This field must match between the config key and the URL. It is possible to specify a `*` as part of the host name to match all subdomains at this level. `https://*.example.com/` for example would match `https://foo.example.com/`, but not `https://foo.bar.example.com/`.
  3. Port number (e.g., `8080` in `http://example.com:8080/`). This field must match exactly between the config key and the URL. Omitted port numbers are automatically converted to the correct default for the scheme before matching.
  4. Path (e.g., `repo.git` in `https://example.com/repo.git`). The path field of the config key must match the path field of the URL either exactly or as a prefix of slash-delimited path elements. This means a config key with path `foo/` matches URL path `foo/bar`. A prefix can only match on a slash (`/`) boundary. Longer matches take precedence (so a config key with path `foo/bar` is a better match to URL path `foo/bar` than a config key with just path `foo/`).
  5. User name (e.g., `user` in `https://user@example.com/repo.git`). If the config key has a user name it must match the user name in the URL exactly. If the config key does not have a user name, that config key will match a URL with any user name (including none), but at a lower precedence than a config key with a user name.


The list above is ordered by decreasing precedence; a URL that matches a config key’s path is preferred to one that matches its user name. For example, if the URL is `https://user@example.com/foo/bar` a config key match of `https://example.com/foo` will be preferred over a config key match of `https://user@example.com`.
All URLs are normalized before attempting any matching (the password part, if embedded in the URL, is always ignored for matching purposes) so that equivalent URLs that are simply spelled differently will match properly. Environment variable settings always override any matches. The URLs that are matched against are those given directly to Git commands. This means any URLs visited as a result of a redirection do not participate in matching. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-i18ncommitEncoding)i18n.commitEncoding 
    
Character encoding the commit messages are stored in; Git itself does not care per se, but this information is necessary e.g. when importing commits from emails or in the gitk graphical history browser (and possibly in other places in the future or in other porcelains). See e.g. [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo). Defaults to _utf-8_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-i18nlogOutputEncoding)i18n.logOutputEncoding 
    
Character encoding the commit messages are converted to when running _git log_ and friends. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imapfolder)imap.folder 
    
The folder to drop the mails into, which is typically the Drafts folder. For example: `INBOX.Drafts`, `INBOX/Drafts` or [`Gmail`]`/Drafts`. The IMAP folder to interact with MUST be specified; the value of this configuration variable is used as the fallback default value when the `--folder` option is not given. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imaptunnel)imap.tunnel 
    
Command used to set up a tunnel to the IMAP server through which commands will be piped instead of using a direct network connection to the server. Required when imap.host is not set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imaphost)imap.host 
    
A URL identifying the server. Use an `imap://` prefix for non-secure connections and an `imaps://` prefix for secure connections. Ignored when imap.tunnel is set, but required otherwise. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imapuser)imap.user 
    
The username to use when logging in to the server. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imappass)imap.pass 
    
The password to use when logging in to the server. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imapport)imap.port 
    
An integer port number to connect to on the server. Defaults to 143 for imap:// hosts and 993 for imaps:// hosts. Ignored when imap.tunnel is set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imapsslverify)imap.sslverify 
    
A boolean to enable/disable verification of the server certificate used by the SSL/TLS connection. Default is `true`. Ignored when imap.tunnel is set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imappreformattedHTML)imap.preformattedHTML 
    
A boolean to enable/disable the use of html encoding when sending a patch. An html encoded patch will be bracketed with <pre> and have a content type of text/html. Ironically, enabling this option causes Thunderbird to send the patch as a plain/text, format=fixed email. Default is `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-imapauthMethod)imap.authMethod 
    
Specify the authentication method for authenticating with the IMAP server. If Git was built with the NO_CURL option, or if your curl version is older than 7.34.0, or if you’re running git-imap-send with the `--no-curl` option, the only supported methods are `PLAIN`, `CRAM-MD5`, `OAUTHBEARER` and `XOAUTH2`. If this is not set then `git` `imap-send` uses the basic IMAP plaintext `LOGIN` command. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-includepath)include.path 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-includeIfconditionpath)includeIf.<condition>.path 
    
Special variables to include other configuration files. See the "CONFIGURATION FILE" section in the main [git-config[1]](https://git-scm.com/docs/git-config) documentation, specifically the "Includes" and "Conditional Includes" subsections. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-indexrecordEndOfIndexEntries)index.recordEndOfIndexEntries 
    
Specifies whether the index file should include an "End Of Index Entry" section. This reduces index load time on multiprocessor machines but produces a message "ignoring EOIE extension" when reading the index using Git versions before 2.20. Defaults to _true_ if index.threads has been explicitly enabled, _false_ otherwise. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-indexrecordOffsetTable)index.recordOffsetTable 
    
Specifies whether the index file should include an "Index Entry Offset Table" section. This reduces index load time on multiprocessor machines but produces a message "ignoring IEOT extension" when reading the index using Git versions before 2.20. Defaults to _true_ if index.threads has been explicitly enabled, _false_ otherwise. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-indexsparse)index.sparse 
    
When enabled, write the index using sparse-directory entries. This has no effect unless `core.sparseCheckout` and `core.sparseCheckoutCone` are both enabled. Defaults to _false_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-indexthreads)index.threads 
    
Specifies the number of threads to spawn when loading the index. This is meant to reduce index load time on multiprocessor machines. Specifying 0 or _true_ will cause Git to auto-detect the number of CPUs and set the number of threads accordingly. Specifying 1 or _false_ will disable multithreading. Defaults to _true_. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-indexversion)index.version 
    
Specify the version with which new index files should be initialized. This does not affect existing repositories. If `feature.manyFiles` is enabled, then the default is 4. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-indexskipHash)index.skipHash 
    
When enabled, do not compute the trailing hash for the index file. This accelerates Git commands that manipulate the index, such as `git` `add`, `git` `commit`, or `git` `status`. Instead of storing the checksum, write a trailing set of bytes with value zero, indicating that the computation was skipped.
If you enable `index.skipHash`, then Git clients older than 2.13.0 will refuse to parse the index and Git clients older than 2.40.0 will report an error during `git` `fsck`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-inittemplateDir)`init.templateDir` 
    
Specify the directory from which templates will be copied. (See the "TEMPLATE DIRECTORY" section of [git-init[1]](https://git-scm.com/docs/git-init).) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-initdefaultBranch)`init.defaultBranch` 
    
Allows overriding the default branch name e.g. when initializing a new repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-initdefaultObjectFormat)`init.defaultObjectFormat` 
    
Allows overriding the default object format for new repositories. See `--object-format=` in [git-init[1]](https://git-scm.com/docs/git-init). Both the command line option and the `GIT_DEFAULT_HASH` environment variable take precedence over this config. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-initdefaultRefFormat)`init.defaultRefFormat` 
    
Allows overriding the default ref storage format for new repositories. See `--ref-format=` in [git-init[1]](https://git-scm.com/docs/git-init). Both the command line option and the `GIT_DEFAULT_REF_FORMAT` environment variable take precedence over this config. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-instawebbrowser)instaweb.browser 
    
Specify the program that will be used to browse your working repository in gitweb. See [git-instaweb[1]](https://git-scm.com/docs/git-instaweb). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-instawebhttpd)instaweb.httpd 
    
The HTTP daemon command-line to start gitweb on your working repository. See [git-instaweb[1]](https://git-scm.com/docs/git-instaweb). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-instaweblocal)instaweb.local 
    
If true the web server started by [git-instaweb[1]](https://git-scm.com/docs/git-instaweb) will be bound to the local IP (127.0.0.1). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-instawebmodulePath)instaweb.modulePath 
    
The default module path for [git-instaweb[1]](https://git-scm.com/docs/git-instaweb) to use instead of /usr/lib/apache2/modules. Only used if httpd is Apache. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-instawebport)instaweb.port 
    
The port number to bind the gitweb httpd to. See [git-instaweb[1]](https://git-scm.com/docs/git-instaweb). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-interactivesingleKey)interactive.singleKey 
    
When set to true, allow the user to provide one-letter input with a single key (i.e., without hitting the Enter key) in interactive commands. This is currently used by the `--patch` mode of [git-add[1]](https://git-scm.com/docs/git-add), [git-checkout[1]](https://git-scm.com/docs/git-checkout), [git-restore[1]](https://git-scm.com/docs/git-restore), [git-commit[1]](https://git-scm.com/docs/git-commit), [git-reset[1]](https://git-scm.com/docs/git-reset), and [git-stash[1]](https://git-scm.com/docs/git-stash). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-interactivediffFilter)interactive.diffFilter 
    
When an interactive command (such as `git` `add` `--patch`) shows a colorized diff, git will pipe the diff through the shell command defined by this configuration variable. The command may mark up the diff further for human consumption, provided that it retains a one-to-one correspondence with the lines in the original diff. Defaults to disabled (no filtering). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logabbrevCommit)`log.abbrevCommit` 
    
If `true`, make [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), and [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged) assume `--abbrev-commit`. You may override this option with `--no-abbrev-commit`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logdate)`log.date` 
    
Set the default date-time mode for the `log` command. Setting a value for log.date is similar to using `git` `log`'s `--date` option. See [git-log[1]](https://git-scm.com/docs/git-log) for details.
If the format is set to "auto:foo" and the pager is in use, format "foo" will be used for the date format. Otherwise, "default" will be used. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logdecorate)`log.decorate` 
    
Print out the ref names of any commits that are shown by the log command. Possible values are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-short)`short` 
    
the ref name prefixes `refs/heads/`, `refs/tags/` and `refs/remotes/` are not printed. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-full)`full` 
    
the full ref name (including prefix) are printed. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-auto-1)`auto` 
    
if the output is going to a terminal, the ref names are shown as if `short` were given, otherwise no ref names are shown.
This is the same as the `--decorate` option of the `git` `log`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-loginitialDecorationSet)`log.initialDecorationSet` 
    
By default, `git` `log` only shows decorations for certain known ref namespaces. If _all_ is specified, then show all refs as decorations. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logexcludeDecoration)`log.excludeDecoration` 
    
Exclude the specified patterns from the log decorations. This is similar to the `--decorate-refs-exclude` command-line option, but the config option can be overridden by the `--decorate-refs` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logdiffMerges)`log.diffMerges` 
    
Set diff format to be used when `--diff-merges=on` is specified, see `--diff-merges` in [git-log[1]](https://git-scm.com/docs/git-log) for details. Defaults to `separate`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logfollow)`log.follow` 
    
If `true`, `git` `log` will act as if the `--follow` option was used when a single <path> is given. This has the same limitations as `--follow`, i.e. it cannot be used to follow multiple files and does not work well on non-linear history. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-loggraphColors)`log.graphColors` 
    
A list of colors, separated by commas, that can be used to draw history lines in `git` `log` `--graph`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logshowRoot)`log.showRoot` 
    
If true, the initial commit will be shown as a big creation event. This is equivalent to a diff against an empty tree. Tools like [git-log[1]](https://git-scm.com/docs/git-log) or [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged), which normally hide the root commit will now show it. True by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logshowSignature)`log.showSignature` 
    
If true, makes [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), and [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged) assume `--show-signature`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-logmailmap)`log.mailmap` 
    
If true, makes [git-log[1]](https://git-scm.com/docs/git-log), [git-show[1]](https://git-scm.com/docs/git-show), and [git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged) assume `--use-mailmap`, otherwise assume `--no-use-mailmap`. True by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-lsrefsunborn)lsrefs.unborn 
    
May be "advertise" (the default), "allow", or "ignore". If "advertise", the server will respond to the client sending "unborn" (as described in [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2)) and will advertise support for this feature during the protocol v2 capability advertisement. "allow" is the same as "advertise" except that the server will not advertise support for this feature; this is useful for load-balanced servers that cannot be updated atomically (for example), since the administrator could configure "allow", then after a delay, configure "advertise". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mailinfoscissors)mailinfo.scissors 
    
If true, makes [git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo) (and therefore [git-am[1]](https://git-scm.com/docs/git-am)) act by default as if the --scissors option was provided on the command-line. When active, this feature removes everything from the message body before a scissors line (i.e. consisting mainly of ">8", "8<" and "-"). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mailmapfile)mailmap.file 
    
The location of an augmenting mailmap file. The default mailmap, located in the root of the repository, is loaded first, then the mailmap file pointed to by this variable. The location of the mailmap file may be in a repository subdirectory, or somewhere outside of the repository itself. See [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) and [git-blame[1]](https://git-scm.com/docs/git-blame). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mailmapblob)mailmap.blob 
    
Like `mailmap.file`, but consider the value as a reference to a blob in the repository. If both `mailmap.file` and `mailmap.blob` are given, both are parsed, with entries from `mailmap.file` taking precedence. In a bare repository, this defaults to `HEAD:.mailmap`. In a non-bare repository, it defaults to empty. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenanceauto)maintenance.auto 
    
This boolean config option controls whether some commands run `git` `maintenance` `run` `--auto` after doing their normal work. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenanceautoDetach)maintenance.autoDetach 
    
Many Git commands trigger automatic maintenance after they have written data into the repository. This boolean config option controls whether this automatic maintenance shall happen in the foreground or whether the maintenance process shall detach and continue to run in the background.
If unset, the value of `gc.autoDetach` is used as a fallback. Defaults to true if both are unset, meaning that the maintenance process will detach. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancestrategy)maintenance.strategy 
    
This string config option provides a way to specify one of a few recommended strategies for repository maintenance. This affects which tasks are run during `git` `maintenance` `run`, provided no `--task=`_< task>_ arguments are provided. This setting impacts manual maintenance, auto-maintenance as well as scheduled maintenance. The tasks that run may be different depending on the maintenance type.
The maintenance strategy can be further tweaked by setting `maintenance.`_< task>_`.enabled` and `maintenance.`_< task>_`.schedule`. If set, these values are used instead of the defaults provided by `maintenance.strategy`.
The possible strategies are:
  * `none`: This strategy implies no tasks are run at all. This is the default strategy for scheduled maintenance.
  * `gc`: This strategy runs the `gc` task. This is the default strategy for manual maintenance.
  * `geometric`: This strategy performs geometric repacking of packfiles and keeps auxiliary data structures up-to-date. The strategy expires data in the reflog and removes worktrees that cannot be located anymore. When the geometric repacking strategy would decide to do an all-into-one repack, then the strategy generates a cruft pack for all unreachable objects. Objects that are already part of a cruft pack will be expired.
This repacking strategy is a full replacement for the `gc` strategy and is recommended for large repositories.
  * `incremental`: This setting optimizes for performing small maintenance activities that do not delete any data. This does not schedule the `gc` task, but runs the `prefetch` and `commit-graph` tasks hourly, the `loose-objects` and `incremental-repack` tasks daily, and the `pack-refs` task weekly. Manual repository maintenance uses the `gc` task.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancetaskenabled)maintenance.<task>.enabled 
    
This boolean config option controls whether the maintenance task with name _< task>_ is run when no `--task` option is specified to `git` `maintenance` `run`. These config values are ignored if a `--task` option exists. By default, only `maintenance.gc.enabled` is true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancetaskschedule)maintenance.<task>.schedule 
    
This config option controls whether or not the given _< task>_ runs during a `git` `maintenance` `run` `--schedule=`_< frequency>_ command. The value must be one of "hourly", "daily", or "weekly". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancecommit-graphauto)maintenance.commit-graph.auto 
    
This integer config option controls how often the `commit-graph` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `commit-graph` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of reachable commits that are not in the commit-graph file is at least the value of `maintenance.commit-graph.auto`. The default value is 100. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenanceloose-objectsauto)maintenance.loose-objects.auto 
    
This integer config option controls how often the `loose-objects` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `loose-objects` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of loose objects is at least the value of `maintenance.loose-objects.auto`. The default value is 100. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenanceloose-objectsbatchSize)maintenance.loose-objects.batchSize 
    
This integer config option controls the maximum number of loose objects written into a packfile during the `loose-objects` task. The default is fifty thousand. Use value `0` to indicate no limit. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenanceincremental-repackauto)maintenance.incremental-repack.auto 
    
This integer config option controls how often the `incremental-repack` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `incremental-repack` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of pack-files not in the multi-pack-index is at least the value of `maintenance.incremental-repack.auto`. The default value is 10. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancegeometric-repackauto)maintenance.geometric-repack.auto 
    
This integer config option controls how often the `geometric-repack` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `geometric-repack` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run either when there are packfiles that need to be merged together to retain the geometric progression, or when there are at least this many loose objects that would be written into a new packfile. The default value is 100. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancegeometric-repacksplitFactor)maintenance.geometric-repack.splitFactor 
    
This integer config option controls the factor used for the geometric sequence. See the `--geometric=` option in [git-repack[1]](https://git-scm.com/docs/git-repack) for more details. Defaults to `2`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancereflog-expireauto)maintenance.reflog-expire.auto 
    
This integer config option controls how often the `reflog-expire` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `reflog-expire` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of expired reflog entries in the "HEAD" reflog is at least the value of `maintenance.loose-objects.auto`. The default value is 100. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenancererere-gcauto)maintenance.rerere-gc.auto 
    
This integer config option controls how often the `rerere-gc` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `rerere-gc` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, any positive value implies the command will run when the "rr-cache" directory exists and has at least one entry, regardless of whether it is stale or not. This heuristic may be refined in the future. The default value is 1. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-maintenanceworktree-pruneauto)maintenance.worktree-prune.auto 
    
This integer config option controls how often the `worktree-prune` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `worktree-prune` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of prunable worktrees exceeds the value. The default value is 1. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-manviewer)man.viewer 
    
Specify the programs that may be used to display help in the _man_ format. See [git-help[1]](https://git-scm.com/docs/git-help). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mantoolcmd)man.<tool>.cmd 
    
Specify the command to invoke the specified man viewer. The specified command is evaluated in shell with the man page passed as an argument. (See [git-help[1]](https://git-scm.com/docs/git-help).) 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mantoolpath)man.<tool>.path 
    
Override the path for the given tool that may be used to display help in the _man_ format. See [git-help[1]](https://git-scm.com/docs/git-help). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeconflictStyle)`merge.conflictStyle` 
    
Specify the style in which conflicted hunks are written out to working tree files upon merge. The default is "merge", which shows a _< <<<<<<_ conflict marker, changes made by one side, a `=======` marker, changes made by the other side, and then a _> >>>>>>_ marker. An alternate style, "diff3", adds a ||||||| marker and the original text before the `=======` marker. The "merge" style tends to produce smaller conflict regions than diff3, both because of the exclusion of the original text, and because when a subset of lines match on the two sides, they are just pulled out of the conflict region. Another alternate style, "zdiff3", is similar to diff3 but removes matching lines on the two sides from the conflict region when those matching lines appear near either the beginning or end of a conflict region. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergedefaultToUpstream)`merge.defaultToUpstream` 
    
If merge is called without any commit argument, merge the upstream branches configured for the current branch by using their last observed values stored in their remote-tracking branches. The values of the _branch. <current branch>.merge_ that name the branches at the remote named by `branch.`_< current-branch>_`.remote` are consulted, and then they are mapped via `remote.`_< remote>_`.fetch` to their corresponding remote-tracking branches, and the tips of these tracking branches are merged. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeff)`merge.ff` 
    
By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to `false`, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the `--no-ff` option from the command line). When set to `only`, only such fast-forward merges are allowed (equivalent to giving the `--ff-only` option from the command line). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeverifySignatures)`merge.verifySignatures` 
    
If true, this is equivalent to the `--verify-signatures` command line option. See [git-merge[1]](https://git-scm.com/docs/git-merge) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergebranchdesc)`merge.branchdesc` 
    
In addition to branch names, populate the log message with the branch description text associated with them. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergelog)`merge.log` 
    
In addition to branch names, populate the log message with at most the specified number of one-line descriptions from the actual commits that are being merged. Defaults to false, and true is a synonym for 20. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergesuppressDest)`merge.suppressDest` 
    
By adding a glob that matches the names of integration branches to this multi-valued configuration variable, the default merge message computed for merges into these integration branches will omit "into _< branch-name>_" from its title.
An element with an empty value can be used to clear the list of globs accumulated from previous configuration entries. When there is no `merge.suppressDest` variable defined, the default value of `master` is used for backward compatibility. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergerenameLimit)`merge.renameLimit` 
    
The number of files to consider in the exhaustive portion of rename detection during a merge. If not specified, defaults to the value of `diff.renameLimit`. If neither `merge.renameLimit` nor `diff.renameLimit` are specified, currently defaults to 7000. This setting has no effect if rename detection is turned off. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergerenames)`merge.renames` 
    
Whether Git detects renames. If set to `false`, rename detection is disabled. If set to `true`, basic rename detection is enabled. Defaults to the value of diff.renames. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergedirectoryRenames)`merge.directoryRenames` 
    
Whether Git detects directory renames, affecting what happens at merge time to new files added to a directory on one side of history when that directory was renamed on the other side of history. Possible values are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-false-1-1)`false` 
    
Directory rename detection is disabled, meaning that such new files will be left behind in the old directory. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-true-1-1)`true` 
    
Directory rename detection is enabled, meaning that such new files will be moved into the new directory. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-conflict)`conflict` 
    
A conflict will be reported for such paths.
If `merge.renames` is `false`, `merge.directoryRenames` is ignored and treated as `false`. Defaults to `conflict`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergerenormalize)`merge.renormalize` 
    
Tell Git that canonical representation of files in the repository has changed over time (e.g. earlier commits record text files with _CRLF_ line endings, but recent ones use _LF_ line endings). In such a repository, for each file where a three-way content merge is needed, Git can convert the data recorded in commits to a canonical form before performing a merge to reduce unnecessary conflicts. For more information, see section "Merging branches with differing checkin/checkout attributes" in [gitattributes[5]](https://git-scm.com/docs/gitattributes). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergestat)`merge.stat` 
    
What, if anything, to print between `ORIG_HEAD` and the merge result at the end of the merge. Possible values are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-false-1-1-1)`false` 
    
Show nothing. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-true-1-1-1)`true` 
    
Show `git` `diff` `--diffstat` `--summary` `ORIG_HEAD`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-compact)`compact` 
    
Show `git` `diff` `--compact-summary` `ORIG_HEAD`.
but any unrecognised value (e.g., a value added by a future version of Git) is taken as `true` instead of triggering an error. Defaults to `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeautoStash)`merge.autoStash` 
    
When set to `true`, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run merge on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. This option can be overridden by the `--no-autostash` and `--autostash` options of [git-merge[1]](https://git-scm.com/docs/git-merge). Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetool)`merge.tool` 
    
Controls which merge tool is used by [git-mergetool[1]](https://git-scm.com/docs/git-mergetool). The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding `mergetool.`_< tool>_`.cmd` variable is defined. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeguitool)`merge.guitool` 
    
Controls which merge tool is used by [git-mergetool[1]](https://git-scm.com/docs/git-mergetool) when the `-g`/`--gui` flag is specified. The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding `mergetool.`_< guitool>_`.cmd` variable is defined.
  * araxis
  * bc
  * codecompare
  * deltawalker
  * diffmerge
  * diffuse
  * ecmerge
  * emerge
  * examdiff
  * guiffy
  * gvimdiff
  * kdiff3
  * meld
  * nvimdiff
  * opendiff
  * p4merge
  * smerge
  * tkdiff
  * tortoisemerge
  * vimdiff
  * vscode
  * winmerge
  * xxdiff



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeverbosity)`merge.verbosity` 
    
Controls the amount of output shown by the recursive merge strategy. Level 0 outputs nothing except a final error message if conflicts were detected. Level 1 outputs only conflicts, 2 outputs conflicts and file changes. Level 5 and above outputs debugging information. The default is level 2. Can be overridden by the `GIT_MERGE_VERBOSITY` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergedrivername)`merge.`_< driver>_`.name` 
    
Defines a human-readable name for a custom low-level merge driver. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergedriverdriver)`merge.`_< driver>_`.driver` 
    
Defines the command that implements a custom low-level merge driver. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergedriverrecursive)`merge.`_< driver>_`.recursive` 
    
Names a low-level merge driver to be used when performing an internal merge between common ancestors. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetooltoolpath)`mergetool.`_< tool>_`.path` 
    
Override the path for the given tool. This is useful in case your tool is not in the `$PATH`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetooltoolcmd)`mergetool.`_< tool>_`.cmd` 
    
Specify the command to invoke the specified merge tool. The specified command is evaluated in shell with the following variables available: `BASE` is the name of a temporary file containing the common base of the files to be merged, if available; `LOCAL` is the name of a temporary file containing the contents of the file on the current branch; `REMOTE` is the name of a temporary file containing the contents of the file from the branch being merged; `MERGED` contains the name of the file to which the merge tool should write the results of a successful merge. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetooltoolhideResolved)`mergetool.`_< tool>_`.hideResolved` 
    
Allows the user to override the global `mergetool.hideResolved` value for a specific tool. See `mergetool.hideResolved` for the full description. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetooltooltrustExitCode)`mergetool.`_< tool>_`.trustExitCode` 
    
For a custom merge command, specify whether the exit code of the merge command can be used to determine whether the merge was successful. If this is not set to true then the merge target file timestamp is checked, and the merge is assumed to have been successful if the file has been updated; otherwise, the user is prompted to indicate the success of the merge. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolmeldhasOutput)`mergetool.meld.hasOutput` 
    
Older versions of `meld` do not support the `--output` option. Git will attempt to detect whether `meld` supports `--output` by inspecting the output of `meld` `--help`. Configuring `mergetool.meld.hasOutput` will make Git skip these checks and use the configured value instead. Setting `mergetool.meld.hasOutput` to `true` tells Git to unconditionally use the `--output` option, and `false` avoids using `--output`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolmelduseAutoMerge)`mergetool.meld.useAutoMerge` 
    
When the `--auto-merge` is given, meld will merge all non-conflicting parts automatically, highlight the conflicting parts, and wait for user decision. Setting `mergetool.meld.useAutoMerge` to `true` tells Git to unconditionally use the `--auto-merge` option with `meld`. Setting this value to `auto` makes git detect whether `--auto-merge` is supported and will only use `--auto-merge` when available. A value of `false` avoids using `--auto-merge` altogether, and is the default value. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolvariantlayout)`mergetool.`_< variant>_`.layout` 
    
Configure the split window layout for vimdiff’s _< variant>_, which is any of `vimdiff`, `nvimdiff`, `gvimdiff`. Upon launching `git` `mergetool` with `--tool=`_< variant>_ (or without `--tool` if `merge.tool` is configured as _< variant>_), Git will consult `mergetool.`_< variant>_`.layout` to determine the tool’s layout. If the variant-specific configuration is not available, `vimdiff` ' s is used as fallback. If that too is not available, a default layout with 4 windows will be used. To configure the layout, see the _BACKEND SPECIFIC HINTS_ section in [git-mergetool[1]](https://git-scm.com/docs/git-mergetool). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolhideResolved)`mergetool.hideResolved` 
    
During a merge, Git will automatically resolve as many conflicts as possible and write the `$MERGED` file containing conflict markers around any conflicts that it cannot resolve; `$LOCAL` and `$REMOTE` normally are the versions of the file from before Git’s conflict resolution. This flag causes `$LOCAL` and `$REMOTE` to be overwritten so that only the unresolved conflicts are presented to the merge tool. Can be configured per-tool via the `mergetool.`_< tool>_`.hideResolved` configuration variable. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolkeepBackup)`mergetool.keepBackup` 
    
After performing a merge, the original file with conflict markers can be saved as a file with a `.orig` extension. If this variable is set to `false` then this file is not preserved. Defaults to `true` (i.e. keep the backup files). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolkeepTemporaries)`mergetool.keepTemporaries` 
    
When invoking a custom merge tool, Git uses a set of temporary files to pass to the tool. If the tool returns an error and this variable is set to `true`, then these temporary files will be preserved; otherwise, they will be removed after the tool has exited. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolwriteToTemp)`mergetool.writeToTemp` 
    
Git writes temporary `BASE`, `LOCAL`, and `REMOTE` versions of conflicting files in the worktree by default. Git will attempt to use a temporary directory for these files when set `true`. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolprompt)`mergetool.prompt` 
    
Prompt before each invocation of the merge resolution program. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergetoolguiDefault)`mergetool.guiDefault` 
    
Set `true` to use the `merge.guitool` by default (equivalent to specifying the `--gui` argument), or `auto` to select `merge.guitool` or `merge.tool` depending on the presence of a `DISPLAY` environment variable value. The default is `false`, where the `--gui` argument must be provided explicitly for the `merge.guitool` to be used. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-notesmergeStrategy)`notes.mergeStrategy` 
    
Which merge strategy to choose by default when resolving notes conflicts. Must be one of `manual`, `ours`, `theirs`, `union`, or `cat_sort_uniq`. Defaults to `manual`. See the "NOTES MERGE STRATEGIES" section of [git-notes[1]](https://git-scm.com/docs/git-notes) for more information on each strategy.
This setting can be overridden by passing the `--strategy` option to [git-notes[1]](https://git-scm.com/docs/git-notes). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-notesnamemergeStrategy)`notes.`_< name>_`.mergeStrategy` 
    
Which merge strategy to choose when doing a notes merge into `refs/notes/`_< name>_. This overrides the more general `notes.mergeStrategy`. See the "NOTES MERGE STRATEGIES" section in [git-notes[1]](https://git-scm.com/docs/git-notes) for more information on the available strategies. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-notesdisplayRef)`notes.displayRef` 
    
Which ref (or refs, if a glob or specified more than once), in addition to the default set by `core.notesRef` or `GIT_NOTES_REF`, to read notes from when showing commit messages with the `git` `log` family of commands.
This setting can be overridden with the `GIT_NOTES_DISPLAY_REF` environment variable, which must be a colon separated list of refs or globs.
A warning will be issued for refs that do not exist, but a glob that does not match any refs is silently ignored.
This setting can be disabled by the `--no-notes` option to the [git-log[1]](https://git-scm.com/docs/git-log) family of commands, or by the `--notes=`_< ref>_ option accepted by those commands.
The effective value of `core.notesRef` (possibly overridden by `GIT_NOTES_REF`) is also implicitly added to the list of refs to be displayed. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-notesrewritecommand)`notes.rewrite.`_< command>_ 
    
When rewriting commits with _< command>_ (currently `amend` or `rebase`), if this variable is `false`, git will not copy notes from the original to the rewritten commit. Defaults to `true`. See also `notes.rewriteRef` below.
This setting can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable, which must be a colon separated list of refs or globs. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-notesrewriteMode)`notes.rewriteMode` 
    
When copying notes during a rewrite (see the `notes.rewrite.`_< command>_ option), determines what to do if the target commit already has a note. Must be one of `overwrite`, `concatenate`, `cat_sort_uniq`, or `ignore`. Defaults to `concatenate`.
This setting can be overridden with the `GIT_NOTES_REWRITE_MODE` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-notesrewriteRef)`notes.rewriteRef` 
    
When copying notes during a rewrite, specifies the (fully qualified) ref whose notes should be copied. May be a glob, in which case notes in all matching refs will be copied. You may also specify this configuration several times.
Does not have a default value; you must configure this variable to enable note rewriting. Set it to `refs/notes/commits` to enable rewriting for the default commit notes.
Can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable. See `notes.rewrite.`_< command>_ above for a further description of its format. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packwindow)pack.window 
    
The size of the window used by [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) when no window size is given on the command line. Defaults to 10. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packdepth)pack.depth 
    
The maximum delta depth used by [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) when no maximum depth is given on the command line. Defaults to 50. Maximum value is 4095. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packwindowMemory)pack.windowMemory 
    
The maximum size of memory that is consumed by each thread in [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) for pack window memory when no limit is given on the command line. The value can be suffixed with "k", "m", or "g". When left unconfigured (or set explicitly to 0), there will be no limit. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packcompression)pack.compression 
    
An integer -1..9, indicating the compression level for objects in a pack file. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If not set, defaults to core.compression. If that is not set, defaults to -1, the zlib default, which is "a default compromise between speed and compression (currently equivalent to level 6)."
Note that changing the compression level will not automatically recompress all existing objects. You can force recompression by passing the -F option to [git-repack[1]](https://git-scm.com/docs/git-repack). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packallowPackReuse)pack.allowPackReuse 
    
When true or "single", and when reachability bitmaps are enabled, pack-objects will try to send parts of the bitmapped packfile verbatim. When "multi", and when a multi-pack reachability bitmap is available, pack-objects will try to send parts of all packs in the MIDX.
If only a single pack bitmap is available, and `pack.allowPackReuse` is set to "multi", reuse parts of just the bitmapped packfile. This can reduce memory and CPU usage to serve fetches, but might result in sending a slightly larger pack. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packisland)pack.island 
    
An extended regular expression configuring a set of delta islands. See "DELTA ISLANDS" in [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packislandCore)pack.islandCore 
    
Specify an island name which gets to have its objects be packed first. This creates a kind of pseudo-pack at the front of one pack, so that the objects from the specified island are hopefully faster to copy into any pack that should be served to a user requesting these objects. In practice this means that the island specified should likely correspond to what is the most commonly cloned in the repo. See also "DELTA ISLANDS" in [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packdeltaCacheSize)pack.deltaCacheSize 
    
The maximum memory in bytes used for caching deltas in [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) before writing them out to a pack. This cache is used to speed up the writing object phase by not having to recompute the final delta result once the best match for all objects is found. Repacking large repositories on machines which are tight with memory might be badly impacted by this though, especially if this cache pushes the system into swapping. A value of 0 means no limit. The smallest size of 1 byte may be used to virtually disable this cache. Defaults to 256 MiB. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packdeltaCacheLimit)pack.deltaCacheLimit 
    
The maximum size of a delta, that is cached in [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects). This cache is used to speed up the writing object phase by not having to recompute the final delta result once the best match for all objects is found. Defaults to 1000. Maximum value is 65535. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packthreads)pack.threads 
    
Specifies the number of threads to spawn when searching for best delta matches. This requires that [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) be compiled with pthreads otherwise this option is ignored with a warning. This is meant to reduce packing time on multiprocessor machines. The required amount of memory for the delta search window is however multiplied by the number of threads. Specifying 0 will cause Git to auto-detect the number of CPUs and set the number of threads accordingly. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packindexVersion)pack.indexVersion 
    
Specify the default pack index version. Valid values are 1 for legacy pack index used by Git versions prior to 1.5.2, and 2 for the new pack index with capabilities for packs larger than 4 GB as well as proper protection against the repacking of corrupted packs. Version 2 is the default. Note that version 2 is enforced and this config option is ignored whenever the corresponding pack is larger than 2 GB.
If you have an old Git that does not understand the version 2 `*.idx` file, cloning or fetching over a non-native protocol (e.g. "http") that will copy both `*.pack` file and corresponding `*.idx` file from the other side may give you a repository that cannot be accessed with your older version of Git. If the `*.pack` file is smaller than 2 GB, however, you can use [git-index-pack[1]](https://git-scm.com/docs/git-index-pack) on the *.pack file to regenerate the `*.idx` file. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packpackSizeLimit)pack.packSizeLimit 
    
The maximum size of a pack. This setting only affects packing to a file when repacking, i.e. the git:// protocol is unaffected. It can be overridden by the `--max-pack-size` option of [git-repack[1]](https://git-scm.com/docs/git-repack). Reaching this limit results in the creation of multiple packfiles.
Note that this option is rarely useful, and may result in a larger total on-disk size (because Git will not store deltas between packs) and worse runtime performance (object lookup within multiple packs is slower than a single pack, and optimizations like reachability bitmaps cannot cope with multiple packs).
If you need to actively run Git using smaller packfiles (e.g., because your filesystem does not support large files), this option may help. But if your goal is to transmit a packfile over a medium that supports limited sizes (e.g., removable media that cannot store the whole repository), you are likely better off creating a single large packfile and splitting it using a generic multi-volume archive tool (e.g., Unix `split`).
The minimum size allowed is limited to 1 MiB. The default is unlimited. Common unit suffixes of _k_ , _m_ , or _g_ are supported. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packuseBitmaps)pack.useBitmaps 
    
When true, git will use pack bitmaps (if available) when packing to stdout (e.g., during the server side of a fetch). Defaults to true. You should not generally need to turn this off unless you are debugging pack bitmaps. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packuseBitmapBoundaryTraversal)pack.useBitmapBoundaryTraversal 
    
When true, Git will use an experimental algorithm for computing reachability queries with bitmaps. Instead of building up complete bitmaps for all of the negated tips and then OR-ing them together, consider negated tips with existing bitmaps as additive (i.e. OR-ing them into the result if they exist, ignoring them otherwise), and build up a bitmap at the boundary instead.
When using this algorithm, Git may include too many objects as a result of not opening up trees belonging to certain UNINTERESTING commits. This inexactness matches the non-bitmap traversal algorithm.
In many cases, this can provide a speed-up over the exact algorithm, particularly when there is poor bitmap coverage of the negated side of the query. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packuseSparse)pack.useSparse 
    
When true, git will default to using the _--sparse_ option in _git pack-objects_ when the _--revs_ option is present. This algorithm only walks trees that appear in paths that introduce new objects. This can have significant performance benefits when computing a pack to send a small change. However, it is possible that extra objects are added to the pack-file if the included commits contain certain types of direct renames. Default is `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packusePathWalk)pack.usePathWalk 
    
Enable the `--path-walk` option by default for `git` `pack-objects` processes. See [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) for full details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packpreferBitmapTips)pack.preferBitmapTips 
    
When selecting which commits will receive bitmaps, prefer a commit at the tip of any reference that is a suffix of any value of this configuration over any other commits in the "selection window".
Note that setting this configuration to `refs/foo` does not mean that the commits at the tips of `refs/foo/bar` and `refs/foo/baz` will necessarily be selected. This is because commits are selected for bitmaps from within a series of windows of variable length.
If a commit at the tip of any reference which is a suffix of any value of this configuration is seen in a window, it is immediately given preference over any other commit in that window. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packwriteBitmapsdeprecated)pack.writeBitmaps (deprecated) 
    
This is a deprecated synonym for `repack.writeBitmaps`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packwriteBitmapHashCache)pack.writeBitmapHashCache 
    
When true, git will include a "hash cache" section in the bitmap index (if one is written). This cache can be used to feed git’s delta heuristics, potentially leading to better deltas between bitmapped and non-bitmapped objects (e.g., when serving a fetch between an older, bitmapped pack and objects that have been pushed since the last gc). The downside is that it consumes 4 bytes per object of disk space. Defaults to true.
When writing a multi-pack reachability bitmap, no new namehashes are computed; instead, any namehashes stored in an existing bitmap are permuted into their appropriate location when writing a new bitmap. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packwriteBitmapLookupTable)pack.writeBitmapLookupTable 
    
When true, Git will include a "lookup table" section in the bitmap index (if one is written). This table is used to defer loading individual bitmaps as late as possible. This can be beneficial in repositories that have relatively large bitmap indexes. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packreadReverseIndex)pack.readReverseIndex 
    
When true, git will read any .rev file(s) that may be available (see: [gitformat-pack[5]](https://git-scm.com/docs/gitformat-pack)). When false, the reverse index will be generated from scratch and stored in memory. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-packwriteReverseIndex)pack.writeReverseIndex 
    
When true, git will write a corresponding .rev file (see: [gitformat-pack[5]](https://git-scm.com/docs/gitformat-pack)) for each new packfile that it writes in all places except for [git-fast-import[1]](https://git-scm.com/docs/git-fast-import) and in the bulk checkin mechanism. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pagercmd)pager.<cmd> 
    
If the value is boolean, turns on or off pagination of the output of a particular Git subcommand when writing to a tty. Otherwise, turns on pagination for the subcommand using the pager specified by the value of `pager.`_< cmd>_. If `--paginate` or `--no-pager` is specified on the command line, it takes precedence over this option. To disable pagination for all commands, set `core.pager` or `GIT_PAGER` to `cat`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-prettyname)pretty.<name> 
    
Alias for a --pretty= format string, as specified in [git-log[1]](https://git-scm.com/docs/git-log). Any aliases defined here can be used just as the built-in pretty formats could. For example, running `git` `config` `pretty.changelog` `"format:*` `%H` `%s"` would cause the invocation `git` `log` `--pretty=changelog` to be equivalent to running `git` `log` `"--pretty=format:*` `%H` `%s"`. Note that an alias with the same name as a built-in format will be silently ignored. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-promisorquiet)promisor.quiet 
    
If set to "true" assume `--quiet` when fetching additional objects for a partial clone. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-promisoradvertise)promisor.advertise 
    
If set to "true", a server will use the "promisor-remote" capability, see [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2), to advertise the promisor remotes it is using, if it uses some. Default is "false", which means the "promisor-remote" capability is not advertised. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-promisorsendFields)promisor.sendFields 
    
A comma or space separated list of additional remote related field names. A server sends these field names and the associated field values from its configuration when advertising its promisor remotes using the "promisor-remote" capability, see [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2). Currently, only the "partialCloneFilter" and "token" field names are supported. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-partialCloneFilter)`partialCloneFilter` 
    
contains the partial clone filter used for the remote. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-token)`token` 
    
contains an authentication token for the remote.
When a field name is part of this list and a corresponding "remote.foo.<field-name>" config variable is set on the server to a non-empty value, then the field name and value are sent when advertising the promisor remote "foo".
This list has no effect unless the "promisor.advertise" config variable is set to "true", and the "name" and "url" fields are always advertised regardless of this setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-promisoracceptFromServer)promisor.acceptFromServer 
    
If set to "all", a client will accept all the promisor remotes a server might advertise using the "promisor-remote" capability. If set to "knownName" the client will accept promisor remotes which are already configured on the client and have the same name as those advertised by the client. This is not very secure, but could be used in a corporate setup where servers and clients are trusted to not switch name and URLs. If set to "knownUrl", the client will accept promisor remotes which have both the same name and the same URL configured on the client as the name and URL advertised by the server. This is more secure than "all" or "knownName", so it should be used if possible instead of those options. Default is "none", which means no promisor remote advertised by a server will be accepted. By accepting a promisor remote, the client agrees that the server might omit objects that are lazily fetchable from this promisor remote from its responses to "fetch" and "clone" requests from the client. Name and URL comparisons are case sensitive. See [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-promisorcheckFields)promisor.checkFields 
    
A comma or space separated list of additional remote related field names. A client checks if the values of these fields transmitted by a server correspond to the values of these fields in its own configuration before accepting a promisor remote. Currently, "partialCloneFilter" and "token" are the only supported field names.
If one of these field names (e.g., "token") is being checked for an advertised promisor remote (e.g., "foo"), three conditions must be met for the check of this specific field to pass:
  1. The corresponding local configuration (e.g., `remote.foo.token`) must be set.
  2. The server must advertise the "token" field for remote "foo".
  3. The value of the locally configured `remote.foo.token` must exactly match the value advertised by the server for the "token" field.
If any of these conditions is not met for any field name listed in `promisor.checkFields`, the advertised remote "foo" is rejected.
For the "partialCloneFilter" field, this allows the client to ensure that the server’s filter matches what it expects locally, preventing inconsistencies in filtering behavior. For the "token" field, this can be used to verify that authentication credentials match expected values.
Field values are compared case-sensitively.
The "name" and "url" fields are always checked according to the `promisor.acceptFromServer` policy, independently of this setting.
The field names and values should be passed by the server through the "promisor-remote" capability by using the `promisor.sendFields` config variable. The fields are checked only if the `promisor.acceptFromServer` config variable is not set to "None". If set to "None", this config variable has no effect. See [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2).



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-protocolallow)protocol.allow 
    
If set, provide a user defined default policy for all protocols which don’t explicitly have a policy (`protocol.`_< name>_`.allow`). By default, if unset, known-safe protocols (http, https, git, ssh) have a default policy of `always`, known-dangerous protocols (ext) have a default policy of `never`, and all other protocols (including file) have a default policy of `user`. Supported policies:
  * `always` - protocol is always able to be used.
  * `never` - protocol is never able to be used.
  * `user` - protocol is only able to be used when `GIT_PROTOCOL_FROM_USER` is either unset or has a value of 1. This policy should be used when you want a protocol to be directly usable by the user but don’t want it used by commands which execute clone/fetch/push commands without user input, e.g. recursive submodule initialization.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-protocolnameallow)protocol.<name>.allow 
    
Set a policy to be used by protocol _< name>_ with clone/fetch/push commands. See `protocol.allow` above for the available policies.
The protocol names currently used by git are:
  * `file`: any local file-based path (including `file://` URLs, or local paths)
  * `git`: the anonymous git protocol over a direct TCP connection (or proxy, if configured)
  * `ssh`: git over ssh (including `host:path` syntax, `ssh://`, etc).
  * `http`: git over http, both "smart http" and "dumb http". Note that this does _not_ include `https`; if you want to configure both, you must do so individually.
  * any external helpers are named by their protocol (e.g., use `hg` to allow the `git-remote-hg` helper)



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-protocolversion)protocol.version 
    
If set, clients will attempt to communicate with a server using the specified protocol version. If the server does not support it, communication falls back to version 0. If unset, the default is `2`. Supported versions:
  * `0` - the original wire protocol.
  * `1` - the original wire protocol with the addition of a version string in the initial response from the server.
  * `2` - Wire protocol version 2, see [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2).



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pullff)pull.ff 
    
By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to `false`, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the `--no-ff` option from the command line). When set to `only`, only such fast-forward merges are allowed (equivalent to giving the `--ff-only` option from the command line). This setting overrides `merge.ff` when pulling. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pullrebase)pull.rebase 
    
When true, rebase branches on top of the fetched branch, instead of merging the default branch from the default remote when "git pull" is run. See "branch.<name>.rebase" for setting this on a per-branch basis.
When `merges` (or just _m_), pass the `--rebase-merges` option to _git rebase_ so that the local merge commits are included in the rebase (see [git-rebase[1]](https://git-scm.com/docs/git-rebase) for details).
When the value is `interactive` (or just _i_), the rebase is run in interactive mode.
**NOTE** : this is a possibly dangerous operation; do **not** use it unless you understand the implications (see [git-rebase[1]](https://git-scm.com/docs/git-rebase) for details). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pulloctopus)pull.octopus 
    
The default merge strategy to use when pulling multiple branches at once. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pullautoStash)pull.autoStash 
    
When set to true, automatically create a temporary stash entry to record the local changes before the operation begins, and restore them after the operation completes. When your "git pull" rebases (instead of merges), this may be convenient, since unlike merging pull that tolerates local changes that do not interfere with the merge, rebasing pull refuses to work with any local changes.
If `pull.autostash` is set (either to true or false), `merge.autostash` and `rebase.autostash` are ignored. If `pull.autostash` is not set at all, depending on the value of `pull.rebase`, `merge.autostash` or `rebase.autostash` is used instead. Can be overridden by the `--`[`no-`]`autostash` command line option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pulltwohead)pull.twohead 
    
The default merge strategy to use when pulling a single branch. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushautoSetupRemote)`push.autoSetupRemote` 
    
If set to `true` assume `--set-upstream` on default push when no upstream tracking exists for the current branch; this option takes effect with `push.default` options `simple`, `upstream`, and `current`. It is useful if by default you want new branches to be pushed to the default remote (like the behavior of `push.default=current`) and you also want the upstream tracking to be set. Workflows most likely to benefit from this option are `simple` central workflows where all branches are expected to have the same name on the remote. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushdefault)`push.default` 
    
Defines the action `git` `push` should take if no refspec is given (whether from the command-line, config, or elsewhere). Different values are well-suited for specific workflows; for instance, in a purely central workflow (i.e. the fetch source is equal to the push destination), `upstream` is probably what you want. Possible values are: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-nothing)`nothing` 
    
do not push anything (error out) unless a refspec is given. This is primarily meant for people who want to avoid mistakes by always being explicit. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-current)`current` 
    
push the current branch to update a branch with the same name on the receiving end. Works in both central and non-central workflows. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-upstream)`upstream` 
    
push the current branch back to the branch whose changes are usually integrated into the current branch (which is called `@{upstream}`). This mode only makes sense if you are pushing to the same repository you would normally pull from (i.e. central workflow). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-tracking)`tracking` 
    
this is a deprecated synonym for `upstream`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-simple-1)`simple` 
    
push the current branch with the same name on the remote.
If you are working on a centralized workflow (pushing to the same repository you pull from, which is typically `origin`), then you need to configure an upstream branch with the same name.
This mode is the default since Git 2.0, and is the safest option suited for beginners. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-matching)`matching` 
    
push all branches having the same name on both ends. This makes the repository you are pushing to remember the set of branches that will be pushed out (e.g. if you always push `maint` and `master` there and no other branches, the repository you push to will have these two branches, and your local `maint` and `master` will be pushed there).
To use this mode effectively, you have to make sure _all_ the branches you would push out are ready to be pushed out before running `git` `push`, as the whole point of this mode is to allow you to push all of the branches in one go. If you usually finish work on only one branch and push out the result, while other branches are unfinished, this mode is not for you. Also this mode is not suitable for pushing into a shared central repository, as other people may add new branches there, or update the tip of existing branches outside your control.
This used to be the default, but not since Git 2.0 (`simple` is the new default). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushfollowTags)`push.followTags` 
    
If set to true, enable `--follow-tags` option by default. You may override this configuration at time of push by specifying `--no-follow-tags`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushgpgSign)`push.gpgSign` 
    
May be set to a boolean value, or the string `if-asked`. A true value causes all pushes to be GPG signed, as if `--signed` is passed to [git-push[1]](https://git-scm.com/docs/git-push). The string `if-asked` causes pushes to be signed if the server supports it, as if `--signed=if-asked` is passed to `git` `push`. A false value may override a value from a lower-priority config file. An explicit command-line flag always overrides this config option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushpushOption)`push.pushOption` 
    
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


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushrecurseSubmodules)`push.recurseSubmodules` 
    
May be `check`, `on-demand`, `only`, or `no`, with the same behavior as that of `push` `--recurse-submodules`. If not set, `no` is used by default, unless `submodule.recurse` is set (in which case a `true` value means `on-demand`). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushuseForceIfIncludes)`push.useForceIfIncludes` 
    
If set to `true`, it is equivalent to specifying `--force-if-includes` as an option to [git-push[1]](https://git-scm.com/docs/git-push) in the command line. Adding `--no-force-if-includes` at the time of push overrides this configuration setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushnegotiate)`push.negotiate` 
    
If set to `true`, attempt to reduce the size of the packfile sent by rounds of negotiation in which the client and the server attempt to find commits in common. If `false`, Git will rely solely on the server’s ref advertisement to find commits in common. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushuseBitmaps)`push.useBitmaps` 
    
If set to `false`, disable use of bitmaps for `git` `push` even if `pack.useBitmaps` is `true`, without preventing other git operations from using bitmaps. Default is `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebasebackend)rebase.backend 
    
Default backend to use for rebasing. Possible choices are _apply_ or _merge_. In the future, if the merge backend gains all remaining capabilities of the apply backend, this setting may become unused. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebasestat)rebase.stat 
    
Whether to show a diffstat of what changed upstream since the last rebase. False by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseautoSquash)rebase.autoSquash 
    
If set to true, enable the `--autosquash` option of [git-rebase[1]](https://git-scm.com/docs/git-rebase) by default for interactive mode. This can be overridden with the `--no-autosquash` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseautoStash)rebase.autoStash 
    
When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts. This option can be overridden by the `--no-autostash` and `--autostash` options of [git-rebase[1]](https://git-scm.com/docs/git-rebase). Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseupdateRefs)rebase.updateRefs 
    
If set to true enable `--update-refs` option by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebasemissingCommitsCheck)rebase.missingCommitsCheck 
    
If set to "warn", git rebase -i will print a warning if some commits are removed (e.g. a line was deleted), however the rebase will still proceed. If set to "error", it will print the previous warning and stop the rebase, _git rebase --edit-todo_ can then be used to correct the error. If set to "ignore", no checking is done. To drop a commit without warning or error, use the `drop` command in the todo list. Defaults to "ignore". 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseinstructionFormat)rebase.instructionFormat 
    
A format string, as specified in [git-log[1]](https://git-scm.com/docs/git-log), to be used for the todo list during an interactive rebase. The format will automatically have the commit hash prepended to the format. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseabbreviateCommands)rebase.abbreviateCommands 
    
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

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaserescheduleFailedExec)rebase.rescheduleFailedExec 
    
Automatically reschedule `exec` commands that failed. This only makes sense in interactive mode (or when an `--exec` option was provided). This is the same as specifying the `--reschedule-failed-exec` option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaseforkPoint)rebase.forkPoint 
    
If set to false set `--no-fork-point` option by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebaserebaseMerges)rebase.rebaseMerges 
    
Whether and how to set the `--rebase-merges` option by default. Can be `rebase-cousins`, `no-rebase-cousins`, or a boolean. Setting to true or to `no-rebase-cousins` is equivalent to `--rebase-merges=no-rebase-cousins`, setting to `rebase-cousins` is equivalent to `--rebase-merges=rebase-cousins`, and setting to false is equivalent to `--no-rebase-merges`. Passing `--rebase-merges` on the command line, with or without an argument, overrides any `rebase.rebaseMerges` configuration. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rebasemaxLabelLength)rebase.maxLabelLength 
    
When generating label names from commit subjects, truncate the names to this length. By default, the names are truncated to a little less than `NAME_MAX` (to allow e.g. `.lock` files to be written for the corresponding loose refs). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveadvertiseAtomic)receive.advertiseAtomic 
    
By default, git-receive-pack will advertise the atomic push capability to its clients. If you don’t want to advertise this capability, set this variable to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveadvertisePushOptions)receive.advertisePushOptions 
    
When set to true, git-receive-pack will advertise the push options capability to its clients. False by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveautogc)receive.autogc 
    
By default, git-receive-pack will run "git maintenance run --auto" after receiving data from git-push and updating refs. You can stop it by setting this variable to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivecertNonceSeed)receive.certNonceSeed 
    
By setting this variable to a string, `git` `receive-pack` will accept a `git` `push` `--signed` and verify it by using a "nonce" protected by HMAC using this string as a secret key. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivecertNonceSlop)receive.certNonceSlop 
    
When a `git` `push` `--signed` sends a push certificate with a "nonce" that was issued by a receive-pack serving the same repository within this many seconds, export the "nonce" found in the certificate to `GIT_PUSH_CERT_NONCE` to the hooks (instead of what the receive-pack asked the sending side to include). This may allow writing checks in `pre-receive` and `post-receive` a bit easier. Instead of checking `GIT_PUSH_CERT_NONCE_SLOP` environment variable that records by how many seconds the nonce is stale to decide if they want to accept the certificate, they only can check `GIT_PUSH_CERT_NONCE_STATUS` is `OK`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivefsckObjects)receive.fsckObjects 
    
If it is set to true, git-receive-pack will check all received objects. See `transfer.fsckObjects` for what’s checked. Defaults to false. If not set, the value of `transfer.fsckObjects` is used instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivefsckmsg-id)receive.fsck.<msg-id> 
    
Acts like `fsck.`_< msg-id>_, but is used by [git-receive-pack[1]](https://git-scm.com/docs/git-receive-pack) instead of [git-fsck[1]](https://git-scm.com/docs/git-fsck). See the `fsck.`_< msg-id>_ documentation for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivefsckskipList)receive.fsck.skipList 
    
Acts like `fsck.skipList`, but is used by [git-receive-pack[1]](https://git-scm.com/docs/git-receive-pack) instead of [git-fsck[1]](https://git-scm.com/docs/git-fsck). See the `fsck.skipList` documentation for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivekeepAlive)receive.keepAlive 
    
After receiving the pack from the client, `receive-pack` may produce no output (if `--quiet` was specified) while processing the pack, causing some networks to drop the TCP connection. With this option set, if `receive-pack` does not transmit any data in this phase for `receive.keepAlive` seconds, it will send a short keepalive packet. The default is 5 seconds; set to 0 to disable keepalives entirely. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveunpackLimit)receive.unpackLimit 
    
If the number of objects received in a push is below this limit then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivemaxInputSize)receive.maxInputSize 
    
If the size of the incoming pack stream is larger than this limit, then git-receive-pack will error out, instead of accepting the pack file. If not set or set to 0, then the size is unlimited. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivedenyDeletes)receive.denyDeletes 
    
If set to true, git-receive-pack will deny a ref update that deletes the ref. Use this to prevent such a ref deletion via a push. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivedenyDeleteCurrent)receive.denyDeleteCurrent 
    
If set to true, git-receive-pack will deny a ref update that deletes the currently checked out branch of a non-bare repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivedenyCurrentBranch)receive.denyCurrentBranch 
    
If set to true or "refuse", git-receive-pack will deny a ref update to the currently checked out branch of a non-bare repository. Such a push is potentially dangerous because it brings the HEAD out of sync with the index and working tree. If set to "warn", print a warning of such a push to stderr, but allow the push to proceed. If set to false or "ignore", allow such pushes with no message. Defaults to "refuse".
Another option is "updateInstead" which will update the working tree if pushing into the current branch. This option is intended for synchronizing working directories when one side is not easily accessible via interactive ssh (e.g. a live web site, hence the requirement that the working directory be clean). This mode also comes in handy when developing inside a VM to test and fix code on different Operating Systems.
By default, "updateInstead" will refuse the push if the working tree or the index have any difference from the HEAD, but the `push-to-checkout` hook can be used to customize this. See [githooks[5]](https://git-scm.com/docs/githooks). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivedenyNonFastForwards)receive.denyNonFastForwards 
    
If set to true, git-receive-pack will deny a ref update which is not a fast-forward. Use this to prevent such an update via a push, even if that push is forced. This configuration variable is set when initializing a shared repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receivehideRefs)receive.hideRefs 
    
This variable is the same as `transfer.hideRefs`, but applies only to `receive-pack` (and so affects pushes, but not fetches). An attempt to update or delete a hidden ref by `git` `push` is rejected. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveprocReceiveRefs)receive.procReceiveRefs 
    
This is a multi-valued variable that defines reference prefixes to match the commands in `receive-pack`. Commands matching the prefixes will be executed by an external hook "proc-receive", instead of the internal `execute_commands` function. If this variable is not defined, the "proc-receive" hook will never be used, and all commands will be executed by the internal `execute_commands` function.
For example, if this variable is set to "refs/for", pushing to reference such as "refs/for/master" will not create or update a reference named "refs/for/master", but may create or update a pull request directly by running the hook "proc-receive".
Optional modifiers can be provided in the beginning of the value to filter commands for specific actions: create (a), modify (m), delete (d). A `!` can be included in the modifiers to negate the reference prefix entry. E.g.:
```
git config --system --add receive.procReceiveRefs ad:refs/heads
git config --system --add receive.procReceiveRefs !:refs/heads
```


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveupdateServerInfo)receive.updateServerInfo 
    
If set to true, git-receive-pack will run git-update-server-info after receiving data from git-push and updating refs. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-receiveshallowUpdate)receive.shallowUpdate 
    
If set to true, .git/shallow can be updated when new refs require new shallow roots. Otherwise those refs are rejected. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-reftableblockSize)reftable.blockSize 
    
The size in bytes used by the reftable backend when writing blocks. The block size is determined by the writer, and does not have to be a power of 2. The block size must be larger than the longest reference name or log entry used in the repository, as references cannot span blocks.
Powers of two that are friendly to the virtual memory system or filesystem (such as 4kB or 8kB) are recommended. Larger sizes (64kB) can yield better compression, with a possible increased cost incurred by readers during access.
The largest block size is `16777215` bytes (15.99 MiB). The default value is `4096` bytes (4kB). A value of `0` will use the default value. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-reftablerestartInterval)reftable.restartInterval 
    
The interval at which to create restart points. The reftable backend determines the restart points at file creation. Every 16 may be more suitable for smaller block sizes (4k or 8k), every 64 for larger block sizes (64k).
More frequent restart points reduces prefix compression and increases space consumed by the restart table, both of which increase file size.
Less frequent restart points makes prefix compression more effective, decreasing overall file size, with increased penalties for readers walking through more records after the binary search step.
A maximum of `65535` restart points per block is supported.
The default value is to create restart points every 16 records. A value of `0` will use the default value. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-reftableindexObjects)reftable.indexObjects 
    
Whether the reftable backend shall write object blocks. Object blocks are a reverse mapping of object ID to the references pointing to them.
The default value is `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-reftablegeometricFactor)reftable.geometricFactor 
    
Whenever the reftable backend appends a new table to the stack, it performs auto compaction to ensure that there is only a handful of tables. The backend does this by ensuring that tables form a geometric sequence regarding the respective sizes of each table.
By default, the geometric sequence uses a factor of 2, meaning that for any table, the next-biggest table must at least be twice as big. A maximum factor of 256 is supported. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-reftablelockTimeout)reftable.lockTimeout 
    
Whenever the reftable backend appends a new table to the stack, it has to lock the central "tables.list" file before updating it. This config controls how long the process will wait to acquire the lock in case another process has already acquired it. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 100 (i.e., retry for 100ms). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotepushDefault)remote.pushDefault 
    
The remote to push to by default. Overrides `branch.`_< name>_`.remote` for all branches, and is overridden by `branch.`_< name>_`.pushRemote` for specific branches. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameurl)remote.<name>.url 
    
The URL of a remote repository. See [git-fetch[1]](https://git-scm.com/docs/git-fetch) or [git-push[1]](https://git-scm.com/docs/git-push). A configured remote can have multiple URLs; in this case the first is used for fetching, and all are used for pushing (assuming no `remote.`_< name>_`.pushurl` is defined). Setting this key to the empty string clears the list of urls, allowing you to override earlier config. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamepushurl)remote.<name>.pushurl 
    
The push URL of a remote repository. See [git-push[1]](https://git-scm.com/docs/git-push). If a `pushurl` option is present in a configured remote, it is used for pushing instead of `remote.`_< name>_`.url`. A configured remote can have multiple push URLs; in this case a push goes to all of them. Setting this key to the empty string clears the list of urls, allowing you to override earlier config. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameproxy)remote.<name>.proxy 
    
For remotes that require curl (http, https and ftp), the URL to the proxy to use for that remote. Set to the empty string to disable proxying for that remote. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameproxyAuthMethod)remote.<name>.proxyAuthMethod 
    
For remotes that require curl (http, https and ftp), the method to use for authenticating against the proxy in use (probably set in `remote.`_< name>_`.proxy`). See `http.proxyAuthMethod`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamefetch)remote.<name>.fetch 
    
The default set of "refspec" for [git-fetch[1]](https://git-scm.com/docs/git-fetch). See [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamepush)remote.<name>.push 
    
The default set of "refspec" for [git-push[1]](https://git-scm.com/docs/git-push). See [git-push[1]](https://git-scm.com/docs/git-push). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamemirror)remote.<name>.mirror 
    
If true, pushing to this remote will automatically behave as if the `--mirror` option was given on the command line. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameskipDefaultUpdate)remote.<name>.skipDefaultUpdate 
    
A deprecated synonym to `remote.`_< name>_`.skipFetchAll` (if both are set in the configuration files with different values, the value of the last occurrence will be used). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameskipFetchAll)remote.<name>.skipFetchAll 
    
If true, this remote will be skipped when updating using [git-fetch[1]](https://git-scm.com/docs/git-fetch), the `update` subcommand of [git-remote[1]](https://git-scm.com/docs/git-remote), and ignored by the prefetch task of `git` `maintenance`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamereceivepack)remote.<name>.receivepack 
    
The default program to execute on the remote side when pushing. See option --receive-pack of [git-push[1]](https://git-scm.com/docs/git-push). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameuploadpack)remote.<name>.uploadpack 
    
The default program to execute on the remote side when fetching. See option --upload-pack of [git-fetch-pack[1]](https://git-scm.com/docs/git-fetch-pack). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenametagOpt)remote.<name>.tagOpt 
    
Setting this value to --no-tags disables automatic tag following when fetching from remote <name>. Setting it to --tags will fetch every tag from remote <name>, even if they are not reachable from remote branch heads. Passing these flags directly to [git-fetch[1]](https://git-scm.com/docs/git-fetch) can override this setting. See options --tags and --no-tags of [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamevcs)remote.<name>.vcs 
    
Setting this to a value <vcs> will cause Git to interact with the remote with the git-remote-<vcs> helper. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameprune)remote.<name>.prune 
    
When set to true, fetching from this remote by default will also remove any remote-tracking references that no longer exist on the remote (as if the `--prune` option was given on the command line). Overrides `fetch.prune` settings, if any. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamepruneTags)remote.<name>.pruneTags 
    
When set to true, fetching from this remote by default will also remove any local tags that no longer exist on the remote if pruning is activated in general via `remote.`_< name>_`.prune`, `fetch.prune` or `--prune`. Overrides `fetch.pruneTags` settings, if any.
See also `remote.`_< name>_`.prune` and the PRUNING section of [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamepromisor)remote.<name>.promisor 
    
When set to true, this remote will be used to fetch promisor objects. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamepartialclonefilter)remote.<name>.partialclonefilter 
    
The filter that will be applied when fetching from this promisor remote. Changing or clearing this value will only affect fetches for new commits. To fetch associated objects for commits already present in the local object database, use the `--refetch` option of [git-fetch[1]](https://git-scm.com/docs/git-fetch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenameserverOption)remote.<name>.serverOption 
    
The default set of server options used when fetching from this remote. These server options can be overridden by the `--server-option=` command line arguments.
This is a multi-valued variable, and an empty value can be used in a higher priority configuration file (e.g. `.git/config` in a repository) to clear the values inherited from a lower priority configuration files (e.g. `$HOME/.gitconfig`). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotenamefollowRemoteHEAD)remote.<name>.followRemoteHEAD 
    
How [git-fetch[1]](https://git-scm.com/docs/git-fetch) should handle updates to `remotes/`_< name>_`/HEAD` when fetching using the configured refspecs of a remote. The default value is "create", which will create `remotes/`_< name>_`/HEAD` if it exists on the remote, but not locally; this will not touch an already existing local reference. Setting it to "warn" will print a message if the remote has a different value than the local one; in case there is no local reference, it behaves like "create". A variant on "warn" is "warn-if-not-$branch", which behaves like "warn", but if `HEAD` on the remote is `$branch` it will be silent. Setting it to "always" will silently update `remotes/`_< name>_`/HEAD` to the value on the remote. Finally, setting it to "never" will never change or create the local reference. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-remotesgroup)remotes.<group> 
    
The list of remotes which are fetched by "git remote update <group>". See [git-remote[1]](https://git-scm.com/docs/git-remote). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackuseDeltaBaseOffset)repack.useDeltaBaseOffset 
    
By default, [git-repack[1]](https://git-scm.com/docs/git-repack) creates packs that use delta-base offset. If you need to share your repository with Git older than version 1.4.4, either directly or via a dumb protocol such as http, then you need to set this option to "false" and repack. Access from old Git versions over the native protocol are unaffected by this option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackpackKeptObjects)repack.packKeptObjects 
    
If set to true, makes `git` `repack` act as if `--pack-kept-objects` was passed. See [git-repack[1]](https://git-scm.com/docs/git-repack) for details. Defaults to `false` normally, but `true` if a bitmap index is being written (either via `--write-bitmap-index` or `repack.writeBitmaps`). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackuseDeltaIslands)repack.useDeltaIslands 
    
If set to true, makes `git` `repack` act as if `--delta-islands` was passed. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackwriteBitmaps)repack.writeBitmaps 
    
When true, git will write a bitmap index when packing all objects to disk (e.g., when `git` `repack` `-a` is run). This index can speed up the "counting objects" phase of subsequent packs created for clones and fetches, at the cost of some disk space and extra time spent on the initial repack. This has no effect if multiple packfiles are created. Defaults to true on bare repos, false otherwise. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackupdateServerInfo)repack.updateServerInfo 
    
If set to false, [git-repack[1]](https://git-scm.com/docs/git-repack) will not run [git-update-server-info[1]](https://git-scm.com/docs/git-update-server-info). Defaults to true. Can be overridden when true by the `-n` option of [git-repack[1]](https://git-scm.com/docs/git-repack). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackcruftWindow)repack.cruftWindow 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackcruftWindowMemory)repack.cruftWindowMemory 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackcruftDepth)repack.cruftDepth 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackcruftThreads)repack.cruftThreads 
    
Parameters used by [git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) when generating a cruft pack and the respective parameters are not given over the command line. See similarly named `pack.*` configuration variables for defaults and meaning. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-repackmidxMustContainCruft)repack.midxMustContainCruft 
    
When set to true, [git-repack[1]](https://git-scm.com/docs/git-repack) will unconditionally include cruft pack(s), if any, in the multi-pack index when invoked with `--write-midx`. When false, cruft packs are only included in the MIDX when necessary (e.g., because they might be required to form a reachability closure with MIDX bitmaps). Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rerereautoUpdate)rerere.autoUpdate 
    
When set to true, `git-rerere` updates the index with the resulting contents after it cleanly resolves conflicts using previously recorded resolutions. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-rerereenabled)rerere.enabled 
    
Activate recording of resolved conflicts, so that identical conflict hunks can be resolved automatically, should they be encountered again. By default, [git-rerere[1]](https://git-scm.com/docs/git-rerere) is enabled if there is an `rr-cache` directory under the `$GIT_DIR`, e.g. if "rerere" was previously used in the repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-revertreference)revert.reference 
    
Setting this variable to true makes `git` `revert` behave as if the `--reference` option is given. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-safebareRepository)safe.bareRepository 
    
Specifies which bare repositories Git will work with. The currently supported values are:
  * `all`: Git works with all bare repositories. This is the default.
  * `explicit`: Git only works with bare repositories specified via the top-level `--git-dir` command-line option, or the `GIT_DIR` environment variable (see [git[1]](https://git-scm.com/docs/git)).
If you do not use bare repositories in your workflow, then it may be beneficial to set `safe.bareRepository` to `explicit` in your global config. This will protect you from attacks that involve cloning a repository that contains a bare repository and running a Git command within that directory.
This config setting is only respected in protected configuration (see [SCOPES](https://git-scm.com/docs/git-config#SCOPES)). This prevents untrusted repositories from tampering with this value.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-safedirectory)safe.directory 
    
These config entries specify Git-tracked directories that are considered safe even if they are owned by someone other than the current user. By default, Git will refuse to even parse a Git config of a repository owned by someone else, let alone run its hooks, and this config setting allows users to specify exceptions, e.g. for intentionally shared repositories (see the `--shared` option in [git-init[1]](https://git-scm.com/docs/git-init)).
This is a multi-valued setting, i.e. you can add more than one directory via `git` `config` `--add`. To reset the list of safe directories (e.g. to override any such directories specified in the system config), add a `safe.directory` entry with an empty value.
This config setting is only respected in protected configuration (see [SCOPES](https://git-scm.com/docs/git-config#SCOPES)). This prevents untrusted repositories from tampering with this value.
The value of this setting is interpolated, i.e. `~/`_< path>_ expands to a path relative to the home directory and `%`(`prefix`)`/`_< path>_ expands to a path relative to Git’s (runtime) prefix.
To completely opt-out of this security check, set `safe.directory` to the string `*`. This will allow all repositories to be treated as if their directory was listed in the `safe.directory` list. If `safe.directory=*` is set in system config and you want to re-enable this protection, then initialize your list with an empty value before listing the repositories that you deem safe. Giving a directory with `/*` appended to it will allow access to all repositories under the named directory.
As explained, Git only allows you to access repositories owned by yourself, i.e. the user who is running Git, by default. When Git is running as _root_ in a non Windows platform that provides sudo, however, git checks the SUDO_UID environment variable that sudo creates and will allow access to the uid recorded as its value in addition to the id from _root_. This is to make it easy to perform a common sequence during installation "make && sudo make install". A git process running under _sudo_ runs as _root_ but the _sudo_ command exports the environment variable to record which id the original user has. If that is not what you would prefer and want git to only trust repositories that are owned by root instead, then you can remove the `SUDO_UID` variable from root’s environment before invoking git. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailidentity)sendemail.identity 
    
A configuration identity. When given, causes values in the `sendemail.`_< identity>_ subsection to take precedence over values in the `sendemail` section. The default identity is the value of `sendemail.identity`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpEncryption)sendemail.smtpEncryption 
    
See [git-send-email[1]](https://git-scm.com/docs/git-send-email) for description. Note that this setting is not subject to the `identity` mechanism. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpSSLCertPath)sendemail.smtpSSLCertPath 
    
Path to ca-certificates (either a directory or a single file). Set it to an empty string to disable certificate verification. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailidentity-1)sendemail.<identity>.* 
    
Identity-specific versions of the `sendemail.*` parameters found below, taking precedence over those when this identity is selected, through either the command-line or `sendemail.identity`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailmultiEdit)sendemail.multiEdit 
    
If `true` (default), a single editor instance will be spawned to edit files you have to edit (patches when `--annotate` is used, and the summary when `--compose` is used). If `false`, files will be edited one after the other, spawning a new editor each time. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailconfirm)sendemail.confirm 
    
Sets the default for whether to confirm before sending. Must be one of `always`, `never`, `cc`, `compose`, or `auto`. See `--confirm` in the [git-send-email[1]](https://git-scm.com/docs/git-send-email) documentation for the meaning of these values. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailmailmap)sendemail.mailmap 
    
If `true`, makes [git-send-email[1]](https://git-scm.com/docs/git-send-email) assume `--mailmap`, otherwise assume `--no-mailmap`. `False` by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailmailmapfile)sendemail.mailmap.file 
    
The location of a [git-send-email[1]](https://git-scm.com/docs/git-send-email) specific augmenting mailmap file. The default mailmap and `mailmap.file` are loaded first. Thus, entries in this file take precedence over entries in the default mailmap locations. See [gitmailmap[5]](https://git-scm.com/docs/gitmailmap). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailmailmapblob)sendemail.mailmap.blob 
    
Like `sendemail.mailmap.file`, but consider the value as a reference to a blob in the repository. Entries in `sendemail.mailmap.file` take precedence over entries here. See [gitmailmap[5]](https://git-scm.com/docs/gitmailmap). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailaliasesFile)sendemail.aliasesFile 
    
To avoid typing long email addresses, point this to one or more email aliases files. You must also supply `sendemail.aliasFileType`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailaliasFileType)sendemail.aliasFileType 
    
Format of the file(s) specified in sendemail.aliasesFile. Must be one of `mutt`, `mailrc`, `pine`, `elm`, `gnus`, or `sendmail`.
What an alias file in each format looks like can be found in the documentation of the email program of the same name. The differences and limitations from the standard formats are described below: 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendmail)sendmail 
    
  * Quoted aliases and quoted addresses are not supported: lines that contain a `"` symbol are ignored.
  * Redirection to a file (`/path/name`) or pipe (|`command`) is not supported.
  * File inclusion (`:include:` `/path/name`) is not supported.
  * Warnings are printed on the standard error output for any explicitly unsupported constructs, and any other lines that are not recognized by the parser.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailannotate)sendemail.annotate 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailbcc)sendemail.bcc 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailcc)sendemail.cc 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailccCmd)sendemail.ccCmd 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailchainReplyTo)sendemail.chainReplyTo 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailenvelopeSender)sendemail.envelopeSender 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailfrom)sendemail.from 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailheaderCmd)sendemail.headerCmd 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsignedOffByCc)sendemail.signedOffByCc 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpPass)sendemail.smtpPass 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsuppressCc)sendemail.suppressCc 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsuppressFrom)sendemail.suppressFrom 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailto)sendemail.to 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailtoCmd)sendemail.toCmd 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpDomain)sendemail.smtpDomain 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpServer)sendemail.smtpServer 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpServerPort)sendemail.smtpServerPort 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpServerOption)sendemail.smtpServerOption 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpUser)sendemail.smtpUser 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailimapSentFolder)sendemail.imapSentFolder 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailuseImapOnly)sendemail.useImapOnly 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailthread)sendemail.thread 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailtransferEncoding)sendemail.transferEncoding 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailvalidate)sendemail.validate 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailxmailer)sendemail.xmailer 
    
These configuration variables all provide a default for [git-send-email[1]](https://git-scm.com/docs/git-send-email) command-line options. See its documentation for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailoutlookidfix)sendemail.outlookidfix 
    
If `true`, makes [git-send-email[1]](https://git-scm.com/docs/git-send-email) assume `--outlook-id-fix`, and if `false` assume `--no-outlook-id-fix`. If not specified, it will behave the same way as if `--outlook-id-fix` is not specified. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsignedOffCcdeprecated)sendemail.signedOffCc (deprecated) 
    
Deprecated alias for `sendemail.signedOffByCc`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpBatchSize)sendemail.smtpBatchSize 
    
Number of messages to be sent per connection, after that a relogin will happen. If the value is `0` or undefined, send all messages in one connection. See also the `--batch-size` option of [git-send-email[1]](https://git-scm.com/docs/git-send-email). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailsmtpReloginDelay)sendemail.smtpReloginDelay 
    
Seconds to wait before reconnecting to the smtp server. See also the `--relogin-delay` option of [git-send-email[1]](https://git-scm.com/docs/git-send-email). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sendemailforbidSendmailVariables)sendemail.forbidSendmailVariables 
    
To avoid common misconfiguration mistakes, [git-send-email[1]](https://git-scm.com/docs/git-send-email) will abort with a warning if any configuration options for `sendmail` exist. Set this variable to bypass the check. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sequenceeditor)sequence.editor 
    
Text editor used by `git` `rebase` `-i` for editing the rebase instruction file. The value is meant to be interpreted by the shell when it is used. It can be overridden by the `GIT_SEQUENCE_EDITOR` environment variable. When not configured, the default commit message editor is used instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-showBranchdefault)showBranch.default 
    
The default set of branches for [git-show-branch[1]](https://git-scm.com/docs/git-show-branch). See [git-show-branch[1]](https://git-scm.com/docs/git-show-branch). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sparseexpectFilesOutsideOfPatterns)sparse.expectFilesOutsideOfPatterns 
    
Typically with sparse checkouts, files not matching any sparsity patterns are marked with a SKIP_WORKTREE bit in the index and are missing from the working tree. Accordingly, Git will ordinarily check whether files with the SKIP_WORKTREE bit are in fact present in the working tree contrary to expectations. If Git finds any, it marks those paths as present by clearing the relevant SKIP_WORKTREE bits. This option can be used to tell Git that such present-despite-skipped files are expected and to stop checking for them.
The default is `false`, which allows Git to automatically recover from the list of files in the index and working tree falling out of sync.
Set this to `true` if you are in a setup where some external factor relieves Git of the responsibility for maintaining the consistency between the presence of working tree files and sparsity patterns. For example, if you have a Git-aware virtual file system that has a robust mechanism for keeping the working tree and the sparsity patterns up to date based on access patterns.
Regardless of this setting, Git does not check for present-despite-skipped files unless sparse checkout is enabled, so this config option has no effect unless `core.sparseCheckout` is `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-splitIndexmaxPercentChange)splitIndex.maxPercentChange 
    
When the split index feature is used, this specifies the percent of entries the split index can contain compared to the total number of entries in both the split index and the shared index before a new shared index is written. The value should be between 0 and 100. If the value is 0, then a new shared index is always written; if it is 100, a new shared index is never written. By default, the value is 20, so a new shared index is written if the number of entries in the split index would be greater than 20 percent of the total number of entries. See [git-update-index[1]](https://git-scm.com/docs/git-update-index). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-splitIndexsharedIndexExpire)splitIndex.sharedIndexExpire 
    
When the split index feature is used, shared index files that were not modified since the time this variable specifies will be removed when a new shared index file is created. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. The default value is "2.weeks.ago". Note that a shared index file is considered modified (for the purpose of expiration) each time a new split-index file is either created based on it or read from it. See [git-update-index[1]](https://git-scm.com/docs/git-update-index). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-sshvariant)ssh.variant 
    
By default, Git determines the command line arguments to use based on the basename of the configured SSH command (configured using the environment variable `GIT_SSH` or `GIT_SSH_COMMAND` or the config setting `core.sshCommand`). If the basename is unrecognized, Git will attempt to detect support of OpenSSH options by first invoking the configured SSH command with the `-G` (print configuration) option and will subsequently use OpenSSH options (if that is successful) or no options besides the host and remote command (if it fails).
The config variable `ssh.variant` can be set to override this detection. Valid values are `ssh` (to use OpenSSH options), `plink`, `putty`, `tortoiseplink`, `simple` (no options except the host and remote command). The default auto-detection can be explicitly requested using the value `auto`. Any other value is treated as `ssh`. This setting can also be overridden via the environment variable `GIT_SSH_VARIANT`.
The current command-line parameters used for each variant are as follows:
  * `ssh` - [-p port] [-4] [-6] [-o option] [username@]host command
  * `simple` - [username@]host command
  * `plink` or `putty` - [-P port] [-4] [-6] [username@]host command
  * `tortoiseplink` - [-P port] [-4] [-6] -batch [username@]host command


Except for the `simple` variant, command-line parameters are likely to change as git gains new features. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-stashindex)`stash.index` 
    
If this is set to true, `git` `stash` `apply` and `git` `stash` `pop` will behave as if `--index` was supplied. Defaults to false. See the descriptions in [git-stash[1]](https://git-scm.com/docs/git-stash).
This also affects invocations of [git-stash[1]](https://git-scm.com/docs/git-stash) via `--autostash` from commands like [git-merge[1]](https://git-scm.com/docs/git-merge), [git-rebase[1]](https://git-scm.com/docs/git-rebase), and [git-pull[1]](https://git-scm.com/docs/git-pull). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-stashshowIncludeUntracked)`stash.showIncludeUntracked` 
    
If this is set to true, the `git` `stash` `show` command will show the untracked files of a stash entry. Defaults to false. See the description of the 'show' command in [git-stash[1]](https://git-scm.com/docs/git-stash). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-stashshowPatch)`stash.showPatch` 
    
If this is set to true, the `git` `stash` `show` command without an option will show the stash entry in patch form. Defaults to false. See the description of the 'show' command in [git-stash[1]](https://git-scm.com/docs/git-stash). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-stashshowStat)`stash.showStat` 
    
If this is set to true, the `git` `stash` `show` command without an option will show a diffstat of the stash entry. Defaults to true. See the description of the 'show' command in [git-stash[1]](https://git-scm.com/docs/git-stash). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusrelativePaths)status.relativePaths 
    
By default, [git-status[1]](https://git-scm.com/docs/git-status) shows paths relative to the current directory. Setting this variable to `false` shows paths relative to the repository root (this was the default for Git prior to v1.5.4). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusshort)status.short 
    
Set to true to enable --short by default in [git-status[1]](https://git-scm.com/docs/git-status). The option --no-short takes precedence over this variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusbranch)status.branch 
    
Set to true to enable --branch by default in [git-status[1]](https://git-scm.com/docs/git-status). The option --no-branch takes precedence over this variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusaheadBehind)status.aheadBehind 
    
Set to true to enable `--ahead-behind` and false to enable `--no-ahead-behind` by default in [git-status[1]](https://git-scm.com/docs/git-status) for non-porcelain status formats. Defaults to true. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusdisplayCommentPrefix)status.displayCommentPrefix 
    
If set to true, [git-status[1]](https://git-scm.com/docs/git-status) will insert a comment prefix before each output line (starting with `core.commentChar`, i.e. `#` by default). This was the behavior of [git-status[1]](https://git-scm.com/docs/git-status) in Git 1.8.4 and previous. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusrenameLimit)status.renameLimit 
    
The number of files to consider when performing rename detection in [git-status[1]](https://git-scm.com/docs/git-status) and [git-commit[1]](https://git-scm.com/docs/git-commit). Defaults to the value of diff.renameLimit. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusrenames)status.renames 
    
Whether and how Git detects renames in [git-status[1]](https://git-scm.com/docs/git-status) and [git-commit[1]](https://git-scm.com/docs/git-commit) . If set to "false", rename detection is disabled. If set to "true", basic rename detection is enabled. If set to "copies" or "copy", Git will detect copies, as well. Defaults to the value of diff.renames. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusshowStash)status.showStash 
    
If set to true, [git-status[1]](https://git-scm.com/docs/git-status) will display the number of entries currently stashed away. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statusshowUntrackedFiles)status.showUntrackedFiles 
    
By default, [git-status[1]](https://git-scm.com/docs/git-status) and [git-commit[1]](https://git-scm.com/docs/git-commit) show files which are not currently tracked by Git. Directories which contain only untracked files, are shown with the directory name only. Showing untracked files means that Git needs to lstat() all the files in the whole repository, which might be slow on some systems. So, this variable controls how the commands display the untracked files. Possible values are:
  * `no` - Show no untracked files.
  * `normal` - Show untracked files and directories.
  * `all` - Show also individual files in untracked directories.


If this variable is not specified, it defaults to _normal_. All usual spellings for Boolean value `true` are taken as `normal` and `false` as `no`. This variable can be overridden with the -u|--untracked-files option of [git-status[1]](https://git-scm.com/docs/git-status) and [git-commit[1]](https://git-scm.com/docs/git-commit). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-statussubmoduleSummary)status.submoduleSummary 
    
Defaults to false. If this is set to a non-zero number or true (identical to -1 or an unlimited number), the submodule summary will be enabled and a summary of commits for modified submodules will be shown (see --summary-limit option of [git-submodule[1]](https://git-scm.com/docs/git-submodule)). Please note that the summary output command will be suppressed for all submodules when `diff.ignoreSubmodules` is set to _all_ or only for those submodules where `submodule.`_< name>_`.ignore=all`. The only exception to that rule is that status and commit will show staged submodule changes. To also view the summary for ignored submodules you can either use the --ignore-submodules=dirty command-line option or the _git submodule summary_ command, which shows a similar output but does not honor these settings. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulenameurl)submodule.<name>.url 
    
The URL for a submodule. This variable is copied from the .gitmodules file to the git config via _git submodule init_. The user can change the configured URL before obtaining the submodule via _git submodule update_. If neither submodule.<name>.active nor submodule.active are set, the presence of this variable is used as a fallback to indicate whether the submodule is of interest to git commands. See [git-submodule[1]](https://git-scm.com/docs/git-submodule) and [gitmodules[5]](https://git-scm.com/docs/gitmodules) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulenameupdate)submodule.<name>.update 
    
The method by which a submodule is updated by _git submodule update_ , which is the only affected command, others such as _git checkout --recurse-submodules_ are unaffected. It exists for historical reasons, when _git submodule_ was the only command to interact with submodules; settings like `submodule.active` and `pull.rebase` are more specific. It is populated by `git` `submodule` `init` from the [gitmodules[5]](https://git-scm.com/docs/gitmodules) file. See description of _update_ command in [git-submodule[1]](https://git-scm.com/docs/git-submodule). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulenamebranch)submodule.<name>.branch 
    
The remote branch name for a submodule, used by `git` `submodule` `update` `--remote`. Set this option to override the value found in the `.gitmodules` file. See [git-submodule[1]](https://git-scm.com/docs/git-submodule) and [gitmodules[5]](https://git-scm.com/docs/gitmodules) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulenamefetchRecurseSubmodules)submodule.<name>.fetchRecurseSubmodules 
    
This option can be used to control recursive fetching of this submodule. It can be overridden by using the --[no-]recurse-submodules command-line option to "git fetch" and "git pull". This setting will override that from in the [gitmodules[5]](https://git-scm.com/docs/gitmodules) file. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulenameignore)submodule.<name>.ignore 
    
Defines under what circumstances "git status" and the diff family show a submodule as modified. When set to "all", it will never be considered modified (but it will nonetheless show up in the output of status and commit when it has been staged), "dirty" will ignore all changes to the submodule’s work tree and takes only differences between the HEAD of the submodule and the commit recorded in the superproject into account. "untracked" will additionally let submodules with modified tracked files in their work tree show up. Using "none" (the default when this option is not set) also shows submodules that have untracked files in their work tree as changed. This setting overrides any setting made in .gitmodules for this submodule, both settings can be overridden on the command line by using the "--ignore-submodules" option. The _git submodule_ commands are not affected by this setting. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulenameactive)submodule.<name>.active 
    
Boolean value indicating if the submodule is of interest to git commands. This config option takes precedence over the submodule.active config option. See [gitsubmodules[7]](https://git-scm.com/docs/gitsubmodules) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submoduleactive)submodule.active 
    
A repeated field which contains a pathspec used to match against a submodule’s path to determine if the submodule is of interest to git commands. See [gitsubmodules[7]](https://git-scm.com/docs/gitsubmodules) for details. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulerecurse)submodule.recurse 
    
A boolean indicating if commands should enable the `--recurse-submodules` option by default. Defaults to false.
When set to true, it can be deactivated via the `--no-recurse-submodules` option. Note that some Git commands lacking this option may call some of the above commands affected by `submodule.recurse`; for instance `git` `remote` `update` will call `git` `fetch` but does not have a `--no-recurse-submodules` option. For these commands a workaround is to temporarily change the configuration value by using `git` `-c` `submodule.recurse=0`.
The following list shows the commands that accept `--recurse-submodules` and whether they are supported by this setting.
  * `checkout`, `fetch`, `grep`, `pull`, `push`, `read-tree`, `reset`, `restore` and `switch` are always supported.
  * `clone` and `ls-files` are not supported.
  * `branch` is supported only if `submodule.propagateBranches` is enabled



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulepropagateBranches)submodule.propagateBranches 
    
[EXPERIMENTAL] A boolean that enables branching support when using `--recurse-submodules` or `submodule.recurse=true`. Enabling this will allow certain commands to accept `--recurse-submodules` and certain commands that already accept `--recurse-submodules` will now consider branches. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulefetchJobs)submodule.fetchJobs 
    
Specifies how many submodules are fetched/cloned at the same time. A positive integer allows up to that number of submodules fetched in parallel. A value of 0 will give some reasonable default. If unset, it defaults to 1. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulealternateLocation)submodule.alternateLocation 
    
Specifies how the submodules obtain alternates when submodules are cloned. Possible values are `no`, `superproject`. By default `no` is assumed, which doesn’t add references. When the value is set to `superproject` the submodule to be cloned computes its alternates location relative to the superprojects alternate. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-submodulealternateErrorStrategy)submodule.alternateErrorStrategy 
    
Specifies how to treat errors with the alternates for a submodule as computed via `submodule.alternateLocation`. Possible values are `ignore`, `info`, `die`. Default is `die`. Note that if set to `ignore` or `info`, and if there is an error with the computed alternate, the clone proceeds as if no alternate was specified. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-tagforceSignAnnotated)`tag.forceSignAnnotated` 
    
A boolean to specify whether annotated tags created should be GPG signed. If `--annotate` is specified on the command line, it takes precedence over this option. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-tagsort)`tag.sort` 
    
This variable controls the sort ordering of tags when displayed by [git-tag[1]](https://git-scm.com/docs/git-tag). Without the `--sort=`_< value>_ option provided, the value of this variable will be used as the default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-taggpgSign)`tag.gpgSign` 
    
A boolean to specify whether all tags should be GPG signed. Use of this option when running in an automated script can result in a large number of tags being signed. It is therefore convenient to use an agent to avoid typing your GPG passphrase several times. Note that this option doesn’t affect tag signing behavior enabled by `-u` _< keyid>_ or `--local-user=`_< keyid>_ options. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-tarumask)tar.umask 
    
This variable can be used to restrict the permission bits of tar archive entries. The default is 0002, which turns off the world write bit. The special value "user" indicates that the archiving user’s umask will be used instead. See umask(2) and [git-archive[1]](https://git-scm.com/docs/git-archive).
Trace2 config settings are only read from the system and global config files; repository local and worktree config files and `-c` command line arguments are not respected. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2normalTarget)trace2.normalTarget 
    
This variable controls the normal target destination. It may be overridden by the `GIT_TRACE2` environment variable. The following table shows possible values. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2perfTarget)trace2.perfTarget 
    
This variable controls the performance target destination. It may be overridden by the `GIT_TRACE2_PERF` environment variable. The following table shows possible values. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2eventTarget)trace2.eventTarget 
    
This variable controls the event target destination. It may be overridden by the `GIT_TRACE2_EVENT` environment variable. The following table shows possible values.
  * `0` or `false` - Disables the target.
  * `1` or `true` - Writes to `STDERR`.
  * [`2-9`] - Writes to the already opened file descriptor.
  * _< absolute-pathname>_ - Writes to the file in append mode. If the target already exists and is a directory, the traces will be written to files (one per process) underneath the given directory.
  * `af_unix:`[_< socket-type>_`:`]_< absolute-pathname>_ - Write to a Unix DomainSocket (on platforms that support them). Socket type can be either `stream` or `dgram`; if omitted Git will try both.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2normalBrief)trace2.normalBrief 
    
Boolean. When true `time`, `filename`, and `line` fields are omitted from normal output. May be overridden by the `GIT_TRACE2_BRIEF` environment variable. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2perfBrief)trace2.perfBrief 
    
Boolean. When true `time`, `filename`, and `line` fields are omitted from PERF output. May be overridden by the `GIT_TRACE2_PERF_BRIEF` environment variable. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2eventBrief)trace2.eventBrief 
    
Boolean. When true `time`, `filename`, and `line` fields are omitted from event output. May be overridden by the `GIT_TRACE2_EVENT_BRIEF` environment variable. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2eventNesting)trace2.eventNesting 
    
Integer. Specifies desired depth of nested regions in the event output. Regions deeper than this value will be omitted. May be overridden by the `GIT_TRACE2_EVENT_NESTING` environment variable. Defaults to 2. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2configParams)trace2.configParams 
    
A comma-separated list of patterns of "important" config settings that should be recorded in the trace2 output. For example, `core.*,remote.*.url` would cause the trace2 output to contain events listing each configured remote. May be overridden by the `GIT_TRACE2_CONFIG_PARAMS` environment variable. Unset by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2envVars)trace2.envVars 
    
A comma-separated list of "important" environment variables that should be recorded in the trace2 output. For example, `GIT_HTTP_USER_AGENT,GIT_CONFIG` would cause the trace2 output to contain events listing the overrides for HTTP user agent and the location of the Git configuration file (assuming any are set). May be overridden by the `GIT_TRACE2_ENV_VARS` environment variable. Unset by default. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2destinationDebug)trace2.destinationDebug 
    
Boolean. When true Git will print error messages when a trace target destination cannot be opened for writing. By default, these errors are suppressed and tracing is silently disabled. May be overridden by the `GIT_TRACE2_DST_DEBUG` environment variable. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trace2maxFiles)trace2.maxFiles 
    
Integer. When writing trace files to a target directory, do not write additional traces if doing so would exceed this many files. Instead, write a sentinel file that will block further tracing to this directory. Defaults to 0, which disables this check. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerseparators)trailer.separators 
    
This option tells which characters are recognized as trailer separators. By default only _:_ is recognized as a trailer separator, except that _=_ is always accepted on the command line for compatibility with other git commands.
The first character given by this option will be the default character used when another separator is not specified in the config for this trailer.
For example, if the value for this option is "%=$", then only lines using the format _< key><sep><value>_ with <sep> containing _%_ , _=_ or _$_ and then spaces will be considered trailers. And _%_ will be the default separator used, so by default trailers will appear like: _< key>% <value>_ (one percent sign and one space will appear between the key and the value). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerwhere)trailer.where 
    
This option tells where a new trailer will be added.
This can be `end`, which is the default, `start`, `after` or `before`.
If it is `end`, then each new trailer will appear at the end of the existing trailers.
If it is `start`, then each new trailer will appear at the start, instead of the end, of the existing trailers.
If it is `after`, then each new trailer will appear just after the last trailer with the same <key>.
If it is `before`, then each new trailer will appear just before the first trailer with the same <key>. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerifexists)trailer.ifexists 
    
This option makes it possible to choose what action will be performed when there is already at least one trailer with the same <key> in the input.
The valid values for this option are: `addIfDifferentNeighbor` (this is the default), `addIfDifferent`, `add`, `replace` or `doNothing`.
With `addIfDifferentNeighbor`, a new trailer will be added only if no trailer with the same (<key>, <value>) pair is above or below the line where the new trailer will be added.
With `addIfDifferent`, a new trailer will be added only if no trailer with the same (<key>, <value>) pair is already in the input.
With `add`, a new trailer will be added, even if some trailers with the same (<key>, <value>) pair are already in the input.
With `replace`, an existing trailer with the same <key> will be deleted and the new trailer will be added. The deleted trailer will be the closest one (with the same <key>) to the place where the new one will be added.
With `doNothing`, nothing will be done; that is no new trailer will be added if there is already one with the same <key> in the input. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerifmissing)trailer.ifmissing 
    
This option makes it possible to choose what action will be performed when there is not yet any trailer with the same <key> in the input.
The valid values for this option are: `add` (this is the default) and `doNothing`.
With `add`, a new trailer will be added.
With `doNothing`, nothing will be done. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerkeyAliaskey)trailer.<keyAlias>.key 
    
Defines a <keyAlias> for the <key>. The <keyAlias> must be a prefix (case does not matter) of the <key>. For example, in `git` `config` `trailer.ack.key` `"Acked-by"` the "Acked-by" is the <key> and the "ack" is the <keyAlias>. This configuration allows the shorter `--trailer` `"ack:..."` invocation on the command line using the "ack" <keyAlias> instead of the longer `--trailer` `"Acked-by:..."`.
At the end of the <key>, a separator can appear and then some space characters. By default the only valid separator is _:_ , but this can be changed using the `trailer.separators` config variable.
If there is a separator in the key, then it overrides the default separator when adding the trailer. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerkeyAliaswhere)trailer.<keyAlias>.where 
    
This option takes the same values as the _trailer.where_ configuration variable and it overrides what is specified by that option for trailers with the specified <keyAlias>. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerkeyAliasifexists)trailer.<keyAlias>.ifexists 
    
This option takes the same values as the _trailer.ifexists_ configuration variable and it overrides what is specified by that option for trailers with the specified <keyAlias>. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerkeyAliasifmissing)trailer.<keyAlias>.ifmissing 
    
This option takes the same values as the _trailer.ifmissing_ configuration variable and it overrides what is specified by that option for trailers with the specified <keyAlias>. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerkeyAliascommand)trailer.<keyAlias>.command 
    
Deprecated in favor of _trailer. <keyAlias>.cmd_. This option behaves in the same way as _trailer. <keyAlias>.cmd_, except that it doesn’t pass anything as argument to the specified command. Instead the first occurrence of substring $ARG is replaced by the <value> that would be passed as argument.
Note that $ARG in the user’s command is only replaced once and that the original way of replacing $ARG is not safe.
When both _trailer. <keyAlias>.cmd_ and _trailer. <keyAlias>.command_ are given for the same <keyAlias>, _trailer. <keyAlias>.cmd_ is used and _trailer. <keyAlias>.command_ is ignored. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-trailerkeyAliascmd)trailer.<keyAlias>.cmd 
    
This option can be used to specify a shell command that will be called once to automatically add a trailer with the specified <keyAlias>, and then called each time a _--trailer <keyAlias>=<value>_ argument is specified to modify the <value> of the trailer that this option would produce.
When the specified command is first called to add a trailer with the specified <keyAlias>, the behavior is as if a special _--trailer <keyAlias>=<value>_ argument was added at the beginning of the "git interpret-trailers" command, where <value> is taken to be the standard output of the command with any leading and trailing whitespace trimmed off.
If some _--trailer <keyAlias>=<value>_ arguments are also passed on the command line, the command is called again once for each of these arguments with the same <keyAlias>. And the <value> part of these arguments, if any, will be passed to the command as its first argument. This way the command can produce a <value> computed from the <value> passed in the _--trailer <keyAlias>=<value>_ argument. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transfercredentialsInUrl)transfer.credentialsInUrl 
    
A configured URL can contain plaintext credentials in the form _< protocol>_`://`_< user>_`:`_< password>_`@`_< domain>_`/`_< path>_. You may want to warn or forbid the use of such configuration (in favor of using [git-credential[1]](https://git-scm.com/docs/git-credential)). This will be used on [git-clone[1]](https://git-scm.com/docs/git-clone), [git-fetch[1]](https://git-scm.com/docs/git-fetch), [git-push[1]](https://git-scm.com/docs/git-push), and any other direct use of the configured URL.
Note that this is currently limited to detecting credentials in `remote.`_< name>_`.url` configuration; it won’t detect credentials in `remote.`_< name>_`.pushurl` configuration.
You might want to enable this to prevent inadvertent credentials exposure, e.g. because:
  * The OS or system where you’re running git may not provide a way or otherwise allow you to configure the permissions of the configuration file where the username and/or password are stored.
  * Even if it does, having such data stored "at rest" might expose you in other ways, e.g. a backup process might copy the data to another system.
  * The git programs will pass the full URL to one another as arguments on the command-line, meaning the credentials will be exposed to other unprivileged users on systems that allow them to see the full process list of other users. On linux the "hidepid" setting documented in procfs(5) allows for configuring this behavior.
If such concerns don’t apply to you then you probably don’t need to be concerned about credentials exposure due to storing sensitive data in git’s configuration files. If you do want to use this, set `transfer.credentialsInUrl` to one of these values:
  * `allow` (default): Git will proceed with its activity without warning.
  * `warn`: Git will write a warning message to `stderr` when parsing a URL with a plaintext credential.
  * `die`: Git will write a failure message to `stderr` when parsing a URL with a plaintext credential.



[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transferfsckObjects)transfer.fsckObjects 
    
When `fetch.fsckObjects` or `receive.fsckObjects` are not set, the value of this variable is used instead. Defaults to false.
When set, the fetch or receive will abort in the case of a malformed object or a link to a nonexistent object. In addition, various other issues are checked for, including legacy issues (see `fsck.`_< msg-id>_), and potential security issues like the existence of a `.GIT` directory or a malicious `.gitmodules` file (see the release notes for v2.2.1 and v2.17.1 for details). Other sanity and security checks may be added in future releases.
On the receiving side, failing fsckObjects will make those objects unreachable, see "QUARANTINE ENVIRONMENT" in [git-receive-pack[1]](https://git-scm.com/docs/git-receive-pack). On the fetch side, malformed objects will instead be left unreferenced in the repository.
Due to the non-quarantine nature of the `fetch.fsckObjects` implementation it cannot be relied upon to leave the object store clean like `receive.fsckObjects` can.
As objects are unpacked they’re written to the object store, so there can be cases where malicious objects get introduced even though the "fetch" failed, only to have a subsequent "fetch" succeed because only new incoming objects are checked, not those that have already been written to the object store. That difference in behavior should not be relied upon. In the future, such objects may be quarantined for "fetch" as well.
For now, the paranoid need to find some way to emulate the quarantine environment if they’d like the same protection as "push". E.g. in the case of an internal mirror do the mirroring in two steps, one to fetch the untrusted objects, and then do a second "push" (which will use the quarantine) to another internal repo, and have internal clients consume this pushed-to repository, or embargo internal fetches and only allow them once a full "fsck" has run (and no new fetches have happened in the meantime). 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transferhideRefs)transfer.hideRefs 
    
String(s) `receive-pack` and `upload-pack` use to decide which refs to omit from their initial advertisements. Use more than one definition to specify multiple prefix strings. A ref that is under the hierarchies listed in the value of this variable is excluded, and is hidden when responding to `git` `push` or `git` `fetch`. See `receive.hideRefs` and `uploadpack.hideRefs` for program-specific versions of this config.
You may also include a `!` in front of the ref name to negate the entry, explicitly exposing it, even if an earlier entry marked it as hidden. If you have multiple hideRefs values, later entries override earlier ones (and entries in more-specific config files override less-specific ones).
If a namespace is in use, the namespace prefix is stripped from each reference before it is matched against `transfer.hiderefs` patterns. In order to match refs before stripping, add a `^` in front of the ref name. If you combine `!` and `^`, `!` must be specified first.
For example, if `refs/heads/master` is specified in `transfer.hideRefs` and the current namespace is `foo`, then `refs/namespaces/foo/refs/heads/master` is omitted from the advertisements. If `uploadpack.allowRefInWant` is set, `upload-pack` will treat `want-ref` `refs/heads/master` in a protocol v2 `fetch` command as if `refs/namespaces/foo/refs/heads/master` did not exist. `receive-pack`, on the other hand, will still advertise the object id the ref is pointing to without mentioning its name (a so-called ".have" line).
Even if you hide refs, a client may still be able to steal the target objects via the techniques described in the "SECURITY" section of the [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces) man page; it’s best to keep private data in a separate repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transferunpackLimit)transfer.unpackLimit 
    
When `fetch.unpackLimit` or `receive.unpackLimit` are not set, the value of this variable is used instead. The default value is 100. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transferadvertiseSID)transfer.advertiseSID 
    
Boolean. When true, client and server processes will advertise their unique session IDs to their remote counterpart. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transferbundleURI)transfer.bundleURI 
    
When `true`, local `git` `clone` commands will request bundle information from the remote server (if advertised) and download bundles before continuing the clone through the Git protocol. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transferadvertiseObjectInfo)transfer.advertiseObjectInfo 
    
When `true`, the `object-info` capability is advertised by servers. Defaults to false. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadarchiveallowUnreachable)uploadarchive.allowUnreachable 
    
If true, allow clients to use `git` `archive` `--remote` to request any tree, whether reachable from the ref tips or not. See the discussion in the "SECURITY" section of [git-upload-archive[1]](https://git-scm.com/docs/git-upload-archive) for more details. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackhideRefs)uploadpack.hideRefs 
    
This variable is the same as `transfer.hideRefs`, but applies only to `upload-pack` (and so affects only fetches, not pushes). An attempt to fetch a hidden ref by `git` `fetch` will fail. See also `uploadpack.allowTipSHA1InWant`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackallowTipSHA1InWant)uploadpack.allowTipSHA1InWant 
    
When `uploadpack.hideRefs` is in effect, allow `upload-pack` to accept a fetch request that asks for an object at the tip of a hidden ref (by default, such a request is rejected). See also `uploadpack.hideRefs`. Even if this is false, a client may be able to steal objects via the techniques described in the "SECURITY" section of the [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces) man page; it’s best to keep private data in a separate repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackallowReachableSHA1InWant)uploadpack.allowReachableSHA1InWant 
    
Allow `upload-pack` to accept a fetch request that asks for an object that is reachable from any ref tip. However, note that calculating object reachability is computationally expensive. Defaults to `false`. Even if this is false, a client may be able to steal objects via the techniques described in the "SECURITY" section of the [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces) man page; it’s best to keep private data in a separate repository. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackallowAnySHA1InWant)uploadpack.allowAnySHA1InWant 
    
Allow `upload-pack` to accept a fetch request that asks for any object at all. It implies `uploadpack.allowTipSHA1InWant` and `uploadpack.allowReachableSHA1InWant`. If set to `true` it will enable both of them, it set to `false` it will disable both of them. By default not set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackkeepAlive)uploadpack.keepAlive 
    
When `upload-pack` has started `pack-objects`, there may be a quiet period while `pack-objects` prepares the pack. Normally it would output progress information, but if `--quiet` was used for the fetch, `pack-objects` will output nothing at all until the pack data begins. Some clients and networks may consider the server to be hung and give up. Setting this option instructs `upload-pack` to send an empty keepalive packet every `uploadpack.keepAlive` seconds. Setting this option to 0 disables keepalive packets entirely. The default is 5 seconds. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackpackObjectsHook)uploadpack.packObjectsHook 
    
If this option is set, when `upload-pack` would run `git` `pack-objects` to create a packfile for a client, it will run this shell command instead. The `pack-objects` command and arguments it _would_ have run (including the `git` `pack-objects` at the beginning) are appended to the shell command. The stdin and stdout of the hook are treated as if `pack-objects` itself was run. I.e., `upload-pack` will feed input intended for `pack-objects` to the hook, and expects a completed packfile on stdout.
Note that this configuration variable is only respected when it is specified in protected configuration (see [SCOPES](https://git-scm.com/docs/git-config#SCOPES)). This is a safety measure against fetching from untrusted repositories. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackallowFilter)uploadpack.allowFilter 
    
If this option is set, `upload-pack` will support partial clone and partial fetch object filtering. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackfilterallow)uploadpackfilter.allow 
    
Provides a default value for unspecified object filters (see: the below configuration variable). If set to `true`, this will also enable all filters which get added in the future. Defaults to `true`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackfilterfilterallow)uploadpackfilter.<filter>.allow 
    
Explicitly allow or ban the object filter corresponding to _< filter>_, where _< filter>_ may be one of: `blob:none`, `blob:limit`, `object:type`, `tree`, `sparse:oid`, or `combine`. If using combined filters, both `combine` and all of the nested filter kinds must be allowed. Defaults to `uploadpackfilter.allow`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackfiltertreemaxDepth)uploadpackfilter.tree.maxDepth 
    
Only allow `--filter=tree:`_< n>_ when _< n>_ is no more than the value of `uploadpackfilter.tree.maxDepth`. If set, this also implies `uploadpackfilter.tree.allow=true`, unless this configuration variable had already been set. Has no effect if unset. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-uploadpackallowRefInWant)uploadpack.allowRefInWant 
    
If this option is set, `upload-pack` will support the `ref-in-want` feature of the protocol version 2 `fetch` command. This feature is intended for the benefit of load-balanced servers which may not have the same view of what OIDs their refs point to due to replication delay. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-urlbaseinsteadOf)url.<base>.insteadOf 
    
Any URL that starts with this value will be rewritten to start, instead, with <base>. In cases where some site serves a large number of repositories, and serves them with multiple access methods, and some users need to use different access methods, this feature allows people to specify any of the equivalent URLs and have Git automatically rewrite the URL to the best alternative for the particular user, even for a never-before-seen repository on the site. When more than one insteadOf strings match a given URL, the longest match is used.
Note that any protocol restrictions will be applied to the rewritten URL. If the rewrite changes the URL to use a custom protocol or remote helper, you may need to adjust the `protocol.*.allow` config to permit the request. In particular, protocols you expect to use for submodules must be set to `always` rather than the default of `user`. See the description of `protocol.allow` above. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-urlbasepushInsteadOf)url.<base>.pushInsteadOf 
    
Any URL that starts with this value will not be pushed to; instead, it will be rewritten to start with <base>, and the resulting URL will be pushed to. In cases where some site serves a large number of repositories, and serves them with multiple access methods, some of which do not allow push, this feature allows people to specify a pull-only URL and have Git automatically use an appropriate URL to push, even for a never-before-seen repository on the site. When more than one pushInsteadOf strings match a given URL, the longest match is used. If a remote has an explicit pushurl, Git will ignore this setting for that remote. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-username)user.name 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-useremail)user.email 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-authorname)author.name 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-authoremail)author.email 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-committername)committer.name 


[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-committeremail)committer.email 
    
The `user.name` and `user.email` variables determine what ends up in the `author` and `committer` fields of commit objects. If you need the `author` or `committer` to be different, the `author.name`, `author.email`, `committer.name`, or `committer.email` variables can be set. All of these can be overridden by the `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL`, and `EMAIL` environment variables.
Note that the `name` forms of these variables conventionally refer to some form of a personal name. See [git-commit[1]](https://git-scm.com/docs/git-commit) and the environment variables section of [git[1]](https://git-scm.com/docs/git) for more information on these settings and the `credential.username` option if you’re looking for authentication credentials instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-useruseConfigOnly)user.useConfigOnly 
    
Instruct Git to avoid trying to guess defaults for `user.email` and `user.name`, and instead retrieve the values only from the configuration. For example, if you have multiple email addresses and would like to use a different one for each repository, then with this configuration option set to `true` in the global config along with a name, Git will prompt you to set up an email before making new commits in a newly cloned repository. Defaults to `false`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-usersigningKey)user.signingKey 
    
If [git-tag[1]](https://git-scm.com/docs/git-tag) or [git-commit[1]](https://git-scm.com/docs/git-commit) is not selecting the key you want it to automatically when creating a signed tag or commit, you can override the default selection with this variable. This option is passed unchanged to gpg’s --local-user parameter, so you may specify a key using any method that gpg supports. If gpg.format is set to `ssh` this can contain the path to either your private ssh key or the public key when ssh-agent is used. Alternatively it can contain a public key prefixed with `key::` directly (e.g.: "key::ssh-rsa XXXXXX identifier"). The private key needs to be available via ssh-agent. If not set Git will call gpg.ssh.defaultKeyCommand (e.g.: "ssh-add -L") and try to use the first key available. For backward compatibility, a raw key which begins with "ssh-", such as "ssh-rsa XXXXXX identifier", is treated as "key::ssh-rsa XXXXXX identifier", but this form is deprecated; use the `key::` form instead. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-versionsortprereleaseSuffixdeprecated)versionsort.prereleaseSuffix (deprecated) 
    
Deprecated alias for `versionsort.suffix`. Ignored if `versionsort.suffix` is set. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-versionsortsuffix)versionsort.suffix 
    
Even when version sort is used in [git-tag[1]](https://git-scm.com/docs/git-tag), tagnames with the same base version but different suffixes are still sorted lexicographically, resulting e.g. in prerelease tags appearing after the main release (e.g. "1.0-rc1" after "1.0"). This variable can be specified to determine the sorting order of tags with different suffixes.
By specifying a single suffix in this variable, any tagname containing that suffix will appear before the corresponding main release. E.g. if the variable is set to "-rc", then all "1.0-rcX" tags will appear before "1.0". If specified multiple times, once per suffix, then the order of suffixes in the configuration will determine the sorting order of tagnames with those suffixes. E.g. if "-pre" appears before "-rc" in the configuration, then all "1.0-preX" tags will be listed before any "1.0-rcX" tags. The placement of the main release tag relative to tags with various suffixes can be determined by specifying the empty suffix among those other suffixes. E.g. if the suffixes "-rc", "", "-ck", and "-bfs" appear in the configuration in this order, then all "v4.8-rcX" tags are listed first, followed by "v4.8", then "v4.8-ckX" and finally "v4.8-bfsX".
If more than one suffix matches the same tagname, then that tagname will be sorted according to the suffix which starts at the earliest position in the tagname. If more than one different matching suffix starts at that earliest position, then that tagname will be sorted according to the longest of those suffixes. The sorting order between different suffixes is undefined if they are in multiple config files. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-webbrowser)web.browser 
    
Specify a web browser that may be used by some commands. Currently only [git-instaweb[1]](https://git-scm.com/docs/git-instaweb) and [git-help[1]](https://git-scm.com/docs/git-help) may use it. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-worktreeguessRemote)`worktree.guessRemote` 
    
If no branch is specified and neither `-b` nor `-B` nor `--detach` is used, then `git` `worktree` `add` defaults to creating a new branch from HEAD. If `worktree.guessRemote` is set to true, `worktree` `add` tries to find a remote-tracking branch whose name uniquely matches the new branch name. If such a branch exists, it is checked out and set as "upstream" for the new branch. If no such match can be found, it falls back to creating a new branch from the current `HEAD`. 

[](https://git-scm.com/docs/git-config#Documentation/git-config.txt-worktreeuseRelativePaths)`worktree.useRelativePaths` 
    
Link worktrees using relative paths (when "`true`") or absolute paths (when "`false`"). This is particularly useful for setups where the repository and worktrees may be moved between different locations or environments. Defaults to "`false`".
Note that setting `worktree.useRelativePaths` to "`true`" implies enabling the `extensions.relativeWorktrees` config (see [git-config[1]](https://git-scm.com/docs/git-config)), thus making it incompatible with older versions of Git.
##  [](https://git-scm.com/docs/git-config#_bugs)BUGS
When using the deprecated [`section.subsection`] syntax, changing a value will result in adding a multi-line key instead of a change, if the subsection is given with at least one uppercase character. For example when the config looks like
```
  [section.subsection]
    key = value1
```

and running `git` `config` `section.Subsection.key` `value2` will result in
```
  [section.subsection]
    key = value1
    key = value2
```

##  [](https://git-scm.com/docs/git-config#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### config
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
