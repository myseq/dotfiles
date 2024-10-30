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
├── private.envs         # Excluded by .gitignore
├── bash.aliases         # BASH: aliases
├── bash.func            # BASH: functions
├── zshrc                # ZSH: zshrc 
├── zsh.aliases          # ZSH: aliases
└── zsh.func             # ZSH: functions 
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



