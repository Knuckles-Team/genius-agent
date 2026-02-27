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
    * [NAME](https://git-scm.com/docs/git-credential#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-credential#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-credential#_description)
    * [TYPICAL USE OF GIT CREDENTIAL](https://git-scm.com/docs/git-credential#_typical_use_of_git_credential)
    * [INPUT/OUTPUT FORMAT](https://git-scm.com/docs/git-credential#IOFMT)
    * [CAPABILITY INPUT/OUTPUT FORMAT](https://git-scm.com/docs/git-credential#CAPA-IOFMT)
    * [GIT](https://git-scm.com/docs/git-credential#_git)


[ English ▾](https://git-scm.com/docs/git-credential)
Localized versions of **git-credential** manual
  1. [English ](https://git-scm.com/docs/git-credential)
  2. [Deutsch ](https://git-scm.com/docs/git-credential/de)
  3. [Français ](https://git-scm.com/docs/git-credential/fr)
  4. [Português (Brasil) ](https://git-scm.com/docs/git-credential/pt_BR)
  5. [українська мова ](https://git-scm.com/docs/git-credential/uk)
  6. [简体中文 ](https://git-scm.com/docs/git-credential/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-credential)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-credential) git-credential last updated in 2.46.0
Changes in the **git-credential** manual
  1. 2.46.1 → 2.53.0 no changes
  2. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git-credential/2.46.0)
  3. 2.43.1 → 2.45.4 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-credential/2.43.0)
  5. 2.42.1 → 2.42.4 no changes
  6. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git-credential/2.42.0)
  7. 2.41.1 → 2.41.3 no changes
  8. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git-credential/2.41.0)
  9. 2.40.1 → 2.40.4 no changes
  10. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/git-credential/2.40.0)
  11. 2.39.1 → 2.39.5 no changes
  12. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-credential/2.39.0)
  13. 2.35.1 → 2.38.5 no changes
  14. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git-credential/2.35.0)
  15. 2.32.1 → 2.34.8 no changes
  16. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git-credential/2.32.0)
  17. 2.27.1 → 2.31.8 no changes
  18. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git-credential/2.27.0)
  19. 2.25.1 → 2.26.3 no changes
  20. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git-credential/2.25.0)
  21. 2.1.4 → 2.24.4 no changes
  22. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-credential/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-credential#_name)NAME
git-credential - Retrieve and store user credentials
##  [](https://git-scm.com/docs/git-credential#_synopsis)SYNOPSIS
```
'git credential' (fill|approve|reject|capability)
```

##  [](https://git-scm.com/docs/git-credential#_description)DESCRIPTION
Git has an internal interface for storing and retrieving credentials from system-specific helpers, as well as prompting the user for usernames and passwords. The git-credential command exposes this interface to scripts which may want to retrieve, store, or prompt for credentials in the same manner as Git. The design of this scriptable interface models the internal C API; see credential.h for more background on the concepts.
git-credential takes an "action" option on the command-line (one of `fill`, `approve`, or `reject`) and reads a credential description on stdin (see [INPUT/OUTPUT FORMAT](https://git-scm.com/docs/git-credential#IOFMT)).
If the action is `fill`, git-credential will attempt to add "username" and "password" attributes to the description by reading config files, by contacting any configured credential helpers, or by prompting the user. The username and password attributes of the credential description are then printed to stdout together with the attributes already provided.
If the action is `approve`, git-credential will send the description to any configured credential helpers, which may store the credential for later use.
If the action is `reject`, git-credential will send the description to any configured credential helpers, which may erase any stored credentials matching the description.
If the action is `capability`, git-credential will announce any capabilities it supports to standard output.
If the action is `approve` or `reject`, no output should be emitted.
##  [](https://git-scm.com/docs/git-credential#_typical_use_of_git_credential)TYPICAL USE OF GIT CREDENTIAL
An application using git-credential will typically use `git` `credential` following these steps:
  1. Generate a credential description based on the context.
For example, if we want a password for `https://example.com/foo.git`, we might generate the following credential description (don’t forget the blank line at the end; it tells `git` `credential` that the application finished feeding all the information it has):
```
protocol=https
host=example.com
path=foo.git
```

  2. Ask git-credential to give us a username and password for this description. This is done by running `git` `credential` `fill`, feeding the description from step (1) to its standard input. The complete credential description (including the credential per se, i.e. the login and password) will be produced on standard output, like:
```
protocol=https
host=example.com
username=bob
password=secr3t
```

In most cases, this means the attributes given in the input will be repeated in the output, but Git may also modify the credential description, for example by removing the `path` attribute when the protocol is HTTP(s) and `credential.useHttpPath` is false.
If the `git` `credential` knew about the password, this step may not have involved the user actually typing this password (the user may have typed a password to unlock the keychain instead, or no user interaction was done if the keychain was already unlocked) before it returned `password=secr3t`.
  3. Use the credential (e.g., access the URL with the username and password from step (2)), and see if it’s accepted.
  4. Report on the success or failure of the password. If the credential allowed the operation to complete successfully, then it can be marked with an "approve" action to tell `git` `credential` to reuse it in its next invocation. If the credential was rejected during the operation, use the "reject" action so that `git` `credential` will ask for a new password in its next invocation. In either case, `git` `credential` should be fed with the credential description obtained from step (2) (which also contains the fields provided in step (1)).


##  [](https://git-scm.com/docs/git-credential#IOFMT)INPUT/OUTPUT FORMAT
`git` `credential` reads and/or writes (depending on the action used) credential information in its standard input/output. This information can correspond either to keys for which `git` `credential` will obtain the login information (e.g. host, protocol, path), or to the actual credential data to be obtained (username/password).
The credential is split into a set of named attributes, with one attribute per line. Each attribute is specified by a key-value pair, separated by an `=` (equals) sign, followed by a newline.
The key may contain any bytes except `=`, newline, or NUL. The value may contain any bytes except newline or NUL. A line, including the trailing newline, may not exceed 65535 bytes in order to allow implementations to parse efficiently.
Attributes with keys that end with C-style array brackets [] can have multiple values. Each instance of a multi-valued attribute forms an ordered list of values - the order of the repeated attributes defines the order of the values. An empty multi-valued attribute (_key[]=\n_) acts to clear any previous entries and reset the list.
In all cases, all bytes are treated as-is (i.e., there is no quoting, and one cannot transmit a value with newline or NUL in it). The list of attributes is terminated by a blank line or end-of-file.
Git understands the following attributes: 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-protocol)`protocol` 
    
The protocol over which the credential will be used (e.g., `https`). 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-host)`host` 
    
The remote hostname for a network credential. This includes the port number if one was specified (e.g., "example.com:8088"). 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-path)`path` 
    
The path with which the credential will be used. E.g., for accessing a remote https repository, this will be the repository’s path on the server. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-username)`username` 
    
