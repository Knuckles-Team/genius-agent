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
    * [NAME](https://git-scm.com/docs/git/2.25.1#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git/2.25.1#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git/2.25.1#_description)
    * [OPTIONS](https://git-scm.com/docs/git/2.25.1#_options)
    * [GIT COMMANDS](https://git-scm.com/docs/git/2.25.1#_git_commands)
    * [High-level commands (porcelain)](https://git-scm.com/docs/git/2.25.1#_high_level_commands_porcelain)
    * [Low-level commands (plumbing)](https://git-scm.com/docs/git/2.25.1#_low_level_commands_plumbing)
    * [Configuration Mechanism](https://git-scm.com/docs/git/2.25.1#_configuration_mechanism)
    * [Identifier Terminology](https://git-scm.com/docs/git/2.25.1#_identifier_terminology)
    * [Symbolic Identifiers](https://git-scm.com/docs/git/2.25.1#_symbolic_identifiers)
    * [File/Directory Structure](https://git-scm.com/docs/git/2.25.1#_filedirectory_structure)
    * [Terminology](https://git-scm.com/docs/git/2.25.1#_terminology)
    * [Environment Variables](https://git-scm.com/docs/git/2.25.1#_environment_variables)
    * [Discussion](https://git-scm.com/docs/git/2.25.1#_discussion)
    * [FURTHER DOCUMENTATION](https://git-scm.com/docs/git/2.25.1#_further_documentation)
    * [Authors](https://git-scm.com/docs/git/2.25.1#_authors)
    * [Reporting Bugs](https://git-scm.com/docs/git/2.25.1#_reporting_bugs)
    * [SEE ALSO](https://git-scm.com/docs/git/2.25.1#_see_also)
    * [GIT](https://git-scm.com/docs/git/2.25.1#_git)


[ English ▾](https://git-scm.com/docs/git/2.25.1)
Localized versions of **git** manual
  1. [English ](https://git-scm.com/docs/git)
  2. [Deutsch ](https://git-scm.com/docs/git/de)
  3. [Español ](https://git-scm.com/docs/git/es)
  4. [Français ](https://git-scm.com/docs/git/fr)
  5. [Português (Brasil) ](https://git-scm.com/docs/git/pt_BR)
  6. [Svenska ](https://git-scm.com/docs/git/sv)
  7. [українська мова ](https://git-scm.com/docs/git/uk)
  8. [简体中文 ](https://git-scm.com/docs/git/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git/2.25.1)
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


[ Version 2.25.1 ▾ ](https://git-scm.com/docs/git/2.25.1) git last updated in 2.53.0
Changes in the **git** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git/2.51.1)
  5. 2.50.1 → 2.51.0 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git/2.50.0)
  7. 2.49.1 no changes
  8. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git/2.49.0)
  9. 2.48.1 → 2.48.2 no changes
  10. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git/2.48.0)
  11. 2.47.1 → 2.47.3 no changes
  12. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git/2.47.0)
  13. 2.46.1 → 2.46.4 no changes
  14. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git/2.46.0)
  15. 2.45.2 → 2.45.4 no changes
  16. [2.45.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git/2.45.1)
  17. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git/2.45.0)
  18. 2.44.2 → 2.44.4 no changes
  19. [2.44.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.44.1)
  20. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git/2.44.0)
  21. 2.43.5 → 2.43.7 no changes
  22. [2.43.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.43.4)
  23. 2.43.2 → 2.43.3 no changes
  24. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git/2.43.1)
  25. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git/2.43.0)
  26. 2.42.3 → 2.42.4 no changes
  27. [2.42.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.42.2)
  28. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git/2.42.1)
  29. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git/2.42.0)
  30. 2.41.2 → 2.41.3 no changes
  31. [2.41.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.41.1)
  32. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git/2.41.0)
  33. 2.40.3 → 2.40.4 no changes
  34. [2.40.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.40.2)
  35. 2.40.1 no changes
  36. 2.40.0 no changes
  37. 2.39.5 no changes
  38. [2.39.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.39.4)
  39. 2.39.1 → 2.39.3 no changes
  40. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git/2.39.0)
  41. 2.38.3 → 2.38.5 no changes
  42. [2.38.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-11_ ](https://git-scm.com/docs/git/2.38.2)
  43. 2.38.1 no changes
  44. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git/2.38.0)
  45. 2.37.3 → 2.37.7 no changes
  46. [2.37.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-08-11_ ](https://git-scm.com/docs/git/2.37.2)
  47. 2.37.1 no changes
  48. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git/2.37.0)
  49. 2.36.1 → 2.36.6 no changes
  50. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git/2.36.0)
  51. 2.35.1 → 2.35.8 no changes
  52. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git/2.35.0)
  53. 2.34.1 → 2.34.8 no changes
  54. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git/2.34.0)
  55. 2.33.3 → 2.33.8 no changes
  56. [2.33.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git/2.33.2)
  57. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git/2.33.1)
  58. 2.32.1 → 2.33.0 no changes
  59. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git/2.32.0)
  60. 2.31.1 → 2.31.8 no changes
  61. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git/2.31.0)
  62. 2.30.1 → 2.30.9 no changes
  63. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git/2.30.0)
  64. 2.29.1 → 2.29.3 no changes
  65. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git/2.29.0)
  66. 2.28.1 no changes
  67. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git/2.28.0)
  68. 2.27.1 no changes
  69. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git/2.27.0)
  70. 2.26.1 → 2.26.3 no changes
  71. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git/2.26.0)
  72. 2.25.2 → 2.25.5 no changes
  73. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git/2.25.1)
  74. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git/2.25.0)
  75. 2.23.1 → 2.24.4 no changes
  76. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git/2.23.0)
  77. 2.22.2 → 2.22.5 no changes
  78. [2.22.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-11_ ](https://git-scm.com/docs/git/2.22.1)
  79. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git/2.22.0)
  80. 2.20.1 → 2.21.4 no changes
  81. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git/2.20.0)
  82. 2.19.3 → 2.19.6 no changes
  83. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git/2.19.2)
  84. 2.19.1 no changes
  85. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git/2.19.0)
  86. 2.18.1 → 2.18.5 no changes
  87. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git/2.18.0)
  88. 2.17.1 → 2.17.6 no changes
  89. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git/2.17.0)
  90. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git/2.16.6)
  91. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git/2.15.4)
  92. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git/2.14.6)
  93. 2.13.7 no changes
  94. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git/2.12.5)
  95. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git/2.11.4)
  96. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git/2.10.5)
  97. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git/2.9.5)
  98. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git/2.8.6)
  99. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git/2.7.6)
  100. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git/2.6.7)
  101. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git/2.5.6)
  102. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git/2.4.12)
  103. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git/2.3.10)
  104. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git/2.2.3)
  105. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git/2.1.4)
  106. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git/2.25.1#_name)NAME
git - the stupid content tracker
##  [](https://git-scm.com/docs/git/2.25.1#_synopsis)SYNOPSIS
```
_git_ [--version] [--help] [-C <path>] [-c <name>=<value>]
    [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
    [-p|--paginate|-P|--no-pager] [--no-replace-objects] [--bare]
    [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
    [--super-prefix=<path>]
    <command> [<args>]
```

