# Textarea

Textarea allows users to enter text in multiple lines.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| textarea | Component | For <textarea> element |
| textarea-ghost | Style | ghost style |
| textarea-neutral | Color | neutral color |
| textarea-primary | Color | primary color |
| textarea-secondary | Color | secondary color |
| textarea-accent | Color | accent color |
| textarea-info | Color | info color |
| textarea-success | Color | success color |
| textarea-warning | Color | warning color |
| textarea-error | Color | error color |
| textarea-xs | Size | Extra small size |
| textarea-sm | Size | Small size |
| textarea-md | Size | Medium size[Default] |
| textarea-lg | Size | Large size |
| textarea-xl | Size | Extra large size |

## HTML Examples

### Textarea

```html
<textarea class="textarea" placeholder="Bio"></textarea>
```

### Ghost (no background)

```html
<textarea class="textarea textarea-ghost" placeholder="Bio"></textarea>
```

### With form control and labels

```html
<fieldset class="fieldset">
  <legend class="fieldset-legend">Your bio</legend>
  <textarea class="textarea h-24" placeholder="Bio"></textarea>
  <div class="label">Optional</div>
</fieldset>
```

### Textarea colors

```html
<textarea placeholder="Primary" class="textarea textarea-primary"></textarea>
<textarea placeholder="Secondary" class="textarea textarea-secondary"></textarea>
<textarea placeholder="Accent" class="textarea textarea-accent"></textarea>
<textarea placeholder="Neutral" class="textarea textarea-neutral"></textarea>
<textarea placeholder="Info" class="textarea textarea-info"></textarea>
<textarea placeholder="Success" class="textarea textarea-success"></textarea>
<textarea placeholder="Warning" class="textarea textarea-warning"></textarea>
<textarea placeholder="Error" class="textarea textarea-error"></textarea>
```

### Sizes

```html
<textarea placeholder="Bio" class="textarea textarea-xs"></textarea>
<textarea placeholder="Bio" class="textarea textarea-sm"></textarea>
<textarea placeholder="Bio" class="textarea textarea-md"></textarea>
<textarea placeholder="Bio" class="textarea textarea-lg"></textarea>
<textarea placeholder="Bio" class="textarea textarea-xl"></textarea>
```

### Disabled

```html
<textarea class="textarea" placeholder="Bio" disabled></textarea>
```

