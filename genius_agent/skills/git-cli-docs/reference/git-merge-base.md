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
    * [NAME](https://git-scm.com/docs/git-merge-base#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-merge-base#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-merge-base#_description)
    * [OPERATION MODES](https://git-scm.com/docs/git-merge-base#_operation_modes)
    * [OPTIONS](https://git-scm.com/docs/git-merge-base#_options)
    * [DISCUSSION](https://git-scm.com/docs/git-merge-base#_discussion)
    * [Discussion on fork-point mode](https://git-scm.com/docs/git-merge-base#_discussion_on_fork_point_mode)
    * [See also](https://git-scm.com/docs/git-merge-base#_see_also)
    * [GIT](https://git-scm.com/docs/git-merge-base#_git)


[ English ▾](https://git-scm.com/docs/git-merge-base)
Localized versions of **git-merge-base** manual
  1. [English ](https://git-scm.com/docs/git-merge-base)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-merge-base/pt_BR)
  3. [Svenska ](https://git-scm.com/docs/git-merge-base/sv)
  4. [українська мова ](https://git-scm.com/docs/git-merge-base/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-merge-base/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-merge-base)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-merge-base) git-merge-base last updated in 2.43.0
Changes in the **git-merge-base** manual
  1. 2.43.1 → 2.53.0 no changes
  2. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-merge-base/2.43.0)
  3. 2.39.1 → 2.42.4 no changes
  4. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-merge-base/2.39.0)
  5. 2.24.1 → 2.38.5 no changes
  6. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-merge-base/2.24.0)
  7. 2.23.1 → 2.23.4 no changes
  8. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git-merge-base/2.23.0)
  9. 2.19.3 → 2.22.5 no changes
  10. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-merge-base/2.19.2)
  11. 2.16.6 → 2.19.1 no changes
  12. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git-merge-base/2.15.4)
  13. 2.11.4 → 2.14.6 no changes
  14. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-merge-base/2.10.5)
  15. 2.1.4 → 2.9.5 no changes
  16. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-merge-base/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-merge-base#_name)NAME
git-merge-base - Find as good common ancestors as possible for a merge
##  [](https://git-scm.com/docs/git-merge-base#_synopsis)SYNOPSIS
```
_git merge-base_ [-a | --all] <commit> <commit>…​
_git merge-base_ [-a | --all] --octopus <commit>…​
_git merge-base_ --is-ancestor <commit> <commit>
_git merge-base_ --independent <commit>…​
_git merge-base_ --fork-point <ref> [<commit>]
```

##  [](https://git-scm.com/docs/git-merge-base#_description)DESCRIPTION
_git merge-base_ finds the best common ancestor(s) between two commits to use in a three-way merge. One common ancestor is _better_ than another common ancestor if the latter is an ancestor of the former. A common ancestor that does not have any better common ancestor is a _best common ancestor_ , i.e. a _merge base_. Note that there can be more than one merge base for a pair of commits.
##  [](https://git-scm.com/docs/git-merge-base#_operation_modes)OPERATION MODES
In the most common special case, specifying only two commits on the command line means computing the merge base between the given two commits.
More generally, among the two commits to compute the merge base from, one is specified by the first commit argument on the command line; the other commit is a (possibly hypothetical) commit that is a merge across all the remaining commits on the command line.
As a consequence, the _merge base_ is not necessarily contained in each of the commit arguments if more than two commits are specified. This is different from [git-show-branch[1]](https://git-scm.com/docs/git-show-branch) when used with the `--merge-base` option. 

[](https://git-scm.com/docs/git-merge-base#Documentation/git-merge-base.txt---octopus)--octopus 
    
Compute the best common ancestors of all supplied commits, in preparation for an n-way merge. This mimics the behavior of _git show-branch --merge-base_. 

[](https://git-scm.com/docs/git-merge-base#Documentation/git-merge-base.txt---independent)--independent 
    
Instead of printing merge bases, print a minimal subset of the supplied commits with the same ancestors. In other words, among the commits given, list those which cannot be reached from any other. This mimics the behavior of _git show-branch --independent_. 

[](https://git-scm.com/docs/git-merge-base#Documentation/git-merge-base.txt---is-ancestor)--is-ancestor 
    
Check if the first <commit> is an ancestor of the second <commit>, and exit with status 0 if true, or with status 1 if not. Errors are signaled by a non-zero status that is not 1. 

[](https://git-scm.com/docs/git-merge-base#Documentation/git-merge-base.txt---fork-point)--fork-point 
    
Find the point at which a branch (or any history that leads to <commit>) forked from another branch (or any reference) <ref>. This does not just look for the common ancestor of the two commits, but also takes into account the reflog of <ref> to see if the history leading to <commit> forked from an earlier incarnation of the branch <ref> (see discussion of this mode below).
##  [](https://git-scm.com/docs/git-merge-base#_options)OPTIONS 

[](https://git-scm.com/docs/git-merge-base#Documentation/git-merge-base.txt--a)-a 


[](https://git-scm.com/docs/git-merge-base#Documentation/git-merge-base.txt---all)--all 
    
Output all merge bases for the commits, instead of just one.
##  [](https://git-scm.com/docs/git-merge-base#_discussion)DISCUSSION
Given two commits _A_ and _B_ , `git` `merge-base` `A` `B` will output a commit which is reachable from both _A_ and _B_ through the parent relationship.
For example, with this topology:
```
	 o---o---o---B
	/
---o---1---o---o---o---A
```

the merge base between _A_ and _B_ is _1_.
Given three commits _A_ , _B_ , and _C_ , `git` `merge-base` `A` `B` `C` will compute the merge base between _A_ and a hypothetical commit _M_ , which is a merge between _B_ and _C_. For example, with this topology:
```
       o---o---o---o---C
      /
     /   o---o---o---B
    /   /
---2---1---o---o---o---A
```

the result of `git` `merge-base` `A` `B` `C` is _1_. This is because the equivalent topology with a merge commit _M_ between _B_ and _C_ is:
```
       o---o---o---o---o
      /                 \
     /   o---o---o---o---M
    /   /
---2---1---o---o---o---A
```

and the result of `git` `merge-base` `A` `M` is _1_. Commit _2_ is also a common ancestor between _A_ and _M_ , but _1_ is a better common ancestor, because _2_ is an ancestor of _1_. Hence, _2_ is not a merge base.
The result of `git` `merge-base` `--octopus` `A` `B` `C` is _2_ , because _2_ is the best common ancestor of all commits.
When the history involves criss-cross merges, there can be more than one _best_ common ancestor for two commits. For example, with this topology:
```
---1---o---A
    \ /
     X
    / \
---2---o---o---B
```

both _1_ and _2_ are merge bases of A and B. Neither one is better than the other (both are _best_ merge bases). When the `--all` option is not given, it is unspecified which best one is output.
A common idiom to check "fast-forward-ness" between two commits A and B is (or at least used to be) to compute the merge base between A and B, and check if it is the same as A, in which case, A is an ancestor of B. You will see this idiom used often in older scripts.
```
A=$(git rev-parse --verify A)
if test "$A" = "$(git merge-base A B)"
then
	... A is an ancestor of B ...
fi
```

In modern git, you can say this in a more direct way:
```
if git merge-base --is-ancestor A B
then
	... A is an ancestor of B ...
fi
```

instead.
##  [](https://git-scm.com/docs/git-merge-base#_discussion_on_fork_point_mode)Discussion on fork-point mode
After working on the `topic` branch created with `git` `switch` `-c` `topic` `origin/master`, the history of remote-tracking branch `origin/master` may have been rewound and rebuilt, leading to a history of this shape:
```
		 o---B2
		/
---o---o---B1--o---o---o---B (origin/master)
	\
	 B0
	  \
	   D0---D1---D (topic)
```

where `origin/master` used to point at commits B0, B1, B2 and now it points at B, and your `topic` branch was started on top of it back when `origin/master` was at B0, and you built three commits, D0, D1, and D, on top of it. Imagine that you now want to rebase the work you did on the topic on top of the updated origin/master.
In such a case, `git` `merge-base` `origin/master` `topic` would return the parent of B0 in the above picture, but B0^..D is **not** the range of commits you would want to replay on top of B (it includes B0, which is not what you wrote; it is a commit the other side discarded when it moved its tip from B0 to B1).
`git` `merge-base` `--fork-point` `origin/master` `topic` is designed to help in such a case. It takes not only B but also B0, B1, and B2 (i.e. old tips of the remote-tracking branches your repository’s reflog knows about) into account to see on which commit your topic branch was built and finds B0, allowing you to replay only the commits on your topic, excluding the commits the other side later discarded.
Hence
```
$ fork_point=$(git merge-base --fork-point origin/master topic)
```

will find B0, and
```
$ git rebase --onto origin/master $fork_point topic
```

will replay D0, D1, and D on top of B to create a new history of this shape:
```
		 o---B2
		/
---o---o---B1--o---o---o---B (origin/master)
	\                   \
	 B0                  D0'--D1'--D' (topic - updated)
	  \
	   D0---D1---D (topic - old)
```

A caveat is that older reflog entries in your repository may be expired by `git` `gc`. If B0 no longer appears in the reflog of the remote-tracking branch `origin/master`, the `--fork-point` mode obviously cannot find it and fails, avoiding to give a random and useless result (such as the parent of B0, like the same command without the `--fork-point` option gives).
Also, the remote-tracking branch you use the `--fork-point` mode with must be the one your topic forked from its tip. If you forked from an older commit than the tip, this mode would not find the fork point (imagine in the above sample history B0 did not exist, origin/master started at B1, moved to B2 and then B, and you forked your topic at origin/master^ when origin/master was B1; the shape of the history would be the same as above, without B0, and the parent of B1 is what `git` `merge-base` `origin/master` `topic` correctly finds, but the `--fork-point` mode will not, because it is not one of the commits that used to be at the tip of origin/master).
##  [](https://git-scm.com/docs/git-merge-base#_see_also)See also
[git-rev-list[1]](https://git-scm.com/docs/git-rev-list), [git-show-branch[1]](https://git-scm.com/docs/git-show-branch), [git-merge[1]](https://git-scm.com/docs/git-merge)
##  [](https://git-scm.com/docs/git-merge-base#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### merge-base
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
