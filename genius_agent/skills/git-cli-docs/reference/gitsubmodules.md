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
    * [NAME](https://git-scm.com/docs/gitsubmodules#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitsubmodules#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitsubmodules#_description)
    * [The configuration of submodules](https://git-scm.com/docs/gitsubmodules#_the_configuration_of_submodules)
    * [FORMS](https://git-scm.com/docs/gitsubmodules#_forms)
    * [ACTIVE SUBMODULES](https://git-scm.com/docs/gitsubmodules#_active_submodules)
    * [Workflow for a third party library](https://git-scm.com/docs/gitsubmodules#_workflow_for_a_third_party_library)
    * [Workflow for an artificially split repo](https://git-scm.com/docs/gitsubmodules#_workflow_for_an_artificially_split_repo)
    * [Implementation details](https://git-scm.com/docs/gitsubmodules#_implementation_details)
    * [SEE ALSO](https://git-scm.com/docs/gitsubmodules#_see_also)
    * [GIT](https://git-scm.com/docs/gitsubmodules#_git)


[ English ▾](https://git-scm.com/docs/gitsubmodules)
Localized versions of **gitsubmodules** manual
  1. [English ](https://git-scm.com/docs/gitsubmodules)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitsubmodules)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitsubmodules) gitsubmodules last updated in 2.52.0
Changes in the **gitsubmodules** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/gitsubmodules/2.52.0)
  3. 2.44.1 → 2.51.2 no changes
  4. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/gitsubmodules/2.44.0)
  5. 2.43.1 → 2.43.7 no changes
  6. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/gitsubmodules/2.43.0)
  7. 2.35.1 → 2.42.4 no changes
  8. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/gitsubmodules/2.35.0)
  9. 2.29.1 → 2.34.8 no changes
  10. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/gitsubmodules/2.29.0)
  11. 2.27.1 → 2.28.1 no changes
  12. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/gitsubmodules/2.27.0)
  13. 2.25.1 → 2.26.3 no changes
  14. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/gitsubmodules/2.25.0)
  15. 2.22.1 → 2.24.4 no changes
  16. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/gitsubmodules/2.22.0)
  17. 2.19.3 → 2.21.4 no changes
  18. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/gitsubmodules/2.19.2)
  19. 2.19.1 no changes
  20. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/gitsubmodules/2.19.0)
  21. 2.17.0 → 2.18.5 no changes
  22. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/gitsubmodules/2.16.6)
  23. 2.15.4 no changes
  24. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/gitsubmodules/2.14.6)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitsubmodules#_name)NAME
gitsubmodules - Mounting one repository inside another
##  [](https://git-scm.com/docs/gitsubmodules#_synopsis)SYNOPSIS
```
.gitmodules, $GIT_DIR/config
```

```
git submodule
git <command> --recurse-submodules
```

