# Avatar

Avatars are used to show a thumbnail representation of an individual or business in the interface.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| avatar | Component | Avatar |
| avatar-group | Component | Container for multiple avatars |
| avatar-online | Modifier | shows a green dot as online indicator |
| avatar-offline | Modifier | shows a gray dot as offline indicator |
| avatar-placeholder | Modifier | To show letters as avatar placeholder |

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

