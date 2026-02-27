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
    * [NAME](https://git-scm.com/docs/gitformat-signature#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitformat-signature#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitformat-signature#_description)
    * [Tag signatures](https://git-scm.com/docs/gitformat-signature#_tag_signatures)
    * [Commit signatures](https://git-scm.com/docs/gitformat-signature#_commit_signatures)
    * [Mergetag signatures](https://git-scm.com/docs/gitformat-signature#_mergetag_signatures)
    * [GIT](https://git-scm.com/docs/gitformat-signature#_git)


[ English ▾](https://git-scm.com/docs/gitformat-signature)
Localized versions of **gitformat-signature** manual
  1. [English ](https://git-scm.com/docs/gitformat-signature)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitformat-signature)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitformat-signature) gitformat-signature last updated in 2.40.0
Changes in the **gitformat-signature** manual
  1. 2.40.1 → 2.53.0 no changes
  2. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/gitformat-signature/2.40.0)
  3. 2.38.1 → 2.39.5 no changes
  4. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/gitformat-signature/2.38.0)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitformat-signature#_name)NAME
gitformat-signature - Git cryptographic signature formats
##  [](https://git-scm.com/docs/gitformat-signature#_synopsis)SYNOPSIS
```
<[tag|commit] object header(s)>
<over-the-wire protocol>
```

##  [](https://git-scm.com/docs/gitformat-signature#_description)DESCRIPTION
Git uses cryptographic signatures in various places, currently objects (tags, commits, mergetags) and transactions (pushes). In every case, the command which is about to create an object or transaction determines a payload from that, calls an external program to obtain a detached signature for the payload (`gpg` `-bsa` in the case of PGP signatures), and embeds the signature into the object or transaction.
Signatures begin with an "ASCII Armor" header line and end with a tail line, which differ depending on signature type (as selected by `gpg.format`, see [git-config[1]](https://git-scm.com/docs/git-config)). These are, for `gpg.format` values: 

[](https://git-scm.com/docs/gitformat-signature#Documentation/gitformat-signature.txt-gpgPGP)`gpg` (PGP) 
    
`-----BEGIN` `PGP` `SIGNATURE-----` and `-----END` `PGP` `SIGNATURE-----`. Or, if gpg is told to produce RFC1991 signatures, `-----BEGIN` `PGP` `MESSAGE-----` and `-----END` `PGP` `MESSAGE-----` 

[](https://git-scm.com/docs/gitformat-signature#Documentation/gitformat-signature.txt-sshSSH)`ssh` (SSH) 
    
`-----BEGIN` `SSH` `SIGNATURE-----` and `-----END` `SSH` `SIGNATURE-----` 

[](https://git-scm.com/docs/gitformat-signature#Documentation/gitformat-signature.txt-x509X509)`x509` (X.509) 
    
`-----BEGIN` `SIGNED` `MESSAGE-----` and `-----END` `SIGNED` `MESSAGE-----`
Signatures sometimes appear as a part of the normal payload (e.g. a signed tag has the signature block appended after the payload that the signature applies to), and sometimes appear in the value of an object header (e.g. a merge commit that merged a signed tag would have the entire tag contents on its "mergetag" header). In the case of the latter, the usual multi-line formatting rule for object headers applies. I.e. the second and subsequent lines are prefixed with a SP to signal that the line is continued from the previous line.
This is even true for an originally empty line. In the following examples, the end of line that ends with a whitespace letter is highlighted with a `$` sign; if you are trying to recreate these example by hand, do not cut and paste them—​they are there primarily to highlight extra whitespace at the end of some lines.
The signed payload and the way the signature is embedded depends on the type of the object resp. transaction.
##  [](https://git-scm.com/docs/gitformat-signature#_tag_signatures)Tag signatures
  * created by: `git` `tag` `-s`
  * payload: annotated tag object
  * embedding: append the signature to the unsigned tag object
  * example: tag `signedtag` with subject `signed` `tag`


```
object 04b871796dc0420f8e7561a895b52484b701d51a
type commit
tag signedtag
tagger C O Mitter <committer@example.com> 1465981006 +0000

signed tag

signed tag message body
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iQEcBAABAgAGBQJXYRhOAAoJEGEJLoW3InGJklkIAIcnhL7RwEb/+QeX9enkXhxn
rxfdqrvWd1K80sl2TOt8Bg/NYwrUBw/RWJ+sg/hhHp4WtvE1HDGHlkEz3y11Lkuh
8tSxS3qKTxXUGozyPGuE90sJfExhZlW4knIQ1wt/yWqM+33E9pN4hzPqLwyrdods
q8FWEqPPUbSJXoMbRPw04S5jrLtZSsUWbRYjmJCHzlhSfFWW4eFd37uquIaLUBS0
rkC3Jrx7420jkIpgFcTI2s60uhSQLzgcCwdA2ukSYIRnjg/zDkj8+3h/GaROJ72x
lZyI6HWixKJkWw8lE9aAOD9TmTW9sFJwcVAzmAuFX2kUreDUKMZduGcoRYGpD7E=
=jpXa
-----END PGP SIGNATURE-----
```

  * verify with: `git` `verify-tag` [`-v`] or `git` `tag` `-v`


```
gpg: Signature made Wed Jun 15 10:56:46 2016 CEST using RSA key ID B7227189
gpg: Good signature from "Eris Discordia <discord@example.net>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: D4BE 2231 1AD3 131E 5EDA  29A4 6109 2E85 B722 7189
object 04b871796dc0420f8e7561a895b52484b701d51a
type commit
tag signedtag
tagger C O Mitter <committer@example.com> 1465981006 +0000

signed tag

signed tag message body
```

##  [](https://git-scm.com/docs/gitformat-signature#_commit_signatures)Commit signatures
  * created by: `git` `commit` `-S`
  * payload: commit object
  * embedding: header entry `gpgsig` (content is preceded by a space)
  * example: commit with subject `signed` `commit`


```
tree eebfed94e75e7760540d1485c740902590a00332
parent 04b871796dc0420f8e7561a895b52484b701d51a
author A U Thor <author@example.com> 1465981137 +0000
committer C O Mitter <committer@example.com> 1465981137 +0000
gpgsig -----BEGIN PGP SIGNATURE-----
 Version: GnuPG v1
 $
 iQEcBAABAgAGBQJXYRjRAAoJEGEJLoW3InGJ3IwIAIY4SA6GxY3BjL60YyvsJPh/
 HRCJwH+w7wt3Yc/9/bW2F+gF72kdHOOs2jfv+OZhq0q4OAN6fvVSczISY/82LpS7
 DVdMQj2/YcHDT4xrDNBnXnviDO9G7am/9OE77kEbXrp7QPxvhjkicHNwy2rEflAA
 zn075rtEERDHr8nRYiDh8eVrefSO7D+bdQ7gv+7GsYMsd2auJWi1dHOSfTr9HIF4
 HJhWXT9d2f8W+diRYXGh4X0wYiGg6na/soXc+vdtDYBzIxanRqjg8jCAeo1eOTk1
 EdTwhcTZlI0x5pvJ3H0+4hA2jtldVtmPM4OTB0cTrEWBad7XV6YgiyuII73Ve3I=
 =jKHM
 -----END PGP SIGNATURE-----

signed commit

signed commit message body
```

  * verify with: `git` `verify-commit` [`-v`] (or `git` `show` `--show-signature`)


```
gpg: Signature made Wed Jun 15 10:58:57 2016 CEST using RSA key ID B7227189
gpg: Good signature from "Eris Discordia <discord@example.net>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: D4BE 2231 1AD3 131E 5EDA  29A4 6109 2E85 B722 7189
tree eebfed94e75e7760540d1485c740902590a00332
parent 04b871796dc0420f8e7561a895b52484b701d51a
author A U Thor <author@example.com> 1465981137 +0000
committer C O Mitter <committer@example.com> 1465981137 +0000

signed commit

signed commit message body
```

##  [](https://git-scm.com/docs/gitformat-signature#_mergetag_signatures)Mergetag signatures
  * created by: `git` `merge` on signed tag
  * payload/embedding: the whole signed tag object is embedded into the (merge) commit object as header entry `mergetag`
  * example: merge of the signed tag `signedtag` as above


```
tree c7b1cff039a93f3600a1d18b82d26688668c7dea
parent c33429be94b5f2d3ee9b0adad223f877f174b05d
parent 04b871796dc0420f8e7561a895b52484b701d51a
author A U Thor <author@example.com> 1465982009 +0000
committer C O Mitter <committer@example.com> 1465982009 +0000
mergetag object 04b871796dc0420f8e7561a895b52484b701d51a
 type commit
 tag signedtag
 tagger C O Mitter <committer@example.com> 1465981006 +0000
 $
 signed tag
 $
 signed tag message body
 -----BEGIN PGP SIGNATURE-----
 Version: GnuPG v1
 $
 iQEcBAABAgAGBQJXYRhOAAoJEGEJLoW3InGJklkIAIcnhL7RwEb/+QeX9enkXhxn
 rxfdqrvWd1K80sl2TOt8Bg/NYwrUBw/RWJ+sg/hhHp4WtvE1HDGHlkEz3y11Lkuh
 8tSxS3qKTxXUGozyPGuE90sJfExhZlW4knIQ1wt/yWqM+33E9pN4hzPqLwyrdods
 q8FWEqPPUbSJXoMbRPw04S5jrLtZSsUWbRYjmJCHzlhSfFWW4eFd37uquIaLUBS0
 rkC3Jrx7420jkIpgFcTI2s60uhSQLzgcCwdA2ukSYIRnjg/zDkj8+3h/GaROJ72x
 lZyI6HWixKJkWw8lE9aAOD9TmTW9sFJwcVAzmAuFX2kUreDUKMZduGcoRYGpD7E=
 =jpXa
 -----END PGP SIGNATURE-----

Merge tag 'signedtag' into downstream

signed tag

signed tag message body

# gpg: Signature made Wed Jun 15 08:56:46 2016 UTC using RSA key ID B7227189
# gpg: Good signature from "Eris Discordia <discord@example.net>"
# gpg: WARNING: This key is not certified with a trusted signature!
# gpg:          There is no indication that the signature belongs to the owner.
# Primary key fingerprint: D4BE 2231 1AD3 131E 5EDA  29A4 6109 2E85 B722 7189
```

  * verify with: verification is embedded in merge commit message by default, alternatively with `git` `show` `--show-signature`:


```
commit 9863f0c76ff78712b6800e199a46aa56afbcbd49
merged tag 'signedtag'
gpg: Signature made Wed Jun 15 10:56:46 2016 CEST using RSA key ID B7227189
gpg: Good signature from "Eris Discordia <discord@example.net>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: D4BE 2231 1AD3 131E 5EDA  29A4 6109 2E85 B722 7189
Merge: c33429b 04b8717
Author: A U Thor <author@example.com>
Date:   Wed Jun 15 09:13:29 2016 +0000

    Merge tag 'signedtag' into downstream

    signed tag

    signed tag message body

    # gpg: Signature made Wed Jun 15 08:56:46 2016 UTC using RSA key ID B7227189
    # gpg: Good signature from "Eris Discordia <discord@example.net>"
    # gpg: WARNING: This key is not certified with a trusted signature!
    # gpg:          There is no indication that the signature belongs to the owner.
    # Primary key fingerprint: D4BE 2231 1AD3 131E 5EDA  29A4 6109 2E85 B722 7189
```

##  [](https://git-scm.com/docs/gitformat-signature#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitformat-signature
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
