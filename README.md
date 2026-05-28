# monochromist

A monochromatic theme for iTerm2, Zed, and Obsidian. Bootstrap-inspired cool grayscale with green/red semantic accents reserved for diff/diagnostics. Dark + light variants.

Inspired by [anotherglitchinthematrix/monochrome](https://github.com/anotherglitchinthematrix/monochrome).

## Fonts

- Serif: [Atkinson Hyperlegible](https://fonts.google.com/specimen/Atkinson+Hyperlegible)
- Monospace: [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono)
- UI: [Inter](https://fonts.google.com/specimen/Inter)

## Palette

See [palette.md](palette.md).

## Install

Themes live here and are symlinked into each app's config location by [dotfiles](https://github.com/timkoopmans/dotfiles) `install.sh`.

Manual install:

### iTerm2

```sh
open -a iTerm iterm2/monochromist-dark.itermcolors
open -a iTerm iterm2/monochromist-light.itermcolors
```

Then iTerm2 → Settings → Profiles → Colors → Color Presets → pick `monochromist-dark` or `monochromist-light`.

### Zed

```sh
mkdir -p ~/.config/zed/themes
ln -sfn "$PWD/zed/monochromist.json" ~/.config/zed/themes/monochromist.json
```

Zed → Settings → Theme → `Monochromist Dark` / `Monochromist Light`.

### Obsidian

```sh
mkdir -p <vault>/.obsidian/themes/Monochromist
ln -sfn "$PWD/obsidian/theme.css" <vault>/.obsidian/themes/Monochromist/theme.css
ln -sfn "$PWD/obsidian/manifest.json" <vault>/.obsidian/themes/Monochromist/manifest.json
```

Obsidian → Settings → Appearance → Theme → `Monochromist`.

## License

MIT
