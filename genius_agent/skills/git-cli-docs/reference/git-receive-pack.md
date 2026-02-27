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
    * [NAME](https://git-scm.com/docs/git-receive-pack#_name)
    * [SYNOPSIS](https://git-scm.com/docs/git-receive-pack#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/git-receive-pack#_description)
    * [OPTIONS](https://git-scm.com/docs/git-receive-pack#_options)
    * [PRE-RECEIVE HOOK](https://git-scm.com/docs/git-receive-pack#_pre_receive_hook)
    * [UPDATE HOOK](https://git-scm.com/docs/git-receive-pack#_update_hook)
    * [POST-RECEIVE HOOK](https://git-scm.com/docs/git-receive-pack#_post_receive_hook)
    * [POST-UPDATE HOOK](https://git-scm.com/docs/git-receive-pack#_post_update_hook)
    * [QUARANTINE ENVIRONMENT](https://git-scm.com/docs/git-receive-pack#_quarantine_environment)
    * [SEE ALSO](https://git-scm.com/docs/git-receive-pack#_see_also)
    * [GIT](https://git-scm.com/docs/git-receive-pack#_git)


[ English ▾](https://git-scm.com/docs/git-receive-pack)
Localized versions of **git-receive-pack** manual
  1. [English ](https://git-scm.com/docs/git-receive-pack)
  2. [Português (Brasil) ](https://git-scm.com/docs/git-receive-pack/pt_BR)
  3. [українська мова ](https://git-scm.com/docs/git-receive-pack/uk)
  4. [简体中文 ](https://git-scm.com/docs/git-receive-pack/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git-receive-pack)
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


[ Latest version ▾ ](https://git-scm.com/docs/git-receive-pack) git-receive-pack last updated in 2.50.0
Changes in the **git-receive-pack** manual
  1. 2.50.1 → 2.53.0 no changes
  2. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git-receive-pack/2.50.0)
  3. 2.43.1 → 2.49.1 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git-receive-pack/2.43.0)
  5. 2.39.1 → 2.42.4 no changes
  6. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git-receive-pack/2.39.0)
  7. 2.34.1 → 2.38.5 no changes
  8. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git-receive-pack/2.34.0)
  9. 2.24.1 → 2.33.8 no changes
  10. [2.24.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-11-04_ ](https://git-scm.com/docs/git-receive-pack/2.24.0)
  11. 2.18.1 → 2.23.4 no changes
  12. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git-receive-pack/2.18.0)
  13. 2.14.6 → 2.17.6 no changes
  14. [2.13.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-05-22_ ](https://git-scm.com/docs/git-receive-pack/2.13.7)
  15. 2.12.5 no changes
  16. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git-receive-pack/2.11.4)
  17. 2.5.6 → 2.10.5 no changes
  18. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git-receive-pack/2.4.12)
  19. 2.3.10 no changes
  20. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git-receive-pack/2.2.3)
  21. 2.1.4 no changes
  22. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git-receive-pack/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git-receive-pack#_name)NAME
git-receive-pack - Receive what is pushed into the repository
##  [](https://git-scm.com/docs/git-receive-pack#_synopsis)SYNOPSIS
```
_git receive-pack_ <git-dir>
```

##  [](https://git-scm.com/docs/git-receive-pack#_description)DESCRIPTION
Invoked by _git send-pack_ and updates the repository with the information fed from the remote end.
This command is usually not invoked directly by the end user. The UI for the protocol is on the _git send-pack_ side, and the program pair is meant to be used to push updates to a remote repository. For pull operations, see [git-fetch-pack[1]](https://git-scm.com/docs/git-fetch-pack).
The command allows for the creation and fast-forwarding of sha1 refs (heads/tags) on the remote end (strictly speaking, it is the local end _git-receive-pack_ runs, but to the user who is sitting at the send-pack end, it is updating the remote. Confused?)
There are other real-world examples of using update and post-update hooks found in the Documentation/howto directory.
_git-receive-pack_ honours the receive.denyNonFastForwards config option, which tells it if updates to a ref should be denied if they are not fast-forwards.
A number of other receive.* config options are available to tweak its behavior, see [git-config[1]](https://git-scm.com/docs/git-config).
##  [](https://git-scm.com/docs/git-receive-pack#_options)OPTIONS 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-git-dir)<git-dir> 
    
The repository to sync into. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt---http-backend-info-refs)--http-backend-info-refs 
    
Used by [git-http-backend[1]](https://git-scm.com/docs/git-http-backend) to serve up _$GIT_URL/info/refs?service=git-receive-pack_ requests. See `--http-backend-info-refs` in [git-upload-pack[1]](https://git-scm.com/docs/git-upload-pack). 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt---skip-connectivity-check)--skip-connectivity-check 
    
Bypasses the connectivity checks that validate the existence of all objects in the transitive closure of reachable objects. This option is intended for server operators that want to implement their own object connectivity validation outside of Git. This is useful in such cases where the server-side knows additional information about how Git is being used and thus can rely on certain guarantees to more efficiently compute object connectivity that Git itself cannot make. Usage of this option without a reliable external mechanism to ensure full reachable object connectivity risks corrupting the repository and should not be used in the general case.
##  [](https://git-scm.com/docs/git-receive-pack#_pre_receive_hook)PRE-RECEIVE HOOK
Before any ref is updated, if $GIT_DIR/hooks/pre-receive file exists and is executable, it will be invoked once with no parameters. The standard input of the hook will be one line per ref to be updated:
```
sha1-old SP sha1-new SP refname LF
```

The refname value is relative to $GIT_DIR; e.g. for the master head this is "refs/heads/master". The two sha1 values before each refname are the object names for the refname before and after the update. Refs to be created will have sha1-old equal to 0{40}, while refs to be deleted will have sha1-new equal to 0{40}, otherwise sha1-old and sha1-new should be valid objects in the repository.
When accepting a signed push (see [git-push[1]](https://git-scm.com/docs/git-push)), the signed push certificate is stored in a blob and an environment variable `GIT_PUSH_CERT` can be consulted for its object name. See the description of `post-receive` hook for an example. In addition, the certificate is verified using GPG and the result is exported with the following environment variables: 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-GITPUSHCERTSIGNER)`GIT_PUSH_CERT_SIGNER` 
    
The name and the e-mail address of the owner of the key that signed the push certificate. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-GITPUSHCERTKEY)`GIT_PUSH_CERT_KEY` 
    
The GPG key ID of the key that signed the push certificate. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-GITPUSHCERTSTATUS)`GIT_PUSH_CERT_STATUS` 
    
The status of GPG verification of the push certificate, using the same mnemonic as used in _%G?_ format of `git` `log` family of commands (see [git-log[1]](https://git-scm.com/docs/git-log)). 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-GITPUSHCERTNONCE)`GIT_PUSH_CERT_NONCE` 
    
The nonce string the process asked the signer to include in the push certificate. If this does not match the value recorded on the "nonce" header in the push certificate, it may indicate that the certificate is a valid one that is being replayed from a separate "git push" session. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-GITPUSHCERTNONCESTATUS)`GIT_PUSH_CERT_NONCE_STATUS` 
     

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-UNSOLICITED)`UNSOLICITED` 
    
"git push --signed" sent a nonce when we did not ask it to send one. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-MISSING)`MISSING` 
    
"git push --signed" did not send any nonce header. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-BAD)`BAD` 
    
"git push --signed" sent a bogus nonce. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-OK)`OK` 
    
"git push --signed" sent the nonce we asked it to send. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-SLOP)`SLOP` 
    
"git push --signed" sent a nonce different from what we asked it to send now, but in a previous session. See `GIT_PUSH_CERT_NONCE_SLOP` environment variable. 

[](https://git-scm.com/docs/git-receive-pack#Documentation/git-receive-pack.txt-GITPUSHCERTNONCESLOP)`GIT_PUSH_CERT_NONCE_SLOP` 
    
"git push --signed" sent a nonce different from what we asked it to send now, but in a different session whose starting time is different by this many seconds from the current session. Only meaningful when `GIT_PUSH_CERT_NONCE_STATUS` says `SLOP`. Also read about `receive.certNonceSlop` variable in [git-config[1]](https://git-scm.com/docs/git-config).
This hook is called before any refname is updated and before any fast-forward checks are performed.
If the pre-receive hook exits with a non-zero exit status no updates will be performed, and the update, post-receive and post-update hooks will not be invoked either. This can be useful to quickly bail out if the update is not to be supported.
See the notes on the quarantine environment below.
##  [](https://git-scm.com/docs/git-receive-pack#_update_hook)UPDATE HOOK
Before each ref is updated, if $GIT_DIR/hooks/update file exists and is executable, it is invoked once per ref, with three parameters:
```
$GIT_DIR/hooks/update refname sha1-old sha1-new
```

The refname parameter is relative to $GIT_DIR; e.g. for the master head this is "refs/heads/master". The two sha1 arguments are the object names for the refname before and after the update. Note that the hook is called before the refname is updated, so either sha1-old is 0{40} (meaning there is no such ref yet), or it should match what is recorded in refname.
The hook should exit with non-zero status if it wants to disallow updating the named ref. Otherwise it should exit with zero.
Successful execution (a zero exit status) of this hook does not ensure the ref will actually be updated, it is only a prerequisite. As such it is not a good idea to send notices (e.g. email) from this hook. Consider using the post-receive hook instead.
##  [](https://git-scm.com/docs/git-receive-pack#_post_receive_hook)POST-RECEIVE HOOK
After all refs were updated (or attempted to be updated), if any ref update was successful, and if $GIT_DIR/hooks/post-receive file exists and is executable, it will be invoked once with no parameters. The standard input of the hook will be one line for each successfully updated ref:
```
sha1-old SP sha1-new SP refname LF
```

The refname value is relative to $GIT_DIR; e.g. for the master head this is "refs/heads/master". The two sha1 values before each refname are the object names for the refname before and after the update. Refs that were created will have sha1-old equal to 0{40}, while refs that were deleted will have sha1-new equal to 0{40}, otherwise sha1-old and sha1-new should be valid objects in the repository.
The `GIT_PUSH_CERT*` environment variables can be inspected, just as in `pre-receive` hook, after accepting a signed push.
Using this hook, it is easy to generate mails describing the updates to the repository. This example script sends one mail message per ref listing the commits pushed to the repository, and logs the push certificates of signed pushes with good signatures to a logger service:
```
#!/bin/sh
# mail out commit update information.
while read oval nval ref
do
	if expr "$oval" : '0*$' >/dev/null
	then
		echo "Created a new ref, with the following commits:"
		git rev-list --pretty "$nval"
	else
		echo "New commits:"
		git rev-list --pretty "$nval" "^$oval"
	fi |
	mail -s "Changes to ref $ref" commit-list@mydomain
done
# log signed push certificate, if any
if test -n "${GIT_PUSH_CERT-}" && test ${GIT_PUSH_CERT_STATUS} = G
then
	(
		echo expected nonce is ${GIT_PUSH_NONCE}
		git cat-file blob ${GIT_PUSH_CERT}
	) | mail -s "push certificate from $GIT_PUSH_CERT_SIGNER" push-log@mydomain
fi
exit 0
```

The exit code from this hook invocation is ignored, however a non-zero exit code will generate an error message.
Note that it is possible for refname to not have sha1-new when this hook runs. This can easily occur if another user modifies the ref after it was updated by _git-receive-pack_ , but before the hook was able to evaluate it. It is recommended that hooks rely on sha1-new rather than the current value of refname.
##  [](https://git-scm.com/docs/git-receive-pack#_post_update_hook)POST-UPDATE HOOK
After all other processing, if at least one ref was updated, and if $GIT_DIR/hooks/post-update file exists and is executable, then post-update will be called with the list of refs that have been updated. This can be used to implement any repository wide cleanup tasks.
The exit code from this hook invocation is ignored; the only thing left for _git-receive-pack_ to do at that point is to exit itself anyway.
This hook can be used, for example, to run `git` `update-server-info` if the repository is packed and is served via a dumb transport.
```
#!/bin/sh
exec git update-server-info
```

##  [](https://git-scm.com/docs/git-receive-pack#_quarantine_environment)QUARANTINE ENVIRONMENT
When `receive-pack` takes in objects, they are placed into a temporary "quarantine" directory within the `$GIT_DIR/objects` directory and migrated into the main object store only after the `pre-receive` hook has completed. If the push fails before then, the temporary directory is removed entirely.
This has a few user-visible effects and caveats:
  1. Pushes which fail due to problems with the incoming pack, missing objects, or due to the `pre-receive` hook will not leave any on-disk data. This is usually helpful to prevent repeated failed pushes from filling up your disk, but can make debugging more challenging.
  2. Any objects created by the `pre-receive` hook will be created in the quarantine directory (and migrated only if it succeeds).
  3. The `pre-receive` hook MUST NOT update any refs to point to quarantined objects. Other programs accessing the repository will not be able to see the objects (and if the pre-receive hook fails, those refs would become corrupted). For safety, any ref updates from within `pre-receive` are automatically rejected.


##  [](https://git-scm.com/docs/git-receive-pack#_see_also)SEE ALSO
[git-send-pack[1]](https://git-scm.com/docs/git-send-pack), [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces)
##  [](https://git-scm.com/docs/git-receive-pack#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### receive-pack
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
