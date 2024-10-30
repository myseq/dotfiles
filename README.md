# DotFiles

This includes all my `dotfiles` setup/config.

And everything start from `shellstartup`.

## Begin 

Everything start from `shellstartup`.

Here's the basic file structure.

```bash
dotfiles/
├── shellstartup         # main startup file
├── shell.envs           # All env exports
├── bash.aliases         # Aliases for BASH
├── bash.func            # Some BASH functions
├── zshrc                # ZSH 
├── zsh.aliases          # Aliases for ZSH
└── zsh.func             # Some ZSH functions 
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



