### Actions Components

1. ~~[Button](#button/)~~
2. ~~[Dropdown](#dropdown/)~~
3. ~~[Modal](#modal/)~~
4. [Swap](#swap/)
5. [Theme Controller](#theme-controller/)



# Button

Buttons allow the user to take actions or make choices.

## Component Details

| Class name    | Type      |                                |
| ------------- | --------- | ------------------------------ |
| btn           | Component | Button                         |
| btn-neutral   | Color     | neutral color                  |
| btn-primary   | Color     | primary color                  |
| btn-secondary | Color     | secondary color                |
| btn-accent    | Color     | accent color                   |
| btn-info      | Color     | info color                     |
| btn-success   | Color     | success color                  |
| btn-warning   | Color     | warning color                  |
| btn-error     | Color     | error color                    |
| btn-outline   | Style     | outline style                  |
| btn-dash      | Style     | dash style                     |
| btn-soft      | Style     | soft style                     |
| btn-ghost     | Style     | ghost style                    |
| btn-link      | Style     | looks like a link              |
| btn-active    | Behavior  | looks active                   |
| btn-disabled  | Behavior  | looks disabled                 |
| btn-xs        | Size      | Extra small size               |
| btn-sm        | Size      | Small size                     |
| btn-md        | Size      | Medium size (default)          |
| btn-lg        | Size      | Large size                     |
| btn-xl        | Size      | Extra large size               |
| btn-wide      | Modifier  | more horizontal padding        |
| btn-block     | Modifier  | Full width                     |
| btn-square    | Modifier  | 1:1 ratio                      |
| btn-circle    | Modifier  | 1:1 ratio with rounded corners |

## HTML Examples

### Button

```html
<button class="btn">Default</button>
```

### Button sizes

```html
<button class="btn btn-xs">Xsmall</button>
<button class="btn btn-sm">Small</button>
<button class="btn">Medium</button>
<button class="btn btn-lg">Large</button>
<button class="btn btn-xl">Xlarge</button>
```

### Responsive button

```html
<button class="btn btn-xs sm:btn-sm md:btn-md lg:btn-lg xl:btn-xl">Responsive</button>
```

### Buttons colors

```html
<button class="btn btn-neutral">Neutral</button>
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-accent">Accent</button>
<button class="btn btn-info">Info</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-warning">Warning</button>
<button class="btn btn-error">Error</button>
```

### Soft buttons

```html
<button class="btn btn-soft">Default</button>
<button class="btn btn-soft btn-primary">Primary</button>
<button class="btn btn-soft btn-secondary">Secondary</button>
<button class="btn btn-soft btn-accent">Accent</button>
<button class="btn btn-soft btn-info">Info</button>
<button class="btn btn-soft btn-success">Success</button>
<button class="btn btn-soft btn-warning">Warning</button>
<button class="btn btn-soft btn-error">Error</button>
```

### Outline buttons

```html
<button class="btn btn-outline">Default</button>
<button class="btn btn-outline btn-primary">Primary</button>
<button class="btn btn-outline btn-secondary">Secondary</button>
<button class="btn btn-outline btn-accent">Accent</button>
<button class="btn btn-outline btn-info">Info</button>
<button class="btn btn-outline btn-success">Success</button>
<button class="btn btn-outline btn-warning">Warning</button>
<button class="btn btn-outline btn-error">Error</button>
```

### Dash buttons

```html
<button class="btn btn-dash">Default</button>
<button class="btn btn-dash btn-primary">Primary</button>
<button class="btn btn-dash btn-secondary">Secondary</button>
<button class="btn btn-dash btn-accent">Accent</button>
<button class="btn btn-dash btn-info">Info</button>
<button class="btn btn-dash btn-success">Success</button>
<button class="btn btn-dash btn-warning">Warning</button>
<button class="btn btn-dash btn-error">Error</button>
```

### neutral button with outline or dash style

```html
<div class="bg-white p-6">
  <button class="btn btn-neutral btn-outline">Outline</button>
  <button class="btn btn-neutral btn-dash">Dash</button>
</div>
```

### Active buttons

```html
<button class="btn btn-active">Default</button>
<button class="btn btn-active btn-primary">Primary</button>
<button class="btn btn-active btn-secondary">Secondary</button>
<button class="btn btn-active btn-accent">Accent</button>
<button class="btn btn-active btn-info">Info</button>
<button class="btn btn-active btn-success">Success</button>
<button class="btn btn-active btn-warning">Warning</button>
<button class="btn btn-active btn-error">Error</button>
```

### Buttons ghost and button link

```html
<button class="btn btn-ghost">Ghost</button>
<button class="btn btn-link">Link</button>
```

### Wide button

```html
<button class="btn btn-wide">Wide</button>
```

### Buttons with any HTML tags

```html
<a role="button" class="btn">Link</a>
<button type="submit" class="btn">Button</button>
<input type="button" value="Input" class="btn" />
<input type="submit" value="Submit" class="btn" />
<input type="radio" aria-label="Radio" class="btn" />
<input type="checkbox" aria-label="Checkbox" class="btn" />
<input type="reset" value="Reset" class="btn" />
```

### Disabled buttons

```html
<button class="btn" disabled="disabled">Disabled using attribute</button>
<button class="btn btn-disabled" tabindex="-1" role="button" aria-disabled="true">
  Disabled using class name
</button>
```

### Square button and circle button

```html
<button class="btn btn-square">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="size-[1.2em]"><path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" /></svg>
</button>
<button class="btn btn-circle">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="size-[1.2em]"><path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" /></svg>
</button>
```

### Button with Icon

```html
<button class="btn">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="size-[1.2em]"><path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" /></svg>
  Like
</button>
<button class="btn">
  Like
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="size-[1.2em]"><path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" /></svg>
</button>
```

### Button block

```html
<button class="btn btn-block">block</button>
```

### Button with loading spinner

```html
<button class="btn btn-square">
  <span class="loading loading-spinner"></span>
</button>
<button class="btn">
  <span class="loading loading-spinner"></span>
  loading
</button>
```



# Dropdown

Dropdown can open a menu or any other element when the button is clicked.

## Component Details

| Class name       | Type      |                                                |
| ---------------- | --------- | ---------------------------------------------- |
| dropdown         | Component | Dropdown container                             |
| dropdown-content | Part      | Content part                                   |
| dropdown-start   | Placement | Align horizontally to start of button[Default] |
| dropdown-center  | Placement | Align horizontally to center of button         |
| dropdown-end     | Placement | Align horizontally to end of button            |
| dropdown-top     | Placement | Open from top                                  |
| dropdown-bottom  | Placement | Open from bottom[Default]                      |
| dropdown-left    | Placement | Open from left                                 |
| dropdown-right   | Placement | Open from right                                |
| dropdown-hover   | Modifier  | Opens on hover too                             |
| dropdown-open    | Modifier  | Force open                                     |

## HTML Examples

### Dropdown using details and summary

```html
<details class="dropdown">
  <summary class="btn m-1">open or close</summary>
  <ul class="menu dropdown-content bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</details>
```

### Dropdown using popover API and anchor positioning

```html
<!-- change popover-1 and --anchor-1 names. Use unique names for each dropdown -->
<button class="btn" popovertarget="popover-1" style="anchor-name:--anchor-1">
  Button
</button>
<ul class="dropdown menu w-52 rounded-box bg-base-100 shadow-sm"
  popover id="popover-1" style="position-anchor:--anchor-1">
  <li><a>Item 1</a></li>
  <li><a>Item 2</a></li>
</ul>
```

### Dropdown menu

```html
<div class="dropdown">
  <div tabindex="0" role="button" class="btn m-1">Click</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown / aligns to start of button horizontally

```html
<div class="dropdown dropdown-start">
  <div tabindex="0" role="button" class="btn m-1">Click ⬇️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown / aligns to end of button horizontally

```html
<div class="dropdown dropdown-end">
  <div tabindex="0" role="button" class="btn m-1">Click  ⬇️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown / aligns to center of button horizontally

```html
<div class="dropdown dropdown-center">
  <div tabindex="0" role="button" class="btn m-1">Click  ⬇️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown top

```html
<div class="dropdown dropdown-top">
  <div tabindex="0" role="button" class="btn m-1">Click ⬆️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown top / aligns to center of button horizontally

```html
<div class="dropdown dropdown-top dropdown-center">
  <div tabindex="0" role="button" class="btn m-1">Click ⬆️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown top / aligns to end of button horizontally

```html
<div class="dropdown dropdown-top dropdown-end">
  <div tabindex="0" role="button" class="btn m-1">Click ⬆️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown bottom (default)

```html
<div class="dropdown dropdown-bottom">
  <div tabindex="0" role="button" class="btn m-1">Click ⬇️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown bottom (default) / aligns to center of button horizontally

```html
<div class="dropdown dropdown-bottom dropdown-center">
  <div tabindex="0" role="button" class="btn m-1">Click ⬇️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown bottom (default) / aligns to end of button horizontally

```html
<div class="dropdown dropdown-bottom dropdown-end">
  <div tabindex="0" role="button" class="btn m-1">Click ⬇️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown left

```html
<div class="dropdown dropdown-left">
  <div tabindex="0" role="button" class="btn m-1">Click ⬅️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown left / aligns to center of button vertically

```html
<div class="dropdown dropdown-left dropdown-center">
  <div tabindex="0" role="button" class="btn m-1">Click ⬅️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown left / aligns to end of button vertically

```html
<div class="dropdown dropdown-left dropdown-end">
  <div tabindex="0" role="button" class="btn m-1">Click ⬅️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown right

```html
<div class="dropdown dropdown-right">
  <div tabindex="0" role="button" class="btn m-1">Click ➡️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown right / aligns to end of button vertically

```html
<div class="dropdown dropdown-right dropdown-end">
  <div tabindex="0" role="button" class="btn m-1">Click ➡️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown right / aligns to center of button vertically

```html
<div class="dropdown dropdown-right dropdown-center">
  <div tabindex="0" role="button" class="btn m-1">Click ➡️</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Dropdown on hover

```html
<div class="dropdown dropdown-hover">
  <div tabindex="0" role="button" class="btn m-1">Hover</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Force open

```html
<div class="dropdown dropdown-open">
  <div tabindex="0" role="button" class="btn m-1">Button</div>
  <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div>
```

### Card as dropdown

```html
<div class="dropdown">
  <div tabindex="0" role="button" class="btn m-1">Click</div>
  <div
    tabindex="0"
    class="dropdown-content card card-sm bg-base-100 z-1 w-64 shadow-md">
    <div class="card-body">
      <p>This is a card. You can use any element as a dropdown.</p>
    </div>
  </div>
</div>
```

### Dropdown in navbar

```html
<div class="navbar bg-base-200">
  <div class="ps-4">
    <a class="text-lg font-bold">daisyUI</a>
  </div>
  <div class="flex grow justify-end px-2">
    <div class="flex items-stretch">
      <a class="btn btn-ghost rounded-field">Button</a>
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost rounded-field">Dropdown</div>
        <ul
          tabindex="0"
          class="menu dropdown-content bg-base-200 rounded-box z-1 mt-4 w-52 p-2 shadow-sm">
          <li><a>Item 1</a></li>
          <li><a>Item 2</a></li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

### Helper dropdown

```html
A normal text and a helper dropdown
<div class="dropdown dropdown-end">
  <div tabindex="0" role="button" class="btn btn-circle btn-ghost btn-xs text-info">
    <svg
      tabindex="0"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      class="h-4 w-4 stroke-current">
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
    </svg>
  </div>
  <div
    tabindex="0"
    class="card card-sm dropdown-content bg-base-100 rounded-box z-1 w-64 shadow-sm">
    <div tabindex="0" class="card-body">
      <h2 class="card-title">You needed more info?</h2>
      <p>Here is a description!</p>
    </div>
  </div>
</div>
```





# Modal

Modal is used to show a dialog or a box when you click a button.

## Component Details

| Class name     | Type      |                                                              |
| -------------- | --------- | ------------------------------------------------------------ |
| modal          | Component | Modal                                                        |
| modal-box      | Part      | The content part                                             |
| modal-action   | Part      | Actions part (buttons, etc.)                                 |
| modal-backdrop | Part      | Label that covers the page when modal is open so we can close the modal by clicking outside |
| modal-toggle   | Part      | Hidden checkbox that controls the state of modal             |
| modal-open     | Modifier  | Keeps the modal open (you can add this class using JS)       |
| modal-top      | Placement | Moves the modal to top                                       |
| modal-middle   | Placement | Moves the modal to middle[Default]                           |
| modal-bottom   | Placement | Moves the modal to bottom                                    |
| modal-start    | Placement | Moves the modal to start horizontally                        |
| modal-end      | Placement | Moves the modal to end horizontally                          |

## HTML Examples

## Method 1. HTML dialog element`recommended`

HTML dialog element is a native way to create modals. It is accessible and we can close the modal using`Esc`key.
 We can open the modal using JS`ID.showModal()`method and close it using`ID.close()`method.
 The ID must be unique for each modal.

### Dialog modal

```html
<!-- Open the modal using ID.showModal() method -->
<button class="btn" onclick="my_modal_1.showModal()">open modal</button>
<dialog id="my_modal_1" class="modal">
  <div class="modal-box">
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">Press ESC key or click the button below to close</p>
    <div class="modal-action">
      <form method="dialog">
        <!-- if there is a button in form, it will close the modal -->
        <button class="btn">Close</button>
      </form>
    </div>
  </div>
</dialog>
```

### Dialog modal, closes when clicked outside

```html
<!-- Open the modal using ID.showModal() method -->
<button class="btn" onclick="my_modal_2.showModal()">open modal</button>
<dialog id="my_modal_2" class="modal">
  <div class="modal-box">
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">Press ESC key or click outside to close</p>
  </div>
  <form method="dialog" class="modal-backdrop">
    <button>close</button>
  </form>
</dialog>
```

### Dialog modal with a close button at corner

```html
<!-- You can open the modal using ID.showModal() method -->
<button class="btn" onclick="my_modal_3.showModal()">open modal</button>
<dialog id="my_modal_3" class="modal">
  <div class="modal-box">
    <form method="dialog">
      <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
    </form>
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">Press ESC key or click on ✕ button to close</p>
  </div>
</dialog>
```

### Dialog modal with custom width

```html
<!-- You can open the modal using ID.showModal() method -->
<button class="btn" onclick="my_modal_4.showModal()">open modal</button>
<dialog id="my_modal_4" class="modal">
  <div class="modal-box w-11/12 max-w-5xl">
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">Click the button below to close</p>
    <div class="modal-action">
      <form method="dialog">
        <!-- if there is a button, it will close the modal -->
        <button class="btn">Close</button>
      </form>
    </div>
  </div>
</dialog>
```

### Responsive

```html
<!-- Open the modal using ID.showModal() method -->
<button class="btn" onclick="my_modal_5.showModal()">open modal</button>
<dialog id="my_modal_5" class="modal modal-bottom sm:modal-middle">
  <div class="modal-box">
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">Press ESC key or click the button below to close</p>
    <div class="modal-action">
      <form method="dialog">
        <!-- if there is a button in form, it will close the modal -->
        <button class="btn">Close</button>
      </form>
    </div>
  </div>
</dialog>
```

## Method 2. checkbox`legacy`

A hidden checkbox can control the state of modal and labels can toggle the checkbox so we can open/close the modal.

### Modal using checkbox

```html
<!-- The button to open modal -->
<label for="my_modal_6" class="btn">open modal</label>
<!-- Put this part before </body> tag -->
<input type="checkbox" id="my_modal_6" class="modal-toggle" />
<div class="modal" role="dialog">
  <div class="modal-box">
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">This modal works with a hidden checkbox!</p>
    <div class="modal-action">
      <label for="my_modal_6" class="btn">Close!</label>
    </div>
  </div>
</div>
```

### Modal that closes when clicked outside

```html
<!-- The button to open modal -->
<label for="my_modal_7" class="btn">open modal</label>
<!-- Put this part before </body> tag -->
<input type="checkbox" id="my_modal_7" class="modal-toggle" />
<div class="modal" role="dialog">
  <div class="modal-box">
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">This modal works with a hidden checkbox!</p>
  </div>
  <label class="modal-backdrop" for="my_modal_7">Close</label>
</div>
```

### Method 3. using anchor links`legacy`

A link adds a parameter to the URL and you only see the modal when the URL has that parameter
 When modal is closed, the page will scroll to the top because of the anchor link. Anchor links might not work well on some SPA frameworks. If there are problems, use the other methods

### Modal using anchor link

```html
<!-- The button to open modal -->
<a href="#my_modal_8" class="btn">open modal</a>
<!-- Put this part before </body> tag -->
<div class="modal" role="dialog" id="my_modal_8">
  <div class="modal-box">
    <h3 class="text-lg font-bold">Hello!</h3>
    <p class="py-4">This modal works with anchor links</p>
    <div class="modal-action">
      <a href="#" class="btn">Yay!</a>
    </div>
  </div>
</div>
```





# Swap

Swap allows you to toggle the visibility of two elements using a checkbox or a class name.

## Component Details

| Class name         | Type      |                                                              |
| ------------------ | --------- | ------------------------------------------------------------ |
| swap               | Component | Swap container                                               |
| swap-on            | Part      | The child element that should be visible when checkbox is checked or when swap is active |
| swap-off           | Part      | The child element that should be visible when checkbox is not checked or when swap is not active |
| swap-indeterminate | Part      | The child element that should be visible when checkbox is indeterminate |
| swap-active        | Modifier  | Activates the swap (no need for checkbox)                    |
| swap-rotate        | Style     | Adds rotate effect to swap                                   |
| swap-flip          | Style     | Adds flip effect to swap                                     |

## HTML Examples

### Swap text

```html
<label class="swap">
  <input type="checkbox" />
  <div class="swap-on">ON</div>
  <div class="swap-off">OFF</div>
</label>
```

### Swap volume icons

```html
<label class="swap">
  <!-- this hidden checkbox controls the state -->
  <input type="checkbox" />
  <!-- volume on icon -->
  <svg
    class="swap-on fill-current"
    xmlns="http://www.w3.org/2000/svg"
    width="48"
    height="48"
    viewBox="0 0 24 24">
    <path
      d="M14,3.23V5.29C16.89,6.15 19,8.83 19,12C19,15.17 16.89,17.84 14,18.7V20.77C18,19.86 21,16.28 21,12C21,7.72 18,4.14 14,3.23M16.5,12C16.5,10.23 15.5,8.71 14,7.97V16C15.5,15.29 16.5,13.76 16.5,12M3,9V15H7L12,20V4L7,9H3Z" />
  </svg>
  <!-- volume off icon -->
  <svg
    class="swap-off fill-current"
    xmlns="http://www.w3.org/2000/svg"
    width="48"
    height="48"
    viewBox="0 0 24 24">
    <path
      d="M3,9H7L12,4V20L7,15H3V9M16.59,12L14,9.41L15.41,8L18,10.59L20.59,8L22,9.41L19.41,12L22,14.59L20.59,16L18,13.41L15.41,16L14,14.59L16.59,12Z" />
  </svg>
</label>
```

### Swap icons with rotate effect

```html
<label class="swap swap-rotate">
  <!-- this hidden checkbox controls the state -->
  <input type="checkbox" />
  <!-- sun icon -->
  <svg
    class="swap-on h-10 w-10 fill-current"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24">
    <path
      d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z" />
  </svg>
  <!-- moon icon -->
  <svg
    class="swap-off h-10 w-10 fill-current"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24">
    <path
      d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z" />
  </svg>
</label>
```

### Hamburger button

```html
<label class="btn btn-circle swap swap-rotate">
  <!-- this hidden checkbox controls the state -->
  <input type="checkbox" />
  <!-- hamburger icon -->
  <svg
    class="swap-off fill-current"
    xmlns="http://www.w3.org/2000/svg"
    width="32"
    height="32"
    viewBox="0 0 512 512">
    <path d="M64,384H448V341.33H64Zm0-106.67H448V234.67H64ZM64,128v42.67H448V128Z" />
  </svg>
  <!-- close icon -->
  <svg
    class="swap-on fill-current"
    xmlns="http://www.w3.org/2000/svg"
    width="32"
    height="32"
    viewBox="0 0 512 512">
    <polygon
      points="400 145.49 366.51 112 256 222.51 145.49 112 112 145.49 222.51 256 112 366.51 145.49 400 256 289.49 366.51 400 400 366.51 289.49 256 400 145.49" />
  </svg>
</label>
```

### Swap icons with flip effect

```html
<label class="swap swap-flip text-9xl">
  <!-- this hidden checkbox controls the state -->
  <input type="checkbox" />
  <div class="swap-on">😈</div>
  <div class="swap-off">😇</div>
</label>
```

### Activate using class name instead of checkbox

```html
<label class="swap text-6xl">
  <div class="swap-on">🥵</div>
  <div class="swap-off">🥶</div>
</label>
<label class="swap swap-active text-6xl">
  <div class="swap-on">🥳</div>
  <div class="swap-off">😭</div>
</label>
```





# Theme Controller

If a checked checkbox input or a checked radio input with theme-controller class exists in the page, The page will have the same theme as that input's value.

## Component Details

| Class name       | Type      |                                                              |
| ---------------- | --------- | ------------------------------------------------------------ |
| theme-controller | Component | For a checkbox or radio input that must change the page theme |

## HTML Examples

### Theme Controller using a toggle

```html
<input type="checkbox" value="synthwave" class="toggle theme-controller" />
```

### Theme Controller using a checkbox

```html
<input type="checkbox" value="synthwave" class="checkbox theme-controller" />
```

### Theme Controller using a swap

```html
<label class="swap swap-rotate">
  <!-- this hidden checkbox controls the state -->
  <input type="checkbox" class="theme-controller" value="synthwave" />
  <!-- sun icon -->
  <svg
    class="swap-off h-10 w-10 fill-current"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24">
    <path
      d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z" />
  </svg>
  <!-- moon icon -->
  <svg
    class="swap-on h-10 w-10 fill-current"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24">
    <path
      d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z" />
  </svg>
</label>
```

### Theme Controller using a toggle with text

```html
<label class="flex cursor-pointer gap-2">
  <span class="label-text">Current</span>
  <input type="checkbox" value="synthwave" class="toggle theme-controller" />
  <span class="label-text">Synthwave</span>
</label>
```

### Theme Controller using a toggle with icons

```html
<label class="flex cursor-pointer gap-2">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round">
    <circle cx="12" cy="12" r="5" />
    <path
      d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4" />
  </svg>
  <input type="checkbox" value="synthwave" class="toggle theme-controller" />
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="20"
    height="20"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round">
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
  </svg>
</label>
```

### Theme Controller using a toggle with icons inside

```html
<label class="toggle text-base-content">
  <input type="checkbox" value="synthwave" class="theme-controller" />
  <svg aria-label="sun" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2"></path><path d="M12 20v2"></path><path d="m4.93 4.93 1.41 1.41"></path><path d="m17.66 17.66 1.41 1.41"></path><path d="M2 12h2"></path><path d="M20 12h2"></path><path d="m6.34 17.66-1.41 1.41"></path><path d="m19.07 4.93-1.41 1.41"></path></g></svg>
  <svg aria-label="moon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"></path></g></svg>
</label>
```

### Theme Controller using a toggle with custom colors

```html
<input
  type="checkbox"
  value="synthwave"
  class="toggle theme-controller col-span-2 col-start-1 row-start-1 border-sky-400 bg-amber-300 [--tglbg:var(--color-sky-500)] checked:border-blue-800 checked:bg-blue-300 checked:[--tglbg:var(--color-blue-900)]" />
```

### Theme Controller using a radio input

```html
<fieldset class="fieldset">
  <label class="flex gap-2 cursor-pointer items-center">
    <input type="radio" name="theme-radios" class="radio radio-sm theme-controller" value="default"/>
    Default
  </label>
  <label class="flex gap-2 cursor-pointer items-center">
    <input type="radio" name="theme-radios" class="radio radio-sm theme-controller" value="retro"/>
    Retro
  </label>
  <label class="flex gap-2 cursor-pointer items-center">
    <input type="radio" name="theme-radios" class="radio radio-sm theme-controller" value="cyberpunk"/>
    Cyberpunk
  </label>
  <label class="flex gap-2 cursor-pointer items-center">
    <input type="radio" name="theme-radios" class="radio radio-sm theme-controller" value="valentine"/>
    Valentine
  </label>
  <label class="flex gap-2 cursor-pointer items-center">
    <input type="radio" name="theme-radios" class="radio radio-sm theme-controller" value="aqua"/>
    Aqua
  </label>
</fieldset>
```

### Theme Controller using a radio button

```html
<div class="join join-vertical">
  <input
    type="radio"
    name="theme-buttons"
    class="btn theme-controller join-item"
    aria-label="Default"
    value="default" />
  <input
    type="radio"
    name="theme-buttons"
    class="btn theme-controller join-item"
    aria-label="Retro"
    value="retro" />
  <input
    type="radio"
    name="theme-buttons"
    class="btn theme-controller join-item"
    aria-label="Cyberpunk"
    value="cyberpunk" />
  <input
    type="radio"
    name="theme-buttons"
    class="btn theme-controller join-item"
    aria-label="Valentine"
    value="valentine" />
  <input
    type="radio"
    name="theme-buttons"
    class="btn theme-controller join-item"
    aria-label="Aqua"
    value="aqua" />
</div>
```

### Theme Controller using a dropdown

```html
<div class="dropdown mb-72">
  <div tabindex="0" role="button" class="btn m-1">
    Theme
    <svg
      width="12px"
      height="12px"
      class="inline-block h-2 w-2 fill-current opacity-60"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 2048 2048">
      <path d="M1799 349l242 241-1017 1017L7 590l242-241 775 775 775-775z"></path>
    </svg>
  </div>
  <ul tabindex="0" class="dropdown-content bg-base-300 rounded-box z-1 w-52 p-2 shadow-2xl">
    <li>
      <input
        type="radio"
        name="theme-dropdown"
        class="theme-controller w-full btn btn-sm btn-block btn-ghost justify-start"
        aria-label="Default"
        value="default" />
    </li>
    <li>
      <input
        type="radio"
        name="theme-dropdown"
        class="theme-controller w-full btn btn-sm btn-block btn-ghost justify-start"
        aria-label="Retro"
        value="retro" />
    </li>
    <li>
      <input
        type="radio"
        name="theme-dropdown"
        class="theme-controller w-full btn btn-sm btn-block btn-ghost justify-start"
        aria-label="Cyberpunk"
        value="cyberpunk" />
    </li>
    <li>
      <input
        type="radio"
        name="theme-dropdown"
        class="theme-controller w-full btn btn-sm btn-block btn-ghost justify-start"
        aria-label="Valentine"
        value="valentine" />
    </li>
    <li>
      <input
        type="radio"
        name="theme-dropdown"
        class="theme-controller w-full btn btn-sm btn-block btn-ghost justify-start"
        aria-label="Aqua"
        value="aqua" />
    </li>
  </ul>
</div>
```

