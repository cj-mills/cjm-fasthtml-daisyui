### Data display Components

1. [Accordion](#accordion/)
2. [Avatar](#avatar/)
3. [Badge](#badge/)
4. [Card](#card/)
5. [Carousel](#carousel/)
6. [Chat bubble](#chat-bubble/)
7. [Collapse](#collapse/)
8. [Countdown](#countdown/)
9. [Diff](#diff/)
10. [Kbd](#kbd/)
11. [List](#list/)
12. [Stat](#stat/)
13. [Status](#status/)
14. [Table](#table/)
15. [Timeline](#timeline/)



# Chat bubble

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
        src="https://img.daisyui.com/images/profile/demo/[email protected]"
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
        src="https://img.daisyui.com/images/profile/demo/[email protected]"
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
        src="https://img.daisyui.com/images/profile/demo/[email protected]"
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
        src="https://img.daisyui.com/images/profile/demo/[email protected]"
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
        src="https://img.daisyui.com/images/profile/demo/[email protected]"
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





# Collapse

Collapse is used for showing and hiding content.

## Component Details

| Class name       | Type      |                      |
| ---------------- | --------- | -------------------- |
| collapse         | Component | Collapse             |
| collapse-title   | Part      | Title part           |
| collapse-content | Part      | Content part         |
| collapse-arrow   | Modifier  | Adds arrow icon      |
| collapse-plus    | Modifier  | Adds plus/minus icon |
| collapse-open    | Modifier  | Force open           |
| collapse-close   | Modifier  | Force close          |

## HTML Examples

### Collapse with focus

```html
<div tabindex="0" class="collapse bg-base-100 border-base-300 border">
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### Collapse with checkbox

```html
<div class="collapse bg-base-100 border-base-300 border">
  <input type="checkbox" />
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### Collapse using details and summary tag

```html
<details class="collapse bg-base-100 border-base-300 border">
  <summary class="collapse-title font-semibold">How do I create an account?</summary>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</details>
```

### Without border and background color

```html
<div tabindex="0" class="collapse">
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### With arrow icon

```html
<div tabindex="0" class="collapse collapse-arrow bg-base-100 border-base-300 border">
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### With arrow plus/minus icon

```html
<div tabindex="0" class="collapse collapse-plus bg-base-100 border-base-300 border">
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### Force open

```html
<div tabindex="0" class="collapse collapse-open bg-base-100 border-base-300 border">
  <div class="collapse-title font-semibold">I have collapse-open class</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### Force close

```html
<div tabindex="0" class="collapse collapse-close bg-base-100 border-base-300 border">
  <div class="collapse-title font-semibold">I have collapse-open class</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### Custom colors for collapse that works with focus

```html
<div
  tabindex="0"
  class="bg-primary text-primary-content focus:bg-secondary focus:text-secondary-content collapse"
>
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```

### Custom colors for collapse that works with checkbox

```html
<div class="bg-base-100 border-base-300 collapse border">
  <input type="checkbox" class="peer" />
  <div
    class="collapse-title bg-primary text-primary-content peer-checked:bg-secondary peer-checked:text-secondary-content"
  >
    How do I create an account?
  </div>
  <div
    class="collapse-content bg-primary text-primary-content peer-checked:bg-secondary peer-checked:text-secondary-content"
  >
    Click the "Sign Up" button in the top right corner and follow the registration process.
  </div>
</div>
```







# Countdown

Countdown gives you a transition effect when you change a number between 0 to 99.

## Component Details

| Class name | Type      |                   |
| ---------- | --------- | ----------------- |
| countdown  | Component | Countdown wrapper |

## HTML Examples

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





# List

List is a vertical layout to display information in rows.

## Component Details

| Class name    | Type      |                                                              |
| ------------- | --------- | ------------------------------------------------------------ |
| list          | Component | A vertical flex layout to include list rows                  |
| list-row      | Component | The item inside list. A horizontal grid layout to include data |
| list-col-wrap | Modifier  | For one of direct children of list-row to push it to the next line |
| list-col-grow | Modifier  | For one of direct children of list-row to make it fill the remaining space |

## HTML Examples

### List (second column grows - default)

```html
<ul class="list bg-base-100 rounded-box shadow-md">
  <li class="p-4 pb-2 text-xs opacity-60 tracking-wide">Most played songs this week</li>
  <li class="list-row">
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div>
      <div>Dio Lupa</div>
      <div class="text-xs uppercase font-semibold opacity-60">Remaining Reason</div>
    </div>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></g></svg>
    </button>
  </li>
  <li class="list-row">
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div>
      <div>Ellie Beilish</div>
      <div class="text-xs uppercase font-semibold opacity-60">Bears of a fever</div>
    </div>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></g></svg>
    </button>
  </li>
  <li class="list-row">
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div>
      <div>Sabrino Gardener</div>
      <div class="text-xs uppercase font-semibold opacity-60">Cappuccino</div>
    </div>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></g></svg>
    </button>
  </li>
</ul>
```

### List (third column grows)

```html
<ul class="list bg-base-100 rounded-box shadow-md">
  <li class="p-4 pb-2 text-xs opacity-60 tracking-wide">Most played songs this week</li>
  <li class="list-row">
    <div class="text-4xl font-thin opacity-30 tabular-nums">01</div>
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div class="list-col-grow">
      <div>Dio Lupa</div>
      <div class="text-xs uppercase font-semibold opacity-60">Remaining Reason</div>
    </div>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
  </li>
  <li class="list-row">
    <div class="text-4xl font-thin opacity-30 tabular-nums">02</div>
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div class="list-col-grow">
      <div>Ellie Beilish</div>
      <div class="text-xs uppercase font-semibold opacity-60">Bears of a fever</div>
    </div>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
  </li>
  <li class="list-row">
    <div class="text-4xl font-thin opacity-30 tabular-nums">03</div>
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div class="list-col-grow">
      <div>Sabrino Gardener</div>
      <div class="text-xs uppercase font-semibold opacity-60">Cappuccino</div>
    </div>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
  </li>
</ul>
```

### List (third column wraps to next row)

```html
<ul class="list bg-base-100 rounded-box shadow-md">
  <li class="p-4 pb-2 text-xs opacity-60 tracking-wide">Most played songs this week</li>
  <li class="list-row">
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div>
      <div>Dio Lupa</div>
      <div class="text-xs uppercase font-semibold opacity-60">Remaining Reason</div>
    </div>
    <p class="list-col-wrap text-xs">
      "Remaining Reason" became an instant hit, praised for its haunting sound and emotional depth. A viral performance brought it widespread recognition, making it one of Dio Lupa’s most iconic tracks.
    </p>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></g></svg>
    </button>
  </li>
  <li class="list-row">
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div>
      <div>Ellie Beilish</div>
      <div class="text-xs uppercase font-semibold opacity-60">Bears of a fever</div>
    </div>
    <p class="list-col-wrap text-xs">
      "Bears of a Fever" captivated audiences with its intense energy and mysterious lyrics. Its popularity skyrocketed after fans shared it widely online, earning Ellie critical acclaim.
    </p>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></g></svg>
    </button>
  </li>
  <li class="list-row">
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
    <div>
      <div>Sabrino Gardener</div>
      <div class="text-xs uppercase font-semibold opacity-60">Cappuccino</div>
    </div>
    <p class="list-col-wrap text-xs">
      "Cappuccino" quickly gained attention for its smooth melody and relatable themes. The song’s success propelled Sabrino into the spotlight, solidifying their status as a rising star.
    </p>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M6 3L20 12 6 21 6 3z"></path></g></svg>
    </button>
    <button class="btn btn-square btn-ghost">
      <svg class="size-[1.2em]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></g></svg>
    </button>
  </li>
</ul>
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
          <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
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
    <div class="stat-value">89,400</div>
    <div class="stat-actions">
      <button class="btn btn-xs btn-success">Add funds</button>
    </div>
  </div>
  <div class="stat">
    <div class="stat-title">Current balance</div>
    <div class="stat-value">89,400</div>
    <div class="stat-actions">
      <button class="btn btn-xs">Withdrawal</button>
      <button class="btn btn-xs">Deposit</button>
    </div>
  </div>
</div>
```
