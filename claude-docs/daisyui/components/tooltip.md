# Tooltip

Tooltip can be used to show a message when hovering over an element.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| tooltip | Component | Container element |
| tooltip-content | Part | Optional. Setting a div as the content of the tooltip instead of the `data-tip` text |
| tooltip-top | Placement | Put tooltip on top[Default] |
| tooltip-bottom | Placement | Put tooltip on bottom |
| tooltip-left | Placement | Put tooltip on left |
| tooltip-right | Placement | Put tooltip on right |
| tooltip-open | Modifier | Force open tooltip |
| tooltip-neutral | Color | neutral color |
| tooltip-primary | Color | primary color |
| tooltip-secondary | Color | secondary color |
| tooltip-accent | Color | accent color |
| tooltip-info | Color | info color |
| tooltip-success | Color | success color |
| tooltip-warning | Color | warning color |
| tooltip-error | Color | error color |

## HTML Examples

### Tooltip

```html
<div class="tooltip" data-tip="hello">
  <button class="btn">Hover me</button>
</div>
```

### Tooltip with tooltip-content

```html
<div class="tooltip">
  <div class="tooltip-content">
    <div class="animate-bounce text-orange-400 -rotate-10 text-2xl font-black">Wow!</div>
  </div>
  <button class="btn">Hover me</button>
</div>
```

### Force open

```html
<div class="tooltip tooltip-open" data-tip="hello">
  <button class="btn">Force open</button>
</div>
```

### Top

```html
<div class="tooltip tooltip-open tooltip-top" data-tip="hello">
  <button class="btn">Top</button>
</div>
```

### Bottom

```html
<div class="tooltip tooltip-open tooltip-bottom" data-tip="hello">
  <button class="btn">Bottom</button>
</div>
```

### Left

```html
<div class="tooltip tooltip-open tooltip-left" data-tip="hello">
  <button class="btn">Left</button>
</div>
```

### Right

```html
<div class="tooltip tooltip-open tooltip-right" data-tip="hello">
  <button class="btn">Right</button>
</div>
```

### Neutral color

```html
<div class="tooltip tooltip-open tooltip-neutral" data-tip="neutral">
  <button class="btn btn-neutral">neutral</button>
</div>
```

### Primary color

```html
<div class="tooltip tooltip-open tooltip-primary" data-tip="primary">
  <button class="btn btn-primary">primary</button>
</div>
```

### Secondary color

```html
<div class="tooltip tooltip-open tooltip-secondary" data-tip="secondary">
  <button class="btn btn-secondary">secondary</button>
</div>
```

### Accent color

```html
<div class="tooltip tooltip-open tooltip-accent" data-tip="accent">
  <button class="btn btn-accent">accent</button>
</div>
```

### Info color

```html
<div class="tooltip tooltip-open tooltip-info" data-tip="info">
  <button class="btn btn-info">info</button>
</div>
```

### Success color

```html
<div class="tooltip tooltip-open tooltip-success" data-tip="success">
  <button class="btn btn-success">success</button>
</div>
```

### Warning color

```html
<div class="tooltip tooltip-open tooltip-warning" data-tip="warning">
  <button class="btn btn-warning">warning</button>
</div>
```

### Error color

```html
<div class="tooltip tooltip-open tooltip-error" data-tip="error">
  <button class="btn btn-error">error</button>
</div>
```

### Responsive tooltip. only show for large screen

```html
<div class="lg:tooltip" data-tip="hello">
  <button class="btn">Hover me</button>
</div>
```

