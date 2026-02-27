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
    * [NAME](https://git-scm.com/docs/gitprotocol-v2#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitprotocol-v2#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitprotocol-v2#_description)
    * [Packet-Line Framing](https://git-scm.com/docs/gitprotocol-v2#_packet_line_framing)
    * [Initial Client Request](https://git-scm.com/docs/gitprotocol-v2#_initial_client_request)
    * [Capability Advertisement](https://git-scm.com/docs/gitprotocol-v2#_capability_advertisement)
    * [Command Request](https://git-scm.com/docs/gitprotocol-v2#_command_request)
    * [Capabilities](https://git-scm.com/docs/gitprotocol-v2#_capabilities)
    * [GIT](https://git-scm.com/docs/gitprotocol-v2#_git)


[ English ▾](https://git-scm.com/docs/gitprotocol-v2)
Localized versions of **gitprotocol-v2** manual
  1. [English ](https://git-scm.com/docs/gitprotocol-v2)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitprotocol-v2)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitprotocol-v2) gitprotocol-v2 last updated in 2.52.0
Changes in the **gitprotocol-v2** manual
  1. 2.53.0 no changes
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/gitprotocol-v2/2.52.0)
  3. 2.51.1 → 2.51.2 no changes
  4. [2.51.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-08-18_ ](https://git-scm.com/docs/gitprotocol-v2/2.51.0)
  5. 2.49.1 → 2.50.1 no changes
  6. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/gitprotocol-v2/2.49.0)
  7. 2.48.1 → 2.48.2 no changes
  8. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/gitprotocol-v2/2.48.0)
  9. 2.47.2 → 2.47.3 no changes
  10. [2.47.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-11-25_ ](https://git-scm.com/docs/gitprotocol-v2/2.47.1)
  11. 2.45.1 → 2.47.0 no changes
  12. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/gitprotocol-v2/2.45.0)
  13. 2.44.1 → 2.44.4 no changes
  14. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/gitprotocol-v2/2.44.0)
  15. 2.43.1 → 2.43.7 no changes
  16. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/gitprotocol-v2/2.43.0)
  17. 2.40.1 → 2.42.4 no changes
  18. [2.40.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-03-12_ ](https://git-scm.com/docs/gitprotocol-v2/2.40.0)
  19. 2.38.1 → 2.39.5 no changes
  20. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/gitprotocol-v2/2.38.0)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitprotocol-v2#_name)NAME
gitprotocol-v2 - Git Wire Protocol, Version 2
##  [](https://git-scm.com/docs/gitprotocol-v2#_synopsis)SYNOPSIS
```
<over-the-wire-protocol>
```

##  [](https://git-scm.com/docs/gitprotocol-v2#_description)DESCRIPTION
This document presents a specification for a version 2 of Git’s wire protocol. Protocol v2 will improve upon v1 in the following ways:
  * Instead of multiple service names, multiple commands will be supported by a single service
  * Easily extendable as capabilities are moved into their own section of the protocol, no longer being hidden behind a NUL byte and limited by the size of a pkt-line
  * Separate out other information hidden behind NUL bytes (e.g. agent string as a capability and symrefs can be requested using _ls-refs_)
  * Reference advertisement will be omitted unless explicitly requested
  * ls-refs command to explicitly request some refs
  * Designed with http and stateless-rpc in mind. With clear flush semantics the http remote helper can simply act as a proxy


In protocol v2 communication is command oriented. When first contacting a server a list of capabilities will be advertised. Some of these capabilities will be commands which a client can request be executed. Once a command has completed, a client can reuse the connection and request that other commands be executed.
##  [](https://git-scm.com/docs/gitprotocol-v2#_packet_line_framing)Packet-Line Framing
All communication is done using packet-line framing, just as in v1. See [gitprotocol-pack[5]](https://git-scm.com/docs/gitprotocol-pack) and [gitprotocol-common[5]](https://git-scm.com/docs/gitprotocol-common) for more information.
In protocol v2 these special packets will have the following semantics:
  * _0000_ Flush Packet (flush-pkt) - indicates the end of a message
  * _0001_ Delimiter Packet (delim-pkt) - separates sections of a message
  * _0002_ Response End Packet (response-end-pkt) - indicates the end of a response for stateless connections


##  [](https://git-scm.com/docs/gitprotocol-v2#_initial_client_request)Initial Client Request
In general a client can request to speak protocol v2 by sending `version=2` through the respective side-channel for the transport being used which inevitably sets `GIT_PROTOCOL`. More information can be found in [gitprotocol-pack[5]](https://git-scm.com/docs/gitprotocol-pack) and [gitprotocol-http[5]](https://git-scm.com/docs/gitprotocol-http), as well as the `GIT_PROTOCOL` definition in [git[1]](https://git-scm.com/docs/git). In all cases the response from the server is the capability advertisement.
###  [](https://git-scm.com/docs/gitprotocol-v2#_git_transport)Git Transport
When using the git:// transport, you can request to use protocol v2 by sending "version=2" as an extra parameter:
```
003egit-upload-pack /project.git\0host=myserver.com\0\0version=2\0
```

###  [](https://git-scm.com/docs/gitprotocol-v2#_ssh_and_file_transport)SSH and File Transport
When using either the ssh:// or file:// transport, the GIT_PROTOCOL environment variable must be set explicitly to include "version=2". The server may need to be configured to allow this environment variable to pass.
###  [](https://git-scm.com/docs/gitprotocol-v2#_http_transport)HTTP Transport
When using the http:// or https:// transport a client makes a "smart" info/refs request as described in [gitprotocol-http[5]](https://git-scm.com/docs/gitprotocol-http) and requests that v2 be used by supplying "version=2" in the `Git-Protocol` header.
```
C: GET $GIT_URL/info/refs?service=git-upload-pack HTTP/1.0
C: Git-Protocol: version=2
```

A v2 server would reply:
```
S: 200 OK
S: <Some headers>
S: ...
S:
S: 000eversion 2\n
S: <capability-advertisement>
```

Subsequent requests are then made directly to the service `$GIT_URL/git-upload-pack`. (This works the same for git-receive-pack).
Uses the `--http-backend-info-refs` option to [git-upload-pack[1]](https://git-scm.com/docs/git-upload-pack).
The server may need to be configured to pass this header’s contents via the `GIT_PROTOCOL` variable. See the discussion in [git-http-backend[1]](https://git-scm.com/docs/git-http-backend).
##  [](https://git-scm.com/docs/gitprotocol-v2#_capability_advertisement)Capability Advertisement
A server which decides to communicate (based on a request from a client) using protocol version 2, notifies the client by sending a version string in its initial response followed by an advertisement of its capabilities. Each capability is a key with an optional value. Clients must ignore all unknown keys. Semantics of unknown values are left to the definition of each key. Some capabilities will describe commands which can be requested to be executed by the client.
```
capability-advertisement = protocol-version
      capability-list
      flush-pkt
```

```
protocol-version = PKT-LINE("version 2" LF)
capability-list = *capability
capability = PKT-LINE(key[=value] LF)
```

```
key = 1*(ALPHA | DIGIT | "-_")
value = 1*(ALPHA | DIGIT | " -_.,?\/{}[]()<>!@#$%^&*+=:;")
```

##  [](https://git-scm.com/docs/gitprotocol-v2#_command_request)Command Request
After receiving the capability advertisement, a client can then issue a request to select the command it wants with any particular capabilities or arguments. There is then an optional section where the client can provide any command specific parameters or queries. Only a single command can be requested at a time.
```
request = empty-request | command-request
empty-request = flush-pkt
command-request = command
    capability-list
    delim-pkt
    command-args
    flush-pkt
command = PKT-LINE("command=" key LF)
command-args = *command-specific-arg
```

```
command-specific-args are packet line framed arguments defined by
each individual command.
```

The server will then check to ensure that the client’s request is comprised of a valid command as well as valid capabilities which were advertised. If the request is valid the server will then execute the command. A server MUST wait till it has received the client’s entire request before issuing a response. The format of the response is determined by the command being executed, but in all cases a flush-pkt indicates the end of the response.
When a command has finished, and the client has received the entire response from the server, a client can either request that another command be executed or can terminate the connection. A client may optionally send an empty request consisting of just a flush-pkt to indicate that no more requests will be made.
##  [](https://git-scm.com/docs/gitprotocol-v2#_capabilities)Capabilities
There are two different types of capabilities: normal capabilities, which can be used to convey information or alter the behavior of a request, and commands, which are the core actions that a client wants to perform (fetch, push, etc).
Protocol version 2 is stateless by default. This means that all commands must only last a single round and be stateless from the perspective of the server side, unless the client has requested a capability indicating that state should be maintained by the server. Clients MUST NOT require state management on the server side in order to function correctly. This permits simple round-robin load-balancing on the server side, without needing to worry about state management.
###  [](https://git-scm.com/docs/gitprotocol-v2#_agent)agent
The server can advertise the `agent` capability with a value `X` (in the form `agent=X`) to notify the client that the server is running version `X`. The client may optionally send its own agent string by including the `agent` capability with a value `Y` (in the form `agent=Y`) in its request to the server (but it MUST NOT do so if the server did not advertise the agent capability). The `X` and `Y` strings may contain any printable ASCII characters except space (i.e., the byte range 33 ⇐ x ⇐ 126), and are typically of the form "package/version-os" (e.g., "git/1.8.3.1-Linux") where `os` is the operating system name (e.g., "Linux"). `X` and `Y` can be configured using the GIT_USER_AGENT environment variable and it takes priority. The `os` is retrieved using the _sysname_ field of the `uname`(`2`) system call or its equivalent. The agent strings are purely informative for statistics and debugging purposes, and MUST NOT be used to programmatically assume the presence or absence of particular features.
###  [](https://git-scm.com/docs/gitprotocol-v2#_ls_refs)ls-refs
`ls-refs` is the command used to request a reference advertisement in v2. Unlike the current reference advertisement, ls-refs takes in arguments which can be used to limit the refs sent from the server.
Additional features not supported in the base command will be advertised as the value of the command in the capability advertisement in the form of a space separated list of features: "<command>=<feature-1> <feature-2>"
ls-refs takes in the following arguments:
```
   symrefs
In addition to the object pointed by it, show the underlying ref
pointed by it when showing a symbolic ref.
   peel
Show peeled tags.
   ref-prefix <prefix>
When specified, only references having a prefix matching one of
the provided prefixes are displayed. Multiple instances may be
given, in which case references matching any prefix will be
shown. Note that this is purely for optimization; a server MAY
show refs not matching the prefix if it chooses, and clients
should filter the result themselves.
```

If the _unborn_ feature is advertised the following argument can be included in the client’s request.
```
   unborn
The server will send information about HEAD even if it is a symref
pointing to an unborn branch in the form "unborn HEAD
symref-target:<target>".
```

The output of ls-refs is as follows:
```
output = *ref
  flush-pkt
obj-id-or-unborn = (obj-id | "unborn")
ref = PKT-LINE(obj-id-or-unborn SP refname *(SP ref-attribute) LF)
ref-attribute = (symref | peeled)
symref = "symref-target:" symref-target
peeled = "peeled:" obj-id
```

###  [](https://git-scm.com/docs/gitprotocol-v2#_fetch)fetch
`fetch` is the command used to fetch a packfile in v2. It can be looked at as a modified version of the v1 fetch where the ref-advertisement is stripped out (since the `ls-refs` command fills that role) and the message format is tweaked to eliminate redundancies and permit easy addition of future extensions.
Additional features not supported in the base command will be advertised as the value of the command in the capability advertisement in the form of a space separated list of features: "<command>=<feature-1> <feature-2>"
A `fetch` request can take the following arguments:
```
   want <oid>
Indicates to the server an object which the client wants to
retrieve.  Wants can be anything and are not limited to
advertised objects.
```

```
   have <oid>
Indicates to the server an object which the client has locally.
This allows the server to make a packfile which only contains
the objects that the client needs. Multiple 'have' lines can be
supplied.
```

```
   done
Indicates to the server that negotiation should terminate (or
not even begin if performing a clone) and that the server should
use the information supplied in the request to construct the
packfile.
```

```
   thin-pack
Request that a thin pack be sent, which is a pack with deltas
which reference base objects not contained within the pack (but
are known to exist at the receiving end). This can reduce the
network traffic significantly, but it requires the receiving end
to know how to "thicken" these packs by adding the missing bases
to the pack.
```

```
   no-progress
Request that progress information that would normally be sent on
side-band channel 2, during the packfile transfer, should not be
sent.  However, the side-band channel 3 is still used for error
responses.
```

```
   include-tag
Request that annotated tags should be sent if the objects they
point to are being sent.
```

```
   ofs-delta
Indicate that the client understands PACKv2 with delta referring
to its base by position in pack rather than by an oid.  That is,
they can read OBJ_OFS_DELTA (aka type 6) in a packfile.
```

If the _shallow_ feature is advertised the following arguments can be included in the clients request as well as the potential addition of the _shallow-info_ section in the server’s response as explained below.
```
   shallow <oid>
A client must notify the server of all commits for which it only
has shallow copies (meaning that it doesn't have the parents of
a commit) by supplying a 'shallow <oid>' line for each such
object so that the server is aware of the limitations of the
client's history.  This is so that the server is aware that the
client may not have all objects reachable from such commits.
```

```
   deepen <depth>
Requests that the fetch/clone should be shallow having a commit
depth of <depth> relative to the remote side.
```

```
   deepen-relative
Requests that the semantics of the "deepen" command be changed
to indicate that the depth requested is relative to the client's
current shallow boundary, instead of relative to the requested
commits.
```

```
   deepen-since <timestamp>
Requests that the shallow clone/fetch should be cut at a
specific time, instead of depth.  Internally it's equivalent to
doing "git rev-list --max-age=<timestamp>". Cannot be used with
"deepen".
```

```
   deepen-not <rev>
Requests that the shallow clone/fetch should be cut at a
specific revision specified by '<rev>', instead of a depth.
Internally it's equivalent of doing "git rev-list --not <rev>".
Cannot be used with "deepen", but can be used with
"deepen-since".
```

If the _filter_ feature is advertised, the following argument can be included in the client’s request:
```
   filter <filter-spec>
Request that various objects from the packfile be omitted
using one of several filtering techniques. These are intended
for use with partial clone and partial fetch operations. See
`rev-list` for possible "filter-spec" values. When communicating
with other processes, senders SHOULD translate scaled integers
(e.g. "1k") into a fully-expanded form (e.g. "1024") to aid
interoperability with older receivers that may not understand
newly-invented scaling suffixes. However, receivers SHOULD
accept the following suffixes: 'k', 'm', and 'g' for 1024,
1048576, and 1073741824, respectively.
```

If the _ref-in-want_ feature is advertised, the following argument can be included in the client’s request as well as the potential addition of the _wanted-refs_ section in the server’s response as explained below.
```
   want-ref <ref>
Indicates to the server that the client wants to retrieve a
particular ref, where <ref> is the full name of a ref on the
server.  It is a protocol error to send want-ref for the
same ref more than once.
```

If the _sideband-all_ feature is advertised, the following argument can be included in the client’s request:
```
   sideband-all
Instruct the server to send the whole response multiplexed, not just
the packfile section. All non-flush and non-delim PKT-LINE in the
response (not only in the packfile section) will then start with a byte
indicating its sideband (1, 2, or 3), and the server may send "0005\2"
(a PKT-LINE of sideband 2 with no payload) as a keepalive packet.
```

If the _packfile-uris_ feature is advertised, the following argument can be included in the client’s request as well as the potential addition of the _packfile-uris_ section in the server’s response as explained below. Note that at most one `packfile-uris` line can be sent to the server.
```
   packfile-uris <comma-separated-list-of-protocols>
Indicates to the server that the client is willing to receive
URIs of any of the given protocols in place of objects in the
sent packfile. Before performing the connectivity check, the
client should download from all given URIs. Currently, the
protocols supported are "http" and "https".
```

If the _wait-for-done_ feature is advertised, the following argument can be included in the client’s request.
```
   wait-for-done
Indicates to the server that it should never send "ready", but
should wait for the client to say "done" before sending the
packfile.
```

The response of `fetch` is broken into a number of sections separated by delimiter packets (0001), with each section beginning with its section header. Most sections are sent only when the packfile is sent.
```
output = acknowledgements flush-pkt |
  [acknowledgments delim-pkt] [shallow-info delim-pkt]
  [wanted-refs delim-pkt] [packfile-uris delim-pkt]
  packfile flush-pkt
```

```
acknowledgments = PKT-LINE("acknowledgments" LF)
    (nak | *ack)
    (ready)
ready = PKT-LINE("ready" LF)
nak = PKT-LINE("NAK" LF)
ack = PKT-LINE("ACK" SP obj-id LF)
```

```
shallow-info = PKT-LINE("shallow-info" LF)
 *PKT-LINE((shallow | unshallow) LF)
shallow = "shallow" SP obj-id
unshallow = "unshallow" SP obj-id
```

```
wanted-refs = PKT-LINE("wanted-refs" LF)
*PKT-LINE(wanted-ref LF)
wanted-ref = obj-id SP refname
```

```
packfile-uris = PKT-LINE("packfile-uris" LF) *packfile-uri
packfile-uri = PKT-LINE(40*(HEXDIGIT) SP *%x20-ff LF)
```

```
packfile = PKT-LINE("packfile" LF)
    *PKT-LINE(%x01-03 *%x00-ff)
```

```
   acknowledgments section
* If the client determines that it is finished with negotiations by
  sending a "done" line (thus requiring the server to send a packfile),
  the acknowledgments sections MUST be omitted from the server's
  response.
```

  * Always begins with the section header "acknowledgments"
  * The server will respond with "NAK" if none of the object ids sent as have lines were common.
  * The server will respond with "ACK obj-id" for all of the object ids sent as have lines which are common.
  * A response cannot have both "ACK" lines as well as a "NAK" line.
  * The server will respond with a "ready" line indicating that the server has found an acceptable common base and is ready to make and send a packfile (which will be found in the packfile section of the same response)
  * If the server has found a suitable cut point and has decided to send a "ready" line, then the server can decide to (as an optimization) omit any "ACK" lines it would have sent during its response. This is because the server will have already determined the objects it plans to send to the client and no further negotiation is needed.
```
   shallow-info section
* If the client has requested a shallow fetch/clone, a shallow
  client requests a fetch or the server is shallow then the
  server's response may include a shallow-info section.  The
  shallow-info section will be included if (due to one of the
  above conditions) the server needs to inform the client of any
  shallow boundaries or adjustments to the clients already
  existing shallow boundaries.
```

  * Always begins with the section header "shallow-info"
  * If a positive depth is requested, the server will compute the set of commits which are no deeper than the desired depth.
  * The server sends a "shallow obj-id" line for each commit whose parents will not be sent in the following packfile.
  * The server sends an "unshallow obj-id" line for each commit which the client has indicated is shallow, but is no longer shallow as a result of the fetch (due to its parents being sent in the following packfile).
  * The server MUST NOT send any "unshallow" lines for anything which the client has not indicated was shallow as a part of its request.
```
   wanted-refs section
* This section is only included if the client has requested a
  ref using a 'want-ref' line and if a packfile section is also
  included in the response.
```

  * Always begins with the section header "wanted-refs".
  * The server will send a ref listing ("<oid> <refname>") for each reference requested using _want-ref_ lines.
  * The server MUST NOT send any refs which were not requested using _want-ref_ lines.
```
   packfile-uris section
* This section is only included if the client sent
  'packfile-uris' and the server has at least one such URI to
  send.
```

  * Always begins with the section header "packfile-uris".
  * For each URI the server sends, it sends a hash of the pack’s contents (as output by git index-pack) followed by the URI.
  * The hashes are 40 hex characters long. When Git upgrades to a new hash algorithm, this might need to be updated. (It should match whatever index-pack outputs after "pack\t" or "keep\t".
```
   packfile section
* This section is only included if the client has sent 'want'
  lines in its request and either requested that no more
  negotiation be done by sending 'done' or if the server has
  decided it has found a sufficient cut point to produce a
  packfile.
```

  * Always begins with the section header "packfile"
  * The transmission of the packfile begins immediately after the section header
  * The data transfer of the packfile is always multiplexed, using the same semantics of the _side-band-64k_ capability from protocol version 1. This means that each packet, during the packfile data stream, is made up of a leading 4-byte pkt-line length (typical of the pkt-line format), followed by a 1-byte stream code, followed by the actual data.
```
 The stream code can be one of:
1 - pack data
2 - progress messages
3 - fatal error message just before stream aborts
```



###  [](https://git-scm.com/docs/gitprotocol-v2#_server_option)server-option
If advertised, indicates that any number of server specific options can be included in a request. This is done by sending each option as a "server-option=<option>" capability line in the capability-list section of a request.
The provided options must not contain a NUL or LF character.
###  [](https://git-scm.com/docs/gitprotocol-v2#_object_format)object-format
The server can advertise the `object-format` capability with a value `X` (in the form `object-format=X`) to notify the client that the server is able to deal with objects using hash algorithm X. If not specified, the server is assumed to only handle SHA-1. If the client would like to use a hash algorithm other than SHA-1, it should specify its object-format string.
###  [](https://git-scm.com/docs/gitprotocol-v2#_session_idsession_id)session-id=<session-id>
The server may advertise a session ID that can be used to identify this process across multiple requests. The client may advertise its own session ID back to the server as well.
Session IDs should be unique to a given process. They must fit within a packet-line, and must not contain non-printable or whitespace characters. The current implementation uses trace2 session IDs (see [api-trace2](https://git-scm.com/docs/api-trace2) for details), but this may change and users of the session ID should not rely on this fact.
###  [](https://git-scm.com/docs/gitprotocol-v2#_object_info)object-info
`object-info` is the command to retrieve information about one or more objects. Its main purpose is to allow a client to make decisions based on this information without having to fully fetch objects. Object size is the only information that is currently supported.
An `object-info` request takes the following arguments:
```
size
Requests size information to be returned for each listed object id.
```

```
oid <oid>
Indicates to the server an object which the client wants to obtain
information for.
```

The response of `object-info` is a list of the requested object ids and associated requested information, each separated by a single space.
```
output = info flush-pkt
```

```
info = PKT-LINE(attrs) LF)
	*PKT-LINE(obj-info LF)
```

```
attrs = attr | attrs SP attrs
```

```
attr = "size"
```

```
obj-info = obj-id SP obj-size
```

###  [](https://git-scm.com/docs/gitprotocol-v2#_bundle_uri)bundle-uri
If the _bundle-uri_ capability is advertised, the server supports the ‘bundle-uri’ command.
The capability is currently advertised with no value (i.e. not "bundle-uri=somevalue"), a value may be added in the future for supporting command-wide extensions. Clients MUST ignore any unknown capability values and proceed with the 'bundle-uri` dialog they support.
The _bundle-uri_ command is intended to be issued before `fetch` to get URIs to bundle files (see [git-bundle[1]](https://git-scm.com/docs/git-bundle)) to "seed" and inform the subsequent `fetch` command.
The client CAN issue `bundle-uri` before or after any other valid command. To be useful to clients it’s expected that it’ll be issued after an `ls-refs` and before `fetch`, but CAN be issued at any time in the dialog.
####  [](https://git-scm.com/docs/gitprotocol-v2#_discussion_of_bundle_uri)DISCUSSION of bundle-uri
The intent of the feature is optimize for server resource consumption in the common case by changing the common case of fetching a very large PACK during [git-clone[1]](https://git-scm.com/docs/git-clone) into a smaller incremental fetch.
It also allows servers to achieve better caching in combination with an `uploadpack.packObjectsHook` (see [git-config[1]](https://git-scm.com/docs/git-config)).
By having new clones or fetches be a more predictable and common negotiation against the tips of recently produces *.bundle file(s). Servers might even pre-generate the results of such negotiations for the `uploadpack.packObjectsHook` as new pushes come in.
One way that servers could take advantage of these bundles is that the server would anticipate that fresh clones will download a known bundle, followed by catching up to the current state of the repository using ref tips found in that bundle (or bundles).
####  [](https://git-scm.com/docs/gitprotocol-v2#_protocol_for_bundle_uri)PROTOCOL for bundle-uri
A `bundle-uri` request takes no arguments, and as noted above does not currently advertise a capability value. Both may be added in the future.
When the client issues a `command=bundle-uri` request, the response is a list of key-value pairs provided as packet lines with value _< key>_`=`_< value>_. Each _< key>_ should be interpreted as a config key from the `bundle.*` namespace to construct a list of bundles. These keys are grouped by a `bundle.`_< id>_`.` subsection, where each key corresponding to a given _< id>_ contributes attributes to the bundle defined by that _< id>_. See [git-config[1]](https://git-scm.com/docs/git-config) for the specific details of these keys and how the Git client will interpret their values.
Clients MUST parse the line according to the above format, lines that do not conform to the format SHOULD be discarded. The user MAY be warned in such a case.
####  [](https://git-scm.com/docs/gitprotocol-v2#_bundle_uri_client_and_server_expectations)bundle-uri CLIENT AND SERVER EXPECTATIONS 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-URICONTENTS)URI CONTENTS 
    
The content at the advertised URIs MUST be one of two types.
The advertised URI may contain a bundle file that `git` `bundle` `verify` would accept. I.e. they MUST contain one or more reference tips for use by the client, MUST indicate prerequisites (in any) with standard "-" prefixes, and MUST indicate their "object-format", if applicable.
The advertised URI may alternatively contain a plaintext file that `git` `config` `--list` would accept (with the `--file` option). The key-value pairs in this list are in the `bundle.*` namespace (see [git-config[1]](https://git-scm.com/docs/git-config)). 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-bundle-uriCLIENTERRORRECOVERY)bundle-uri CLIENT ERROR RECOVERY 
    
A client MUST above all gracefully degrade on errors, whether that error is because of bad missing/data in the bundle URI(s), because that client is too dumb to e.g. understand and fully parse out bundle headers and their prerequisite relationships, or something else.
Server operators should feel confident in turning on "bundle-uri" and not worry if e.g. their CDN goes down that clones or fetches will run into hard failures. Even if the server bundle(s) are incomplete, or bad in some way the client should still end up with a functioning repository, just as if it had chosen not to use this protocol extension.
All subsequent discussion on client and server interaction MUST keep this in mind. 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-bundle-uriSERVERTOCLIENT)bundle-uri SERVER TO CLIENT 
    
The ordering of the returned bundle uris is not significant. Clients MUST parse their headers to discover their contained OIDS and prerequisites. A client MUST consider the content of the bundle(s) themselves and their header as the ultimate source of truth.
A server MAY even return bundle(s) that don’t have any direct relationship to the repository being cloned (either through accident, or intentional "clever" configuration), and expect a client to sort out what data they’d like from the bundle(s), if any. 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-bundle-uriCLIENTTOSERVER)bundle-uri CLIENT TO SERVER 
    
The client SHOULD provide reference tips found in the bundle header(s) as _have_ lines in any subsequent `fetch` request. A client MAY also ignore the bundle(s) entirely if doing so is deemed worse for some reason, e.g. if the bundles can’t be downloaded, it doesn’t like the tips it finds etc. 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-WHENADVERTISEDBUNDLESREQUIRENOFURTHERNEGOTIATION)WHEN ADVERTISED BUNDLE(S) REQUIRE NO FURTHER NEGOTIATION 
    
If after issuing `bundle-uri` and `ls-refs`, and getting the header(s) of the bundle(s) the client finds that the ref tips it wants can be retrieved entirely from advertised bundle(s), the client MAY disconnect from the Git server. The results of such a _clone_ or _fetch_ should be indistinguishable from the state attained without using bundle-uri. 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-EARLYCLIENTDISCONNECTIONSANDERRORRECOVERY)EARLY CLIENT DISCONNECTIONS AND ERROR RECOVERY 
    
A client MAY perform an early disconnect while still downloading the bundle(s) (having streamed and parsed their headers). In such a case the client MUST gracefully recover from any errors related to finishing the download and validation of the bundle(s).
I.e. a client might need to re-connect and issue a _fetch_ command, and possibly fall back to not making use of _bundle-uri_ at all.
This "MAY" behavior is specified as such (and not a "SHOULD") on the assumption that a server advertising bundle uris is more likely than not to be serving up a relatively large repository, and to be pointing to URIs that have a good chance of being in working order. A client MAY e.g. look at the payload size of the bundles as a heuristic to see if an early disconnect is worth it, should falling back on a full "fetch" dialog be necessary. 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-WHENADVERTISEDBUNDLESREQUIREFURTHERNEGOTIATION)WHEN ADVERTISED BUNDLE(S) REQUIRE FURTHER NEGOTIATION 
    
A client SHOULD commence a negotiation of a PACK from the server via the "fetch" command using the OID tips found in advertised bundles, even if’s still in the process of downloading those bundle(s).
This allows for aggressive early disconnects from any interactive server dialog. The client blindly trusts that the advertised OID tips are relevant, and issues them as _have_ lines, it then requests any tips it would like (usually from the "ls-refs" advertisement) via _want_ lines. The server will then compute a (hopefully small) PACK with the expected difference between the tips from the bundle(s) and the data requested.
The only connection the client then needs to keep active is to the concurrently downloading static bundle(s), when those and the incremental PACK are retrieved they should be inflated and validated. Any errors at this point should be gracefully recovered from, see above.
####  [](https://git-scm.com/docs/gitprotocol-v2#_bundle_uri_protocol_features)bundle-uri PROTOCOL FEATURES
The client constructs a bundle list from the _< key>_`=`_< value>_ pairs provided by the server. These pairs are part of the `bundle.*` namespace as documented in [git-config[1]](https://git-scm.com/docs/git-config). In this section, we discuss some of these keys and describe the actions the client will do in response to this information.
In particular, the `bundle.version` key specifies an integer value. The only accepted value at the moment is `1`, but if the client sees an unexpected value here then the client MUST ignore the bundle list.
As long as `bundle.version` is understood, all other unknown keys MAY be ignored by the client. The server will guarantee compatibility with older clients, though newer clients may be better able to use the extra keys to minimize downloads.
Any backwards-incompatible addition of pre-URI key-value will be guarded by a new `bundle.version` value or values in _bundle-uri_ capability advertisement itself, and/or by new future `bundle-uri` request arguments.
Some example key-value pairs that are not currently implemented but could be implemented in the future include:
  * Add a "hash=<val>" or "size=<bytes>" advertise the expected hash or size of the bundle file.
  * Advertise that one or more bundle files are the same (to e.g. have clients round-robin or otherwise choose one of N possible files).
  * A "oid=<OID>" shortcut and "prerequisite=<OID>" shortcut. For expressing the common case of a bundle with one tip and no prerequisites, or one tip and one prerequisite.
This would allow for optimizing the common case of servers who’d like to provide one "big bundle" containing only their "main" branch, and/or incremental updates thereof.
A client receiving such a response MAY assume that they can skip retrieving the header from a bundle at the indicated URI, and thus save themselves and the server(s) the request(s) needed to inspect the headers of that bundle or bundles.


###  [](https://git-scm.com/docs/gitprotocol-v2#_promisor_remotepr_info)promisor-remote=<pr-info>
The server may advertise some promisor remotes it is using or knows about to a client which may want to use them as its promisor remotes, instead of this repository. In this case <pr-info> should be of the form:
```
pr-info = pr-fields | pr-info ";" pr-fields
```

```
pr-fields = pr-field | pr-fields "," pr-field
```

```
pr-field = field-name "=" field-value
```

where all the `field-name` and `field-value` in a given `pr-fields` are field names and values related to a single promisor remote. A given `field-name` MUST NOT appear more than once in given `pr-fields`.
The server MUST advertise at least the "name" and "url" field names along with the associated field values, which are the name of a valid remote and its URL, in each `pr-fields`. The "name" and "url" fields MUST appear first in each pr-fields, in that order.
After these mandatory fields, the server MAY advertise the following optional fields in any order: 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-partialCloneFilter)`partialCloneFilter` 
    
The filter specification used by the remote. Clients can use this to determine if the remote’s filtering strategy is compatible with their needs (e.g., checking if both use "blob:none"). It corresponds to the "remote.<name>.partialCloneFilter" config setting. 

[](https://git-scm.com/docs/gitprotocol-v2#Documentation/gitprotocol-v2.txt-token)`token` 
    
An authentication token that clients can use when connecting to the remote. It corresponds to the "remote.<name>.token" config setting.
No other fields are defined by the protocol at this time. Field names are case-sensitive and MUST be transmitted exactly as specified above. Clients MUST ignore fields they don’t recognize to allow for future protocol extensions.
For now, the client can only use information transmitted through these fields to decide if it accepts the advertised promisor remote. In the future that information might be used for other purposes though.
Field values MUST be urlencoded.
If the client decides to use one or more promisor remotes the server advertised, it can reply with "promisor-remote=<pr-names>" where <pr-names> should be of the form:
```
pr-names = pr-name | pr-names ";" pr-name
```

where `pr-name` is the urlencoded name of a promisor remote the server advertised and the client accepts.
Note that, everywhere in this document, the _;_ and _,_ characters MUST be encoded if they appear in `pr-name` or `field-value`.
If the server doesn’t know any promisor remote that could be good for a client to use, or prefers a client not to use any promisor remote it uses or knows about, it shouldn’t advertise the "promisor-remote" capability at all.
In this case, or if the client doesn’t want to use any promisor remote the server advertised, the client shouldn’t advertise the "promisor-remote" capability at all in its reply.
On the server side, the "promisor.advertise" and "promisor.sendFields" configuration options can be used to control what it advertises. On the client side, the "promisor.acceptFromServer" configuration option can be used to control what it accepts. See the documentation of these configuration options for more information.
Note that in the future it would be nice if the "promisor-remote" protocol capability could be used by the server, when responding to `git` `fetch` or `git` `clone`, to advertise better-connected remotes that the client can use as promisor remotes, instead of this repository, so that the client can lazily fetch objects from these other better-connected remotes. This would require the server to omit in its response the objects available on the better-connected remotes that the client has accepted. This hasn’t been implemented yet though. So for now this "promisor-remote" capability is useful only when the server advertises some promisor remotes it already uses to borrow objects from.
##  [](https://git-scm.com/docs/gitprotocol-v2#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitprotocol-v2
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
