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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
    <div><img class="size-10 rounded-box" src="https://img.daisyui.com/images/profile/demo/[email protected]"/></div>
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
          <img src="https://img.daisyui.com/images/profile/demo/[email protected]" />
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







# Table

Table can be used to show a list of data in a table format.

## Component Details

| Class name     | Type      |                                                              |
| -------------- | --------- | ------------------------------------------------------------ |
| table          | Component | For <table> tag                                              |
| table-zebra    | Modifier  | For <table> to show zebra stripe rows                        |
| table-pin-rows | Modifier  | For <table> to make all the rows inside <thead> and <tfoot> sticky |
| table-pin-cols | Modifier  | For <table> to make all the <th> columns sticky              |
| table-xs       | Size      | Extra small size                                             |
| table-sm       | Size      | Small size                                                   |
| table-md       | Size      | Medium size[Default]                                         |
| table-lg       | Size      | Large size                                                   |
| table-xl       | Size      | Extra large size                                             |

## HTML Examples

### Table

```html
<div class="overflow-x-auto">
  <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Blue</td>
      </tr>
      <!-- row 2 -->
      <tr>
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Purple</td>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Red</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Table with border and background

```html
<div class="overflow-x-auto rounded-box border border-base-content/5 bg-base-100">
  <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Blue</td>
      </tr>
      <!-- row 2 -->
      <tr>
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Purple</td>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Red</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Table with an active row

```html
<div class="overflow-x-auto">
  <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr class="bg-base-200">
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Blue</td>
      </tr>
      <!-- row 2 -->
      <tr>
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Purple</td>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Red</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Table with a row that highlights on hover

```html
<div class="overflow-x-auto">
  <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Blue</td>
      </tr>
      <!-- row 2 -->
      <tr class="hover:bg-base-300">
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Purple</td>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Red</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Zebra

```html
<div class="overflow-x-auto">
  <table class="table table-zebra">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Blue</td>
      </tr>
      <!-- row 2 -->
      <tr>
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Purple</td>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Red</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Table with visual elements

```html
<div class="overflow-x-auto">
  <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th>
          <label>
            <input type="checkbox" class="checkbox" />
          </label>
        </th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr>
        <th>
          <label>
            <input type="checkbox" class="checkbox" />
          </label>
        </th>
        <td>
          <div class="flex items-center gap-3">
            <div class="avatar">
              <div class="mask mask-squircle h-12 w-12">
                <img
                  src="https://img.daisyui.com/images/profile/demo/[email protected]"
                  alt="Avatar Tailwind CSS Component" />
              </div>
            </div>
            <div>
              <div class="font-bold">Hart Hagerty</div>
              <div class="text-sm opacity-50">United States</div>
            </div>
          </div>
        </td>
        <td>
          Zemlak, Daniel and Leannon
          <br />
          <span class="badge badge-ghost badge-sm">Desktop Support Technician</span>
        </td>
        <td>Purple</td>
        <th>
          <button class="btn btn-ghost btn-xs">details</button>
        </th>
      </tr>
      <!-- row 2 -->
      <tr>
        <th>
          <label>
            <input type="checkbox" class="checkbox" />
          </label>
        </th>
        <td>
          <div class="flex items-center gap-3">
            <div class="avatar">
              <div class="mask mask-squircle h-12 w-12">
                <img
                  src="https://img.daisyui.com/images/profile/demo/[email protected]"
                  alt="Avatar Tailwind CSS Component" />
              </div>
            </div>
            <div>
              <div class="font-bold">Brice Swyre</div>
              <div class="text-sm opacity-50">China</div>
            </div>
          </div>
        </td>
        <td>
          Carroll Group
          <br />
          <span class="badge badge-ghost badge-sm">Tax Accountant</span>
        </td>
        <td>Red</td>
        <th>
          <button class="btn btn-ghost btn-xs">details</button>
        </th>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>
          <label>
            <input type="checkbox" class="checkbox" />
          </label>
        </th>
        <td>
          <div class="flex items-center gap-3">
            <div class="avatar">
              <div class="mask mask-squircle h-12 w-12">
                <img
                  src="https://img.daisyui.com/images/profile/demo/[email protected]"
                  alt="Avatar Tailwind CSS Component" />
              </div>
            </div>
            <div>
              <div class="font-bold">Marjy Ferencz</div>
              <div class="text-sm opacity-50">Russia</div>
            </div>
          </div>
        </td>
        <td>
          Rowe-Schoen
          <br />
          <span class="badge badge-ghost badge-sm">Office Assistant I</span>
        </td>
        <td>Crimson</td>
        <th>
          <button class="btn btn-ghost btn-xs">details</button>
        </th>
      </tr>
      <!-- row 4 -->
      <tr>
        <th>
          <label>
            <input type="checkbox" class="checkbox" />
          </label>
        </th>
        <td>
          <div class="flex items-center gap-3">
            <div class="avatar">
              <div class="mask mask-squircle h-12 w-12">
                <img
                  src="https://img.daisyui.com/images/profile/demo/[email protected]"
                  alt="Avatar Tailwind CSS Component" />
              </div>
            </div>
            <div>
              <div class="font-bold">Yancy Tear</div>
              <div class="text-sm opacity-50">Brazil</div>
            </div>
          </div>
        </td>
        <td>
          Wyman-Ledner
          <br />
          <span class="badge badge-ghost badge-sm">Community Outreach Specialist</span>
        </td>
        <td>Indigo</td>
        <th>
          <button class="btn btn-ghost btn-xs">details</button>
        </th>
      </tr>
    </tbody>
    <!-- foot -->
    <tfoot>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
        <th></th>
      </tr>
    </tfoot>
  </table>
