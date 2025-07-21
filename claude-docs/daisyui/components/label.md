# Label

Label is used to provide a name or title for an input field. Label can be placed before or after the field.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| label | Component | For styling the text next to an input field (or select) |
| floating-label | Component | For the parent of an input field (or select) and a span that floats above the input field when the field is focused |

## HTML Examples

### Label for input

```html
<label class="input">
  <span class="label">https://</span>
  <input type="text" placeholder="URL" />
</label>
```

### Label for input at the end

```html
<label class="input">
  <input type="text" placeholder="domain name" />
  <span class="label">.com</span>
</label>
```

### Label for select

```html
<label class="select">
  <span class="label">Type</span>
  <select>
    <option>Personal</option>
    <option>Business</option>
  </select>
</label>
```

### Label for date input

```html
<label class="input">
  <span class="label">Publish date</span>
  <input type="date" />
</label>
```

### Floating Label

```html
<label class="floating-label">
  <span>Your Email</span>
  <input type="text" placeholder="[email protected]" class="input input-md" />
</label>
```

### Floating Label with Different Sizes

```html
<label class="floating-label">
  <input type="text" placeholder="Extra Small" class="input input-xs" />
  <span>Extra Small</span>
</label>
<label class="floating-label">
  <input type="text" placeholder="Small" class="input input-sm" />
  <span>Small</span>
</label>
<label class="floating-label">
  <input type="text" placeholder="Medium" class="input input-md" />
  <span>Medium</span>
</label>
<label class="floating-label">
  <input type="text" placeholder="Large" class="input input-lg" />
  <span>Large</span>
</label>
<label class="floating-label">
  <input type="text" placeholder="Extra Large" class="input input-xl" />
  <span>Extra Large</span>
</label>
```

