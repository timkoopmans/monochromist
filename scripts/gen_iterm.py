#!/usr/bin/env python3
"""Generate .itermcolors files from palette."""
from pathlib import Path

def hx(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def color(name, h):
    r, g, b = hx(h)
    return f"""\t<key>{name}</key>
\t<dict>
\t\t<key>Color Space</key><string>sRGB</string>
\t\t<key>Red Component</key><real>{r:.6f}</real>
\t\t<key>Green Component</key><real>{g:.6f}</real>
\t\t<key>Blue Component</key><real>{b:.6f}</real>
\t\t<key>Alpha Component</key><real>1</real>
\t</dict>"""

def build(palette, out):
    keys = [
        ("Ansi 0 Color",  palette["ansi"][0]),
        ("Ansi 1 Color",  palette["ansi"][1]),
        ("Ansi 2 Color",  palette["ansi"][2]),
        ("Ansi 3 Color",  palette["ansi"][3]),
        ("Ansi 4 Color",  palette["ansi"][4]),
        ("Ansi 5 Color",  palette["ansi"][5]),
        ("Ansi 6 Color",  palette["ansi"][6]),
        ("Ansi 7 Color",  palette["ansi"][7]),
        ("Ansi 8 Color",  palette["ansi"][8]),
        ("Ansi 9 Color",  palette["ansi"][9]),
        ("Ansi 10 Color", palette["ansi"][10]),
        ("Ansi 11 Color", palette["ansi"][11]),
        ("Ansi 12 Color", palette["ansi"][12]),
        ("Ansi 13 Color", palette["ansi"][13]),
        ("Ansi 14 Color", palette["ansi"][14]),
        ("Ansi 15 Color", palette["ansi"][15]),
        ("Background Color", palette["bg"]),
        ("Foreground Color", palette["fg"]),
        ("Bold Color",       palette["bold"]),
        ("Cursor Color",     palette["cursor"]),
        ("Cursor Text Color", palette["cursor_text"]),
        ("Selection Color",  palette["selection"]),
        ("Selected Text Color", palette["selected_text"]),
        ("Link Color",       palette["link"]),
        ("Badge Color",      palette["accent"]),
    ]
    body = "\n".join(color(k, v) for k, v in keys)
    plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
{body}
</dict>
</plist>
"""
    out.write_text(plist)

# Strict grayscale ramp:
# F4F4F4 E3E3E3 D2D2D2 C0C0C0 AFAFAF 9D9D9D 8C8C8C 7A7A7A 696969 575757 464646 343434 232323 111111

dark = {
    "ansi": [
        "#343434", "#C0C0C0", "#9D9D9D", "#AFAFAF",
        "#D2D2D2", "#8C8C8C", "#C0C0C0", "#E3E3E3",
        "#575757", "#E3E3E3", "#AFAFAF", "#C0C0C0",
        "#E3E3E3", "#9D9D9D", "#D2D2D2", "#F4F4F4",
    ],
    "bg": "#343434",
    "fg": "#E3E3E3",
    "bold": "#F4F4F4",
    "cursor": "#F4F4F4",
    "cursor_text": "#343434",
    "selection": "#575757",
    "selected_text": "#F4F4F4",
    "link": "#F4F4F4",
    "accent": "#F4F4F4",
}

light = {
    "ansi": [
        "#111111", "#464646", "#696969", "#575757",
        "#343434", "#7A7A7A", "#464646", "#E3E3E3",
        "#696969", "#232323", "#575757", "#464646",
        "#232323", "#696969", "#343434", "#F4F4F4",
    ],
    "bg": "#F4F4F4",
    "fg": "#232323",
    "bold": "#111111",
    "cursor": "#111111",
    "cursor_text": "#F4F4F4",
    "selection": "#C0C0C0",
    "selected_text": "#111111",
    "link": "#111111",
    "accent": "#111111",
}

root = Path(__file__).resolve().parent.parent / "iterm2"
root.mkdir(parents=True, exist_ok=True)
build(dark,  root / "monochromist-dark.itermcolors")
build(light, root / "monochromist-light.itermcolors")
print("wrote:", root)
