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

dark = {
    "ansi": [
        "#0E0E0E", "#B36A6A", "#7A9C7A", "#B8A06A",
        "#6B8EAE", "#8A8A8A", "#B8B8B8", "#E8E8E8",
        "#5A5A5A", "#C88080", "#94B894", "#D4BC80",
        "#88A8C8", "#B8B8B8", "#D8D8D8", "#FFFFFF",
    ],
    "bg": "#0E0E0E",
    "fg": "#E8E8E8",
    "bold": "#FFFFFF",
    "cursor": "#E8E8E8",
    "cursor_text": "#0E0E0E",
    "selection": "#2A2A2A",
    "selected_text": "#E8E8E8",
    "link": "#6B8EAE",
    "accent": "#6B8EAE",
}

light = {
    "ansi": [
        "#1A1A1A", "#944747", "#4F6F4F", "#8A7440",
        "#4A6582", "#6A6A6A", "#3D3D3D", "#FAFAF8",
        "#6A6A6A", "#B36A6A", "#6F8F6F", "#A88858",
        "#6B8EAE", "#8A8A8A", "#5A5A5A", "#FFFFFF",
    ],
    "bg": "#FAFAF8",
    "fg": "#1A1A1A",
    "bold": "#000000",
    "cursor": "#1A1A1A",
    "cursor_text": "#FAFAF8",
    "selection": "#D8D8D6",
    "selected_text": "#1A1A1A",
    "link": "#4A6582",
    "accent": "#4A6582",
}

root = Path(__file__).resolve().parent.parent / "iterm2"
root.mkdir(parents=True, exist_ok=True)
build(dark,  root / "monochromist-dark.itermcolors")
build(light, root / "monochromist-light.itermcolors")
print("wrote:", root)
