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
    * [NAME](https://git-scm.com/docs/gitprotocol-capabilities#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitprotocol-capabilities#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitprotocol-capabilities#_description)
    * [multi_ack](https://git-scm.com/docs/gitprotocol-capabilities#_multi_ack)
    * [multi_ack_detailed](https://git-scm.com/docs/gitprotocol-capabilities#_multi_ack_detailed)
    * [no-done](https://git-scm.com/docs/gitprotocol-capabilities#_no_done)
    * [thin-pack](https://git-scm.com/docs/gitprotocol-capabilities#_thin_pack)
    * [side-band, side-band-64k](https://git-scm.com/docs/gitprotocol-capabilities#_side_band_side_band_64k)
    * [ofs-delta](https://git-scm.com/docs/gitprotocol-capabilities#_ofs_delta)
    * [agent](https://git-scm.com/docs/gitprotocol-capabilities#_agent)
    * [object-format](https://git-scm.com/docs/gitprotocol-capabilities#_object_format)
    * [symref](https://git-scm.com/docs/gitprotocol-capabilities#_symref)
    * [shallow](https://git-scm.com/docs/gitprotocol-capabilities#_shallow)
    * [deepen-since](https://git-scm.com/docs/gitprotocol-capabilities#_deepen_since)
    * [deepen-not](https://git-scm.com/docs/gitprotocol-capabilities#_deepen_not)
    * [deepen-relative](https://git-scm.com/docs/gitprotocol-capabilities#_deepen_relative)
    * [no-progress](https://git-scm.com/docs/gitprotocol-capabilities#_no_progress)
    * [include-tag](https://git-scm.com/docs/gitprotocol-capabilities#_include_tag)
    * [report-status](https://git-scm.com/docs/gitprotocol-capabilities#_report_status)
    * [report-status-v2](https://git-scm.com/docs/gitprotocol-capabilities#_report_status_v2)
    * [delete-refs](https://git-scm.com/docs/gitprotocol-capabilities#_delete_refs)
    * [quiet](https://git-scm.com/docs/gitprotocol-capabilities#_quiet)
    * [atomic](https://git-scm.com/docs/gitprotocol-capabilities#_atomic)
    * [push-options](https://git-scm.com/docs/gitprotocol-capabilities#_push_options)
    * [allow-tip-sha1-in-want](https://git-scm.com/docs/gitprotocol-capabilities#_allow_tip_sha1_in_want)
    * [allow-reachable-sha1-in-want](https://git-scm.com/docs/gitprotocol-capabilities#_allow_reachable_sha1_in_want)
    * [push-cert=<nonce>](https://git-scm.com/docs/gitprotocol-capabilities#_push_certnonce)
    * [filter](https://git-scm.com/docs/gitprotocol-capabilities#_filter)
    * [session-id=<session-id>](https://git-scm.com/docs/gitprotocol-capabilities#_session_idsession_id)
    * [GIT](https://git-scm.com/docs/gitprotocol-capabilities#_git)


[ English ▾](https://git-scm.com/docs/gitprotocol-capabilities)
Localized versions of **gitprotocol-capabilities** manual
  1. [English ](https://git-scm.com/docs/gitprotocol-capabilities)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitprotocol-capabilities)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitprotocol-capabilities) gitprotocol-capabilities last updated in 2.44.0
Changes in the **gitprotocol-capabilities** manual
  1. 2.44.1 → 2.53.0 no changes
  2. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/gitprotocol-capabilities/2.44.0)
  3. 2.43.1 → 2.43.7 no changes
  4. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/gitprotocol-capabilities/2.43.0)
  5. 2.38.1 → 2.42.4 no changes
  6. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/gitprotocol-capabilities/2.38.0)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_name)NAME
gitprotocol-capabilities - Protocol v0 and v1 capabilities
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_synopsis)SYNOPSIS
```
<over-the-wire-protocol>
```

##  [](https://git-scm.com/docs/gitprotocol-capabilities#_description)DESCRIPTION
Note |  this document describes capabilities for versions 0 and 1 of the pack protocol. For version 2, please refer to the [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2) doc.   
---|---  
Servers SHOULD support all capabilities defined in this document.
On the very first line of the initial server response of either receive-pack and upload-pack the first reference is followed by a NUL byte and then a list of space delimited server capabilities. These allow the server to declare what it can and cannot support to the client.
Client will then send a space separated list of capabilities it wants to be in effect. The client MUST NOT ask for capabilities the server did not say it supports.
Server MUST diagnose and abort if capabilities it does not understand were sent. Server MUST NOT ignore capabilities that client requested and server advertised. As a consequence of these rules, server MUST NOT advertise capabilities it does not understand.
The _atomic_ , _report-status_ , _report-status-v2_ , _delete-refs_ , _quiet_ , and _push-cert_ capabilities are sent and recognized by the receive-pack (push to server) process.
The _ofs-delta_ and _side-band-64k_ capabilities are sent and recognized by both upload-pack and receive-pack protocols. The _agent_ and _session-id_ capabilities may optionally be sent in both protocols.
All other capabilities are only recognized by the upload-pack (fetch from server) process.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_multi_ack)multi_ack
The _multi_ack_ capability allows the server to return "ACK obj-id continue" as soon as it finds a commit that it can use as a common base, between the client’s wants and the client’s have set.
By sending this early, the server can potentially head off the client from walking any further down that particular branch of the client’s repository history. The client may still need to walk down other branches, sending have lines for those, until the server has a complete cut across the DAG, or the client has said "done".
Without multi_ack, a client sends have lines in --date-order until the server has found a common base. That means the client will send have lines that are already known by the server to be common, because they overlap in time with another branch on which the server hasn’t found a common base yet.
For example suppose the client has commits in caps that the server doesn’t and the server has commits in lower case that the client doesn’t, as in the following diagram:
```
      +---- u ---------------------- x
     /              +----- y
    /              /
   a -- b -- c -- d -- E -- F
      \
+--- Q -- R -- S
```

If the client wants x,y and starts out by saying have F,S, the server doesn’t know what F,S is. Eventually the client says "have d" and the server sends "ACK d continue" to let the client know to stop walking down that line (so don’t send c-b-a), but it’s not done yet, it needs a base for x. The client keeps going with S-R-Q, until a gets reached, at which point the server has a clear base and it all ends.
Without multi_ack the client would have sent that c-b-a chain anyway, interleaved with S-R-Q.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_multi_ack_detailed)multi_ack_detailed
This is an extension of multi_ack that permits the client to better understand the server’s in-memory state. See [gitprotocol-pack[5]](https://git-scm.com/docs/gitprotocol-pack), section "Packfile Negotiation" for more information.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_no_done)no-done
This capability should only be used with the smart HTTP protocol. If multi_ack_detailed and no-done are both present, then the sender is free to immediately send a pack following its first "ACK obj-id ready" message.
Without no-done in the smart HTTP protocol, the server session would end and the client has to make another trip to send "done" before the server can send the pack. no-done removes the last round and thus slightly reduces latency.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_thin_pack)thin-pack
A thin pack is one with deltas which reference base objects not contained within the pack (but are known to exist at the receiving end). This can reduce the network traffic significantly, but it requires the receiving end to know how to "thicken" these packs by adding the missing bases to the pack.
The upload-pack server advertises _thin-pack_ when it can generate and send a thin pack. A client requests the _thin-pack_ capability when it understands how to "thicken" it, notifying the server that it can receive such a pack. A client MUST NOT request the _thin-pack_ capability if it cannot turn a thin pack into a self-contained pack.
Receive-pack, on the other hand, is assumed by default to be able to handle thin packs, but can ask the client not to use the feature by advertising the _no-thin_ capability. A client MUST NOT send a thin pack if the server advertises the _no-thin_ capability.
The reasons for this asymmetry are historical. The receive-pack program did not exist until after the invention of thin packs, so historically the reference implementation of receive-pack always understood thin packs. Adding _no-thin_ later allowed receive-pack to disable the feature in a backwards-compatible manner.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_side_band_side_band_64k)side-band, side-band-64k
This capability means that the server can send, and the client can understand, multiplexed progress reports and error info interleaved with the packfile itself.
These two options are mutually exclusive. A modern client always favors _side-band-64k_.
Either mode indicates that the packfile data will be streamed broken up into packets of up to either 1000 bytes in the case of _side_band_ , or 65520 bytes in the case of _side_band_64k_. Each packet is made up of a leading 4-byte pkt-line length of how much data is in the packet, followed by a 1-byte stream code, followed by the actual data.
The stream code can be one of:
```
1 - pack data
2 - progress messages
3 - fatal error message just before stream aborts
```

The "side-band-64k" capability came about as a way for newer clients that can handle much larger packets to request packets that are actually crammed nearly full, while maintaining backward compatibility for the older clients.
Further, with side-band and its up to 1000-byte messages, it’s actually 999 bytes of payload and 1 byte for the stream code. With side-band-64k, same deal, you have up to 65519 bytes of data and 1 byte for the stream code.
The client MUST send only one of "side-band" and "side- band-64k". The server MUST diagnose it as an error if client requests both.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_ofs_delta)ofs-delta
The server can send, and the client can understand, PACKv2 with delta referring to its base by position in pack rather than by an obj-id. That is, they can send/read OBJ_OFS_DELTA (aka type 6) in a packfile.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_agent)agent
The server may optionally send a capability of the form `agent=X` to notify the client that the server is running version `X`. The client may optionally return its own agent string by responding with an `agent=Y` capability (but it MUST NOT do so if the server did not mention the agent capability). The `X` and `Y` strings may contain any printable ASCII characters except space (i.e., the byte range 32 < x < 127), and are typically of the form "package/version" (e.g., "git/1.8.3.1"). The agent strings are purely informative for statistics and debugging purposes, and MUST NOT be used to programmatically assume the presence or absence of particular features.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_object_format)object-format
This capability, which takes a hash algorithm as an argument, indicates that the server supports the given hash algorithms. It may be sent multiple times; if so, the first one given is the one used in the ref advertisement.
When provided by the client, this indicates that it intends to use the given hash algorithm to communicate. The algorithm provided must be one that the server supports.
If this capability is not provided, it is assumed that the only supported algorithm is SHA-1.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_symref)symref
This parameterized capability is used to inform the receiver which symbolic ref points to which ref; for example, "symref=HEAD:refs/heads/master" tells the receiver that HEAD points to master. This capability can be repeated to represent multiple symrefs.
Servers SHOULD include this capability for the HEAD symref if it is one of the refs being sent.
Clients MAY use the parameters from this capability to select the proper initial branch when cloning a repository.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_shallow)shallow
This capability adds "deepen", "shallow" and "unshallow" commands to the fetch-pack/upload-pack protocol so clients can request shallow clones.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_deepen_since)deepen-since
This capability adds "deepen-since" command to fetch-pack/upload-pack protocol so the client can request shallow clones that are cut at a specific time, instead of depth. Internally it’s equivalent of doing "rev-list --max-age=<timestamp>" on the server side. "deepen-since" cannot be used with "deepen".
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_deepen_not)deepen-not
This capability adds "deepen-not" command to fetch-pack/upload-pack protocol so the client can request shallow clones that are cut at a specific revision, instead of depth. Internally it’s equivalent of doing "rev-list --not <rev>" on the server side. "deepen-not" cannot be used with "deepen", but can be used with "deepen-since".
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_deepen_relative)deepen-relative
If this capability is requested by the client, the semantics of "deepen" command is changed. The "depth" argument is the depth from the current shallow boundary, instead of the depth from remote refs.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_no_progress)no-progress
The client was started with "git clone -q" or something similar, and doesn’t want that side band 2. Basically the client just says "I do not wish to receive stream 2 on sideband, so do not send it to me, and if you did, I will drop it on the floor anyway". However, the sideband channel 3 is still used for error responses.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_include_tag)include-tag
The _include-tag_ capability is about sending annotated tags if we are sending objects they point to. If we pack an object to the client, and a tag object points exactly at that object, we pack the tag object too. In general this allows a client to get all new annotated tags when it fetches a branch, in a single network connection.
Clients MAY always send include-tag, hardcoding it into a request when the server advertises this capability. The decision for a client to request include-tag only has to do with the client’s desires for tag data, whether or not a server had advertised objects in the refs/tags/* namespace.
Servers MUST pack the tags if their referent is packed and the client has requested include-tags.
Clients MUST be prepared for the case where a server has ignored include-tag and has not actually sent tags in the pack. In such cases the client SHOULD issue a subsequent fetch to acquire the tags that include-tag would have otherwise given the client.
The server SHOULD send include-tag, if it supports it, regardless of whether or not there are tags available.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_report_status)report-status
The receive-pack process can receive a _report-status_ capability, which tells it that the client wants a report of what happened after a packfile upload and reference update. If the pushing client requests this capability, after unpacking and updating references the server will respond with whether the packfile unpacked successfully and if each reference was updated successfully. If any of those were not successful, it will send back an error message. See [gitprotocol-pack[5]](https://git-scm.com/docs/gitprotocol-pack) for example messages.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_report_status_v2)report-status-v2
Capability _report-status-v2_ extends capability _report-status_ by adding new "option" directives in order to support reference rewritten by the "proc-receive" hook. The "proc-receive" hook may handle a command for a pseudo-reference which may create or update a reference with different name, new-oid, and old-oid. While the capability _report-status_ cannot report for such case. See [gitprotocol-pack[5]](https://git-scm.com/docs/gitprotocol-pack) for details.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_delete_refs)delete-refs
If the server sends back the _delete-refs_ capability, it means that it is capable of accepting a zero-id value as the target value of a reference update. It is not sent back by the client, it simply informs the client that it can be sent zero-id values to delete references.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_quiet)quiet
If the receive-pack server advertises the _quiet_ capability, it is capable of silencing human-readable progress output which otherwise may be shown when processing the received pack. A send-pack client should respond with the _quiet_ capability to suppress server-side progress reporting if the local progress reporting is also being suppressed (e.g., via `push` `-q`, or if stderr does not go to a tty).
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_atomic)atomic
If the server sends the _atomic_ capability it is capable of accepting atomic pushes. If the pushing client requests this capability, the server will update the refs in one atomic transaction. Either all refs are updated or none.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_push_options)push-options
If the server sends the _push-options_ capability it is able to accept push options after the update commands have been sent, but before the packfile is streamed. If the pushing client requests this capability, the server will pass the options to the pre- and post- receive hooks that process this push request.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_allow_tip_sha1_in_want)allow-tip-sha1-in-want
If the upload-pack server advertises this capability, fetch-pack may send "want" lines with object names that exist at the server but are not advertised by upload-pack. For historical reasons, the name of this capability contains "sha1". Object names are always given using the object format negotiated through the _object-format_ capability.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_allow_reachable_sha1_in_want)allow-reachable-sha1-in-want
If the upload-pack server advertises this capability, fetch-pack may send "want" lines with object names that exist at the server but are not advertised by upload-pack. For historical reasons, the name of this capability contains "sha1". Object names are always given using the object format negotiated through the _object-format_ capability.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_push_certnonce)push-cert=<nonce>
The receive-pack server that advertises this capability is willing to accept a signed push certificate, and asks the <nonce> to be included in the push certificate. A send-pack client MUST NOT send a push-cert packet unless the receive-pack server advertises this capability.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_filter)filter
If the upload-pack server advertises the _filter_ capability, fetch-pack may send "filter" commands to request a partial clone or partial fetch and request that the server omit various objects from the packfile.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_session_idsession_id)session-id=<session-id>
The server may advertise a session ID that can be used to identify this process across multiple requests. The client may advertise its own session ID back to the server as well.
Session IDs should be unique to a given process. They must fit within a packet-line, and must not contain non-printable or whitespace characters. The current implementation uses trace2 session IDs (see [api-trace2](https://git-scm.com/docs/api-trace2) for details), but this may change and users of the session ID should not rely on this fact.
##  [](https://git-scm.com/docs/gitprotocol-capabilities#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitprotocol-capabilities
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
