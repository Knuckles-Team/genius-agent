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
    * [NAME](https://git-scm.com/docs/git-ls-tree#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-ls-tree#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-ls-tree#_description)
    * [OPTIONS](https://git-scm.com/docs/git-ls-tree#_options)
    * [Output Format](https://git-scm.com/docs/git-ls-tree#_output_format)
    * [FIELD NAMES](https://git-scm.com/docs/git-ls-tree#_field_names)
    * [GIT](https://git-scm.com/docs/git-ls-tree#_git)


[ English ▾](https://git-scm.com/docs/git-ls-tree)
Localized versions of **git-ls-tree** manual
  1. [English ](https://git-scm.com/docs/git-ls-tree)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-ls-tree/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-ls-tree/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-ls-tree/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-ls-tree)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-ls-tree) git-ls-tree last updated in 2.42.0
Changes in the **git-ls-tree** manual
  1. 2.42.1 → 2.53.0 no changes
  2. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-ls-tree/2.42.0)
  3. 2.36.1 → 2.41.3 no changes
  4. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-ls-tree/2.36.0)
  5. 2.30.1 → 2.35.8 no changes
  6. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-ls-tree/2.30.0)
  7. 2.22.1 → 2.29.3 no changes
  8. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-ls-tree/2.22.0)
  9. 2.14.6 → 2.21.4 no changes
  10. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-ls-tree/2.13.7)
  11. 2.10.5 → 2.12.5 no changes
  12. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-ls-tree/2.9.5)
  13. 2.1.4 → 2.8.6 no changes
  14. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-ls-tree/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-ls-tree#_name)NAME
git-ls-tree - List the contents of a tree object
##  [](https://git-scm.com/docs/git-ls-tree#_synopsis)SYNOPSIS
```
_git ls-tree_ [-d] [-r] [-t] [-l] [-z]
	    [--name-only] [--name-status] [--object-only] [--full-name] [--full-tree] [--abbrev[=<n>]] [--format=<format>]
	    <tree-ish> [<path>…​]
```

##  [](https://git-scm.com/docs/git-ls-tree#_description)DESCRIPTION
Lists the contents of a given tree object, like what "/bin/ls -a" does in the current working directory. Note that:
  * the behaviour is slightly different from that of "/bin/ls" in that the _< path>_ denotes just a list of patterns to match, e.g. so specifying directory name (without `-r`) will behave differently, and order of the arguments does not matter.
  * the behaviour is similar to that of "/bin/ls" in that the _< path>_ is taken as relative to the current working directory. E.g. when you are in a directory _sub_ that has a directory _dir_ , you can run _git ls-tree -r HEAD dir_ to list the contents of the tree (that is `sub/dir` in `HEAD`). You don’t want to give a tree that is not at the root level (e.g. `git` `ls-tree` `-r` `HEAD:sub` `dir`) in this case, as that would result in asking for `sub/sub/dir` in the `HEAD` commit. However, the current working directory can be ignored by passing --full-tree option.


##  [](https://git-scm.com/docs/git-ls-tree#_options)OPTIONS 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt-tree-ish)<tree-ish> 
    
Id of a tree-ish. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt--d)-d 
    
Show only the named tree entry itself, not its children. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt--r)-r 
    
Recurse into sub-trees. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt--t)-t 
    
Show tree entries even when going to recurse them. Has no effect if `-r` was not passed. `-d` implies `-t`. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt--l)-l 


[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---long)--long 
    
Show object size of blob (file) entries. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt--z)-z 
    
\0 line termination on output and do not quote filenames. See OUTPUT FORMAT below for more information. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---name-only)--name-only 


[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---name-status)--name-status 
    
List only filenames (instead of the "long" output), one per line. Cannot be combined with `--object-only`. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---object-only)--object-only 
    
List only names of the objects, one per line. Cannot be combined with `--name-only` or `--name-status`. This is equivalent to specifying `--format='%`(`objectname`), but for both this option and that exact format the command takes a hand-optimized codepath instead of going through the generic formatting mechanism. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---abbrevn)--abbrev[=<n>] 
    
Instead of showing the full 40-byte hexadecimal object lines, show the shortest prefix that is at least _< n>_ hexdigits long that uniquely refers the object. Non default number of digits can be specified with --abbrev=<n>. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---full-name)--full-name 
    
Instead of showing the path names relative to the current working directory, show the full path names. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---full-tree)--full-tree 
    
Do not limit the listing to the current working directory. Implies --full-name. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt---formatformat)--format=<format> 
    
A string that interpolates `%`(`fieldname`) from the result being shown. It also interpolates `%%` to `%`, and `%xNN` where `NN` are hex digits interpolates to character with hex code `NN`; for example `%x00` interpolates to _\0_ (NUL), `%x09` to _\t_ (TAB) and `%x0a` to _\n_ (LF). When specified, `--format` cannot be combined with other format-altering options, including `--long`, `--name-only` and `--object-only`. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt-path)[<path>…​] 
    
When paths are given, show them (note that this isn’t really raw pathnames, but rather a list of patterns to match). Otherwise implicitly uses the root level of the tree as the sole path argument.
##  [](https://git-scm.com/docs/git-ls-tree#_output_format)Output Format
The output format of `ls-tree` is determined by either the `--format` option, or other format-altering options such as `--name-only` etc. (see `--format` above).
The use of certain `--format` directives is equivalent to using those options, but invoking the full formatting machinery can be slower than using an appropriate formatting option.
In cases where the `--format` would exactly map to an existing option `ls-tree` will use the appropriate faster path. Thus the default format is equivalent to:
```
%(objectmode) %(objecttype) %(objectname)%x09%(path)
```

This output format is compatible with what `--index-info` `--stdin` of _git update-index_ expects.
When the `-l` option is used, format changes to
```
%(objectmode) %(objecttype) %(objectname) %(objectsize:padded)%x09%(path)
```

Object size identified by <objectname> is given in bytes, and right-justified with minimum width of 7 characters. Object size is given only for blobs (file) entries; for other entries `-` character is used in place of size.
Without the `-z` option, pathnames with "unusual" characters are quoted as explained for the configuration variable `core.quotePath` (see [git-config[1]](https://git-scm.com/docs/git-config)). Using `-z` the filename is output verbatim and the line is terminated by a NUL byte.
Customized format:
It is possible to print in a custom format by using the `--format` option, which is able to interpolate different fields using a `%`(`fieldname`) notation. For example, if you only care about the "objectname" and "path" fields, you can execute with a specific "--format" like
```
git ls-tree --format='%(objectname) %(path)' <tree-ish>
```

##  [](https://git-scm.com/docs/git-ls-tree#_field_names)FIELD NAMES
Various values from structured fields can be used to interpolate into the resulting output. For each outputting line, the following names can be used: 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt-objectmode)objectmode 
    
The mode of the object. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt-objecttype)objecttype 
    
The type of the object (`commit`, `blob` or `tree`). 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt-objectname)objectname 
    
The name of the object. 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt-objectsizepadded)objectsize[:padded] 
    
The size of a `blob` object ("-" if it’s a `commit` or `tree`). It also supports a padded format of size with "%(objectsize:padded)". 

[](https://git-scm.com/docs/git-ls-tree#Documentation/git-ls-tree.txt-path-1)path 
    
The pathname of the object.
##  [](https://git-scm.com/docs/git-ls-tree#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### ls-tree
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
