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
    * [NAME](https://git-scm.com/docs/git-show-ref#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-show-ref#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-show-ref#_description)
    * [OPTIONS](https://git-scm.com/docs/git-show-ref#_options)
    * [OUTPUT](https://git-scm.com/docs/git-show-ref#_output)
    * [EXAMPLES](https://git-scm.com/docs/git-show-ref#_examples)
    * [FILES](https://git-scm.com/docs/git-show-ref#_files)
    * [SEE ALSO](https://git-scm.com/docs/git-show-ref#_see_also)
    * [GIT](https://git-scm.com/docs/git-show-ref#_git)


[ English ▾](https://git-scm.com/docs/git-show-ref)
Localized versions of **git-show-ref** manual
  1. [English ](https://git-scm.com/docs/git-show-ref)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-show-ref/pt_BR)
  3. [Svenska ](https://git-scm.com/docs/git-show-ref/sv)
  4. [українська мова ](https://git-scm.com/docs/git-show-ref/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-show-ref/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-show-ref)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-show-ref) git-show-ref last updated in 2.46.0
Changes in the **git-show-ref** manual
  1. 2.46.1 → 2.53.0 no changes
  2. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-show-ref/2.46.0)
  3. 2.43.1 → 2.45.4 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-show-ref/2.43.0)
  5. 2.42.1 → 2.42.4 no changes
  6. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-show-ref/2.42.0)
  7. 2.39.1 → 2.41.3 no changes
  8. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-show-ref/2.39.0)
  9. 2.21.1 → 2.38.5 no changes
  10. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/git-show-ref/2.21.0)
  11. 2.18.1 → 2.20.5 no changes
  12. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-show-ref/2.18.0)
  13. 2.10.5 → 2.17.6 no changes
  14. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-show-ref/2.9.5)
  15. 2.7.6 → 2.8.6 no changes
  16. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-show-ref/2.6.7)
  17. 2.1.4 → 2.5.6 no changes
  18. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-show-ref/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-show-ref#_name)NAME
git-show-ref - List references in a local repository
##  [](https://git-scm.com/docs/git-show-ref#_synopsis)SYNOPSIS
```
_git show-ref_ [--head] [-d | --dereference]
	     [-s | --hash[=<n>]] [--abbrev[=<n>]] [--branches] [--tags]
	     [--] [<pattern>…​]
_git show-ref_ --verify [-q | --quiet] [-d | --dereference]
	     [-s | --hash[=<n>]] [--abbrev[=<n>]]
	     [--] [<ref>…​]
_git show-ref_ --exclude-existing[=<pattern>]
_git show-ref_ --exists <ref>
```

##  [](https://git-scm.com/docs/git-show-ref#_description)DESCRIPTION
Displays references available in a local repository along with the associated commit IDs. Results can be filtered using a pattern and tags can be dereferenced into object IDs. Additionally, it can be used to test whether a particular ref exists.
By default, shows the tags, heads, and remote refs.
The `--exclude-existing` form is a filter that does the inverse. It reads refs from stdin, one ref per line, and shows those that don’t exist in the local repository.
The `--exists` form can be used to check for the existence of a single references. This form does not verify whether the reference resolves to an actual object.
Use of this utility is encouraged in favor of directly accessing files under the `.git` directory.
##  [](https://git-scm.com/docs/git-show-ref#_options)OPTIONS 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---head)--head 
    
Show the HEAD reference, even if it would normally be filtered out. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---branches)--branches 


[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---tags)--tags 
    
Limit to local branches and local tags, respectively. These options are not mutually exclusive; when given both, references stored in "refs/heads" and "refs/tags" are displayed. Note that `--heads` is a deprecated synonym for `--branches` and may be removed in the future. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt--d)-d 


[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---dereference)--dereference 
    
Dereference tags into object IDs as well. They will be shown with `^{}` appended. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt--s)-s 


[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---hashn)--hash[=<n>] 
    
Only show the OID, not the reference name. When combined with `--dereference`, the dereferenced tag will still be shown after the OID. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---verify)--verify 
    
Enable stricter reference checking by requiring an exact ref path. Aside from returning an error code of 1, it will also print an error message if `--quiet` was not specified. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---exists)--exists 
    
Check whether the given reference exists. Returns an exit code of 0 if it does, 2 if it is missing, and 1 in case looking up the reference failed with an error other than the reference being missing. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---abbrevn)--abbrev[=<n>] 
    
