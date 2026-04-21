#!/bin/bash -x

LN=`which ln`

$LN -s dotfiles/vimrc ~/.vimrc
$LN -s dotfiles/gitconfig ~/.gitconfig
$LN -s dotfiles/pythonstartup ~/.pythonstartup

