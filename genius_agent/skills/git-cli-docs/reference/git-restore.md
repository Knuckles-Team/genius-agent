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
    * [NAME](https://git-scm.com/docs/git-restore#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-restore#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-restore#_description)
    * [OPTIONS](https://git-scm.com/docs/git-restore#_options)
    * [EXAMPLES](https://git-scm.com/docs/git-restore#_examples)
    * [SEE ALSO](https://git-scm.com/docs/git-restore#_see_also)
    * [GIT](https://git-scm.com/docs/git-restore#_git)


[ English ▾](https://git-scm.com/docs/git-restore)
Localized versions of **git-restore** manual
  1. [English ](https://git-scm.com/docs/git-restore)
  2. [Deutsch ](https://git-scm.com/docs/git-restore/de)
  3. [Español ](https://git-scm.com/docs/git-restore/es)
  4. [Français ](https://git-scm.com/docs/git-restore/fr)
  5. [Português (Brasil) ](https://git-scm.com/docs/git-restore/pt_BR)
  6. [українська мова ](https://git-scm.com/docs/git-restore/uk)
  7. [简体中文 ](https://git-scm.com/docs/git-restore/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-restore)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-restore) git-restore last updated in 2.51.0
Changes in the **git-restore** manual
  1. 2.51.1 → 2.53.0 no changes
  2. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/git-restore/2.51.0)
  3. 2.50.1 no changes
  4. 2.50.0 no changes
  5. 2.49.1 no changes
  6. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-restore/2.49.0)
  7. 2.43.1 → 2.48.2 no changes
  8. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-restore/2.43.0)
  9. 2.35.1 → 2.42.4 no changes
  10. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-restore/2.35.0)
  11. 2.30.1 → 2.34.8 no changes
  12. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-restore/2.30.0)
  13. 2.27.1 → 2.29.3 no changes
  14. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-restore/2.27.0)
  15. 2.25.1 → 2.26.3 no changes
  16. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-restore/2.25.0)
  17. 2.23.1 → 2.24.4 no changes
  18. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-restore/2.23.0)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-restore#_name)NAME
git-restore - Restore working tree files
##  [](https://git-scm.com/docs/git-restore#_synopsis)SYNOPSIS
```
git restore [_<options>_] [--source=_<tree>_] [--staged] [--worktree] [--] _<pathspec>_…​
git restore [_<options>_] [--source=_<tree>_] [--staged] [--worktree] --pathspec-from-file=_<file>_ [--pathspec-file-nul]
git restore (-p|--patch) [_<options>_] [--source=_<tree>_] [--staged] [--worktree] [--] [_<pathspec>_…​]
```

##  [](https://git-scm.com/docs/git-restore#_description)DESCRIPTION
Restore specified paths in the working tree with some contents from a restore source. If a path is tracked but does not exist in the restore source, it will be removed to match the source.
The command can also be used to restore the content in the index with `--staged`, or restore both the working tree and the index with `--staged` `--worktree`.
By default, if `--staged` is given, the contents are restored from `HEAD`, otherwise from the index. Use `--source` to restore from a different commit.
See "Reset, restore and revert" in [git[1]](https://git-scm.com/docs/git) for the differences between the three commands.
##  [](https://git-scm.com/docs/git-restore#_options)OPTIONS 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt--stree)`-s` _< tree>_ 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---sourcetree)`--source=`_< tree>_ 
    
Restore the working tree files with the content from the given tree. It is common to specify the source tree by naming a commit, branch or tag associated with it.
If not specified, the contents are restored from `HEAD` if `--staged` is given, otherwise from the index.
As a special case, you may use `"`_< rev-A>_`...`_< rev-B>_`"` as a shortcut for the merge base of _< rev-A>_ and _< rev-B>_ if there is exactly one merge base. You can leave out at most one of _< rev-A>__ and _< rev-B>_, in which case it defaults to `HEAD`. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt--p)`-p` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---patch)`--patch` 
    
Interactively select hunks in the difference between the restore source and the restore location. See the "Interactive Mode" section of [git-add[1]](https://git-scm.com/docs/git-add) to learn how to operate the `--patch` mode. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt--Un)`-U`_< n>_ 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---unifiedn)`--unified=`_< n>_ 
    
Generate diffs with _< n>_ lines of context. Defaults to `diff.context` or 3 if the config option is unset. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---inter-hunk-contextn)`--inter-hunk-context=`_< n>_ 
    
Show the context between diff hunks, up to the specified _< number>_ of lines, thereby fusing hunks that are close to each other. Defaults to `diff.interHunkContext` or 0 if the config option is unset. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt--W)`-W` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---worktree)`--worktree` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt--S)`-S` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---staged)`--staged` 
    
Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying `--staged` will only restore the index. Specifying both restores both. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt--q)`-q` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---quiet)`--quiet` 
    
Quiet, suppress feedback messages. Implies `--no-progress`. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---progress)`--progress` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---no-progress)`--no-progress` 
    
