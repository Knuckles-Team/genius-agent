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
    * [NAME](https://git-scm.com/docs/git-update-ref#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-update-ref#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-update-ref#_description)
    * [LOGGING UPDATES](https://git-scm.com/docs/git-update-ref#_logging_updates)
    * [NOTES](https://git-scm.com/docs/git-update-ref#_notes)
    * [SEE ALSO](https://git-scm.com/docs/git-update-ref#_see_also)
    * [GIT](https://git-scm.com/docs/git-update-ref#_git)


[ English ▾](https://git-scm.com/docs/git-update-ref)
Localized versions of **git-update-ref** manual
  1. [English ](https://git-scm.com/docs/git-update-ref)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-update-ref/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-update-ref/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-update-ref/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-update-ref)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-update-ref) git-update-ref last updated in 2.53.0
Changes in the **git-update-ref** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git-update-ref/2.53.0)
  2. 2.50.1 → 2.52.0 no changes
  3. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-update-ref/2.50.0)
  4. 2.48.1 → 2.49.1 no changes
  5. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git-update-ref/2.48.0)
  6. 2.46.1 → 2.47.3 no changes
  7. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-update-ref/2.46.0)
  8. 2.45.1 → 2.45.4 no changes
  9. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git-update-ref/2.45.0)
  10. 2.43.1 → 2.44.4 no changes
  11. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-update-ref/2.43.0)
  12. 2.30.1 → 2.42.4 no changes
  13. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git-update-ref/2.30.0)
  14. 2.29.1 → 2.29.3 no changes
  15. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-update-ref/2.29.0)
  16. 2.27.1 → 2.28.1 no changes
  17. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-update-ref/2.27.0)
  18. 2.19.3 → 2.26.3 no changes
  19. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git-update-ref/2.19.2)
  20. 2.18.1 → 2.19.1 no changes
  21. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-update-ref/2.18.0)
  22. 2.7.6 → 2.17.6 no changes
  23. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-update-ref/2.6.7)
  24. 2.2.3 → 2.5.6 no changes
  25. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-update-ref/2.1.4)
  26. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-update-ref/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-update-ref#_name)NAME
git-update-ref - Update the object name stored in a ref safely
##  [](https://git-scm.com/docs/git-update-ref#_synopsis)SYNOPSIS
```
git update-ref [-m _<reason>_] [--no-deref] -d _<ref>_ [_<old-oid>_]
git update-ref [-m _<reason>_] [--no-deref] [--create-reflog] _<ref>_ _<new-oid>_ [_<old-oid>_]
git update-ref [-m _<reason>_] [--no-deref] --stdin [-z] [--batch-updates]
```

##  [](https://git-scm.com/docs/git-update-ref#_description)DESCRIPTION
Given two arguments, stores the <new-oid> in the <ref>, possibly dereferencing the symbolic refs. E.g. `git` `update-ref` `HEAD` _< new-oid>_ updates the current branch head to the new object.
Given three arguments, stores the <new-oid> in the <ref>, possibly dereferencing the symbolic refs, after verifying that the current value of the <ref> matches <old-oid>. E.g. `git` `update-ref` `refs/heads/master` _< new-oid>_ _< old-oid>_ updates the master branch head to <new-oid> only if its current value is <old-oid>. You can specify 40 "0" or an empty string as <old-oid> to make sure that the ref you are creating does not exist.
The final arguments are object names; this command without any options does not support updating a symbolic ref to point to another ref (see [git-symbolic-ref[1]](https://git-scm.com/docs/git-symbolic-ref)). But `git` `update-ref` `--stdin` does have the `symref-*` commands so that regular refs and symbolic refs can be committed in the same transaction.
If --no-deref is given, <ref> itself is overwritten, rather than the result of following the symbolic pointers.
With `-d`, it deletes the named <ref> after verifying that it still contains <old-oid>.
With `--stdin`, update-ref reads instructions from standard input and performs all modifications together. Specify commands of the form:
```
update SP <ref> SP <new-oid> [SP <old-oid>] LF
create SP <ref> SP <new-oid> LF
delete SP <ref> [SP <old-oid>] LF
verify SP <ref> [SP <old-oid>] LF
symref-update SP <ref> SP <new-target> [SP (ref SP <old-target> | oid SP <old-oid>)] LF
symref-create SP <ref> SP <new-target> LF
symref-delete SP <ref> [SP <old-target>] LF
symref-verify SP <ref> [SP <old-target>] LF
option SP <opt> LF
start LF
prepare LF
commit LF
abort LF
```

With `--create-reflog`, update-ref will create a reflog for each ref even if one would not ordinarily be created.
With `--batch-updates`, update-ref executes the updates in a batch but allows individual updates to fail due to invalid or incorrect user input, applying only the successful updates. However, system-related errors—such as I/O failures or memory issues—will result in a full failure of all batched updates. Any failed updates will be reported in the following format:
```
rejected SP (<old-oid> | <old-target>) SP (<new-oid> | <new-target>) SP <rejection-reason> LF
```

Quote fields containing whitespace as if they were strings in C source code; i.e., surrounded by double-quotes and with backslash escapes. Use 40 "0" characters or the empty string to specify a zero value. To specify a missing value, omit the value and its preceding SP entirely.
Alternatively, use `-z` to specify in NUL-terminated format, without quoting:
```
update SP <ref> NUL <new-oid> NUL [<old-oid>] NUL
create SP <ref> NUL <new-oid> NUL
delete SP <ref> NUL [<old-oid>] NUL
verify SP <ref> NUL [<old-oid>] NUL
symref-update SP <ref> NUL <new-target> [NUL (ref NUL <old-target> | oid NUL <old-oid>)] NUL
symref-create SP <ref> NUL <new-target> NUL
symref-delete SP <ref> [NUL <old-target>] NUL
symref-verify SP <ref> [NUL <old-target>] NUL
option SP <opt> NUL
start NUL
prepare NUL
commit NUL
abort NUL
```

In this format, use 40 "0" to specify a zero value, and use the empty string to specify a missing value.
In either format, values can be specified in any form that Git recognizes as an object name. Commands in any other format or a repeated <ref> produce an error. Command meanings are: 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-update)update 
    
Set <ref> to <new-oid> after verifying <old-oid>, if given. Specify a zero <new-oid> to ensure the ref does not exist after the update and/or a zero <old-oid> to make sure the ref does not exist before the update. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-create)create 
    
