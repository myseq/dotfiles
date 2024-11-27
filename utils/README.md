# README

Have some utils that help to fine tune the `dotfiles` settings, such as ANSI colors.

|       | Utils | Description |
| ----: | :---- | :---------- |
| 1 | ansi_color_table.py | Loop through all 256 ANSI codes and print the RGB/HEX codes and sample colors. |
| 2 | ansi_markdown_table.py | Loop through all 256 ANSI codes and generate rows for the Markdown table. | 

## ANSI Color

```console
$ python ansi_color_table.py 
ANSI Code  RGB               HEX        Color
==================================================
ANSI Code   0: RGB (0, 0, 0)      | HEX #000000  █████
ANSI Code   1: RGB (128, 0, 0)    | HEX #800000  █████
ANSI Code   2: RGB (0, 128, 0)    | HEX #008000  █████
...
ANSI Code 154: RGB (209, 255, 0)  | HEX #D1FF00  █████
ANSI Code 255: RGB (248, 248, 248)| HEX #F8F8F8  █████
```

```console
$ python ansi_markdown_table.py > ansi_color_table.md
```

