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
    * [NAME](https://git-scm.com/docs/git-apply#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-apply#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-apply#_description)
    * [OPTIONS](https://git-scm.com/docs/git-apply#_options)
    * [CONFIGURATION](https://git-scm.com/docs/git-apply#_configuration)
    * [SUBMODULES](https://git-scm.com/docs/git-apply#_submodules)
    * [SEE ALSO](https://git-scm.com/docs/git-apply#_see_also)
    * [GIT](https://git-scm.com/docs/git-apply#_git)


[ English ▾](https://git-scm.com/docs/git-apply)
Localized versions of **git-apply** manual
  1. [English ](https://git-scm.com/docs/git-apply)
  2. [Français ](https://git-scm.com/docs/git-apply/fr)
  3. [日本語 ](https://git-scm.com/docs/git-apply/ja)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-apply/pt_BR)
  5. [Svenska ](https://git-scm.com/docs/git-apply/sv)
  6. [українська мова ](https://git-scm.com/docs/git-apply/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-apply/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-apply)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-apply) git-apply last updated in 2.51.0
Changes in the **git-apply** manual
  1. 2.51.1 → 2.53.0 no changes
  2. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-apply/2.51.0)
  3. 2.47.1 → 2.50.1 no changes
  4. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git-apply/2.47.0)
  5. 2.43.1 → 2.46.4 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-apply/2.43.0)
  7. 2.40.1 → 2.42.4 no changes
  8. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-apply/2.40.0)
  9. 2.38.1 → 2.39.5 no changes
  10. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-apply/2.38.0)
  11. 2.35.1 → 2.37.7 no changes
  12. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-apply/2.35.0)
  13. 2.32.1 → 2.34.8 no changes
  14. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-apply/2.32.0)
  15. 2.29.1 → 2.31.8 no changes
  16. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-apply/2.29.0)
  17. 2.19.1 → 2.28.1 no changes
  18. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-apply/2.19.0)
  19. 2.18.1 → 2.18.5 no changes
  20. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-apply/2.18.0)
  21. 2.16.6 → 2.17.6 no changes
  22. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-apply/2.15.4)
  23. 2.14.6 no changes
  24. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-apply/2.13.7)
  25. 2.9.5 → 2.12.5 no changes
  26. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-apply/2.8.6)
  27. 2.5.6 → 2.7.6 no changes
  28. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-apply/2.4.12)
  29. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git-apply/2.3.10)
  30. 2.1.4 → 2.2.3 no changes
  31. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-apply/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-apply#_name)NAME
git-apply - Apply a patch to files and/or to the index
##  [](https://git-scm.com/docs/git-apply#_synopsis)SYNOPSIS
```
_git apply_ [--stat] [--numstat] [--summary] [--check]
	  [--index | --intent-to-add] [--3way] [--ours | --theirs | --union]
	  [--apply] [--no-add] [--build-fake-ancestor=<file>] [-R | --reverse]
	  [--allow-binary-replacement | --binary] [--reject] [-z]
	  [-p<n>] [-C<n>] [--inaccurate-eof] [--recount] [--cached]
	  [--ignore-space-change | --ignore-whitespace]
	  [--whitespace=(nowarn|warn|fix|error|error-all)]
	  [--exclude=<path>] [--include=<path>] [--directory=<root>]
	  [--verbose | --quiet] [--unsafe-paths] [--allow-empty] [<patch>…​]
```

##  [](https://git-scm.com/docs/git-apply#_description)DESCRIPTION
Reads the supplied diff output (i.e. "a patch") and applies it to files. When running from a subdirectory in a repository, patched paths outside the directory are ignored. With the `--index` option, the patch is also applied to the index, and with the `--cached` option, the patch is only applied to the index. Without these options, the command applies the patch only to files, and does not require them to be in a Git repository.
This command applies the patch but does not create a commit. Use [git-am[1]](https://git-scm.com/docs/git-am) to create commits from patches generated by [git-format-patch[1]](https://git-scm.com/docs/git-format-patch) and/or received by email.
##  [](https://git-scm.com/docs/git-apply#_options)OPTIONS 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt-patch)<patch>…​ 
    
The files to read the patch from. _-_ can be used to read from the standard input. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---stat)--stat 
    
Instead of applying the patch, output diffstat for the input. Turns off "apply". 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---numstat)--numstat 
    
Similar to `--stat`, but shows the number of added and deleted lines in decimal notation and the pathname without abbreviation, to make it more machine friendly. For binary files, outputs two `-` instead of saying `0` `0`. Turns off "apply". 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---summary)--summary 
    