The credential’s username, if we already have one (e.g., from a URL, the configuration, the user, or from a previously run helper). 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-password)`password` 
    
The credential’s password, if we are asking it to be stored. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-passwordexpiryutc)`password_expiry_utc` 
    
Generated passwords such as an OAuth access token may have an expiry date. When reading credentials from helpers, `git` `credential` `fill` ignores expired passwords. Represented as Unix time UTC, seconds since 1970. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-oauthrefreshtoken)`oauth_refresh_token` 
    
An OAuth refresh token may accompany a password that is an OAuth access token. Helpers must treat this attribute as confidential like the password attribute. Git itself has no special behaviour for this attribute. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-url)`url` 
    
When this special attribute is read by `git` `credential`, the value is parsed as a URL and treated as if its constituent parts were read (e.g., `url=https://example.com` would behave as if `protocol=https` and `host=example.com` had been provided). This can help callers avoid parsing URLs themselves.
Note that specifying a protocol is mandatory and if the URL doesn’t specify a hostname (e.g., "cert:///path/to/file") the credential will contain a hostname attribute whose value is an empty string.
Components which are missing from the URL (e.g., there is no username in the example above) will be left unset. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-authtype)`authtype` 
    
This indicates that the authentication scheme in question should be used. Common values for HTTP and HTTPS include `basic`, `bearer`, and `digest`, although the latter is insecure and should not be used. If `credential` is used, this may be set to an arbitrary string suitable for the protocol in question (usually HTTP).
This value should not be sent unless the appropriate capability (see below) is provided on input. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-credential)`credential` 
    
