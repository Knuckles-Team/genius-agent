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
    * [NAME](https://git-scm.com/docs/git-describe#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-describe#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-describe#_description)
    * [OPTIONS](https://git-scm.com/docs/git-describe#_options)
    * [EXAMPLES](https://git-scm.com/docs/git-describe#_examples)
    * [SEARCH STRATEGY](https://git-scm.com/docs/git-describe#_search_strategy)
    * [BUGS](https://git-scm.com/docs/git-describe#_bugs)
    * [GIT](https://git-scm.com/docs/git-describe#_git)


[ English ▾](https://git-scm.com/docs/git-describe)
Localized versions of **git-describe** manual
  1. [English ](https://git-scm.com/docs/git-describe)
  2. [Français ](https://git-scm.com/docs/git-describe/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-describe/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-describe/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-describe/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-describe)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-describe) git-describe last updated in 2.42.0
Changes in the **git-describe** manual
  1. 2.42.1 → 2.53.0 no changes
  2. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-describe/2.42.0)
  3. 2.33.1 → 2.41.3 no changes
  4. [2.33.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-08-16_ ](https://git-scm.com/docs/git-describe/2.33.0)
  5. 2.22.1 → 2.32.7 no changes
  6. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git-describe/2.22.0)
  7. 2.19.3 → 2.21.4 no changes
  8. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-describe/2.19.2)
  9. 2.17.0 → 2.19.1 no changes
  10. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-describe/2.16.6)
  11. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-describe/2.15.4)
  12. 2.14.6 no changes
  13. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-describe/2.13.7)
  14. 2.10.5 → 2.12.5 no changes
  15. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git-describe/2.9.5)
  16. 2.7.6 → 2.8.6 no changes
  17. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-describe/2.6.7)
  18. 2.5.6 no changes
  19. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-describe/2.4.12)
  20. 2.1.4 → 2.3.10 no changes
  21. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-describe/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-describe#_name)NAME
git-describe - Give an object a human readable name based on an available ref
##  [](https://git-scm.com/docs/git-describe#_synopsis)SYNOPSIS
```
_git describe_ [--all] [--tags] [--contains] [--abbrev=<n>] [<commit-ish>…​]
_git describe_ [--all] [--tags] [--contains] [--abbrev=<n>] --dirty[=<mark>]
_git describe_ <blob>
```

##  [](https://git-scm.com/docs/git-describe#_description)DESCRIPTION
The command finds the most recent tag that is reachable from a commit. If the tag points to the commit, then only the tag is shown. Otherwise, it suffixes the tag name with the number of additional commits on top of the tagged object and the abbreviated object name of the most recent commit. The result is a "human-readable" object name which can also be used to identify the commit to other git commands.
By default (without --all or --tags) `git` `describe` only shows annotated tags. For more information about creating annotated tags see the -a and -s options to [git-tag[1]](https://git-scm.com/docs/git-tag).
If the given object refers to a blob, it will be described as _< commit-ish>_`:`_< path>_, such that the blob can be found at _< path>_ in the _< commit-ish>_, which itself describes the first commit in which this blob occurs in a reverse revision walk from HEAD.
##  [](https://git-scm.com/docs/git-describe#_options)OPTIONS 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt-commit-ish)<commit-ish>…​ 
    
Commit-ish object names to describe. Defaults to HEAD if omitted. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---dirtymark)--dirty[=<mark>] 


[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---brokenmark)--broken[=<mark>] 
    
Describe the state of the working tree. When the working tree matches HEAD, the output is the same as "git describe HEAD". If the working tree has local modification "-dirty" is appended to it. If a repository is corrupt and Git cannot determine if there is local modification, Git will error out, unless ‘--broken’ is given, which appends the suffix "-broken" instead. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---all)--all 
    
Instead of using only the annotated tags, use any ref found in `refs/` namespace. This option enables matching any known branch, remote-tracking branch, or lightweight tag. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---tags)--tags 
    
Instead of using only the annotated tags, use any tag found in `refs/tags` namespace. This option enables matching a lightweight (non-annotated) tag. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---contains)--contains 
    
Instead of finding the tag that predates the commit, find the tag that comes after the commit, and thus contains it. Automatically implies --tags. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---abbrevn)--abbrev=<n> 
    
Instead of using the default number of hexadecimal digits (which will vary according to the number of objects in the repository with a default of 7) of the abbreviated object name, use <n> digits, or as many digits as needed to form a unique object name. An <n> of 0 will suppress long format, only showing the closest tag. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---candidatesn)--candidates=<n> 
    
Instead of considering only the 10 most recent tags as candidates to describe the input commit-ish consider up to <n> candidates. Increasing <n> above 10 will take slightly longer but may produce a more accurate result. An <n> of 0 will cause only exact matches to be output. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---exact-match)--exact-match 
    
Only output exact matches (a tag directly references the supplied commit). This is a synonym for --candidates=0. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---debug)--debug 
    