##  [](https://git-scm.com/docs/git/2.25.1#_description)DESCRIPTION
Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.
See [gittutorial[7]](https://git-scm.com/docs/gittutorial) to get started, then see [giteveryday[7]](https://git-scm.com/docs/giteveryday) for a useful minimum set of commands. The [Git User’s Manual](https://git-scm.com/docs/user-manual) has a more in-depth introduction.
After you mastered the basic concepts, you can come back to this page to learn what commands Git offers. You can learn more about individual Git commands with "git help command". [gitcli[7]](https://git-scm.com/docs/gitcli) manual page gives you an overview of the command-line command syntax.
A formatted and hyperlinked copy of the latest Git documentation can be viewed at <https://git.github.io/htmldocs/git.html> or <https://git-scm.com/docs>.
##  [](https://git-scm.com/docs/git/2.25.1#_options)OPTIONS 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---version)--version 
    
Prints the Git suite version that the _git_ program came from. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---help)--help 
    
Prints the synopsis and a list of the most commonly used commands. If the option `--all` or `-a` is given then all available commands are printed. If a Git command is named this option will bring up the manual page for that command.
Other options are available to control how the manual page is displayed. See [git-help[1]](https://git-scm.com/docs/git-help) for more information, because `git` `--help` ... is converted internally into `git` `help` .... 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt--Cpath)-C <path> 
    
Run as if git was started in _< path>_ instead of the current working directory. When multiple `-C` options are given, each subsequent non-absolute `-C` _< path>_ is interpreted relative to the preceding `-C` _< path>_. If _< path>_ is present but empty, e.g. `-C` `""`, then the current working directory is left unchanged.
This option affects options that expect path name like `--git-dir` and `--work-tree` in that their interpretations of the path names would be made relative to the working directory caused by the `-C` option. For example the following invocations are equivalent:
```
git --git-dir=a.git --work-tree=b -C c status
git --git-dir=c/a.git --work-tree=c/b status
```


[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt--cnamevalue)-c <name>=<value> 
    
Pass a configuration parameter to the command. The value given will override values from configuration files. The <name> is expected in the same format as listed by _git config_ (subkeys separated by dots).
Note that omitting the `=` in `git` `-c` `foo.bar` ... is allowed and sets `foo.bar` to the boolean true value (just like [`foo`]`bar` would in a config file). Including the equals but with an empty value (like `git` `-c` `foo.bar=` ...) sets `foo.bar` to the empty string which `git` `config` `--type=bool` will convert to `false`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---exec-pathpath)--exec-path[=<path>] 
    
Path to wherever your core Git programs are installed. This can also be controlled by setting the GIT_EXEC_PATH environment variable. If no path is given, _git_ will print the current setting and then exit. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---html-path)--html-path 
    
Print the path, without trailing slash, where Git’s HTML documentation is installed and exit. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---man-path)--man-path 
    
Print the manpath (see `man`(`1`)) for the man pages for this version of Git and exit. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---info-path)--info-path 
    
Print the path where the Info files documenting this version of Git are installed and exit. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt--p)-p 


[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---paginate)--paginate 
    
Pipe all output into _less_ (or if set, $PAGER) if standard output is a terminal. This overrides the `pager.`_< cmd>_ configuration options (see the "Configuration Mechanism" section below). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt--P)-P 


[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---no-pager)--no-pager 
    
Do not pipe Git output into a pager. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---git-dirpath)--git-dir=<path> 
    
Set the path to the repository. This can also be controlled by setting the `GIT_DIR` environment variable. It can be an absolute path or relative path to current working directory. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---work-treepath)--work-tree=<path> 
    
Set the path to the working tree. It can be an absolute path or a path relative to the current working directory. This can also be controlled by setting the GIT_WORK_TREE environment variable and the core.worktree configuration variable (see core.worktree in [git-config[1]](https://git-scm.com/docs/git-config) for a more detailed discussion). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---namespacepath)--namespace=<path> 
    
Set the Git namespace. See [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces) for more details. Equivalent to setting the `GIT_NAMESPACE` environment variable. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---super-prefixpath)--super-prefix=<path> 
    
Currently for internal use only. Set a prefix which gives a path from above a repository down to its root. One use is to give submodules context about the superproject that invoked it. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---bare)--bare 
    
Treat the repository as a bare repository. If GIT_DIR environment is not set, it is set to the current working directory. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---no-replace-objects)--no-replace-objects 
    
Do not use replacement refs to replace Git objects. See [git-replace[1]](https://git-scm.com/docs/git-replace) for more information. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---literal-pathspecs)--literal-pathspecs 
    
Treat pathspecs literally (i.e. no globbing, no pathspec magic). This is equivalent to setting the `GIT_LITERAL_PATHSPECS` environment variable to `1`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---glob-pathspecs)--glob-pathspecs 
    
Add "glob" magic to all pathspec. This is equivalent to setting the `GIT_GLOB_PATHSPECS` environment variable to `1`. Disabling globbing on individual pathspecs can be done using pathspec magic ":(literal)" 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---noglob-pathspecs)--noglob-pathspecs 
    
Add "literal" magic to all pathspec. This is equivalent to setting the `GIT_NOGLOB_PATHSPECS` environment variable to `1`. Enabling globbing on individual pathspecs can be done using pathspec magic ":(glob)" 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---icase-pathspecs)--icase-pathspecs 
    
Add "icase" magic to all pathspec. This is equivalent to setting the `GIT_ICASE_PATHSPECS` environment variable to `1`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---no-optional-locks)--no-optional-locks 
    
Do not perform optional operations that require locks. This is equivalent to setting the `GIT_OPTIONAL_LOCKS` to `0`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt---list-cmdsgroupgroup)--list-cmds=group[,group…​] 
    
List commands by group. This is an internal/experimental option and may change or be removed in the future. Supported groups are: builtins, parseopt (builtin commands that use parse-options), main (all commands in libexec directory), others (all other commands in `$PATH` that have git- prefix), list-<category> (see categories in command-list.txt), nohelpers (exclude helper commands), alias and config (retrieve command list from config variable completion.commands)
##  [](https://git-scm.com/docs/git/2.25.1#_git_commands)GIT COMMANDS
We divide Git into high level ("porcelain") commands and low level ("plumbing") commands.
##  [](https://git-scm.com/docs/git/2.25.1#_high_level_commands_porcelain)High-level commands (porcelain)
We separate the porcelain commands into the main commands and some ancillary user utilities.
###  [](https://git-scm.com/docs/git/2.25.1#_main_porcelain_commands)Main porcelain commands 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-add1)[git-add[1]](https://git-scm.com/docs/git-add) 
    
