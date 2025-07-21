# Steps

Steps can be used to show a list of steps in a process.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| steps | Component | Container of multiple step nodes |
| step | Part | A single step node |
| step-icon | Part | For custom icon inside step |
| step-neutral | Color | neutral color |
| step-primary | Color | primary color |
| step-secondary | Color | secondary color |
| step-accent | Color | accent color |
| step-info | Color | info color |
| step-success | Color | success color |
| step-warning | Color | warning color |
| step-error | Color | error color |
| steps-vertical | direction | Makes steps vertical (default) |
| steps-horizontal | direction | Makes steps horizontal |

## HTML Examples

### Horizontal

```html
<ul class="steps">
  <li class="step step-primary">Register</li>
  <li class="step step-primary">Choose plan</li>
  <li class="step">Purchase</li>
  <li class="step">Receive Product</li>
</ul>
```

### Vertical

```html
<ul class="steps steps-vertical">
  <li class="step step-primary">Register</li>
  <li class="step step-primary">Choose plan</li>
  <li class="step">Purchase</li>
  <li class="step">Receive Product</li>
</ul>
```

### responsive (vertical on small screen, horizontal on large screen)

```html
<ul class="steps steps-vertical lg:steps-horizontal">
  <li class="step step-primary">Register</li>
  <li class="step step-primary">Choose plan</li>
  <li class="step">Purchase</li>
  <li class="step">Receive Product</li>
</ul>
```

### With custom content in step-icon

```html
<ul class="steps">
  <li class="step step-neutral">
    <span class="step-icon">😕</span>Step 1
  </li>
  <li class="step step-neutral">
    <span class="step-icon">😃</span>Step 2
  </li>
  <li class="step">
    <span class="step-icon">😍</span>Step 3
  </li>
</ul>
```

### With data-content

```html
<ul class="steps">
  <li data-content="?" class="step step-neutral">Step 1</li>
  <li data-content="!" class="step step-neutral">Step 2</li>
  <li data-content="✓" class="step step-neutral">Step 3</li>
  <li data-content="✕" class="step step-neutral">Step 4</li>
  <li data-content="★" class="step step-neutral">Step 5</li>
  <li data-content="" class="step step-neutral">Step 6</li>
  <li data-content="●" class="step step-neutral">Step 7</li>
</ul>
```

### Custom colors

```html
<ul class="steps">
  <li class="step step-info">Fly to moon</li>
  <li class="step step-info">Shrink the moon</li>
  <li class="step step-info">Grab the moon</li>
  <li class="step step-error" data-content="?">Sit on toilet</li>
</ul>
```

### With scrollable wrapper

```html
<div class="overflow-x-auto">
  <ul class="steps">
    <li class="step">start</li>
    <li class="step step-secondary">2</li>
    <li class="step step-secondary">3</li>
    <li class="step step-secondary">4</li>
    <li class="step">5</li>
    <li class="step step-accent">6</li>
    <li class="step step-accent">7</li>
    <li class="step">8</li>
    <li class="step step-error">9</li>
    <li class="step step-error">10</li>
    <li class="step">11</li>
    <li class="step">12</li>
    <li class="step step-warning">13</li>
    <li class="step step-warning">14</li>
    <li class="step">15</li>
    <li class="step step-neutral">16</li>
    <li class="step step-neutral">17</li>
    <li class="step step-neutral">18</li>
    <li class="step step-neutral">19</li>
    <li class="step step-neutral">20</li>
    <li class="step step-neutral">21</li>
    <li class="step step-neutral">22</li>
    <li class="step step-neutral">23</li>
    <li class="step step-neutral">end</li>
  </ul>
</div>
```

