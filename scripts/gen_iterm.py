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
        "#111827", "#B36A6A", "#7A9C7A", "#B8A06A",
        "#7B92AC", "#6B7280", "#D1D5DB", "#F9FAFB",
        "#4B5563", "#C88080", "#94B894", "#D4BC80",
        "#93A8C2", "#9CA3AF", "#E5E7EB", "#FFFFFF",
    ],
    "bg": "#111827",
    "fg": "#F9FAFB",
    "bold": "#FFFFFF",
    "cursor": "#F9FAFB",
    "cursor_text": "#111827",
    "selection": "#374151",
    "selected_text": "#F9FAFB",
    "link": "#7B92AC",
    "accent": "#7B92AC",
}

light = {
    "ansi": [
        "#111827", "#944747", "#4F6F4F", "#8A7440",
        "#4A6582", "#6B7280", "#374151", "#F9FAFB",
        "#9CA3AF", "#B36A6A", "#6F8F6F", "#A88858",
        "#7B92AC", "#6B7280", "#4B5563", "#FFFFFF",
    ],
    "bg": "#F9FAFB",
    "fg": "#111827",
    "bold": "#000000",
    "cursor": "#111827",
    "cursor_text": "#F9FAFB",
    "selection": "#D1D5DB",
    "selected_text": "#111827",
    "link": "#4A6582",
    "accent": "#4A6582",
}

root = Path(__file__).resolve().parent.parent / "iterm2"
root.mkdir(parents=True, exist_ok=True)
build(dark,  root / "monochromist-dark.itermcolors")
build(light, root / "monochromist-light.itermcolors")
print("wrote:", root)