Add file contents to the index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-am1)[git-am[1]](https://git-scm.com/docs/git-am) 
    
Apply a series of patches from a mailbox 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-archive1)[git-archive[1]](https://git-scm.com/docs/git-archive) 
    
Create an archive of files from a named tree 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-bisect1)[git-bisect[1]](https://git-scm.com/docs/git-bisect) 
    
Use binary search to find the commit that introduced a bug 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-branch1)[git-branch[1]](https://git-scm.com/docs/git-branch) 
    
List, create, or delete branches 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-bundle1)[git-bundle[1]](https://git-scm.com/docs/git-bundle) 
    
Move objects and refs by archive 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-checkout1)[git-checkout[1]](https://git-scm.com/docs/git-checkout) 
    
Switch branches or restore working tree files 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-cherry-pick1)[git-cherry-pick[1]](https://git-scm.com/docs/git-cherry-pick) 
    
Apply the changes introduced by some existing commits 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-citool1)[git-citool[1]](https://git-scm.com/docs/git-citool) 
    
Graphical alternative to git-commit 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-clean1)[git-clean[1]](https://git-scm.com/docs/git-clean) 
    
Remove untracked files from the working tree 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-clone1)[git-clone[1]](https://git-scm.com/docs/git-clone) 
    
Clone a repository into a new directory 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-commit1)[git-commit[1]](https://git-scm.com/docs/git-commit) 
    
Record changes to the repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-describe1)[git-describe[1]](https://git-scm.com/docs/git-describe) 
    
Give an object a human readable name based on an available ref 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-diff1)[git-diff[1]](https://git-scm.com/docs/git-diff) 
    
Show changes between commits, commit and working tree, etc 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-fetch1)[git-fetch[1]](https://git-scm.com/docs/git-fetch) 
    
Download objects and refs from another repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-format-patch1)[git-format-patch[1]](https://git-scm.com/docs/git-format-patch) 
    
Prepare patches for e-mail submission 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-gc1)[git-gc[1]](https://git-scm.com/docs/git-gc) 
    
Cleanup unnecessary files and optimize the local repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-grep1)[git-grep[1]](https://git-scm.com/docs/git-grep) 
    
Print lines matching a pattern 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-gui1)[git-gui[1]](https://git-scm.com/docs/git-gui) 
    
A portable graphical interface to Git 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-init1)[git-init[1]](https://git-scm.com/docs/git-init) 
    
Create an empty Git repository or reinitialize an existing one 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-gitk1)[gitk[1]](https://git-scm.com/docs/gitk) 
    
The Git repository browser 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-log1)[git-log[1]](https://git-scm.com/docs/git-log) 
    
Show commit logs 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-merge1)[git-merge[1]](https://git-scm.com/docs/git-merge) 
    
Join two or more development histories together 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-mv1)[git-mv[1]](https://git-scm.com/docs/git-mv) 
    
Move or rename a file, a directory, or a symlink 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-notes1)[git-notes[1]](https://git-scm.com/docs/git-notes) 
    
Add or inspect object notes 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-pull1)[git-pull[1]](https://git-scm.com/docs/git-pull) 
    
Fetch from and integrate with another repository or a local branch 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-push1)[git-push[1]](https://git-scm.com/docs/git-push) 
    
Update remote refs along with associated objects 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-range-diff1)[git-range-diff[1]](https://git-scm.com/docs/git-range-diff) 
    
Compare two commit ranges (e.g. two versions of a branch) 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-rebase1)[git-rebase[1]](https://git-scm.com/docs/git-rebase) 
    
Reapply commits on top of another base tip 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-reset1)[git-reset[1]](https://git-scm.com/docs/git-reset) 
    
Reset current HEAD to the specified state 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-restore1)[git-restore[1]](https://git-scm.com/docs/git-restore) 
    
Restore working tree files 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-revert1)[git-revert[1]](https://git-scm.com/docs/git-revert) 
    
Revert some existing commits 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-rm1)[git-rm[1]](https://git-scm.com/docs/git-rm) 
    
Remove files from the working tree and from the index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-shortlog1)[git-shortlog[1]](https://git-scm.com/docs/git-shortlog) 
    
Summarize _git log_ output 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-show1)[git-show[1]](https://git-scm.com/docs/git-show) 
    
Show various types of objects 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-sparse-checkout1)[git-sparse-checkout[1]](https://git-scm.com/docs/git-sparse-checkout) 
    
Initialize and modify the sparse-checkout 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-stash1)[git-stash[1]](https://git-scm.com/docs/git-stash) 
    
Stash the changes in a dirty working directory away 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-status1)[git-status[1]](https://git-scm.com/docs/git-status) 
    
Show the working tree status 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-submodule1)[git-submodule[1]](https://git-scm.com/docs/git-submodule) 
    
Initialize, update or inspect submodules 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-switch1)[git-switch[1]](https://git-scm.com/docs/git-switch) 
    
Switch branches 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-tag1)[git-tag[1]](https://git-scm.com/docs/git-tag) 
    
Create, list, delete or verify a tag object signed with GPG 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-worktree1)[git-worktree[1]](https://git-scm.com/docs/git-worktree) 
    
Manage multiple working trees
###  [](https://git-scm.com/docs/git/2.25.1#_ancillary_commands)Ancillary Commands
Manipulators: 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-config1)[git-config[1]](https://git-scm.com/docs/git-config) 
    
Get and set repository or global options 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-fast-export1)[git-fast-export[1]](https://git-scm.com/docs/git-fast-export) 
    
Git data exporter 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-fast-import1)[git-fast-import[1]](https://git-scm.com/docs/git-fast-import) 
    
Backend for fast Git data importers 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-filter-branch1)[git-filter-branch[1]](https://git-scm.com/docs/git-filter-branch) 
    
Rewrite branches 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-mergetool1)[git-mergetool[1]](https://git-scm.com/docs/git-mergetool) 
    
Run merge conflict resolution tools to resolve merge conflicts 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-pack-refs1)[git-pack-refs[1]](https://git-scm.com/docs/git-pack-refs) 
    
Pack heads and tags for efficient repository access 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-prune1)[git-prune[1]](https://git-scm.com/docs/git-prune) 
    
Prune all unreachable objects from the object database 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-reflog1)[git-reflog[1]](https://git-scm.com/docs/git-reflog) 
    
Manage reflog information 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-remote1)[git-remote[1]](https://git-scm.com/docs/git-remote) 
    
Manage set of tracked repositories 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-repack1)[git-repack[1]](https://git-scm.com/docs/git-repack) 
    
Pack unpacked objects in a repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-replace1)[git-replace[1]](https://git-scm.com/docs/git-replace) 
    
Create, list, delete refs to replace objects
Interrogators: 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-annotate1)[git-annotate[1]](https://git-scm.com/docs/git-annotate) 
    
Annotate file lines with commit information 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-blame1)[git-blame[1]](https://git-scm.com/docs/git-blame) 
    
Show what revision and author last modified each line of a file 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-count-objects1)[git-count-objects[1]](https://git-scm.com/docs/git-count-objects) 
    
Count unpacked number of objects and their disk consumption 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-difftool1)[git-difftool[1]](https://git-scm.com/docs/git-difftool) 
    
Show changes using common diff tools 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-fsck1)[git-fsck[1]](https://git-scm.com/docs/git-fsck) 
    
Verifies the connectivity and validity of the objects in the database 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-help1)[git-help[1]](https://git-scm.com/docs/git-help) 
    
Display help information about Git 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-instaweb1)[git-instaweb[1]](https://git-scm.com/docs/git-instaweb) 
    
Instantly browse your working repository in gitweb 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-merge-tree1)[git-merge-tree[1]](https://git-scm.com/docs/git-merge-tree) 
    
Show three-way merge without touching index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-rerere1)[git-rerere[1]](https://git-scm.com/docs/git-rerere) 
    
Reuse recorded resolution of conflicted merges 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-show-branch1)[git-show-branch[1]](https://git-scm.com/docs/git-show-branch) 
    
Show branches and their commits 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-verify-commit1)[git-verify-commit[1]](https://git-scm.com/docs/git-verify-commit) 
    
Check the GPG signature of commits 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-verify-tag1)[git-verify-tag[1]](https://git-scm.com/docs/git-verify-tag) 
    
Check the GPG signature of tags 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-gitweb1)[gitweb[1]](https://git-scm.com/docs/gitweb) 
    
Git web interface (web frontend to Git repositories) 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-whatchanged1)[git-whatchanged[1]](https://git-scm.com/docs/git-whatchanged) 
    
Show logs with difference each commit introduces
###  [](https://git-scm.com/docs/git/2.25.1#_interacting_with_others)Interacting with Others
These commands are to interact with foreign SCM and with other people via patch over e-mail. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-archimport1)[git-archimport[1]](https://git-scm.com/docs/git-archimport) 
    
Import a GNU Arch repository into Git 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-cvsexportcommit1)[git-cvsexportcommit[1]](https://git-scm.com/docs/git-cvsexportcommit) 
    
Export a single commit to a CVS checkout 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-cvsimport1)[git-cvsimport[1]](https://git-scm.com/docs/git-cvsimport) 
    
Salvage your data out of another SCM people love to hate 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-cvsserver1)[git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver) 
    
