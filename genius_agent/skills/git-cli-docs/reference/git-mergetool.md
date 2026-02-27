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
    * [NAME](https://git-scm.com/docs/git-mergetool#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-mergetool#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-mergetool#_description)
    * [OPTIONS](https://git-scm.com/docs/git-mergetool#_options)
    * [CONFIGURATION](https://git-scm.com/docs/git-mergetool#_configuration)
    * [TEMPORARY FILES](https://git-scm.com/docs/git-mergetool#_temporary_files)
    * [BACKEND SPECIFIC HINTS](https://git-scm.com/docs/git-mergetool#_backend_specific_hints)
    * [GIT](https://git-scm.com/docs/git-mergetool#_git)


[ English ▾](https://git-scm.com/docs/git-mergetool)
Localized versions of **git-mergetool** manual
  1. [English ](https://git-scm.com/docs/git-mergetool)
  2. [Français ](https://git-scm.com/docs/git-mergetool/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-mergetool/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-mergetool/sv)
  5. [українська мова ](https://git-scm.com/docs/git-mergetool/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-mergetool/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-mergetool)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-mergetool) git-mergetool last updated in 2.52.0
Changes in the **git-mergetool** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-mergetool/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-mergetool/2.51.1)
  5. 2.50.1 → 2.51.0 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-mergetool/2.50.0)
  7. 2.45.1 → 2.49.1 no changes
  8. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-mergetool/2.45.0)
  9. 2.43.1 → 2.44.4 no changes
  10. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-mergetool/2.43.0)
  11. 2.41.1 → 2.42.4 no changes
  12. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-mergetool/2.41.0)
  13. 2.38.3 → 2.40.4 no changes
  14. [2.38.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-11_ ](https://git-scm.com/docs/git-mergetool/2.38.2)
  15. 2.38.1 no changes
  16. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-mergetool/2.38.0)
  17. 2.37.1 → 2.37.7 no changes
  18. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-mergetool/2.37.0)
  19. 2.31.1 → 2.36.6 no changes
  20. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-mergetool/2.31.0)
  21. 2.22.1 → 2.30.9 no changes
  22. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-mergetool/2.22.0)
  23. 2.20.1 → 2.21.4 no changes
  24. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-mergetool/2.20.0)
  25. 2.12.5 → 2.19.6 no changes
  26. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-mergetool/2.11.4)
  27. 2.2.3 → 2.10.5 no changes
  28. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-mergetool/2.1.4)
  29. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-mergetool/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-mergetool#_name)NAME
git-mergetool - Run merge conflict resolution tools to resolve merge conflicts
##  [](https://git-scm.com/docs/git-mergetool#_synopsis)SYNOPSIS
```
git mergetool [--tool=_<tool>_] [-y | --[no-]prompt] [_<file>_…​]
```

##  [](https://git-scm.com/docs/git-mergetool#_description)DESCRIPTION
Use `git` `mergetool` to run one of several merge utilities to resolve merge conflicts. It is typically run after `git` `merge`.
If one or more <file> parameters are given, the merge tool program will be run to resolve differences in each file (skipping those without conflicts). Specifying a directory will include all unresolved files in that path. If no _< file>_ names are specified, `git` `mergetool` will run the merge tool program on every file with merge conflicts.
##  [](https://git-scm.com/docs/git-mergetool#_options)OPTIONS 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt--ttool)`-t` _< tool>_ 


[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt---tooltool)`--tool=`_< tool>_ 
    
Use the merge resolution program specified by _< tool>_. Valid values include `emerge`, `gvimdiff`, `kdiff3`, `meld`, `vimdiff`, and `tortoisemerge`. Run `git` `mergetool` `--tool-help` for the list of valid _< tool>_ settings.
If a merge resolution program is not specified, `git` `mergetool` will use the configuration variable `merge.tool`. If the configuration variable `merge.tool` is not set, `git` `mergetool` will pick a suitable default.
You can explicitly provide a full path to the tool by setting the configuration variable `mergetool.`_< tool>_`.path`. For example, you can configure the absolute path to kdiff3 by setting `mergetool.kdiff3.path`. Otherwise, `git` `mergetool` assumes the tool is available in `$PATH`.
Instead of running one of the known merge tool programs, `git` `mergetool` can be customized to run an alternative program by specifying the command line to invoke in a configuration variable `mergetool.`_< tool>_`.cmd`.
When `git` `mergetool` is invoked with this tool (either through the `-t` or `--tool` option or the `merge.tool` configuration variable), the configured command line will be invoked with `BASE` set to the name of a temporary file containing the common base for the merge, if available; `LOCAL` set to the name of a temporary file containing the contents of the file on the current branch; `REMOTE` set to the name of a temporary file containing the contents of the file to be merged, and `MERGED` set to the name of the file to which the merge tool should write the result of the merge resolution.
If the custom merge tool correctly indicates the success of a merge resolution with its exit code, then the configuration variable `mergetool.`_< tool>_`.trustExitCode` can be set to `true`. Otherwise, `git` `mergetool` will prompt the user to indicate the success of the resolution after the custom tool has exited. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt---tool-help)`--tool-help` 
    
