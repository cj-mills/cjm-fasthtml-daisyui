### Feedback

1. [Alert](#alert/)
2. [Loading](#loading/)
3. [Progress](#progress/)
4. [Radial progress](#radial-progress/)
5. [Skeleton](#skeleton/)
6. [Toast](#toast/)
7. [Tooltip](#tooltip/)





# Alert

Alert informs users about important events.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| alert | Component | Container element |
| alert-outline | Style | outline style |
| alert-dash | Style | dash outline style |
| alert-soft | Style | soft style |
| alert-info | Color | info color |
| alert-success | Color | success color |
| alert-warning | Color | warning color |
| alert-error | Color | error color |
| alert-vertical | direction | Vertical layout, good for mobile |
| alert-horizontal | direction | Horizontal layout, good for desktop |

## HTML Examples

### Alert

```html
<div role="alert" class="alert">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-info h-6 w-6 shrink-0">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
  </svg>
  <span>12 unread messages. Tap to see.</span>
</div>
```

### Info color

```html
<div role="alert" class="alert alert-info">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="h-6 w-6 shrink-0 stroke-current">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
  </svg>
  <span>New software update available.</span>
</div>
```

### Success color

```html
<div role="alert" class="alert alert-success">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
  </svg>
  <span>Your purchase has been confirmed!</span>
</div>
```

### Warning color

```html
<div role="alert" class="alert alert-warning">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
  </svg>
  <span>Warning: Invalid email address!</span>
</div>
```

### Error color

```html
<div role="alert" class="alert alert-error">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
  </svg>
  <span>Error! Task failed successfully.</span>
</div>
```

### Alert soft style

```html
<div role="alert" class="alert alert-info alert-soft">
  <span>12 unread messages. Tap to see.</span>
</div>
<div role="alert" class="alert alert-success alert-soft">
  <span>Your purchase has been confirmed!</span>
</div>
<div role="alert" class="alert alert-warning alert-soft">
  <span>Warning: Invalid email address!</span>
</div>
<div role="alert" class="alert alert-error alert-soft">
  <span>Error! Task failed successfully.</span>
</div>
```

### Alert outline style

```html
<div role="alert" class="alert alert-info alert-outline">
  <span>12 unread messages. Tap to see.</span>
</div>
<div role="alert" class="alert alert-success alert-outline">
  <span>Your purchase has been confirmed!</span>
</div>
<div role="alert" class="alert alert-warning alert-outline">
  <span>Warning: Invalid email address!</span>
</div>
<div role="alert" class="alert alert-error alert-outline">
  <span>Error! Task failed successfully.</span>
</div>
```

### Alert dash style

```html
<div role="alert" class="alert alert-info alert-dash">
  <span>12 unread messages. Tap to see.</span>
</div>
<div role="alert" class="alert alert-success alert-dash">
  <span>Your purchase has been confirmed!</span>
</div>
<div role="alert" class="alert alert-warning alert-dash">
  <span>Warning: Invalid email address!</span>
</div>
<div role="alert" class="alert alert-error alert-dash">
  <span>Error! Task failed successfully.</span>
</div>
```

### Alert with buttons + responsive

```html
<div role="alert" class="alert alert-vertical sm:alert-horizontal">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-info h-6 w-6 shrink-0">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
  </svg>
  <span>we use cookies for no reason.</span>
  <div>
    <button class="btn btn-sm">Deny</button>
    <button class="btn btn-sm btn-primary">Accept</button>
  </div>
</div>
```

### Alert with title and description

```html
<div role="alert" class="alert alert-vertical sm:alert-horizontal">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-info h-6 w-6 shrink-0">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
  </svg>
  <div>
    <h3 class="font-bold">New message!</h3>
    <div class="text-xs">You have 1 unread message</div>
  </div>
  <button class="btn btn-sm">See</button>
</div>
```





---



# Loading

Loading shows an animation to indicate that something is loading.

## Component Details

| Class name       | Type      |                      |
| ---------------- | --------- | -------------------- |
| loading          | Component | Loading element      |
| loading-spinner  | Style     | spinner animation    |
| loading-dots     | Style     | dots animation       |
| loading-ring     | Style     | ring animation       |
| loading-ball     | Style     | ball animation       |
| loading-bars     | Style     | bars animation       |
| loading-infinity | Style     | infinity animation   |
| loading-xs       | Size      | Extra small size     |
| loading-sm       | Size      | Small size           |
| loading-md       | Size      | Medium size[Default] |
| loading-lg       | Size      | Large size           |
| loading-xl       | Size      | Extra large size     |

## HTML Examples

### Loading spinner

```html
<span class="loading loading-spinner loading-xs"></span>
<span class="loading loading-spinner loading-sm"></span>
<span class="loading loading-spinner loading-md"></span>
<span class="loading loading-spinner loading-lg"></span>
<span class="loading loading-spinner loading-xl"></span>
```

### Loading dots

```html
<span class="loading loading-dots loading-xs"></span>
<span class="loading loading-dots loading-sm"></span>
<span class="loading loading-dots loading-md"></span>
<span class="loading loading-dots loading-lg"></span>
<span class="loading loading-dots loading-xl"></span>
```

### Loading ring

```html
<span class="loading loading-ring loading-xs"></span>
<span class="loading loading-ring loading-sm"></span>
<span class="loading loading-ring loading-md"></span>
<span class="loading loading-ring loading-lg"></span>
<span class="loading loading-ring loading-xl"></span>
```

### Loading ball

```html
<span class="loading loading-ball loading-xs"></span>
<span class="loading loading-ball loading-sm"></span>
<span class="loading loading-ball loading-md"></span>
<span class="loading loading-ball loading-lg"></span>
<span class="loading loading-ball loading-xl"></span>
```

### Loading bars

```html
<span class="loading loading-bars loading-xs"></span>
<span class="loading loading-bars loading-sm"></span>
<span class="loading loading-bars loading-md"></span>
<span class="loading loading-bars loading-lg"></span>
<span class="loading loading-bars loading-xl"></span>
```

### Loading infinity

```html
<span class="loading loading-infinity loading-xs"></span>
<span class="loading loading-infinity loading-sm"></span>
<span class="loading loading-infinity loading-md"></span>
<span class="loading loading-infinity loading-lg"></span>
<span class="loading loading-infinity loading-xl"></span>
```

### Loading with colors

```html
<span class="loading loading-spinner text-primary"></span>
<span class="loading loading-spinner text-secondary"></span>
<span class="loading loading-spinner text-accent"></span>
<span class="loading loading-spinner text-neutral"></span>
<span class="loading loading-spinner text-info"></span>
<span class="loading loading-spinner text-success"></span>
<span class="loading loading-spinner text-warning"></span>
<span class="loading loading-spinner text-error"></span>
```





---



# Progress

Progress bar can be used to show the progress of a task or to show the passing of time.

## Component Details

| Class name         | Type      |                    |
| ------------------ | --------- | ------------------ |
| progress           | Component | For <progress> tag |
| progress-neutral   | Color     | neutral color      |
| progress-primary   | Color     | primary color      |
| progress-secondary | Color     | secondary color    |
| progress-accent    | Color     | accent color       |
| progress-info      | Color     | info color         |
| progress-success   | Color     | success color      |
| progress-warning   | Color     | warning color      |
| progress-error     | Color     | error color        |

## HTML Examples

### Progress

```html
<progress class="progress w-56" value="0" max="100"></progress>
<progress class="progress w-56" value="10" max="100"></progress>
<progress class="progress w-56" value="40" max="100"></progress>
<progress class="progress w-56" value="70" max="100"></progress>
<progress class="progress w-56" value="100" max="100"></progress>
```

### Primary color

```html
<progress class="progress progress-primary w-56" value="0" max="100"></progress>
<progress class="progress progress-primary w-56" value="10" max="100"></progress>
<progress class="progress progress-primary w-56" value="40" max="100"></progress>
<progress class="progress progress-primary w-56" value="70" max="100"></progress>
<progress class="progress progress-primary w-56" value="100" max="100"></progress>
```

### Secondary color

```html
<progress class="progress progress-secondary w-56" value="0" max="100"></progress>
<progress class="progress progress-secondary w-56" value="10" max="100"></progress>
<progress class="progress progress-secondary w-56" value="40" max="100"></progress>
<progress class="progress progress-secondary w-56" value="70" max="100"></progress>
<progress class="progress progress-secondary w-56" value="100" max="100"></progress>
```

### Accent color

```html
<progress class="progress progress-accent w-56" value="0" max="100"></progress>
<progress class="progress progress-accent w-56" value="10" max="100"></progress>
<progress class="progress progress-accent w-56" value="40" max="100"></progress>
<progress class="progress progress-accent w-56" value="70" max="100"></progress>
<progress class="progress progress-accent w-56" value="100" max="100"></progress>
```

### Neutral color

```html
<progress class="progress progress-neutral w-56" value="0" max="100"></progress>
<progress class="progress progress-neutral w-56" value="10" max="100"></progress>
<progress class="progress progress-neutral w-56" value="40" max="100"></progress>
<progress class="progress progress-neutral w-56" value="70" max="100"></progress>
<progress class="progress progress-neutral w-56" value="100" max="100"></progress>
```

### Info color

```html
<progress class="progress progress-info w-56" value="0" max="100"></progress>
<progress class="progress progress-info w-56" value="10" max="100"></progress>
<progress class="progress progress-info w-56" value="40" max="100"></progress>
<progress class="progress progress-info w-56" value="70" max="100"></progress>
<progress class="progress progress-info w-56" value="100" max="100"></progress>
```

### Success color

```html
<progress class="progress progress-success w-56" value="0" max="100"></progress>
<progress class="progress progress-success w-56" value="10" max="100"></progress>
<progress class="progress progress-success w-56" value="40" max="100"></progress>
<progress class="progress progress-success w-56" value="70" max="100"></progress>
<progress class="progress progress-success w-56" value="100" max="100"></progress>
```

### Warning color

```html
<progress class="progress progress-warning w-56" value="0" max="100"></progress>
<progress class="progress progress-warning w-56" value="10" max="100"></progress>
<progress class="progress progress-warning w-56" value="40" max="100"></progress>
<progress class="progress progress-warning w-56" value="70" max="100"></progress>
<progress class="progress progress-warning w-56" value="100" max="100"></progress>
```

### Error color

```html
<progress class="progress progress-error w-56" value="0" max="100"></progress>
<progress class="progress progress-error w-56" value="10" max="100"></progress>
<progress class="progress progress-error w-56" value="40" max="100"></progress>
<progress class="progress progress-error w-56" value="70" max="100"></progress>
<progress class="progress progress-error w-56" value="100" max="100"></progress>
```

### Indeterminate (without value)

```html
<progress class="progress w-56"></progress>
```





----



# Radial progress

Radial progress can be used to show the progress of a task or to show the passing of time.

## Component Details

| Class name      | Type      |                         |
| --------------- | --------- | ----------------------- |
| radial-progress | Component | Shows a radial progress |

## HTML Examples

### Radial progress

```html
<div class="radial-progress" style="--value:70;" aria-valuenow="70" role="progressbar">70%</div>
```

### Different values

```html
<div class="radial-progress" style="--value:0;" aria-valuenow="0" role="progressbar">0%</div>
<div class="radial-progress" style="--value:20;" aria-valuenow="20" role="progressbar">20%</div>
<div class="radial-progress" style="--value:60;" aria-valuenow="60" role="progressbar">60%</div>
<div class="radial-progress" style="--value:80;" aria-valuenow="80" role="progressbar">80%</div>
<div class="radial-progress" style="--value:100;" aria-valuenow="100" role="progressbar">100%</div>
```

### Custom color

```html
<div class="radial-progress text-primary" style="--value:70;" aria-valuenow="70" role="progressbar">70%</div>
```

### With background color and border

```html
<div
  class="radial-progress bg-primary text-primary-content border-primary border-4"
  style="--value:70;" aria-valuenow="70" role="progressbar">
  70%
</div>
```

### Custom size and custom thickness

```html
<div class="radial-progress" style="--value:70; --size:12rem; --thickness: 2px;" aria-valuenow="70" role="progressbar">70%</div>
<div class="radial-progress" style="--value:70; --size:12rem; --thickness: 2rem;" aria-valuenow="70" role="progressbar">70%</div>
```





---



# Skeleton

Skeleton is a component that can be used to show a loading state of a component.

## Component Details

| Class name | Type      |                                          |
| ---------- | --------- | ---------------------------------------- |
| skeleton   | Component | A placeholder div with loading animation |

## HTML Examples

### Skeleton

```html
<div class="skeleton h-32 w-32"></div>
```

### Skeleton - circle with content

```html
<div class="flex w-52 flex-col gap-4">
  <div class="flex items-center gap-4">
    <div class="skeleton h-16 w-16 shrink-0 rounded-full"></div>
    <div class="flex flex-col gap-4">
      <div class="skeleton h-4 w-20"></div>
      <div class="skeleton h-4 w-28"></div>
    </div>
  </div>
  <div class="skeleton h-32 w-full"></div>
</div>
```

### Skeleton - rectangle with content

```html
<div class="flex w-52 flex-col gap-4">
  <div class="skeleton h-32 w-full"></div>
  <div class="skeleton h-4 w-28"></div>
  <div class="skeleton h-4 w-full"></div>
  <div class="skeleton h-4 w-full"></div>
</div>
```





---



# Toast

Toast is a wrapper to stack elements, positioned on the corner of page.

## Component Details

| Class name   | Type      |                                                     |
| ------------ | --------- | --------------------------------------------------- |
| toast        | Component | Container element that sticks to the corner of page |
| toast-start  | Placement | align horizontally to the left                      |
| toast-center | Placement | align horizontally to the center                    |
| toast-end    | Placement | align horizontally to the right[Default]            |
| toast-top    | Placement | align vertically to top                             |
| toast-middle | Placement | align vertically to middle                          |
| toast-bottom | Placement | align vertically to bottom[Default]                 |

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





---



# Tooltip

Tooltip can be used to show a message when hovering over an element.

## Component Details

| Class name        | Type      |                                                              |
| ----------------- | --------- | ------------------------------------------------------------ |
| tooltip           | Component | Container element                                            |
| tooltip-content   | Part      | Optional. Setting a div as the content of the tooltip instead of the `data-tip` text |
| tooltip-top       | Placement | Put tooltip on top[Default]                                  |
| tooltip-bottom    | Placement | Put tooltip on bottom                                        |
| tooltip-left      | Placement | Put tooltip on left                                          |
| tooltip-right     | Placement | Put tooltip on right                                         |
| tooltip-open      | Modifier  | Force open tooltip                                           |
| tooltip-neutral   | Color     | neutral color                                                |
| tooltip-primary   | Color     | primary color                                                |
| tooltip-secondary | Color     | secondary color                                              |
| tooltip-accent    | Color     | accent color                                                 |
| tooltip-info      | Color     | info color                                                   |
| tooltip-success   | Color     | success color                                                |
| tooltip-warning   | Color     | warning color                                                |
| tooltip-error     | Color     | error color                                                  |

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

