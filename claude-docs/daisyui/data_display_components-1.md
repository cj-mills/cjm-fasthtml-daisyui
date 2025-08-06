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



# Accordion

Accordion is used for showing and hiding content but only one item can stay open at a time.

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

### Accordion using radio inputs

```html
<div class="collapse bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-1" checked="checked" />
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">Click the "Sign Up" button in the top right corner and follow the registration process.</div>
</div>
<div class="collapse bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-1" />
  <div class="collapse-title font-semibold">I forgot my password. What should I do?</div>
  <div class="collapse-content text-sm">Click on "Forgot Password" on the login page and follow the instructions sent to your email.</div>
</div>
<div class="collapse bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-1" />
  <div class="collapse-title font-semibold">How do I update my profile information?</div>
  <div class="collapse-content text-sm">Go to "My Account" settings and select "Edit Profile" to make changes.</div>
</div>
```

### Accordion with arrow icon

```html
<div class="collapse collapse-arrow bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-2" checked="checked" />
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">Click the "Sign Up" button in the top right corner and follow the registration process.</div>
</div>
<div class="collapse collapse-arrow bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-2" />
  <div class="collapse-title font-semibold">I forgot my password. What should I do?</div>
  <div class="collapse-content text-sm">Click on "Forgot Password" on the login page and follow the instructions sent to your email.</div>
</div>
<div class="collapse collapse-arrow bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-2" />
  <div class="collapse-title font-semibold">How do I update my profile information?</div>
  <div class="collapse-content text-sm">Go to "My Account" settings and select "Edit Profile" to make changes.</div>
</div>
```

### Accordion with plus/minus icon

```html
<div class="collapse collapse-plus bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-3" checked="checked" />
  <div class="collapse-title font-semibold">How do I create an account?</div>
  <div class="collapse-content text-sm">Click the "Sign Up" button in the top right corner and follow the registration process.</div>
</div>
<div class="collapse collapse-plus bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-3" />
  <div class="collapse-title font-semibold">I forgot my password. What should I do?</div>
  <div class="collapse-content text-sm">Click on "Forgot Password" on the login page and follow the instructions sent to your email.</div>
</div>
<div class="collapse collapse-plus bg-base-100 border border-base-300">
  <input type="radio" name="my-accordion-3" />
  <div class="collapse-title font-semibold">How do I update my profile information?</div>
  <div class="collapse-content text-sm">Go to "My Account" settings and select "Edit Profile" to make changes.</div>
</div>
```

### Using Accordion and Join together

```html
<div class="join join-vertical bg-base-100">
  <div class="collapse collapse-arrow join-item border-base-300 border">
    <input type="radio" name="my-accordion-4" checked="checked" />
    <div class="collapse-title font-semibold">How do I create an account?</div>
    <div class="collapse-content text-sm">Click the "Sign Up" button in the top right corner and follow the registration process.</div>
  </div>
  <div class="collapse collapse-arrow join-item border-base-300 border">
    <input type="radio" name="my-accordion-4" />
    <div class="collapse-title font-semibold">I forgot my password. What should I do?</div>
    <div class="collapse-content text-sm">Click on "Forgot Password" on the login page and follow the instructions sent to your email.</div>
  </div>
  <div class="collapse collapse-arrow join-item border-base-300 border">
    <input type="radio" name="my-accordion-4" />
    <div class="collapse-title font-semibold">How do I update my profile information?</div>
    <div class="collapse-content text-sm">Go to "My Account" settings and select "Edit Profile" to make changes.</div>
  </div>
</div>
```





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
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
```

### Avatar in custom sizes

```html
<div class="avatar">
  <div class="w-32 rounded">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
<div class="avatar">
  <div class="w-20 rounded">
    <img
      src="https://img.daisyui.com/images/profile/demo/[email protected]"
      alt="Tailwind-CSS-Avatar-component"
    />
  </div>
</div>
<div class="avatar">
  <div class="w-16 rounded">
    <img
      src="https://img.daisyui.com/images/profile/demo/[email protected]"
      alt="Tailwind-CSS-Avatar-component"
    />
  </div>
</div>
<div class="avatar">
  <div class="w-8 rounded">
    <img
      src="https://img.daisyui.com/images/profile/demo/[email protected]"
      alt="Tailwind-CSS-Avatar-component"
    />
  </div>
</div>
```

### Avatar rounded

```html
<div class="avatar">
  <div class="w-24 rounded-xl">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