The pre-encoded credential, suitable for the protocol in question (usually HTTP). If this key is sent, `authtype` is mandatory, and `username` and `password` are not used. For HTTP, Git concatenates the `authtype` value and this value with a single space to determine the `Authorization` header.
This value should not be sent unless the appropriate capability (see below) is provided on input. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-ephemeral)`ephemeral` 
    
This boolean value indicates, if true, that the value in the `credential` field should not be saved by the credential helper because its usefulness is limited in time. For example, an HTTP Digest `credential` value is computed using a nonce and reusing it will not result in successful authentication. This may also be used for situations with short duration (e.g., 24-hour) credentials. The default value is false.
The credential helper will still be invoked with `store` or `erase` so that it can determine whether the operation was successful.
This value should not be sent unless the appropriate capability (see below) is provided on input. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-state)`state`[] 
    
This value provides an opaque state that will be passed back to this helper if it is called again. Each different credential helper may specify this once. The value should include a prefix unique to the credential helper and should ignore values that don’t match its prefix.
This value should not be sent unless the appropriate capability (see below) is provided on input. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-continue)`continue` 
    
This is a boolean value, which, if enabled, indicates that this authentication is a non-final part of a multistage authentication step. This is common in protocols such as NTLM and Kerberos, where two rounds of client authentication are required, and setting this flag allows the credential helper to implement the multistage authentication step. This flag should only be sent if a further stage is required; that is, if another round of authentication is expected.
This value should not be sent unless the appropriate capability (see below) is provided on input. This attribute is _one-way_ from a credential helper to pass information to Git (or other programs invoking `git` `credential`). 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-wwwauth)`wwwauth`[] 
    
When an HTTP response is received by Git that includes one or more _WWW-Authenticate_ authentication headers, these will be passed by Git to credential helpers.
Each _WWW-Authenticate_ header value is passed as a multi-valued attribute _wwwauth[]_ , where the order of the attributes is the same as they appear in the HTTP response. This attribute is _one-way_ from Git to pass additional information to credential helpers. 

[](https://git-scm.com/docs/git-credential#Documentation/git-credential.txt-capability)`capability`[] 
    
This signals that Git, or the helper, as appropriate, supports the capability in question. This can be used to provide better, more specific data as part of the protocol. A `capability`[] directive must precede any value depending on it and these directives _should_ be the first item announced in the protocol.
There are two currently supported capabilities. The first is `authtype`, which indicates that the `authtype`, `credential`, and `ephemeral` values are understood. The second is `state`, which indicates that the `state`[] and `continue` values are understood.
It is not obligatory to use the additional features just because the capability is supported, but they should not be provided without the capability.
Unrecognised attributes and capabilities are silently discarded.
##  [](https://git-scm.com/docs/git-credential#CAPA-IOFMT)CAPABILITY INPUT/OUTPUT FORMAT
For `git` `credential` `capability`, the format is slightly different. First, a `version` `0` announcement is made to indicate the current version of the protocol, and then each capability is announced with a line like `capability` `authtype`. Credential helpers may also implement this format, again with the `capability` argument. Additional lines may be added in the future; callers should ignore lines which they don’t understand.
Because this is a new part of the credential helper protocol, older versions of Git, as well as some credential helpers, may not support it. If a non-zero exit status is received, or if the first line doesn’t start with the word `version` and a space, callers should assume that no capabilities are supported.
The intention of this format is to differentiate it from the credential output in an unambiguous way. It is possible to use very simple credential helpers (e.g., inline shell scripts) which always produce identical output. Using a distinct format allows users to continue to use this syntax without having to worry about correctly implementing capability advertisements or accidentally confusing callers querying for capabilities.
##  [](https://git-scm.com/docs/git-credential#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### credential
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
