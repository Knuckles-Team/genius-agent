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
    * [NAME](https://git-scm.com/docs/git-commit-tree#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-commit-tree#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-commit-tree#_description)
    * [OPTIONS](https://git-scm.com/docs/git-commit-tree#_options)
    * [Commit Information](https://git-scm.com/docs/git-commit-tree#_commit_information)
    * [DATE FORMATS](https://git-scm.com/docs/git-commit-tree#_date_formats)
    * [Discussion](https://git-scm.com/docs/git-commit-tree#_discussion)
    * [FILES](https://git-scm.com/docs/git-commit-tree#_files)
    * [SEE ALSO](https://git-scm.com/docs/git-commit-tree#_see_also)
    * [GIT](https://git-scm.com/docs/git-commit-tree#_git)


[ English ▾](https://git-scm.com/docs/git-commit-tree)
Localized versions of **git-commit-tree** manual
  1. [English ](https://git-scm.com/docs/git-commit-tree)
  2. [Français ](https://git-scm.com/docs/git-commit-tree/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-commit-tree/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-commit-tree/sv)
  5. [українська мова ](https://git-scm.com/docs/git-commit-tree/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-commit-tree/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-commit-tree)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-commit-tree) git-commit-tree last updated in 2.49.0
Changes in the **git-commit-tree** manual
  1. 2.49.1 → 2.53.0 no changes
  2. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git-commit-tree/2.49.0)
  3. 2.45.1 → 2.48.2 no changes
  4. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-commit-tree/2.45.0)
  5. 2.43.1 → 2.44.4 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-commit-tree/2.43.0)
  7. 2.35.1 → 2.42.4 no changes
  8. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-commit-tree/2.35.0)
  9. 2.31.1 → 2.34.8 no changes
  10. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-commit-tree/2.31.0)
  11. 2.27.1 → 2.30.9 no changes
  12. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-commit-tree/2.27.0)
  13. 2.25.2 → 2.26.3 no changes
  14. 2.25.1 no changes
  15. 2.22.1 → 2.25.0 no changes
  16. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-commit-tree/2.22.0)
  17. 2.14.6 → 2.21.4 no changes
  18. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-commit-tree/2.13.7)
  19. 2.12.5 no changes
  20. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-commit-tree/2.11.4)
  21. 2.10.5 no changes
  22. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-commit-tree/2.9.5)
  23. 2.7.6 → 2.8.6 no changes
  24. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-commit-tree/2.6.7)
  25. 2.5.6 no changes
  26. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-commit-tree/2.4.12)
  27. 2.1.4 → 2.3.10 no changes
  28. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-commit-tree/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-commit-tree#_name)NAME
git-commit-tree - Create a new commit object
##  [](https://git-scm.com/docs/git-commit-tree#_synopsis)SYNOPSIS
```
_git commit-tree_ <tree> [(-p <parent>)…​]
_git commit-tree_ [(-p <parent>)…​] [-S[<keyid>]] [(-m <message>)…​]
		  [(-F <file>)…​] <tree>
```

##  [](https://git-scm.com/docs/git-commit-tree#_description)DESCRIPTION
This is usually not what an end user wants to run directly. See [git-commit[1]](https://git-scm.com/docs/git-commit) instead.
Creates a new commit object based on the provided tree object and emits the new commit object id on stdout. The log message is read from the standard input, unless `-m` or `-F` options are given.
The `-m` and `-F` options can be given any number of times, in any order. The commit log message will be composed in the order in which the options are given.
A commit object may have any number of parents. With exactly one parent, it is an ordinary commit. Having more than one parent makes the commit a merge between several lines of history. Initial (root) commits have no parents.
While a tree represents a particular directory state of a working directory, a commit represents that state in "time", and explains how to get there.
Normally a commit would identify a new "HEAD" state, and while Git doesn’t care where you save the note about that state, in practice we tend to just write the result to the file that is pointed at by `.git/HEAD`, so that we can always see what the last committed state was.
##  [](https://git-scm.com/docs/git-commit-tree#_options)OPTIONS 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt-tree)<tree> 
    
An existing tree object. 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt--pparent)-p <parent> 
    
Each `-p` indicates the id of a parent commit object. 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt--mmessage)-m <message> 
    
A paragraph in the commit log message. This can be given more than once and each <message> becomes its own paragraph. 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt--Ffile)-F <file> 
    
Read the commit log message from the given file. Use `-` to read from the standard input. This can be given more than once and the content of each file becomes its own paragraph. 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt--Skeyid)-S[<keyid>] 


[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt---gpg-signkeyid)--gpg-sign[=<keyid>] 


[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt---no-gpg-sign)--no-gpg-sign 
    