</div>
```

### Table xs

```html
<div class="overflow-x-auto">
  <table class="table table-xs">
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>company</th>
        <th>location</th>
        <th>Last Login</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Littel, Schaden and Vandervort</td>
        <td>Canada</td>
        <td>12/16/2020</td>
        <td>Blue</td>
      </tr>
      <tr>
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Zemlak, Daniel and Leannon</td>
        <td>United States</td>
        <td>12/5/2020</td>
        <td>Purple</td>
      </tr>
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Carroll Group</td>
        <td>China</td>
        <td>8/15/2020</td>
        <td>Red</td>
      </tr>
      <tr>
        <th>4</th>
        <td>Marjy Ferencz</td>
        <td>Office Assistant I</td>
        <td>Rowe-Schoen</td>
        <td>Russia</td>
        <td>3/25/2021</td>
        <td>Crimson</td>
      </tr>
      <tr>
        <th>5</th>
        <td>Yancy Tear</td>
        <td>Community Outreach Specialist</td>
        <td>Wyman-Ledner</td>
        <td>Brazil</td>
        <td>5/22/2020</td>
        <td>Indigo</td>
      </tr>
      <tr>
        <th>6</th>
        <td>Irma Vasilik</td>
        <td>Editor</td>
        <td>Wiza, Bins and Emard</td>
        <td>Venezuela</td>
        <td>12/8/2020</td>
        <td>Purple</td>
      </tr>
      <tr>
        <th>7</th>
        <td>Meghann Durtnal</td>
        <td>Staff Accountant IV</td>
        <td>Schuster-Schimmel</td>
        <td>Philippines</td>
        <td>2/17/2021</td>
        <td>Yellow</td>
      </tr>
      <tr>
        <th>8</th>
        <td>Sammy Seston</td>
        <td>Accountant I</td>
        <td>O'Hara, Welch and Keebler</td>
        <td>Indonesia</td>
        <td>5/23/2020</td>
        <td>Crimson</td>
      </tr>
      <tr>
        <th>9</th>
        <td>Lesya Tinham</td>
        <td>Safety Technician IV</td>
        <td>Turner-Kuhlman</td>
        <td>Philippines</td>
        <td>2/21/2021</td>
        <td>Maroon</td>
      </tr>
      <tr>
        <th>10</th>
        <td>Zaneta Tewkesbury</td>
        <td>VP Marketing</td>
        <td>Sauer LLC</td>
        <td>Chad</td>
        <td>6/23/2020</td>
        <td>Green</td>
      </tr>
      <tr>
        <th>11</th>
        <td>Andy Tipple</td>
        <td>Librarian</td>
        <td>Hilpert Group</td>
        <td>Poland</td>
        <td>7/9/2020</td>
        <td>Indigo</td>
      </tr>
      <tr>
        <th>12</th>
        <td>Sophi Biles</td>
        <td>Recruiting Manager</td>
        <td>Gutmann Inc</td>
        <td>Indonesia</td>
        <td>2/12/2021</td>
        <td>Maroon</td>
      </tr>
      <tr>
        <th>13</th>
        <td>Florida Garces</td>
        <td>Web Developer IV</td>
        <td>Gaylord, Pacocha and Baumbach</td>
        <td>Poland</td>
        <td>5/31/2020</td>
        <td>Purple</td>
      </tr>
      <tr>
        <th>14</th>
        <td>Maribeth Popping</td>
        <td>Analyst Programmer</td>
        <td>Deckow-Pouros</td>
        <td>Portugal</td>
        <td>4/27/2021</td>
        <td>Aquamarine</td>
      </tr>
      <tr>
        <th>15</th>
        <td>Moritz Dryburgh</td>
        <td>Dental Hygienist</td>
        <td>Schiller, Cole and Hackett</td>
        <td>Sri Lanka</td>
        <td>8/8/2020</td>
        <td>Crimson</td>
      </tr>
      <tr>
        <th>16</th>
        <td>Reid Semiras</td>
        <td>Teacher</td>
        <td>Sporer, Sipes and Rogahn</td>
        <td>Poland</td>
        <td>7/30/2020</td>
        <td>Green</td>
      </tr>
      <tr>
        <th>17</th>
        <td>Alec Lethby</td>
        <td>Teacher</td>
        <td>Reichel, Glover and Hamill</td>
        <td>China</td>
        <td>2/28/2021</td>
        <td>Khaki</td>
      </tr>
      <tr>
        <th>18</th>
        <td>Aland Wilber</td>
        <td>Quality Control Specialist</td>
        <td>Kshlerin, Rogahn and Swaniawski</td>
        <td>Czech Republic</td>
        <td>9/29/2020</td>
        <td>Purple</td>
      </tr>
      <tr>
        <th>19</th>
        <td>Teddie Duerden</td>
        <td>Staff Accountant III</td>
        <td>Pouros, Ullrich and Windler</td>
        <td>France</td>
        <td>10/27/2020</td>
        <td>Aquamarine</td>
      </tr>
      <tr>
        <th>20</th>
        <td>Lorelei Blackstone</td>
        <td>Data Coordiator</td>
        <td>Witting, Kutch and Greenfelder</td>
        <td>Kazakhstan</td>
        <td>6/3/2020</td>
        <td>Red</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>company</th>
        <th>location</th>
        <th>Last Login</th>
        <th>Favorite Color</th>
      </tr>
    </tfoot>
  </table>
