# DotFiles

This includes all my `dotfiles` setup/config.

And everything start from `shellstartup`.

> To update, simple `git pull --rebase`.
> It simply combining your local changes with the latest published changes on your remote.

## Begin 

Everything start from `shellstartup`.

Here's the basic file structure.

```bash
dotfiles/
├── bash.aliases        # BASH: aliases
├── bash.func           # BASH: functions
├── gitconfig           # git config file
├── private.envs        # Excluded by .gitignore
├── profiles/           # Folder: profile pictures
├── pythonstartup       # Python startup file
├── shell.envs          # All env exports
├── shellstartup        # main startup file
├── utils/              # Folder: utilities/scripts
├── vimrc               # vim config file
├── zsh.aliases         # ZSH: aliases
├── zsh.func            # ZSH: functions
└── zshrc               # ZSH: zshrc
```

### BASH

Append the following line to the end `.bashrc`.

```bash
source $HOME/dotfiles/shellstartup
```

### ZSH

Install `zsh` first.

```console
$ sudo apt install zsh
$ touch .zshrc
```

Append the following line to the end `.zshrc`.

```bash
source $HOME/dotfiles/shellstartup
```

### Markdown Viewer (mdv)

```console
% sudo apt install python3-pip
% pip3 install mdv --break-system-packages 
```

## Troubleshoot

To setup the `.gitconfig`: `ln -s dotfiles/gitconfig ~/.gitconfig`

To reset the Git repo remote-url from HTTPS to SSH: `git remote set-url origin git@github.com:myseq/dotfiles.git`


