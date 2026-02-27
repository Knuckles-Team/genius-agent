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
    * [NAME](https://git-scm.com/docs/git-replace#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-replace#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-replace#_description)
    * [OPTIONS](https://git-scm.com/docs/git-replace#_options)
    * [FORMATS](https://git-scm.com/docs/git-replace#_formats)
    * [CREATING REPLACEMENT OBJECTS](https://git-scm.com/docs/git-replace#_creating_replacement_objects)
    * [BUGS](https://git-scm.com/docs/git-replace#_bugs)
    * [SEE ALSO](https://git-scm.com/docs/git-replace#_see_also)
    * [GIT](https://git-scm.com/docs/git-replace#_git)


[ English ▾](https://git-scm.com/docs/git-replace)
Localized versions of **git-replace** manual
  1. [English ](https://git-scm.com/docs/git-replace)
  2. [Français ](https://git-scm.com/docs/git-replace/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-replace/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-replace/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-replace/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-replace)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-replace) git-replace last updated in 2.44.0
Changes in the **git-replace** manual
  1. 2.44.1 → 2.53.0 no changes
  2. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git-replace/2.44.0)
  3. 2.43.1 → 2.43.7 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-replace/2.43.0)
  5. 2.24.1 → 2.42.4 no changes
  6. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-replace/2.24.0)
  7. 2.18.1 → 2.23.4 no changes
  8. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-replace/2.18.0)
  9. 2.10.5 → 2.17.6 no changes
  10. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-replace/2.9.5)
  11. 2.2.3 → 2.8.6 no changes
  12. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-replace/2.1.4)
  13. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-replace/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-replace#_name)NAME
git-replace - Create, list, delete refs to replace objects
##  [](https://git-scm.com/docs/git-replace#_synopsis)SYNOPSIS
```
_git replace_ [-f] <object> <replacement>
_git replace_ [-f] --edit <object>
_git replace_ [-f] --graft <commit> [<parent>…​]
_git replace_ [-f] --convert-graft-file
_git replace_ -d <object>…​
_git replace_ [--format=<format>] [-l [<pattern>]]
```

##  [](https://git-scm.com/docs/git-replace#_description)DESCRIPTION
Adds a _replace_ reference in `refs/replace/` namespace.
The name of the _replace_ reference is the SHA-1 of the object that is replaced. The content of the _replace_ reference is the SHA-1 of the replacement object.
The replaced object and the replacement object must be of the same type. This restriction can be bypassed using `-f`.
Unless `-f` is given, the _replace_ reference must not yet exist.
There is no other restriction on the replaced and replacement objects. Merge commits can be replaced by non-merge commits and vice versa.
Replacement references will be used by default by all Git commands except those doing reachability traversal (prune, pack transfer and fsck).
It is possible to disable the use of replacement references for any command using the `--no-replace-objects` option just after _git_.
For example if commit _foo_ has been replaced by commit _bar_ :
```
$ git --no-replace-objects cat-file commit foo
```

shows information about commit _foo_ , while:
```
$ git cat-file commit foo
```

shows information about commit _bar_.
The `GIT_NO_REPLACE_OBJECTS` environment variable can be set to achieve the same effect as the `--no-replace-objects` option.
##  [](https://git-scm.com/docs/git-replace#_options)OPTIONS 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt--f)-f 


[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---force)--force 
    
If an existing replace ref for the same object exists, it will be overwritten (instead of failing). 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt--d)-d 


[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---delete)--delete 
    
Delete existing replace refs for the given objects. 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---editobject)--edit <object> 
    
Edit an object’s content interactively. The existing content for <object> is pretty-printed into a temporary file, an editor is launched on the file, and the result is parsed to create a new object of the same type as <object>. A replacement ref is then created to replace <object> with the newly created object. See [git-var[1]](https://git-scm.com/docs/git-var) for details about how the editor will be chosen. 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---raw)--raw 
    
When editing, provide the raw object contents rather than pretty-printed ones. Currently this only affects trees, which will be shown in their binary form. This is harder to work with, but can help when repairing a tree that is so corrupted it cannot be pretty-printed. Note that you may need to configure your editor to cleanly read and write binary data. 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---graftcommitparent)--graft <commit> [<parent>…​] 
    
Create a graft commit. A new commit is created with the same content as <commit> except that its parents will be [<parent>…​] instead of <commit>'s parents. A replacement ref is then created to replace <commit> with the newly created commit. Use `--convert-graft-file` to convert a `$GIT_DIR/info/grafts` file and use replace refs instead. 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---convert-graft-file)--convert-graft-file 
    
Creates graft commits for all entries in `$GIT_DIR/info/grafts` and deletes that file upon success. The purpose is to help users with transitioning off of the now-deprecated graft file. 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt--lpattern)-l <pattern> 


[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---listpattern)--list <pattern> 
    
List replace refs for objects that match the given pattern (or all if no pattern is given). Typing "git replace" without arguments, also lists all replace refs. 

[](https://git-scm.com/docs/git-replace#Documentation/git-replace.txt---formatformat)--format=<format> 
    
When listing, use the specified <format>, which can be one of _short_ , _medium_ and _long_. When omitted, the format defaults to _short_.
##  [](https://git-scm.com/docs/git-replace#_formats)FORMATS
The following formats are available:
  * _short_ : <replaced-sha1>
  * _medium_ : <replaced-sha1> → <replacement-sha1>
  * _long_ : <replaced-sha1> (<replaced-type>) → <replacement-sha1> (<replacement-type>)


##  [](https://git-scm.com/docs/git-replace#_creating_replacement_objects)CREATING REPLACEMENT OBJECTS
[git-hash-object[1]](https://git-scm.com/docs/git-hash-object), [git-rebase[1]](https://git-scm.com/docs/git-rebase), and [git-filter-repo](https://github.com/newren/git-filter-repo), among other git commands, can be used to create replacement objects from existing objects. The `--edit` option can also be used with _git replace_ to create a replacement object by editing an existing object.
If you want to replace many blobs, trees or commits that are part of a string of commits, you may just want to create a replacement string of commits and then only replace the commit at the tip of the target string of commits with the commit at the tip of the replacement string of commits.
##  [](https://git-scm.com/docs/git-replace#_bugs)BUGS
Comparing blobs or trees that have been replaced with those that replace them will not work properly. And using `git` `reset` `--hard` to go back to a replaced commit will move the branch to the replacement commit instead of the replaced commit.
There may be other problems when using _git rev-list_ related to pending objects.
##  [](https://git-scm.com/docs/git-replace#_see_also)SEE ALSO
[git-hash-object[1]](https://git-scm.com/docs/git-hash-object) [git-rebase[1]](https://git-scm.com/docs/git-rebase) [git-tag[1]](https://git-scm.com/docs/git-tag) [git-branch[1]](https://git-scm.com/docs/git-branch) [git-commit[1]](https://git-scm.com/docs/git-commit) [git-var[1]](https://git-scm.com/docs/git-var) [git[1]](https://git-scm.com/docs/git) [git-filter-repo](https://github.com/newren/git-filter-repo)
##  [](https://git-scm.com/docs/git-replace#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### replace
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