</div>
```

### Table with pinned-rows

```html
<div class="h-96 overflow-x-auto">
  <table class="table table-pin-rows bg-base-200">
    <thead>
      <tr>
        <th>A</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Ant-Man</td></tr>
      <tr><td>Aquaman</td></tr>
      <tr><td>Asterix</td></tr>
      <tr><td>The Atom</td></tr>
      <tr><td>The Avengers</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>B</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Batgirl</td></tr>
      <tr><td>Batman</td></tr>
      <tr><td>Batwoman</td></tr>
      <tr><td>Black Canary</td></tr>
      <tr><td>Black Panther</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>C</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Captain America</td></tr>
      <tr><td>Captain Marvel</td></tr>
      <tr><td>Catwoman</td></tr>
      <tr><td>Conan the Barbarian</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>D</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Daredevil</td></tr>
      <tr><td>The Defenders</td></tr>
      <tr><td>Doc Savage</td></tr>
      <tr><td>Doctor Strange</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>E</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Elektra</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>F</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Fantastic Four</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>G</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Ghost Rider</td></tr>
      <tr><td>Green Arrow</td></tr>
      <tr><td>Green Lantern</td></tr>
      <tr><td>Guardians of the Galaxy</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>H</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Hawkeye</td></tr>
      <tr><td>Hellboy</td></tr>
      <tr><td>Incredible Hulk</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>I</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Iron Fist</td></tr>
      <tr><td>Iron Man</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>M</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Marvelman</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>R</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Robin</td></tr>
      <tr><td>The Rocketeer</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>S</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>The Shadow</td></tr>
      <tr><td>Spider-Man</td></tr>
      <tr><td>Sub-Mariner</td></tr>
      <tr><td>Supergirl</td></tr>
      <tr><td>Superman</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>T</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Teenage Mutant Ninja Turtles</td></tr>
      <tr><td>Thor</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>W</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>The Wasp</td></tr>
      <tr><td>Watchmen</td></tr>
      <tr><td>Wolverine</td></tr>
      <tr><td>Wonder Woman</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>X</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>X-Men</td></tr>
    </tbody>
    <thead>
      <tr>
        <th>Z</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Zatanna</td></tr>
      <tr><td>Zatara</td></tr>
    </tbody>
  </table>
