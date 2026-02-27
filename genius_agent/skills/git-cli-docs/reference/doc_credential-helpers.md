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


# Git credential helpers
This page lists available [credential helpers](https://git-scm.com/docs/gitcredentials).
## Included in Git
  * [git-credential-store](https://git-scm.com/docs/git-credential-store): saves credentials in plaintext.
  * [git-credential-cache](https://git-scm.com/docs/git-credential-cache): holds credentials temporarily in process memory. (Note that since credentials are lost when the cache expires or system restarts, this is inconvenient to store long-lived personal access tokens.)


## Platform specific storage
  * git-credential-osxkeychain: stores in [macOS keychain](https://support.apple.com/en-gb/guide/keychain-access/kyca1083/mac). Included in macOS Git installations.
  * git-credential-libsecret: stores in Linux secret service such as GNOME Keyring or KDE Wallet. [Packaged in many Linux distributions](https://pkgs.org/search/?q=git-credential-libsecret).
  * git-credential-wincred: stores in [Windows Credential Manager](https://support.microsoft.com/en-us/windows/accessing-credential-manager-1b5c916a-6a16-889f-8581-fc16e8165ac0). Included with Git for Windows.


## OAuth
The following cross-platform helpers support authentication using OAuth. Initial authentication opens a browser window to the host. Subsequent authentication happens in the background.
  * [Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager): included with Git for Windows. Supports multiple credential stores.
  * [git-credential-oauth](https://github.com/hickford/git-credential-oauth): included in many Linux distributions.


## Storage specific
  * [git-credential-gopass](https://github.com/gopasspw/git-credential-gopass): stores in gopass password manager.
  * [git-credential-lastpass](https://github.com/lastpass/lastpass-cli/blob/master/contrib/examples/git-credential-lastpass): stores in LastPass password manager.
  * [git-credential-1password](https://github.com/ethrgeist/git-credential-1password): stores in 1Password password manager.
  * [git-credential-keepassxc](https://github.com/Frederick888/git-credential-keepassxc): stores in KeePassXC password manager.


## Host specific
  * [git-credential-netlify](https://github.com/netlify/netlify-credential-helper): authenticates to Netlify.
  * [git-credential-azure](https://github.com/hickford/git-credential-azure): authenticates to Azure Repos.


[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
