[![Git](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/) --distributed-is-the-new-centralized
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
    * [NAME](https://git-scm.com/docs/gitcvs-migration#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitcvs-migration#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitcvs-migration#_description)
    * [Developing against a shared repository](https://git-scm.com/docs/gitcvs-migration#_developing_against_a_shared_repository)
    * [Setting Up a Shared Repository](https://git-scm.com/docs/gitcvs-migration#_setting_up_a_shared_repository)
    * [Importing a CVS archive](https://git-scm.com/docs/gitcvs-migration#_importing_a_cvs_archive)
    * [Advanced Shared Repository Management](https://git-scm.com/docs/gitcvs-migration#_advanced_shared_repository_management)
    * [Providing CVS Access to a Git Repository](https://git-scm.com/docs/gitcvs-migration#_providing_cvs_access_to_a_git_repository)
    * [Alternative Development Models](https://git-scm.com/docs/gitcvs-migration#_alternative_development_models)
    * [SEE ALSO](https://git-scm.com/docs/gitcvs-migration#_see_also)
    * [GIT](https://git-scm.com/docs/gitcvs-migration#_git)


[ English ▾](https://git-scm.com/docs/gitcvs-migration)
Localized versions of **gitcvs-migration** manual
  1. [English ](https://git-scm.com/docs/gitcvs-migration)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitcvs-migration)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitcvs-migration) gitcvs-migration last updated in 2.12.5
Changes in the **gitcvs-migration** manual
  1. 2.13.7 → 2.53.0 no changes
  2. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/gitcvs-migration/2.12.5)
  3. 2.11.4 no changes
  4. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/gitcvs-migration/2.10.5)
  5. 2.3.10 → 2.9.5 no changes
  6. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/gitcvs-migration/2.2.3)
  7. 2.1.4 no changes
  8. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/gitcvs-migration/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitcvs-migration#_name)NAME
gitcvs-migration - Git for CVS users
##  [](https://git-scm.com/docs/gitcvs-migration#_synopsis)SYNOPSIS
```
_git cvsimport_ *
```

##  [](https://git-scm.com/docs/gitcvs-migration#_description)DESCRIPTION
Git differs from CVS in that every working tree contains a repository with a full copy of the project history, and no repository is inherently more important than any other. However, you can emulate the CVS model by designating a single shared repository which people can synchronize with; this document explains how to do that.
Some basic familiarity with Git is required. Having gone through [gittutorial[7]](https://git-scm.com/docs/gittutorial) and [gitglossary[7]](https://git-scm.com/docs/gitglossary) should be sufficient.
##  [](https://git-scm.com/docs/gitcvs-migration#_developing_against_a_shared_repository)Developing against a shared repository
Suppose a shared repository is set up in /pub/repo.git on the host foo.com. Then as an individual committer you can clone the shared repository over ssh with:
```
$ git clone foo.com:/pub/repo.git/ my-project
$ cd my-project
```

and hack away. The equivalent of _cvs update_ is
```
$ git pull origin
```

which merges in any work that others might have done since the clone operation. If there are uncommitted changes in your working tree, commit them first before running git pull.
Note |  The _pull_ command knows where to get updates from because of certain configuration variables that were set by the first _git clone_ command; see `git` `config` `-l` and the [git-config[1]](https://git-scm.com/docs/git-config) man page for details.  
---|---  
You can update the shared repository with your changes by first committing your changes, and then using the _git push_ command:
```
$ git push origin master
```

to "push" those commits to the shared repository. If someone else has updated the repository more recently, _git push_ , like _cvs commit_ , will complain, in which case you must pull any changes before attempting the push again.
In the _git push_ command above we specify the name of the remote branch to update (`master`). If we leave that out, _git push_ tries to update any branches in the remote repository that have the same name as a branch in the local repository. So the last _push_ can be done with either of:
```
$ git push origin
$ git push foo.com:/pub/project.git/
```

as long as the shared repository does not have any branches other than `master`.
##  [](https://git-scm.com/docs/gitcvs-migration#_setting_up_a_shared_repository)Setting Up a Shared Repository
We assume you have already created a Git repository for your project, possibly created from scratch or from a tarball (see [gittutorial[7]](https://git-scm.com/docs/gittutorial)), or imported from an already existing CVS repository (see the next section).
Assume your existing repo is at /home/alice/myproject. Create a new "bare" repository (a repository without a working tree) and fetch your project into it:
```
$ mkdir /pub/my-repo.git
$ cd /pub/my-repo.git
$ git --bare init --shared
$ git --bare fetch /home/alice/myproject master:master
```

Next, give every team member read/write access to this repository. One easy way to do this is to give all the team members ssh access to the machine where the repository is hosted. If you don’t want to give them a full shell on the machine, there is a restricted shell which only allows users to do Git pushes and pulls; see [git-shell[1]](https://git-scm.com/docs/git-shell).
Put all the committers in the same group, and make the repository writable by that group:
```
$ chgrp -R $group /pub/my-repo.git
```

Make sure committers have a umask of at most 027, so that the directories they create are writable and searchable by other group members.
##  [](https://git-scm.com/docs/gitcvs-migration#_importing_a_cvs_archive)Importing a CVS archive
Note |  These instructions use the `git-cvsimport` script which ships with git, but other importers may provide better results. See the note in [git-cvsimport[1]](https://git-scm.com/docs/git-cvsimport) for other options.   
---|---  
First, install version 2.1 or higher of cvsps from <https://github.com/andreyvit/cvsps> and make sure it is in your path. Then cd to a checked out CVS working directory of the project you are interested in and run [git-cvsimport[1]](https://git-scm.com/docs/git-cvsimport):
```
$ git cvsimport -C <destination> <module>
```

This puts a Git archive of the named CVS module in the directory <destination>, which will be created if necessary.
The import checks out from CVS every revision of every file. Reportedly cvsimport can average some twenty revisions per second, so for a medium-sized project this should not take more than a couple of minutes. Larger projects or remote repositories may take longer.
The main trunk is stored in the Git branch named `origin`, and additional CVS branches are stored in Git branches with the same names. The most recent version of the main trunk is also left checked out on the `master` branch, so you can start adding your own changes right away.
The import is incremental, so if you call it again next month it will fetch any CVS updates that have been made in the meantime. For this to work, you must not modify the imported branches; instead, create new branches for your own changes, and merge in the imported branches as necessary.
If you want a shared repository, you will need to make a bare clone of the imported directory, as described above. Then treat the imported directory as another development clone for purposes of merging incremental imports.
##  [](https://git-scm.com/docs/gitcvs-migration#_advanced_shared_repository_management)Advanced Shared Repository Management
Git allows you to specify scripts called "hooks" to be run at certain points. You can use these, for example, to send all commits to the shared repository to a mailing list. See [githooks[5]](https://git-scm.com/docs/githooks).
You can enforce finer grained permissions using update hooks. See [Controlling access to branches using update hooks](https://git-scm.com/docs/howto/update-hook-example).
##  [](https://git-scm.com/docs/gitcvs-migration#_providing_cvs_access_to_a_git_repository)Providing CVS Access to a Git Repository
It is also possible to provide true CVS access to a Git repository, so that developers can still use CVS; see [git-cvsserver[1]](https://git-scm.com/docs/git-cvsserver) for details.
##  [](https://git-scm.com/docs/gitcvs-migration#_alternative_development_models)Alternative Development Models
CVS users are accustomed to giving a group of developers commit access to a common repository. As we’ve seen, this is also possible with Git. However, the distributed nature of Git allows other development models, and you may want to first consider whether one of them might be a better fit for your project.
For example, you can choose a single person to maintain the project’s primary public repository. Other developers then clone this repository and each work in their own clone. When they have a series of changes that they’re happy with, they ask the maintainer to pull from the branch containing the changes. The maintainer reviews their changes and pulls them into the primary repository, which other developers pull from as necessary to stay coordinated. The Linux kernel and other projects use variants of this model.
With a small group, developers may just pull changes from each other’s repositories without the need for a central maintainer.
##  [](https://git-scm.com/docs/gitcvs-migration#_see_also)SEE ALSO
[gittutorial[7]](https://git-scm.com/docs/gittutorial), [gittutorial-2[7]](https://git-scm.com/docs/gittutorial-2), [gitcore-tutorial[7]](https://git-scm.com/docs/gitcore-tutorial), [gitglossary[7]](https://git-scm.com/docs/gitglossary), [giteveryday[7]](https://git-scm.com/docs/giteveryday), [The Git User’s Manual](https://git-scm.com/docs/user-manual)
##  [](https://git-scm.com/docs/gitcvs-migration#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitcvs-migration
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