</div>
```

### Table with pinned-rows and pinned-cols

```html
<div class="overflow-x-auto">
  <table class="table table-xs table-pin-rows table-pin-cols">
    <thead>
      <tr>
        <th></th>
        <td>Name</td>
        <td>Job</td>
        <td>company</td>
        <td>location</td>
        <td>Last Login</td>
        <td>Favorite Color</td>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Littel, Schaden and Vandervort</td>
        <td>Canada</td>
        <td>12/16/2020</td>
        <td>Blue</td>
        <th>1</th>
      </tr>
      <tr>
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Zemlak, Daniel and Leannon</td>
        <td>United States</td>
        <td>12/5/2020</td>
        <td>Purple</td>
        <th>2</th>
      </tr>
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Carroll Group</td>
        <td>China</td>
        <td>8/15/2020</td>
        <td>Red</td>
        <th>3</th>
      </tr>
      <tr>
        <th>4</th>
        <td>Marjy Ferencz</td>
        <td>Office Assistant I</td>
        <td>Rowe-Schoen</td>
        <td>Russia</td>
        <td>3/25/2021</td>
        <td>Crimson</td>
        <th>4</th>
      </tr>
      <tr>
        <th>5</th>
        <td>Yancy Tear</td>
        <td>Community Outreach Specialist</td>
        <td>Wyman-Ledner</td>
        <td>Brazil</td>
        <td>5/22/2020</td>
        <td>Indigo</td>
        <th>5</th>
      </tr>
      <tr>
        <th>6</th>
        <td>Irma Vasilik</td>
        <td>Editor</td>
        <td>Wiza, Bins and Emard</td>
        <td>Venezuela</td>
        <td>12/8/2020</td>
        <td>Purple</td>
        <th>6</th>
      </tr>
      <tr>
        <th>7</th>
        <td>Meghann Durtnal</td>
        <td>Staff Accountant IV</td>
        <td>Schuster-Schimmel</td>
        <td>Philippines</td>
        <td>2/17/2021</td>
        <td>Yellow</td>
        <th>7</th>
      </tr>
      <tr>
        <th>8</th>
        <td>Sammy Seston</td>
        <td>Accountant I</td>
        <td>O'Hara, Welch and Keebler</td>
        <td>Indonesia</td>
        <td>5/23/2020</td>
        <td>Crimson</td>
        <th>8</th>
      </tr>
      <tr>
        <th>9</th>
        <td>Lesya Tinham</td>
        <td>Safety Technician IV</td>
        <td>Turner-Kuhlman</td>
        <td>Philippines</td>
        <td>2/21/2021</td>
        <td>Maroon</td>
        <th>9</th>
      </tr>
      <tr>
        <th>10</th>
        <td>Zaneta Tewkesbury</td>
        <td>VP Marketing</td>
        <td>Sauer LLC</td>
        <td>Chad</td>
        <td>6/23/2020</td>
        <td>Green</td>
        <th>10</th>
      </tr>
      <tr>
        <th>11</th>
        <td>Andy Tipple</td>
        <td>Librarian</td>
        <td>Hilpert Group</td>
        <td>Poland</td>
        <td>7/9/2020</td>
        <td>Indigo</td>
        <th>11</th>
      </tr>
      <tr>
        <th>12</th>
        <td>Sophi Biles</td>
        <td>Recruiting Manager</td>
        <td>Gutmann Inc</td>
        <td>Indonesia</td>
        <td>2/12/2021</td>
        <td>Maroon</td>
        <th>12</th>
      </tr>
      <tr>
        <th>13</th>
        <td>Florida Garces</td>
        <td>Web Developer IV</td>
        <td>Gaylord, Pacocha and Baumbach</td>
        <td>Poland</td>
        <td>5/31/2020</td>
        <td>Purple</td>
        <th>13</th>
      </tr>
      <tr>
        <th>14</th>
        <td>Maribeth Popping</td>
        <td>Analyst Programmer</td>
        <td>Deckow-Pouros</td>
        <td>Portugal</td>
        <td>4/27/2021</td>
        <td>Aquamarine</td>
        <th>14</th>
      </tr>
      <tr>
        <th>15</th>
        <td>Moritz Dryburgh</td>
        <td>Dental Hygienist</td>
        <td>Schiller, Cole and Hackett</td>
        <td>Sri Lanka</td>
        <td>8/8/2020</td>
        <td>Crimson</td>
        <th>15</th>
      </tr>
      <tr>
        <th>16</th>
        <td>Reid Semiras</td>
        <td>Teacher</td>
        <td>Sporer, Sipes and Rogahn</td>
        <td>Poland</td>
        <td>7/30/2020</td>
        <td>Green</td>
        <th>16</th>
      </tr>
      <tr>
        <th>17</th>
        <td>Alec Lethby</td>
        <td>Teacher</td>
        <td>Reichel, Glover and Hamill</td>
        <td>China</td>
        <td>2/28/2021</td>
        <td>Khaki</td>
        <th>17</th>
      </tr>
      <tr>
        <th>18</th>
        <td>Aland Wilber</td>
        <td>Quality Control Specialist</td>
        <td>Kshlerin, Rogahn and Swaniawski</td>
        <td>Czech Republic</td>
        <td>9/29/2020</td>
        <td>Purple</td>
        <th>18</th>
      </tr>
      <tr>
        <th>19</th>
        <td>Teddie Duerden</td>
        <td>Staff Accountant III</td>
        <td>Pouros, Ullrich and Windler</td>
        <td>France</td>
        <td>10/27/2020</td>
        <td>Aquamarine</td>
        <th>19</th>
      </tr>
      <tr>
        <th>20</th>
        <td>Lorelei Blackstone</td>
        <td>Data Coordinator</td>
        <td>Witting, Kutch and Greenfelder</td>
        <td>Kazakhstan</td>
        <td>6/3/2020</td>
        <td>Red</td>
        <th>20</th>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <th></th>
        <td>Name</td>
        <td>Job</td>
        <td>company</td>
        <td>location</td>
        <td>Last Login</td>
        <td>Favorite Color</td>
        <th></th>
      </tr>
    </tfoot>
  </table>
