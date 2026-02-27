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
    * [NAME](https://git-scm.com/docs/git-merge-tree#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-merge-tree#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-merge-tree#NEWMERGE)
    * [OPTIONS](https://git-scm.com/docs/git-merge-tree#_options)
    * [OUTPUT](https://git-scm.com/docs/git-merge-tree#OUTPUT)
    * [EXIT STATUS](https://git-scm.com/docs/git-merge-tree#_exit_status)
    * [USAGE NOTES](https://git-scm.com/docs/git-merge-tree#_usage_notes)
    * [INPUT FORMAT](https://git-scm.com/docs/git-merge-tree#INPUT)
    * [MISTAKES TO AVOID](https://git-scm.com/docs/git-merge-tree#_mistakes_to_avoid)
    * [DEPRECATED DESCRIPTION](https://git-scm.com/docs/git-merge-tree#DEPMERGE)
    * [GIT](https://git-scm.com/docs/git-merge-tree#_git)


[ English ▾](https://git-scm.com/docs/git-merge-tree)
Localized versions of **git-merge-tree** manual
  1. [English ](https://git-scm.com/docs/git-merge-tree)
  2. [Français ](https://git-scm.com/docs/git-merge-tree/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-merge-tree/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-merge-tree/sv)
  5. [українська мова ](https://git-scm.com/docs/git-merge-tree/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-merge-tree/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-merge-tree)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-merge-tree) git-merge-tree last updated in 2.52.0
Changes in the **git-merge-tree** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-merge-tree/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git-merge-tree/2.51.1)
  5. 2.50.1 → 2.51.0 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-merge-tree/2.50.0)
  7. 2.49.1 no changes
  8. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-merge-tree/2.49.0)
  9. 2.47.2 → 2.48.2 no changes
  10. [2.47.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-25_ ](https://git-scm.com/docs/git-merge-tree/2.47.1)
  11. 2.45.4 → 2.47.0 no changes
  12. [2.45.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-26_ ](https://git-scm.com/docs/git-merge-tree/2.45.3)
  13. 2.45.1 → 2.45.2 no changes
  14. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-merge-tree/2.45.0)
  15. 2.43.1 → 2.44.4 no changes
  16. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-merge-tree/2.43.0)
  17. 2.41.1 → 2.42.4 no changes
  18. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-merge-tree/2.41.0)
  19. 2.40.1 → 2.40.4 no changes
  20. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-merge-tree/2.40.0)
  21. 2.39.1 → 2.39.5 no changes
  22. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-merge-tree/2.39.0)
  23. 2.38.1 → 2.38.5 no changes
  24. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-merge-tree/2.38.0)
  25. 2.1.4 → 2.37.7 no changes
  26. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-merge-tree/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-merge-tree#_name)NAME
git-merge-tree - Perform merge without touching index or working tree
##  [](https://git-scm.com/docs/git-merge-tree#_synopsis)SYNOPSIS
```
_git merge-tree_ [--write-tree] [<options>] <branch1> <branch2>
_git merge-tree_ [--trivial-merge] <base-tree> <branch1> <branch2> (deprecated)
```

##  [](https://git-scm.com/docs/git-merge-tree#NEWMERGE)DESCRIPTION
This command has a modern `--write-tree` mode and a deprecated `--trivial-merge` mode. With the exception of the [DEPRECATED DESCRIPTION](https://git-scm.com/docs/git-merge-tree#DEPMERGE) section at the end, the rest of this documentation describes the modern `--write-tree` mode.
Performs a merge, but does not make any new commits and does not read from or write to either the working tree or index.
The performed merge will use the same features as the "real" [git-merge[1]](https://git-scm.com/docs/git-merge), including:
  * three way content merges of individual files
  * rename detection
  * proper directory/file conflict handling
  * recursive ancestor consolidation (i.e. when there is more than one merge base, creating a virtual merge base by merging the merge bases)
  * etc.


After the merge completes, a new toplevel tree object is created. See `OUTPUT` below for details.
##  [](https://git-scm.com/docs/git-merge-tree#_options)OPTIONS 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---stdin)--stdin 
    
Read the commits to merge from the standard input rather than the command-line. See [INPUT FORMAT](https://git-scm.com/docs/git-merge-tree#INPUT) below for more information. Implies `-z`. 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt--z)-z 
    
Do not quote filenames in the <Conflicted file info> section, and end each filename with a NUL character rather than newline. Also begin the messages section with a NUL character instead of a newline. See [OUTPUT](https://git-scm.com/docs/git-merge-tree#OUTPUT) below for more information. 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---name-only)--name-only 
    
In the Conflicted file info section, instead of writing a list of (mode, oid, stage, path) tuples to output for conflicted files, just provide a list of filenames with conflicts (and do not list filenames multiple times if they have multiple conflicting stages). 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---messages)--messages 


[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---no-messages)--no-messages 
    
Write any informational messages such as "Auto-merging <path>" or CONFLICT notices to the end of stdout. If unspecified, the default is to include these messages if there are merge conflicts, and to omit them otherwise. 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---quiet)--quiet 
    
Disable all output from the program. Useful when you are only interested in the exit status. Allows merge-tree to exit early when it finds a conflict, and allows it to avoid writing most objects created by merges. 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---allow-unrelated-histories)--allow-unrelated-histories 
    
merge-tree will by default error out if the two branches specified share no common history. This flag can be given to override that check and make the merge proceed anyway. 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---merge-basetree-ish)--merge-base=<tree-ish> 
    
Instead of finding the merge-bases for <branch1> and <branch2>, specify a merge-base for the merge. This option is incompatible with `--stdin`.
Specifying multiple bases is currently not supported, which means that when merging two branches with more than one merge-base, using this option may cause merge results to differ from what `git` `merge` would compute. This can include potentially losing some changes made on one side of the history in the resulting merge.
With this option, since the merge-base is provided directly, <branch1> and <branch2> do not need to specify commits; trees are enough. 

[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt--Xoption)-X<option> 


[](https://git-scm.com/docs/git-merge-tree#Documentation/git-merge-tree.txt---strategy-optionoption)--strategy-option=<option> 
    
Pass the merge strategy-specific option through to the merge strategy. See [git-merge[1]](https://git-scm.com/docs/git-merge) for details.
##  [](https://git-scm.com/docs/git-merge-tree#OUTPUT)OUTPUT
For a successful merge, the output from git-merge-tree is simply one line:
```
<OID of toplevel tree>
```

Whereas for a conflicted merge, the output is by default of the form:
```
<OID of toplevel tree>
<Conflicted file info>
<Informational messages>
```

These are discussed individually below.
However, there is an exception. If `--stdin` is passed, then there is an extra section at the beginning, a NUL character at the end, and then all the sections repeat for each line of input. Thus, if the first merge is conflicted and the second is clean, the output would be of the form:
```
<Merge status>
<OID of toplevel tree>
<Conflicted file info>
<Informational messages>
NUL
<Merge status>
<OID of toplevel tree>
NUL
```

###  [](https://git-scm.com/docs/git-merge-tree#MS)Merge status
This is an integer status followed by a NUL character. The integer status is:
```
0: merge had conflicts
1: merge was clean
```

###  [](https://git-scm.com/docs/git-merge-tree#OIDTLT)OID of toplevel tree
This is a tree object that represents what would be checked out in the working tree at the end of `git` `merge`. If there were conflicts, then files within this tree may have embedded conflict markers. This section is always followed by a newline (or NUL if `-z` is passed).
###  [](https://git-scm.com/docs/git-merge-tree#CFI)Conflicted file info
This is a sequence of lines with the format
```
<mode> <object> <stage> <filename>
```

The filename will be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). However, if the `--name-only` option is passed, the mode, object, and stage will be omitted. If `-z` is passed, the "lines" are terminated by a NUL character instead of a newline character.
###  [](https://git-scm.com/docs/git-merge-tree#IM)Informational messages
This section provides informational messages, typically about conflicts. The format of the section varies significantly depending on whether `-z` is passed.
If `-z` is passed:
The output format is zero or more conflict informational records, each of the form:
```
<list-of-paths><conflict-type>NUL<conflict-message>NUL
```

where <list-of-paths> is of the form
```
<number-of-paths>NUL<path1>NUL<path2>NUL...<pathN>NUL
```

and includes paths (or branch names) affected by the conflict or informational message in <conflict-message>. Also, <conflict-type> is a stable string explaining the type of conflict, such as
  * "Auto-merging"
  * "CONFLICT (rename/delete)"
  * "CONFLICT (submodule lacks merge base)"
  * "CONFLICT (binary)"


and <conflict-message> is a more detailed message about the conflict which often (but not always) embeds the <stable-short-type-description> within it. These strings may change in future Git versions. Some examples:
  * "Auto-merging <file>"
  * "CONFLICT (rename/delete): <oldfile> renamed…​but deleted in…​"
  * "Failed to merge submodule <submodule> (no merge base)"
  * "Warning: cannot merge binary files: <filename>"


If `-z` is NOT passed:
This section starts with a blank line to separate it from the previous sections, and then only contains the <conflict-message> information from the previous section (separated by newlines). These are non-stable strings that should not be parsed by scripts, and are just meant for human consumption. Also, note that while <conflict-message> strings usually do not contain embedded newlines, they sometimes do. (However, the free-form messages will never have an embedded NUL character). So, the entire block of information is meant for human readers as an agglomeration of all conflict messages.
##  [](https://git-scm.com/docs/git-merge-tree#_exit_status)EXIT STATUS
For a successful, non-conflicted merge, the exit status is 0. When the merge has conflicts, the exit status is 1. If the merge is not able to complete (or start) due to some kind of error, the exit status is something other than 0 or 1 (and the output is unspecified). When --stdin is passed, the return status is 0 for both successful and conflicted merges, and something other than 0 or 1 if it cannot complete all the requested merges.
##  [](https://git-scm.com/docs/git-merge-tree#_usage_notes)USAGE NOTES
This command is intended as low-level plumbing, similar to [git-hash-object[1]](https://git-scm.com/docs/git-hash-object), [git-mktree[1]](https://git-scm.com/docs/git-mktree), [git-commit-tree[1]](https://git-scm.com/docs/git-commit-tree), [git-write-tree[1]](https://git-scm.com/docs/git-write-tree), [git-update-ref[1]](https://git-scm.com/docs/git-update-ref), and [git-mktag[1]](https://git-scm.com/docs/git-mktag). Thus, it can be used as a part of a series of steps such as:
```
vi message.txt
BRANCH1=refs/heads/test
BRANCH2=main
NEWTREE=$(git merge-tree --write-tree $BRANCH1 $BRANCH2) || {
    echo "There were conflicts..." 1>&2
    exit 1
}
NEWCOMMIT=$(git commit-tree $NEWTREE -F message.txt \
    -p $BRANCH1 -p $BRANCH2)
git update-ref $BRANCH1 $NEWCOMMIT
```

Note that when the exit status is non-zero, `NEWTREE` in this sequence will contain a lot more output than just a tree.
For conflicts, the output includes the same information that you’d get with [git-merge[1]](https://git-scm.com/docs/git-merge):
  * what would be written to the working tree (the [OID of toplevel tree](https://git-scm.com/docs/git-merge-tree#OIDTLT))
  * the higher order stages that would be written to the index (the [Conflicted file info](https://git-scm.com/docs/git-merge-tree#CFI))
  * any messages that would have been printed to stdout (the [Informational messages](https://git-scm.com/docs/git-merge-tree#IM))


##  [](https://git-scm.com/docs/git-merge-tree#INPUT)INPUT FORMAT
_git merge-tree --stdin_ input format is fully text based. Each line has this format:
```
[<base-commit> -- ]<branch1> <branch2>
```

If one line is separated by `--`, the string before the separator is used for specifying a merge-base for the merge and the string after the separator describes the branches to be merged.
##  [](https://git-scm.com/docs/git-merge-tree#_mistakes_to_avoid)MISTAKES TO AVOID
Do NOT look through the resulting toplevel tree to try to find which files conflict; parse the [Conflicted file info](https://git-scm.com/docs/git-merge-tree#CFI) section instead. Not only would parsing an entire tree be horrendously slow in large repositories, there are numerous types of conflicts not representable by conflict markers (modify/delete, mode conflict, binary file changed on both sides, file/directory conflicts, various rename conflict permutations, etc.)
Do NOT interpret an empty [Conflicted file info](https://git-scm.com/docs/git-merge-tree#CFI) list as a clean merge; check the exit status. A merge can have conflicts without having individual files conflict (there are a few types of directory rename conflicts that fall into this category, and others might also be added in the future).
Do NOT attempt to guess or make the user guess the conflict types from the [Conflicted file info](https://git-scm.com/docs/git-merge-tree#CFI) list. The information there is insufficient to do so. For example: Rename/rename(1to2) conflicts (both sides renamed the same file differently) will result in three different files having higher order stages (but each only has one higher order stage), with no way (short of the [Informational messages](https://git-scm.com/docs/git-merge-tree#IM) section) to determine which three files are related. File/directory conflicts also result in a file with exactly one higher order stage. Possibly-involved-in-directory-rename conflicts (when "merge.directoryRenames" is unset or set to "conflicts") also result in a file with exactly one higher order stage. In all cases, the [Informational messages](https://git-scm.com/docs/git-merge-tree#IM) section has the necessary info, though it is not designed to be machine parseable.
Do NOT assume that each path from [Conflicted file info](https://git-scm.com/docs/git-merge-tree#CFI), and the logical conflicts in the [Informational messages](https://git-scm.com/docs/git-merge-tree#IM) have a one-to-one mapping, nor that there is a one-to-many mapping, nor a many-to-one mapping. Many-to-many mappings exist, meaning that each path can have many logical conflict types in a single merge, and each logical conflict type can affect many paths.
Do NOT assume all filenames listed in the [Informational messages](https://git-scm.com/docs/git-merge-tree#IM) section had conflicts. Messages can be included for files that have no conflicts, such as "Auto-merging <file>".
AVOID taking the OIDS from the [Conflicted file info](https://git-scm.com/docs/git-merge-tree#CFI) and re-merging them to present the conflicts to the user. This will lose information. Instead, look up the version of the file found within the [OID of toplevel tree](https://git-scm.com/docs/git-merge-tree#OIDTLT) and show that instead. In particular, the latter will have conflict markers annotated with the original branch/commit being merged and, if renames were involved, the original filename. While you could include the original branch/commit in the conflict marker annotations when re-merging, the original filename is not available from the [Conflicted file info](https://git-scm.com/docs/git-merge-tree#CFI) and thus you would be losing information that might help the user resolve the conflict.
##  [](https://git-scm.com/docs/git-merge-tree#DEPMERGE)DEPRECATED DESCRIPTION
Per the [DESCRIPTION](https://git-scm.com/docs/git-merge-tree#NEWMERGE) and unlike the rest of this documentation, this section describes the deprecated `--trivial-merge` mode.
Other than the optional `--trivial-merge`, this mode accepts no options.
This mode reads three tree-ish, and outputs trivial merge results and conflicting stages to the standard output in a semi-diff format. Since this was designed for higher level scripts to consume and merge the results back into the index, it omits entries that match <branch1>. The result of this second form is similar to what three-way _git read-tree -m_ does, but instead of storing the results in the index, the command outputs the entries to the standard output.
This form not only has limited applicability (a trivial merge cannot handle content merges of individual files, rename detection, proper directory/file conflict handling, etc.), the output format is also difficult to work with, and it will generally be less performant than the first form even on successful merges (especially if working in large repositories).
##  [](https://git-scm.com/docs/git-merge-tree#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### merge-tree
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