Create <ref> with <new-oid> after verifying that it does not exist. The given <new-oid> may not be zero. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-delete)delete 
    
Delete <ref> after verifying that it exists with <old-oid>, if given. If given, <old-oid> may not be zero. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-symref-update)symref-update 
    
Set <ref> to <new-target> after verifying <old-target> or <old-oid>, if given. Specify a zero <old-oid> to ensure that the ref does not exist before the update. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-verify)verify 
    
Verify <ref> against <old-oid> but do not change it. If <old-oid> is zero or missing, the ref must not exist. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-symref-create)symref-create 
    
Create symbolic ref <ref> with <new-target> after verifying that it does not exist. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-symref-delete)symref-delete 
    
Delete <ref> after verifying that it exists with <old-target>, if given. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-symref-verify)symref-verify 
    
Verify symbolic <ref> against <old-target> but do not change it. If <old-target> is missing, the ref must not exist. Can only be used in `no-deref` mode. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-option)option 
    
Modify the behavior of the next command naming a <ref>. The only valid option is `no-deref` to avoid dereferencing a symbolic ref. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-start)start 
    
Start a transaction. In contrast to a non-transactional session, a transaction will automatically abort if the session ends without an explicit commit. This command may create a new empty transaction when the current one has been committed or aborted already. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-prepare)prepare 
    
Prepare to commit the transaction. This will create lock files for all queued reference updates. If one reference could not be locked, the transaction will be aborted. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-commit)commit 
    
Commit all reference updates queued for the transaction, ending the transaction. 

[](https://git-scm.com/docs/git-update-ref#Documentation/git-update-ref.txt-abort)abort 
    
Abort the transaction, releasing all locks if the transaction is in prepared state.
If all <ref>s can be locked with matching <old-oid>s simultaneously, all modifications are performed. Otherwise, no modifications are performed. Note that while each individual <ref> is updated or deleted atomically, a concurrent reader may still see a subset of the modifications.
##  [](https://git-scm.com/docs/git-update-ref#_logging_updates)LOGGING UPDATES
If config parameter "core.logAllRefUpdates" is true and the ref is one under "refs/heads/", "refs/remotes/", "refs/notes/", or a pseudoref like HEAD or ORIG_HEAD; or the file "$GIT_DIR/logs/<ref>" exists then `git` `update-ref` will append a line to the log file "$GIT_DIR/logs/<ref>" (dereferencing all symbolic refs before creating the log name) describing the change in ref value. Log lines are formatted as:
```
oldsha1 SP newsha1 SP committer LF
```

Where "oldsha1" is the 40 character hexadecimal value previously stored in <ref>, "newsha1" is the 40 character hexadecimal value of <new-oid> and "committer" is the committer’s name, email address and date in the standard Git committer ident format.
Optionally with -m:
```
oldsha1 SP newsha1 SP committer TAB message LF
```

Where all fields are as described above and "message" is the value supplied to the -m option.
An update will fail (without changing <ref>) if the current user is unable to create a new log file, append to the existing log file or does not have committer information available.
##  [](https://git-scm.com/docs/git-update-ref#_notes)NOTES
Symbolic refs were initially implemented using symbolic links. This is now deprecated since not all filesystems support symbolic links.
This command follows **real** symlinks only if they start with "refs/": otherwise it will just try to read them and update them as a regular file (i.e. it will allow the filesystem to follow them, but will overwrite such a symlink to somewhere else with a regular filename).
##  [](https://git-scm.com/docs/git-update-ref#_see_also)SEE ALSO
[git-symbolic-ref[1]](https://git-scm.com/docs/git-symbolic-ref)
##  [](https://git-scm.com/docs/git-update-ref#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### update-ref
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