Verbosely display information about the searching strategy being employed to standard error. The tag name will still be printed to standard out. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---long)--long 
    
Always output the long format (the tag, the number of commits and the abbreviated commit name) even when it matches a tag. This is useful when you want to see parts of the commit object name in "describe" output, even when the commit in question happens to be a tagged version. Instead of just emitting the tag name, it will describe such a commit as v1.2-0-gdeadbee (0th commit since tag v1.2 that points at object deadbee…​.). 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---matchpattern)--match <pattern> 
    
Only consider tags matching the given `glob`(`7`) pattern, excluding the "refs/tags/" prefix. If used with `--all`, it also considers local branches and remote-tracking references matching the pattern, excluding respectively "refs/heads/" and "refs/remotes/" prefix; references of other types are never considered. If given multiple times, a list of patterns will be accumulated, and tags matching any of the patterns will be considered. Use `--no-match` to clear and reset the list of patterns. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---excludepattern)--exclude <pattern> 
    
Do not consider tags matching the given `glob`(`7`) pattern, excluding the "refs/tags/" prefix. If used with `--all`, it also does not consider local branches and remote-tracking references matching the pattern, excluding respectively "refs/heads/" and "refs/remotes/" prefix; references of other types are never considered. If given multiple times, a list of patterns will be accumulated and tags matching any of the patterns will be excluded. When combined with --match a tag will be considered when it matches at least one --match pattern and does not match any of the --exclude patterns. Use `--no-exclude` to clear and reset the list of patterns. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---always)--always 
    
Show uniquely abbreviated commit object as fallback. 

[](https://git-scm.com/docs/git-describe#Documentation/git-describe.txt---first-parent)--first-parent 
    
Follow only the first parent commit upon seeing a merge commit. This is useful when you wish to not match tags on branches merged in the history of the target commit.
##  [](https://git-scm.com/docs/git-describe#_examples)EXAMPLES
With something like git.git current tree, I get:
```
[torvalds@g5 git]$ git describe parent
v1.0.4-14-g2414721
```

i.e. the current head of my "parent" branch is based on v1.0.4, but since it has a few commits on top of that, describe has added the number of additional commits ("14") and an abbreviated object name for the commit itself ("2414721") at the end.
The number of additional commits is the number of commits which would be displayed by "git log v1.0.4..parent". The hash suffix is "-g" + an unambiguous abbreviation for the tip commit of parent (which was `2414721b194453f058079d897d13c4e377f92dc6`). The length of the abbreviation scales as the repository grows, using the approximate number of objects in the repository and a bit of math around the birthday paradox, and defaults to a minimum of 7. The "g" prefix stands for "git" and is used to allow describing the version of a software depending on the SCM the software is managed with. This is useful in an environment where people may use different SCMs.
Doing a _git describe_ on a tag-name will just show the tag name:
```
[torvalds@g5 git]$ git describe v1.0.4
v1.0.4
```

With --all, the command can use branch heads as references, so the output shows the reference path as well:
```
[torvalds@g5 git]$ git describe --all --abbrev=4 v1.0.5^2
tags/v1.0.0-21-g975b
```

```
[torvalds@g5 git]$ git describe --all --abbrev=4 HEAD^
heads/lt/describe-7-g975b
```

With --abbrev set to 0, the command can be used to find the closest tagname without any suffix:
```
[torvalds@g5 git]$ git describe --abbrev=0 v1.0.5^2
tags/v1.0.0
```

Note that the suffix you get if you type these commands today may be longer than what Linus saw above when he ran these commands, as your Git repository may have new commits whose object names begin with 975b that did not exist back then, and "-g975b" suffix alone may not be sufficient to disambiguate these commits.
##  [](https://git-scm.com/docs/git-describe#_search_strategy)SEARCH STRATEGY
For each commit-ish supplied, _git describe_ will first look for a tag which tags exactly that commit. Annotated tags will always be preferred over lightweight tags, and tags with newer dates will always be preferred over tags with older dates. If an exact match is found, its name will be output and searching will stop.
If an exact match was not found, _git describe_ will walk back through the commit history to locate an ancestor commit which has been tagged. The ancestor’s tag will be output along with an abbreviation of the input commit-ish’s SHA-1. If `--first-parent` was specified then the walk will only consider the first parent of each commit.
If multiple tags were found during the walk then the tag which has the fewest commits different from the input commit-ish will be selected and output. Here fewest commits different is defined as the number of commits which would be shown by `git` `log` `tag..input` will be the smallest number of commits possible.
##  [](https://git-scm.com/docs/git-describe#_bugs)BUGS
Tree objects as well as tag objects not pointing at commits, cannot be described. When describing blobs, the lightweight tags pointing at blobs are ignored, but the blob is still described as <commit-ish>:<path> despite the lightweight tag being favorable.
##  [](https://git-scm.com/docs/git-describe#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### describe
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