##  [](https://git-scm.com/docs/gitsubmodules#_description)DESCRIPTION
A submodule is a repository embedded inside another repository. The submodule has its own history; the repository it is embedded in is called a superproject.
On the filesystem, a submodule usually (but not always - see FORMS below) consists of (i) a Git directory located under the `$GIT_DIR/modules/` directory of its superproject, (ii) a working directory inside the superproject’s working directory, and a `.git` file at the root of the submodule’s working directory pointing to (i).
Assuming the submodule has a Git directory at `$GIT_DIR/modules/foo/` and a working directory at `path/to/bar/`, the superproject tracks the submodule via a `gitlink` entry in the tree at `path/to/bar` and an entry in its `.gitmodules` file (see [gitmodules[5]](https://git-scm.com/docs/gitmodules)) of the form `submodule.foo.path` `=` `path/to/bar`.
The `gitlink` entry contains the object name of the commit that the superproject expects the submodule’s working directory to be at.
The section `submodule.foo.*` in the `.gitmodules` file gives additional hints to Git’s porcelain layer. For example, the `submodule.foo.url` setting specifies where to obtain the submodule.
Submodules can be used for at least two different use cases:
  1. Using another project while maintaining independent history. Submodules allow you to contain the working tree of another project within your own working tree while keeping the history of both projects separate. Also, since submodules are fixed to an arbitrary version, the other project can be independently developed without affecting the superproject, allowing the superproject project to fix itself to new versions only when desired.
  2. Splitting a (logically single) project into multiple repositories and tying them back together. This can be used to overcome current limitations of Git’s implementation to have finer grained access:
     * Size of the Git repository: In its current form Git scales up poorly for large repositories containing content that is not compressed by delta computation between trees. For example, you can use submodules to hold large binary assets and these repositories can be shallowly cloned such that you do not have a large history locally.
     * Transfer size: In its current form Git requires the whole working tree present. It does not allow partial trees to be transferred in fetch or clone. If the project you work on consists of multiple repositories tied together as submodules in a superproject, you can avoid fetching the working trees of the repositories you are not interested in.
     * Access control: By restricting user access to submodules, this can be used to implement read/write policies for different users.


##  [](https://git-scm.com/docs/gitsubmodules#_the_configuration_of_submodules)The configuration of submodules
Submodule operations can be configured using the following mechanisms (from highest to lowest precedence):
  * The command line for those commands that support taking submodules as part of their pathspecs. Most commands have a boolean flag `--recurse-submodules` which specifies whether to recurse into submodules. Examples are `grep` and `checkout`. Some commands take enums, such as `fetch` and `push`, where you can specify how submodules are affected.
  * The configuration inside the submodule. This includes `$GIT_DIR/config` in the submodule, but also settings in the tree such as a `.gitattributes` or `.gitignore` files that specify behavior of commands inside the submodule.
For example an effect from the submodule’s `.gitignore` file would be observed when you run `git` `status` `--ignore-submodules=none` in the superproject. This collects information from the submodule’s working directory by running `status` in the submodule while paying attention to the `.gitignore` file of the submodule.
The submodule’s `$GIT_DIR/config` file would come into play when running `git` `push` `--recurse-submodules=check` in the superproject, as this would check if the submodule has any changes not published to any remote. The remotes are configured in the submodule as usual in the `$GIT_DIR/config` file.
  * The configuration file `$GIT_DIR/config` in the superproject. Git only recurses into active submodules (see "ACTIVE SUBMODULES" section below).
If the submodule is not yet initialized, then the configuration inside the submodule does not exist yet, so where to obtain the submodule from is configured here for example.
  * The `.gitmodules` file inside the superproject. A project usually uses this file to suggest defaults for the upstream collection of repositories for the mapping that is required between a submodule’s name and its path.
This file mainly serves as the mapping between the name and path of submodules in the superproject, such that the submodule’s Git directory can be located.
If the submodule has never been initialized, this is the only place where submodule configuration is found. It serves as the last fallback to specify where to obtain the submodule from.


##  [](https://git-scm.com/docs/gitsubmodules#_forms)FORMS
Submodules can take the following forms:
  * The basic form described in DESCRIPTION with a Git directory, a working directory, a `gitlink`, and a `.gitmodules` entry.
  * "Old-form" submodule: A working directory with an embedded `.git` directory, and the tracking `gitlink` and `.gitmodules` entry in the superproject. This is typically found in repositories generated using older versions of Git.
It is possible to construct these old form repositories manually.
When deinitialized or deleted (see below), the submodule’s Git directory is automatically moved to `$GIT_DIR/modules/`_< name>_`/` of the superproject.
  * Deinitialized submodule: A `gitlink`, and a `.gitmodules` entry, but no submodule working directory. The submodule’s Git directory may be there as after deinitializing the Git directory is kept around. The directory which is supposed to be the working directory is empty instead.
A submodule can be deinitialized by running `git` `submodule` `deinit`. Besides emptying the working directory, this command only modifies the superproject’s `$GIT_DIR/config` file, so the superproject’s history is not affected. This can be undone using `git` `submodule` `init`.
  * Deleted submodule: A submodule can be deleted by running _git rm <submodule-path> && git commit_. This can be undone using `git` `revert`.
The deletion removes the superproject’s tracking data, which are both the `gitlink` entry and the section in the `.gitmodules` file. The submodule’s working directory is removed from the file system, but the Git directory is kept around as it to make it possible to checkout past commits without requiring fetching from another repository.
To completely remove a submodule, manually delete `$GIT_DIR/modules/`_< name>_`/`.


##  [](https://git-scm.com/docs/gitsubmodules#_active_submodules)ACTIVE SUBMODULES
A submodule is considered active,
  1. if `submodule.`_< name>_`.active` is set to `true`
or
  2. if the submodule’s path matches the pathspec in `submodule.active`
or
  3. if `submodule.`_< name>_`.url` is set.


and these are evaluated in this order.
For example:
```
[submodule "foo"]
  active = false
  url = https://example.org/foo
[submodule "bar"]
  active = true
  url = https://example.org/bar
[submodule "baz"]
  url = https://example.org/baz
```

In the above config only the submodules _bar_ and _baz_ are active, _bar_ due to (1) and _baz_ due to (3). _foo_ is inactive because (1) takes precedence over (3)
Note that (3) is a historical artefact and will be ignored if the (1) and (2) specify that the submodule is not active. In other words, if we have a `submodule.`_< name>_`.active` set to `false` or if the submodule’s path is excluded in the pathspec in `submodule.active`, the url doesn’t matter whether it is present or not. This is illustrated in the example that follows.
```
[submodule "foo"]
  active = true
  url = https://example.org/foo
[submodule "bar"]
  url = https://example.org/bar
[submodule "baz"]
  url = https://example.org/baz
[submodule "bob"]
  ignore = true
[submodule]
  active = b*
  active = :(exclude) baz
```

In here all submodules except _baz_ (foo, bar, bob) are active. _foo_ due to its own active flag and all the others due to the submodule active pathspec, which specifies that any submodule starting with _b_ except _baz_ are also active, regardless of the presence of the .url field.
##  [](https://git-scm.com/docs/gitsubmodules#_workflow_for_a_third_party_library)Workflow for a third party library
```
# Add a submodule
git submodule add <URL> <path>
```

```
# Occasionally update the submodule to a new version:
git -C <path> checkout <new-version>
git add <path>
git commit -m "update submodule to new version"
```

```
# See the list of submodules in a superproject
git submodule status
```

```
# See FORMS on removing submodules
```

##  [](https://git-scm.com/docs/gitsubmodules#_workflow_for_an_artificially_split_repo)Workflow for an artificially split repo
```
# Enable recursion for relevant commands, such that
# regular commands recurse into submodules by default
git config --global submodule.recurse true
```

```
# Unlike most other commands below, clone still needs
# its own recurse flag:
git clone --recurse <URL> <directory>
cd <directory>
```

```
# Get to know the code:
git grep foo
git ls-files --recurse-submodules
```

Note |  `git` `ls-files` also requires its own `--recurse-submodules` flag.   
---|---  
```
# Get new code
git fetch
git pull --rebase
```

```
# Change worktree
git checkout
git reset
```

##  [](https://git-scm.com/docs/gitsubmodules#_implementation_details)Implementation details
When cloning or pulling a repository containing submodules the submodules will not be checked out by default; you can instruct `clone` to recurse into submodules. The `init` and `update` subcommands of `git` `submodule` will maintain submodules checked out and at an appropriate revision in your working tree. Alternatively you can set `submodule.recurse` to have `checkout` recurse into submodules (note that `submodule.recurse` also affects other Git commands, see [git-config[1]](https://git-scm.com/docs/git-config) for a complete list).
##  [](https://git-scm.com/docs/gitsubmodules#_see_also)SEE ALSO
[git-submodule[1]](https://git-scm.com/docs/git-submodule), [gitmodules[5]](https://git-scm.com/docs/gitmodules).
##  [](https://git-scm.com/docs/gitsubmodules#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitsubmodules
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
