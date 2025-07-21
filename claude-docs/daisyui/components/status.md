# Status

Status is a really small icon to visually show the current status of an element, like online, offline, error, etc.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| status | Component | Status icon |
| status-neutral | Color | neutral color |
| status-primary | Color | primary color |
| status-secondary | Color | secondary color |
| status-accent | Color | accent color |
| status-info | Color | info color |
| status-success | Color | success color |
| status-warning | Color | warning color |
| status-error | Color | error color |
| status-xs | Size | extra small size |
| status-sm | Size | small size |
| status-md | Size | medium size[Default] |
| status-lg | Size | large size |
| status-xl | Size | extra large size |

## HTML Examples

### Status

```html
<span class="status"></span>
```

### Status sizes

```html
<div aria-label="status" class="status status-xs"></div>
<div aria-label="status" class="status status-sm"></div>
<div aria-label="status" class="status status-md"></div>
<div aria-label="status" class="status status-lg"></div>
<div aria-label="status" class="status status-xl"></div>
```

### Status with colors

```html
<div aria-label="status" class="status status-primary"></div>
<div aria-label="status" class="status status-secondary"></div>
<div aria-label="status" class="status status-accent"></div>
<div aria-label="status" class="status status-neutral"></div>
<div aria-label="info" class="status status-info"></div>
<div aria-label="success" class="status status-success"></div>
<div aria-label="warning" class="status status-warning"></div>
<div aria-label="error" class="status status-error"></div>
```

### Status with ping animation

```html
<div class="inline-grid *:[grid-area:1/1]">
  <div class="status status-error animate-ping"></div>
  <div class="status status-error"></div>
</div> Server is down
```

### Status with bounce animation

```html
<div class="status status-info animate-bounce"></div> Unread messages
```