<div class="avatar">
  <div class="w-24 rounded-full">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
```

### Avatar with mask

```html
<div class="avatar">
  <div class="mask mask-heart w-24">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
<div class="avatar">
  <div class="mask mask-squircle w-24">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
<div class="avatar">
  <div class="mask mask-hexagon-2 w-24">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
```

### Avatar group

```html
<div class="avatar-group -space-x-6">
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
    </div>
  </div>
</div>
```

### Avatar group with counter

```html
<div class="avatar-group -space-x-6">
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
    </div>
  </div>
  <div class="avatar">
    <div class="w-12">
      <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
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
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
```

### Avatar with presence indicator

```html
<div class="avatar avatar-online">
  <div class="w-24 rounded-full">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
  </div>
</div>
<div class="avatar avatar-offline">
  <div class="w-24 rounded-full">
    <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
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



# Card

Cards are used to group and display content in a way that is easily readable.

## Component Details

| Class name   | Type      |                                                      |
| ------------ | --------- | ---------------------------------------------------- |
| card         | Component | Card                                                 |
| card-title   | Part      | Title part                                           |
| card-body    | Part      | Body part (content)                                  |
| card-actions | Part      | Actions part (buttons, etc.)                         |
| card-border  | Style     | Adds border to <card>                                |
| card-dash    | Style     | dash style                                           |
| card-side    | Modifier  | The image in <figure> will be on to the side         |
| image-full   | Modifier  | The image in <figure> element will be the background |
| card-xs      | Size      | Extra small size                                     |
| card-sm      | Size      | Small size                                           |
| card-md      | Size      | Medium size (default)                                |
| card-lg      | Size      | Large size                                           |
| card-xl      | Size      | Extra large size                                     |

## HTML Examples

### Card

```html
<div class="card bg-base-100 w-96 shadow-sm">
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
      alt="Shoes" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
```

### Pricing Card

```html
<div class="card w-96 bg-base-100 shadow-sm">
  <div class="card-body">
    <span class="badge badge-xs badge-warning">Most Popular</span>
    <div class="flex justify-between">
      <h2 class="text-3xl font-bold">Premium</h2>
      <span class="text-xl">29/mo</span>
    </div>
    <ul class="mt-6 flex flex-col gap-2 text-xs">
      <li>
        <svg xmlns="http://www.w3.org/2000/svg" class="size-4 me-2 inline-block text-success" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        <span>High-resolution image generation</span>
      </li>
      <li>
        <svg xmlns="http://www.w3.org/2000/svg" class="size-4 me-2 inline-block text-success" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        <span>Customizable style templates</span>
      </li>
      <li>
        <svg xmlns="http://www.w3.org/2000/svg" class="size-4 me-2 inline-block text-success" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        <span>Batch processing capabilities</span>
      </li>
      <li>
        <svg xmlns="http://www.w3.org/2000/svg" class="size-4 me-2 inline-block text-success" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        <span>AI-driven image enhancements</span>
      </li>
      <li class="opacity-50">
        <svg xmlns="http://www.w3.org/2000/svg" class="size-4 me-2 inline-block text-base-content/50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        <span class="line-through">Seamless cloud integration</span>
      </li>
      <li class="opacity-50">
        <svg xmlns="http://www.w3.org/2000/svg" class="size-4 me-2 inline-block text-base-content/50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        <span class="line-through">Real-time collaboration tools</span>
      </li>
    </ul>
    <div class="mt-6">
      <button class="btn btn-primary btn-block">Subscribe</button>
    </div>
  </div>
</div>
```

### Card sizes

```html
<div class="card w-96 bg-base-100 card-xs shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Xsmall Card</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="justify-end card-actions">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
<div class="card w-96 bg-base-100 card-sm shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Small Card</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="justify-end card-actions">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
<div class="card w-96 bg-base-100 card-md shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Medium Card</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="justify-end card-actions">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
<div class="card w-96 bg-base-100 card-lg shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Large Card</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="justify-end card-actions">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
<div class="card w-96 bg-base-100 card-xl shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Xlarge Card</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="justify-end card-actions">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
```

### Card with a card-border

```html
<div class="card card-border bg-base-100 w-96">
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
```

### Card with a dash border

```html
<div class="card card-dash bg-base-100 w-96">
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
```

### Card with badge

