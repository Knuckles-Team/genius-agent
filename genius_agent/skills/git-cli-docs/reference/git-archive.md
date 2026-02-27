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
    * [NAME](https://git-scm.com/docs/git-archive#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-archive#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-archive#_description)
    * [OPTIONS](https://git-scm.com/docs/git-archive#_options)
    * [BACKEND EXTRA OPTIONS](https://git-scm.com/docs/git-archive#_backend_extra_options)
    * [CONFIGURATION](https://git-scm.com/docs/git-archive#_configuration)
    * [ATTRIBUTES](https://git-scm.com/docs/git-archive#ATTRIBUTES)
    * [EXAMPLES](https://git-scm.com/docs/git-archive#_examples)
    * [SEE ALSO](https://git-scm.com/docs/git-archive#_see_also)
    * [GIT](https://git-scm.com/docs/git-archive#_git)


[ English ▾](https://git-scm.com/docs/git-archive)
Localized versions of **git-archive** manual
  1. [English ](https://git-scm.com/docs/git-archive)
  2. [Français ](https://git-scm.com/docs/git-archive/fr)
  3. [Português (Brasil) ](https://git-scm.com/docs/git-archive/pt_BR)
  4. [Svenska ](https://git-scm.com/docs/git-archive/sv)
  5. [українська мова ](https://git-scm.com/docs/git-archive/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-archive/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-archive)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-archive) git-archive last updated in 2.46.0
Changes in the **git-archive** manual
  1. 2.46.1 → 2.53.0 no changes
  2. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-archive/2.46.0)
  3. 2.43.1 → 2.45.4 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-archive/2.43.0)
  5. 2.40.1 → 2.42.4 no changes
  6. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-archive/2.40.0)
  7. 2.38.1 → 2.39.5 no changes
  8. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git-archive/2.38.0)
  9. 2.37.1 → 2.37.7 no changes
  10. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git-archive/2.37.0)
  11. 2.34.1 → 2.36.6 no changes
  12. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-archive/2.34.0)
  13. 2.29.1 → 2.33.8 no changes
  14. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git-archive/2.29.0)
  15. 2.1.4 → 2.28.1 no changes
  16. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-archive/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-archive#_name)NAME
git-archive - Create an archive of files from a named tree
##  [](https://git-scm.com/docs/git-archive#_synopsis)SYNOPSIS
```
_git archive_ [--format=<fmt>] [--list] [--prefix=<prefix>/] [<extra>]
	      [-o <file> | --output=<file>] [--worktree-attributes]
	      [--remote=<repo> [--exec=<git-upload-archive>]] <tree-ish>
	      [<path>…​]
```

##  [](https://git-scm.com/docs/git-archive#_description)DESCRIPTION
Creates an archive of the specified format containing the tree structure for the named tree, and writes it out to the standard output. If <prefix> is specified it is prepended to the filenames in the archive.
_git archive_ behaves differently when given a tree ID as opposed to a commit ID or tag ID. When a tree ID is provided, the current time is used as the modification time of each file in the archive. On the other hand, when a commit ID or tag ID is provided, the commit time as recorded in the referenced commit object is used instead. Additionally the commit ID is stored in a global extended pax header if the tar format is used; it can be extracted using _git get-tar-commit-id_. In ZIP files it is stored as a file comment.
##  [](https://git-scm.com/docs/git-archive#_options)OPTIONS 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---formatfmt)--format=<fmt> 
    
Format of the resulting archive. Possible values are `tar`, `zip`, `tar.gz`, `tgz`, and any format defined using the configuration option `tar.`_< format>_`.command`. If `--format` is not given, and the output file is specified, the format is inferred from the filename if possible (e.g. writing to `foo.zip` makes the output to be in the `zip` format). Otherwise the output format is `tar`. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt--l)-l 


[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---list)--list 
    
Show all available formats. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt--v)-v 


[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---verbose)--verbose 
    
Report progress to stderr. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---prefixprefix)--prefix=<prefix>/ 
    
Prepend <prefix>/ to paths in the archive. Can be repeated; its rightmost value is used for all tracked files. See below which value gets used by `--add-file`. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt--ofile)-o <file> 


[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---outputfile)--output=<file> 
    
Write the archive to <file> instead of stdout. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---add-filefile)--add-file=<file> 
    
Add a non-tracked file to the archive. Can be repeated to add multiple files. The path of the file in the archive is built by concatenating the value of the last `--prefix` option (if any) before this `--add-file` and the basename of <file>. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---add-virtual-filepathcontent)--add-virtual-file=<path>:<content> 
    
Add the specified contents to the archive. Can be repeated to add multiple files.
The _< path>_ argument can start and end with a literal double-quote character; the contained file name is interpreted as a C-style string, i.e. the backslash is interpreted as escape character. The path must be quoted if it contains a colon, to avoid the colon from being misinterpreted as the separator between the path and the contents, or if the path begins or ends with a double-quote character.
The file mode is limited to a regular file, and the option may be subject to platform-dependent command-line limits. For non-trivial cases, write an untracked file and use `--add-file` instead.
Note that unlike `--add-file` the path created in the archive is not affected by the `--prefix` option, as a full _< path>_ can be given as the value of the option. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---worktree-attributes)--worktree-attributes 
    