A CVS server emulator for Git 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-imap-send1)[git-imap-send[1]](https://git-scm.com/docs/git-imap-send) 
    
Send a collection of patches from stdin to an IMAP folder 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-p41)[git-p4[1]](https://git-scm.com/docs/git-p4) 
    
Import from and submit to Perforce repositories 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-quiltimport1)[git-quiltimport[1]](https://git-scm.com/docs/git-quiltimport) 
    
Applies a quilt patchset onto the current branch 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-request-pull1)[git-request-pull[1]](https://git-scm.com/docs/git-request-pull) 
    
Generates a summary of pending changes 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-send-email1)[git-send-email[1]](https://git-scm.com/docs/git-send-email) 
    
Send a collection of patches as emails 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-svn1)[git-svn[1]](https://git-scm.com/docs/git-svn) 
    
Bidirectional operation between a Subversion repository and Git
###  [](https://git-scm.com/docs/git/2.25.1#_reset_restore_and_revert)Reset, restore and revert
There are three commands with similar names: `git` `reset`, `git` `restore` and `git` `revert`.
  * [git-revert[1]](https://git-scm.com/docs/git-revert) is about making a new commit that reverts the changes made by other commits.
  * [git-restore[1]](https://git-scm.com/docs/git-restore) is about restoring files in the working tree from either the index or another commit. This command does not update your branch. The command can also be used to restore files in the index from another commit.
  * [git-reset[1]](https://git-scm.com/docs/git-reset) is about updating your branch, moving the tip in order to add or remove commits from the branch. This operation changes the commit history.
`git` `reset` can also be used to restore the index, overlapping with `git` `restore`.


##  [](https://git-scm.com/docs/git/2.25.1#_low_level_commands_plumbing)Low-level commands (plumbing)
Although Git includes its own porcelain layer, its low-level commands are sufficient to support development of alternative porcelains. Developers of such porcelains might start by reading about [git-update-index[1]](https://git-scm.com/docs/git-update-index) and [git-read-tree[1]](https://git-scm.com/docs/git-read-tree).
The interface (input, output, set of options and the semantics) to these low-level commands are meant to be a lot more stable than Porcelain level commands, because these commands are primarily for scripted use. The interface to Porcelain commands on the other hand are subject to change in order to improve the end user experience.
The following description divides the low-level commands into commands that manipulate objects (in the repository, index, and working tree), commands that interrogate and compare objects, and commands that move objects and references between repositories.
###  [](https://git-scm.com/docs/git/2.25.1#_manipulation_commands)Manipulation commands 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-apply1)[git-apply[1]](https://git-scm.com/docs/git-apply) 
    
Apply a patch to files and/or to the index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-checkout-index1)[git-checkout-index[1]](https://git-scm.com/docs/git-checkout-index) 
    
Copy files from the index to the working tree 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-commit-graph1)[git-commit-graph[1]](https://git-scm.com/docs/git-commit-graph) 
    
Write and verify Git commit-graph files 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-commit-tree1)[git-commit-tree[1]](https://git-scm.com/docs/git-commit-tree) 
    
Create a new commit object 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-hash-object1)[git-hash-object[1]](https://git-scm.com/docs/git-hash-object) 
    
Compute object ID and optionally creates a blob from a file 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-index-pack1)[git-index-pack[1]](https://git-scm.com/docs/git-index-pack) 
    
Build pack index file for an existing packed archive 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-merge-file1)[git-merge-file[1]](https://git-scm.com/docs/git-merge-file) 
    
Run a three-way file merge 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-merge-index1)[git-merge-index[1]](https://git-scm.com/docs/git-merge-index) 
    
Run a merge for files needing merging 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-multi-pack-index1)[git-multi-pack-index[1]](https://git-scm.com/docs/git-multi-pack-index) 
    
Write and verify multi-pack-indexes 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-mktag1)[git-mktag[1]](https://git-scm.com/docs/git-mktag) 
    
Creates a tag object 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-mktree1)[git-mktree[1]](https://git-scm.com/docs/git-mktree) 
    
Build a tree-object from ls-tree formatted text 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-pack-objects1)[git-pack-objects[1]](https://git-scm.com/docs/git-pack-objects) 
    
Create a packed archive of objects 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-prune-packed1)[git-prune-packed[1]](https://git-scm.com/docs/git-prune-packed) 
    
Remove extra objects that are already in pack files 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-read-tree1)[git-read-tree[1]](https://git-scm.com/docs/git-read-tree) 
    
Reads tree information into the index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-symbolic-ref1)[git-symbolic-ref[1]](https://git-scm.com/docs/git-symbolic-ref) 
    
Read, modify and delete symbolic refs 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-unpack-objects1)[git-unpack-objects[1]](https://git-scm.com/docs/git-unpack-objects) 
    
Unpack objects from a packed archive 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-update-index1)[git-update-index[1]](https://git-scm.com/docs/git-update-index) 
    
Register file contents in the working tree to the index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-update-ref1)[git-update-ref[1]](https://git-scm.com/docs/git-update-ref) 
    
Update the object name stored in a ref safely 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-write-tree1)[git-write-tree[1]](https://git-scm.com/docs/git-write-tree) 
    
Create a tree object from the current index
###  [](https://git-scm.com/docs/git/2.25.1#_interrogation_commands)Interrogation commands 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-cat-file1)[git-cat-file[1]](https://git-scm.com/docs/git-cat-file) 
    
Provide content or type and size information for repository objects 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-cherry1)[git-cherry[1]](https://git-scm.com/docs/git-cherry) 
    
Find commits yet to be applied to upstream 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-diff-files1)[git-diff-files[1]](https://git-scm.com/docs/git-diff-files) 
    
Compares files in the working tree and the index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-diff-index1)[git-diff-index[1]](https://git-scm.com/docs/git-diff-index) 
    
Compare a tree to the working tree or index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-diff-tree1)[git-diff-tree[1]](https://git-scm.com/docs/git-diff-tree) 
    
Compares the content and mode of blobs found via two tree objects 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-for-each-ref1)[git-for-each-ref[1]](https://git-scm.com/docs/git-for-each-ref) 
    
Output information on each ref 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-get-tar-commit-id1)[git-get-tar-commit-id[1]](https://git-scm.com/docs/git-get-tar-commit-id) 
    
Extract commit ID from an archive created using git-archive 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-ls-files1)[git-ls-files[1]](https://git-scm.com/docs/git-ls-files) 
    
Show information about files in the index and the working tree 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-ls-remote1)[git-ls-remote[1]](https://git-scm.com/docs/git-ls-remote) 
    
List references in a remote repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-ls-tree1)[git-ls-tree[1]](https://git-scm.com/docs/git-ls-tree) 
    
List the contents of a tree object 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-merge-base1)[git-merge-base[1]](https://git-scm.com/docs/git-merge-base) 
    
Find as good common ancestors as possible for a merge 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-name-rev1)[git-name-rev[1]](https://git-scm.com/docs/git-name-rev) 
    
Find symbolic names for given revs 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-pack-redundant1)[git-pack-redundant[1]](https://git-scm.com/docs/git-pack-redundant) 
    
Find redundant pack files 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-rev-list1)[git-rev-list[1]](https://git-scm.com/docs/git-rev-list) 
    
Lists commit objects in reverse chronological order 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-rev-parse1)[git-rev-parse[1]](https://git-scm.com/docs/git-rev-parse) 
    
Pick out and massage parameters 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-show-index1)[git-show-index[1]](https://git-scm.com/docs/git-show-index) 
    
Show packed archive index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-show-ref1)[git-show-ref[1]](https://git-scm.com/docs/git-show-ref) 
    
List references in a local repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-unpack-file1)[git-unpack-file[1]](https://git-scm.com/docs/git-unpack-file) 
    
Creates a temporary file with a blob’s contents 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-var1)[git-var[1]](https://git-scm.com/docs/git-var) 
    
Show a Git logical variable 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-verify-pack1)[git-verify-pack[1]](https://git-scm.com/docs/git-verify-pack) 
    
Validate packed Git archive files
In general, the interrogate commands do not touch the files in the working tree.
###  [](https://git-scm.com/docs/git/2.25.1#_syncing_repositories)Syncing repositories 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-daemon1)[git-daemon[1]](https://git-scm.com/docs/git-daemon) 
    
A really simple server for Git repositories 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-fetch-pack1)[git-fetch-pack[1]](https://git-scm.com/docs/git-fetch-pack) 
    
Receive missing objects from another repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-http-backend1)[git-http-backend[1]](https://git-scm.com/docs/git-http-backend) 
    
Server side implementation of Git over HTTP 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-send-pack1)[git-send-pack[1]](https://git-scm.com/docs/git-send-pack) 
    
Push objects over Git protocol to another repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-update-server-info1)[git-update-server-info[1]](https://git-scm.com/docs/git-update-server-info) 
    
Update auxiliary info file to help dumb servers
The following are helper commands used by the above; end users typically do not use them directly. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-http-fetch1)[git-http-fetch[1]](https://git-scm.com/docs/git-http-fetch) 
    
Download from a remote Git repository via HTTP 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-http-push1)[git-http-push[1]](https://git-scm.com/docs/git-http-push) 
    
Push objects over HTTP/DAV to another repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-parse-remote1)[git-parse-remote[1]](https://git-scm.com/docs/git-parse-remote) 
    
Routines to help parsing remote repository access parameters 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-receive-pack1)[git-receive-pack[1]](https://git-scm.com/docs/git-receive-pack) 
    
Receive what is pushed into the repository 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-shell1)[git-shell[1]](https://git-scm.com/docs/git-shell) 
    
Restricted login shell for Git-only SSH access 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-upload-archive1)[git-upload-archive[1]](https://git-scm.com/docs/git-upload-archive) 
    
Send archive back to git-archive 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-upload-pack1)[git-upload-pack[1]](https://git-scm.com/docs/git-upload-pack) 
    
Send objects packed back to git-fetch-pack
###  [](https://git-scm.com/docs/git/2.25.1#_internal_helper_commands)Internal helper commands
These are internal helper commands used by other commands; end users typically do not use them directly. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-check-attr1)[git-check-attr[1]](https://git-scm.com/docs/git-check-attr) 
    
Display gitattributes information 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-check-ignore1)[git-check-ignore[1]](https://git-scm.com/docs/git-check-ignore) 
    
Debug gitignore / exclude files 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-check-mailmap1)[git-check-mailmap[1]](https://git-scm.com/docs/git-check-mailmap) 
    
Show canonical names and email addresses of contacts 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-check-ref-format1)[git-check-ref-format[1]](https://git-scm.com/docs/git-check-ref-format) 
    
Ensures that a reference name is well formed 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-column1)[git-column[1]](https://git-scm.com/docs/git-column) 
    
Display data in columns 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-credential1)[git-credential[1]](https://git-scm.com/docs/git-credential) 
    
Retrieve and store user credentials 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-credential-cache1)[git-credential-cache[1]](https://git-scm.com/docs/git-credential-cache) 
    
Helper to temporarily store passwords in memory 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-credential-store1)[git-credential-store[1]](https://git-scm.com/docs/git-credential-store) 
    
Helper to store credentials on disk 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-fmt-merge-msg1)[git-fmt-merge-msg[1]](https://git-scm.com/docs/git-fmt-merge-msg) 
    
Produce a merge commit message 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-interpret-trailers1)[git-interpret-trailers[1]](https://git-scm.com/docs/git-interpret-trailers) 
    
Add or parse structured information in commit messages 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-mailinfo1)[git-mailinfo[1]](https://git-scm.com/docs/git-mailinfo) 
    
Extracts patch and authorship from a single e-mail message 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-mailsplit1)[git-mailsplit[1]](https://git-scm.com/docs/git-mailsplit) 
    
Simple UNIX mbox splitter program 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-merge-one-file1)[git-merge-one-file[1]](https://git-scm.com/docs/git-merge-one-file) 
    
The standard helper program to use with git-merge-index 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-patch-id1)[git-patch-id[1]](https://git-scm.com/docs/git-patch-id) 
    
Compute unique ID for a patch 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-sh-i18n1)[git-sh-i18n[1]](https://git-scm.com/docs/git-sh-i18n) 
    
Git’s i18n setup code for shell scripts 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-sh-setup1)[git-sh-setup[1]](https://git-scm.com/docs/git-sh-setup) 
    
Common Git shell script setup code 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-git-stripspace1)[git-stripspace[1]](https://git-scm.com/docs/git-stripspace) 
    
Remove unnecessary whitespace
##  [](https://git-scm.com/docs/git/2.25.1#_configuration_mechanism)Configuration Mechanism
Git uses a simple text format to store customizations that are per repository and are per user. Such a configuration file may look like this:
```
#
# A '#' or ';' character indicates a comment.
#

; core variables
[core]
	; Don't trust file modes
	filemode = false

; user identity
[user]
	name = "Junio C Hamano"
	email = "gitster@pobox.com"
```

Various commands read from the configuration file and adjust their operation accordingly. See [git-config[1]](https://git-scm.com/docs/git-config) for a list and more details about the configuration mechanism.
##  [](https://git-scm.com/docs/git/2.25.1#_identifier_terminology)Identifier Terminology 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-object)<object> 
    
Indicates the object name for any type of object. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-blob)<blob> 
    
Indicates a blob object name. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-tree)<tree> 
    
Indicates a tree object name. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-commit)<commit> 
    
Indicates a commit object name. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-tree-ish)<tree-ish> 
    
Indicates a tree, commit or tag object name. A command that takes a <tree-ish> argument ultimately wants to operate on a <tree> object but automatically dereferences <commit> and <tag> objects that point at a <tree>. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-commit-ish)<commit-ish> 
    
Indicates a commit or tag object name. A command that takes a <commit-ish> argument ultimately wants to operate on a <commit> object but automatically dereferences <tag> objects that point at a <commit>. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-type)<type> 
    
