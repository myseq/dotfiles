def ansi256_to_rgb(ansi_code):
    """
    Convert an ANSI 256 color code to an RGB tuple.
    """
    if 0 <= ansi_code <= 15:
        # Standard colors (0-15)
        ansi_palette = [
            (0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0),
            (0, 0, 128), (128, 0, 128), (0, 128, 128), (192, 192, 192),
            (128, 128, 128), (255, 0, 0), (0, 255, 0), (255, 255, 0),
            (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255),
        ]
        return ansi_palette[ansi_code]
    elif 16 <= ansi_code <= 231:
        # 6x6x6 color cube (16-231)
        ansi_code -= 16
        r = (ansi_code // 36) % 6 * 40 + 55
        g = (ansi_code // 6) % 6 * 40 + 55
        b = ansi_code % 6 * 40 + 55
        return (r, g, b)
    elif 232 <= ansi_code <= 255:
        # Grayscale colors (232-255)
        gray = (ansi_code - 232) * 10 + 8
        return (gray, gray, gray)
    else:
        raise ValueError("ANSI code must be in the range 0-255")


def rgb_to_hex(rgb):
    """
    Convert an RGB tuple to a HEX string.
    """
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def markdown_color_row(ansi_code, rgb, hex_color):
    """
    Generate a row for the Markdown table with the color block.
    """
    color_block = f'<span style="background-color:{hex_color};color:{hex_color}">█</span>'
    return f"| {ansi_code:3} | {rgb} | {hex_color} | {color_block} |"


if __name__ == "__main__":
    # Header for the Markdown table
    print("| ANSI Code | RGB          | HEX      | Color Block |")
    print("|-----------|--------------|----------|-------------|")

    # Loop through all 256 ANSI codes and generate rows for the Markdown table
    for code in range(256):
        rgb = ansi256_to_rgb(code)
        hex_color = rgb_to_hex(rgb)
        print(markdown_color_row(code, rgb, hex_color))