</div>
```





# Timeline

Timeline component shows a list of events in chronological order.

## Component Details

| Class name          | Type      |                                                             |
| ------------------- | --------- | ----------------------------------------------------------- |
| timeline            | Component | Timeline container                                          |
| timeline-start      | Part      | The content inside <li> that will be at the start direction |
| timeline-middle     | Part      | The content inside <li> that will be at the middle          |
| timeline-end        | Part      | The content inside <li> that will be at the end direction   |
| timeline-snap-icon  | Modifier  | snaps the icon to the start instead of middle               |
| timeline-box        | Modifier  | Applies a box style to timeline-start or timeline-end       |
| timeline-compact    | Modifier  | forces all items on one side                                |
| timeline-horizontal | direction | horizontal layout (default)                                 |
| timeline-vertical   | direction | vertical layout                                             |

## HTML Examples

### Timeline with text on both sides and icon

```html
<ul class="timeline">
  <li>
    <div class="timeline-start">1984</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">First Macintosh computer</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">1998</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2001</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPod</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2007</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2015</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">Apple Watch</div>
  </li>
</ul>
```

### Timeline with bottom side only

```html
<ul class="timeline">
  <li>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">First Macintosh computer</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPod</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">Apple Watch</div>
  </li>
</ul>
```

### Timeline with top side only

```html
<ul class="timeline">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iMac</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPod</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPhone</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
  </li>
</ul>
```

### Timeline with different sides

```html
<ul class="timeline">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPod</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
  </li>
</ul>
```

### Timeline with colorful lines

```html
<ul class="timeline">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="text-primary h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr class="bg-primary" />
  </li>
  <li>
    <hr class="bg-primary" />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="text-primary h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr class="bg-primary" />
  </li>
  <li>
    <hr class="bg-primary" />
    <div class="timeline-start timeline-box">iPod</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="text-primary h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
  </li>
</ul>
```

### Timeline without icons

```html
<ul class="timeline">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPod</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
  </li>
</ul>
```

### Vertical timeline with text on both sides and icon

```html
<ul class="timeline timeline-vertical">
  <li>
    <div class="timeline-start">1984</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">First Macintosh computer</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">1998</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2001</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPod</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2007</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2015</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">Apple Watch</div>
  </li>
