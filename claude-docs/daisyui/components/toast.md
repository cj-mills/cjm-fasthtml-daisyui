# Toast

Toast is a wrapper to stack elements, positioned on the corner of page.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| toast | Component | Container element that sticks to the corner of page |
| toast-start | Placement | align horizontally to the left |
| toast-center | Placement | align horizontally to the center |
| toast-end | Placement | align horizontally to the right[Default] |
| toast-top | Placement | align vertically to top |
| toast-middle | Placement | align vertically to middle |
| toast-bottom | Placement | align vertically to bottom[Default] |

## HTML Examples

### toast with alert inside

```html
<div class="toast">
  <div class="alert alert-info">
    <span>New message arrived.</span>
  </div>
</div>
```

### toast-top toast-start

```html
<div class="toast toast-top toast-start">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-top toast-center

```html
<div class="toast toast-top toast-center">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-top toast-end

```html
<div class="toast toast-top toast-end">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-start toast-middle

```html
<div class="toast toast-start toast-middle">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-center toast-middle

```html
<div class="toast toast-center toast-middle">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-end toast-middle

```html
<div class="toast toast-end toast-middle">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-start toast-bottom (default)

```html
<div class="toast toast-start">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-center toast-bottom (default)

```html
<div class="toast toast-center">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

### toast-end (default) toast-bottom (default)

```html
<div class="toast toast-end">
  <div class="alert alert-info">
    <span>New mail arrived.</span>
  </div>
  <div class="alert alert-success">
    <span>Message sent successfully.</span>
  </div>
</div>
```