GPG-sign commits. The `keyid` argument is optional and defaults to the committer identity; if specified, it must be stuck to the option without a space. `--no-gpg-sign` is useful to countermand a `--gpg-sign` option given earlier on the command line.
##  [](https://git-scm.com/docs/git-commit-tree#_commit_information)Commit Information
A commit encapsulates:
  * all parent object ids
  * author name, email and date
  * committer name and email and the commit time.


A commit comment is read from stdin. If a changelog entry is not provided via "<" redirection, _git commit-tree_ will just wait for one to be entered and terminated with ^D.
##  [](https://git-scm.com/docs/git-commit-tree#_date_formats)DATE FORMATS
The `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables support the following date formats: 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt-Gitinternalformat)Git internal format 
    
It is _< unix-timestamp>_ _< time-zone-offset>_, where _< unix-timestamp>_ is the number of seconds since the UNIX epoch. _< time-zone-offset>_ is a positive or negative offset from UTC. For example CET (which is 1 hour ahead of UTC) is `+0100`. 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt-RFC2822)RFC 2822 
    
The standard date format as described by RFC 2822, for example `Thu,` `07` `Apr` `2005` `22:13:13` `+0200`. 

[](https://git-scm.com/docs/git-commit-tree#Documentation/git-commit-tree.txt-ISO8601)ISO 8601 
    
Time and date specified by the ISO 8601 standard, for example `2005-04-07T22:13:13`. The parser accepts a space instead of the `T` character as well. Fractional parts of a second will be ignored, for example `2005-04-07T22:13:13.019` will be treated as `2005-04-07T22:13:13`.
Note |  In addition, the date part is accepted in the following formats: `YYYY.MM.DD`, `MM/DD/YYYY` and `DD.MM.YYYY`.   
---|---  
##  [](https://git-scm.com/docs/git-commit-tree#_discussion)Discussion
Git is to some extent character encoding agnostic.
  * The contents of the blob objects are uninterpreted sequences of bytes. There is no encoding translation at the core level.
  * Path names are encoded in UTF-8 normalization form C. This applies to tree objects, the index file, ref names, as well as path names in command line arguments, environment variables and config files (`.git/config` (see [git-config[1]](https://git-scm.com/docs/git-config)), [gitignore[5]](https://git-scm.com/docs/gitignore), [gitattributes[5]](https://git-scm.com/docs/gitattributes) and [gitmodules[5]](https://git-scm.com/docs/gitmodules)).
Note that Git at the core level treats path names simply as sequences of non-NUL bytes, there are no path name encoding conversions (except on Mac and Windows). Therefore, using non-ASCII path names will mostly work even on platforms and file systems that use legacy extended ASCII encodings. However, repositories created on such systems will not work properly on UTF-8-based systems (e.g. Linux, Mac, Windows) and vice versa. Additionally, many Git-based tools simply assume path names to be UTF-8 and will fail to display other encodings correctly.
  * Commit log messages are typically encoded in UTF-8, but other extended ASCII encodings are also supported. This includes ISO-8859-x, CP125x and many others, but _not_ UTF-16/32, EBCDIC and CJK multi-byte encodings (GBK, Shift-JIS, Big5, EUC-x, CP9xx etc.).


Although we encourage that the commit log messages are encoded in UTF-8, both the core and Git Porcelain are designed not to force UTF-8 on projects. If all participants of a particular project find it more convenient to use legacy encodings, Git does not forbid it. However, there are a few things to keep in mind.
  1. `git` `commit` and `git` `commit-tree` issue a warning if the commit log message given to it does not look like a valid UTF-8 string, unless you explicitly say your project uses a legacy encoding. The way to say this is to have `i18n.commitEncoding` in `.git/config` file, like this:
```
[i18n]
	commitEncoding = ISO-8859-1
```

Commit objects created with the above setting record the value of `i18n.commitEncoding` in their `encoding` header. This is to help other people who look at them later. Lack of this header implies that the commit log message is encoded in UTF-8.
  2. `git` `log`, `git` `show`, `git` `blame` and friends look at the `encoding` header of a commit object, and try to re-code the log message into UTF-8 unless otherwise specified. You can specify the desired output encoding with `i18n.logOutputEncoding` in `.git/config` file, like this:
```
[i18n]
	logOutputEncoding = ISO-8859-1
```

If you do not have this configuration variable, the value of `i18n.commitEncoding` is used instead.


Note that we deliberately chose not to re-code the commit log message when a commit is made to force UTF-8 at the commit object level, because re-coding to UTF-8 is not necessarily a reversible operation.
##  [](https://git-scm.com/docs/git-commit-tree#_files)FILES
/etc/mailname
##  [](https://git-scm.com/docs/git-commit-tree#_see_also)SEE ALSO
[git-write-tree[1]](https://git-scm.com/docs/git-write-tree) [git-commit[1]](https://git-scm.com/docs/git-commit)
##  [](https://git-scm.com/docs/git-commit-tree#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### commit-tree
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
