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
    * [NAME](https://git-scm.com/docs/git-send-pack#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-send-pack#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-send-pack#_description)
    * [OPTIONS](https://git-scm.com/docs/git-send-pack#_options)
    * [SPECIFYING THE REFS](https://git-scm.com/docs/git-send-pack#_specifying_the_refs)
    * [GIT](https://git-scm.com/docs/git-send-pack#_git)


[ English ▾](https://git-scm.com/docs/git-send-pack)
Localized versions of **git-send-pack** manual
  1. [English ](https://git-scm.com/docs/git-send-pack)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-send-pack/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-send-pack/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-send-pack/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-send-pack)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-send-pack) git-send-pack last updated in 2.52.0
Changes in the **git-send-pack** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-send-pack/2.52.0)
  3. 2.43.1 → 2.51.2 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-send-pack/2.43.0)
  5. 2.39.1 → 2.42.4 no changes
  6. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-send-pack/2.39.0)
  7. 2.34.1 → 2.38.5 no changes
  8. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-send-pack/2.34.0)
  9. 2.18.1 → 2.33.8 no changes
  10. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-send-pack/2.18.0)
  11. 2.16.6 → 2.17.6 no changes
  12. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-send-pack/2.15.4)
  13. 2.14.6 no changes
  14. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-send-pack/2.13.7)
  15. 2.10.5 → 2.12.5 no changes
  16. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-send-pack/2.9.5)
  17. 2.7.6 → 2.8.6 no changes
  18. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-send-pack/2.6.7)
  19. 2.5.6 no changes
  20. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-send-pack/2.4.12)
  21. 2.2.3 → 2.3.10 no changes
  22. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-send-pack/2.1.4)
  23. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-send-pack/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-send-pack#_name)NAME
git-send-pack - Push objects over Git protocol to another repository
##  [](https://git-scm.com/docs/git-send-pack#_synopsis)SYNOPSIS
```
_git send-pack_ [--mirror] [--dry-run] [--force]
		[--receive-pack=<git-receive-pack>]
		[--verbose] [--thin] [--atomic]
		[--[no-]signed | --signed=(true|false|if-asked)]
		[<host>:]<directory> (--all | <ref>…​)
```

##  [](https://git-scm.com/docs/git-send-pack#_description)DESCRIPTION
Usually you would want to use _git push_ , which is a higher-level wrapper of this command, instead. See [git-push[1]](https://git-scm.com/docs/git-push).
Invokes _git-receive-pack_ on a possibly remote repository, and updates it from the current repository, sending named refs.
##  [](https://git-scm.com/docs/git-send-pack#_options)OPTIONS 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---receive-packgit-receive-pack)--receive-pack=<git-receive-pack> 
    
Path to the _git-receive-pack_ program on the remote end. Sometimes useful when pushing to a remote repository over ssh, and you do not have the program in a directory on the default $PATH. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---execgit-receive-pack)--exec=<git-receive-pack> 
    
Same as --receive-pack=<git-receive-pack>. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---all)--all 
    
Instead of explicitly specifying which refs to update, update all heads that locally exist. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---stdin)--stdin 
    
Take the list of refs from stdin, one per line. If there are refs specified on the command line in addition to this option, then the refs from stdin are processed after those on the command line.
If `--stateless-rpc` is specified together with this option then the list of refs must be in packet format (pkt-line). Each ref must be in a separate packet, and the list must end with a flush packet. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---dry-run)--dry-run 
    
Do everything except actually send the updates. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---force)--force 
    
Usually, the command refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. This flag disables the check. This means that the remote repository can lose commits; use it with care. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---verbose)--verbose 
    
Run verbosely. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---thin)--thin 
    
Send a "thin" pack, which records objects in deltified form based on objects not included in the pack to reduce network traffic. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---atomic)--atomic 
    
Use an atomic transaction for updating the refs. If any of the refs fails to update then the entire push will fail without changing any refs. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---signed)--signed 


[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---no-signed)--no-signed 


[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---signedtruefalseif-asked)--signed=(true|false|if-asked) 
    
GPG-sign the push request to update refs on the receiving side, to allow it to be checked by the hooks and/or be logged. If `false` or `--no-signed`, no signing will be attempted. If `true` or `--signed`, the push will fail if the server does not support signed pushes. If set to `if-asked`, sign if and only if the server supports signed pushes. The push will also fail if the actual call to `gpg` `--sign` fails. See [git-receive-pack[1]](https://git-scm.com/docs/git-receive-pack) for the details on the receiving end. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt---push-optionstring)--push-option=<string> 
    
Pass the specified string as a push option for consumption by hooks on the server side. If the server doesn’t support push options, error out. See [git-push[1]](https://git-scm.com/docs/git-push) and [githooks[5]](https://git-scm.com/docs/githooks) for details. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt-host)<host> 
    
A remote host to house the repository. When this part is specified, _git-receive-pack_ is invoked via ssh. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt-directory)<directory> 
    
The repository to update. 

[](https://git-scm.com/docs/git-send-pack#Documentation/git-send-pack.txt-ref)<ref>…​ 
    
The remote refs to update.
##  [](https://git-scm.com/docs/git-send-pack#_specifying_the_refs)SPECIFYING THE REFS
There are three ways to specify which refs to update on the remote end.
With the `--all` flag, all refs that exist locally are transferred to the remote side. You cannot specify any _< ref>_ if you use this flag.
Without `--all` and without any _< ref>_, the heads that exist both on the local side and on the remote side are updated.
When one or more _< ref>_ are specified explicitly (whether on the command line or via `--stdin`), it can be either a single pattern, or a pair of such patterns separated by a colon ":" (this means that a ref name cannot have a colon in it). A single pattern _< name>_ is just shorthand for _< name>:<name>_.
Each pattern pair consists of the source side (before the colon) and the destination side (after the colon). The ref to be pushed is determined by finding a match that matches the source side, and where it is pushed is determined by using the destination side. The rules used to match a ref are the same rules used by _git rev-parse_ to resolve a symbolic ref name. See [git-rev-parse[1]](https://git-scm.com/docs/git-rev-parse).
  * It is an error if <src> does not match exactly one of the local refs.
  * It is an error if <dst> matches more than one remote ref.
  * If <dst> does not match any remote ref, either
    * it has to start with "refs/"; <dst> is used as the destination literally in this case.
    * <src> == <dst> and the ref that matched the <src> must not exist in the set of remote refs; the ref matched <src> locally is used as the name of the destination.


Without `--force`, the <src> ref is stored at the remote only if <dst> does not exist, or <dst> is a proper subset (i.e. an ancestor) of <src>. This check, known as the "fast-forward check", is performed to avoid accidentally overwriting the remote ref and losing other people’s commits from there.
With `--force`, the fast-forward check is disabled for all refs.
Optionally, a <ref> parameter can be prefixed with a plus _+_ sign to disable the fast-forward check only on that ref.
##  [](https://git-scm.com/docs/git-send-pack#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### send-pack
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