Indicates that an object type is required. Currently one of: `blob`, `tree`, `commit`, or `tag`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-file)<file> 
    
Indicates a filename - almost always relative to the root of the tree structure `GIT_INDEX_FILE` describes.
##  [](https://git-scm.com/docs/git/2.25.1#_symbolic_identifiers)Symbolic Identifiers
Any Git command accepting any <object> can also use the following symbolic notation: 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-HEAD)HEAD 
    
indicates the head of the current branch. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-tag)<tag> 
    
a valid tag _name_ (i.e. a `refs/tags/`_< tag>_ reference). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-head)<head> 
    
a valid head _name_ (i.e. a `refs/heads/`_< head>_ reference).
For a more complete list of ways to spell object names, see "SPECIFYING REVISIONS" section in [gitrevisions[7]](https://git-scm.com/docs/gitrevisions).
##  [](https://git-scm.com/docs/git/2.25.1#_filedirectory_structure)File/Directory Structure
Please see the [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout) document.
Read [githooks[5]](https://git-scm.com/docs/githooks) for more details about each hook.
Higher level SCMs may provide and manage additional information in the `$GIT_DIR`.
##  [](https://git-scm.com/docs/git/2.25.1#_terminology)Terminology
Please see [gitglossary[7]](https://git-scm.com/docs/gitglossary).
##  [](https://git-scm.com/docs/git/2.25.1#_environment_variables)Environment Variables
Various Git commands use the following environment variables:
###  [](https://git-scm.com/docs/git/2.25.1#_the_git_repository)The Git Repository
These environment variables apply to _all_ core Git commands. Nb: it is worth noting that they may be used/overridden by SCMS sitting above Git so take care if using a foreign front-end. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITINDEXFILE)`GIT_INDEX_FILE` 
    
This environment allows the specification of an alternate index file. If not specified, the default of `$GIT_DIR/index` is used. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITINDEXVERSION)`GIT_INDEX_VERSION` 
    
This environment variable allows the specification of an index version for new repositories. It won’t affect existing index files. By default index file version 2 or 3 is used. See [git-update-index[1]](https://git-scm.com/docs/git-update-index) for more information. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITOBJECTDIRECTORY)`GIT_OBJECT_DIRECTORY` 
    
If the object storage directory is specified via this environment variable then the sha1 directories are created underneath - otherwise the default `$GIT_DIR/objects` directory is used. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITALTERNATEOBJECTDIRECTORIES)`GIT_ALTERNATE_OBJECT_DIRECTORIES` 
    
Due to the immutable nature of Git objects, old objects can be archived into shared, read-only directories. This variable specifies a ":" separated (on Windows ";" separated) list of Git object directories which can be used to search for Git objects. New objects will not be written to these directories.
Entries that begin with `"` (double-quote) will be interpreted as C-style quoted paths, removing leading and trailing double-quotes and respecting backslash escapes. E.g., the value _"path-with-\"-and-:-in-it":vanilla-path_ has two paths: `path-with-"-and-:-in-it` and `vanilla-path`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITDIR)`GIT_DIR` 
    