Progress status is reported on the standard error stream by default when it is attached to a terminal, unless `--quiet` is specified. This flag enables progress reporting even if not attached to a terminal, regardless of `--quiet`. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---ours)`--ours` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---theirs)`--theirs` 
    
When restoring files in the working tree from the index, use stage #2 (`ours`) or #3 (`theirs`) for unmerged paths. This option cannot be used when checking out paths from a tree-ish (i.e. with the `--source` option).
Note that during `git` `rebase` and `git` `pull` `--rebase`, `ours` and `theirs` may appear swapped. See the explanation of the same options in [git-checkout[1]](https://git-scm.com/docs/git-checkout) for details. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt--m)`-m` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---merge)`--merge` 
    
When restoring files on the working tree from the index, recreate the conflicted merge in the unmerged paths. This option cannot be used when checking out paths from a tree-ish (i.e. with the `--source` option). 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---conflictstyle)`--conflict=`_< style>_ 
    
The same as `--merge` option above, but changes the way the conflicting hunks are presented, overriding the `merge.conflictStyle` configuration variable. Possible values are `merge` (default), `diff3`, and `zdiff3`. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---ignore-unmerged)`--ignore-unmerged` 
    
When restoring files on the working tree from the index, do not abort the operation if there are unmerged entries and neither `--ours`, `--theirs`, `--merge` or `--conflict` is specified. Unmerged paths on the working tree are left alone. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---ignore-skip-worktree-bits)`--ignore-skip-worktree-bits` 
    
In sparse checkout mode, the default is to only update entries matched by _< pathspec>_ and sparse patterns in `$GIT_DIR/info/sparse-checkout`. This option ignores the sparse patterns and unconditionally restores any files in _< pathspec>_. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---recurse-submodules)`--recurse-submodules` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---no-recurse-submodules)`--no-recurse-submodules` 
    
If _< pathspec>_ names an active submodule and the restore location includes the working tree, the submodule will only be updated if this option is given, in which case its working tree will be restored to the commit recorded in the superproject, and any local modifications overwritten. If nothing (or `--no-recurse-submodules`) is used, submodules working trees will not be updated. Just like [git-checkout[1]](https://git-scm.com/docs/git-checkout), this will detach `HEAD` of the submodule. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---overlay)`--overlay` 


[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---no-overlay)`--no-overlay` 
    
In overlay mode, never remove files when restoring. In no-overlay mode, remove tracked files that do not appear in the _< tree>_ of `--source=`_< tree>_, to make them match _< tree>_ exactly. The default is no-overlay mode. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---pathspec-from-filefile)`--pathspec-from-file=`_< file>_ 
    
Pathspec is passed in _< file>_ instead of commandline args. If _< file>_ is exactly `-` then standard input is used. Pathspec elements are separated by _LF_ or _CR_ /_LF_. Pathspec elements can be quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). See also `--pathspec-file-nul` and global `--literal-pathspecs`. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---pathspec-file-nul)`--pathspec-file-nul` 
    
Only meaningful with `--pathspec-from-file`. Pathspec elements are separated with _NUL_ character and all other characters are taken literally (including newlines and quotes). 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt---)`--` 
    
Do not interpret any more arguments as options. 

[](https://git-scm.com/docs/git-restore#Documentation/git-restore.txt-pathspec)_< pathspec>_... 
    
Limits the paths affected by the operation.
For more details, see the _pathspec_ entry in [gitglossary[7]](https://git-scm.com/docs/gitglossary).
##  [](https://git-scm.com/docs/git-restore#_examples)EXAMPLES
The following sequence switches to the `master` branch, reverts the `Makefile` to two revisions back, deletes `hello.c` by mistake, and gets it back from the index.
```
$ git switch master
$ git restore --source master~2 Makefile  **(1)**
$ rm -f hello.c
$ git restore hello.c                     **(2)**
```

  1. take a file out of another commit
  2. restore `hello.c` from the index


If you want to restore _all_ C source files to match the version in the index, you can say
```
$ git restore '*.c'
```

Note the quotes around `*.c`. The file `hello.c` will also be restored, even though it is no longer in the working tree, because the file globbing is used to match entries in the index (not in the working tree by the shell).
To restore all files in the current directory
```
$ git restore .
```

or to restore all working tree files with _top_ pathspec magic (see [gitglossary[7]](https://git-scm.com/docs/gitglossary))
```
$ git restore :/
```

To restore a file in the index to match the version in `HEAD` (this is the same as using [git-reset[1]](https://git-scm.com/docs/git-reset))
```
$ git restore --staged hello.c
```

or you can restore both the index and the working tree (this is the same as using [git-checkout[1]](https://git-scm.com/docs/git-checkout))
```
$ git restore --source=HEAD --staged --worktree hello.c
```

or the short form which is more practical but less readable:
```
$ git restore -s@ -SW hello.c
```

##  [](https://git-scm.com/docs/git-restore#_see_also)SEE ALSO
[git-checkout[1]](https://git-scm.com/docs/git-checkout), [git-reset[1]](https://git-scm.com/docs/git-reset)
##  [](https://git-scm.com/docs/git-restore#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### restore
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
