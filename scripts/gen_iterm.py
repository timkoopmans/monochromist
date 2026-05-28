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

# Palette:
# bright-snow #f8f9fa  platinum #e9ecef  alabaster-grey #dee2e6
# pale-slate #ced4da   pale-slate-2 #adb5bd   slate-grey #6c757d
# iron-grey #495057    gunmetal #343a40       carbon-black #212529
# semantic: red #d97f7f / #b03a3a   green #7fc09a / #2e6e46

dark = {
    "ansi": [
        "#343A40", "#D97F7F", "#7FC09A", "#CED4DA",
        "#DEE2E6", "#ADB5BD", "#CED4DA", "#DEE2E6",
        "#6C757D", "#E8A5A5", "#A5D4B8", "#E9ECEF",
        "#E9ECEF", "#CED4DA", "#E9ECEF", "#F8F9FA",
    ],
    "bg": "#343A40",
    "fg": "#DEE2E6",
    "bold": "#F8F9FA",
    "cursor": "#F8F9FA",
    "cursor_text": "#343A40",
    "selection": "#495057",
    "selected_text": "#F8F9FA",
    "link": "#F8F9FA",
    "accent": "#F8F9FA",
}

light = {
    "ansi": [
        "#212529", "#B03A3A", "#2E6E46", "#495057",
        "#212529", "#495057", "#343A40", "#DEE2E6",
        "#495057", "#C75252", "#3E8C5A", "#343A40",
        "#000000", "#343A40", "#212529", "#F8F9FA",
    ],
    "bg": "#F8F9FA",
    "fg": "#212529",
    "bold": "#000000",
    "cursor": "#212529",
    "cursor_text": "#F8F9FA",
    "selection": "#CED4DA",
    "selected_text": "#212529",
    "link": "#212529",
    "accent": "#212529",
}

root = Path(__file__).resolve().parent.parent / "iterm2"
root.mkdir(parents=True, exist_ok=True)
build(dark,  root / "monochromist-dark.itermcolors")
build(light, root / "monochromist-light.itermcolors")
print("wrote:", root)