```html
<div class="card bg-base-100 w-96 shadow-sm">
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
      alt="Shoes" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">
      Card Title
      <div class="badge badge-secondary">NEW</div>
    </h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <div class="badge badge-outline">Fashion</div>
      <div class="badge badge-outline">Products</div>
    </div>
  </div>
</div>
```

### Card with bottom image

```html
<div class="card bg-base-100 w-96 shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
  </div>
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
      alt="Shoes" />
  </figure>
</div>
```

### Card with centered content and paddings

```html
<div class="card bg-base-100 w-96 shadow-sm">
  <figure class="px-10 pt-10">
    <img
      src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
      alt="Shoes"
      class="rounded-xl" />
  </figure>
  <div class="card-body items-center text-center">
    <h2 class="card-title">Card Title</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
```

### Card with image overlay

```html
<div class="card bg-base-100 image-full w-96 shadow-sm">
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
      alt="Shoes" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
```

### Card with no image

```html
<div class="card bg-base-100 w-96 shadow-sm">
  <div class="card-body">
    <h2 class="card-title">Card title!</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
```

### Card with custom color

```html
<div class="card bg-primary text-primary-content w-96">
  <div class="card-body">
    <h2 class="card-title">Card title!</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <button class="btn">Buy Now</button>
    </div>
  </div>
</div>
```

### Centered card with neutral color

```html
<div class="card bg-neutral text-neutral-content w-96">
  <div class="card-body items-center text-center">
    <h2 class="card-title">Cookies!</h2>
    <p>We are using cookies for no reason.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Accept</button>
      <button class="btn btn-ghost">Deny</button>
    </div>
  </div>
</div>
```

### Card with action on top

```html
<div class="card bg-base-100 w-96 shadow-sm">
  <div class="card-body">
    <div class="card-actions justify-end">
      <button class="btn btn-square btn-sm">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
    <p>We are using cookies for no reason.</p>
  </div>
</div>
```

### Card with image on side

```html
<div class="card card-side bg-base-100 shadow-sm">
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1635805737707-575885ab0820.webp"
      alt="Movie" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">New movie is released!</h2>
    <p>Click the button to watch on Jetflix app.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Watch</button>
    </div>
  </div>
</div>
```

### Responsive card (vertical on small screen, horizontal on large screen)

```html
<div class="card lg:card-side bg-base-100 shadow-sm">
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1494232410401-ad00d5433cfa.webp"
      alt="Album" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">New album is released!</h2>
    <p>Click the button to listen on Spotiwhy app.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Listen</button>
    </div>
  </div>
</div>
```





# Carousel

Carousel show images or content in a scrollable area.

## Component Details

| Class name          | Type      |                                 |
| ------------------- | --------- | ------------------------------- |
| carousel            | Component | Carousel container              |
| carousel-item       | Part      | Carousel item                   |
| carousel-start      | Modifier  | Snap elements to start[Default] |
| carousel-center     | Modifier  | Snap elements to center         |
| carousel-end        | Modifier  | Snap elements to end            |
| carousel-horizontal | direction | Horizontal layout (default)     |
| carousel-vertical   | direction | Vertical layout                 |

## HTML Examples

### Snap to start (default)

```html
<div class="carousel rounded-box">
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp"
      alt="Burger" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp"
      alt="Burger" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp"
      alt="Burger" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp"
      alt="Burger" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp"
      alt="Burger" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp"
      alt="Burger" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp"
      alt="Burger" />
  </div>
</div>
```

### Snap to center

```html
<div class="carousel carousel-center rounded-box">
  <div class="carousel-item">
    <img src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp" alt="Pizza" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp"
      alt="Pizza" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp"
      alt="Pizza" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp"
      alt="Pizza" />
  </div>
  <div class="carousel-item">
    <img src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp" alt="Pizza" />
  </div>
  <div class="carousel-item">
    <img src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp" alt="Pizza" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp"
      alt="Pizza" />
  </div>
</div>
```

### Snap to end

```html
<div class="carousel carousel-end rounded-box">
  <div class="carousel-item">
    <img src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp" alt="Drink" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp"
      alt="Drink" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp"
      alt="Drink" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp"
      alt="Drink" />
  </div>
  <div class="carousel-item">
    <img src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp" alt="Drink" />
  </div>
  <div class="carousel-item">
    <img src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp" alt="Drink" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp"
      alt="Drink" />
  </div>
</div>
```

### Carousel with full width items