Instead of applying the patch, output a condensed summary of information obtained from git diff extended headers, such as creations, renames, and mode changes. Turns off "apply". 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---check)--check 
    
Instead of applying the patch, see if the patch is applicable to the current working tree and/or the index file and detects errors. Turns off "apply". 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---index)--index 
    
Apply the patch to both the index and the working tree (or merely check that it would apply cleanly to both if `--check` is in effect). Note that `--index` expects index entries and working tree copies for relevant paths to be identical (their contents and metadata such as file mode must match), and will raise an error if they are not, even if the patch would apply cleanly to both the index and the working tree in isolation. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---cached)--cached 
    
Apply the patch to just the index, without touching the working tree. If `--check` is in effect, merely check that it would apply cleanly to the index entry. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--N)-N 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---intent-to-add)--intent-to-add 
    
When applying the patch only to the working tree, mark new files to be added to the index later (see `--intent-to-add` option in [git-add[1]](https://git-scm.com/docs/git-add)). This option is ignored if `--index` or `--cached` are used, and has no effect outside a Git repository. Note that `--index` could be implied by other options such as `--3way`. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--3)-3 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---3way)--3way 
    
Attempt 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally, possibly leaving the conflict markers in the files in the working tree for the user to resolve. This option implies the `--index` option unless the `--cached` option is used, and is incompatible with the `--reject` option. When used with the `--cached` option, any conflicts are left at higher stages in the cache. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---ours)--ours 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---theirs)--theirs 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---union)--union 
    
Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines. Requires --3way. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---build-fake-ancestorfile)--build-fake-ancestor=<file> 
    
Newer _git diff_ output has embedded _index information_ for each blob to help identify the original version that the patch applies to. When this flag is given, and if the original versions of the blobs are available locally, builds a temporary index containing those blobs.
When a pure mode change is encountered (which has no index information), the information is read from the current index instead. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--R)-R 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---reverse)--reverse 
    
Apply the patch in reverse. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---reject)--reject 
    
For atomicity, _git apply_ by default fails the whole patch and does not touch the working tree when some of the hunks do not apply. This option makes it apply the parts of the patch that are applicable, and leave the rejected hunks in corresponding *.rej files. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--z)-z 
    
When `--numstat` has been given, do not munge pathnames, but use a NUL-terminated machine-readable format.
Without this option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--pn)-p<n> 
    
Remove <n> leading path components (separated by slashes) from traditional diff paths. E.g., with `-p2`, a patch against `a/dir/file` will be applied directly to `file`. The default is 1. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--Cn)-C<n> 
    
Ensure at least <n> lines of surrounding context match before and after each change. When fewer lines of surrounding context exist they all must match. By default no context is ever ignored. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---unidiff-zero)--unidiff-zero 
    
By default, _git apply_ expects that the patch being applied is a unified diff with at least one line of context. This provides good safety measures, but breaks down when applying a diff generated with `--unified=0`. To bypass these checks use `--unidiff-zero`.
Note, for the reasons stated above, the usage of context-free patches is discouraged. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---apply)--apply 
    
If you use any of the options marked "Turns off _apply_ " above, _git apply_ reads and outputs the requested information without actually applying the patch. Give this flag after those flags to also apply the patch. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---no-add)--no-add 
    
When applying a patch, ignore additions made by the patch. This can be used to extract the common part between two files by first running _diff_ on them and applying the result with this option, which would apply the deletion part but not the addition part. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---allow-binary-replacement)--allow-binary-replacement 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---binary)--binary 
    
Historically we did not allow binary patch application without an explicit permission from the user, and this flag was the way to do so. Currently, we always allow binary patch application, so this is a no-op. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---excludepath-pattern)--exclude=<path-pattern> 
    
Don’t apply changes to files matching the given path pattern. This can be useful when importing patchsets, where you want to exclude certain files or directories. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---includepath-pattern)--include=<path-pattern> 
    
Apply changes to files matching the given path pattern. This can be useful when importing patchsets, where you want to include certain files or directories.
When `--exclude` and `--include` patterns are used, they are examined in the order they appear on the command line, and the first match determines if a patch to each path is used. A patch to a path that does not match any include/exclude pattern is used by default if there is no include pattern on the command line, and ignored if there is any include pattern. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---ignore-space-change)--ignore-space-change 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---ignore-whitespace)--ignore-whitespace 
    
