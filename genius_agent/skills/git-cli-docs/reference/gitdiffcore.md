[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --distributed-even-if-your-workflow-isnt
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
    * [NAME](https://git-scm.com/docs/gitdiffcore#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitdiffcore#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitdiffcore#_description)
    * [The chain of operation](https://git-scm.com/docs/gitdiffcore#_the_chain_of_operation)
    * [diffcore-break: For Splitting Up Complete Rewrites](https://git-scm.com/docs/gitdiffcore#_diffcore_break_for_splitting_up_complete_rewrites)
    * [diffcore-rename: For Detecting Renames and Copies](https://git-scm.com/docs/gitdiffcore#_diffcore_rename_for_detecting_renames_and_copies)
    * [diffcore-merge-broken: For Putting Complete Rewrites Back Together](https://git-scm.com/docs/gitdiffcore#_diffcore_merge_broken_for_putting_complete_rewrites_back_together)
    * [diffcore-pickaxe: For Detecting Addition/Deletion of Specified String](https://git-scm.com/docs/gitdiffcore#_diffcore_pickaxe_for_detecting_additiondeletion_of_specified_string)
    * [diffcore-order: For Sorting the Output Based on Filenames](https://git-scm.com/docs/gitdiffcore#_diffcore_order_for_sorting_the_output_based_on_filenames)
    * [diffcore-rotate: For Changing At Which Path Output Starts](https://git-scm.com/docs/gitdiffcore#_diffcore_rotate_for_changing_at_which_path_output_starts)
    * [SEE ALSO](https://git-scm.com/docs/gitdiffcore#_see_also)
    * [GIT](https://git-scm.com/docs/gitdiffcore#_git)


[ English ▾](https://git-scm.com/docs/gitdiffcore)
Localized versions of **gitdiffcore** manual
  1. [English ](https://git-scm.com/docs/gitdiffcore)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitdiffcore)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitdiffcore) gitdiffcore last updated in 2.44.0
Changes in the **gitdiffcore** manual
  1. 2.44.1 → 2.53.0 no changes
  2. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/gitdiffcore/2.44.0)
  3. 2.43.1 → 2.43.7 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/gitdiffcore/2.43.0)
  5. 2.32.1 → 2.42.4 no changes
  6. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/gitdiffcore/2.32.0)
  7. 2.31.1 → 2.31.8 no changes
  8. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/gitdiffcore/2.31.0)
  9. 2.21.1 → 2.30.9 no changes
  10. [2.21.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-02-24_ ](https://git-scm.com/docs/gitdiffcore/2.21.0)
  11. 2.13.7 → 2.20.5 no changes
  12. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/gitdiffcore/2.12.5)
  13. 2.10.5 → 2.11.4 no changes
  14. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/gitdiffcore/2.9.5)
  15. 2.5.6 → 2.8.6 no changes
  16. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/gitdiffcore/2.4.12)
  17. 2.1.4 → 2.3.10 no changes
  18. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/gitdiffcore/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitdiffcore#_name)NAME
gitdiffcore - Tweaking diff output
##  [](https://git-scm.com/docs/gitdiffcore#_synopsis)SYNOPSIS
```
_git diff_ *
```

##  [](https://git-scm.com/docs/gitdiffcore#_description)DESCRIPTION
The diff commands _git diff-index_ , _git diff-files_ , and _git diff-tree_ can be told to manipulate differences they find in unconventional ways before showing _diff_ output. The manipulation is collectively called "diffcore transformation". This short note describes what they are and how to use them to produce _diff_ output that is easier to understand than the conventional kind.
##  [](https://git-scm.com/docs/gitdiffcore#_the_chain_of_operation)The chain of operation
The _git diff-*_ family works by first comparing two sets of files:
  * _git diff-index_ compares contents of a "tree" object and the working directory (when `--cached` flag is not used) or a "tree" object and the index file (when `--cached` flag is used);
  * _git diff-files_ compares contents of the index file and the working directory;
  * _git diff-tree_ compares contents of two "tree" objects;


In all of these cases, the commands themselves first optionally limit the two sets of files by any pathspecs given on their command-lines, and compare corresponding paths in the two resulting sets of files.
The pathspecs are used to limit the world diff operates in. They remove the filepairs outside the specified sets of pathnames. E.g. If the input set of filepairs included:
```
:100644 100644 bcd1234... 0123456... M junkfile
```

but the command invocation was `git` `diff-files` `myfile`, then the junkfile entry would be removed from the list because only "myfile" is under consideration.
The result of comparison is passed from these commands to what is internally called "diffcore", in a format similar to what is output when the -p option is not used. E.g.
```
in-place edit  :100644 100644 bcd1234... 0123456... M file0
create         :000000 100644 0000000... 1234567... A file4
delete         :100644 000000 1234567... 0000000... D file5
unmerged       :000000 000000 0000000... 0000000... U file6
```

The diffcore mechanism is fed a list of such comparison results (each of which is called "filepair", although at this point each of them talks about a single file), and transforms such a list into another list. There are currently 5 such transformations:
  * diffcore-break
  * diffcore-rename
  * diffcore-merge-broken
  * diffcore-pickaxe
  * diffcore-order
  * diffcore-rotate


These are applied in sequence. The set of filepairs _git diff-*_ commands find are used as the input to diffcore-break, and the output from diffcore-break is used as the input to the next transformation. The final result is then passed to the output routine and generates either diff-raw format (see Output format sections of the manual for _git diff-*_ commands) or diff-patch format.
##  [](https://git-scm.com/docs/gitdiffcore#_diffcore_break_for_splitting_up_complete_rewrites)diffcore-break: For Splitting Up Complete Rewrites
The second transformation in the chain is diffcore-break, and is controlled by the -B option to the _git diff-*_ commands. This is used to detect a filepair that represents "complete rewrite" and break such filepair into two filepairs that represent delete and create. E.g. If the input contained this filepair:
```
:100644 100644 bcd1234... 0123456... M file0
```

and if it detects that the file "file0" is completely rewritten, it changes it to:
```
:100644 000000 bcd1234... 0000000... D file0
:000000 100644 0000000... 0123456... A file0
```

For the purpose of breaking a filepair, diffcore-break examines the extent of changes between the contents of the files before and after modification (i.e. the contents that have "bcd1234…​" and "0123456…​" as their SHA-1 content ID, in the above example). The amount of deletion of original contents and insertion of new material are added together, and if it exceeds the "break score", the filepair is broken into two. The break score defaults to 50% of the size of the smaller of the original and the result (i.e. if the edit shrinks the file, the size of the result is used; if the edit lengthens the file, the size of the original is used), and can be customized by giving a number after "-B" option (e.g. "-B75" to tell it to use 75%).
##  [](https://git-scm.com/docs/gitdiffcore#_diffcore_rename_for_detecting_renames_and_copies)diffcore-rename: For Detecting Renames and Copies
This transformation is used to detect renames and copies, and is controlled by the -M option (to detect renames) and the -C option (to detect copies as well) to the _git diff-*_ commands. If the input contained these filepairs:
```
:100644 000000 0123456... 0000000... D fileX
:000000 100644 0000000... 0123456... A file0
```

and the contents of the deleted file fileX is similar enough to the contents of the created file file0, then rename detection merges these filepairs and creates:
```
:100644 100644 0123456... 0123456... R100 fileX file0
```

When the "-C" option is used, the original contents of modified files, and deleted files (and also unmodified files, if the "--find-copies-harder" option is used) are considered as candidates of the source files in rename/copy operation. If the input were like these filepairs, that talk about a modified file fileY and a newly created file file0:
```
:100644 100644 0123456... 1234567... M fileY
:000000 100644 0000000... bcd3456... A file0
```

the original contents of fileY and the resulting contents of file0 are compared, and if they are similar enough, they are changed to:
```
:100644 100644 0123456... 1234567... M fileY
:100644 100644 0123456... bcd3456... C100 fileY file0
```

In both rename and copy detection, the same "extent of changes" algorithm used in diffcore-break is used to determine if two files are "similar enough", and can be customized to use a similarity score different from the default of 50% by giving a number after the "-M" or "-C" option (e.g. "-M8" to tell it to use 8/10 = 80%).
Note that when rename detection is on but both copy and break detection are off, rename detection adds a preliminary step that first checks if files are moved across directories while keeping their filename the same. If there is a file added to a directory whose contents are sufficiently similar to a file with the same name that got deleted from a different directory, it will mark them as renames and exclude them from the later quadratic step (the one that pairwise compares all unmatched files to find the "best" matches, determined by the highest content similarity). So, for example, if a deleted docs/ext.txt and an added docs/config/ext.txt are similar enough, they will be marked as a rename and prevent an added docs/ext.md that may be even more similar to the deleted docs/ext.txt from being considered as the rename destination in the later step. For this reason, the preliminary "match same filename" step uses a bit higher threshold to mark a file pair as a rename and stop considering other candidates for better matches. At most, one comparison is done per file in this preliminary pass; so if there are several remaining ext.txt files throughout the directory hierarchy after exact rename detection, this preliminary step may be skipped for those files.
Note. When the "-C" option is used with `--find-copies-harder` option, _git diff-*_ commands feed unmodified filepairs to diffcore mechanism as well as modified ones. This lets the copy detector consider unmodified files as copy source candidates at the expense of making it slower. Without `--find-copies-harder`, _git diff-*_ commands can detect copies only if the file that was copied happened to have been modified in the same changeset.
##  [](https://git-scm.com/docs/gitdiffcore#_diffcore_merge_broken_for_putting_complete_rewrites_back_together)diffcore-merge-broken: For Putting Complete Rewrites Back Together
This transformation is used to merge filepairs broken by diffcore-break, and not transformed into rename/copy by diffcore-rename, back into a single modification. This always runs when diffcore-break is used.
For the purpose of merging broken filepairs back, it uses a different "extent of changes" computation from the ones used by diffcore-break and diffcore-rename. It counts only the deletion from the original, and does not count insertion. If you removed only 10 lines from a 100-line document, even if you added 910 new lines to make a new 1000-line document, you did not do a complete rewrite. diffcore-break breaks such a case in order to help diffcore-rename to consider such filepairs as a candidate of rename/copy detection, but if filepairs broken that way were not matched with other filepairs to create rename/copy, then this transformation merges them back into the original "modification".
The "extent of changes" parameter can be tweaked from the default 80% (that is, unless more than 80% of the original material is deleted, the broken pairs are merged back into a single modification) by giving a second number to -B option, like these:
  * -B50/60 (give 50% "break score" to diffcore-break, use 60% for diffcore-merge-broken).
  * -B/60 (the same as above, since diffcore-break defaults to 50%).


Note that earlier implementation left a broken pair as separate creation and deletion patches. This was an unnecessary hack, and the latest implementation always merges all the broken pairs back into modifications, but the resulting patch output is formatted differently for easier review in case of such a complete rewrite by showing the entire contents of the old version prefixed with _-_ , followed by the entire contents of the new version prefixed with _+_.
##  [](https://git-scm.com/docs/gitdiffcore#_diffcore_pickaxe_for_detecting_additiondeletion_of_specified_string)diffcore-pickaxe: For Detecting Addition/Deletion of Specified String
This transformation limits the set of filepairs to those that change specified strings between the preimage and the postimage in a certain way. -S<block-of-text> and -G<regular-expression> options are used to specify different ways these strings are sought.
"-S<block-of-text>" detects filepairs whose preimage and postimage have different number of occurrences of the specified block of text. By definition, it will not detect in-file moves. Also, when a changeset moves a file wholesale without affecting the interesting string, diffcore-rename kicks in as usual, and `-S` omits the filepair (since the number of occurrences of that string didn’t change in that rename-detected filepair). When used with `--pickaxe-regex`, treat the <block-of-text> as an extended POSIX regular expression to match, instead of a literal string.
"-G<regular-expression>" (mnemonic: grep) detects filepairs whose textual diff has an added or a deleted line that matches the given regular expression. This means that it will detect in-file (or what rename-detection considers the same file) moves, which is noise. The implementation runs diff twice and greps, and this can be quite expensive. To speed things up, binary files without textconv filters will be ignored.
When `-S` or `-G` are used without `--pickaxe-all`, only filepairs that match their respective criterion are kept in the output. When `--pickaxe-all` is used, if even one filepair matches their respective criterion in a changeset, the entire changeset is kept. This behavior is designed to make reviewing changes in the context of the whole changeset easier.
##  [](https://git-scm.com/docs/gitdiffcore#_diffcore_order_for_sorting_the_output_based_on_filenames)diffcore-order: For Sorting the Output Based on Filenames
This is used to reorder the filepairs according to the user’s (or project’s) taste, and is controlled by the -O option to the _git diff-*_ commands.
This takes a text file each of whose lines is a shell glob pattern. Filepairs that match a glob pattern on an earlier line in the file are output before ones that match a later line, and filepairs that do not match any glob pattern are output last.
As an example, a typical orderfile for the core Git probably would look like this:
```
README
Makefile
Documentation
*.h
*.c
t
```

##  [](https://git-scm.com/docs/gitdiffcore#_diffcore_rotate_for_changing_at_which_path_output_starts)diffcore-rotate: For Changing At Which Path Output Starts
This transformation takes one pathname, and rotates the set of filepairs so that the filepair for the given pathname comes first, optionally discarding the paths that come before it. This is used to implement the `--skip-to` and the `--rotate-to` options. It is an error when the specified pathname is not in the set of filepairs, but it is not useful to error out when used with "git log" family of commands, because it is unreasonable to expect that a given path would be modified by each and every commit shown by the "git log" command. For this reason, when used with "git log", the filepair that sorts the same as, or the first one that sorts after, the given pathname is where the output starts.
Use of this transformation combined with diffcore-order will produce unexpected results, as the input to this transformation is likely not sorted when diffcore-order is in effect.
##  [](https://git-scm.com/docs/gitdiffcore#_see_also)SEE ALSO
[git-diff[1]](https://git-scm.com/docs/git-diff), [git-diff-files[1]](https://git-scm.com/docs/git-diff-files), [git-diff-index[1]](https://git-scm.com/docs/git-diff-index), [git-diff-tree[1]](https://git-scm.com/docs/git-diff-tree), [git-format-patch[1]](https://git-scm.com/docs/git-format-patch), [git-log[1]](https://git-scm.com/docs/git-log), [gitglossary[7]](https://git-scm.com/docs/gitglossary), [The Git User’s Manual](https://git-scm.com/docs/user-manual)
##  [](https://git-scm.com/docs/gitdiffcore#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitdiffcore
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