If the `GIT_DIR` environment variable is set then it specifies a path to use instead of the default `.git` for the base of the repository. The `--git-dir` command-line option also sets this value. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITWORKTREE)`GIT_WORK_TREE` 
    
Set the path to the root of the working tree. This can also be controlled by the `--work-tree` command-line option and the core.worktree configuration variable. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITNAMESPACE)`GIT_NAMESPACE` 
    
Set the Git namespace; see [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces) for details. The `--namespace` command-line option also sets this value. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITCEILINGDIRECTORIES)`GIT_CEILING_DIRECTORIES` 
    
This should be a colon-separated list of absolute paths. If set, it is a list of directories that Git should not chdir up into while looking for a repository directory (useful for excluding slow-loading network directories). It will not exclude the current working directory or a GIT_DIR set on the command line or in the environment. Normally, Git has to read the entries in this list and resolve any symlink that might be present in order to compare them with the current directory. However, if even this access is slow, you can add an empty entry to the list to tell Git that the subsequent entries are not symlinks and needn’t be resolved; e.g., `GIT_CEILING_DIRECTORIES=/maybe/symlink::/very/slow/non/symlink`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITDISCOVERYACROSSFILESYSTEM)`GIT_DISCOVERY_ACROSS_FILESYSTEM` 
    
When run in a directory that does not have ".git" repository directory, Git tries to find such a directory in the parent directories to find the top of the working tree, but by default it does not cross filesystem boundaries. This environment variable can be set to true to tell Git not to stop at filesystem boundaries. Like `GIT_CEILING_DIRECTORIES`, this will not affect an explicit repository directory set via `GIT_DIR` or on the command line. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITCOMMONDIR)`GIT_COMMON_DIR` 
    
If this variable is set to a path, non-worktree files that are normally in $GIT_DIR will be taken from this path instead. Worktree-specific files such as HEAD or index are taken from $GIT_DIR. See [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout) and [git-worktree[1]](https://git-scm.com/docs/git-worktree) for details. This variable has lower precedence than other path variables such as GIT_INDEX_FILE, GIT_OBJECT_DIRECTORY…​
###  [](https://git-scm.com/docs/git/2.25.1#_git_commits)Git Commits 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITAUTHORNAME)`GIT_AUTHOR_NAME` 
    
The human-readable name used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.name` and `author.name` configuration settings. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITAUTHOREMAIL)`GIT_AUTHOR_EMAIL` 
    
The email address used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.email` and `author.email` configuration settings. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITAUTHORDATE)`GIT_AUTHOR_DATE` 
    
The date used for the author identity when creating commit or tag objects, or when writing reflogs. See [git-commit[1]](https://git-scm.com/docs/git-commit) for valid formats. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITCOMMITTERNAME)`GIT_COMMITTER_NAME` 
    
The human-readable name used in the committer identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.name` and `committer.name` configuration settings. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITCOMMITTEREMAIL)`GIT_COMMITTER_EMAIL` 
    
The email address used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.email` and `committer.email` configuration settings. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITCOMMITTERDATE)`GIT_COMMITTER_DATE` 
    
The date used for the committer identity when creating commit or tag objects, or when writing reflogs. See [git-commit[1]](https://git-scm.com/docs/git-commit) for valid formats. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-EMAIL)`EMAIL` 
    
The email address used in the author and committer identities if no other relevant environment variable or configuration setting has been set.
###  [](https://git-scm.com/docs/git/2.25.1#_git_diffs)Git Diffs 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITDIFFOPTS)`GIT_DIFF_OPTS` 
    
Only valid setting is "--unified=??" or "-u??" to set the number of context lines shown when a unified diff is created. This takes precedence over any "-U" or "--unified" option value passed on the Git diff command line. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITEXTERNALDIFF)`GIT_EXTERNAL_DIFF` 
    
When the environment variable `GIT_EXTERNAL_DIFF` is set, the program named by it is called, instead of the diff invocation described above. For a path that is added, removed, or modified, `GIT_EXTERNAL_DIFF` is called with 7 parameters:
```
path old-file old-hex old-mode new-file new-hex new-mode
```

where: 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-oldnew-file)<old|new>-file 
    
are files GIT_EXTERNAL_DIFF can use to read the contents of <old|new>, 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-oldnew-hex)<old|new>-hex 
    
are the 40-hexdigit SHA-1 hashes, 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-oldnew-mode)<old|new>-mode 
    
are the octal representation of the file modes.
The file parameters can point at the user’s working file (e.g. `new-file` in "git-diff-files"), `/dev/null` (e.g. `old-file` when a new file is added), or a temporary file (e.g. `old-file` in the index). `GIT_EXTERNAL_DIFF` should not worry about unlinking the temporary file --- it is removed when `GIT_EXTERNAL_DIFF` exits.
For a path that is unmerged, `GIT_EXTERNAL_DIFF` is called with 1 parameter, <path>.
For each path `GIT_EXTERNAL_DIFF` is called, two environment variables, `GIT_DIFF_PATH_COUNTER` and `GIT_DIFF_PATH_TOTAL` are set. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITDIFFPATHCOUNTER)`GIT_DIFF_PATH_COUNTER` 
    
A 1-based counter incremented by one for every path. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITDIFFPATHTOTAL)`GIT_DIFF_PATH_TOTAL` 
    
The total number of paths.
###  [](https://git-scm.com/docs/git/2.25.1#_other)other 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITMERGEVERBOSITY)`GIT_MERGE_VERBOSITY` 
    
A number controlling the amount of output shown by the recursive merge strategy. Overrides merge.verbosity. See [git-merge[1]](https://git-scm.com/docs/git-merge) 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITPAGER)`GIT_PAGER` 
    
This environment variable overrides `$PAGER`. If it is set to an empty string or to the value "cat", Git will not launch a pager. See also the `core.pager` option in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITPROGRESSDELAY)`GIT_PROGRESS_DELAY` 
    
A number controlling how many seconds to delay before showing optional progress indicators. Defaults to 2. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITEDITOR)`GIT_EDITOR` 
    
This environment variable overrides `$EDITOR` and `$VISUAL`. It is used by several Git commands when, on interactive mode, an editor is to be launched. See also [git-var[1]](https://git-scm.com/docs/git-var) and the `core.editor` option in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITSSH)`GIT_SSH` 


[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITSSHCOMMAND)`GIT_SSH_COMMAND` 
    
If either of these environment variables is set then _git fetch_ and _git push_ will use the specified command instead of _ssh_ when they need to connect to a remote system. The command-line parameters passed to the configured command are determined by the ssh variant. See `ssh.variant` option in [git-config[1]](https://git-scm.com/docs/git-config) for details.
`$GIT_SSH_COMMAND` takes precedence over `$GIT_SSH`, and is interpreted by the shell, which allows additional arguments to be included. `$GIT_SSH` on the other hand must be just the path to a program (which can be a wrapper shell script, if additional arguments are needed).
Usually it is easier to configure any desired options through your personal `.ssh/config` file. Please consult your ssh documentation for further details. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITSSHVARIANT)`GIT_SSH_VARIANT` 
    
If this environment variable is set, it overrides Git’s autodetection whether `GIT_SSH`/`GIT_SSH_COMMAND`/`core.sshCommand` refer to OpenSSH, plink or tortoiseplink. This variable overrides the config setting `ssh.variant` that serves the same purpose. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITASKPASS)`GIT_ASKPASS` 
    
