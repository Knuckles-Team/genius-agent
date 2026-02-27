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
    * [NAME](https://git-scm.com/docs/git-ls-remote#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-ls-remote#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-ls-remote#_description)
    * [OPTIONS](https://git-scm.com/docs/git-ls-remote#_options)
    * [OUTPUT](https://git-scm.com/docs/git-ls-remote#_output)
    * [EXAMPLES](https://git-scm.com/docs/git-ls-remote#_examples)
    * [SEE ALSO](https://git-scm.com/docs/git-ls-remote#_see_also)
    * [GIT](https://git-scm.com/docs/git-ls-remote#_git)


[ English ▾](https://git-scm.com/docs/git-ls-remote)
Localized versions of **git-ls-remote** manual
  1. [English ](https://git-scm.com/docs/git-ls-remote)
  2. [Français ](https://git-scm.com/docs/git-ls-remote/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-ls-remote/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-ls-remote/sv)
  5. [українська мова ](https://git-scm.com/docs/git-ls-remote/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-ls-remote/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-ls-remote)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-ls-remote) git-ls-remote last updated in 2.48.0
Changes in the **git-ls-remote** manual
  1. 2.48.1 → 2.53.0 no changes
  2. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-ls-remote/2.48.0)
  3. 2.46.1 → 2.47.3 no changes
  4. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-ls-remote/2.46.0)
  5. 2.42.1 → 2.45.4 no changes
  6. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-ls-remote/2.42.0)
  7. 2.40.1 → 2.41.3 no changes
  8. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-ls-remote/2.40.0)
  9. 2.28.1 → 2.39.5 no changes
  10. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git-ls-remote/2.28.0)
  11. 2.25.3 → 2.27.1 no changes
  12. [2.25.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-17_ ](https://git-scm.com/docs/git-ls-remote/2.25.2)
  13. 2.24.1 → 2.25.1 no changes
  14. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-ls-remote/2.24.0)
  15. 2.22.1 → 2.23.4 no changes
  16. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-ls-remote/2.22.0)
  17. 2.18.1 → 2.21.4 no changes
  18. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-ls-remote/2.18.0)
  19. 2.9.5 → 2.17.6 no changes
  20. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-ls-remote/2.8.6)
  21. 2.7.6 no changes
  22. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-ls-remote/2.6.7)
  23. 2.1.4 → 2.5.6 no changes
  24. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-ls-remote/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-ls-remote#_name)NAME
git-ls-remote - List references in a remote repository
##  [](https://git-scm.com/docs/git-ls-remote#_synopsis)SYNOPSIS
```
_git ls-remote_ [--branches] [--tags] [--refs] [--upload-pack=<exec>]
	      [-q | --quiet] [--exit-code] [--get-url] [--sort=<key>]
	      [--symref] [<repository> [<patterns>…​]]
```

##  [](https://git-scm.com/docs/git-ls-remote#_description)DESCRIPTION
Displays references available in a remote repository along with the associated commit IDs.
##  [](https://git-scm.com/docs/git-ls-remote#_options)OPTIONS 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt--b)-b 


[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---branches)--branches 


[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt--t)-t 


[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---tags)--tags 
    
Limit to only local branches and local tags, respectively. These options are _not_ mutually exclusive; when given both, references stored in refs/heads and refs/tags are displayed. Note that `--heads` and `-h` are deprecated synonyms for `--branches` and `-b` and may be removed in the future. Also note that `git` `ls-remote` `-h` used without anything else on the command line gives help, consistent with other git subcommands. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---refs)--refs 
    
Do not show peeled tags or pseudorefs like `HEAD` in the output. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt--q)-q 


[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---quiet)--quiet 
    
Do not print remote URL to stderr. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---upload-packexec)--upload-pack=<exec> 
    
Specify the full path of _git-upload-pack_ on the remote host. This allows listing references from repositories accessed via SSH and where the SSH daemon does not use the PATH configured by the user. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---exit-code)--exit-code 
    
Exit with status "2" when no matching refs are found in the remote repository. Usually the command exits with status "0" to indicate it successfully talked with the remote repository, whether it found any matching refs. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---get-url)--get-url 
    