Print a list of merge tools that may be used with `--tool`. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt--y)`-y` 


[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt---no-prompt)`--no-prompt` 
    
Don’t prompt before each invocation of the merge resolution program. This is the default if the merge resolution program is explicitly specified with the `--tool` option or with the `merge.tool` configuration variable. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt---prompt)`--prompt` 
    
Prompt before each invocation of the merge resolution program to give the user a chance to skip the path. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt--g)`-g` 


[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt---gui)`--gui` 
    
When `git-mergetool` is invoked with the `-g` or `--gui` option, the default merge tool will be read from the configured `merge.guitool` variable instead of `merge.tool`. If `merge.guitool` is not set, we will fallback to the tool configured under `merge.tool`. This may be autoselected using the configuration variable `mergetool.guiDefault`. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt---no-gui)`--no-gui` 
    
This overrides a previous `-g` or `--gui` setting or `mergetool.guiDefault` configuration and reads the default merge tool from the configured `merge.tool` variable. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt--Oorderfile)`-O`_< orderfile>_ 
    
Process files in the order specified in the _< orderfile>_, which has one shell glob pattern per line. This overrides the `diff.orderFile` configuration variable (see [git-config[1]](https://git-scm.com/docs/git-config)). To cancel `diff.orderFile`, use `-O/dev/null`.
##  [](https://git-scm.com/docs/git-mergetool#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetooltoolpath)`mergetool.`_< tool>_`.path` 
    
Override the path for the given tool. This is useful in case your tool is not in the `$PATH`. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetooltoolcmd)`mergetool.`_< tool>_`.cmd` 
    
Specify the command to invoke the specified merge tool. The specified command is evaluated in shell with the following variables available: `BASE` is the name of a temporary file containing the common base of the files to be merged, if available; `LOCAL` is the name of a temporary file containing the contents of the file on the current branch; `REMOTE` is the name of a temporary file containing the contents of the file from the branch being merged; `MERGED` contains the name of the file to which the merge tool should write the results of a successful merge. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetooltoolhideResolved)`mergetool.`_< tool>_`.hideResolved` 
    
Allows the user to override the global `mergetool.hideResolved` value for a specific tool. See `mergetool.hideResolved` for the full description. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetooltooltrustExitCode)`mergetool.`_< tool>_`.trustExitCode` 
    
For a custom merge command, specify whether the exit code of the merge command can be used to determine whether the merge was successful. If this is not set to true then the merge target file timestamp is checked, and the merge is assumed to have been successful if the file has been updated; otherwise, the user is prompted to indicate the success of the merge. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolmeldhasOutput)`mergetool.meld.hasOutput` 
    
Older versions of `meld` do not support the `--output` option. Git will attempt to detect whether `meld` supports `--output` by inspecting the output of `meld` `--help`. Configuring `mergetool.meld.hasOutput` will make Git skip these checks and use the configured value instead. Setting `mergetool.meld.hasOutput` to `true` tells Git to unconditionally use the `--output` option, and `false` avoids using `--output`. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolmelduseAutoMerge)`mergetool.meld.useAutoMerge` 
    
When the `--auto-merge` is given, meld will merge all non-conflicting parts automatically, highlight the conflicting parts, and wait for user decision. Setting `mergetool.meld.useAutoMerge` to `true` tells Git to unconditionally use the `--auto-merge` option with `meld`. Setting this value to `auto` makes git detect whether `--auto-merge` is supported and will only use `--auto-merge` when available. A value of `false` avoids using `--auto-merge` altogether, and is the default value. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolvariantlayout)`mergetool.`_< variant>_`.layout` 
    
Configure the split window layout for vimdiff’s _< variant>_, which is any of `vimdiff`, `nvimdiff`, `gvimdiff`. Upon launching `git` `mergetool` with `--tool=`_< variant>_ (or without `--tool` if `merge.tool` is configured as _< variant>_), Git will consult `mergetool.`_< variant>_`.layout` to determine the tool’s layout. If the variant-specific configuration is not available, `vimdiff` ' s is used as fallback. If that too is not available, a default layout with 4 windows will be used. To configure the layout, see the _BACKEND SPECIFIC HINTS_ section. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolhideResolved)`mergetool.hideResolved` 
    