If this environment variable is set, then Git commands which need to acquire passwords or passphrases (e.g. for HTTP or IMAP authentication) will call this program with a suitable prompt as command-line argument and read the password from its STDOUT. See also the `core.askPass` option in [git-config[1]](https://git-scm.com/docs/git-config). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTERMINALPROMPT)`GIT_TERMINAL_PROMPT` 
    
If this environment variable is set to `0`, git will not prompt on the terminal (e.g., when asking for HTTP authentication). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITCONFIGNOSYSTEM)`GIT_CONFIG_NOSYSTEM` 
    
Whether to skip reading settings from the system-wide `$`(`prefix`)`/etc/gitconfig` file. This environment variable can be used along with `$HOME` and `$XDG_CONFIG_HOME` to create a predictable environment for a picky script, or you can set it temporarily to avoid using a buggy `/etc/gitconfig` file while waiting for someone with sufficient permissions to fix it. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITFLUSH)`GIT_FLUSH` 
    
If this environment variable is set to "1", then commands such as _git blame_ (in incremental mode), _git rev-list_ , _git log_ , _git check-attr_ and _git check-ignore_ will force a flush of the output stream after each record have been flushed. If this variable is set to "0", the output of these commands will be done using completely buffered I/O. If this environment variable is not set, Git will choose buffered or record-oriented flushing based on whether stdout appears to be redirected to a file or not. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACE)`GIT_TRACE` 
    
Enables general trace messages, e.g. alias expansion, built-in command execution and external command execution.
If this variable is set to "1", "2" or "true" (comparison is case insensitive), trace messages will be printed to stderr.
If the variable is set to an integer value greater than 2 and lower than 10 (strictly) then Git will interpret this value as an open file descriptor and will try to write the trace messages into this file descriptor.
Alternatively, if the variable is set to an absolute path (starting with a _/_ character), Git will interpret this as a file path and will try to append the trace messages to it.
Unsetting the variable, or setting it to empty, "0" or "false" (case insensitive) disables trace messages. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACEFSMONITOR)`GIT_TRACE_FSMONITOR` 
    
Enables trace messages for the filesystem monitor extension. See `GIT_TRACE` for available trace output options. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACEPACKACCESS)`GIT_TRACE_PACK_ACCESS` 
    
Enables trace messages for all accesses to any packs. For each access, the pack file name and an offset in the pack is recorded. This may be helpful for troubleshooting some pack-related performance problems. See `GIT_TRACE` for available trace output options. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACEPACKET)`GIT_TRACE_PACKET` 
    
Enables trace messages for all packets coming in or out of a given program. This can help with debugging object negotiation or other protocol issues. Tracing is turned off at a packet starting with "PACK" (but see `GIT_TRACE_PACKFILE` below). See `GIT_TRACE` for available trace output options. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACEPACKFILE)`GIT_TRACE_PACKFILE` 
    
Enables tracing of packfiles sent or received by a given program. Unlike other trace output, this trace is verbatim: no headers, and no quoting of binary data. You almost certainly want to direct into a file (e.g., `GIT_TRACE_PACKFILE=/tmp/my.pack`) rather than displaying it on the terminal or mixing it with other trace output.
Note that this is currently only implemented for the client side of clones and fetches. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACEPERFORMANCE)`GIT_TRACE_PERFORMANCE` 
    
Enables performance related trace messages, e.g. total execution time of each Git command. See `GIT_TRACE` for available trace output options. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACESETUP)`GIT_TRACE_SETUP` 
    
Enables trace messages printing the .git, working tree and current working directory after Git has completed its setup phase. See `GIT_TRACE` for available trace output options. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACESHALLOW)`GIT_TRACE_SHALLOW` 
    
Enables trace messages that can help debugging fetching / cloning of shallow repositories. See `GIT_TRACE` for available trace output options. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACECURL)`GIT_TRACE_CURL` 
    
Enables a curl full trace dump of all incoming and outgoing data, including descriptive information, of the git transport protocol. This is similar to doing curl `--trace-ascii` on the command line. This option overrides setting the `GIT_CURL_VERBOSE` environment variable. See `GIT_TRACE` for available trace output options. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACECURLNODATA)`GIT_TRACE_CURL_NO_DATA` 
    
When a curl trace is enabled (see `GIT_TRACE_CURL` above), do not dump data (that is, only dump info lines and headers). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACE2)`GIT_TRACE2` 
    
Enables more detailed trace messages from the "trace2" library. Output from `GIT_TRACE2` is a simple text-based format for human readability.
If this variable is set to "1", "2" or "true" (comparison is case insensitive), trace messages will be printed to stderr.
If the variable is set to an integer value greater than 2 and lower than 10 (strictly) then Git will interpret this value as an open file descriptor and will try to write the trace messages into this file descriptor.
Alternatively, if the variable is set to an absolute path (starting with a _/_ character), Git will interpret this as a file path and will try to append the trace messages to it. If the path already exists and is a directory, the trace messages will be written to files (one per process) in that directory, named according to the last component of the SID and an optional counter (to avoid filename collisions).
In addition, if the variable is set to `af_unix:`[_< socket_type>_`:`]_< absolute-pathname>_, Git will try to open the path as a Unix Domain Socket. The socket type can be either `stream` or `dgram`.
Unsetting the variable, or setting it to empty, "0" or "false" (case insensitive) disables trace messages.
See [Trace2 documentation](https://git-scm.com/docs/api-trace2) for full details. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACE2EVENT)`GIT_TRACE2_EVENT` 
    
This setting writes a JSON-based format that is suited for machine interpretation. See `GIT_TRACE2` for available trace output options and [Trace2 documentation](https://git-scm.com/docs/api-trace2) for full details. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITTRACE2PERF)`GIT_TRACE2_PERF` 
    
In addition to the text-based messages available in `GIT_TRACE2`, this setting writes a column-based format for understanding nesting regions. See `GIT_TRACE2` for available trace output options and [Trace2 documentation](https://git-scm.com/docs/api-trace2) for full details. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITREDACTCOOKIES)`GIT_REDACT_COOKIES` 
    
This can be set to a comma-separated list of strings. When a curl trace is enabled (see `GIT_TRACE_CURL` above), whenever a "Cookies:" header sent by the client is dumped, values of cookies whose key is in that list (case-sensitive) are redacted. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITLITERALPATHSPECS)`GIT_LITERAL_PATHSPECS` 
    
Setting this variable to `1` will cause Git to treat all pathspecs literally, rather than as glob patterns. For example, running `GIT_LITERAL_PATHSPECS=1` `git` `log` `--` `*.c'` will search for commits that touch the path `*.c`, not any paths that the glob `*.c` matches. You might want this if you are feeding literal paths to Git (e.g., paths previously given to you by `git` `ls-tree`, `--raw` diff output, etc). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITGLOBPATHSPECS)`GIT_GLOB_PATHSPECS` 
    
Setting this variable to `1` will cause Git to treat all pathspecs as glob patterns (aka "glob" magic). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITNOGLOBPATHSPECS)`GIT_NOGLOB_PATHSPECS` 
    
Setting this variable to `1` will cause Git to treat all pathspecs as literal (aka "literal" magic). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITICASEPATHSPECS)`GIT_ICASE_PATHSPECS` 
    
Setting this variable to `1` will cause Git to treat all pathspecs as case-insensitive. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITREFLOGACTION)`GIT_REFLOG_ACTION` 
    
When a ref is updated, reflog entries are created to keep track of the reason why the ref was updated (which is typically the name of the high-level command that updated the ref), in addition to the old and new values of the ref. A scripted Porcelain command can use set_reflog_action helper function in `git-sh-setup` to set its name to this variable when it is invoked as the top level command by the end user, to be recorded in the body of the reflog. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITREFPARANOIA)`GIT_REF_PARANOIA` 
    
