# monochromist palette

Bootstrap-inspired cool grayscale + green/red semantic accents for diff/diagnostics.

## Mono ramp (single source of truth)

| Name             | Hex       |
|------------------|-----------|
| bright-snow      | `#F8F9FA` |
| platinum         | `#E9ECEF` |
| alabaster-grey   | `#DEE2E6` |
| pale-slate       | `#CED4DA` |
| pale-slate-2     | `#ADB5BD` |
| slate-grey       | `#6C757D` |
| iron-grey        | `#495057` |
| gunmetal         | `#343A40` |
| carbon-black     | `#212529` |

## Semantic (allowed colors)

| Role         | Dark        | Light       |
|--------------|-------------|-------------|
| red/error    | `#D97F7F`   | `#B03A3A`   |
| red dim      | `#8C4242`   | `#7A2828`   |
| green/ok     | `#7FC09A`   | `#2E6E46`   |
| green dim    | `#4F7D63`   | `#1F4D30`   |

Used only for: errors, diff add/remove, success states. Warnings stay grayscale.

## Dark (bg gunmetal)

| Role            | Hex       |
|-----------------|-----------|
| bg0 (page)      | `#343A40` gunmetal |
| bg1 (panel)     | `#495057` iron-grey |
| bg2 (elevated)  | `#6C757D` slate-grey |
| bg3 (select)    | `#ADB5BD` pale-slate-2 |
| border          | `#495057` |
| fg3 (disabled)  | `#6C757D` |
| fg2 (comment)   | `#ADB5BD` italic |
| fg1 (muted)     | `#CED4DA` |
| property        | `#CED4DA` |
| primary         | `#DEE2E6` |
| accent/emphasis | `#F8F9FA` bright-snow |

## Light (bg bright-snow)

| Role            | Hex       |
|-----------------|-----------|
| bg0 (page)      | `#F8F9FA` bright-snow |
| bg1 (panel)     | `#E9ECEF` platinum |
| bg2 (elevated)  | `#DEE2E6` alabaster-grey |
| bg3 (select)    | `#CED4DA` pale-slate |
| border          | `#CED4DA` |
| fg-disabled     | `#ADB5BD` |
| fg2 (comment)   | `#6C757D` slate-grey italic |
| fg1 (muted)     | `#495057` iron-grey |
| property        | `#343A40` gunmetal |
| primary         | `#212529` carbon-black |
| accent/emphasis | `#212529` carbon-black |