When applying a patch, ignore changes in whitespace in context lines if necessary. Context lines will preserve their whitespace, and they will not undergo whitespace fixing regardless of the value of the `--whitespace` option. New lines will still be fixed, though. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---whitespaceaction)--whitespace=<action> 
    
When applying a patch, detect a new or modified line that has whitespace errors. What are considered whitespace errors is controlled by `core.whitespace` configuration. By default, trailing whitespaces (including lines that solely consist of whitespaces) and a space character that is immediately followed by a tab character inside the initial indent of the line are considered whitespace errors.
By default, the command outputs warning messages but applies the patch. When `git-apply` is used for statistics and not applying a patch, it defaults to `nowarn`.
You can use different _< action>_ values to control this behavior:
  * `nowarn` turns off the trailing whitespace warning.
  * `warn` outputs warnings for a few such errors, but applies the patch as-is (default).
  * `fix` outputs warnings for a few such errors, and applies the patch after fixing them (`strip` is a synonym — the tool used to consider only trailing whitespace characters as errors, and the fix involved _stripping_ them, but modern Gits do more).
  * `error` outputs warnings for a few such errors, and refuses to apply the patch.
  * `error-all` is similar to `error` but shows all errors.



[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---inaccurate-eof)--inaccurate-eof 
    
Under certain circumstances, some versions of _diff_ do not correctly detect a missing new-line at the end of the file. As a result, patches created by such _diff_ programs do not record incomplete lines correctly. This option adds support for applying such patches by working around this bug. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--v)-v 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---verbose)--verbose 
    
Report progress to stderr. By default, only a message about the current patch being applied will be printed. This option will cause additional information to be reported. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt--q)-q 


[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---quiet)--quiet 
    
Suppress stderr output. Messages about patch status and progress will not be printed. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---recount)--recount 
    
Do not trust the line counts in the hunk headers, but infer them by inspecting the patch (e.g. after editing the patch without adjusting the hunk headers appropriately). 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---directoryroot)--directory=<root> 
    
Prepend <root> to all filenames. If a "-p" argument was also passed, it is applied before prepending the new root.
For example, a patch that talks about updating `a/git-gui.sh` to `b/git-gui.sh` can be applied to the file in the working tree `modules/git-gui/git-gui.sh` by running `git` `apply` `--directory=modules/git-gui`. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---unsafe-paths)--unsafe-paths 
    
By default, a patch that affects outside the working area (either a Git controlled working tree, or the current working directory when "git apply" is used as a replacement of GNU patch) is rejected as a mistake (or a mischief).
When `git` `apply` is used as a "better GNU patch", the user can pass the `--unsafe-paths` option to override this safety check. This option has no effect when `--index` or `--cached` is in use. 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt---allow-empty)--allow-empty 
    
Don’t return an error for patches containing no diff. This includes empty patches and patches with commit text only.
##  [](https://git-scm.com/docs/git-apply#_configuration)CONFIGURATION
Everything below this line in this section is selectively included from the [git-config[1]](https://git-scm.com/docs/git-config) documentation. The content is the same as what’s found there: 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt-applyignoreWhitespace)apply.ignoreWhitespace 
    
When set to _change_ , tells _git apply_ to ignore changes in whitespace, in the same way as the `--ignore-space-change` option. When set to one of: no, none, never, false, it tells _git apply_ to respect all whitespace differences. See [git-apply[1]](https://git-scm.com/docs/git-apply). 

[](https://git-scm.com/docs/git-apply#Documentation/git-apply.txt-applywhitespace)apply.whitespace 
    
Tells _git apply_ how to handle whitespace, in the same way as the `--whitespace` option. See [git-apply[1]](https://git-scm.com/docs/git-apply).
##  [](https://git-scm.com/docs/git-apply#_submodules)SUBMODULES
If the patch contains any changes to submodules then _git apply_ treats these changes as follows.
If `--index` is specified (explicitly or implicitly), then the submodule commits must match the index exactly for the patch to apply. If any of the submodules are checked-out, then these check-outs are completely ignored, i.e., they are not required to be up to date or clean and they are not updated.
If `--index` is not specified, then the submodule commits in the patch are ignored and only the absence or presence of the corresponding subdirectory is checked and (if possible) updated.
##  [](https://git-scm.com/docs/git-apply#_see_also)SEE ALSO
[git-am[1]](https://git-scm.com/docs/git-am).
##  [](https://git-scm.com/docs/git-apply#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### apply
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