During a merge, Git will automatically resolve as many conflicts as possible and write the `$MERGED` file containing conflict markers around any conflicts that it cannot resolve; `$LOCAL` and `$REMOTE` normally are the versions of the file from before Git’s conflict resolution. This flag causes `$LOCAL` and `$REMOTE` to be overwritten so that only the unresolved conflicts are presented to the merge tool. Can be configured per-tool via the `mergetool.`_< tool>_`.hideResolved` configuration variable. Defaults to `false`. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolkeepBackup)`mergetool.keepBackup` 
    
After performing a merge, the original file with conflict markers can be saved as a file with a `.orig` extension. If this variable is set to `false` then this file is not preserved. Defaults to `true` (i.e. keep the backup files). 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolkeepTemporaries)`mergetool.keepTemporaries` 
    
When invoking a custom merge tool, Git uses a set of temporary files to pass to the tool. If the tool returns an error and this variable is set to `true`, then these temporary files will be preserved; otherwise, they will be removed after the tool has exited. Defaults to `false`. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolwriteToTemp)`mergetool.writeToTemp` 
    
Git writes temporary `BASE`, `LOCAL`, and `REMOTE` versions of conflicting files in the worktree by default. Git will attempt to use a temporary directory for these files when set `true`. Defaults to `false`. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolprompt)`mergetool.prompt` 
    
Prompt before each invocation of the merge resolution program. 

