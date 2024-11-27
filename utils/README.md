# README

Have some utils that help to fine tune the `dotfiles` settings, such as ANSI colors.

|       | Utils | Description |
| ----: | :---- | :---------- |
| 1 | ansi_color_table.py | Loop through all 256 ANSI codes and print the RGB/HEX codes and sample colors. |
| 2 | ansi_markdown_table.py | Loop through all 256 ANSI codes and generate rows for the Markdown table. | 
| 3 | color2.bash | Simple BASH to compare 2 different colors. | 

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

```console
$ bash color2.bash
This is DYEL (ANSI 154) - Dynamic Yellow #DFFF00
This is LIME (ANSI 118) - Lime Green #7FFF00
Side-by-side comparison:
DYEL | LIME
```