Look for attributes in .gitattributes files in the working tree as well (see [ATTRIBUTES](https://git-scm.com/docs/git-archive#ATTRIBUTES)). 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---mtimetime)--mtime=<time> 
    
Set modification time of archive entries. Without this option the committer time is used if _< tree-ish>_ is a commit or tag, and the current time if it is a tree. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-extra)<extra> 
    
This can be any options that the archiver backend understands. See next section. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---remoterepo)--remote=<repo> 
    
Instead of making a tar archive from the local repository, retrieve a tar archive from a remote repository. Note that the remote repository may place restrictions on which sha1 expressions may be allowed in _< tree-ish>_. See [git-upload-archive[1]](https://git-scm.com/docs/git-upload-archive) for details. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt---execgit-upload-archive)--exec=<git-upload-archive> 
    
Used with --remote to specify the path to the _git-upload-archive_ on the remote side. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-tree-ish)<tree-ish> 
    
The tree or commit to produce an archive for. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-path)<path> 
    
Without an optional path parameter, all files and subdirectories of the current working directory are included in the archive. If one or more paths are specified, only these are included.
##  [](https://git-scm.com/docs/git-archive#_backend_extra_options)BACKEND EXTRA OPTIONS
###  [](https://git-scm.com/docs/git-archive#_zip)zip 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt--digit)-<digit> 
    
Specify compression level. Larger values allow the command to spend more time to compress to smaller size. Supported values are from `-0` (store-only) to `-9` (best ratio). Default is `-6` if not given.
###  [](https://git-scm.com/docs/git-archive#_tar)tar 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt--number)-<number> 
    
Specify compression level. The value will be passed to the compression command configured in `tar.`_< format>_`.command`. See manual page of the configured command for the list of supported levels and the default level if this option isn’t specified.
##  [](https://git-scm.com/docs/git-archive#_configuration)CONFIGURATION 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-tarumask)tar.umask 
    
This variable can be used to restrict the permission bits of tar archive entries. The default is 0002, which turns off the world write bit. The special value "user" indicates that the archiving user’s umask will be used instead. See umask(2) for details. If `--remote` is used then only the configuration of the remote repository takes effect. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-tarformatcommand)tar.<format>.command 
    
This variable specifies a shell command through which the tar output generated by `git` `archive` should be piped. The command is executed using the shell with the generated tar file on its standard input, and should produce the final output on its standard output. Any compression-level options will be passed to the command (e.g., `-9`).
The `tar.gz` and `tgz` formats are defined automatically and use the magic command `git` `archive` `gzip` by default, which invokes an internal implementation of gzip. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-tarformatremote)tar.<format>.remote 
    
