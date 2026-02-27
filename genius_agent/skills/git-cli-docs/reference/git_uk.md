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
    * [НАЗВА](https://git-scm.com/docs/git/uk#_%d0%bd%d0%b0%d0%b7%d0%b2%d0%b0)
    * [СИНОПСИС](https://git-scm.com/docs/git/uk#_%d1%81%d0%b8%d0%bd%d0%be%d0%bf%d1%81%d0%b8%d1%81)
    * [ОПИС](https://git-scm.com/docs/git/uk#_%d0%be%d0%bf%d0%b8%d1%81)
    * [ОПЦІЇ](https://git-scm.com/docs/git/uk#_%d0%be%d0%bf%d1%86%d1%96%d1%97)
    * [GIT-КОМАНДИ](https://git-scm.com/docs/git/uk#_git_%d0%ba%d0%be%d0%bc%d0%b0%d0%bd%d0%b4%d0%b8)
    * [Команди високого рівня (порцеляна)](https://git-scm.com/docs/git/uk#_%d0%ba%d0%be%d0%bc%d0%b0%d0%bd%d0%b4%d0%b8_%d0%b2%d0%b8%d1%81%d0%be%d0%ba%d0%be%d0%b3%d0%be_%d1%80%d1%96%d0%b2%d0%bd%d1%8f_%d0%bf%d0%be%d1%80%d1%86%d0%b5%d0%bb%d1%8f%d0%bd%d0%b0)
    * [Низькорівневі команди (сантехніка)](https://git-scm.com/docs/git/uk#_%d0%bd%d0%b8%d0%b7%d1%8c%d0%ba%d0%be%d1%80%d1%96%d0%b2%d0%bd%d0%b5%d0%b2%d1%96_%d0%ba%d0%be%d0%bc%d0%b0%d0%bd%d0%b4%d0%b8_%d1%81%d0%b0%d0%bd%d1%82%d0%b5%d1%85%d0%bd%d1%96%d0%ba%d0%b0)
    * [Путівники](https://git-scm.com/docs/git/uk#_%d0%bf%d1%83%d1%82%d1%96%d0%b2%d0%bd%d0%b8%d0%ba%d0%b8)
    * [Інтерфейси репозиторію, команд та файлів](https://git-scm.com/docs/git/uk#_%d1%96%d0%bd%d1%82%d0%b5%d1%80%d1%84%d0%b5%d0%b9%d1%81%d0%b8_%d1%80%d0%b5%d0%bf%d0%be%d0%b7%d0%b8%d1%82%d0%be%d1%80%d1%96%d1%8e_%d0%ba%d0%be%d0%bc%d0%b0%d0%bd%d0%b4_%d1%82%d0%b0_%d1%84%d0%b0%d0%b9%d0%bb%d1%96%d0%b2)
    * [Формати файлів, протоколи та інші інтерфейси розробника](https://git-scm.com/docs/git/uk#_%d1%84%d0%be%d1%80%d0%bc%d0%b0%d1%82%d0%b8_%d1%84%d0%b0%d0%b9%d0%bb%d1%96%d0%b2_%d0%bf%d1%80%d0%be%d1%82%d0%be%d0%ba%d0%be%d0%bb%d0%b8_%d1%82%d0%b0_%d1%96%d0%bd%d1%88%d1%96_%d1%96%d0%bd%d1%82%d0%b5%d1%80%d1%84%d0%b5%d0%b9%d1%81%d0%b8_%d1%80%d0%be%d0%b7%d1%80%d0%be%d0%b1%d0%bd%d0%b8%d0%ba%d0%b0)
    * [Механізм конфігурації](https://git-scm.com/docs/git/uk#_%d0%bc%d0%b5%d1%85%d0%b0%d0%bd%d1%96%d0%b7%d0%bc_%d0%ba%d0%be%d0%bd%d1%84%d1%96%d0%b3%d1%83%d1%80%d0%b0%d1%86%d1%96%d1%97)
    * [Термінологія ідентифікаторів](https://git-scm.com/docs/git/uk#_%d1%82%d0%b5%d1%80%d0%bc%d1%96%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d1%96%d1%8f_%d1%96%d0%b4%d0%b5%d0%bd%d1%82%d0%b8%d1%84%d1%96%d0%ba%d0%b0%d1%82%d0%be%d1%80%d1%96%d0%b2)
    * [Символічні ідентифікатори](https://git-scm.com/docs/git/uk#_%d1%81%d0%b8%d0%bc%d0%b2%d0%be%d0%bb%d1%96%d1%87%d0%bd%d1%96_%d1%96%d0%b4%d0%b5%d0%bd%d1%82%d0%b8%d1%84%d1%96%d0%ba%d0%b0%d1%82%d0%be%d1%80%d0%b8)
    * [Структура файлів/каталогів](https://git-scm.com/docs/git/uk#_%d1%81%d1%82%d1%80%d1%83%d0%ba%d1%82%d1%83%d1%80%d0%b0_%d1%84%d0%b0%d0%b9%d0%bb%d1%96%d0%b2%d0%ba%d0%b0%d1%82%d0%b0%d0%bb%d0%be%d0%b3%d1%96%d0%b2)
    * [Термінологія](https://git-scm.com/docs/git/uk#_%d1%82%d0%b5%d1%80%d0%bc%d1%96%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d1%96%d1%8f)
    * [Змінні середовища](https://git-scm.com/docs/git/uk#_%d0%b7%d0%bc%d1%96%d0%bd%d0%bd%d1%96_%d1%81%d0%b5%d1%80%d0%b5%d0%b4%d0%be%d0%b2%d0%b8%d1%89%d0%b0)
    * [Обговорення](https://git-scm.com/docs/git/uk#_%d0%be%d0%b1%d0%b3%d0%be%d0%b2%d0%be%d1%80%d0%b5%d0%bd%d0%bd%d1%8f)
    * [БЕЗПЕКА](https://git-scm.com/docs/git/uk#_%d0%b1%d0%b5%d0%b7%d0%bf%d0%b5%d0%ba%d0%b0)
    * [ДОДАТКОВА ДОКУМЕНТАЦІЯ](https://git-scm.com/docs/git/uk#_%d0%b4%d0%be%d0%b4%d0%b0%d1%82%d0%ba%d0%be%d0%b2%d0%b0_%d0%b4%d0%be%d0%ba%d1%83%d0%bc%d0%b5%d0%bd%d1%82%d0%b0%d1%86%d1%96%d1%8f)
    * [Автори](https://git-scm.com/docs/git/uk#_%d0%b0%d0%b2%d1%82%d0%be%d1%80%d0%b8)
    * [Повідомлення про помилки](https://git-scm.com/docs/git/uk#_%d0%bf%d0%be%d0%b2%d1%96%d0%b4%d0%be%d0%bc%d0%bb%d0%b5%d0%bd%d0%bd%d1%8f_%d0%bf%d1%80%d0%be_%d0%bf%d0%be%d0%bc%d0%b8%d0%bb%d0%ba%d0%b8)
    * [ДИВ. ТАКОЖ](https://git-scm.com/docs/git/uk#_%d0%b4%d0%b8%d0%b2_%d1%82%d0%b0%d0%ba%d0%be%d0%b6)
    * [GIT](https://git-scm.com/docs/git/uk#_git)


[ українська мова ▾](https://git-scm.com/docs/git/uk)
Localized versions of **git** manual
  1. [English ](https://git-scm.com/docs/git)
  2. [Deutsch ](https://git-scm.com/docs/git/de)
  3. [Español ](https://git-scm.com/docs/git/es)
  4. [Français ](https://git-scm.com/docs/git/fr)
  5. [Português (Brasil) ](https://git-scm.com/docs/git/pt_BR)
  6. [Svenska ](https://git-scm.com/docs/git/sv)
  7. [українська мова ](https://git-scm.com/docs/git/uk)
  8. [简体中文 ](https://git-scm.com/docs/git/zh_HANS-CN)

Want to read in your language or fix typos?  
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). 
[Topics ▾](https://git-scm.com/docs/git/uk)
### Setup and Config
  * [ git ](https://git-scm.com/docs/git/uk)
  * [ config ](https://git-scm.com/docs/git-config/uk)
  * [ help ](https://git-scm.com/docs/git-help/uk)
  * [ bugreport ](https://git-scm.com/docs/git-bugreport/uk)
  * [ Credential helpers ](https://git-scm.com/doc/credential-helpers)


### Getting and Creating Projects
  * [ init ](https://git-scm.com/docs/git-init/uk)
  * [ clone ](https://git-scm.com/docs/git-clone/uk)


### Basic Snapshotting
  * [ add ](https://git-scm.com/docs/git-add/uk)
  * [ status ](https://git-scm.com/docs/git-status/uk)
  * [ diff ](https://git-scm.com/docs/git-diff/uk)
  * [ commit ](https://git-scm.com/docs/git-commit/uk)
  * [ notes ](https://git-scm.com/docs/git-notes/uk)
  * [ restore ](https://git-scm.com/docs/git-restore/uk)
  * [ reset ](https://git-scm.com/docs/git-reset/uk)
  * [ rm ](https://git-scm.com/docs/git-rm/uk)
  * [ mv ](https://git-scm.com/docs/git-mv/uk)


### Branching and Merging
  * [ branch ](https://git-scm.com/docs/git-branch/uk)
  * [ checkout ](https://git-scm.com/docs/git-checkout/uk)
  * [ switch ](https://git-scm.com/docs/git-switch/uk)
  * [ merge ](https://git-scm.com/docs/git-merge/uk)
  * [ mergetool ](https://git-scm.com/docs/git-mergetool/uk)
  * [ log ](https://git-scm.com/docs/git-log/uk)
  * [ stash ](https://git-scm.com/docs/git-stash/uk)
  * [ tag ](https://git-scm.com/docs/git-tag/uk)
  * [ worktree ](https://git-scm.com/docs/git-worktree/uk)


### Sharing and Updating Projects
  * [ fetch ](https://git-scm.com/docs/git-fetch/uk)
  * [ pull ](https://git-scm.com/docs/git-pull/uk)
  * [ push ](https://git-scm.com/docs/git-push/uk)
  * [ remote ](https://git-scm.com/docs/git-remote/uk)
  * [ submodule ](https://git-scm.com/docs/git-submodule/uk)


### Inspection and Comparison
  * [ show ](https://git-scm.com/docs/git-show/uk)
  * [ log ](https://git-scm.com/docs/git-log/uk)
  * [ diff ](https://git-scm.com/docs/git-diff/uk)
  * [ difftool ](https://git-scm.com/docs/git-difftool/uk)
  * [ range-diff ](https://git-scm.com/docs/git-range-diff/uk)
  * [ shortlog ](https://git-scm.com/docs/git-shortlog/uk)
  * [ describe ](https://git-scm.com/docs/git-describe/uk)


### Patching
  * [ apply ](https://git-scm.com/docs/git-apply/uk)
  * [ cherry-pick ](https://git-scm.com/docs/git-cherry-pick/uk)
  * [ diff ](https://git-scm.com/docs/git-diff/uk)
  * [ rebase ](https://git-scm.com/docs/git-rebase/uk)
  * [ revert ](https://git-scm.com/docs/git-revert/uk)


### Debugging
  * [ bisect ](https://git-scm.com/docs/git-bisect/uk)
  * [ blame ](https://git-scm.com/docs/git-blame/uk)
  * [ grep ](https://git-scm.com/docs/git-grep/uk)


### Email
  * [ am ](https://git-scm.com/docs/git-am/uk)
  * [ apply ](https://git-scm.com/docs/git-apply/uk)
  * [ imap-send ](https://git-scm.com/docs/git-imap-send/uk)
  * [ format-patch ](https://git-scm.com/docs/git-format-patch/uk)
  * [ send-email ](https://git-scm.com/docs/git-send-email/uk)
  * [ request-pull ](https://git-scm.com/docs/git-request-pull/uk)


### External Systems
  * [ svn ](https://git-scm.com/docs/git-svn/uk)
  * [ fast-import ](https://git-scm.com/docs/git-fast-import/uk)


### Server Admin
  * [ daemon ](https://git-scm.com/docs/git-daemon/uk)
  * [ update-server-info ](https://git-scm.com/docs/git-update-server-info/uk)


### Guides
  * [ gitattributes ](https://git-scm.com/docs/gitattributes)
  * [ Command-line interface conventions ](https://git-scm.com/docs/gitcli)
  * [ Everyday Git ](https://git-scm.com/docs/giteveryday)
  * [ Frequently Asked Questions (FAQ) ](https://git-scm.com/docs/gitfaq)
  * [ Glossary ](https://git-scm.com/docs/gitglossary/uk)
  * [ Hooks ](https://git-scm.com/docs/githooks)
  * [ gitignore ](https://git-scm.com/docs/gitignore/uk)
  * [ gitmodules ](https://git-scm.com/docs/gitmodules)
  * [ Revisions ](https://git-scm.com/docs/gitrevisions)
  * [ Submodules ](https://git-scm.com/docs/gitsubmodules)
  * [ Tutorial ](https://git-scm.com/docs/gittutorial)
  * [ Workflows ](https://git-scm.com/docs/gitworkflows)
  * [ All guides... ](https://git-scm.com/docs/git#_guides)


### Administration
  * [ clean ](https://git-scm.com/docs/git-clean/uk)
  * [ gc ](https://git-scm.com/docs/git-gc/uk)
  * [ fsck ](https://git-scm.com/docs/git-fsck/uk)
  * [ reflog ](https://git-scm.com/docs/git-reflog/uk)
  * [ filter-branch ](https://git-scm.com/docs/git-filter-branch/uk)
  * [ instaweb ](https://git-scm.com/docs/git-instaweb/uk)
  * [ archive ](https://git-scm.com/docs/git-archive/uk)
  * [ bundle ](https://git-scm.com/docs/git-bundle/uk)


### Plumbing Commands
  * [ cat-file ](https://git-scm.com/docs/git-cat-file/uk)
  * [ check-ignore ](https://git-scm.com/docs/git-check-ignore/uk)
  * [ checkout-index ](https://git-scm.com/docs/git-checkout-index/uk)
  * [ commit-tree ](https://git-scm.com/docs/git-commit-tree/uk)
  * [ count-objects ](https://git-scm.com/docs/git-count-objects/uk)
  * [ diff-index ](https://git-scm.com/docs/git-diff-index/uk)
  * [ for-each-ref ](https://git-scm.com/docs/git-for-each-ref/uk)
  * [ hash-object ](https://git-scm.com/docs/git-hash-object/uk)
  * [ ls-files ](https://git-scm.com/docs/git-ls-files/uk)
  * [ ls-tree ](https://git-scm.com/docs/git-ls-tree/uk)
  * [ merge-base ](https://git-scm.com/docs/git-merge-base/uk)
  * [ read-tree ](https://git-scm.com/docs/git-read-tree/uk)
  * [ rev-list ](https://git-scm.com/docs/git-rev-list/uk)
  * [ rev-parse ](https://git-scm.com/docs/git-rev-parse/uk)
  * [ show-ref ](https://git-scm.com/docs/git-show-ref/uk)
  * [ symbolic-ref ](https://git-scm.com/docs/git-symbolic-ref/uk)
  * [ update-index ](https://git-scm.com/docs/git-update-index/uk)
  * [ update-ref ](https://git-scm.com/docs/git-update-ref/uk)
  * [ verify-pack ](https://git-scm.com/docs/git-verify-pack/uk)
  * [ write-tree ](https://git-scm.com/docs/git-write-tree/uk)


[ Latest version ▾ ](https://git-scm.com/docs/git/uk) git last updated in 2.53.0
Changes in the **git** manual
  1. [2.53.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2026-02-02_ ](https://git-scm.com/docs/git/2.53.0)
  2. [2.52.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-11-17_ ](https://git-scm.com/docs/git/2.52.0)
  3. 2.51.2 no changes
  4. [2.51.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-10-15_ ](https://git-scm.com/docs/git/2.51.1)
  5. 2.50.1 → 2.51.0 no changes
  6. [2.50.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-06-16_ ](https://git-scm.com/docs/git/2.50.0)
  7. 2.49.1 no changes
  8. [2.49.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-03-14_ ](https://git-scm.com/docs/git/2.49.0)
  9. 2.48.1 → 2.48.2 no changes
  10. [2.48.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2025-01-10_ ](https://git-scm.com/docs/git/2.48.0)
  11. 2.47.1 → 2.47.3 no changes
  12. [2.47.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-10-06_ ](https://git-scm.com/docs/git/2.47.0)
  13. 2.46.1 → 2.46.4 no changes
  14. [2.46.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-07-29_ ](https://git-scm.com/docs/git/2.46.0)
  15. 2.45.2 → 2.45.4 no changes
  16. [2.45.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git/2.45.1)
  17. [2.45.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-29_ ](https://git-scm.com/docs/git/2.45.0)
  18. 2.44.2 → 2.44.4 no changes
  19. [2.44.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.44.1)
  20. [2.44.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-23_ ](https://git-scm.com/docs/git/2.44.0)
  21. 2.43.5 → 2.43.7 no changes
  22. [2.43.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.43.4)
  23. 2.43.2 → 2.43.3 no changes
  24. [2.43.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-02-09_ ](https://git-scm.com/docs/git/2.43.1)
  25. [2.43.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-20_ ](https://git-scm.com/docs/git/2.43.0)
  26. 2.42.3 → 2.42.4 no changes
  27. [2.42.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.42.2)
  28. [2.42.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-11-02_ ](https://git-scm.com/docs/git/2.42.1)
  29. [2.42.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-08-21_ ](https://git-scm.com/docs/git/2.42.0)
  30. 2.41.2 → 2.41.3 no changes
  31. [2.41.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.41.1)
  32. [2.41.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2023-06-01_ ](https://git-scm.com/docs/git/2.41.0)
  33. 2.40.3 → 2.40.4 no changes
  34. [2.40.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.40.2)
  35. 2.40.1 no changes
  36. 2.40.0 no changes
  37. 2.39.5 no changes
  38. [2.39.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2024-04-19_ ](https://git-scm.com/docs/git/2.39.4)
  39. 2.39.1 → 2.39.3 no changes
  40. [2.39.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-12_ ](https://git-scm.com/docs/git/2.39.0)
  41. 2.38.3 → 2.38.5 no changes
  42. [2.38.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-12-11_ ](https://git-scm.com/docs/git/2.38.2)
  43. 2.38.1 no changes
  44. [2.38.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-10-02_ ](https://git-scm.com/docs/git/2.38.0)
  45. 2.37.3 → 2.37.7 no changes
  46. [2.37.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-08-11_ ](https://git-scm.com/docs/git/2.37.2)
  47. 2.37.1 no changes
  48. [2.37.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-06-27_ ](https://git-scm.com/docs/git/2.37.0)
  49. 2.36.1 → 2.36.6 no changes
  50. [2.36.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-04-18_ ](https://git-scm.com/docs/git/2.36.0)
  51. 2.35.1 → 2.35.8 no changes
  52. [2.35.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-01-24_ ](https://git-scm.com/docs/git/2.35.0)
  53. 2.34.1 → 2.34.8 no changes
  54. [2.34.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-11-15_ ](https://git-scm.com/docs/git/2.34.0)
  55. 2.33.3 → 2.33.8 no changes
  56. [2.33.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2022-03-23_ ](https://git-scm.com/docs/git/2.33.2)
  57. [2.33.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-10-12_ ](https://git-scm.com/docs/git/2.33.1)
  58. 2.32.1 → 2.33.0 no changes
  59. [2.32.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-06-06_ ](https://git-scm.com/docs/git/2.32.0)
  60. 2.31.1 → 2.31.8 no changes
  61. [2.31.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2021-03-15_ ](https://git-scm.com/docs/git/2.31.0)
  62. 2.30.1 → 2.30.9 no changes
  63. [2.30.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-12-27_ ](https://git-scm.com/docs/git/2.30.0)
  64. 2.29.1 → 2.29.3 no changes
  65. [2.29.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-10-19_ ](https://git-scm.com/docs/git/2.29.0)
  66. 2.28.1 no changes
  67. [2.28.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-07-27_ ](https://git-scm.com/docs/git/2.28.0)
  68. 2.27.1 no changes
  69. [2.27.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-06-01_ ](https://git-scm.com/docs/git/2.27.0)
  70. 2.26.1 → 2.26.3 no changes
  71. [2.26.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-03-22_ ](https://git-scm.com/docs/git/2.26.0)
  72. 2.25.2 → 2.25.5 no changes
  73. [2.25.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-02-17_ ](https://git-scm.com/docs/git/2.25.1)
  74. [2.25.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2020-01-13_ ](https://git-scm.com/docs/git/2.25.0)
  75. 2.23.1 → 2.24.4 no changes
  76. [2.23.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-16_ ](https://git-scm.com/docs/git/2.23.0)
  77. 2.22.2 → 2.22.5 no changes
  78. [2.22.1 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-08-11_ ](https://git-scm.com/docs/git/2.22.1)
  79. [2.22.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-06-07_ ](https://git-scm.com/docs/git/2.22.0)
  80. 2.20.1 → 2.21.4 no changes
  81. [2.20.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-12-09_ ](https://git-scm.com/docs/git/2.20.0)
  82. 2.19.3 → 2.19.6 no changes
  83. [2.19.2 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-11-21_ ](https://git-scm.com/docs/git/2.19.2)
  84. 2.19.1 no changes
  85. [2.19.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-09-10_ ](https://git-scm.com/docs/git/2.19.0)
  86. 2.18.1 → 2.18.5 no changes
  87. [2.18.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-06-21_ ](https://git-scm.com/docs/git/2.18.0)
  88. 2.17.1 → 2.17.6 no changes
  89. [2.17.0 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2018-04-02_ ](https://git-scm.com/docs/git/2.17.0)
  90. [2.16.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git/2.16.6)
  91. [2.15.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git/2.15.4)
  92. [2.14.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2019-12-06_ ](https://git-scm.com/docs/git/2.14.6)
  93. 2.13.7 no changes
  94. [2.12.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git/2.12.5)
  95. [2.11.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git/2.11.4)
  96. [2.10.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-09-22_ ](https://git-scm.com/docs/git/2.10.5)
  97. [2.9.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git/2.9.5)
  98. [2.8.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git/2.8.6)
  99. [2.7.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-07-30_ ](https://git-scm.com/docs/git/2.7.6)
  100. [2.6.7 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git/2.6.7)
  101. [2.5.6 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git/2.5.6)
  102. [2.4.12 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2017-05-05_ ](https://git-scm.com/docs/git/2.4.12)
  103. [2.3.10 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-28_ ](https://git-scm.com/docs/git/2.3.10)
  104. [2.2.3 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2015-09-04_ ](https://git-scm.com/docs/git/2.2.3)
  105. [2.1.4 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git/2.1.4)
  106. [2.0.5 ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/green-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/red-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) ![](https://git-scm.com/images/icons/grey-dot.png) _2014-12-17_ ](https://git-scm.com/docs/git/2.0.5)


Check your version of git by running
`git --version`
##  [](https://git-scm.com/docs/git/uk#_%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0)НАЗВА
git - дурний трекер контенту
##  [](https://git-scm.com/docs/git/uk#_%D1%81%D0%B8%D0%BD%D0%BE%D0%BF%D1%81%D0%B8%D1%81)СИНОПСИС
```
_git_ [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
    [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
    [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
    [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
    [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
    <command> [<args>]
```

##  [](https://git-scm.com/docs/git/uk#_%D0%BE%D0%BF%D0%B8%D1%81)ОПИС
Git — це швидка, масштабована, розподілена система контролю версій з надзвичайно багатим набором команд, яка забезпечує як високорівневі операції, так і повний доступ до внутрішніх компонентів.
Дивіться [gittutorial[7]](https://git-scm.com/docs/gittutorial/uk) для початку, а потім перегляньте [giteveryday[7]](https://git-scm.com/docs/giteveryday/uk) для корисного мінімального набору команд. [Посібник користувача Git](https://git-scm.com/docs/user-manual/uk) містить більш детальний вступ.
Після того, як ви опануєте основні концепції, ви можете повернутися на цю сторінку, щоб дізнатися, які команди пропонує Git. Ви можете дізнатися більше про окремі команди Git за допомогою команди "git help". Сторінка довідки [gitcli[7]](https://git-scm.com/docs/gitcli/uk) містить огляд синтаксису команд командного рядка.
Відформатовану копію останньої документації Git з гіперпосиланнями можна переглянути за адресою <https://git.github.io/htmldocs/git.html> або <https://git-scm.com/docs>.
##  [](https://git-scm.com/docs/git/uk#_%D0%BE%D0%BF%D1%86%D1%96%D1%97)ОПЦІЇ 

[](https://git-scm.com/docs/git/uk#git--v)-v 


[](https://git-scm.com/docs/git/uk#git---version)--version 
    
Виводить версію пакету Git, з якого походить програма «git».
Цей параметр внутрішньо перетворюється на `git` `version` ... та приймає ті ж параметри, що й команда [git-version[1]](https://git-scm.com/docs/git-version/uk). Якщо також вказано `--help`, він має пріоритет над `--version`. 

[](https://git-scm.com/docs/git/uk#git--h)-h 


[](https://git-scm.com/docs/git/uk#git---help)--help 
    
Друкує короткий опис та список найчастіше використовуваних команд. Якщо вказано опцію `--all` або `-a`, то друкуються всі доступні команди. Якщо названо команду Git, ця опція відкриє сторінку довідки для цієї команди.
Доступні інші опції для керування відображенням сторінки довідки. Див. [git-help[1]](https://git-scm.com/docs/git-help/uk) для отримання додаткової інформації, оскільки `git` `--help` ... внутрішньо перетворюється на `git` `help` .... 

[](https://git-scm.com/docs/git/uk#git--Cpath) [](https://git-scm.com/docs/git/uk#git--Cltpathgt)-C <path> 
    
Запускати так, ніби git було запущено в _< шлях>_, а не в поточному робочому каталозі. Коли задано кілька опцій `-C`, кожна наступна неабсолютна `-C` _< шлях>_ інтерпретується відносно попередньої `-C` _< шлях>_. Якщо _< шлях>_ присутній, але порожній, наприклад, `-C` `""`, то поточний робочий каталог залишається незмінним.
Цей параметр впливає на параметри, які очікують шлях до каталогу, такі як `--git-dir` та `--work-tree`, оскільки їхні інтерпретації шляхів будуть здійснюватися відносно робочого каталогу, спричиненого параметром `-C`. Наприклад, наступні виклики еквівалентні:
```
git --git-dir=a.git --work-tree=b -C c status
git --git-dir=c/a.git --work-tree=c/b status
```


[](https://git-scm.com/docs/git/uk#git--cnamevalue) [](https://git-scm.com/docs/git/uk#git--cltnamegtltvaluegt)-c <name>=<value> 
    
Передайте команді параметр конфігурації. Надане значення замінить значення з файлів конфігурації. Очікується, що <name> буде у тому ж форматі, що й у _git config_ (підрозділи, розділені крапками).
Зверніть увагу, що пропуск символу `=` у `git` `-c` `foo.bar` ... дозволено, і це встановлює `foo.bar` у логічне значення true (як і [`foo`]`bar` у конфігураційному файлі). Включення символу equals, але з порожнім значенням (наприклад, `git` `-c` `foo.bar=` ...), встановлює `foo.bar` у порожній рядок, який `git` `config` `--type=bool` перетворить на `false`. 

[](https://git-scm.com/docs/git/uk#git---config-envnameenvvar) [](https://git-scm.com/docs/git/uk#git---config-envltnamegtltenvvargt)--config-env=<name>=<envvar> 
    
Як і `-c` _< назва>_`=`_< значення>_, надайте змінній конфігурації _< назва>_ значення, де <змінна середовища> — це назва змінної середовища, з якої потрібно отримати значення. На відміну від `-c`, немає скорочення для безпосереднього встановлення значення в порожній рядок, натомість сама змінна середовища має бути встановлена в порожній рядок. Якщо _< змінна середовища>_ не існує в середовищі, це помилка. _< змінна середовища>_ може не містити знак рівності, щоб уникнути двозначності зі _< назва>_, що містить його.
Це корисно у випадках, коли ви хочете передати тимчасові параметри конфігурації до git, але робите це в операційних системах, де інші процеси можуть читати ваш командний рядок (наприклад, `/proc/self/cmdline`), але не ваше середовище (наприклад, `/proc/self/environ`). Така поведінка є типовою в Linux, але може не бути такою у вашій системі.
Зверніть увагу, що це може додати безпеку для таких змінних, як `http.extraHeader`, де конфіденційна інформація є частиною значення, але не, наприклад, `url.`_< base>_`.insteadOf`, де конфіденційна інформація може бути частиною ключа. 

[](https://git-scm.com/docs/git/uk#git---exec-pathpath) [](https://git-scm.com/docs/git/uk#git---exec-pathltpathgt)--exec-path[=<path>] 
    
Шлях до місця встановлення ваших основних програм Git. Цим також можна керувати, встановивши змінну середовища GIT_EXEC_PATH. Якщо шлях не вказано, «git» виведе поточні налаштування та завершить роботу. 

[](https://git-scm.com/docs/git/uk#git---html-path)--html-path 
    
Виведіть шлях, без косої риски в кінці, де встановлено HTML-документацію Git, та завершіть роботу. 

[](https://git-scm.com/docs/git/uk#git---man-path)--man-path 
    
Виведіть шлях до сторінок довідки (див. `man`(`1`)) для цієї версії Git та вийдіть. 

[](https://git-scm.com/docs/git/uk#git---info-path)--info-path 
    
Виведіть шлях до інстальованих інформаційних файлів, що документують цю версію Git, та завершіть роботу. 

[](https://git-scm.com/docs/git/uk#git--p)-p 


[](https://git-scm.com/docs/git/uk#git---paginate)--paginate 
    
Передати весь вивід до _less_ (або, якщо встановлено, $PAGER), якщо стандартний вивід є терміналом. Це замінює параметри конфігурації `pager.`_< cmd>_ (див. розділ "Механізм конфігурації" нижче). 

[](https://git-scm.com/docs/git/uk#git--P)-P 


[](https://git-scm.com/docs/git/uk#git---no-pager)--no-pager 
    
Не перенаправляйте вивід Git у пейджер. 

[](https://git-scm.com/docs/git/uk#git---git-dirpath) [](https://git-scm.com/docs/git/uk#git---git-dirltpathgt)--git-dir=<path> 
    
Встановіть шлях до репозиторію (каталог ".git"). Це також можна контролювати, встановивши змінну середовища `GIT_DIR`. Це може бути абсолютний або відносний шлях до поточного робочого каталогу.
Вказівка розташування каталогу ".git" за допомогою цього параметра (або змінної середовища `GIT_DIR`) вимикає пошук репозиторію, який намагається знайти каталог з підкаталогом ".git" (саме так виявляється репозиторій та верхній рівень робочого дерева), та повідомляє Git, що ви знаходитесь на верхньому рівні робочого дерева. Якщо ви не знаходитесь у верхньому каталозі робочого дерева, вам слід повідомити Git, де знаходиться верхній рівень робочого дерева, за допомогою параметра `--work-tree=`_< шлях>_ (або змінної середовища `GIT_WORK_TREE`)
Якщо ви просто хочете запустити git так, ніби він був запущений у _< шлях>_, тоді використовуйте `git` `-C` _< шлях>_. 

[](https://git-scm.com/docs/git/uk#git---work-treepath) [](https://git-scm.com/docs/git/uk#git---work-treeltpathgt)--work-tree=<path> 
    
Встановіть шлях до робочого дерева. Це може бути абсолютний шлях або шлях відносно поточного робочого каталогу. Це також можна контролювати, встановивши змінну середовища GIT_WORK_TREE та змінну конфігурації core.worktree (див. core.worktree у [git-config[1]](https://git-scm.com/docs/git-config/uk) для більш детального обговорення). 

[](https://git-scm.com/docs/git/uk#git---namespacepath) [](https://git-scm.com/docs/git/uk#git---namespaceltpathgt)--namespace=<path> 
    
Встановіть простір імен Git. Див. [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces/uk) для отримання додаткової інформації. Еквівалентно встановленню змінної середовища `GIT_NAMESPACE`. 

[](https://git-scm.com/docs/git/uk#git---bare)--bare 
    
Розглядати репозиторій як чистий репозиторій. Якщо середовище GIT_DIR не встановлено, воно встановлюється на поточний робочий каталог. 

[](https://git-scm.com/docs/git/uk#git---no-replace-objects)--no-replace-objects 
    
Не використовуйте замінюючі посилання для заміни об’єктів Git. Це еквівалентно експорту змінної середовища `GIT_NO_REPLACE_OBJECTS` з будь-яким значенням. Див. [git-replace[1]](https://git-scm.com/docs/git-replace/uk) для отримання додаткової інформації. 

[](https://git-scm.com/docs/git/uk#git---no-lazy-fetch)--no-lazy-fetch 
    
Не вибирати відсутні об’єкти з віддаленого сервера-промісника на вимогу. Корисно разом з `git` `cat-file` `-e` _< object>_, щоб перевірити, чи об’єкт доступний локально. Це еквівалентно встановленню змінної середовища `GIT_NO_LAZY_FETCH` на `1`. 

[](https://git-scm.com/docs/git/uk#git---no-optional-locks)--no-optional-locks 
    
Не виконуйте додаткові операції, що потребують блокування. Це еквівалентно встановленню `GIT_OPTIONAL_LOCKS` на `0`. 

[](https://git-scm.com/docs/git/uk#git---no-advice)--no-advice 
    
Вимкнути друк усіх підказок. 

[](https://git-scm.com/docs/git/uk#git---literal-pathspecs)--literal-pathspecs 
    
Ставтеся до pathspecs буквально (тобто без глобалізації, без магії pathspecs). Це еквівалентно встановленню змінної середовища `GIT_LITERAL_PATHSPECS` на `1`. 

[](https://git-scm.com/docs/git/uk#git---glob-pathspecs)--glob-pathspecs 
    
Додайте магію "glob" до всіх специфікацій шляхів. Це еквівалентно встановленню змінної середовища `GIT_GLOB_PATHSPECS` на `1`. Вимкнення глобалізації для окремих специфікацій шляхів можна виконати за допомогою магії специфікацій шляхів ":(літерал)" 

[](https://git-scm.com/docs/git/uk#git---noglob-pathspecs)--noglob-pathspecs 
    
Додайте "літеральну" магію до всіх специфікацій шляхів. Це еквівалентно встановленню змінної середовища `GIT_NOGLOB_PATHSPECS` на `1`. Увімкнення глобалізації для окремих специфікацій шляхів можна зробити за допомогою магії специфікацій шляхів ":(glob)" 

[](https://git-scm.com/docs/git/uk#git---icase-pathspecs)--icase-pathspecs 
    
Додайте магію "icase" до всіх pathspec. Це еквівалентно встановленню змінної середовища `GIT_ICASE_PATHSPECS` на `1`. 

[](https://git-scm.com/docs/git/uk#git---list-cmdsgroupgroup) [](https://git-scm.com/docs/git/uk#git---list-cmdsltgroupgtltgroupgt82308203)--list-cmds=<group>[,<group>…​] 
    
Список команд за групами. Це внутрішній/експериментальний параметр, який може бути змінений або видалений у майбутньому. Підтримувані групи: builtins, parseopt (вбудовані команди, що використовують parse-options), deprecated (застарілі вбудовані команди), main (всі команди в каталозі libexec), others (всі інші команди в `$PATH`, що мають префікс git-), list-<category> (див. категорії в command-list.txt), nohelpers (виключити допоміжні команди), alias та config (отримати список команд зі змінної конфігурації completion.commands) 

[](https://git-scm.com/docs/git/uk#git---attr-sourcetree-ish) [](https://git-scm.com/docs/git/uk#git---attr-sourcelttree-ishgt)--attr-source=<tree-ish> 
    
Зчитувати gitattributes з <tree-ish> замість робочого дерева. Див. [gitattributes[5]](https://git-scm.com/docs/gitattributes/uk). Це еквівалентно встановленню змінної середовища `GIT_ATTR_SOURCE`.
##  [](https://git-scm.com/docs/git/uk#_git_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8)GIT-КОМАНДИ
Ми поділяємо Git на команди високого рівня ("порцелянові") та команди низького рівня ("сантехніка").
##  [](https://git-scm.com/docs/git/uk#_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8_%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D0%B3%D0%BE_%D1%80%D1%96%D0%B2%D0%BD%D1%8F_%D0%BF%D0%BE%D1%80%D1%86%D0%B5%D0%BB%D1%8F%D0%BD%D0%B0)Команди високого рівня (порцеляна)
Ми розділяємо команди porcelain на основні команди та деякі допоміжні утиліти користувача.
###  [](https://git-scm.com/docs/git/uk#_%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%96_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8_%D0%B4%D0%BB%D1%8F_%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%B8_%D0%B7_%D0%BF%D0%BE%D1%80%D1%86%D0%B5%D0%BB%D1%8F%D0%BD%D0%BE%D1%8E)Основні команди для роботи з порцеляною
Warning |  Missing `uk/{build_dir}/cmds-mainporcelain.adoc` See original version for this content.  
---|---  
###  [](https://git-scm.com/docs/git/uk#_%D0%B4%D0%BE%D0%BF%D0%BE%D0%BC%D1%96%D0%B6%D0%BD%D1%96_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8)Допоміжні команди
Маніпулятори:
Warning |  Missing `uk/{build_dir}/cmds-ancillarymanipulators.adoc` See original version for this content.  
---|---  
Слідчі:
Warning |  Missing `uk/{build_dir}/cmds-ancillaryinterrogators.adoc` See original version for this content.  
---|---  
###  [](https://git-scm.com/docs/git/uk#_%D0%B2%D0%B7%D0%B0%D1%94%D0%BC%D0%BE%D0%B4%D1%96%D1%8F_%D0%B7_%D1%96%D0%BD%D1%88%D0%B8%D0%BC%D0%B8)Взаємодія з іншими
Ці команди призначені для взаємодії із зовнішнім SCM та з іншими людьми через патч через електронну пошту.
Warning |  Missing `uk/{build_dir}/cmds-foreignscminterface.adoc` See original version for this content.  
---|---  
###  [](https://git-scm.com/docs/git/uk#_%D1%81%D0%BA%D0%B8%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F_%D0%B2%D1%96%D0%B4%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D1%82%D0%B0_%D0%BF%D0%BE%D0%B2%D0%B5%D1%80%D0%BD%D0%B5%D0%BD%D0%BD%D1%8F)Скидання, відновлення та повернення
Існує три команди зі схожими назвами: `git` `reset`, `git` `restore` та `git` `revert`.
  * [git-revert[1]](https://git-scm.com/docs/git-revert/uk) йдеться про створення нового коміту, який скасовує зміни, внесені іншими комітами.
  * [git-restore[1]](https://git-scm.com/docs/git-restore/uk) йдеться про відновлення файлів у робочому дереві з індексу або іншого коміту. Ця команда не оновлює вашу гілку. Команду також можна використовувати для відновлення файлів в індексі з іншого коміту.
  * [git-reset[1]](https://git-scm.com/docs/git-reset/uk) йдеться про оновлення вашої гілки, переміщення підказки для додавання або видалення комітів з гілки. Ця операція змінює історію комітів.
Команда `git` `reset` також може бути використана для відновлення індексу, що перетинається з командою `git` `restore`.


##  [](https://git-scm.com/docs/git/uk#_%D0%BD%D0%B8%D0%B7%D1%8C%D0%BA%D0%BE%D1%80%D1%96%D0%B2%D0%BD%D0%B5%D0%B2%D1%96_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8_%D1%81%D0%B0%D0%BD%D1%82%D0%B5%D1%85%D0%BD%D1%96%D0%BA%D0%B0)Низькорівневі команди (сантехніка)
Хоча Git містить власний шар порцеляни, його низькорівневих команд достатньо для підтримки розробки альтернативних порцелянових шарів. Розробники таких порцелянових шарів можуть почати з ознайомлення з [git-update-index[1]](https://git-scm.com/docs/git-update-index/uk) та [git-read-tree[1]](https://git-scm.com/docs/git-read-tree/uk).
Інтерфейс (введення, виведення, набір опцій та семантика) цих низькорівневих команд має бути набагато стабільнішим, ніж команди рівня Porcelain, оскільки ці команди призначені переважно для використання за допомогою скриптів. Інтерфейс команд Porcelain, з іншого боку, може бути змінений для покращення взаємодії з кінцевим користувачем.
У наступному описі низькорівневі команди поділяються на команди, що маніпулюють об’єктами (у репозиторії, індексі та робочому дереві), команди, що опитують та порівнюють об’єкти, та команди, що переміщують об’єкти та посилання між репозиторіями.
###  [](https://git-scm.com/docs/git/uk#_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8_%D0%BC%D0%B0%D0%BD%D1%96%D0%BF%D1%83%D0%BB%D1%8F%D1%86%D1%96%D0%B9)Команди маніпуляцій
Warning |  Missing `uk/{build_dir}/cmds-plumbingmanipulators.adoc` See original version for this content.  
---|---  
###  [](https://git-scm.com/docs/git/uk#_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8_%D0%B4%D0%BE%D0%BF%D0%B8%D1%82%D1%83)Команди допиту
Warning |  Missing `uk/{build_dir}/cmds-plumbinginterrogators.adoc` See original version for this content.  
---|---  
Загалом, команди запиту не стосуються файлів у робочому дереві.
###  [](https://git-scm.com/docs/git/uk#_%D1%81%D0%B8%D0%BD%D1%85%D1%80%D0%BE%D0%BD%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F_%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D1%96%D1%97%D0%B2)Синхронізація репозиторіїв
Warning |  Missing `uk/{build_dir}/cmds-synchingrepositories.adoc` See original version for this content.  
---|---  
Нижче наведено допоміжні команди, що використовуються вищезазначеними; кінцеві користувачі зазвичай не використовують їх безпосередньо.
Warning |  Missing `uk/{build_dir}/cmds-synchelpers.adoc` See original version for this content.  
---|---  
###  [](https://git-scm.com/docs/git/uk#_%D0%B2%D0%BD%D1%83%D1%82%D1%80%D1%96%D1%88%D0%BD%D1%96_%D0%B4%D0%BE%D0%BF%D0%BE%D0%BC%D1%96%D0%B6%D0%BD%D1%96_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8)Внутрішні допоміжні команди
Це внутрішні допоміжні команди, що використовуються іншими командами; кінцеві користувачі зазвичай не використовують їх безпосередньо.
Warning |  Missing `uk/{build_dir}/cmds-purehelpers.adoc` See original version for this content.  
---|---  
##  [](https://git-scm.com/docs/git/uk#_%D0%BF%D1%83%D1%82%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B8)Путівники
Наведені нижче сторінки документації є посібниками з концепцій Git.
Warning |  Missing `uk/{build_dir}/cmds-guide.adoc` See original version for this content.  
---|---  
##  [](https://git-scm.com/docs/git/uk#_%D1%96%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B8_%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D1%96%D1%8E_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4_%D1%82%D0%B0_%D1%84%D0%B0%D0%B9%D0%BB%D1%96%D0%B2)Інтерфейси репозиторію, команд та файлів
У цій документації обговорюються інтерфейси репозиторію та команд, з якими користувачі повинні безпосередньо взаємодіяти. Див. `--user-formats` у [git-help[1]](https://git-scm.com/docs/git-help/uk) для отримання додаткової інформації про критерії.
Warning |  Missing `uk/{build_dir}/cmds-userinterfaces.adoc` See original version for this content.  
---|---  
##  [](https://git-scm.com/docs/git/uk#_%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8_%D1%84%D0%B0%D0%B9%D0%BB%D1%96%D0%B2_%D0%BF%D1%80%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%BB%D0%B8_%D1%82%D0%B0_%D1%96%D0%BD%D1%88%D1%96_%D1%96%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B8_%D1%80%D0%BE%D0%B7%D1%80%D0%BE%D0%B1%D0%BD%D0%B8%D0%BA%D0%B0)Формати файлів, протоколи та інші інтерфейси розробника
У цій документації обговорюються формати файлів, протоколи OTP та інші інтерфейси розробника git. Див. `--developer-interfaces` у [git-help[1]](https://git-scm.com/docs/git-help/uk).
Warning |  Missing `uk/{build_dir}/cmds-developerinterfaces.adoc` See original version for this content.  
---|---  
##  [](https://git-scm.com/docs/git/uk#_%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D1%96%D0%B7%D0%BC_%D0%BA%D0%BE%D0%BD%D1%84%D1%96%D0%B3%D1%83%D1%80%D0%B0%D1%86%D1%96%D1%97)Механізм конфігурації
Git використовує простий текстовий формат для зберігання налаштувань, які надаються для кожного репозиторію та кожного користувача. Такий файл конфігурації може виглядати так:
```
#
# A '#' or ';' character indicates a comment.
#

; основні змінні
[core]
	; Не довіряйте режимам файлів
	filemode = false

; user identity
[user]
	name = "Junio C Hamano"
	email = "gitster@pobox.com"
```

Різні команди зчитують дані з конфігураційного файлу та відповідно налаштовують свою роботу. Список та докладнішу інформацію про механізм конфігурації див. у [git-config[1]](https://git-scm.com/docs/git-config/uk).
##  [](https://git-scm.com/docs/git/uk#_%D1%82%D0%B5%D1%80%D0%BC%D1%96%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%8F_%D1%96%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D1%96%D0%BA%D0%B0%D1%82%D0%BE%D1%80%D1%96%D0%B2)Термінологія ідентифікаторів 

[](https://git-scm.com/docs/git/uk#git-object) [](https://git-scm.com/docs/git/uk#git-ltobjectgt)<object> 
    
Вказує назву об’єкта для будь-якого типу об’єкта. 

[](https://git-scm.com/docs/git/uk#git-blob) [](https://git-scm.com/docs/git/uk#git-ltblobgt)<blob> 
    
Вказує ім’я об’єкта blob. 

[](https://git-scm.com/docs/git/uk#git-tree) [](https://git-scm.com/docs/git/uk#git-lttreegt)<tree> 
    
Вказує назву об’єкта дерева. 

[](https://git-scm.com/docs/git/uk#git-commit) [](https://git-scm.com/docs/git/uk#git-ltcommitgt)<commit> 
    
Вказує назву об’єкта коміту. 

[](https://git-scm.com/docs/git/uk#git-tree-ish) [](https://git-scm.com/docs/git/uk#git-lttree-ishgt)<tree-ish> 
    
Вказує назву об’єкта дерева, коміту або тегу. Команда, яка приймає аргумент типу <tree-ish>, зрештою хоче працювати з об’єктом <tree>, але автоматично розіменовує об’єкти <commit> та <tag>, що вказують на <tree>. 

[](https://git-scm.com/docs/git/uk#git-commit-ish) [](https://git-scm.com/docs/git/uk#git-ltcommit-ishgt)<commit-ish> 
    
Вказує назву об’єкта комміту або тегу. Команда, яка приймає аргумент типу <commit-ish>, зрештою хоче працювати з об’єктом <commit>, але автоматично розіменовує об’єкти <tag>, що вказують на <commit>. 

[](https://git-scm.com/docs/git/uk#git-type) [](https://git-scm.com/docs/git/uk#git-lttypegt)<type> 
    
Вказує на необхідність вказати тип об’єкта. Наразі це один із таких типів: `blob`, `tree`, `commit` або `tag`. 

[](https://git-scm.com/docs/git/uk#git-file) [](https://git-scm.com/docs/git/uk#git-ltfilegt)<file> 
    
Вказує ім’я файлу — майже завжди відносно кореня деревоподібної структури, яку описує `GIT_INDEX_FILE`.
##  [](https://git-scm.com/docs/git/uk#_%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%96%D1%87%D0%BD%D1%96_%D1%96%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D1%96%D0%BA%D0%B0%D1%82%D0%BE%D1%80%D0%B8)Символічні ідентифікатори
Будь-яка команда Git, яка приймає будь-який <object>, також може використовувати наступну символічну нотацію: 

[](https://git-scm.com/docs/git/uk#git-HEAD)HEAD 
    
вказує на керівника поточного відділення. 

[](https://git-scm.com/docs/git/uk#git-tag) [](https://git-scm.com/docs/git/uk#git-lttaggt)<tag> 
    
коректний тег _name_ (тобто посилання `refs/tags/`_< tag>_). 

[](https://git-scm.com/docs/git/uk#git-head) [](https://git-scm.com/docs/git/uk#git-ltheadgt)<head> 
    
коректне ім’я заголовка (тобто посилання `refs/heads/`_< заголовок>_).
Для отримання повнішого списку способів написання назв об’єктів див. розділ «ВИЗНАЧЕННЯ РЕВІЗІЙ» у [gitrevisions[7]](https://git-scm.com/docs/gitrevisions/uk).
##  [](https://git-scm.com/docs/git/uk#_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0_%D1%84%D0%B0%D0%B9%D0%BB%D1%96%D0%B2%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%D1%96%D0%B2)Структура файлів/каталогів
Будь ласка, перегляньте документ [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout/uk).
Більш детальну інформацію про кожен хук дивіться у [githooks[5]](https://git-scm.com/docs/githooks/uk).
SCM вищого рівня можуть надавати та керувати додатковою інформацією в `$GIT_DIR`.
##  [](https://git-scm.com/docs/git/uk#_%D1%82%D0%B5%D1%80%D0%BC%D1%96%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D1%8F)Термінологія
Будь ласка, дивіться [gitglossary[7]](https://git-scm.com/docs/gitglossary/uk).
##  [](https://git-scm.com/docs/git/uk#_%D0%B7%D0%BC%D1%96%D0%BD%D0%BD%D1%96_%D1%81%D0%B5%D1%80%D0%B5%D0%B4%D0%BE%D0%B2%D0%B8%D1%89%D0%B0)Змінні середовища
Різні команди Git звертають увагу на змінні середовища та змінюють їхню поведінку. Змінні середовища, позначені як "Boolean", приймають свої значення так само, як і змінні конфігурації з логічними значеннями, тобто "true", "yes", "on" та додатні числа приймаються як "yes", тоді як "false", "no", "off" та "0" приймаються як "no".
Ось змінні:
###  [](https://git-scm.com/docs/git/uk#_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0)Система 

[](https://git-scm.com/docs/git/uk#git-HOME) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeHOMEcodespan)`HOME` 
    
Вказує шлях до домашнього каталогу користувача. У Windows, якщо не встановлено, Git встановить змінну середовища процесу, що дорівнює: `$HOMEDRIVE$HOMEPATH`, якщо існують обидві змінні, `$HOMEDRIVE` та `$HOMEPATH`; інакше `$USERPROFILE`, якщо `$USERPROFILE` існує.
###  [](https://git-scm.com/docs/git/uk#_%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D1%96%D0%B9_git)Репозиторій Git
Ці змінні середовища застосовуються до «всіх» основних команд Git. Примітка: варто зазначити, що вони можуть бути використані/перевизначені SCMS, що працює над Git, тому будьте обережні, якщо використовуєте сторонній фронтенд. 

[](https://git-scm.com/docs/git/uk#git-GITINDEXFILE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITINDEXFILEcodespan)`GIT_INDEX_FILE` 
    
Ця змінна середовища вказує на альтернативний файл індексу. Якщо не вказано, використовується значення за замовчуванням `$GIT_DIR/index`. 

[](https://git-scm.com/docs/git/uk#git-GITINDEXVERSION) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITINDEXVERSIONcodespan)`GIT_INDEX_VERSION` 
    
Ця змінна середовища вказує, яка версія індексу використовується під час запису індексного файлу. Вона не вплине на існуючі індексні файли. За замовчуванням використовується версія індексного файлу 2 або 3. Див. [git-update-index[1]](https://git-scm.com/docs/git-update-index/uk) для отримання додаткової інформації. 

[](https://git-scm.com/docs/git/uk#git-GITOBJECTDIRECTORY) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITOBJECTDIRECTORYcodespan)`GIT_OBJECT_DIRECTORY` 
    
Якщо каталог для зберігання об’єктів вказано через цю змінну середовища, то каталоги sha1 створюються під ним, інакше використовується каталог за замовчуванням `$GIT_DIR/objects`. 

[](https://git-scm.com/docs/git/uk#git-GITALTERNATEOBJECTDIRECTORIES) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITALTERNATEOBJECTDIRECTORIEScodespan)`GIT_ALTERNATE_OBJECT_DIRECTORIES` 
    
Через незмінну природу об’єктів Git, старі об’єкти можна архівувати у спільні каталоги лише для читання. Ця змінна визначає список каталогів об’єктів Git, розділений символами ":" (у Windows - ";"), які можна використовувати для пошуку об’єктів Git. Нові об’єкти не будуть записані в ці каталоги.
Записи, що починаються з `"` (подвійних лапок), будуть інтерпретовані як шляхи в лапках у стилі C, без початкових та кінцевих подвійних лапок та з урахуванням екранування зворотної склесної риски. Наприклад, значення _"path-with-\"-and-:-in-it":vanilla-path_ має два шляхи: `path-with-"-and-:-in-it` та `vanilla-path`. 

[](https://git-scm.com/docs/git/uk#git-GITDIR) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITDIRcodespan)`GIT_DIR` 
    
Якщо встановлено змінну середовища `GIT_DIR`, вона вказує шлях, який використовуватиметься замість стандартного `.git` для бази репозиторію. Параметр командного рядка `--git-dir` також встановлює це значення. 

[](https://git-scm.com/docs/git/uk#git-GITWORKTREE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITWORKTREEcodespan)`GIT_WORK_TREE` 
    
Встановіть шлях до кореня робочого дерева. Це також можна контролювати за допомогою параметра командного рядка `--work-tree` та змінної конфігурації core.worktree. 

[](https://git-scm.com/docs/git/uk#git-GITNAMESPACE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITNAMESPACEcodespan)`GIT_NAMESPACE` 
    
Встановіть простір імен Git; див. деталі у [gitnamespaces[7]](https://git-scm.com/docs/gitnamespaces/uk). Параметр командного рядка `--namespace` також встановлює це значення. 

[](https://git-scm.com/docs/git/uk#git-GITCEILINGDIRECTORIES) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCEILINGDIRECTORIEScodespan)`GIT_CEILING_DIRECTORIES` 
    
Це має бути список абсолютних шляхів, розділених двокрапками. Якщо встановлено, це список каталогів, до яких Git не повинен переходити за допомогою chdir під час пошуку каталогу репозиторію (корисно для виключення мережевих каталогів, що повільно завантажуються). Він не виключатиме поточний робочий каталог або GIT_DIR, встановлений у командному рядку або в середовищі. Зазвичай Git має прочитати записи в цьому списку та вирішити будь-яке символічне посилання, яке може бути присутнім, щоб порівняти їх з поточним каталогом. Однак, якщо навіть цей доступ повільний, ви можете додати порожній запис до списку, щоб повідомити Git, що наступні записи не є символічними посиланнями і їх не потрібно розв’язувати; наприклад, `GIT_CEILING_DIRECTORIES=/maybe/symlink::/very/slow/non/symlink`. 

[](https://git-scm.com/docs/git/uk#git-GITDISCOVERYACROSSFILESYSTEM) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITDISCOVERYACROSSFILESYSTEMcodespan)`GIT_DISCOVERY_ACROSS_FILESYSTEM` 
    
Під час запуску в каталозі, який не має каталогу репозиторію ".git", Git намагається знайти такий каталог у батьківських каталогах, щоб знайти вершину робочого дерева, але за замовчуванням він не перетинає межі файлової системи. Цю булеву змінну середовища можна встановити в значення true, щоб вказати Git не зупинятися на межах файлової системи. Як і `GIT_CEILING_DIRECTORIES`, це не вплине на явний каталог репозиторію, встановлений через `GIT_DIR` або в командному рядку. 

[](https://git-scm.com/docs/git/uk#git-GITCOMMONDIR) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCOMMONDIRcodespan)`GIT_COMMON_DIR` 
    
Якщо для цієї змінної встановлено шлях, файли, що не належать до робочого дерева та зазвичай знаходяться в $GIT_DIR, будуть взяті з цього шляху. Файли, специфічні для робочого дерева, такі як HEAD або index, беруться з $GIT_DIR. Див. [gitrepository-layout[5]](https://git-scm.com/docs/gitrepository-layout/uk) та [git-worktree[1]](https://git-scm.com/docs/git-worktree/uk) для отримання детальної інформації. Ця змінна має нижчий пріоритет, ніж інші змінні шляху, такі як GIT_INDEX_FILE, GIT_OBJECT_DIRECTORY…​ 

[](https://git-scm.com/docs/git/uk#git-GITDEFAULTHASH) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITDEFAULTHASHcodespan)`GIT_DEFAULT_HASH` 
    
Якщо цю змінну встановлено, алгоритм хешування за замовчуванням для нових репозиторіїв буде встановлено на це значення. Це значення ігнорується під час клонування, і завжди використовуються налаштування віддаленого репозиторію. Значення за замовчуванням — "sha1". Див. `--object-format` у [git-init[1]](https://git-scm.com/docs/git-init/uk). 

[](https://git-scm.com/docs/git/uk#git-GITDEFAULTREFFORMAT) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITDEFAULTREFFORMATcodespan)`GIT_DEFAULT_REF_FORMAT` 
    
Якщо цю змінну встановлено, формат посилань на серверну частину за замовчуванням для нових репозиторіїв буде встановлено на це значення. Значення за замовчуванням — "файли". Див. `--ref-format` у [git-init[1]](https://git-scm.com/docs/git-init/uk).
###  [](https://git-scm.com/docs/git/uk#_%D0%BA%D0%BE%D0%BC%D1%96%D1%82%D0%B8_git)Коміти Git 

[](https://git-scm.com/docs/git/uk#git-GITAUTHORNAME) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITAUTHORNAMEcodespan)`GIT_AUTHOR_NAME` 
    
Зрозуміле для людини ім’я, яке використовується в ідентифікації автора під час створення об’єктів комітів або тегів, або під час написання рефлогів. Замінює налаштування конфігурації `user.name` та `author.name`. 

[](https://git-scm.com/docs/git/uk#git-GITAUTHOREMAIL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITAUTHOREMAILcodespan)`GIT_AUTHOR_EMAIL` 
    
Адреса електронної пошти, що використовується в ідентифікації автора під час створення об’єктів комітів або тегів, або під час написання рефлогів. Замінює налаштування конфігурації `user.email` та `author.email`. 

[](https://git-scm.com/docs/git/uk#git-GITAUTHORDATE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITAUTHORDATEcodespan)`GIT_AUTHOR_DATE` 
    
Дата, що використовується для ідентифікації автора під час створення об’єктів комітів або тегів, або під час написання рефлогів. Див. [git-commit[1]](https://git-scm.com/docs/git-commit/uk) для коректних форматів. 

[](https://git-scm.com/docs/git/uk#git-GITCOMMITTERNAME) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCOMMITTERNAMEcodespan)`GIT_COMMITTER_NAME` 
    
Зрозуміле для людини ім’я, яке використовується в ідентифікації комітера під час створення об’єктів комітів або тегів, або під час написання рефлогів. Замінює налаштування конфігурації `user.name` та `committer.name`. 

[](https://git-scm.com/docs/git/uk#git-GITCOMMITTEREMAIL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCOMMITTEREMAILcodespan)`GIT_COMMITTER_EMAIL` 
    
Адреса електронної пошти, що використовується в ідентифікації автора під час створення об’єктів комітів або тегів, або під час написання рефлогів. Замінює налаштування конфігурації `user.email` та `committer.email`. 

[](https://git-scm.com/docs/git/uk#git-GITCOMMITTERDATE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCOMMITTERDATEcodespan)`GIT_COMMITTER_DATE` 
    
Дата, що використовується для ідентифікації комітера під час створення об’єктів комітів або тегів, або під час написання рефлогів. Див. [git-commit[1]](https://git-scm.com/docs/git-commit/uk) для коректних форматів. 

[](https://git-scm.com/docs/git/uk#git-EMAIL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeEMAILcodespan)`EMAIL` 
    
Адреса електронної пошти, що використовується в ідентифікаторах автора та комітера, якщо не було встановлено жодної іншої відповідної змінної середовища або налаштування конфігурації.
###  [](https://git-scm.com/docs/git/uk#_%D1%80%D1%96%D0%B7%D0%BD%D0%B8%D1%86%D1%96_%D0%B2_git)Різниці в Git 

[](https://git-scm.com/docs/git/uk#git-GITDIFFOPTS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITDIFFOPTScodespan)`GIT_DIFF_OPTS` 
    
Єдиним допустимим параметром є "--unified=??" або "-u??", щоб встановити кількість рядків контексту, що відображаються під час створення уніфікованого різниці. Це має пріоритет над будь-яким значенням опції "-U" або "--unified", переданим у командному рядку Git diff. 

[](https://git-scm.com/docs/git/uk#git-GITEXTERNALDIFF) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITEXTERNALDIFFcodespan)`GIT_EXTERNAL_DIFF` 
    
Коли встановлено змінну середовища `GIT_EXTERNAL_DIFF`, програма, названа нею, викликається для генерації різниць, і Git не використовує вбудований механізм різниці. Для шляху, який додається, видаляється або змінюється, `GIT_EXTERNAL_DIFF` викликається з 7 параметрами:
```
шлях до старого файлу старий шістнадцятковий старий режим новий файл новий шістнадцятковий новий режим
```

де: 

[](https://git-scm.com/docs/git/uk#git-oldnew-file) [](https://git-scm.com/docs/git/uk#git-ltoldnewgt-file)<old|new>-file 
    
файли, які GIT_EXTERNAL_DIFF може використовувати для читання вмісту <old|new>, 

[](https://git-scm.com/docs/git/uk#git-oldnew-hex) [](https://git-scm.com/docs/git/uk#git-ltoldnewgt-hex)<old|new>-hex 
    
є 40-шістнадцятковими хешами SHA-1, 

[](https://git-scm.com/docs/git/uk#git-oldnew-mode) [](https://git-scm.com/docs/git/uk#git-ltoldnewgt-mode)<old|new>-mode 
    
є вісімковим представленням режимів файлу.
Параметри файлу можуть вказувати на робочий файл користувача (наприклад, `new-file` у "git-diff-files"), `/dev/null` (наприклад, `old-file`, коли додається новий файл) або тимчасовий файл (наприклад, `old-file` в індексі). `GIT_EXTERNAL_DIFF` не повинен турбуватися про від’єднання тимчасового файлу — він видаляється, коли `GIT_EXTERNAL_DIFF` завершує роботу.
Для шляху, що не об’єднаний, викликається `GIT_EXTERNAL_DIFF` з 1 параметром, <шлях>.
Для кожного викликаного шляху `GIT_EXTERNAL_DIFF` встановлюються дві змінні середовища: `GIT_DIFF_PATH_COUNTER` та `GIT_DIFF_PATH_TOTAL`. 

[](https://git-scm.com/docs/git/uk#git-GITEXTERNALDIFFTRUSTEXITCODE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITEXTERNALDIFFTRUSTEXITCODEcodespan)`GIT_EXTERNAL_DIFF_TRUST_EXIT_CODE` 
    
Якщо для цієї булевої змінної середовища встановлено значення true, то команда `GIT_EXTERNAL_DIFF` має повернути код виходу 0, якщо вона вважає вхідні файли рівними, або 1, якщо вона вважає їх різними, як-от `diff`(`1`). Якщо ж для неї встановлено значення false, що є значенням за замовчуванням, то команда має повернути код виходу 0 незалежно від рівності. Будь-який інший код виходу призведе до того, що Git повідомить про фатальну помилку. 

[](https://git-scm.com/docs/git/uk#git-GITDIFFPATHCOUNTER) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITDIFFPATHCOUNTERcodespan)`GIT_DIFF_PATH_COUNTER` 
    
Лічильник, що базується на 1, збільшується на одиницю для кожного шляху. 

[](https://git-scm.com/docs/git/uk#git-GITDIFFPATHTOTAL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITDIFFPATHTOTALcodespan)`GIT_DIFF_PATH_TOTAL` 
    
Загальна кількість шляхів.
###  [](https://git-scm.com/docs/git/uk#_%D1%96%D0%BD%D1%88%D0%B8%D0%B9)інший 

[](https://git-scm.com/docs/git/uk#git-GITMERGEVERBOSITY) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITMERGEVERBOSITYcodespan)`GIT_MERGE_VERBOSITY` 
    
Число, що контролює обсяг виводу, що відображається рекурсивною стратегією злиття. Перевизначає merge.verbosity. Див. [git-merge[1]](https://git-scm.com/docs/git-merge/uk) 

[](https://git-scm.com/docs/git/uk#git-GITPAGER) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITPAGERcodespan)`GIT_PAGER` 
    
Ця змінна середовища перевизначає `$PAGER`. Якщо їй встановлено значення порожнього рядка або значення "cat", Git не запустить пейджер. Дивіться також опцію `core.pager` у [git-config[1]](https://git-scm.com/docs/git-config/uk). 

[](https://git-scm.com/docs/git/uk#git-GITPROGRESSDELAY) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITPROGRESSDELAYcodespan)`GIT_PROGRESS_DELAY` 
    
Число, яке контролює, на скільки секунд слід затримати показ необов’язкових індикаторів виконання. За замовчуванням використовується значення 1. 

[](https://git-scm.com/docs/git/uk#git-GITEDITOR) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITEDITORcodespan)`GIT_EDITOR` 
    
Ця змінна середовища перевизначає `$EDITOR` та `$VISUAL`. Вона використовується кількома командами Git, коли в інтерактивному режимі потрібно запустити редактор. Див. також [git-var[1]](https://git-scm.com/docs/git-var/uk) та опцію `core.editor` у [git-config[1]](https://git-scm.com/docs/git-config/uk). 

[](https://git-scm.com/docs/git/uk#git-GITSEQUENCEEDITOR) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITSEQUENCEEDITORcodespan)`GIT_SEQUENCE_EDITOR` 
    
Ця змінна середовища перевизначає налаштований редактор Git під час редагування списку справ інтерактивного перебазування. Див. також [git-rebase[1]](https://git-scm.com/docs/git-rebase/uk) та опцію `sequence.editor` у [git-config[1]](https://git-scm.com/docs/git-config/uk). 

[](https://git-scm.com/docs/git/uk#git-GITSSH) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITSSHcodespan)`GIT_SSH` 


[](https://git-scm.com/docs/git/uk#git-GITSSHCOMMAND) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITSSHCOMMANDcodespan)`GIT_SSH_COMMAND` 
    
Якщо будь-яка з цих змінних середовища встановлена, то _git fetch_ та _git push_ використовуватимуть зазначену команду замість _ssh_ , коли їм потрібно буде підключитися до віддаленої системи. Параметри командного рядка, що передаються налаштованій команді, визначаються варіантом ssh. Дивіться опцію `ssh.variant` у [git-config[1]](https://git-scm.com/docs/git-config/uk) для отримання детальної інформації.
`$GIT_SSH_COMMAND` має пріоритет над `$GIT_SSH` та інтерпретується оболонкою, що дозволяє додавати додаткові аргументи. `$GIT_SSH`, з іншого боку, має бути лише шляхом до програми (яка може бути скриптом оболонки, якщо потрібні додаткові аргументи).
Зазвичай простіше налаштувати будь-які потрібні опції через ваш особистий файл `.ssh/config`. Будь ласка, зверніться до документації ssh для отримання додаткової інформації. 

[](https://git-scm.com/docs/git/uk#git-GITSSHVARIANT) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITSSHVARIANTcodespan)`GIT_SSH_VARIANT` 
    
Якщо цю змінну середовища встановлено, вона перевизначає автоматичне визначення Git, чи посилаються `GIT_SSH`/`GIT_SSH_COMMAND`/`core.sshCommand` на OpenSSH, plink чи tortoiseplink. Ця змінна перевизначає налаштування конфігурації `ssh.variant`, яке виконує ту саму функцію. 

[](https://git-scm.com/docs/git/uk#git-GITSSLNOVERIFY) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITSSLNOVERIFYcodespan)`GIT_SSL_NO_VERIFY` 
    
Встановлення та експорт цієї змінної середовища до будь-якого значення повідомляє Git, що не потрібно перевіряти SSL-сертифікат під час отримання або надсилання через HTTPS. 

[](https://git-scm.com/docs/git/uk#git-GITATTRSOURCE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITATTRSOURCEcodespan)`GIT_ATTR_SOURCE` 
    
Встановлює деревоподібну структуру, з якої будуть зчитуватися атрибути gitattributes. 

[](https://git-scm.com/docs/git/uk#git-GITASKPASS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITASKPASScodespan)`GIT_ASKPASS` 
    
Якщо цю змінну середовища встановлено, то команди Git, яким потрібно отримати паролі або парольні фрази (наприклад, для автентифікації HTTP або IMAP), викличуть цю програму з відповідним запитом як аргументом командного рядка та зчитають пароль з її STDOUT. Дивіться також опцію `core.askPass` у [git-config[1]](https://git-scm.com/docs/git-config/uk). 

[](https://git-scm.com/docs/git/uk#git-GITTERMINALPROMPT) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTERMINALPROMPTcodespan)`GIT_TERMINAL_PROMPT` 
    
Якщо для цієї булевої змінної середовища встановлено значення false, git не виводитиме запити в терміналі (наприклад, під час запиту HTTP-автентифікації). 

[](https://git-scm.com/docs/git/uk#git-GITCONFIGGLOBAL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCONFIGGLOBALcodespan)`GIT_CONFIG_GLOBAL` 


[](https://git-scm.com/docs/git/uk#git-GITCONFIGSYSTEM) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCONFIGSYSTEMcodespan)`GIT_CONFIG_SYSTEM` 
    
Беріть конфігурацію з заданих файлів, а не з глобальних або системних файлів конфігурації. Якщо встановлено `GIT_CONFIG_SYSTEM`, файл конфігурації системи, визначений під час збірки (зазвичай `/etc/gitconfig`), не буде зчитуватися. Аналогічно, якщо встановлено `GIT_CONFIG_GLOBAL`, ні `$HOME/.gitconfig`, ні `$XDG_CONFIG_HOME/git/config` не будуть зчитуватися. Можна встановити значення `/dev/null`, щоб пропустити зчитування файлів конфігурації відповідного рівня. 

[](https://git-scm.com/docs/git/uk#git-GITCONFIGNOSYSTEM) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCONFIGNOSYSTEMcodespan)`GIT_CONFIG_NOSYSTEM` 
    
Чи слід пропускати зчитування налаштувань із загальносистемного файлу `$`(`prefix`)`/etc/gitconfig`. Цю булеву змінну середовища можна використовувати разом із `$HOME` та `$XDG_CONFIG_HOME` для створення передбачуваного середовища для вимогливого скрипта, або ж встановити для неї значення true, щоб тимчасово уникнути використання файлу `/etc/gitconfig` з помилками, поки хтось із достатніми правами виправить це. 

[](https://git-scm.com/docs/git/uk#git-GITFLUSH) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITFLUSHcodespan)`GIT_FLUSH` 
    
Якщо для цієї булевої змінної середовища встановлено значення true, то такі команди, як _git blame_ (у поступовому режимі), _git rev-list_ , _git log_ , _git check-attr_ та _git check-ignore_ , примусово очищатимуть вихідний потік після очищення кожного запису. Якщо для цієї змінної встановлено значення false, вивід цих команд буде виконуватися з використанням повністю буферизованого вводу-виводу. Якщо цю змінну середовища не встановлено, Git вибере буферизоване або орієнтоване на записи очищення залежно від того, чи перенаправляється stdout до файлу чи ні. 

[](https://git-scm.com/docs/git/uk#git-GITTRACE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEcodespan)`GIT_TRACE` 
    
Дозволяє загальні повідомлення трасування, наприклад, розширення псевдонімів, виконання вбудованих команд та виконання зовнішніх команд.
Якщо для цієї змінної встановлено значення "1", "2" або "true" (порівняння не враховує регістр), повідомлення трасування будуть виведені на stderr.
Якщо змінній встановлено ціле значення більше за 2 та менше за 10 (строго кажучи), то Git інтерпретуватиме це значення як відкритий файловий дескриптор і спробує записати повідомлення трасування в цей файловий дескриптор.
Або ж, якщо змінній встановлено абсолютний шлях (що починається з символу _/_), Git інтерпретуватиме це як шлях до файлу та спробує додати до нього повідомлення трасування.
Скасування значення змінної або встановлення для неї порожнього значення, "0" або "false" (без урахування регістру) вимикає повідомлення трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACEFSMONITOR) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEFSMONITORcodespan)`GIT_TRACE_FSMONITOR` 
    
Вмикає повідомлення трасування для розширення монітора файлової системи. Див. `GIT_TRACE` для отримання доступних параметрів виводу трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACEPACKACCESS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEPACKACCESScodespan)`GIT_TRACE_PACK_ACCESS` 
    
Вмикає повідомлення трасування для всіх звернень до будь-яких пакетів. Для кожного звернення записується ім’я файлу пакета та зміщення в пакеті. Це може бути корисним для усунення деяких проблем продуктивності, пов’язаних з пакетом. Див. `GIT_TRACE` для отримання інформації про доступні параметри виводу трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACEPACKET) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEPACKETcodespan)`GIT_TRACE_PACKET` 
    
Вмикає повідомлення трасування для всіх пакетів, що надходять або виходять з певної програми. Це може допомогти з налагодженням узгодження об’єктів або іншими проблемами протоколу. Трасування вимикається для пакета, що починається з "PACK" (але див. `GIT_TRACE_PACKFILE` нижче). Див. `GIT_TRACE` для доступних параметрів виводу трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACEPACKFILE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEPACKFILEcodespan)`GIT_TRACE_PACKFILE` 
    
Дозволяє трасувати пакетні файли, надіслані або отримані певною програмою. На відміну від інших виводів трасування, це трасування є дослівним: без заголовків і без цитування двійкових даних. Ви майже напевно захочете направити його у файл (наприклад, `GIT_TRACE_PACKFILE=/tmp/my.pack`), а не відображати його в терміналі чи змішувати з іншими виводами трасування.
Зверніть увагу, що наразі це реалізовано лише для клієнтської частини клонів та вибірок. 

[](https://git-scm.com/docs/git/uk#git-GITTRACEPERFORMANCE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEPERFORMANCEcodespan)`GIT_TRACE_PERFORMANCE` 
    
Вмикає трасування повідомлень, пов’язаних із продуктивністю, наприклад, загальний час виконання кожної команди Git. Див. `GIT_TRACE` для отримання доступних параметрів трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACEREFS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEREFScodespan)`GIT_TRACE_REFS` 
    
Вмикає повідомлення трасування для операцій з базою даних посилань. Див. `GIT_TRACE` для отримання доступних параметрів виводу трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACESETUP) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACESETUPcodespan)`GIT_TRACE_SETUP` 
    
Дозволяє виводити повідомлення трасування .git, робоче дерево та поточний робочий каталог після завершення фази налаштування Git. Див. `GIT_TRACE` для доступних параметрів виводу трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACESHALLOW) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACESHALLOWcodespan)`GIT_TRACE_SHALLOW` 
    
Вмикає повідомлення трасування, які можуть допомогти налагоджувати вибірку/клонування поверхневих репозиторіїв. Див. `GIT_TRACE` для доступних параметрів виводу трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACECURL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACECURLcodespan)`GIT_TRACE_CURL` 
    
Вмикає повний дамп трасування curl для всіх вхідних та вихідних даних, включаючи описову інформацію, транспортного протоколу git. Це схоже на виконання curl `--trace-ascii` у командному рядку. Див. `GIT_TRACE` для доступних параметрів виводу трасування. 

[](https://git-scm.com/docs/git/uk#git-GITTRACECURLNODATA) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACECURLNODATAcodespan)`GIT_TRACE_CURL_NO_DATA` 
    
Коли ввімкнено трасування curl (див. `GIT_TRACE_CURL` вище), не виводьте дані (тобто виводьте лише інформаційні рядки та заголовки). 

[](https://git-scm.com/docs/git/uk#git-GITTRACE2) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACE2codespan)`GIT_TRACE2` 
    
Дозволяє отримувати детальніші повідомлення трасування з бібліотеки "trace2". Вивід з `GIT_TRACE2` — це простий текстовий формат для зручності читання людиною.
Якщо для цієї змінної встановлено значення "1", "2" або "true" (порівняння не враховує регістр), повідомлення трасування будуть виведені на stderr.
Якщо змінній встановлено ціле значення більше за 2 та менше за 10 (строго кажучи), то Git інтерпретуватиме це значення як відкритий файловий дескриптор і спробує записати повідомлення трасування в цей файловий дескриптор.
Або ж, якщо змінній встановлено абсолютний шлях (що починається з символу _/_), Git інтерпретуватиме це як шлях до файлу та спробує додати до нього повідомлення трасування. Якщо шлях вже існує та є каталогом, повідомлення трасування будуть записані до файлів (по одному на процес) у цьому каталозі, названих відповідно до останнього компонента SID та необов’язкового лічильника (щоб уникнути колізій імен файлів).
Крім того, якщо змінна має значення `af_unix:`[_< тип-сокета>_`:`]_< абсолютний-шлях>_, Git спробує відкрити шлях як Unix Domain Socket. Тип сокета може бути `stream` або `dgram`.
Скасування значення змінної або встановлення для неї порожнього значення, "0" або "false" (без урахування регістру) вимикає повідомлення трасування.
Див. [документація Trace2](https://git-scm.com/docs/api-trace2/uk) для отримання повної інформації. 

[](https://git-scm.com/docs/git/uk#git-GITTRACE2EVENT) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACE2EVENTcodespan)`GIT_TRACE2_EVENT` 
    
Цей параметр записує дані у форматі JSON, який підходить для машинної інтерпретації. Див. `GIT_TRACE2` для отримання доступних параметрів виводу трасування та [документація Trace2](https://git-scm.com/docs/api-trace2/uk) для отримання повної інформації. 

[](https://git-scm.com/docs/git/uk#git-GITTRACE2PERF) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACE2PERFcodespan)`GIT_TRACE2_PERF` 
    
Окрім текстових повідомлень, доступних у `GIT_TRACE2`, цей параметр записує формат на основі стовпців для розуміння вкладених областей. Див. `GIT_TRACE2` для отримання інформації про доступні параметри виводу трасування та [документація Trace2](https://git-scm.com/docs/api-trace2/uk) для отримання повної інформації. 

[](https://git-scm.com/docs/git/uk#git-GITTRACEREDACT) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITTRACEREDACTcodespan)`GIT_TRACE_REDACT` 
    
За замовчуванням, коли трасування активовано, Git видаляє значення файлів cookie, заголовків "Authorization:", "Proxy-Authorization:" та URI packfile. Встановіть для цієї логічної змінної середовища значення false, щоб запобігти цьому видаленню. 

[](https://git-scm.com/docs/git/uk#git-GITNOREPLACEOBJECTS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITNOREPLACEOBJECTScodespan)`GIT_NO_REPLACE_OBJECTS` 
    
Встановлення та експорт цієї змінної середовища вказує Git ігнорувати посилання на заміну та не замінювати об’єкти Git. 

[](https://git-scm.com/docs/git/uk#git-GITLITERALPATHSPECS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITLITERALPATHSPECScodespan)`GIT_LITERAL_PATHSPECS` 
    
Встановлення цієї логічної змінної середовища в значення true призведе до того, що Git трактуватиме всі специфікації шляхів буквально, а не як шаблони глобальних змінних. Наприклад, виконання команди `GIT_LITERAL_PATHSPECS=1` `git` `log` `--` `*.c'` шукатиме коміти, що стосуються шляху `*.c`, а не будь-які шляхи, яким відповідає глобальний змінний `*.c`. Вам може знадобитися це, якщо ви передаєте буквальні шляхи до Git (наприклад, шляхи, раніше надані вам за допомогою `git` `ls-tree`, вивід `--raw` diff тощо). 

[](https://git-scm.com/docs/git/uk#git-GITGLOBPATHSPECS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITGLOBPATHSPECScodespan)`GIT_GLOB_PATHSPECS` 
    
Встановлення цієї логічної змінної середовища в значення true призведе до того, що Git трактуватиме всі специфікації шляхів як шаблони глобів (також відомі як "глобальна" магія). 

[](https://git-scm.com/docs/git/uk#git-GITNOGLOBPATHSPECS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITNOGLOBPATHSPECScodespan)`GIT_NOGLOB_PATHSPECS` 
    
Встановлення цієї логічної змінної середовища в значення true призведе до того, що Git трактуватиме всі специфікації шляхів як літерали (тобто "літеральну" магію). 

[](https://git-scm.com/docs/git/uk#git-GITICASEPATHSPECS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITICASEPATHSPECScodespan)`GIT_ICASE_PATHSPECS` 
    
Якщо встановити для цієї логічної змінної середовища значення true, Git трактуватиме всі специфікації шляхів як нечутливі до регістру. 

[](https://git-scm.com/docs/git/uk#git-GITNOLAZYFETCH) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITNOLAZYFETCHcodespan)`GIT_NO_LAZY_FETCH` 
    
Встановлення цієї логічної змінної середовища на значення true повідомляє Git, що він не буде ліниво отримувати відсутні об’єкти з віддаленого сервера-промісника на вимогу. 

[](https://git-scm.com/docs/git/uk#git-GITREFLOGACTION) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITREFLOGACTIONcodespan)`GIT_REFLOG_ACTION` 
    
Коли посилання оновлюється, записи в журналі посилань створюються для відстеження причини оновлення посилання (зазвичай це назва команди верхнього рівня, яка оновила посилання), на додаток до старих та нових значень посилання. Скриптована команда Porcelain може використовувати допоміжну функцію set_reflog_action у `git-sh-setup`, щоб встановити свою назву для цієї змінної, коли вона викликається кінцевим користувачем як команда верхнього рівня, для запису в тілі журналу посилань. 

[](https://git-scm.com/docs/git/uk#git-GITREFPARANOIA) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITREFPARANOIAcodespan)`GIT_REF_PARANOIA` 
    
Якщо для цієї булевої змінної середовища встановлено значення false, ігноруйте пошкоджені або неправильно названі посилання під час ітерації по списках посилань. Зазвичай Git намагатиметься включити будь-які такі посилання, що може призвести до збою деяких операцій. Зазвичай це краще, оскільки потенційно деструктивні операції (наприклад, [git-prune[1]](https://git-scm.com/docs/git-prune/uk)) краще переривати, ніж ігнорувати пошкоджені посилання (і таким чином вважати історію, на яку вони вказують, невартою збереження). Значення за замовчуванням — `1` (тобто, варто побоюватися виявлення та переривання всіх операцій). Зазвичай вам не потрібно встановлювати це значення на `0`, але це може бути корисним під час спроби врятувати дані з пошкодженого репозиторію. 

[](https://git-scm.com/docs/git/uk#git-GITCOMMITGRAPHPARANOIA) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITCOMMITGRAPHPARANOIAcodespan)`GIT_COMMIT_GRAPH_PARANOIA` 
    
Під час завантаження об’єкта коміту з графу комітів, Git виконує перевірку існування об’єкта в базі даних об’єктів. Це робиться для того, щоб уникнути проблем із застарілими графами комітів, які містять посилання на вже видалені коміти, але це призводить до зниження продуктивності.
Значення за замовчуванням — «false», що вимикає вищезгадану поведінку. Встановлення цього значення на «true» вмикає перевірку існування, щоб застарілі коміти ніколи не поверталися з графа комітів, що призвело б до зниження продуктивності. 

[](https://git-scm.com/docs/git/uk#git-GITALLOWPROTOCOL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITALLOWPROTOCOLcodespan)`GIT_ALLOW_PROTOCOL` 
    
Якщо встановлено список протоколів, розділених двокрапками, поводитися так, ніби `protocol.allow` встановлено на `never`, і для кожного зі перелічених протоколів `protocol.`_< name>_`.allow` встановлено на `always` (замінюючи будь-яку існуючу конфігурацію). Див. опис `protocol.allow` у [git-config[1]](https://git-scm.com/docs/git-config/uk) для отримання додаткової інформації. 

[](https://git-scm.com/docs/git/uk#git-GITPROTOCOLFROMUSER) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITPROTOCOLFROMUSERcodespan)`GIT_PROTOCOL_FROM_USER` 
    
Встановіть цю булеву змінну середовища на значення false, щоб запобігти використанню протоколів fetch/push/clone, які налаштовані на стан `user`. Це корисно для обмеження рекурсивної ініціалізації підмодулів з ненадійного репозиторію або для програм, які передають потенційно ненадійні URL-адреси командам git. Див. [git-config[1]](https://git-scm.com/docs/git-config/uk) для отримання додаткової інформації. 

[](https://git-scm.com/docs/git/uk#git-GITPROTOCOL) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITPROTOCOLcodespan)`GIT_PROTOCOL` 
    
Тільки для внутрішнього використання. Використовується для встановлення зв’язку з протоколом Wire. Містить список ключів, розділених двокрапкою _:_ , з необов’язковими значеннями _< ключ>[=<значення>]_. Наявність невідомих ключів та значень слід ігнорувати.
Зверніть увагу, що сервери можуть потребувати налаштування, щоб дозволити цій змінній передавати дані через деякі транспортні канали. Вона буде поширюватися автоматично під час доступу до локальних репозиторіїв (тобто `file://` або шлях файлової системи), а також через протокол `git://`. Для git-over-http це має працювати автоматично в більшості конфігурацій, але див. обговорення в [git-http-backend[1]](https://git-scm.com/docs/git-http-backend/uk). Для git-over-ssh ssh-сервер може потребувати налаштування, щоб дозволити клієнтам передавати цю змінну (наприклад, використовуючи `AcceptEnv` `GIT_PROTOCOL` з OpenSSH).
Ця конфігурація необов’язкова. Якщо змінну не поширювати, клієнти повернуться до оригінального протоколу "v0" (але можуть втратити деякі покращення продуктивності або функції). Ця змінна наразі впливає лише на клони та вибірки; вона ще не використовується для надсилання (але може використовується в майбутньому). 

[](https://git-scm.com/docs/git/uk#git-GITOPTIONALLOCKS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITOPTIONALLOCKScodespan)`GIT_OPTIONAL_LOCKS` 
    
Якщо для цієї булевої змінної середовища встановлено значення false, Git виконає будь-яку запитувану операцію без виконання будь-яких необов’язкових підоперацій, які потребують блокування. Наприклад, це запобіжить оновленню індексу `git` `status` як побічний ефект. Це корисно для процесів, що працюють у фоновому режимі та не хочуть спричиняти конфлікт блокувань з іншими операціями в репозиторії. За замовчуванням `1`. 

[](https://git-scm.com/docs/git/uk#git-GITREDIRECTSTDIN) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITREDIRECTSTDINcodespan)`GIT_REDIRECT_STDIN` 


[](https://git-scm.com/docs/git/uk#git-GITREDIRECTSTDOUT) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITREDIRECTSTDOUTcodespan)`GIT_REDIRECT_STDOUT` 


[](https://git-scm.com/docs/git/uk#git-GITREDIRECTSTDERR) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITREDIRECTSTDERRcodespan)`GIT_REDIRECT_STDERR` 
    
Тільки для Windows: дозволяє перенаправлення стандартних дескрипторів вводу/виводу/помилок на шляхи, визначені змінними середовища. Це особливо корисно в багатопотокових застосунках, де канонічний спосіб передачі стандартних дескрипторів через `CreateProcess`() не є варіантом, оскільки це вимагатиме, щоб дескриптори були позначені як успадковувані (і, як наслідок, **кожен** породжений процес успадковуватиме їх, можливо, блокуючи звичайні операції Git). Основним цільовим варіантом використання є використання іменованих каналів для зв’язку (наприклад, _\\\\.\pipe\my-git-stdin-123_).
Підтримуються два спеціальні значення: `off` просто закриє відповідний стандартний дескриптор, а якщо `GIT_REDIRECT_STDERR` дорівнює _2 >&1_, стандартна помилка буде перенаправлена на той самий дескриптор, що й стандартний вивід. 

[](https://git-scm.com/docs/git/uk#git-GITPRINTSHA1ELLIPSIS) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITPRINTSHA1ELLIPSIScodespan)`GIT_PRINT_SHA1_ELLIPSIS` (застарілий) 
    
Якщо встановлено значення `yes`, вивести три крапки після (скороченого) значення SHA-1. Це впливає на індикацію відокремлених HEAD ([git-checkout[1]](https://git-scm.com/docs/git-checkout/uk)) та необроблений вивід diff ([git-diff[1]](https://git-scm.com/docs/git-diff/uk)). Виведення трикрапки у згаданих випадках більше не вважається адекватним, і його підтримка, ймовірно, буде видалена в найближчому майбутньому (разом зі змінною). 

[](https://git-scm.com/docs/git/uk#git-GITADVICE) [](https://git-scm.com/docs/git/uk#git-spanclasssynopsiscodeGITADVICEcodespan)`GIT_ADVICE` 
    
Якщо встановлено значення `0`, то вимкніть усі повідомлення з порадами. Ці повідомлення призначені для надання підказок користувачам, які можуть допомогти їм вийти з проблемних ситуацій або скористатися новими функціями. Користувачі можуть вимикати окремі повідомлення за допомогою ключів конфігурації `advice.*`. Ці повідомлення можуть заважати інструментам, що виконують процеси Git, тому ця змінна доступна для вимкнення повідомлень. (Глобальний параметр `--no-advice` також доступний, але старі версії Git можуть не працювати, якщо цей параметр не зрозумілий. Змінна середовища буде ігноруватися версіями Git, які її не розуміють.)
##  [](https://git-scm.com/docs/git/uk#_%D0%BE%D0%B1%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%B5%D0%BD%D0%BD%D1%8F)Обговорення
Більш детальну інформацію про наступне можна знайти за [розділ посібника користувача про концепції Git](https://git-scm.com/docs/user-manual/uk#git-concepts) та [gitcore-tutorial[7]](https://git-scm.com/docs/gitcore-tutorial/uk).
Проект Git зазвичай складається з робочого каталогу з підкаталогом ".git" на верхньому рівні. Каталог .git містить, серед іншого, стиснуту базу даних об’єктів, що представляє повну історію проекту, файл "індексу", який пов’язує цю історію з поточним вмістом робочого дерева, та іменовані вказівники на цю історію, такі як теги та заголовки гілок.
База даних об’єктів містить об’єкти трьох основних типів: блоби, які зберігають дані файлів; дерева, які вказують на блоби та інші дерева для побудови ієрархій каталогів; та коміти, кожен з яких посилається на одне дерево та певну кількість батьківських комітів.
Коміт, еквівалентний тому, що в інших системах називається «набором змін» або «версією», представляє крок в історії проєкту, а кожен батьківський елемент представляє безпосередньо попередній крок. Коміти з більш ніж одним батьківським елементом представляють злиття незалежних ліній розробки.
Усі об’єкти іменуються за допомогою SHA-1 хешу їхнього вмісту, який зазвичай записується у вигляді рядка з 40 шістнадцяткових цифр. Такі імена є глобально унікальними. Всю історію, що веде до коміту, можна підтвердити, підписавши лише цей коміт. Для цієї мети передбачено четвертий тип об’єкта, тег.
Під час першого створення об’єкти зберігаються в окремих файлах, але для ефективності пізніше їх можна стиснути разом у «пакетні файли».
Іменовані вказівники, які називаються посиланнями (refs), позначають цікаві моменти в історії. Посилання може містити SHA-1-ім’я об’єкта або ім’я іншого посилання (останнє називається "символічним посиланням"). Посилання з іменами, що починаються з `refs/head/`, містять SHA-1-ім’я останнього коміту (або "head") гілки, що розробляється. SHA-1-імена тегів, що цікавлять, зберігаються в `refs/tags/`. Символічне посилання з іменем `HEAD` містить ім’я поточної витягнутої гілки.
Файл індексу ініціалізується списком усіх шляхів та, для кожного шляху, об’єктом blob та набором атрибутів. Об’єкт blob представляє вміст файлу станом на початок поточної гілки. Атрибути (час останньої зміни, розмір тощо) беруться з відповідного файлу в робочому дереві. Подальші зміни в робочому дереві можна знайти шляхом порівняння цих атрибутів. Індекс можна оновлювати новим вмістом, а нові коміти можна створювати з вмісту, що зберігається в індексі.
Індекс також може зберігати кілька записів (так званих "етапів") для заданого шляху. Ці етапи використовуються для зберігання різних необ’єднаних версій файлу під час виконання об’єднання.
##  [](https://git-scm.com/docs/git/uk#_%D0%B1%D0%B5%D0%B7%D0%BF%D0%B5%D0%BA%D0%B0)БЕЗПЕКА
Деякі параметри конфігурації та файли перехоплень можуть призвести до запуску Git довільних команд оболонки. Оскільки конфігурація та перехоплення не копіюються за допомогою `git` `clone`, загалом безпечно клонувати віддалені репозиторії з ненадійним вмістом, перевіряти їх за допомогою `git` `log` тощо.
Однак, небезпечно запускати команди Git у каталозі `.git` (або робочому дереві, що його оточує), якщо цей каталог `.git` походить з ненадійного джерела. Команди в його конфігурації та перехопленнях виконуються звичайним чином.
За замовчуванням Git відмовиться запускатися, якщо репозиторій належить комусь іншому, ніж користувач, який виконує команду. Див. запис `safe.directory` у [git-config[1]](https://git-scm.com/docs/git-config/uk). Хоча це може допомогти захистити вас у багатокористувацькому середовищі, зверніть увагу, що ви також можете отримати ненадійні репозиторії, які належать вам (наприклад, якщо ви розпакуєте zip-файл або tar-архів з ненадійного джерела). У таких випадках вам спочатку потрібно буде "очистити" ненадійний репозиторій.
Якщо у вас є ненадійний каталог `.git`, спочатку слід клонувати його за допомогою `git` `clone` `--no-local`, щоб отримати чисту копію. Git обмежує набір опцій та перехоплювачів, які будуть виконуватися `upload-pack`, що обробляє серверну частину клону або fetch, але майте на увазі, що область поверхні для атаки на `upload-pack` велика, тому це несе певний ризик. Найбезпечніше — обслуговувати репозиторій як непривілейований користувач (або через [git-daemon[1]](https://git-scm.com/docs/git-daemon/uk), ssh, або використовуючи інші інструменти для зміни ідентифікаторів користувачів). Дивіться обговорення в розділі _БЕЗПЕКА_ у [git-upload-pack[1]](https://git-scm.com/docs/git-upload-pack/uk).
##  [](https://git-scm.com/docs/git/uk#_%D0%B4%D0%BE%D0%B4%D0%B0%D1%82%D0%BA%D0%BE%D0%B2%D0%B0_%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D1%96%D1%8F)ДОДАТКОВА ДОКУМЕНТАЦІЯ
Дивіться посилання в розділі «опис», щоб розпочати роботу з Git. Наведена нижче інформація, ймовірно, містить більше деталей, ніж потрібно для користувача-початківця.
У розділах [розділ про концепції Git у посібнику користувача](https://git-scm.com/docs/user-manual/uk#git-concepts) та [gitcore-tutorial[7]](https://git-scm.com/docs/gitcore-tutorial/uk) наведено вступ до базової архітектури Git.
Див. огляд рекомендованих робочих процесів у [gitworkflows[7]](https://git-scm.com/docs/gitworkflows/uk).
Дивіться також документи за [howto](https://git-scm.com/docs/howto-index/uk) для отримання корисних прикладів.
Внутрішня документація описана за [Документація Git API](https://git-scm.com/docs/api-index/uk).
Користувачам, які мігрують з CVS, також може бути цікаво прочитати [gitcvs-migration[7]](https://git-scm.com/docs/gitcvs-migration/uk).
##  [](https://git-scm.com/docs/git/uk#_%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B8)Автори
Git був започаткований Лінусом Торвальдсом, а наразі його підтримує Джуніо К. Хамано. Численні внески надійшли зі списку розсилки Git <git@vger.kernel.org>. <https://openhub.net/p/git/contributors/summary> надає вам повніший список учасників.
Якщо у вас є клон самого git.git, вивід [git-shortlog[1]](https://git-scm.com/docs/git-shortlog/uk) та [git-blame[1]](https://git-scm.com/docs/git-blame/uk) може показати вам авторів певних частин проєкту.
##  [](https://git-scm.com/docs/git/uk#_%D0%BF%D0%BE%D0%B2%D1%96%D0%B4%D0%BE%D0%BC%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%BF%D1%80%D0%BE_%D0%BF%D0%BE%D0%BC%D0%B8%D0%BB%D0%BA%D0%B8)Повідомлення про помилки
Повідомляйте про помилки до списку розсилки Git <git@vger.kernel.org>, де в основному здійснюється розробка та підтримка. Вам не потрібно бути підписаним на список, щоб надіслати туди повідомлення. Перегляньте архів списку розсилки за адресою <https://lore.kernel.org/git>, щоб переглянути попередні звіти про помилки та інші обговорення.
Проблеми, що стосуються безпеки, слід повідомляти приватно до списку розсилки Git Security <git-security@googlegroups.com>.
##  [](https://git-scm.com/docs/git/uk#_%D0%B4%D0%B8%D0%B2_%D1%82%D0%B0%D0%BA%D0%BE%D0%B6)ДИВ. ТАКОЖ
[gittutorial[7]](https://git-scm.com/docs/gittutorial/uk), [gittutorial-2[7]](https://git-scm.com/docs/gittutorial-2/uk), [giteveryday[7]](https://git-scm.com/docs/giteveryday/uk), [gitcvs-migration[7]](https://git-scm.com/docs/gitcvs-migration/uk), [gitglossary[7]](https://git-scm.com/docs/gitglossary/uk), [gitcore-tutorial[7]](https://git-scm.com/docs/gitcore-tutorial/uk), [gitcli[7]](https://git-scm.com/docs/gitcli/uk), [Посібник користувача Git](https://git-scm.com/docs/user-manual/uk), [gitworkflows[7]](https://git-scm.com/docs/gitworkflows/uk)
##  [](https://git-scm.com/docs/git/uk#_git)GIT
Частина набору [git[1]](https://git-scm.com/docs/git/uk)
[About this site](https://git-scm.com/site)  
Patches, suggestions, and comments are welcome. 
Git is a member of [Software Freedom Conservancy](https://git-scm.com/sfc)
