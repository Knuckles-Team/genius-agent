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
    * [NAME](https://git-scm.com/docs/gitprotocol-pack#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitprotocol-pack#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitprotocol-pack#_description)
    * [pkt-line Format](https://git-scm.com/docs/gitprotocol-pack#_pkt_line_format)
    * [Transports](https://git-scm.com/docs/gitprotocol-pack#_transports)
    * [Extra Parameters](https://git-scm.com/docs/gitprotocol-pack#_extra_parameters)
    * [Git Transport](https://git-scm.com/docs/gitprotocol-pack#_git_transport)
    * [SSH Transport](https://git-scm.com/docs/gitprotocol-pack#_ssh_transport)
    * [Fetching Data From a Server](https://git-scm.com/docs/gitprotocol-pack#_fetching_data_from_a_server)
    * [Reference Discovery](https://git-scm.com/docs/gitprotocol-pack#_reference_discovery)
    * [Packfile Negotiation](https://git-scm.com/docs/gitprotocol-pack#_packfile_negotiation)
    * [Packfile Data](https://git-scm.com/docs/gitprotocol-pack#_packfile_data)
    * [Pushing Data To a Server](https://git-scm.com/docs/gitprotocol-pack#_pushing_data_to_a_server)
    * [Authentication](https://git-scm.com/docs/gitprotocol-pack#_authentication)
    * [Reference Discovery](https://git-scm.com/docs/gitprotocol-pack#_reference_discovery_2)
    * [Reference Update Request and Packfile Transfer](https://git-scm.com/docs/gitprotocol-pack#_reference_update_request_and_packfile_transfer)
    * [Push Certificate](https://git-scm.com/docs/gitprotocol-pack#_push_certificate)
    * [Report Status](https://git-scm.com/docs/gitprotocol-pack#_report_status)
    * [GIT](https://git-scm.com/docs/gitprotocol-pack#_git)


[ English ▾](https://git-scm.com/docs/gitprotocol-pack)
Localized versions of **gitprotocol-pack** manual
  1. [English ](https://git-scm.com/docs/gitprotocol-pack)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitprotocol-pack)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitprotocol-pack) gitprotocol-pack last updated in 2.43.0
Changes in the **gitprotocol-pack** manual
  1. 2.43.1 → 2.53.0 no changes
  2. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/gitprotocol-pack/2.43.0)
  3. 2.38.1 → 2.42.4 no changes
  4. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/gitprotocol-pack/2.38.0)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitprotocol-pack#_name)NAME
gitprotocol-pack - How packs are transferred over-the-wire
##  [](https://git-scm.com/docs/gitprotocol-pack#_synopsis)SYNOPSIS
```
<over-the-wire-protocol>
```

##  [](https://git-scm.com/docs/gitprotocol-pack#_description)DESCRIPTION
Git supports transferring data in packfiles over the ssh://, git://, http:// and file:// transports. There exist two sets of protocols, one for pushing data from a client to a server and another for fetching data from a server to a client. The three transports (ssh, git, file) use the same protocol to transfer data. http is documented in [gitprotocol-http[5]](https://git-scm.com/docs/gitprotocol-http).
The processes invoked in the canonical Git implementation are _upload-pack_ on the server side and _fetch-pack_ on the client side for fetching data; then _receive-pack_ on the server and _send-pack_ on the client for pushing data. The protocol functions to have a server tell a client what is currently on the server, then for the two to negotiate the smallest amount of data to send in order to fully update one or the other.
##  [](https://git-scm.com/docs/gitprotocol-pack#_pkt_line_format)pkt-line Format
The descriptions below build on the pkt-line format described in [gitprotocol-common[5]](https://git-scm.com/docs/gitprotocol-common). When the grammar indicates `PKT-LINE`(`...`), unless otherwise noted the usual pkt-line LF rules apply: the sender SHOULD include a LF, but the receiver MUST NOT complain if it is not present.
An error packet is a special pkt-line that contains an error string.
```
  error-line     =  PKT-LINE("ERR" SP explanation-text)
```

Throughout the protocol, where `PKT-LINE`(`...`) is expected, an error packet MAY be sent. Once this packet is sent by a client or a server, the data transfer process defined in this protocol is terminated.
##  [](https://git-scm.com/docs/gitprotocol-pack#_transports)Transports
There are three transports over which the packfile protocol is initiated. The Git transport is a simple, unauthenticated server that takes the command (almost always _upload-pack_ , though Git servers can be configured to be globally writable, in which _receive- pack_ initiation is also allowed) with which the client wishes to communicate and executes it and connects it to the requesting process.
In the SSH transport, the client just runs the _upload-pack_ or _receive-pack_ process on the server over the SSH protocol and then communicates with that invoked process over the SSH connection.
The file:// transport runs the _upload-pack_ or _receive-pack_ process locally and communicates with it over a pipe.
##  [](https://git-scm.com/docs/gitprotocol-pack#_extra_parameters)Extra Parameters
The protocol provides a mechanism in which clients can send additional information in its first message to the server. These are called "Extra Parameters", and are supported by the Git, SSH, and HTTP protocols.
Each Extra Parameter takes the form of _< key>_`=`_< value>_ or _< key>_.
Servers that receive any such Extra Parameters MUST ignore all unrecognized keys. Currently, the only Extra Parameter recognized is "version" with a value of _1_ or _2_. See [gitprotocol-v2[5]](https://git-scm.com/docs/gitprotocol-v2) for more information on protocol version 2.
##  [](https://git-scm.com/docs/gitprotocol-pack#_git_transport)Git Transport
The Git transport starts off by sending the command and repository on the wire using the pkt-line format, followed by a NUL byte and a hostname parameter, terminated by a NUL byte.
```
0033git-upload-pack /project.git\0host=myserver.com\0
```

The transport may send Extra Parameters by adding an additional NUL byte, and then adding one or more NUL-terminated strings:
```
003egit-upload-pack /project.git\0host=myserver.com\0\0version=1\0
```

```
git-proto-request = request-command SP pathname NUL
      [ host-parameter NUL ] [ NUL extra-parameters ]
request-command   = "git-upload-pack" / "git-receive-pack" /
      "git-upload-archive"   ; case sensitive
pathname          = *( %x01-ff ) ; exclude NUL
host-parameter    = "host=" hostname [ ":" port ]
extra-parameters  = 1*extra-parameter
extra-parameter   = 1*( %x01-ff ) NUL
```

host-parameter is used for the git-daemon name based virtual hosting. See --interpolated-path option to git daemon, with the %H/%CH format characters.
Basically what the Git client is doing to connect to an _upload-pack_ process on the server side over the Git protocol is this:
```
$ echo -e -n \
  "003agit-upload-pack /schacon/gitbook.git\0host=example.com\0" |
  nc -v example.com 9418
```

##  [](https://git-scm.com/docs/gitprotocol-pack#_ssh_transport)SSH Transport
Initiating the upload-pack or receive-pack processes over SSH is executing the binary on the server via SSH remote execution. It is basically equivalent to running this:
```
$ ssh git.example.com "git-upload-pack '/project.git'"
```

For a server to support Git pushing and pulling for a given user over SSH, that user needs to be able to execute one or both of those commands via the SSH shell that they are provided on login. On some systems, that shell access is limited to only being able to run those two commands, or even just one of them.
In an ssh:// format URI, it’s absolute in the URI, so the _/_ after the host name (or port number) is sent as an argument, which is then read by the remote git-upload-pack exactly as is, so it’s effectively an absolute path in the remote filesystem.
```
   git clone ssh://user@example.com/project.git
  |
  v
ssh user@example.com "git-upload-pack '/project.git'"
```

In a "user@host:path" format URI, it’s relative to the user’s home directory, because the Git client will run:
```
   git clone user@example.com:project.git
    |
    v
ssh user@example.com "git-upload-pack 'project.git'"
```

The exception is if a _~_ is used, in which case we execute it without the leading _/_.
```
   ssh://user@example.com/~alice/project.git,
    |
    v
ssh user@example.com "git-upload-pack '~alice/project.git'"
```

Depending on the value of the `protocol.version` configuration variable, Git may attempt to send Extra Parameters as a colon-separated string in the GIT_PROTOCOL environment variable. This is done only if the `ssh.variant` configuration variable indicates that the ssh command supports passing environment variables as an argument.
A few things to remember here:
  * The "command name" is spelled with dash (e.g. git-upload-pack), but this can be overridden by the client;
  * The repository path is always quoted with single quotes.


##  [](https://git-scm.com/docs/gitprotocol-pack#_fetching_data_from_a_server)Fetching Data From a Server
When one Git repository wants to get data that a second repository has, the first can _fetch_ from the second. This operation determines what data the server has that the client does not then streams that data down to the client in packfile format.
##  [](https://git-scm.com/docs/gitprotocol-pack#_reference_discovery)Reference Discovery
When the client initially connects the server will immediately respond with a version number (if "version=1" is sent as an Extra Parameter), and a listing of each reference it has (all branches and tags) along with the object name that each reference currently points to.
```
 $ echo -e -n "0045git-upload-pack /schacon/gitbook.git\0host=example.com\0\0version=1\0" |
    nc -v example.com 9418
 000eversion 1
 00887217a7c7e582c46cec22a130adf4b9d7d950fba0 HEAD\0multi_ack thin-pack
side-band side-band-64k ofs-delta shallow no-progress include-tag
 00441d3fcd5ced445d1abc402225c0b8a1299641f497 refs/heads/integration
 003f7217a7c7e582c46cec22a130adf4b9d7d950fba0 refs/heads/master
 003cb88d2441cac0977faf98efc80305012112238d9d refs/tags/v0.9
 003c525128480b96c89e6418b1e40909bf6c5b2d580f refs/tags/v1.0
 003fe92df48743b7bc7d26bcaabfddde0a1e20cae47c refs/tags/v1.0^{}
 0000
```

The returned response is a pkt-line stream describing each ref and its current value. The stream MUST be sorted by name according to the C locale ordering.
If HEAD is a valid ref, HEAD MUST appear as the first advertised ref. If HEAD is not a valid ref, HEAD MUST NOT appear in the advertisement list at all, but other refs may still appear.
The stream MUST include capability declarations behind a NUL on the first ref. The peeled value of a ref (that is "ref^{}") MUST be immediately after the ref itself, if presented. A conforming server MUST peel the ref if it’s an annotated tag.
```
  advertised-refs  =  *1("version 1")
		      (no-refs / list-of-refs)
		      *shallow
		      flush-pkt

  no-refs          =  PKT-LINE(zero-id SP "capabilities^{}"
		      NUL capability-list)

  list-of-refs     =  first-ref *other-ref
  first-ref        =  PKT-LINE(obj-id SP refname
		      NUL capability-list)

  other-ref        =  PKT-LINE(other-tip / other-peeled)
  other-tip        =  obj-id SP refname
  other-peeled     =  obj-id SP refname "^{}"

  shallow          =  PKT-LINE("shallow" SP obj-id)

  capability-list  =  capability *(SP capability)
  capability       =  1*(LC_ALPHA / DIGIT / "-" / "_")
  LC_ALPHA         =  %x61-7A
```

Server and client MUST use lowercase for obj-id, both MUST treat obj-id as case-insensitive.
See protocol-capabilities.txt for a list of allowed server capabilities and descriptions.
##  [](https://git-scm.com/docs/gitprotocol-pack#_packfile_negotiation)Packfile Negotiation
After reference and capabilities discovery, the client can decide to terminate the connection by sending a flush-pkt, telling the server it can now gracefully terminate, and disconnect, when it does not need any pack data. This can happen with the ls-remote command, and also can happen when the client already is up to date.
Otherwise, it enters the negotiation phase, where the client and server determine what the minimal packfile necessary for transport is, by telling the server what objects it wants, its shallow objects (if any), and the maximum commit depth it wants (if any). The client will also send a list of the capabilities it wants to be in effect, out of what the server said it could do with the first _want_ line.
```
  upload-request    =  want-list
		       *shallow-line
		       *1depth-request
		       [filter-request]
		       flush-pkt

  want-list         =  first-want
		       *additional-want

  shallow-line      =  PKT-LINE("shallow" SP obj-id)

  depth-request     =  PKT-LINE("deepen" SP depth) /
		       PKT-LINE("deepen-since" SP timestamp) /
		       PKT-LINE("deepen-not" SP ref)

  first-want        =  PKT-LINE("want" SP obj-id SP capability-list)
  additional-want   =  PKT-LINE("want" SP obj-id)

  depth             =  1*DIGIT

  filter-request    =  PKT-LINE("filter" SP filter-spec)
```

Clients MUST send all the obj-ids it wants from the reference discovery phase as _want_ lines. Clients MUST send at least one _want_ command in the request body. Clients MUST NOT mention an obj-id in a _want_ command which did not appear in the response obtained through ref discovery.
The client MUST write all obj-ids which it only has shallow copies of (meaning that it does not have the parents of a commit) as _shallow_ lines so that the server is aware of the limitations of the client’s history.
The client now sends the maximum commit history depth it wants for this transaction, which is the number of commits it wants from the tip of the history, if any, as a _deepen_ line. A depth of 0 is the same as not making a depth request. The client does not want to receive any commits beyond this depth, nor does it want objects needed only to complete those commits. Commits whose parents are not received as a result are defined as shallow and marked as such in the server. This information is sent back to the client in the next step.
The client can optionally request that pack-objects omit various objects from the packfile using one of several filtering techniques. These are intended for use with partial clone and partial fetch operations. An object that does not meet a filter-spec value is omitted unless explicitly requested in a _want_ line. See `rev-list` for possible filter-spec values.
Once all the _want’s and 'shallow’s (and optional 'deepen_) are transferred, clients MUST send a flush-pkt, to tell the server side that it is done sending the list.
Otherwise, if the client sent a positive depth request, the server will determine which commits will and will not be shallow and send this information to the client. If the client did not request a positive depth, this step is skipped.
```
  shallow-update   =  *shallow-line
		      *unshallow-line
		      flush-pkt

  shallow-line     =  PKT-LINE("shallow" SP obj-id)

  unshallow-line   =  PKT-LINE("unshallow" SP obj-id)
```

If the client has requested a positive depth, the server will compute the set of commits which are no deeper than the desired depth. The set of commits starts at the client’s wants.
The server writes _shallow_ lines for each commit whose parents will not be sent as a result. The server writes an _unshallow_ line for each commit which the client has indicated is shallow, but is no longer shallow at the currently requested depth (that is, its parents will now be sent). The server MUST NOT mark as unshallow anything which the client has not indicated was shallow.
Now the client will send a list of the obj-ids it has using _have_ lines, so the server can make a packfile that only contains the objects that the client needs. In multi_ack mode, the canonical implementation will send up to 32 of these at a time, then will send a flush-pkt. The canonical implementation will skip ahead and send the next 32 immediately, so that there is always a block of 32 "in-flight on the wire" at a time.
```
  upload-haves      =  have-list
		       compute-end

  have-list         =  *have-line
  have-line         =  PKT-LINE("have" SP obj-id)
  compute-end       =  flush-pkt / PKT-LINE("done")
```

If the server reads _have_ lines, it then will respond by ACKing any of the obj-ids the client said it had that the server also has. The server will ACK obj-ids differently depending on which ack mode is chosen by the client.
In multi_ack mode:
  * the server will respond with _ACK obj-id continue_ for any common commits.
  * once the server has found an acceptable common base commit and is ready to make a packfile, it will blindly ACK all _have_ obj-ids back to the client.
  * the server will then send a _NAK_ and then wait for another response from the client - either a _done_ or another list of _have_ lines.


In multi_ack_detailed mode:
  * the server will differentiate the ACKs where it is signaling that it is ready to send data with _ACK obj-id ready_ lines, and signals the identified common commits with _ACK obj-id common_ lines.


Without either multi_ack or multi_ack_detailed:
  * upload-pack sends "ACK obj-id" on the first common object it finds. After that it says nothing until the client gives it a "done".
  * upload-pack sends "NAK" on a flush-pkt if no common object has been found yet. If one has been found, and thus an ACK was already sent, it’s silent on the flush-pkt.


After the client has gotten enough ACK responses that it can determine that the server has enough information to send an efficient packfile (in the canonical implementation, this is determined when it has received enough ACKs that it can color everything left in the --date-order queue as common with the server, or the --date-order queue is empty), or the client determines that it wants to give up (in the canonical implementation, this is determined when the client sends 256 _have_ lines without getting any of them ACKed by the server - meaning there is nothing in common and the server should just send all of its objects), then the client will send a _done_ command. The _done_ command signals to the server that the client is ready to receive its packfile data.
However, the 256 limit **only** turns on in the canonical client implementation if we have received at least one "ACK %s continue" during a prior round. This helps to ensure that at least one common ancestor is found before we give up entirely.
Once the _done_ line is read from the client, the server will either send a final _ACK obj-id_ or it will send a _NAK_. _obj-id_ is the object name of the last commit determined to be common. The server only sends ACK after _done_ if there is at least one common base and multi_ack or multi_ack_detailed is enabled. The server always sends NAK after _done_ if there is no common base found.
Instead of _ACK_ or _NAK_ , the server may send an error message (for example, if it does not recognize an object in a _want_ line received from the client).
Then the server will start sending its packfile data.
```
  server-response = *ack_multi ack / nak
  ack_multi       = PKT-LINE("ACK" SP obj-id ack_status)
  ack_status      = "continue" / "common" / "ready"
  ack             = PKT-LINE("ACK" SP obj-id)
  nak             = PKT-LINE("NAK")
```

A simple clone may look like this (with no _have_ lines):
```
   C: 0054want 74730d410fcb6603ace96f1dc55ea6196122532d multi_ack \
     side-band-64k ofs-delta\n
   C: 0032want 7d1665144a3a975c05f1f43902ddaf084e784dbe\n
   C: 0032want 5a3f6be755bbb7deae50065988cbfa1ffa9ab68a\n
   C: 0032want 7e47fe2bd8d01d481f44d7af0531bd93d3b21c01\n
   C: 0032want 74730d410fcb6603ace96f1dc55ea6196122532d\n
   C: 0000
   C: 0009done\n

   S: 0008NAK\n
   S: [PACKFILE]
```

An incremental update (fetch) response might look like this:
```
   C: 0054want 74730d410fcb6603ace96f1dc55ea6196122532d multi_ack \
     side-band-64k ofs-delta\n
   C: 0032want 7d1665144a3a975c05f1f43902ddaf084e784dbe\n
   C: 0032want 5a3f6be755bbb7deae50065988cbfa1ffa9ab68a\n
   C: 0000
   C: 0032have 7e47fe2bd8d01d481f44d7af0531bd93d3b21c01\n
   C: [30 more have lines]
   C: 0032have 74730d410fcb6603ace96f1dc55ea6196122532d\n
   C: 0000

   S: 003aACK 7e47fe2bd8d01d481f44d7af0531bd93d3b21c01 continue\n
   S: 003aACK 74730d410fcb6603ace96f1dc55ea6196122532d continue\n
   S: 0008NAK\n

   C: 0009done\n

   S: 0031ACK 74730d410fcb6603ace96f1dc55ea6196122532d\n
   S: [PACKFILE]
```

##  [](https://git-scm.com/docs/gitprotocol-pack#_packfile_data)Packfile Data
Now that the client and server have finished negotiation about what the minimal amount of data that needs to be sent to the client is, the server will construct and send the required data in packfile format.
See [gitformat-pack[5]](https://git-scm.com/docs/gitformat-pack) for what the packfile itself actually looks like.
If _side-band_ or _side-band-64k_ capabilities have been specified by the client, the server will send the packfile data multiplexed.
Each packet starting with the packet-line length of the amount of data that follows, followed by a single byte specifying the sideband the following data is coming in on.
In _side-band_ mode, it will send up to 999 data bytes plus 1 control code, for a total of up to 1000 bytes in a pkt-line. In _side-band-64k_ mode it will send up to 65519 data bytes plus 1 control code, for a total of up to 65520 bytes in a pkt-line.
The sideband byte will be a _1_ , _2_ or a _3_. Sideband _1_ will contain packfile data, sideband _2_ will be used for progress information that the client will generally print to stderr and sideband _3_ is used for error information.
If no _side-band_ capability was specified, the server will stream the entire packfile without multiplexing.
##  [](https://git-scm.com/docs/gitprotocol-pack#_pushing_data_to_a_server)Pushing Data To a Server
Pushing data to a server will invoke the _receive-pack_ process on the server, which will allow the client to tell it which references it should update and then send all the data the server will need for those new references to be complete. Once all the data is received and validated, the server will then update its references to what the client specified.
##  [](https://git-scm.com/docs/gitprotocol-pack#_authentication)Authentication
The protocol itself contains no authentication mechanisms. That is to be handled by the transport, such as SSH, before the _receive-pack_ process is invoked. If _receive-pack_ is configured over the Git transport, those repositories will be writable by anyone who can access that port (9418) as that transport is unauthenticated.
##  [](https://git-scm.com/docs/gitprotocol-pack#_reference_discovery_2)Reference Discovery
The reference discovery phase is done nearly the same way as it is in the fetching protocol. Each reference obj-id and name on the server is sent in packet-line format to the client, followed by a flush-pkt. The only real difference is that the capability listing is different - the only possible values are _report-status_ , _report-status-v2_ , _delete-refs_ , _ofs-delta_ , _atomic_ and _push-options_.
##  [](https://git-scm.com/docs/gitprotocol-pack#_reference_update_request_and_packfile_transfer)Reference Update Request and Packfile Transfer
Once the client knows what references the server is at, it can send a list of reference update requests. For each reference on the server that it wants to update, it sends a line listing the obj-id currently on the server, the obj-id the client would like to update it to and the name of the reference.
This list is followed by a flush-pkt.
```
  update-requests   =  *shallow ( command-list | push-cert )

  shallow           =  PKT-LINE("shallow" SP obj-id)

  command-list      =  PKT-LINE(command NUL capability-list)
		       *PKT-LINE(command)
		       flush-pkt

  command           =  create / delete / update
  create            =  zero-id SP new-id  SP name
  delete            =  old-id  SP zero-id SP name
  update            =  old-id  SP new-id  SP name

  old-id            =  obj-id
  new-id            =  obj-id

  push-cert         = PKT-LINE("push-cert" NUL capability-list LF)
		      PKT-LINE("certificate version 0.1" LF)
		      PKT-LINE("pusher" SP ident LF)
		      PKT-LINE("pushee" SP url LF)
		      PKT-LINE("nonce" SP nonce LF)
		      *PKT-LINE("push-option" SP push-option LF)
		      PKT-LINE(LF)
		      *PKT-LINE(command LF)
		      *PKT-LINE(gpg-signature-lines LF)
		      PKT-LINE("push-cert-end" LF)

  push-option       =  1*( VCHAR | SP )
```

If the server has advertised the _push-options_ capability and the client has specified _push-options_ as part of the capability list above, the client then sends its push options followed by a flush-pkt.
```
  push-options      =  *PKT-LINE(push-option) flush-pkt
```

For backwards compatibility with older Git servers, if the client sends a push cert and push options, it MUST send its push options both embedded within the push cert and after the push cert. (Note that the push options within the cert are prefixed, but the push options after the cert are not.) Both these lists MUST be the same, modulo the prefix.
After that the packfile that should contain all the objects that the server will need to complete the new references will be sent.
```
  packfile          =  "PACK" 28*(OCTET)
```

If the receiving end does not support delete-refs, the sending end MUST NOT ask for delete command.
If the receiving end does not support push-cert, the sending end MUST NOT send a push-cert command. When a push-cert command is sent, command-list MUST NOT be sent; the commands recorded in the push certificate is used instead.
The packfile MUST NOT be sent if the only command used is _delete_.
A packfile MUST be sent if either create or update command is used, even if the server already has all the necessary objects. In this case the client MUST send an empty packfile. The only time this is likely to happen is if the client is creating a new branch or a tag that points to an existing obj-id.
The server will receive the packfile, unpack it, then validate each reference that is being updated that it hasn’t changed while the request was being processed (the obj-id is still the same as the old-id), and it will run any update hooks to make sure that the update is acceptable. If all of that is fine, the server will then update the references.
##  [](https://git-scm.com/docs/gitprotocol-pack#_push_certificate)Push Certificate
A push certificate begins with a set of header lines. After the header and an empty line, the protocol commands follow, one per line. Note that the trailing LF in push-cert PKT-LINEs is _not_ optional; it must be present.
Currently, the following header fields are defined: 

[](https://git-scm.com/docs/gitprotocol-pack#Documentation/gitprotocol-pack.txt-pusherident)`pusher` ident 
    
Identify the GPG key in "Human Readable Name <email@address>" format. 

[](https://git-scm.com/docs/gitprotocol-pack#Documentation/gitprotocol-pack.txt-pusheeurl)`pushee` url 
    
The repository URL (anonymized, if the URL contains authentication material) the user who ran `git` `push` intended to push into. 

[](https://git-scm.com/docs/gitprotocol-pack#Documentation/gitprotocol-pack.txt-noncenonce)`nonce` nonce 
    
The _nonce_ string the receiving repository asked the pushing user to include in the certificate, to prevent replay attacks.
The GPG signature lines are a detached signature for the contents recorded in the push certificate before the signature block begins. The detached signature is used to certify that the commands were given by the pusher, who must be the signer.
##  [](https://git-scm.com/docs/gitprotocol-pack#_report_status)Report Status
After receiving the pack data from the sender, the receiver sends a report if _report-status_ or _report-status-v2_ capability is in effect. It is a short listing of what happened in that update. It will first list the status of the packfile unpacking as either _unpack ok_ or _unpack [error]_. Then it will list the status for each of the references that it tried to update. Each line is either _ok [refname]_ if the update was successful, or _ng [refname] [error]_ if the update was not.
```
  report-status     = unpack-status
		      1*(command-status)
		      flush-pkt

  unpack-status     = PKT-LINE("unpack" SP unpack-result)
  unpack-result     = "ok" / error-msg

  command-status    = command-ok / command-fail
  command-ok        = PKT-LINE("ok" SP refname)
  command-fail      = PKT-LINE("ng" SP refname SP error-msg)

  error-msg         = 1*(OCTET) ; where not "ok"
```

The _report-status-v2_ capability extends the protocol by adding new option lines in order to support reporting of reference rewritten by the _proc-receive_ hook. The _proc-receive_ hook may handle a command for a pseudo-reference which may create or update one or more references, and each reference may have different name, different new-oid, and different old-oid.
```
  report-status-v2  = unpack-status
		      1*(command-status-v2)
		      flush-pkt

  unpack-status     = PKT-LINE("unpack" SP unpack-result)
  unpack-result     = "ok" / error-msg

  command-status-v2 = command-ok-v2 / command-fail
  command-ok-v2     = command-ok
		      *option-line

  command-ok        = PKT-LINE("ok" SP refname)
  command-fail      = PKT-LINE("ng" SP refname SP error-msg)

  error-msg         = 1*(OCTET) ; where not "ok"

  option-line       = *1(option-refname)
		      *1(option-old-oid)
		      *1(option-new-oid)
		      *1(option-forced-update)

  option-refname    = PKT-LINE("option" SP "refname" SP refname)
  option-old-oid    = PKT-LINE("option" SP "old-oid" SP obj-id)
  option-new-oid    = PKT-LINE("option" SP "new-oid" SP obj-id)
  option-force      = PKT-LINE("option" SP "forced-update")
```

Updates can be unsuccessful for a number of reasons. The reference can have changed since the reference discovery phase was originally sent, meaning someone pushed in the meantime. The reference being pushed could be a non-fast-forward reference and the update hooks or configuration could be set to not allow that, etc. Also, some references can be updated while others can be rejected.
An example client/server communication might look like this:
```
   S: 006274730d410fcb6603ace96f1dc55ea6196122532d refs/heads/local\0report-status delete-refs ofs-delta\n
   S: 003e7d1665144a3a975c05f1f43902ddaf084e784dbe refs/heads/debug\n
   S: 003f74730d410fcb6603ace96f1dc55ea6196122532d refs/heads/master\n
   S: 003d74730d410fcb6603ace96f1dc55ea6196122532d refs/heads/team\n
   S: 0000

   C: 00677d1665144a3a975c05f1f43902ddaf084e784dbe 74730d410fcb6603ace96f1dc55ea6196122532d refs/heads/debug\n
   C: 006874730d410fcb6603ace96f1dc55ea6196122532d 5a3f6be755bbb7deae50065988cbfa1ffa9ab68a refs/heads/master\n
   C: 0000
   C: [PACKDATA]

   S: 000eunpack ok\n
   S: 0018ok refs/heads/debug\n
   S: 002ang refs/heads/master non-fast-forward\n
```

##  [](https://git-scm.com/docs/gitprotocol-pack#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitprotocol-pack
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