If true, enable the format for use by remote clients via [git-upload-archive[1]](https://git-scm.com/docs/git-upload-archive). Defaults to false for user-defined formats, but true for the `tar.gz` and `tgz` formats.
##  [](https://git-scm.com/docs/git-archive#ATTRIBUTES)ATTRIBUTES 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-export-ignore)export-ignore 
    
Files and directories with the attribute export-ignore won’t be added to archive files. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-export-subst)export-subst 
    
If the attribute export-subst is set for a file then Git will expand several placeholders when adding this file to an archive. See [gitattributes[5]](https://git-scm.com/docs/gitattributes) for details.
Note that attributes are by default taken from the `.gitattributes` files in the tree that is being archived. If you want to tweak the way the output is generated after the fact (e.g. you committed without adding an appropriate export-ignore in its `.gitattributes`), adjust the checked out `.gitattributes` file as necessary and use `--worktree-attributes` option. Alternatively you can keep necessary attributes that should apply while archiving any tree in your `$GIT_DIR/info/attributes` file.
##  [](https://git-scm.com/docs/git-archive#_examples)EXAMPLES 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive--formattar--prefixjunkHEADcdvartmptarxf-)_git archive --format=tar --prefix=junk/ HEAD | (cd /var/tmp/ && tar xf -)_ 
    
Create a tar archive that contains the contents of the latest commit on the current branch, and extract it in the `/var/tmp/junk` directory. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive--formattar--prefixgit-140v140gzipgit-140targz)_git archive --format=tar --prefix=git-1.4.0/ v1.4.0 | gzip >git-1.4.0.tar.gz_ 
    
Create a compressed tarball for v1.4.0 release. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive--formattargz--prefixgit-140v140git-140targz)_git archive --format=tar.gz --prefix=git-1.4.0/ v1.4.0 >git-1.4.0.tar.gz_ 
    
Same as above, but using the builtin tar.gz handling. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive--prefixgit-140-ogit-140targzv140)`git` `archive` `--prefix=git-1.4.0/` `-o` `git-1.4.0.tar.gz` `v1.4.0` 
    
Same as above, but the format is inferred from the output file. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive--formattar--prefixgit-140v140treegzipgit-140targz)_git archive --format=tar --prefix=git-1.4.0/ v1.4.0^{tree} | gzip >git-1.4.0.tar.gz_ 
    
Create a compressed tarball for v1.4.0 release, but without a global extended pax header. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive--formatzip--prefixgit-docsHEADDocumentationgit-140-docszip)_git archive --format=zip --prefix=git-docs/ HEAD:Documentation/ > git-1.4.0-docs.zip_ 
    
Put everything in the current head’s Documentation/ directory into _git-1.4.0-docs.zip_ , with the prefix _git-docs/_. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive-olatestzipHEAD)`git` `archive` `-o` `latest.zip` `HEAD` 
    
Create a Zip archive that contains the contents of the latest commit on the current branch. Note that the output format is inferred by the extension of the output file. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitarchive-olatesttar--prefixbuild--add-fileconfigure--prefixHEAD)`git` `archive` `-o` `latest.tar` `--prefix=build/` `--add-file=configure` `--prefix=` `HEAD` 
    
Creates a tar archive that contains the contents of the latest commit on the current branch with no prefix and the untracked file _configure_ with the prefix _build/_. 

[](https://git-scm.com/docs/git-archive#Documentation/git-archive.txt-gitconfigtartarxzcommandxz-c)`git` `config` `tar.tar.xz.command` `"xz` `-c"` 
    
Configure a "tar.xz" format for making LZMA-compressed tarfiles. You can use it specifying `--format=tar.xz`, or by creating an output file like `-o` `foo.tar.xz`.
##  [](https://git-scm.com/docs/git-archive#_see_also)SEE ALSO
[gitattributes[5]](https://git-scm.com/docs/gitattributes)
##  [](https://git-scm.com/docs/git-archive#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### archive
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