[](https://git-scm.com/docs/git-mergetool#Documentation/git-mergetool.txt-mergetoolguiDefault)`mergetool.guiDefault` 
    
Set `true` to use the `merge.guitool` by default (equivalent to specifying the `--gui` argument), or `auto` to select `merge.guitool` or `merge.tool` depending on the presence of a `DISPLAY` environment variable value. The default is `false`, where the `--gui` argument must be provided explicitly for the `merge.guitool` to be used.
##  [](https://git-scm.com/docs/git-mergetool#_temporary_files)TEMPORARY FILES
`git` `mergetool` creates `*.orig` backup files while resolving merges. These are safe to remove once a file has been merged and its `git` `mergetool` session has completed.
Setting the `mergetool.keepBackup` configuration variable to `false` causes `git` `mergetool` to automatically remove the backup files as files are successfully merged.
##  [](https://git-scm.com/docs/git-mergetool#_backend_specific_hints)BACKEND SPECIFIC HINTS
###  [](https://git-scm.com/docs/git-mergetool#_vimdiff)vimdiff
####  [](https://git-scm.com/docs/git-mergetool#_description_2)Description
When specifying `--tool=vimdiff` in `git` `mergetool` Git will open Vim with a 4 windows layout distributed in the following way:
```
------------------------------------------
|             |           |              |
|   LOCAL     |   BASE    |   REMOTE     |
|             |           |              |
------------------------------------------
|                                        |
|                MERGED                  |
|                                        |
------------------------------------------
```

`LOCAL`, `BASE` and `REMOTE` are read-only buffers showing the contents of the conflicting file in specific commits ("commit you are merging into", "common ancestor commit" and "commit you are merging from" respectively)
`MERGED` is a writable buffer where you have to resolve the conflicts (using the other read-only buffers as a reference). Once you are done, save and exit Vim as usual (`:wq`) or, if you want to abort, exit using `:cq`.
####  [](https://git-scm.com/docs/git-mergetool#_layout_configuration)Layout configuration
You can change the windows layout used by Vim by setting configuration variable `mergetool.vimdiff.layout` which accepts a string where the following separators have special meaning:
  * `+` is used to "open a new tab"
  * `,` is used to "open a new vertical split"
  * `/` is used to "open a new horizontal split"
  * `@` is used to indicate the file containing the final version after solving the conflicts. If not present, `MERGED` will be used by default.


The precedence of the operators is as follows (you can use parentheses to change it):
```
`@` > `+` > `/` > `,`
```

Let’s see some examples to understand how it works:
  * `layout` `=` `"`(`LOCAL,BASE,REMOTE`)`/MERGED"`
This is exactly the same as the default layout we have already seen.
Note that `/` has precedence over `,` and thus the parenthesis are not needed in this case. The next layout definition is equivalent:
```
layout = "LOCAL,BASE,REMOTE / MERGED"
```

  * `layout` `=` `"LOCAL,MERGED,REMOTE"`
If, for some reason, we are not interested in the `BASE` buffer.
```
------------------------------------------
|             |           |              |
|             |           |              |
|   LOCAL     |   MERGED  |   REMOTE     |
|             |           |              |
|             |           |              |
------------------------------------------
```

  * `layout` `=` `"MERGED"`
Only the `MERGED` buffer will be shown. Note, however, that all the other ones are still loaded in vim, and you can access them with the "buffers" command.
```
------------------------------------------
|                                        |
|                                        |
|                 MERGED                 |
|                                        |
|                                        |
------------------------------------------
```

  * `layout` `=` `"@LOCAL,REMOTE"`
When `MERGED` is not present in the layout, you must "mark" one of the buffers with an arobase (`@`). That will become the buffer you need to edit and save after resolving the conflicts.
```
------------------------------------------
|                   |                    |
|                   |                    |
|                   |                    |
|     LOCAL         |    REMOTE          |
|                   |                    |
|                   |                    |
|                   |                    |
------------------------------------------
```

  * `layout` `=` `"LOCAL,BASE,REMOTE` `/` `MERGED` `+` `BASE,LOCAL` `+` `BASE,REMOTE"`
Three tabs will open: the first one is a copy of the default layout, while the other two only show the differences between (`BASE` and `LOCAL`) and (`BASE` and `REMOTE`) respectively.
```
------------------------------------------
| <TAB #1> |  TAB #2  |  TAB #3  |       |
------------------------------------------
|             |           |              |
|   LOCAL     |   BASE    |   REMOTE     |
|             |           |              |
------------------------------------------
|                                        |
|                MERGED                  |
|                                        |
------------------------------------------
```

```
------------------------------------------
|  TAB #1  | <TAB #2> |  TAB #3  |       |
------------------------------------------
|                   |                    |
|                   |                    |
|                   |                    |
|     BASE          |    LOCAL           |
|                   |                    |
|                   |                    |
|                   |                    |
------------------------------------------
```

```
------------------------------------------
|  TAB #1  |  TAB #2  | <TAB #3> |       |
------------------------------------------
|                   |                    |
|                   |                    |
|                   |                    |
|     BASE          |    REMOTE          |
|                   |                    |
|                   |                    |
|                   |                    |
------------------------------------------
```

  * `layout` `=` `"LOCAL,BASE,REMOTE` `/` `MERGED` `+` `BASE,LOCAL` `+` `BASE,REMOTE` `+` (`LOCAL/BASE/REMOTE`)`,MERGED"`
Same as the previous example, but adds a fourth tab with the same information as the first tab, with a different layout.
```
---------------------------------------------
|  TAB #1  |  TAB #2  |  TAB #3  | <TAB #4> |
---------------------------------------------
|       LOCAL         |                     |
|---------------------|                     |
|       BASE          |        MERGED       |
|---------------------|                     |
|       REMOTE        |                     |
---------------------------------------------
```

Note how in the third tab definition we need to use parentheses to make `,` have precedence over `/`.


####  [](https://git-scm.com/docs/git-mergetool#_variants)Variants
Instead of `--tool=vimdiff`, you can also use one of these other variants:
  * `--tool=gvimdiff`, to open gVim instead of Vim.
  * `--tool=nvimdiff`, to open Neovim instead of Vim.


When using these variants, in order to specify a custom layout you will have to set configuration variables `mergetool.gvimdiff.layout` and `mergetool.nvimdiff.layout` instead of `mergetool.vimdiff.layout` (though the latter will be used as fallback if the variant-specific one is not set).
In addition, for backwards compatibility with previous Git versions, you can also append `1`, `2` or `3` to either `vimdiff` or any of the variants (ex: `vimdiff3`, `nvimdiff1`, etc…​) to use a predefined layout. In other words, using `--tool=`[`g`|`n`]`vimdiff`_< x>_ is the same as using `--tool=`[`g`|`n`]`vimdiff` and setting configuration variable `mergetool.`[`g`|`n`]`vimdiff.layout` to…​
  * _< x>_`=1`: `"@LOCAL,` `REMOTE"`
  * _< x>_`=2`: `"LOCAL,` `MERGED,` `REMOTE"`
  * _< x>_`=3`: `"MERGED"`


Example: using `--tool=gvimdiff2` will open `gvim` with three columns (`LOCAL`, `MERGED` and `REMOTE`).
##  [](https://git-scm.com/docs/git-mergetool#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### mergetool
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