If set to `1`, include broken or badly named refs when iterating over lists of refs. In a normal, non-corrupted repository, this does nothing. However, enabling it may help git to detect and abort some operations in the presence of broken refs. Git sets this variable automatically when performing destructive operations like [git-prune[1]](https://git-scm.com/docs/git-prune). You should not need to set it yourself unless you want to be paranoid about making sure an operation has touched every ref (e.g., because you are cloning a repository to make a backup). 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITALLOWPROTOCOL)`GIT_ALLOW_PROTOCOL` 
    
If set to a colon-separated list of protocols, behave as if `protocol.allow` is set to `never`, and each of the listed protocols has `protocol.`_< name>_`.allow` set to `always` (overriding any existing configuration). In other words, any protocol not mentioned will be disallowed (i.e., this is a whitelist, not a blacklist). See the description of `protocol.allow` in [git-config[1]](https://git-scm.com/docs/git-config) for more details. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITPROTOCOLFROMUSER)`GIT_PROTOCOL_FROM_USER` 
    
Set to 0 to prevent protocols used by fetch/push/clone which are configured to the `user` state. This is useful to restrict recursive submodule initialization from an untrusted repository or for programs which feed potentially-untrusted URLS to git commands. See [git-config[1]](https://git-scm.com/docs/git-config) for more details. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITPROTOCOL)`GIT_PROTOCOL` 
    
For internal use only. Used in handshaking the wire protocol. Contains a colon _:_ separated list of keys with optional values _key[=value]_. Presence of unknown keys and values must be ignored. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITOPTIONALLOCKS)`GIT_OPTIONAL_LOCKS` 
    
If set to `0`, Git will complete any requested operation without performing any optional sub-operations that require taking a lock. For example, this will prevent `git` `status` from refreshing the index as a side effect. This is useful for processes running in the background which do not want to cause lock contention with other operations on the repository. Defaults to `1`. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITREDIRECTSTDIN)`GIT_REDIRECT_STDIN` 


[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITREDIRECTSTDOUT)`GIT_REDIRECT_STDOUT` 


[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITREDIRECTSTDERR)`GIT_REDIRECT_STDERR` 
    
Windows-only: allow redirecting the standard input/output/error handles to paths specified by the environment variables. This is particularly useful in multi-threaded applications where the canonical way to pass standard handles via `CreateProcess`() is not an option because it would require the handles to be marked inheritable (and consequently **every** spawned process would inherit them, possibly blocking regular Git operations). The primary intended use case is to use named pipes for communication (e.g. _\\\\.\pipe\my-git-stdin-123_).
Two special values are supported: `off` will simply close the corresponding standard handle, and if `GIT_REDIRECT_STDERR` is _2 >&1_, standard error will be redirected to the same handle as standard output. 

[](https://git-scm.com/docs/git/2.25.1#Documentation/git.txt-GITPRINTSHA1ELLIPSISdeprecated)`GIT_PRINT_SHA1_ELLIPSIS` (deprecated) 
    
If set to `yes`, print an ellipsis following an (abbreviated) SHA-1 value. This affects indications of detached HEADs ([git-checkout[1]](https://git-scm.com/docs/git-checkout)) and the raw diff output ([git-diff[1]](https://git-scm.com/docs/git-diff)). Printing an ellipsis in the cases mentioned is no longer considered adequate and support for it is likely to be removed in the foreseeable future (along with the variable).
##  [](https://git-scm.com/docs/git/2.25.1#_discussion)Discussion
More detail on the following is available from the [Git concepts chapter of the user-manual](https://git-scm.com/docs/user-manual#git-concepts) and [gitcore-tutorial[7]](https://git-scm.com/docs/gitcore-tutorial).
A Git project normally consists of a working directory with a ".git" subdirectory at the top level. The .git directory contains, among other things, a compressed object database representing the complete history of the project, an "index" file which links that history to the current contents of the working tree, and named pointers into that history such as tags and branch heads.
The object database contains objects of three main types: blobs, which hold file data; trees, which point to blobs and other trees to build up directory hierarchies; and commits, which each reference a single tree and some number of parent commits.
The commit, equivalent to what other systems call a "changeset" or "version", represents a step in the project’s history, and each parent represents an immediately preceding step. Commits with more than one parent represent merges of independent lines of development.
All objects are named by the SHA-1 hash of their contents, normally written as a string of 40 hex digits. Such names are globally unique. The entire history leading up to a commit can be vouched for by signing just that commit. A fourth object type, the tag, is provided for this purpose.
When first created, objects are stored in individual files, but for efficiency may later be compressed together into "pack files".
Named pointers called refs mark interesting points in history. A ref may contain the SHA-1 name of an object or the name of another ref. Refs with names beginning `ref/head/` contain the SHA-1 name of the most recent commit (or "head") of a branch under development. SHA-1 names of tags of interest are stored under `ref/tags/`. A special ref named `HEAD` contains the name of the currently checked-out branch.
The index file is initialized with a list of all paths and, for each path, a blob object and a set of attributes. The blob object represents the contents of the file as of the head of the current branch. The attributes (last modified time, size, etc.) are taken from the corresponding file in the working tree. Subsequent changes to the working tree can be found by comparing these attributes. The index may be updated with new content, and new commits may be created from the content stored in the index.
The index is also capable of storing multiple entries (called "stages") for a given pathname. These stages are used to hold the various unmerged version of a file when a merge is in progress.
##  [](https://git-scm.com/docs/git/2.25.1#_further_documentation)FURTHER DOCUMENTATION
See the references in the "description" section to get started using Git. The following is probably more detail than necessary for a first-time user.
The [Git concepts chapter of the user-manual](https://git-scm.com/docs/user-manual#git-concepts) and [gitcore-tutorial[7]](https://git-scm.com/docs/gitcore-tutorial) both provide introductions to the underlying Git architecture.
See [gitworkflows[7]](https://git-scm.com/docs/gitworkflows) for an overview of recommended workflows.
See also the [howto](https://git-scm.com/docs/howto-index) documents for some useful examples.
The internals are documented in the [Git API documentation](https://git-scm.com/docs/api-index).
Users migrating from CVS may also want to read [gitcvs-migration[7]](https://git-scm.com/docs/gitcvs-migration).
##  [](https://git-scm.com/docs/git/2.25.1#_authors)Authors
Git was started by Linus Torvalds, and is currently maintained by Junio C Hamano. Numerous contributions have come from the Git mailing list <git@vger.kernel.org>. <http://www.openhub.net/p/git/contributors/summary> gives you a more complete list of contributors.
If you have a clone of git.git itself, the output of [git-shortlog[1]](https://git-scm.com/docs/git-shortlog) and [git-blame[1]](https://git-scm.com/docs/git-blame) can show you the authors for specific parts of the project.
##  [](https://git-scm.com/docs/git/2.25.1#_reporting_bugs)Reporting Bugs
Report bugs to the Git mailing list <git@vger.kernel.org> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there. See the list archive at <https://lore.kernel.org/git> for previous bug reports and other discussions.
Issues which are security relevant should be disclosed privately to the Git Security mailing list <git-security@googlegroups.com>.
##  [](https://git-scm.com/docs/git/2.25.1#_see_also)SEE ALSO
[gittutorial[7]](https://git-scm.com/docs/gittutorial), [gittutorial-2[7]](https://git-scm.com/docs/gittutorial-2), [giteveryday[7]](https://git-scm.com/docs/giteveryday), [gitcvs-migration[7]](https://git-scm.com/docs/gitcvs-migration), [gitglossary[7]](https://git-scm.com/docs/gitglossary), [gitcore-tutorial[7]](https://git-scm.com/docs/gitcore-tutorial), [gitcli[7]](https://git-scm.com/docs/gitcli), [The Git User’s Manual](https://git-scm.com/docs/user-manual), [gitworkflows[7]](https://git-scm.com/docs/gitworkflows)
##  [](https://git-scm.com/docs/git/2.25.1#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### git
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