Abbreviate the object name. When using `--hash`, you do not have to say `--hash` `--abbrev`; `--hash=n` would do. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt--q)-q 


[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---quiet)--quiet 
    
Do not print any results to stdout. Can be used with `--verify` to silently check if a reference exists. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt---exclude-existingpattern)--exclude-existing[=<pattern>] 
    
Make `git` `show-ref` act as a filter that reads refs from stdin of the form _^(?: <anything>\s)?<refname>(?:\^{})?$_ and performs the following actions on each: (1) strip `^{}` at the end of line if any; (2) ignore if pattern is provided and does not head-match refname; (3) warn if refname is not a well-formed refname and skip; (4) ignore if refname is a ref that exists in the local repository; (5) otherwise output the line. 

[](https://git-scm.com/docs/git-show-ref#Documentation/git-show-ref.txt-pattern)<pattern>…​ 
    
Show references matching one or more patterns. Patterns are matched from the end of the full name, and only complete parts are matched, e.g. _master_ matches _refs/heads/master_ , _refs/remotes/origin/master_ , _refs/tags/jedi/master_ but not _refs/heads/mymaster_ or _refs/remotes/master/jedi_.
##  [](https://git-scm.com/docs/git-show-ref#_output)OUTPUT
The output is in the format:
```
<oid> SP <ref> LF
```

For example,
```
$ git show-ref --head --dereference
832e76a9899f560a90ffd62ae2ce83bbeff58f54 HEAD
832e76a9899f560a90ffd62ae2ce83bbeff58f54 refs/heads/master
832e76a9899f560a90ffd62ae2ce83bbeff58f54 refs/heads/origin
3521017556c5de4159da4615a39fa4d5d2c279b5 refs/tags/v0.99.9c
6ddc0964034342519a87fe013781abf31c6db6ad refs/tags/v0.99.9c^{}
055e4ae3ae6eb344cbabf2a5256a49ea66040131 refs/tags/v1.0rc4
423325a2d24638ddcc82ce47be5e40be550f4507 refs/tags/v1.0rc4^{}
...
```

When using `--hash` (and not `--dereference`), the output is in the format:
```
<oid> LF
```

For example,
```
$ git show-ref --branches --hash
2e3ba0114a1f52b47df29743d6915d056be13278
185008ae97960c8d551adcd9e23565194651b5d1
03adf42c988195b50e1a1935ba5fcbc39b2b029b
...
```

##  [](https://git-scm.com/docs/git-show-ref#_examples)EXAMPLES
To show all references called "master", whether tags or heads or anything else, and regardless of how deep in the reference naming hierarchy they are, use:
```
	git show-ref master
```

This will show "refs/heads/master" but also "refs/remote/other-repo/master", if such references exist.
When using the `--verify` flag, the command requires an exact path:
```
	git show-ref --verify refs/heads/master
```

will only match the exact branch called "master".
If nothing matches, `git` `show-ref` will return an error code of 1, and in the case of verification, it will show an error message.
For scripting, you can ask it to be quiet with the `--quiet` flag, which allows you to do things like
```
	git show-ref --quiet --verify -- "refs/heads/$headname" ||
		echo "$headname is not a valid branch"
```

to check whether a particular branch exists or not (notice how we don’t actually want to show any results, and we want to use the full refname for it in order to not trigger the problem with ambiguous partial matches).
To show only tags, or only proper branch heads, use `--tags` and/or `--branches` respectively (using both means that it shows tags and branches, but not other random references under the refs/ subdirectory).
To do automatic tag object dereferencing, use the `-d` or `--dereference` flag, so you can do
```
	git show-ref --tags --dereference
```

to get a listing of all tags together with what they dereference.
##  [](https://git-scm.com/docs/git-show-ref#_files)FILES
`.git/refs/*`, `.git/packed-refs`
##  [](https://git-scm.com/docs/git-show-ref#_see_also)SEE ALSO
[git-for-each-ref[1]](https://git-scm.com/docs/git-for-each-ref), [git-ls-remote[1]](https://git-scm.com/docs/git-ls-remote), [git-update-ref[1]](https://git-scm.com/docs/git-update-ref), [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout)
##  [](https://git-scm.com/docs/git-show-ref#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### show-ref
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
