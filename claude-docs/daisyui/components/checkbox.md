# Checkbox

Checkboxes are used to select or deselect a value.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| checkbox | Component | Checkbox |
| checkbox-primary | Color | primary color |
| checkbox-secondary | Color | secondary color |
| checkbox-accent | Color | accent color |
| checkbox-neutral | Color | neutral color |
| checkbox-success | Color | success color |
| checkbox-warning | Color | warning color |
| checkbox-info | Color | info color |
| checkbox-error | Color | error color |
| checkbox-xs | Size | Extra small size |
| checkbox-sm | Size | Small size |
| checkbox-md | Size | Medium size[Default] |
| checkbox-lg | Size | Large size |
| checkbox-xl | Size | Extra large size |

## HTML Examples

### Checkbox

```html
<input type="checkbox" checked="checked" class="checkbox" />
```

### With fieldset and label

```html
<fieldset class="fieldset bg-base-100 border-base-300 rounded-box w-64 border p-4">
  <legend class="fieldset-legend">Login options</legend>
  <label class="label">
    <input type="checkbox" checked="checked" class="checkbox" />
    Remember me
  </label>
</fieldset>
```

### Sizes

```html
<input type="checkbox" checked="checked" class="checkbox checkbox-xs" />
<input type="checkbox" checked="checked" class="checkbox checkbox-sm" />
<input type="checkbox" checked="checked" class="checkbox checkbox-md" />
<input type="checkbox" checked="checked" class="checkbox checkbox-lg" />
<input type="checkbox" checked="checked" class="checkbox checkbox-xl" />
```

### Colors

```html
<input type="checkbox" checked="checked" class="checkbox checkbox-primary" />
<input type="checkbox" checked="checked" class="checkbox checkbox-secondary" />
<input type="checkbox" checked="checked" class="checkbox checkbox-accent" />
<input type="checkbox" checked="checked" class="checkbox checkbox-neutral" />
<input type="checkbox" checked="checked" class="checkbox checkbox-info" />
<input type="checkbox" checked="checked" class="checkbox checkbox-success" />
<input type="checkbox" checked="checked" class="checkbox checkbox-warning" />
<input type="checkbox" checked="checked" class="checkbox checkbox-error" />
```

### Disabled

```html
<input type="checkbox" class="checkbox" disabled />
<input type="checkbox" class="checkbox" disabled checked="checked" />
```

### Indeterminate

```html
<!-- You can make a checkbox indeterminate using JS -->
<script>
  document.getElementById("my-checkbox").indeterminate = true
</script>
<input type="checkbox" class="checkbox" id="my-checkbox" />
```

### Checkbox with custom colors

```html
<input
  type="checkbox"
  checked="checked"
  class="checkbox border-indigo-600 bg-indigo-500 checked:border-orange-500 checked:bg-orange-400 checked:text-orange-800"
/>
```

