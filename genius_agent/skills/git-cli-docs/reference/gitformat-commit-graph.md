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
    * [NAME](https://git-scm.com/docs/gitformat-commit-graph#_name)
    * [SYNOPSIS](https://git-scm.com/docs/gitformat-commit-graph#_synopsis)
    * [DESCRIPTION](https://git-scm.com/docs/gitformat-commit-graph#_description)
    * [Commit-graph files have the following format:](https://git-scm.com/docs/gitformat-commit-graph#_commit_graph_files_have_the_following_format)
    * [Historical Notes:](https://git-scm.com/docs/gitformat-commit-graph#_historical_notes)
    * [GIT](https://git-scm.com/docs/gitformat-commit-graph#_git)


[ English ▾](https://git-scm.com/docs/gitformat-commit-graph)
Localized versions of **gitformat-commit-graph** manual
  1. [English ](https://git-scm.com/docs/gitformat-commit-graph)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/gitformat-commit-graph)
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


[ Latest version ▾ ](https://git-scm.com/docs/gitformat-commit-graph) gitformat-commit-graph last updated in 2.47.0
Changes in the **gitformat-commit-graph** manual
  1. 2.47.1 → 2.53.0 no changes
  2. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/gitformat-commit-graph/2.47.0)
  3. 2.46.1 → 2.46.4 no changes
  4. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/gitformat-commit-graph/2.46.0)
  5. 2.39.1 → 2.45.4 no changes
  6. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/gitformat-commit-graph/2.39.0)
  7. 2.38.1 → 2.38.5 no changes
  8. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/gitformat-commit-graph/2.38.0)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/gitformat-commit-graph#_name)NAME
gitformat-commit-graph - Git commit-graph format
##  [](https://git-scm.com/docs/gitformat-commit-graph#_synopsis)SYNOPSIS
```
$GIT_DIR/objects/info/commit-graph
$GIT_DIR/objects/info/commit-graphs/*
```

##  [](https://git-scm.com/docs/gitformat-commit-graph#_description)DESCRIPTION
The Git commit-graph stores a list of commit OIDs and some associated metadata, including:
  * The generation number of the commit.
  * The root tree OID.
  * The commit date.
  * The parents of the commit, stored using positional references within the graph file.
  * The Bloom filter of the commit carrying the paths that were changed between the commit and its first parent, if requested.


These positional references are stored as unsigned 32-bit integers corresponding to the array position within the list of commit OIDs. Due to some special constants we use to track parents, we can store at most (1 << 30) + (1 << 29) + (1 << 28) - 1 (around 1.8 billion) commits.
##  [](https://git-scm.com/docs/gitformat-commit-graph#_commit_graph_files_have_the_following_format)Commit-graph files have the following format:
In order to allow extensions that add extra data to the graph, we organize the body into "chunks" and provide a binary lookup table at the beginning of the body. The header includes certain values, such as number of chunks and hash type.
All multi-byte numbers are in network byte order.
###  [](https://git-scm.com/docs/gitformat-commit-graph#_header)HEADER:
```
4-byte signature:
    The signature is: {'C', 'G', 'P', 'H'}
```

```
1-byte version number:
    Currently, the only valid version is 1.
```

```
 1-byte Hash Version
     We infer the hash length (H) from this value:
1 => SHA-1
2 => SHA-256
     If the hash type does not match the repository's hash algorithm, the
     commit-graph file should be ignored with a warning presented to the
     user.
```

```
1-byte number (C) of "chunks"
```

```
1-byte number (B) of base commit-graphs
    We infer the length (H*B) of the Base Graphs chunk
    from this value.
```

###  [](https://git-scm.com/docs/gitformat-commit-graph#_chunk_lookup)CHUNK LOOKUP:
```
(C + 1) * 12 bytes listing the table of contents for the chunks:
    First 4 bytes describe the chunk id. Value 0 is a terminating label.
    Other 8 bytes provide the byte-offset in current file for chunk to
    start. (Chunks are ordered contiguously in the file, so you can infer
    the length using the next chunk position if necessary.) Each chunk
    ID appears at most once.
```

```
The CHUNK LOOKUP matches the table of contents from
the chunk-based file format, see gitformat-chunk[5][](https://git-scm.com/docs/gitformat-chunk)
```

```
The remaining data in the body is described one chunk at a time, and
these chunks may be given in any order. Chunks are required unless
otherwise specified.
```

###  [](https://git-scm.com/docs/gitformat-commit-graph#_chunk_data)CHUNK DATA:
####  [](https://git-scm.com/docs/gitformat-commit-graph#_oid_fanout_id_o_i_d_f_256_4_bytes)OID Fanout (ID: {_O_ , _I_ , _D_ , _F_}) (256 * 4 bytes)
```
The ith entry, F[i], stores the number of OIDs with first
byte at most i. Thus F[255] stores the total
number of commits (N).
```

####  [](https://git-scm.com/docs/gitformat-commit-graph#_oid_lookup_id_o_i_d_l_n_h_bytes)OID Lookup (ID: {_O_ , _I_ , _D_ , _L_}) (N * H bytes)
```
The OIDs for all commits in the graph, sorted in ascending order.
```

####  [](https://git-scm.com/docs/gitformat-commit-graph#_commit_data_id_c_d_a_t_n_h_16_bytes)Commit Data (ID: {_C_ , _D_ , _A_ , _T_ }) (N * (H + 16) bytes)
  * The first H bytes are for the OID of the root tree.
  * The next 8 bytes are for the positions of the first two parents of the ith commit. Stores value 0x70000000 if no parent in that position. If there are more than two parents, the second value has its most-significant bit on and the other bits store an array position into the Extra Edge List chunk.
  * The next 8 bytes store the topological level (generation number v1) of the commit and the commit time in seconds since EPOCH. The generation number uses the higher 30 bits of the first 4 bytes, while the commit time uses the 32 bits of the second 4 bytes, along with the lowest 2 bits of the lowest byte, storing the 33rd and 34th bit of the commit time.


####  [](https://git-scm.com/docs/gitformat-commit-graph#_generation_data_id_g_d_a_2_n_4_bytes_optional)Generation Data (ID: {_G_ , _D_ , _A_ , _2_ }) (N * 4 bytes) [Optional]
  * This list of 4-byte values store corrected commit date offsets for the commits, arranged in the same order as commit data chunk.
  * If the corrected commit date offset cannot be stored within 31 bits, the value has its most-significant bit on and the other bits store the position of corrected commit date into the Generation Data Overflow chunk.
  * Generation Data chunk is present only when commit-graph file is written by compatible versions of Git and in case of split commit-graph chains, the topmost layer also has Generation Data chunk.


####  [](https://git-scm.com/docs/gitformat-commit-graph#_generation_data_overflow_id_g_d_o_2_optional)Generation Data Overflow (ID: {_G_ , _D_ , _O_ , _2_ }) [Optional]
  * This list of 8-byte values stores the corrected commit date offsets for commits with corrected commit date offsets that cannot be stored within 31 bits.
  * Generation Data Overflow chunk is present only when Generation Data chunk is present and at least one corrected commit date offset cannot be stored within 31 bits.


####  [](https://git-scm.com/docs/gitformat-commit-graph#_extra_edge_list_id_e_d_g_e_optional)Extra Edge List (ID: {_E_ , _D_ , _G_ , _E_}) [Optional]
```
This list of 4-byte values store the second through nth parents for
all octopus merges. The second parent value in the commit data stores
an array position within this list along with the most-significant bit
on. Starting at that array position, iterate through this list of commit
positions for the parents until reaching a value with the most-significant
bit on. The other bits correspond to the position of the last parent.
```

####  [](https://git-scm.com/docs/gitformat-commit-graph#_bloom_filter_index_id_b_i_d_x_n_4_bytes_optional)Bloom Filter Index (ID: {_B_ , _I_ , _D_ , _X_}) (N * 4 bytes) [Optional]
  * The ith entry, BIDX[i], stores the number of bytes in all Bloom filters from commit 0 to commit i (inclusive) in lexicographic order. The Bloom filter for the i-th commit spans from BIDX[i-1] to BIDX[i] (plus header length), where BIDX[-1] is 0.
  * The BIDX chunk is ignored if the BDAT chunk is not present.


####  [](https://git-scm.com/docs/gitformat-commit-graph#_bloom_filter_data_id_b_d_a_t_optional)Bloom Filter Data (ID: {_B_ , _D_ , _A_ , _T_}) [Optional]
  * It starts with header consisting of three unsigned 32-bit integers:
    * Version of the hash algorithm being used. We currently support value 2 which corresponds to the 32-bit version of the murmur3 hash implemented exactly as described in <https://en.wikipedia.org/wiki/MurmurHash#Algorithm> and the double hashing technique using seed values 0x293ae76f and 0x7e646e2 as described in <https://doi.org/10.1007/978-3-540-30494-4_26> "Bloom Filters in Probabilistic Verification". Version 1 Bloom filters have a bug that appears when char is signed and the repository has path names that have characters >= 0x80; Git supports reading and writing them, but this ability will be removed in a future version of Git.
    * The number of times a path is hashed and hence the number of bit positions that cumulatively determine whether a file is present in the commit.
    * The minimum number of bits _b_ per entry in the Bloom filter. If the filter contains _n_ entries, then the filter size is the minimum number of 64-bit words that contain n*b bits.
  * The rest of the chunk is the concatenation of all the computed Bloom filters for the commits in lexicographic order.
  * Note: Commits with no changes or more than 512 changes have Bloom filters of length one, with either all bits set to zero or one respectively.
  * The BDAT chunk is present if and only if BIDX is present.


####  [](https://git-scm.com/docs/gitformat-commit-graph#_base_graphs_list_id_b_a_s_e_optional)Base Graphs List (ID: {_B_ , _A_ , _S_ , _E_}) [Optional]
```
This list of H-byte hashes describe a set of B commit-graph files that
form a commit-graph chain. The graph position for the ith commit in this
file's OID Lookup chunk is equal to i plus the number of commits in all
base graphs.  If B is non-zero, this chunk must exist.
```

###  [](https://git-scm.com/docs/gitformat-commit-graph#_trailer)TRAILER:
```
H-byte HASH-checksum of all of the above.
```

##  [](https://git-scm.com/docs/gitformat-commit-graph#_historical_notes)Historical Notes:
The Generation Data (GDA2) and Generation Data Overflow (GDO2) chunks have the number _2_ in their chunk IDs because a previous version of Git wrote possibly erroneous data in these chunks with the IDs "GDAT" and "GDOV". By changing the IDs, newer versions of Git will silently ignore those older chunks and write the new information without trusting the incorrect data.
##  [](https://git-scm.com/docs/gitformat-commit-graph#_git)GIT
Part of the [git[1]](https://git-scm.com/docs/git) suite
### gitformat-commit-graph
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
