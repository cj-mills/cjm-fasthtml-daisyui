### Data display Indicator Components

1. ~~[Avatar](#avatar/)~~
2. ~~[Badge](#badge/)~~
3. ~~[Chat bubble](#chat-bubble/)~~
4. ~~[Countdown](#countdown/)~~
5. ~~[Diff](#diff/)~~
6. ~~[Kbd](#kbd/)~~
7. ~~[Stat](#stat/)~~
8. ~~[Status](#status/)~~



# Avatar

Avatars are used to show a thumbnail representation of an individual or business in the interface.

## Component Details

| Class name         | Type      |                                       |
| ------------------ | --------- | ------------------------------------- |
| avatar             | Component | Avatar                                |
| avatar-group       | Component | Container for multiple avatars        |
| avatar-online      | Modifier  | shows a green dot as online indicator |
| avatar-offline     | Modifier  | shows a gray dot as offline indicator |
| avatar-placeholder | Modifier  | To show letters as avatar placeholder |

## HTML Examples

### Avatar

```html
<div class="avatar">
  <div class="w-24 rounded">
    <img src="https://img.daisyui.com/images/profile/demo/batperson@192.webp" />
  </div>
</div>
```

### Avatar in custom sizes

```html
<div class="avatar">
  <div class="w-32 rounded">
    <img src="https://img.daisyui.com/images/profile/demo/superperson@192.webp" />
  </div>
</div>
<div class="avatar">
  <div class="w-20 rounded">
    <img
      src="https://img.daisyui.com/images/profile/demo/superperson@192.webp"
      alt="Tailwind-CSS-Avatar-component"
    />
  </div>
</div>
<div class="avatar">
  <div class="w-16 rounded">
    <img
      src="https://img.daisyui.com/images/profile/demo/superperson@192.webp"
      alt="Tailwind-CSS-Avatar-component"
    />
  </div>
</div>
<div class="avatar">
  <div class="w-8 rounded">
    <img
      src="https://img.daisyui.com/images/profile/demo/superperson@192.webp"
      alt="Tailwind-CSS-Avatar-component"
    />
  </div>
</div>
```

### Avatar rounded

```html
<div class="avatar">
  <div class="w-24 rounded-xl">
    <img src="https://img.daisyui.com/images/profile/demo/yellingwoman@192.webp" />
  </div>
</div>
<div class="avatar">
  <div class="w-24 rounded-full">
    <img src="https://img.daisyui.com/images/profile/demo/yellingcat@192.webp" />
  </div>
</div>
```

### Avatar with mask

```html
<div class="avatar">
  <div class="mask mask-heart w-24">
    <img src="https://img.daisyui.com/images/profile/demo/distracted3@192.webp" />
  </div>
</div>
<div class="avatar">
  <div class="mask mask-squircle w-24">
    <img src="https://img.daisyui.com/images/profile/demo/distracted1@192.webp" />
  </div>
</div>
<div class="avatar">
  <div class="mask mask-hexagon-2 w-24">
    <img src="https://img.daisyui.com/images/profile/demo/distracted2@192.webp" />
  </div>
</div>
```

### Avatar group

```html
<div class="avatar-group -space-x-6">
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/batperson@192.webp" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/spiderperson@192.webp" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/averagebulk@192.webp" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/wonderperson@192.webp" />
    </div>
  </div>
</div>
```

### Avatar group with counter

```html
<div class="avatar-group -space-x-6">
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/batperson@192.webp" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/spiderperson@192.webp" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/averagebulk@192.webp" />
    </div>
  </div>
  <div class="avatar avatar-placeholder">
    <div class="bg-neutral text-neutral-content w-12">
      <span>+99</span>
    </div>
  </div>
</div>
```

### Avatar with ring

```html
<div class="avatar">
  <div class="ring-primary ring-offset-base-100 w-24 rounded-full ring-2 ring-offset-2">
    <img src="https://img.daisyui.com/images/profile/demo/spiderperson@192.webp" />
  </div>
</div>
```

### Avatar with presence indicator

```html
<div class="avatar avatar-online">
  <div class="w-24 rounded-full">
    <img src="https://img.daisyui.com/images/profile/demo/gordon@192.webp" />
  </div>
</div>
<div class="avatar avatar-offline">
  <div class="w-24 rounded-full">
    <img src="https://img.daisyui.com/images/profile/demo/idiotsandwich@192.webp" />
  </div>
</div>
```

### Avatar placeholder

```html
<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-24 rounded-full">
    <span class="text-3xl">D</span>
  </div>
</div>
<div class="avatar avatar-online avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-16 rounded-full">
    <span class="text-xl">AI</span>
  </div>
</div>
<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-12 rounded-full">
    <span>SY</span>
  </div>
</div>
<div class="avatar avatar-placeholder">
  <div class="bg-neutral text-neutral-content w-8 rounded-full">
    <span class="text-xs">UI</span>
  </div>
</div>
```



# Badge

Badges are used to inform the user of the status of specific data.

## Component Details

| Class name      | Type      |                       |
| --------------- | --------- | --------------------- |
| badge           | Component | Container element     |
| badge-outline   | Style     | outline style         |
| badge-dash      | Style     | dash outline style    |
| badge-soft      | Style     | soft style            |
| badge-ghost     | Style     | ghost style           |
| badge-neutral   | Color     | neutral color         |
| badge-primary   | Color     | primary color         |
| badge-secondary | Color     | secondary color       |
| badge-accent    | Color     | accent color          |
| badge-info      | Color     | info color            |
| badge-success   | Color     | success color         |
| badge-warning   | Color     | warning color         |
| badge-error     | Color     | error color           |
| badge-xs        | Size      | extra small size      |
| badge-sm        | Size      | small size            |
| badge-md        | Size      | medium size (default) |
| badge-lg        | Size      | large size            |
| badge-xl        | Size      | extra large size      |

## HTML Examples

### Badge

```html
<span class="badge">Badge</span>
```

### Badge sizes

```html
<div class="badge badge-xs">Xsmall</div>
<div class="badge badge-sm">Small</div>
<div class="badge badge-md">Medium</div>
<div class="badge badge-lg">Large</div>
<div class="badge badge-xl">Xlarge</div>
```

### Badge with colors

```html
<div class="badge badge-primary">Primary</div>
<div class="badge badge-secondary">Secondary</div>
<div class="badge badge-accent">Accent</div>
<div class="badge badge-neutral">Neutral</div>
<div class="badge badge-info">Info</div>
<div class="badge badge-success">Success</div>
<div class="badge badge-warning">Warning</div>
<div class="badge badge-error">Error</div>
```

### Badge with soft style

```html
<div class="badge badge-soft badge-primary">Primary</div>
<div class="badge badge-soft badge-secondary">Secondary</div>
<div class="badge badge-soft badge-accent">Accent</div>
<div class="badge badge-soft badge-info">Info</div>
<div class="badge badge-soft badge-success">Success</div>
<div class="badge badge-soft badge-warning">Warning</div>
<div class="badge badge-soft badge-error">Error</div>
```

### Badge with outline style

```html
<div class="badge badge-outline badge-primary">Primary</div>
<div class="badge badge-outline badge-secondary">Secondary</div>
<div class="badge badge-outline badge-accent">Accent</div>
<div class="badge badge-outline badge-info">Info</div>
<div class="badge badge-outline badge-success">Success</div>
<div class="badge badge-outline badge-warning">Warning</div>
<div class="badge badge-outline badge-error">Error</div>
```

### Badge with dash style

```html
<div class="badge badge-dash badge-primary">Primary</div>
<div class="badge badge-dash badge-secondary">Secondary</div>
<div class="badge badge-dash badge-accent">Accent</div>
<div class="badge badge-dash badge-info">Info</div>
<div class="badge badge-dash badge-success">Success</div>
<div class="badge badge-dash badge-warning">Warning</div>
<div class="badge badge-dash badge-error">Error</div>
```

### neutral badge with outline or dash style

> These badges use dark text, only use them on light backgrounds

```html
<div class="bg-white p-6">
  <div class="badge badge-neutral badge-outline">Outline</div>
  <div class="badge badge-neutral badge-dash">Dash</div>
</div>
```

### Badge ghost

```html
<div class="badge badge-ghost">ghost</div>
```

### Empty badge

```html
<div class="badge badge-primary badge-lg"></div>
<div class="badge badge-primary badge-md"></div>
<div class="badge badge-primary badge-sm"></div>
<div class="badge badge-primary badge-xs"></div>
```

### Badge with icon

```html
<div class="badge badge-info">
  <svg class="size-[1em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g fill="currentColor" stroke-linejoin="miter" stroke-linecap="butt"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-linecap="square" stroke-miterlimit="10" stroke-width="2"></circle><path d="m12,17v-5.5c0-.276-.224-.5-.5-.5h-1.5" fill="none" stroke="currentColor" stroke-linecap="square" stroke-miterlimit="10" stroke-width="2"></path><circle cx="12" cy="7.25" r="1.25" fill="currentColor" stroke-width="2"></circle></g></svg>
  Info
</div>
<div class="badge badge-success">
  <svg class="size-[1em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g fill="currentColor" stroke-linejoin="miter" stroke-linecap="butt"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-linecap="square" stroke-miterlimit="10" stroke-width="2"></circle><polyline points="7 13 10 16 17 8" fill="none" stroke="currentColor" stroke-linecap="square" stroke-miterlimit="10" stroke-width="2"></polyline></g></svg>
  Success
</div>
<div class="badge badge-warning">
  <svg class="size-[1em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18"><g fill="currentColor"><path d="M7.638,3.495L2.213,12.891c-.605,1.048,.151,2.359,1.362,2.359H14.425c1.211,0,1.967-1.31,1.362-2.359L10.362,3.495c-.605-1.048-2.119-1.048-2.724,0Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><line x1="9" y1="6.5" x2="9" y2="10" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></line><path d="M9,13.569c-.552,0-1-.449-1-1s.448-1,1-1,1,.449,1,1-.448,1-1,1Z" fill="currentColor" data-stroke="none" stroke="none"></path></g></svg>
  Warning
</div>
<div class="badge badge-error">
  <svg class="size-[1em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g fill="currentColor"><rect x="1.972" y="11" width="20.056" height="2" transform="translate(-4.971 12) rotate(-45)" fill="currentColor" stroke-width="0"></rect><path d="m12,23c-6.065,0-11-4.935-11-11S5.935,1,12,1s11,4.935,11,11-4.935,11-11,11Zm0-20C7.038,3,3,7.037,3,12s4.038,9,9,9,9-4.037,9-9S16.962,3,12,3Z" stroke-width="0" fill="currentColor"></path></g></svg>
  Error
</div>
```

### Badge in a text

```html
<h1 class="text-xl font-semibold">
  Heading 1 <span class="badge badge-xl">Badge</span>
</h1>
<h2 class="text-lg font-semibold">
  Heading 2 <span class="badge badge-lg">Badge</span>
</h2>
<h3 class="text-base font-semibold">
  Heading 3 <span class="badge badge-md">Badge</span>
</h3>
<h4 class="text-sm font-semibold">
  Heading 4 <span class="badge badge-sm">Badge</span>
</h4>
<h5 class="text-xs font-semibold">
  Heading 5 <span class="badge badge-xs">Badge</span>
</h5>
<p class="text-xs">
  Paragraph <span class="badge badge-xs">Badge</span>
</p>
```

### Badge in a button

```html
<button class="btn">
  Inbox <div class="badge badge-sm">+99</div>
</button>
<button class="btn">
  Inbox <div class="badge badge-sm badge-secondary">+99</div>
</button>
```




# .Chat bubble

Chat bubbles are used to show one line of conversation and all its data, including the author image, author name, time, etc.

## Component Details

| Class name            | Type      |                                                     |
| --------------------- | --------- | --------------------------------------------------- |
| chat                  | Component | Container for one line of conversation and its data |
| chat-image            | Part      | Author image                                        |
| chat-header           | Part      | Text above the chat bubble                          |
| chat-footer           | Part      | Text below the chat bubble                          |
| chat-bubble           | Part      | Chat bubble                                         |
| chat-start            | Placement | Aligns chat to start horizontally (required)        |
| chat-end              | Placement | Aligns chat to end horizontally (required)          |
| chat-bubble-neutral   | Color     | neutral color for chat-bubble                       |
| chat-bubble-primary   | Color     | primary color for chat-bubble                       |
| chat-bubble-secondary | Color     | secondary color for chat-bubble                     |
| chat-bubble-accent    | Color     | accent color for chat-bubble                        |
| chat-bubble-info      | Color     | info color for chat-bubble                          |
| chat-bubble-success   | Color     | success color for chat-bubble                       |
| chat-bubble-warning   | Color     | warning color for chat-bubble                       |
| chat-bubble-error     | Color     | error color for chat-bubble                         |

## HTML Examples

### chat-start and chat-end

```html
<div class="chat chat-start">
  <div class="chat-bubble">
    It's over Anakin,
    <br />
    I have the high ground.
  </div>
</div>
<div class="chat chat-end">
  <div class="chat-bubble">You underestimate my power!</div>
</div>
```

### Chat with image

```html
<div class="chat chat-start">
  <div class="chat-image avatar">
    <div class="w-10 rounded-full">
      <img
        alt="Tailwind CSS chat bubble component"
        src="https://img.daisyui.com/images/profile/demo/kenobee@192.webp"
      />
    </div>
  </div>
  <div class="chat-bubble">It was said that you would, destroy the Sith, not join them.</div>
</div>
<div class="chat chat-start">
  <div class="chat-image avatar">
    <div class="w-10 rounded-full">
      <img
        alt="Tailwind CSS chat bubble component"
        src="https://img.daisyui.com/images/profile/demo/kenobee@192.webp"
      />
    </div>
  </div>
  <div class="chat-bubble">It was you who would bring balance to the Force</div>
</div>
<div class="chat chat-start">
  <div class="chat-image avatar">
    <div class="w-10 rounded-full">
      <img
        alt="Tailwind CSS chat bubble component"
        src="https://img.daisyui.com/images/profile/demo/kenobee@192.webp"
      />
    </div>
  </div>
  <div class="chat-bubble">Not leave it in Darkness</div>
</div>
```

### Chat with image, header and footer

```html
<div class="chat chat-start">
  <div class="chat-image avatar">
    <div class="w-10 rounded-full">
      <img
        alt="Tailwind CSS chat bubble component"
        src="https://img.daisyui.com/images/profile/demo/kenobee@192.webp"
      />
    </div>
  </div>
  <div class="chat-header">
    Obi-Wan Kenobi
    <time class="text-xs opacity-50">12:45</time>
  </div>
  <div class="chat-bubble">You were the Chosen One!</div>
  <div class="chat-footer opacity-50">Delivered</div>
</div>
<div class="chat chat-end">
  <div class="chat-image avatar">
    <div class="w-10 rounded-full">
      <img
        alt="Tailwind CSS chat bubble component"
        src="https://img.daisyui.com/images/profile/demo/anakeen@192.webp"
      />
    </div>
  </div>
  <div class="chat-header">
    Anakin
    <time class="text-xs opacity-50">12:46</time>
  </div>
  <div class="chat-bubble">I hate you!</div>
  <div class="chat-footer opacity-50">Seen at 12:46</div>
</div>
```

### Chat with header and footer

```html
<div class="chat chat-start">
  <div class="chat-header">
    Obi-Wan Kenobi
    <time class="text-xs opacity-50">2 hours ago</time>
  </div>
  <div class="chat-bubble">You were the Chosen One!</div>
  <div class="chat-footer opacity-50">Seen</div>
</div>
<div class="chat chat-start">
  <div class="chat-header">
    Obi-Wan Kenobi
    <time class="text-xs opacity-50">2 hour ago</time>
  </div>
  <div class="chat-bubble">I loved you.</div>
  <div class="chat-footer opacity-50">Delivered</div>
</div>
```

### Chat Bubble with colors

```html
<div class="chat chat-start">
  <div class="chat-bubble chat-bubble-primary">What kind of nonsense is this</div>
</div>
<div class="chat chat-start">
  <div class="chat-bubble chat-bubble-secondary">
    Put me on the Council and not make me a Master!??
  </div>
</div>
<div class="chat chat-start">
  <div class="chat-bubble chat-bubble-accent">
    That's never been done in the history of the Jedi.
  </div>
</div>
<div class="chat chat-start">
  <div class="chat-bubble chat-bubble-neutral">It's insulting!</div>
</div>
<div class="chat chat-end">
  <div class="chat-bubble chat-bubble-info">Calm down, Anakin.</div>
</div>
<div class="chat chat-end">
  <div class="chat-bubble chat-bubble-success">You have been given a great honor.</div>
</div>
<div class="chat chat-end">
  <div class="chat-bubble chat-bubble-warning">To be on the Council at your age.</div>
</div>
<div class="chat chat-end">
  <div class="chat-bubble chat-bubble-error">It's never happened before.</div>
</div>
```




# Countdown

Countdown gives you a transition effect when you change a number between 0 to 99.

## Component Details

| Class name | Type      |                   |
| ---------- | --------- | ----------------- |
| countdown  | Component | Countdown wrapper |

## HTML Examples

> Note: you need to change the span text and the `--value` CSS variable using JS. Value must be a number between 0 and 99.

### Countdown

```html
<span class="countdown">
  <span style="--value:59;" aria-live="polite" aria-label="59">59</span>
</span>
```

### Large text

```html
<span class="countdown font-mono text-6xl">
  <span style="--value:59;" aria-live="polite" aria-label="59">59</span>
</span>
```

### Clock countdown

```html
<span class="countdown font-mono text-2xl">
  <span style="--value:10;" aria-live="polite" aria-label="10">10</span>
  h
  <span style="--value:24;" aria-live="polite" aria-label="24">24</span>
  m
  <span style="--value:59;" aria-live="polite" aria-label="59">59</span>
  s
</span>
```

### Clock countdown with colons

```html
<span class="countdown font-mono text-2xl">
  <span style="--value:10;" aria-live="polite" aria-label="10">10</span>
  :
  <span style="--value:24;" aria-live="polite" aria-label="24">24</span>
  :
  <span style="--value:59;" aria-live="polite" aria-label="59">59</span>
</span>
```

### Large text with labels

```html
<div class="flex gap-5">
  <div>
    <span class="countdown font-mono text-4xl">
      <span style="--value:15;" aria-live="polite" aria-label="15">15</span>
    </span>
    days
  </div>
  <div>
    <span class="countdown font-mono text-4xl">
      <span style="--value:10;" aria-live="polite" aria-label="10">10</span>
    </span>
    hours
  </div>
  <div>
    <span class="countdown font-mono text-4xl">
      <span style="--value:24;" aria-live="polite" aria-label="24">24</span>
    </span>
    min
  </div>
  <div>
    <span class="countdown font-mono text-4xl">
      <span style="--value:59;" aria-live="polite" aria-label="59">59</span>
    </span>
    sec
  </div>
</div>
```

### Large text with labels under

```html
<div class="grid auto-cols-max grid-flow-col gap-5 text-center">
  <div class="flex flex-col">
    <span class="countdown font-mono text-5xl">
      <span style="--value:15;" aria-live="polite" aria-label="15">15</span>
    </span>
    days
  </div>
  <div class="flex flex-col">
    <span class="countdown font-mono text-5xl">
      <span style="--value:10;" aria-live="polite" aria-label="10">10</span>
    </span>
    hours
  </div>
  <div class="flex flex-col">
    <span class="countdown font-mono text-5xl">
      <span style="--value:24;" aria-live="polite" aria-label="24">24</span>
    </span>
    min
  </div>
  <div class="flex flex-col">
    <span class="countdown font-mono text-5xl">
      <span style="--value:59;" aria-live="polite" aria-label="59">59</span>
    </span>
    sec
  </div>
</div>
```

### In boxes

```html
<div class="grid auto-cols-max grid-flow-col gap-5 text-center">
  <div class="bg-neutral rounded-box text-neutral-content flex flex-col p-2">
    <span class="countdown font-mono text-5xl">
      <span style="--value:15;" aria-live="polite" aria-label="15">15</span>
    </span>
    days
  </div>
  <div class="bg-neutral rounded-box text-neutral-content flex flex-col p-2">
    <span class="countdown font-mono text-5xl">
      <span style="--value:10;" aria-live="polite" aria-label="10">10</span>
    </span>
    hours
  </div>
  <div class="bg-neutral rounded-box text-neutral-content flex flex-col p-2">
    <span class="countdown font-mono text-5xl">
      <span style="--value:24;" aria-live="polite" aria-label="24">24</span>
    </span>
    min
  </div>
  <div class="bg-neutral rounded-box text-neutral-content flex flex-col p-2">
    <span class="countdown font-mono text-5xl">
      <span style="--value:59;" aria-live="polite" aria-label="59">59</span>
    </span>
    sec
  </div>
</div>
```





# Diff

Diff component shows a side-by-side comparison of two items.

## Component Details

| Class name   | Type      |                     |
| ------------ | --------- | ------------------- |
| diff         | Component | Container element   |
| diff-item-1  | Part      | First item          |
| diff-item-2  | Part      | Second item         |
| diff-resizer | Part      | The resizer control |

## HTML Examples

### Diff

```html
<figure class="diff aspect-16/9" tabindex="0">
  <div class="diff-item-1" role="img" tabindex="0">
    <img alt="daisy" src="https://img.daisyui.com/images/stock/photo-1560717789-0ac7c58ac90a.webp" />
  </div>
  <div class="diff-item-2" role="img">
    <img
      alt="daisy"
      src="https://img.daisyui.com/images/stock/photo-1560717789-0ac7c58ac90a-blur.webp" />
  </div>
  <div class="diff-resizer"></div>
</figure>
```

### Diff text

```html
<figure class="diff aspect-16/9" tabindex="0">
  <div class="diff-item-1" role="img" tabindex="0">
    <div class="bg-primary text-primary-content grid place-content-center text-9xl font-black">
      DAISY
    </div>
  </div>
  <div class="diff-item-2" role="img">
    <div class="bg-base-200 grid place-content-center text-9xl font-black">DAISY</div>
  </div>
  <div class="diff-resizer"></div>
</figure>
```





# Kbd

Kbd is used to display keyboard shortcuts.

## Component Details

| Class name | Type      |                                          |
| ---------- | --------- | ---------------------------------------- |
| kbd        | Component | Do show a keyboard key or a shortcut key |
| kbd-xs     | Size      | Extra small size                         |
| kbd-sm     | Size      | Small size                               |
| kbd-md     | Size      | Medium size[Default]                     |
| kbd-lg     | Size      | Large size                               |
| kbd-xl     | Size      | Extra large size                         |

## HTML Examples

### Kbd

```html
<kbd class="kbd">K</kbd>
```

### Kbd sizes

```html
<kbd class="kbd kbd-xs">Xsmall</kbd>
<kbd class="kbd kbd-sm">Small</kbd>
<kbd class="kbd kbd-md">Medium</kbd>
<kbd class="kbd kbd-lg">Large</kbd>
<kbd class="kbd kbd-xl">Xlarge</kbd>
```

### In text

```html
Press
<kbd class="kbd kbd-sm">F</kbd>
to pay respects.
```

### Key combination

```html
<kbd class="kbd">ctrl</kbd>
+
<kbd class="kbd">shift</kbd>
+
<kbd class="kbd">del</kbd>
```

### Function Keys

```html
<kbd class="kbd">⌘</kbd>
<kbd class="kbd">⌥</kbd>
<kbd class="kbd">⇧</kbd>
<kbd class="kbd">⌃</kbd>
```

### A full keyboard

```html
<div class="my-1 flex w-full justify-center gap-1">
  <kbd class="kbd">q</kbd>
  <kbd class="kbd">w</kbd>
  <kbd class="kbd">e</kbd>
  <kbd class="kbd">r</kbd>
  <kbd class="kbd">t</kbd>
  <kbd class="kbd">y</kbd>
  <kbd class="kbd">u</kbd>
  <kbd class="kbd">i</kbd>
  <kbd class="kbd">o</kbd>
  <kbd class="kbd">p</kbd>
</div>
<div class="my-1 flex w-full justify-center gap-1">
  <kbd class="kbd">a</kbd>
  <kbd class="kbd">s</kbd>
  <kbd class="kbd">d</kbd>
  <kbd class="kbd">f</kbd>
  <kbd class="kbd">g</kbd>
  <kbd class="kbd">h</kbd>
  <kbd class="kbd">j</kbd>
  <kbd class="kbd">k</kbd>
  <kbd class="kbd">l</kbd>
</div>
<div class="my-1 flex w-full justify-center gap-1">
  <kbd class="kbd">z</kbd>
  <kbd class="kbd">x</kbd>
  <kbd class="kbd">c</kbd>
  <kbd class="kbd">v</kbd>
  <kbd class="kbd">b</kbd>
  <kbd class="kbd">n</kbd>
  <kbd class="kbd">m</kbd>
  <kbd class="kbd">/</kbd>
</div>
```

### Arrow Keys

```html
<div class="flex w-full justify-center">
  <kbd class="kbd">▲</kbd>
</div>
<div class="flex w-full justify-center gap-12">
  <kbd class="kbd">◀︎</kbd>
  <kbd class="kbd">▶︎</kbd>
</div>
<div class="flex w-full justify-center">
  <kbd class="kbd">▼</kbd>
</div>
```







# Stat

Stat is used to show numbers and data in a block.

## Component Details

| Class name       | Type      |                                            |
| ---------------- | --------- | ------------------------------------------ |
| stats            | Component | Container of multiple stat items           |
| stat             | Part      | A block to display stat data about a topic |
| stat-title       | Part      | Title part                                 |
| stat-value       | Part      | Value part                                 |
| stat-desc        | Part      | Description part                           |
| stat-figure      | Part      | Figure part for icon, etc                  |
| stat-actions     | Part      | Actions part for button, etc               |
| stats-horizontal | direction | Makes stats horizontal (default)           |
| stats-vertical   | direction | Makes stats vertical                       |

## HTML Examples

### Stat

```html
<div class="stats shadow">
  <div class="stat">
    <div class="stat-title">Total Page Views</div>
    <div class="stat-value">89,400</div>
    <div class="stat-desc">21% more than last month</div>
  </div>
</div>
```

### Stat with icons or image

```html
<div class="stats shadow">
  <div class="stat">
    <div class="stat-figure text-primary">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        class="inline-block h-8 w-8 stroke-current"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
        ></path>
      </svg>
    </div>
    <div class="stat-title">Total Likes</div>
    <div class="stat-value text-primary">25.6K</div>
    <div class="stat-desc">21% more than last month</div>
  </div>

  <div class="stat">
    <div class="stat-figure text-secondary">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        class="inline-block h-8 w-8 stroke-current"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M13 10V3L4 14h7v7l9-11h-7z"
        ></path>
      </svg>
    </div>
    <div class="stat-title">Page Views</div>
    <div class="stat-value text-secondary">2.6M</div>
    <div class="stat-desc">21% more than last month</div>
  </div>

  <div class="stat">
    <div class="stat-figure text-secondary">
      <div class="avatar avatar-online">
        <div class="w-16 rounded-full">
          <img src="https://img.daisyui.com/images/profile/demo/anakeen@192.webp" />
        </div>
      </div>
    </div>
    <div class="stat-value">86%</div>
    <div class="stat-title">Tasks done</div>
    <div class="stat-desc text-secondary">31 tasks remaining</div>
  </div>
</div>
```

### Stat

```html
<div class="stats shadow">
  <div class="stat">
    <div class="stat-figure text-secondary">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        class="inline-block h-8 w-8 stroke-current"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
        ></path>
      </svg>
    </div>
    <div class="stat-title">Downloads</div>
    <div class="stat-value">31K</div>
    <div class="stat-desc">Jan 1st - Feb 1st</div>
  </div>

  <div class="stat">
    <div class="stat-figure text-secondary">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        class="inline-block h-8 w-8 stroke-current"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
        ></path>
      </svg>
    </div>
    <div class="stat-title">New Users</div>
    <div class="stat-value">4,200</div>
    <div class="stat-desc">↗︎ 400 (22%)</div>
  </div>

  <div class="stat">
    <div class="stat-figure text-secondary">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        class="inline-block h-8 w-8 stroke-current"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"
        ></path>
      </svg>
    </div>
    <div class="stat-title">New Registers</div>
    <div class="stat-value">1,200</div>
    <div class="stat-desc">↘︎ 90 (14%)</div>
  </div>
</div>
```

### Centered items

```html
<div class="stats shadow">
  <div class="stat place-items-center">
    <div class="stat-title">Downloads</div>
    <div class="stat-value">31K</div>
    <div class="stat-desc">From January 1st to February 1st</div>
  </div>

  <div class="stat place-items-center">
    <div class="stat-title">Users</div>
    <div class="stat-value text-secondary">4,200</div>
    <div class="stat-desc text-secondary">↗︎ 40 (2%)</div>
  </div>

  <div class="stat place-items-center">
    <div class="stat-title">New Registers</div>
    <div class="stat-value">1,200</div>
    <div class="stat-desc">↘︎ 90 (14%)</div>
  </div>
</div>
```

### Vertical

```html
<div class="stats stats-vertical shadow">
  <div class="stat">
    <div class="stat-title">Downloads</div>
    <div class="stat-value">31K</div>
    <div class="stat-desc">Jan 1st - Feb 1st</div>
  </div>

  <div class="stat">
    <div class="stat-title">New Users</div>
    <div class="stat-value">4,200</div>
    <div class="stat-desc">↗︎ 400 (22%)</div>
  </div>

  <div class="stat">
    <div class="stat-title">New Registers</div>
    <div class="stat-value">1,200</div>
    <div class="stat-desc">↘︎ 90 (14%)</div>
  </div>
</div>
```

### Responsive (vertical on small screen, horizontal on large screen)

```html
<div class="stats stats-vertical lg:stats-horizontal shadow">
  <div class="stat">
    <div class="stat-title">Downloads</div>
    <div class="stat-value">31K</div>
    <div class="stat-desc">Jan 1st - Feb 1st</div>
  </div>

  <div class="stat">
    <div class="stat-title">New Users</div>
    <div class="stat-value">4,200</div>
    <div class="stat-desc">↗︎ 400 (22%)</div>
  </div>

  <div class="stat">
    <div class="stat-title">New Registers</div>
    <div class="stat-value">1,200</div>
    <div class="stat-desc">↘︎ 90 (14%)</div>
  </div>
</div>
```

### With custom colors and button

```html
<div class="stats bg-base-100 border-base-300 border">
  <div class="stat">
    <div class="stat-title">Account balance</div>
    <div class="stat-value">$89,400</div>
    <div class="stat-actions">
      <button class="btn btn-xs btn-success">Add funds</button>
    </div>
  </div>

  <div class="stat">
    <div class="stat-title">Current balance</div>
    <div class="stat-value">$89,400</div>
    <div class="stat-actions">
      <button class="btn btn-xs">Withdrawal</button>
      <button class="btn btn-xs">Deposit</button>
    </div>
  </div>
</div>
```





# Status

Status is a really small icon to visually show the current status of an element, like online, offline, error, etc.

## Component Details

| Class name       | Type      |                      |
| ---------------- | --------- | -------------------- |
| status           | Component | Status icon          |
| status-neutral   | Color     | neutral color        |
| status-primary   | Color     | primary color        |
| status-secondary | Color     | secondary color      |
| status-accent    | Color     | accent color         |
| status-info      | Color     | info color           |
| status-success   | Color     | success color        |
| status-warning   | Color     | warning color        |
| status-error     | Color     | error color          |
| status-xs        | Size      | extra small size     |
| status-sm        | Size      | small size           |
| status-md        | Size      | medium size[Default] |
| status-lg        | Size      | large size           |
| status-xl        | Size      | extra large size     |

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