</ul>
```

### Vertical timeline with right side only

```html
<ul class="timeline timeline-vertical">
  <li>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">First Macintosh computer</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPod</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">Apple Watch</div>
  </li>
</ul>
```

### Vertical timeline with left side only

```html
<ul class="timeline timeline-vertical">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iMac</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPod</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPhone</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
  </li>
</ul>
```

### Vertical timeline with different sides

```html
<ul class="timeline timeline-vertical">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPod</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
  </li>
</ul>
```

### Vertical timeline with colorful lines

```html
<ul class="timeline timeline-vertical">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="text-primary h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr class="bg-primary" />
  </li>
  <li>
    <hr class="bg-primary" />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="text-primary h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr class="bg-primary" />
  </li>
  <li>
    <hr class="bg-primary" />
    <div class="timeline-start timeline-box">iPod</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="text-primary h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
  </li>
</ul>
```

### Vertical timeline without icons

```html
<ul class="timeline timeline-vertical">
  <li>
    <div class="timeline-start timeline-box">First Macintosh computer</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">iPod</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start timeline-box">Apple Watch</div>
  </li>
</ul>
```

### Responsive: vertical by default, horizontal on large screen

```html
<ul class="timeline timeline-vertical lg:timeline-horizontal">
  <li>
    <div class="timeline-start">1984</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">First Macintosh computer</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">1998</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iMac</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2001</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPod</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2007</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">iPhone</div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-start">2015</div>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end timeline-box">Apple Watch</div>
  </li>
</ul>
```

### Timeline with icon snapped to the start

```html
<ul class="timeline timeline-snap-icon max-md:timeline-compact timeline-vertical">
  <li>
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-start mb-10 md:text-end">
      <time class="font-mono italic">1984</time>
      <div class="text-lg font-black">First Macintosh computer</div>
      The Apple Macintosh—later rebranded as the Macintosh 128K—is the original Apple Macintosh
      personal computer. It played a pivotal role in establishing desktop publishing as a general
      office function. The motherboard, a 9 in (23 cm) CRT monitor, and a floppy drive were housed
      in a beige case with integrated carrying handle; it came with a keyboard and single-button
      mouse.
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end md:mb-10">
      <time class="font-mono italic">1998</time>
      <div class="text-lg font-black">iMac</div>
      iMac is a family of all-in-one Mac desktop computers designed and built by Apple Inc. It has
      been the primary part of Apple's consumer desktop offerings since its debut in August 1998,
      and has evolved through seven distinct forms
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-start mb-10 md:text-end">
      <time class="font-mono italic">2001</time>
      <div class="text-lg font-black">iPod</div>
      The iPod is a discontinued series of portable media players and multi-purpose mobile devices
      designed and marketed by Apple Inc. The first version was released on October 23, 2001, about
      8+1⁄2 months after the Macintosh version of iTunes was released. Apple sold an estimated 450
      million iPod products as of 2022. Apple discontinued the iPod product line on May 10, 2022. At
      over 20 years, the iPod brand is the oldest to be discontinued by Apple
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-end md:mb-10">
      <time class="font-mono italic">2007</time>
      <div class="text-lg font-black">iPhone</div>
      iPhone is a line of smartphones produced by Apple Inc. that use Apple's own iOS mobile
      operating system. The first-generation iPhone was announced by then-Apple CEO Steve Jobs on
      January 9, 2007. Since then, Apple has annually released new iPhone models and iOS updates. As
      of November 1, 2018, more than 2.2 billion iPhones had been sold. As of 2022, the iPhone
      accounts for 15.6% of global smartphone market share
    </div>
    <hr />
  </li>
  <li>
    <hr />
    <div class="timeline-middle">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
        fill="currentColor"
        class="h-5 w-5"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
          clip-rule="evenodd"
        />
      </svg>
    </div>
    <div class="timeline-start mb-10 md:text-end">
      <time class="font-mono italic">2015</time>
      <div class="text-lg font-black">Apple Watch</div>
      The Apple Watch is a line of smartwatches produced by Apple Inc. It incorporates fitness
      tracking, health-oriented capabilities, and wireless telecommunication, and integrates with
      iOS and other Apple products and services
    </div>
  </li>
</ul>
```

