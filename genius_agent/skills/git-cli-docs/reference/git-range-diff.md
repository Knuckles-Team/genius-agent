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
    * [NAME](https://git-scm.com/docs/git-range-diff#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-range-diff#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-range-diff#_description)
    * [OPTIONS](https://git-scm.com/docs/git-range-diff#_options)
    * [OUTPUT STABILITY](https://git-scm.com/docs/git-range-diff#_output_stability)
    * [CONFIGURATION](https://git-scm.com/docs/git-range-diff#_configuration)
    * [EXAMPLES](https://git-scm.com/docs/git-range-diff#_examples)
    * [Algorithm](https://git-scm.com/docs/git-range-diff#_algorithm)
    * [SEE ALSO](https://git-scm.com/docs/git-range-diff#_see_also)
    * [GIT](https://git-scm.com/docs/git-range-diff#_git)


[ English ▾](https://git-scm.com/docs/git-range-diff)
Localized versions of **git-range-diff** manual
  1. [English ](https://git-scm.com/docs/git-range-diff)
  2. [Français ](https://git-scm.com/docs/git-range-diff/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-range-diff/pt_BR)
  4. [українська мова ](https://git-scm.com/docs/git-range-diff/uk)
  5. [简体中文 ](https://git-scm.com/docs/git-range-diff/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-range-diff)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-range-diff) git-range-diff last updated in 2.52.0
Changes in the **git-range-diff** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git-range-diff/2.52.0)
  3. 2.48.1 → 2.51.2 no changes
  4. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-range-diff/2.48.0)
  5. 2.43.1 → 2.47.3 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-range-diff/2.43.0)
  7. 2.38.1 → 2.42.4 no changes
  8. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-range-diff/2.38.0)
  9. 2.31.1 → 2.37.7 no changes
  10. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git-range-diff/2.31.0)
  11. 2.25.1 → 2.30.9 no changes
  12. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-range-diff/2.25.0)
  13. 2.20.1 → 2.24.4 no changes
  14. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git-range-diff/2.20.0)
  15. 2.19.1 → 2.19.6 no changes
  16. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git-range-diff/2.19.0)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-range-diff#_name)NAME
git-range-diff - Compare two commit ranges (e.g. two versions of a branch)
##  [](https://git-scm.com/docs/git-range-diff#_synopsis)SYNOPSIS
```
_git range-diff_ [--color=[<when>]] [--no-color] [<diff-options>]
	[--no-dual-color] [--creation-factor=<factor>]
	[--left-only | --right-only] [--diff-merges=<format>]
	[--remerge-diff]
	( <range1> <range2> | <rev1>…​<rev2> | <base> <rev1> <rev2> )
	[[--] <path>…​]
```

##  [](https://git-scm.com/docs/git-range-diff#_description)DESCRIPTION
This command shows the differences between two versions of a patch series, or more generally, two commit ranges (ignoring merge commits).
In the presence of _< path>_ arguments, these commit ranges are limited accordingly.
To that end, it first finds pairs of commits from both commit ranges that correspond with each other. Two commits are said to correspond when the diff between their patches (i.e. the author information, the commit message and the commit diff) is reasonably small compared to the patches' size. See ``Algorithm`` below for details.
Finally, the list of matching commits is shown in the order of the second commit range, with unmatched commits being inserted just after all of their ancestors have been shown.
There are three ways to specify the commit ranges:
  * _< range1>_ _< range2>_: Either commit range can be of the form _< base>_`..`_< rev>_, _< rev>_`^!` or _< rev>_`^-`_< n>_. See `SPECIFYING` `RANGES` in [gitrevisions[7]](https://git-scm.com/docs/gitrevisions) for more details.
  * _< rev1>_`...`_< rev2>_. This is equivalent to _< rev2>_`..`_< rev1>_ _< rev1>_`..`_< rev2>_.
  * _< base>_ _< rev1>_ _< rev2>_: This is equivalent to _< base>_`..`_< rev1>_ _< base>_`..`_< rev2>_.


##  [](https://git-scm.com/docs/git-range-diff#_options)OPTIONS 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---no-dual-color)--no-dual-color 
    
When the commit diffs differ, `git` `range-diff` recreates the original diffs' coloring, and adds outer -/+ diff markers with the **background** being red/green to make it easier to see e.g. when there was a change in what exact lines were added.
Additionally, the commit diff lines that are only present in the first commit range are shown "dimmed" (this can be overridden using the `color.diff.`_< slot>_ config setting where _< slot>_ is one of `contextDimmed`, `oldDimmed` and `newDimmed`), and the commit diff lines that are only present in the second commit range are shown in bold (which can be overridden using the config settings `color.diff.`_< slot>_ with _< slot>_ being one of `contextBold`, `oldBold` or `newBold`).
This is known to `range-diff` as "dual coloring". Use `--no-dual-color` to revert to color all lines according to the outer diff markers (and completely ignore the inner diff when it comes to color). 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---creation-factorpercent)--creation-factor=<percent> 
    
Set the creation/deletion cost fudge factor to _< percent>_. Defaults to 60. Try a larger value if `git` `range-diff` erroneously considers a large change a total rewrite (deletion of one commit and addition of another), and a smaller one in the reverse case. See the ``Algorithm`` section below for an explanation of why this is needed. 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---left-only)--left-only 
    
Suppress commits that are missing from the first specified range (or the "left range" when using the _< rev1>_`...`_< rev2>_ format). 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---right-only)--right-only 
    
Suppress commits that are missing from the second specified range (or the "right range" when using the _< rev1>_`...`_< rev2>_ format). 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---diff-mergesformat)--diff-merges=<format> 
    
Instead of ignoring merge commits, generate diffs for them using the corresponding `--diff-merges=`_< format>_ option of [git-log[1]](https://git-scm.com/docs/git-log), and include them in the comparison.
Note: In the common case, the `remerge` mode will be the most natural one to use, as it shows only the diff on top of what Git’s merge machinery would have produced. In other words, if a merge commit is the result of a non-conflicting `git` `merge`, the `remerge` mode will represent it with an empty diff. 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---remerge-diff)--remerge-diff 
    
Convenience option, equivalent to `--diff-merges=remerge`. 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---notesref)--notes[=<ref>] 


[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt---no-notes)--no-notes 
    
This flag is passed to the `git` `log` program (see [git-log[1]](https://git-scm.com/docs/git-log)) that generates the patches. 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt-range1range2)<range1> <range2> 
    
Compare the commits specified by the two ranges, where _< range1>_ is considered an older version of _< range2>_. 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt-rev1rev2)<rev1>…​<rev2> 
    
Equivalent to passing _< rev2>_`..`_< rev1>_ and _< rev1>_`..`_< rev2>_. 

[](https://git-scm.com/docs/git-range-diff#Documentation/git-range-diff.txt-baserev1rev2)<base> <rev1> <rev2> 
    
Equivalent to passing _< base>_`..`_< rev1>_ and _< base>_`..`_< rev2>_. Note that _< base>_ does not need to be the exact branch point of the branches. Example: after rebasing a branch `my-topic`, `git` `range-diff` `my-topic@{u}` `my-topic@{1}` `my-topic` would show the differences introduced by the rebase.
`git` `range-diff` also accepts the regular diff options (see [git-diff[1]](https://git-scm.com/docs/git-diff)), most notably the `--color=`[_< when>_] and `--no-color` options. These options are used when generating the "diff between patches", i.e. to compare the author, commit message and diff of corresponding old/new commits. There is currently no means to tweak most of the diff options passed to `git` `log` when generating those patches.
##  [](https://git-scm.com/docs/git-range-diff#_output_stability)OUTPUT STABILITY
The output of the `range-diff` command is subject to change. It is intended to be human-readable porcelain output, not something that can be used across versions of Git to get a textually stable `range-diff` (as opposed to something like the `--stable` option to [git-patch-id[1]](https://git-scm.com/docs/git-patch-id)). There’s also no equivalent of [git-apply[1]](https://git-scm.com/docs/git-apply) for `range-diff`, the output is not intended to be machine-readable.
This is particularly true when passing in diff options. Currently some options like `--stat` can, as an emergent effect, produce output that’s quite useless in the context of `range-diff`. Future versions of `range-diff` may learn to interpret such options in a manner specific to `range-diff` (e.g. for `--stat` producing human-readable output which summarizes how the diffstat changed).
##  [](https://git-scm.com/docs/git-range-diff#_configuration)CONFIGURATION
This command uses the `diff.color.*` and `pager.range-diff` settings (the latter is on by default). See [git-config[1]](https://git-scm.com/docs/git-config).
##  [](https://git-scm.com/docs/git-range-diff#_examples)EXAMPLES
When a rebase required merge conflicts to be resolved, compare the changes introduced by the rebase directly afterwards using:
```
$ git range-diff @{u} @{1} @
```

A typical output of `git` `range-diff` would look like this:
```
-:  ------- > 1:  0ddba11 Prepare for the inevitable!
1:  c0debee = 2:  cab005e Add a helpful message at the start
2:  f00dbal ! 3:  decafe1 Describe a bug
    @@ -1,3 +1,3 @@
     Author: A U Thor <author@example.com>

    -TODO: Describe a bug
    +Describe a bug
    @@ -324,5 +324,6
      This is expected.

    -+What is unexpected is that it will also crash.
    ++Unexpectedly, it also crashes. This is a bug, and the jury is
    ++still out there how to fix it best. See ticket #314 for details.

      Contact
3:  bedead < -:  ------- TO-UNDO
```

In this example, there are 3 old and 3 new commits, where the developer removed the 3rd, added a new one before the first two, and modified the commit message of the 2nd commit as well as its diff.
When the output goes to a terminal, it is color-coded by default, just like regular `git` `diff`'s output. In addition, the first line (adding a commit) is green, the last line (deleting a commit) is red, the second line (with a perfect match) is yellow like the commit header of `git` `show`'s output, and the third line colors the old commit red, the new one green and the rest like `git` `show`'s commit header.
A naive color-coded diff of diffs is actually a bit hard to read, though, as it colors the entire lines red or green. The line that added "What is unexpected" in the old commit, for example, is completely red, even if the intent of the old commit was to add something.
To help with that, `range` uses the `--dual-color` mode by default. In this mode, the diff of diffs will retain the original diff colors, and prefix the lines with -/+ markers that have their **background** red or green, to make it more obvious that they describe how the diff itself changed.
##  [](https://git-scm.com/docs/git-range-diff#_algorithm)Algorithm
The general idea is this: we generate a cost matrix between the commits in both commit ranges, then solve the least-cost assignment.
The cost matrix is populated thusly: for each pair of commits, both diffs are generated and the "diff of diffs" is generated, with 3 context lines, then the number of lines in that diff is used as cost.
To avoid false positives (e.g. when a patch has been removed, and an unrelated patch has been added between two iterations of the same patch series), the cost matrix is extended to allow for that, by adding fixed-cost entries for wholesale deletes/adds.
Example: Let commits `1--2` be the first iteration of a patch series and `A--C` the second iteration. Let’s assume that `A` is a cherry-pick of `2,` and `C` is a cherry-pick of `1` but with a small modification (say, a fixed typo). Visualize the commits as a bipartite graph:
```
    1            A

    2            B

		 C
```

We are looking for a "best" explanation of the new series in terms of the old one. We can represent an "explanation" as an edge in the graph:
```
    1            A
	       /
    2 --------'  B

		 C
```

This explanation comes for "free" because there was no change. Similarly `C` could be explained using `1`, but that comes at some cost c>0 because of the modification:
```
    1 ----.      A
	  |    /
    2 ----+---'  B
	  |
	  `----- C
	  c>0
```

In mathematical terms, what we are looking for is some sort of a minimum cost bipartite matching; `1` is matched to `C` at some cost, etc. The underlying graph is in fact a complete bipartite graph; the cost we associate with every edge is the size of the diff between the two commits' patches. To explain also new commits, we introduce dummy nodes on both sides:
```
    1 ----.      A
	  |    /
    2 ----+---'  B
	  |
    o     `----- C
	  c>0
    o            o

    o            o
```

The cost of an edge `o--C` is the size of `C`'s diff, modified by a fudge factor that should be smaller than 100%. The cost of an edge `o--o` is free. The fudge factor is necessary because even if `1` and `C` have nothing in common, they may still share a few empty lines and such, possibly making the assignment `1--C`, `o--o` slightly cheaper than `1--o`, `o--C` even if `1` and `C` have nothing in common. With the fudge factor we require a much larger common part to consider patches as corresponding.
The overall time needed to compute this algorithm is the time needed to compute n+m commit diffs and then n*m diffs of patches, plus the time needed to compute the least-cost assignment between n and m diffs. Git uses an implementation of the Jonker-Volgenant algorithm to solve the assignment problem, which has cubic runtime complexity. The matching found in this case will look like this:
```
    1 ----.      A
	  |    /
    2 ----+---'  B
       .--+-----'
    o -'  `----- C
	  c>0
    o ---------- o

    o ---------- o
```

##  [](https://git-scm.com/docs/git-range-diff#_see_also)SEE ALSO
[git-log[1]](https://git-scm.com/docs/git-log)
##  [](https://git-scm.com/docs/git-range-diff#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### range-diff
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
