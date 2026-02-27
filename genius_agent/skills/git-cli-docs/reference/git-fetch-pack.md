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
    * [NAME](https://git-scm.com/docs/git-fetch-pack#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-fetch-pack#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-fetch-pack#_description)
    * [OPTIONS](https://git-scm.com/docs/git-fetch-pack#_options)
    * [SEE ALSO](https://git-scm.com/docs/git-fetch-pack#_see_also)
    * [GIT](https://git-scm.com/docs/git-fetch-pack#_git)


[ English ▾](https://git-scm.com/docs/git-fetch-pack)
Localized versions of **git-fetch-pack** manual
  1. [English ](https://git-scm.com/docs/git-fetch-pack)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-fetch-pack/pt_BR)
  3. [Svenska ](https://git-scm.com/docs/git-fetch-pack/sv)
  4. [українська мова ](https://git-scm.com/docs/git-fetch-pack/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-fetch-pack/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-fetch-pack)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-fetch-pack) git-fetch-pack last updated in 2.48.0
Changes in the **git-fetch-pack** manual
  1. 2.48.1 → 2.53.0 no changes
  2. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-fetch-pack/2.48.0)
  3. 2.43.1 → 2.47.3 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-fetch-pack/2.43.0)
  5. 2.36.1 → 2.42.4 no changes
  6. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git-fetch-pack/2.36.0)
  7. 2.18.1 → 2.35.8 no changes
  8. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-fetch-pack/2.18.0)
  9. 2.12.5 → 2.17.6 no changes
  10. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-fetch-pack/2.11.4)
  11. 2.10.5 no changes
  12. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-fetch-pack/2.9.5)
  13. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-fetch-pack/2.8.6)
  14. 2.5.6 → 2.7.6 no changes
  15. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-fetch-pack/2.4.12)
  16. 2.1.4 → 2.3.10 no changes
  17. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-fetch-pack/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-fetch-pack#_name)NAME
git-fetch-pack - Receive missing objects from another repository
##  [](https://git-scm.com/docs/git-fetch-pack#_synopsis)SYNOPSIS
```
_git fetch-pack_ [--all] [--quiet|-q] [--keep|-k] [--thin] [--include-tag]
	[--upload-pack=<git-upload-pack>]
	[--depth=<n>] [--no-progress]
	[-v] <repository> [<refs>…​]
```

##  [](https://git-scm.com/docs/git-fetch-pack#_description)DESCRIPTION
Usually you would want to use _git fetch_ , which is a higher level wrapper of this command, instead.
Invokes _git-upload-pack_ on a possibly remote repository and asks it to send objects missing from this repository, to update the named heads. The list of commits available locally is found out by scanning the local refs/ hierarchy and sent to _git-upload-pack_ running on the other end.
This command degenerates to download everything to complete the asked refs from the remote side when the local side does not have a common ancestor commit.
##  [](https://git-scm.com/docs/git-fetch-pack#_options)OPTIONS 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---all)--all 
    
Fetch all remote refs. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---stdin)--stdin 
    
Take the list of refs from stdin, one per line. If there are refs specified on the command line in addition to this option, then the refs from stdin are processed after those on the command line.
If `--stateless-rpc` is specified together with this option then the list of refs must be in packet format (pkt-line). Each ref must be in a separate packet, and the list must end with a flush packet. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt--q)-q 


[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---quiet)--quiet 
    
Pass `-q` flag to _git unpack-objects_ ; this makes the cloning process less verbose. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt--k)-k 


[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---keep)--keep 
    
Do not invoke _git unpack-objects_ on received data, but create a single packfile out of it instead, and store it in the object database. If provided twice then the pack is locked against repacking. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---thin)--thin 
    
Fetch a "thin" pack, which records objects in deltified form based on objects not included in the pack to reduce network traffic. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---include-tag)--include-tag 
    
If the remote side supports it, annotated tags objects will be downloaded on the same connection as the other objects if the object the tag references is downloaded. The caller must otherwise determine the tags this option made available. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---upload-packgit-upload-pack)--upload-pack=<git-upload-pack> 
    
Use this to specify the path to _git-upload-pack_ on the remote side, if it is not found on your $PATH. Installations of sshd ignores the user’s environment setup scripts for login shells (e.g. .bash_profile) and your privately installed git may not be found on the system default $PATH. Another workaround suggested is to set up your $PATH in ".bashrc", but this flag is for people who do not want to pay the overhead for non-interactive shells by having a lean .bashrc file (they set most of the things up in .bash_profile). 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---execgit-upload-pack)--exec=<git-upload-pack> 
    
Same as --upload-pack=<git-upload-pack>. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---depthn)--depth=<n> 
    
Limit fetching to ancestor-chains not longer than n. _git-upload-pack_ treats the special depth 2147483647 as infinite even if there is an ancestor-chain that long. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---shallow-sincedate)--shallow-since=<date> 
    
Deepen or shorten the history of a shallow repository to include all reachable commits after <date>. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---shallow-excluderef)--shallow-exclude=<ref> 
    
Deepen or shorten the history of a shallow repository to exclude commits reachable from a specified remote branch or tag. This option can be specified multiple times. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---deepen-relative)--deepen-relative 
    
Argument --depth specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---refetch)--refetch 
    
Skips negotiating commits with the server in order to fetch all matching objects. Use to reapply a new partial clone blob/tree filter. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---no-progress)--no-progress 
    
Do not show the progress. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt---check-self-contained-and-connected)--check-self-contained-and-connected 
    
Output "connectivity-ok" if the received pack is self-contained and connected. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt--v)-v 
    
Run verbosely. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt-repository)<repository> 
    
The URL to the remote repository. 

[](https://git-scm.com/docs/git-fetch-pack#Documentation/git-fetch-pack.txt-refs)<refs>…​ 
    
The remote heads to update from. This is relative to $GIT_DIR (e.g. "HEAD", "refs/heads/master"). When unspecified, update from all heads the remote side has.
If the remote has enabled the options `uploadpack.allowTipSHA1InWant`, `uploadpack.allowReachableSHA1InWant`, or `uploadpack.allowAnySHA1InWant`, they may alternatively be 40-hex sha1s present on the remote.
##  [](https://git-scm.com/docs/git-fetch-pack#_see_also)SEE ALSO
[git-fetch[1]](https://git-scm.com/docs/git-fetch)
##  [](https://git-scm.com/docs/git-fetch-pack#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### fetch-pack
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
