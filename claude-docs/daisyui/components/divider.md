# Divider

Divider will be used to separate content vertically or horizontally.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| divider | Component | A divider line between two elements |
| divider-neutral | Color | neutral color |
| divider-primary | Color | primary color |
| divider-secondary | Color | secondary color |
| divider-accent | Color | accent color |
| divider-success | Color | success color |
| divider-warning | Color | warning color |
| divider-info | Color | info color |
| divider-error | Color | error color |
| divider-vertical | direction | Divide vertical elements (on top of each other)[Default] |
| divider-horizontal | direction | Divide horizontal elements (next to each other) |
| divider-start | Placement | Pushes the divider text to the start |
| divider-end | Placement | Pushes the divider text to the end |

## HTML Examples

### Divider

```html
<div class="flex w-full flex-col">
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
  <div class="divider">OR</div>
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
</div>
```

### Divider horizontal

```html
<div class="flex w-full">
  <div class="card bg-base-300 rounded-box grid h-20 grow place-items-center">content</div>
  <div class="divider divider-horizontal">OR</div>
  <div class="card bg-base-300 rounded-box grid h-20 grow place-items-center">content</div>
</div>
```

### Divider with no text

```html
<div class="flex w-full flex-col">
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
  <div class="divider"></div>
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
</div>
```

### responsive (lg:divider-horizontal)

```html
<div class="flex w-full flex-col lg:flex-row">
  <div class="card bg-base-300 rounded-box grid h-32 grow place-items-center">content</div>
  <div class="divider lg:divider-horizontal">OR</div>
  <div class="card bg-base-300 rounded-box grid h-32 grow place-items-center">content</div>
</div>
```

### Divider with colors

```html
<div class="flex w-full flex-col">
  <div class="divider">Default</div>
  <div class="divider divider-neutral">Neutral</div>
  <div class="divider divider-primary">Primary</div>
  <div class="divider divider-secondary">Secondary</div>
  <div class="divider divider-accent">Accent</div>
  <div class="divider divider-success">Success</div>
  <div class="divider divider-warning">Warning</div>
  <div class="divider divider-info">Info</div>
  <div class="divider divider-error">Error</div>
</div>
```

### Divider in different positions

```html
<div class="flex w-full flex-col">
  <div class="divider divider-start">Start</div>
  <div class="divider">Default</div>
  <div class="divider divider-end">End</div>
</div>
```

### Divider in different positions (horizontal)

```html
<div class="flex w-full">
  <div class="divider divider-horizontal divider-start">Start</div>
  <div class="divider divider-horizontal">Default</div>
  <div class="divider divider-horizontal divider-end">End</div>
</div>
```