Expand the URL of the given remote repository taking into account any "url.<base>.insteadOf" config setting (See [git-config[1]](https://git-scm.com/docs/git-config)) and exit without talking to the remote. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---symref)--symref 
    
In addition to the object pointed by it, show the underlying ref pointed by it when showing a symbolic ref. Currently, upload-pack only shows the symref HEAD, so it will be the only one shown by ls-remote. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---sortkey)--sort=<key> 
    
Sort based on the key given. Prefix `-` to sort in descending order of the value. Supports "version:refname" or "v:refname" (tag names are treated as versions). The "version:refname" sort order can also be affected by the "versionsort.suffix" configuration variable. See [git-for-each-ref[1]](https://git-scm.com/docs/git-for-each-ref) for more sort options, but be aware keys like `committerdate` that require access to the objects themselves will not work for refs whose objects have not yet been fetched from the remote, and will give a `missing` `object` error. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt--ooption)-o <option> 


[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt---server-optionoption)--server-option=<option> 
    
Transmit the given string to the server when communicating using protocol version 2. The given string must not contain a NUL or LF character. When multiple `--server-option=`_< option>_ are given, they are all sent to the other side in the order listed on the command line. When no `--server-option=`_< option>_ is given from the command line, the values of configuration variable `remote.`_< name>_`.serverOption` are used instead. 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt-repository)<repository> 
    
The "remote" repository to query. This parameter can be either a URL or the name of a remote (see the GIT URLS and REMOTES sections of [git-fetch[1]](https://git-scm.com/docs/git-fetch)). 

[](https://git-scm.com/docs/git-ls-remote#Documentation/git-ls-remote.txt-patterns)<patterns>…​ 
    
When unspecified, all references, after filtering done with --heads and --tags, are shown. When <patterns>…​ are specified, only references matching one or more of the given patterns are displayed. Each pattern is interpreted as a glob (see `glob` in [gitglossary[7]](https://git-scm.com/docs/gitglossary)) which is matched against the "tail" of a ref, starting either from the start of the ref (so a full name like `refs/heads/foo` matches) or from a slash separator (so `bar` matches `refs/heads/bar` but not `refs/heads/foobar`).
##  [](https://git-scm.com/docs/git-ls-remote#_output)OUTPUT
The output is in the format:
```
<oid> TAB <ref> LF
```

When showing an annotated tag, unless `--refs` is given, two such lines are shown: one with the refname for the tag itself as _< ref>_, and another with _< ref>_ followed by `^{}`. The _< oid>_ on the latter line shows the name of the object the tag points at.
##  [](https://git-scm.com/docs/git-ls-remote#_examples)EXAMPLES
  * List all references (including symbolics and pseudorefs), peeling tags:
```
$ git ls-remote
27d43aaaf50ef0ae014b88bba294f93658016a2e	HEAD
950264636c68591989456e3ba0a5442f93152c1a	refs/heads/main
d9ab777d41f92a8c1684c91cfb02053d7dd1046b	refs/heads/next
d4ca2e3147b409459955613c152220f4db848ee1	refs/tags/v2.40.0
73876f4861cd3d187a4682290ab75c9dccadbc56	refs/tags/v2.40.0^{}
```

  * List all references matching given patterns:
```
$ git ls-remote http://www.kernel.org/pub/scm/git/git.git master seen rc
5fe978a5381f1fbad26a80e682ddd2a401966740	refs/heads/master
c781a84b5204fb294c9ccc79f8b3baceeb32c061	refs/heads/seen
```

  * List only tags matching a given wildcard pattern:
```
$ git ls-remote --tags http://www.kernel.org/pub/scm/git/git.git v\*
485a869c64a68cc5795dd99689797c5900f4716d	refs/tags/v2.39.2
cbf04937d5b9fcf0a76c28f69e6294e9e3ecd7e6	refs/tags/v2.39.2^{}
d4ca2e3147b409459955613c152220f4db848ee1	refs/tags/v2.40.0
73876f4861cd3d187a4682290ab75c9dccadbc56	refs/tags/v2.40.0^{}
```



##  [](https://git-scm.com/docs/git-ls-remote#_see_also)SEE ALSO
[git-check-ref-format[1]](https://git-scm.com/docs/git-check-ref-format).
##  [](https://git-scm.com/docs/git-ls-remote#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### ls-remote
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