```html
<div class="carousel rounded-box w-64">
  <div class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp"
      class="w-full"
      alt="Tailwind CSS Carousel component" />
  </div>
  <div class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp"
      class="w-full"
      alt="Tailwind CSS Carousel component" />
  </div>
  <div class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp"
      class="w-full"
      alt="Tailwind CSS Carousel component" />
  </div>
  <div class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp"
      class="w-full"
      alt="Tailwind CSS Carousel component" />
  </div>
  <div class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp"
      class="w-full"
      alt="Tailwind CSS Carousel component" />
  </div>
  <div class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp"
      class="w-full"
      alt="Tailwind CSS Carousel component" />
  </div>
  <div class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp"
      class="w-full"
      alt="Tailwind CSS Carousel component" />
  </div>
</div>
```

### Vertical carousel

```html
<div class="carousel carousel-vertical rounded-box h-96">
  <div class="carousel-item h-full">
    <img src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp" />
  </div>
  <div class="carousel-item h-full">
    <img src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp" />
  </div>
  <div class="carousel-item h-full">
    <img src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp" />
  </div>
  <div class="carousel-item h-full">
    <img src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp" />
  </div>
  <div class="carousel-item h-full">
    <img src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp" />
  </div>
  <div class="carousel-item h-full">
    <img src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp" />
  </div>
  <div class="carousel-item h-full">
    <img src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp" />
  </div>
</div>
```

### Carousel with half width items

```html
<div class="carousel rounded-box w-96">
  <div class="carousel-item w-1/2">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp"
      class="w-full" />
  </div>
  <div class="carousel-item w-1/2">
    <img
      src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp"
      class="w-full" />
  </div>
  <div class="carousel-item w-1/2">
    <img
      src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp"
      class="w-full" />
  </div>
  <div class="carousel-item w-1/2">
    <img
      src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp"
      class="w-full" />
  </div>
  <div class="carousel-item w-1/2">
    <img
      src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp"
      class="w-full" />
  </div>
  <div class="carousel-item w-1/2">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp"
      class="w-full" />
  </div>
  <div class="carousel-item w-1/2">
    <img
      src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp"
      class="w-full" />
  </div>
</div>
```

### Full-bleed carousel

```html
<div class="carousel carousel-center bg-neutral rounded-box max-w-md space-x-4 p-4">
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1494253109108-2e30c049369b.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1550258987-190a2d41a8ba.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1559181567-c3190ca9959b.webp"
      class="rounded-box" />
  </div>
  <div class="carousel-item">
    <img
      src="https://img.daisyui.com/images/stock/photo-1601004890684-d8cbf643f5f2.webp"
      class="rounded-box" />
  </div>
</div>
```

### Carousel with indicator buttons

```html
<div class="carousel w-full">
  <div id="item1" class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.webp"
      class="w-full" />
  </div>
  <div id="item2" class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1609621838510-5ad474b7d25d.webp"
      class="w-full" />
  </div>
  <div id="item3" class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1414694762283-acccc27bca85.webp"
      class="w-full" />
  </div>
  <div id="item4" class="carousel-item w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.webp"
      class="w-full" />
  </div>
</div>
<div class="flex w-full justify-center gap-2 py-2">
  <a href="#item1" class="btn btn-xs">1</a>
  <a href="#item2" class="btn btn-xs">2</a>
  <a href="#item3" class="btn btn-xs">3</a>
  <a href="#item4" class="btn btn-xs">4</a>
</div>
```

### Carousel with next/prev buttons

```html
<div class="carousel w-full">
  <div id="slide1" class="carousel-item relative w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide4" class="btn btn-circle">❮</a>
      <a href="#slide2" class="btn btn-circle">❯</a>
    </div>
  </div>
  <div id="slide2" class="carousel-item relative w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1609621838510-5ad474b7d25d.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide1" class="btn btn-circle">❮</a>
      <a href="#slide3" class="btn btn-circle">❯</a>
    </div>
  </div>
  <div id="slide3" class="carousel-item relative w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1414694762283-acccc27bca85.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide2" class="btn btn-circle">❮</a>
      <a href="#slide4" class="btn btn-circle">❯</a>
    </div>
  </div>
  <div id="slide4" class="carousel-item relative w-full">
    <img
      src="https://img.daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.webp"
      class="w-full" />
    <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
      <a href="#slide3" class="btn btn-circle">❮</a>
      <a href="#slide1" class="btn btn-circle">❯</a>
    </div>
  </div>
</div>
```



