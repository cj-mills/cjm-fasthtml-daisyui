### Data input

1. [Calendar](#calendar/)
2. [Checkbox](#checkbox/)
3. [Fieldset](#fieldset/)
4. [File Input](#file-input/)
5. [Filter](#filter/)
6. [Label](#label/)
7. [Radio](#radio/)
8. [Range](#range-slider/)
9. [Rating](#rating/)
10. [Select](#select/)
11. [Input field](#text-input/)
12. [Textarea](#textarea/)
13. [Toggle](#toggle/)
14. [Validator](#validator/)



# Calendar

Calendar includes styles for different calendar libraries.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| cally | Component | for Cally web component |
| pika-single | Component | for the input field that opens Pikaday calendar |
| react-day-picker | Component | for the DayPicker component |

## HTML Examples

### Cally calendar example

```html
<!--
* Import Cally web component from CDN
<script type="module" src="https://unpkg.com/cally"></script>
* Or install as a dependency:
npm i cally
* and import it in JS
import "cally";
-->
<calendar-date class="cally bg-base-100 border border-base-300 shadow-lg rounded-box">
  <svg aria-label="Previous" class="fill-current size-4" slot="previous" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="M15.75 19.5 8.25 12l7.5-7.5"></path></svg>
  <svg aria-label="Next" class="fill-current size-4" slot="next" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="currentColor" d="m8.25 4.5 7.5 7.5-7.5 7.5"></path></svg>
  <calendar-month></calendar-month>
</calendar-date>
```

### Cally date picker example

```html
<!--
* Import Cally web component from CDN
<script type="module" src="https://unpkg.com/cally"></script>
* Or install as a dependency:
npm i cally
* and import it in JS
import "cally";
-->
<button popovertarget="cally-popover1" class="input input-border" id="cally1" style="anchor-name:--cally1">
  Pick a date
</button>
<div popover id="cally-popover1" class="dropdown bg-base-100 rounded-box shadow-lg" style="position-anchor:--cally1">
  <calendar-date class="cally" onchange={document.getElementById('cally1').innerText = this.value}>
    <svg aria-label="Previous" class="fill-current size-4" slot="previous" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M15.75 19.5 8.25 12l7.5-7.5"></path></svg>
    <svg aria-label="Next" class="fill-current size-4" slot="next" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m8.25 4.5 7.5 7.5-7.5 7.5"></path></svg>
    <calendar-month></calendar-month>
  </calendar-date>
</div>
```



---



# Checkbox

Checkboxes are used to select or deselect a value.

## Component Details

| Class name         | Type      |                      |
| ------------------ | --------- | -------------------- |
| checkbox           | Component | Checkbox             |
| checkbox-primary   | Color     | primary color        |
| checkbox-secondary | Color     | secondary color      |
| checkbox-accent    | Color     | accent color         |
| checkbox-neutral   | Color     | neutral color        |
| checkbox-success   | Color     | success color        |
| checkbox-warning   | Color     | warning color        |
| checkbox-info      | Color     | info color           |
| checkbox-error     | Color     | error color          |
| checkbox-xs        | Size      | Extra small size     |
| checkbox-sm        | Size      | Small size           |
| checkbox-md        | Size      | Medium size[Default] |
| checkbox-lg        | Size      | Large size           |
| checkbox-xl        | Size      | Extra large size     |

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





----



# Fieldset

Fieldset is a container for grouping related form elements. It includes fieldset-legend as a title and label as a description.

## Component Details

| Class name      | Type      |                               |
| --------------- | --------- | ----------------------------- |
| fieldset        | Component | for the fieldset container    |
| label           | Component | label for inputs              |
| fieldset-legend | Part      | for the title of the fieldset |

## HTML Examples

### Fieldset fieldset-legend and label

```html
<fieldset class="fieldset">
  <legend class="fieldset-legend">Page title</legend>
  <input type="text" class="input" placeholder="My awesome page" />
  <p class="label">You can edit page title later on from settings</p>
</fieldset>
```

### Fieldset with background and border

```html
<fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
  <legend class="fieldset-legend">Page title</legend>
  <input type="text" class="input" placeholder="My awesome page" />
  <p class="label">You can edit page title later on from settings</p>
</fieldset>
```

### Fieldset with multiple inputs

```html
<fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
  <legend class="fieldset-legend">Page details</legend>
  <label class="label">Title</label>
  <input type="text" class="input" placeholder="My awesome page" />
  <label class="label">Slug</label>
  <input type="text" class="input" placeholder="my-awesome-page" />
  <label class="label">Author</label>
  <input type="text" class="input" placeholder="Name" />
</fieldset>
```

### Fieldset with multiple join items

```html
<fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
  <legend class="fieldset-legend">Settings</legend>
  <div class="join">
    <input type="text" class="input join-item" placeholder="Product name" />
    <button class="btn join-item">save</button>
  </div>
</fieldset>
```

### Login form with fieldset

```html
<fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
  <legend class="fieldset-legend">Login</legend>
  <label class="label">Email</label>
  <input type="email" class="input" placeholder="Email" />
  <label class="label">Password</label>
  <input type="password" class="input" placeholder="Password" />
  <button class="btn btn-neutral mt-4">Login</button>
</fieldset>
```





---



# File Input

File Input is a an input field for uploading files.

## Component Details

| Class name           | Type      |                                 |
| -------------------- | --------- | ------------------------------- |
| file-input           | Component | For <input type="file"> element |
| file-input-ghost     | Style     | ghost style                     |
| file-input-neutral   | Color     | neutral color                   |
| file-input-primary   | Color     | primary color                   |
| file-input-secondary | Color     | secondary color                 |
| file-input-accent    | Color     | accent color                    |
| file-input-info      | Color     | info color                      |
| file-input-success   | Color     | success color                   |
| file-input-warning   | Color     | warning color                   |
| file-input-error     | Color     | error color                     |
| file-input-xs        | Size      | Extra small size                |
| file-input-sm        | Size      | Small size                      |
| file-input-md        | Size      | Medium size[Default]            |
| file-input-lg        | Size      | Large size                      |
| file-input-xl        | Size      | Extra large size                |

## HTML Examples

### File input

```html
<input type="file" class="file-input" />
```

### File input ghost

```html
<input type="file" class="file-input file-input-ghost" />
```

### With fieldset and label

```html
<fieldset class="fieldset">
  <legend class="fieldset-legend">Pick a file</legend>
  <input type="file" class="file-input" />
  <label class="label">Max size 2MB</label>
</fieldset>
```

### Sizes

```html
<input type="file" class="file-input file-input-xs" />
<input type="file" class="file-input file-input-sm" />
<input type="file" class="file-input file-input-md" />
<input type="file" class="file-input file-input-lg" />
<input type="file" class="file-input file-input-xl" />
```

### Primary color

```html
<input type="file" class="file-input file-input-primary" />
<input type="file" class="file-input file-input-secondary" />
<input type="file" class="file-input file-input-accent" />
<input type="file" class="file-input file-input-neutral" />
<input type="file" class="file-input file-input-info" />
<input type="file" class="file-input file-input-success" />
<input type="file" class="file-input file-input-warning" />
<input type="file" class="file-input file-input-error" />
```

### Disabled

```html
<input type="file" placeholder="You can't touch this" class="file-input" disabled />
```





---



# Filter

Filter is a group of radio buttons. Choosing one of the options will hide the others and shows a reset button next to the chosen option.

## Component Details

| Class name   | Type      |                                                              |
| ------------ | --------- | ------------------------------------------------------------ |
| filter       | Component | For a HTML <form> or a <div> element that includes radio buttons for filtering items |
| filter-reset | Part      | An alternative to the reset button if you can't use a HTML form |

## HTML Examples

### Filter using HTML form, radio buttons and reset button

```html
<form class="filter">
  <input class="btn btn-square" type="reset" value="×"/>
  <input class="btn" type="radio" name="frameworks" aria-label="Svelte"/>
  <input class="btn" type="radio" name="frameworks" aria-label="Vue"/>
  <input class="btn" type="radio" name="frameworks" aria-label="React"/>
</form>
```

### Filter without HTML form

```html
<div class="filter">
  <input class="btn filter-reset" type="radio" name="metaframeworks" aria-label="All"/>
  <input class="btn" type="radio" name="metaframeworks" aria-label="Sveltekit"/>
  <input class="btn" type="radio" name="metaframeworks" aria-label="Nuxt"/>
  <input class="btn" type="radio" name="metaframeworks" aria-label="Next.js"/>
</div>
```





---



# Label

Label is used to provide a name or title for an input field. Label can be placed before or after the field.

## Component Details

| Class name     | Type      |                                                              |
| -------------- | --------- | ------------------------------------------------------------ |
| label          | Component | For styling the text next to an input field (or select)      |
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





---



# Radio

Radio buttons allow the user to select one option from a set.

## Component Details

| Class name      | Type      |                      |
| --------------- | --------- | -------------------- |
| radio           | Component | For radio input      |
| radio-neutral   | Color     | neutral color        |
| radio-primary   | Color     | primary color        |
| radio-secondary | Color     | secondary color      |
| radio-accent    | Color     | accent color         |
| radio-success   | Color     | success color        |
| radio-warning   | Color     | warning color        |
| radio-info      | Color     | info color           |
| radio-error     | Color     | error color          |
| radio-xs        | Size      | Extra small size     |
| radio-sm        | Size      | Small size           |
| radio-md        | Size      | Medium size[Default] |
| radio-lg        | Size      | Large size           |
| radio-xl        | Size      | Extra large size     |

## HTML Examples

### Radio

```html
<input type="radio" name="radio-1" class="radio" checked="checked" />
<input type="radio" name="radio-1" class="radio" />
```

### Radio sizes

```html
<input type="radio" name="radio-2" class="radio radio-xs" checked="checked" />
<input type="radio" name="radio-2" class="radio radio-sm" checked="checked" />
<input type="radio" name="radio-2" class="radio radio-md" checked="checked" />
<input type="radio" name="radio-2" class="radio radio-lg" checked="checked" />
<input type="radio" name="radio-2" class="radio radio-xl" checked="checked" />
```

### Neutral color

```html
<input type="radio" name="radio-3" class="radio radio-neutral" checked="checked" />
<input type="radio" name="radio-3" class="radio radio-neutral" />
```

### Primary color

```html
<input type="radio" name="radio-4" class="radio radio-primary" checked="checked" />
<input type="radio" name="radio-4" class="radio radio-primary" />
```

### Secondary color

```html
<input type="radio" name="radio-5" class="radio radio-secondary" checked="checked" />
<input type="radio" name="radio-5" class="radio radio-secondary" />
```

### Accent color

```html
<input type="radio" name="radio-6" class="radio radio-accent" checked="checked" />
<input type="radio" name="radio-6" class="radio radio-accent" />
```

### Success color

```html
<input type="radio" name="radio-7" class="radio radio-success" checked="checked" />
<input type="radio" name="radio-7" class="radio radio-success" />
```

### Warning color

```html
<input type="radio" name="radio-8" class="radio radio-warning" checked="checked" />
<input type="radio" name="radio-8" class="radio radio-warning" />
```

### Info color

```html
<input type="radio" name="radio-9" class="radio radio-info" checked="checked" />
<input type="radio" name="radio-9" class="radio radio-info" />
```

### Error color

```html
<input type="radio" name="radio-10" class="radio radio-error" checked="checked" />
<input type="radio" name="radio-10" class="radio radio-error" />
```

### Disabled

```html
<input type="radio" name="radio-11" class="radio" disabled checked="checked" />
<input type="radio" name="radio-11" class="radio" disabled />
```

### Radio with custom colors

```html
<input
  type="radio" name="radio-12" checked="checked"
  class="radio bg-red-100 border-red-300 checked:bg-red-200 checked:text-red-600 checked:border-red-600" />
<input
  type="radio" name="radio-12" checked="checked"
  class="radio bg-blue-100 border-blue-300 checked:bg-blue-200 checked:text-blue-600 checked:border-blue-600" />
```





---





# Range slider

Range slider is used to select a value by sliding a handle.

## Component Details

| Class name      | Type      |                              |
| --------------- | --------- | ---------------------------- |
| range           | Component | For <input type="range"> tag |
| range-neutral   | Color     | neutral color                |
| range-primary   | Color     | primary color                |
| range-secondary | Color     | secondary color              |
| range-accent    | Color     | accent color                 |
| range-success   | Color     | success color                |
| range-warning   | Color     | warning color                |
| range-info      | Color     | info color                   |
| range-error     | Color     | error color                  |
| range-xs        | Size      | Extra small size             |
| range-sm        | Size      | Small size                   |
| range-md        | Size      | Medium size[Default]         |
| range-lg        | Size      | Large size                   |
| range-xl        | Size      | Extra large size             |

## HTML Examples

### Range

```html
<input type="range" min="0" max="100" value="40" class="range" />
```

### With steps and measure

```html
<div class="w-full max-w-xs">
  <input type="range" min="0" max="100" value="25" class="range" step="25" />
  <div class="flex justify-between px-2.5 mt-2 text-xs">
    <span>|</span>
    <span>|</span>
    <span>|</span>
    <span>|</span>
    <span>|</span>
  </div>
  <div class="flex justify-between px-2.5 mt-2 text-xs">
    <span>1</span>
    <span>2</span>
    <span>3</span>
    <span>4</span>
    <span>5</span>
  </div>
</div>
```

### Neutral color

```html
<input type="range" min="0" max="100" value="40" class="range range-neutral" />
```

### Primary color

```html
<input type="range" min="0" max="100" value="40" class="range range-primary" />
```

### Secondary color

```html
<input type="range" min="0" max="100" value="40" class="range range-secondary" />
```

### Accent color

```html
<input type="range" min="0" max="100" value="40" class="range range-accent" />
```

### Success color

```html
<input type="range" min="0" max="100" value="40" class="range range-success" />
```

### Warning color

```html
<input type="range" min="0" max="100" value="40" class="range range-warning" />
```

### Info color

```html
<input type="range" min="0" max="100" value="40" class="range range-info" />
```

### Error color

```html
<input type="range" min="0" max="100" value="40" class="range range-error" />
```

### Sizes

```html
<input type="range" min="0" max="100" value="30" class="range range-xs" />
<input type="range" min="0" max="100" value="40" class="range range-sm" />
<input type="range" min="0" max="100" value="50" class="range range-md" />
<input type="range" min="0" max="100" value="60" class="range range-lg" />
<input type="range" min="0" max="100" value="70" class="range range-xl" />
```

### Range with custom color and no fill

```html
<input type="range" min="0" max="100" value="40" 
  class="range text-blue-300 [--range-bg:orange] [--range-thumb:blue] [--range-fill:0]" />
```





---



# Rating

Rating is a set of radio buttons that allow the user to rate something.

## Component Details

| Class name    | Type      |                                                              |
| ------------- | --------- | ------------------------------------------------------------ |
| rating        | Component | For a div containing radio inputs                            |
| rating-half   | Modifier  | To shows half of the shapes. Useful for half star ratings    |
| rating-hidden | Modifier  | For the first radio to make it hidden so user can clear the rating |
| rating-xs     | Size      | Extra small size                                             |
| rating-sm     | Size      | Small size                                                   |
| rating-md     | Size      | Medium size[Default]                                         |
| rating-lg     | Size      | Large size                                                   |
| rating-xl     | Size      | Extra large size                                             |

## HTML Examples

### Rating

```html
<div class="rating">
  <input type="radio" name="rating-1" class="mask mask-star" aria-label="1 star" />
  <input type="radio" name="rating-1" class="mask mask-star" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-1" class="mask mask-star" aria-label="3 star" />
  <input type="radio" name="rating-1" class="mask mask-star" aria-label="4 star" />
  <input type="radio" name="rating-1" class="mask mask-star" aria-label="5 star" />
</div>
```

### Read-only Rating

```html
<div class="rating">
  <div class="mask mask-star" aria-label="1 star"></div>
  <div class="mask mask-star" aria-label="2 star"></div>
  <div class="mask mask-star" aria-label="3 star" aria-current="true"></div>
  <div class="mask mask-star" aria-label="4 star"></div>
  <div class="mask mask-star" aria-label="5 star"></div>
</div>
```

### mask-star-2 with warning color

```html
<div class="rating">
  <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" aria-label="1 star" />
  <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" aria-label="3 star" />
  <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" aria-label="4 star" />
  <input type="radio" name="rating-2" class="mask mask-star-2 bg-orange-400" aria-label="5 star" />
</div>
```

### mask-heart with multiple colors

```html
<div class="rating gap-1">
  <input type="radio" name="rating-3" class="mask mask-heart bg-red-400" aria-label="1 star" />
  <input type="radio" name="rating-3" class="mask mask-heart bg-orange-400" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-3" class="mask mask-heart bg-yellow-400" aria-label="3 star" />
  <input type="radio" name="rating-3" class="mask mask-heart bg-lime-400" aria-label="4 star" />
  <input type="radio" name="rating-3" class="mask mask-heart bg-green-400" aria-label="5 star" />
</div>
```

### mask-star-2 with green-500 color

```html
<div class="rating">
  <input type="radio" name="rating-4" class="mask mask-star-2 bg-green-500" aria-label="1 star" />
  <input type="radio" name="rating-4" class="mask mask-star-2 bg-green-500" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-4" class="mask mask-star-2 bg-green-500" aria-label="3 star" />
  <input type="radio" name="rating-4" class="mask mask-star-2 bg-green-500" aria-label="4 star" />
  <input type="radio" name="rating-4" class="mask mask-star-2 bg-green-500" aria-label="5 star" />
</div>
```

### Sizes

```html
<!-- xs -->
<div class="rating rating-xs">
  <input type="radio" name="rating-5" class="mask mask-star-2 bg-orange-400" aria-label="1 star" />
  <input type="radio" name="rating-5" class="mask mask-star-2 bg-orange-400" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-5" class="mask mask-star-2 bg-orange-400" aria-label="3 star" />
  <input type="radio" name="rating-5" class="mask mask-star-2 bg-orange-400" aria-label="4 star" />
  <input type="radio" name="rating-5" class="mask mask-star-2 bg-orange-400" aria-label="5 star" />
</div>
<!-- sm -->
<div class="rating rating-sm">
  <input type="radio" name="rating-6" class="mask mask-star-2 bg-orange-400" aria-label="1 star" />
  <input type="radio" name="rating-6" class="mask mask-star-2 bg-orange-400" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-6" class="mask mask-star-2 bg-orange-400" aria-label="3 star" />
  <input type="radio" name="rating-6" class="mask mask-star-2 bg-orange-400" aria-label="4 star" />
  <input type="radio" name="rating-6" class="mask mask-star-2 bg-orange-400" aria-label="5 star" />
</div>
<!-- md -->
<div class="rating rating-md">
  <input type="radio" name="rating-7" class="mask mask-star-2 bg-orange-400" aria-label="1 star" />
  <input type="radio" name="rating-7" class="mask mask-star-2 bg-orange-400" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-7" class="mask mask-star-2 bg-orange-400" aria-label="3 star" />
  <input type="radio" name="rating-7" class="mask mask-star-2 bg-orange-400" aria-label="4 star" />
  <input type="radio" name="rating-7" class="mask mask-star-2 bg-orange-400" aria-label="5 star" />
</div>
<!-- lg -->
<div class="rating rating-lg">
  <input type="radio" name="rating-8" class="mask mask-star-2 bg-orange-400" aria-label="1 star" />
  <input type="radio" name="rating-8" class="mask mask-star-2 bg-orange-400" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-8" class="mask mask-star-2 bg-orange-400" aria-label="3 star" />
  <input type="radio" name="rating-8" class="mask mask-star-2 bg-orange-400" aria-label="4 star" />
  <input type="radio" name="rating-8" class="mask mask-star-2 bg-orange-400" aria-label="5 star" />
</div>
<!-- xl -->
<div class="rating rating-xl">
  <input type="radio" name="rating-9" class="mask mask-star-2 bg-orange-400" aria-label="1 star" />
  <input type="radio" name="rating-9" class="mask mask-star-2 bg-orange-400" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-9" class="mask mask-star-2 bg-orange-400" aria-label="3 star" />
  <input type="radio" name="rating-9" class="mask mask-star-2 bg-orange-400" aria-label="4 star" />
  <input type="radio" name="rating-9" class="mask mask-star-2 bg-orange-400" aria-label="5 star" />
</div>
```

### with

```html
<div class="rating rating-lg">
  <input type="radio" name="rating-10" class="rating-hidden" aria-label="clear" />
  <input type="radio" name="rating-10" class="mask mask-star-2" aria-label="1 star" />
  <input type="radio" name="rating-10" class="mask mask-star-2" aria-label="2 star" checked="checked" />
  <input type="radio" name="rating-10" class="mask mask-star-2" aria-label="3 star" />
  <input type="radio" name="rating-10" class="mask mask-star-2" aria-label="4 star" />
  <input type="radio" name="rating-10" class="mask mask-star-2" aria-label="5 star" />
</div>
```

### half stars

```html
<div class="rating rating-lg rating-half">
  <input type="radio" name="rating-11" class="rating-hidden" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-1 bg-green-500" aria-label="0.5 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-2 bg-green-500" aria-label="1 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-1 bg-green-500" aria-label="1.5 star" checked="checked" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-2 bg-green-500" aria-label="2 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-1 bg-green-500" aria-label="2.5 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-2 bg-green-500" aria-label="3 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-1 bg-green-500" aria-label="3.5 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-2 bg-green-500" aria-label="4 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-1 bg-green-500" aria-label="4.5 star" />
  <input type="radio" name="rating-11" class="mask mask-star-2 mask-half-2 bg-green-500" aria-label="5 star" />
</div>
```





---



# Select

Select is used to pick a value from a list of options.

## Component Details

| Class name       | Type      |                      |
| ---------------- | --------- | -------------------- |
| select           | Component | For <select> element |
| select-ghost     | Style     | ghost style          |
| select-neutral   | Color     | neutral color        |
| select-primary   | Color     | primary color        |
| select-secondary | Color     | secondary color      |
| select-accent    | Color     | accent color         |
| select-info      | Color     | info color           |
| select-success   | Color     | success color        |
| select-warning   | Color     | warning color        |
| select-error     | Color     | error color          |
| select-xs        | Size      | Extra small size     |
| select-sm        | Size      | Small size           |
| select-md        | Size      | Medium size[Default] |
| select-lg        | Size      | Large size           |
| select-xl        | Size      | Extra large size     |

## HTML Examples

### Select

```html
<select class="select">
  <option disabled selected>Pick a color</option>
  <option>Crimson</option>
  <option>Amber</option>
  <option>Velvet</option>
</select>
```

### Ghost (no background)

```html
<select class="select select-ghost">
  <option disabled selected>Pick a font</option>
  <option>Inter</option>
  <option>Poppins</option>
  <option>Raleway</option>
</select>
```

### With fieldset and labels

```html
<fieldset class="fieldset">
  <legend class="fieldset-legend">Browsers</legend>
  <select class="select">
    <option disabled selected>Pick a browser</option>
    <option>Chrome</option>
    <option>FireFox</option>
    <option>Safari</option>
  </select>
  <span class="label">Optional</span>
</fieldset>
```

### Primary color

```html
<select class="select select-primary">
  <option disabled selected>Pick a text editor</option>
  <option>VScode</option>
  <option>VScode fork</option>
  <option>Another VScode fork</option>
</select>
```

### Secondary color

```html
<select class="select select-secondary">
  <option disabled selected>Pick a language</option>
  <option>Zig</option>
  <option>Go</option>
  <option>Rust</option>
</select>
```

### Accent color

```html
<select class="select select-accent">
  <option selected disabled>Color scheme</option>
  <option>Light mode</option>
  <option>Dark mode</option>
  <option>System</option>
</select>
```

### Neutral color

```html
<select class="select select-neutral">
  <option disabled selected>Server location</option>
  <option>North America</option>
  <option>EU west</option>
  <option>South East Asia</option>
</select>
```

### Info color

```html
<select class="select select-info">
  <option disabled selected>Pick a Framework</option>
  <option>React</option>
  <option>Vue</option>
  <option>Angular</option>
</select>
```

### Success color

```html
<select class="select select-success">
  <option disabled selected>Pick a Runtime</option>
  <option>npm</option>
  <option>Bun</option>
  <option>yarn</option>
</select>
```

### Warning color

```html
<select class="select select-warning">
  <option disabled selected>Pick an OS</option>
  <option>Windows</option>
  <option>MacOS</option>
  <option>Linux</option>
</select>
```

### Error color

```html
<select class="select select-error">
  <option disabled selected>Pick an AI Model</option>
  <option>GPT-4</option>
  <option>Claude</option>
  <option>Llama</option>
</select>
```

### Sizes

```html
<select class="select select-xs">
  <option disabled selected>Xsmall</option>
  <option>Xsmall Apple</option>
  <option>Xsmall Orange</option>
  <option>Xsmall Tomato</option>
</select>
<select class="select select-sm">
  <option disabled selected>Small</option>
  <option>Small Apple</option>
  <option>Small Orange</option>
  <option>Small Tomato</option>
</select>
<select class="select select-md">
  <option disabled selected>Medium</option>
  <option>Medium Apple</option>
  <option>Medium Orange</option>
  <option>Medium Tomato</option>
</select>
<select class="select select-lg">
  <option disabled selected>Large</option>
  <option>Large Apple</option>
  <option>Large Orange</option>
  <option>Large Tomato</option>
</select>
<select class="select select-xl">
  <option disabled selected>Xlarge</option>
  <option>Xlarge Apple</option>
  <option>Xlarge Orange</option>
  <option>Xlarge Tomato</option>
</select>
```

### Disabled

```html
<select class="select" disabled>
  <option>You can't touch this</option>
</select>
```





---





# Text Input

Text Input is a simple input field.

## Component Details

| Class name      | Type      |                                                              |
| --------------- | --------- | ------------------------------------------------------------ |
| input           | Component | For <input type="text"> tag or a wrapper of <input type="text"> tag |
| input-ghost     | Style     | ghost style                                                  |
| input-neutral   | Color     | neutral color                                                |
| input-primary   | Color     | primary color                                                |
| input-secondary | Color     | secondary color                                              |
| input-accent    | Color     | accent color                                                 |
| input-info      | Color     | info color                                                   |
| input-success   | Color     | success color                                                |
| input-warning   | Color     | warning color                                                |
| input-error     | Color     | error color                                                  |
| input-xs        | Size      | Extra small size                                             |
| input-sm        | Size      | Small size                                                   |
| input-md        | Size      | Medium size[Default]                                         |
| input-lg        | Size      | Large size                                                   |
| input-xl        | Size      | Extra large size                                             |

## HTML Examples

### Text input

```html
<input type="text" placeholder="Type here" class="input" />
```

### Text input with text label inside

```html
<label class="input">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="2.5"
      fill="none"
      stroke="currentColor"
    >
      <circle cx="11" cy="11" r="8"></circle>
      <path d="m21 21-4.3-4.3"></path>
    </g>
  </svg>
  <input type="search" class="grow" placeholder="Search" />
  <kbd class="kbd kbd-sm">⌘</kbd>
  <kbd class="kbd kbd-sm">K</kbd>
</label>
<label class="input">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="2.5"
      fill="none"
      stroke="currentColor"
    >
      <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
      <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
    </g>
  </svg>
  <input type="text" class="grow" placeholder="index.php" />
</label>
<label class="input">
  Path
  <input type="text" class="grow" placeholder="src/app/" />
  <span class="badge badge-neutral badge-xs">Optional</span>
</label>
```

### Ghost style

```html
<input type="text" placeholder="Type here" class="input input-ghost" />
```

### With fieldset and fieldset-legend

```html
<fieldset class="fieldset">
  <legend class="fieldset-legend">What is your name?</legend>
  <input type="text" class="input" placeholder="Type here" />
  <p class="label">Optional</p>
</fieldset>
```

### Input colors

```html
<input type="text" placeholder="neutral" class="input input-neutral" />
<input type="text" placeholder="Primary" class="input input-primary" />
<input type="text" placeholder="Secondary" class="input input-secondary" />
<input type="text" placeholder="Accent" class="input input-accent" />
<input type="text" placeholder="Info" class="input input-info" />
<input type="text" placeholder="Success" class="input input-success" />
<input type="text" placeholder="Warning" class="input input-warning" />
<input type="text" placeholder="Error" class="input input-error" />
```

### Sizes

```html
<input type="text" placeholder="Xsmall" class="input input-xs" />
<input type="text" placeholder="Small" class="input input-sm" />
<input type="text" placeholder="Medium" class="input input-md" />
<input type="text" placeholder="Large" class="input input-lg" />
<input type="text" placeholder="Xlarge" class="input input-xl" />
```

### Disabled

```html
<input type="text" placeholder="You can't touch this" class="input" disabled />
```

### Text input with data list suggestion

```html
<input type="text" class="input" placeholder="Which browser do you use" list="browsers" />
<datalist id="browsers">
  <option value="Chrome"></option>
  <option value="Firefox"></option>
  <option value="Safari"></option>
  <option value="Opera"></option>
  <option value="Edge"></option>
</datalist>
```

### Date input

```html
<input type="date" class="input" />
```

### Time input

```html
<input type="time" class="input" />
```

### datetime-local input

```html
<input type="datetime-local" class="input" />
```

### Username text input with icon and validator

```html
<label class="input validator">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="2.5"
      fill="none"
      stroke="currentColor"
    >
      <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path>
      <circle cx="12" cy="7" r="4"></circle>
    </g>
  </svg>
  <input
    type="text"
    required
    placeholder="Username"
    pattern="[A-Za-z][A-Za-z0-9\-]*"
    minlength="3"
    maxlength="30"
    title="Only letters, numbers or dash"
  />
</label>
<p class="validator-hint">
  Must be 3 to 30 characters
  <br />containing only letters, numbers or dash
</p>
```

### Search input with icon

```html
<label class="input">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="2.5"
      fill="none"
      stroke="currentColor"
    >
      <circle cx="11" cy="11" r="8"></circle>
      <path d="m21 21-4.3-4.3"></path>
    </g>
  </svg>
  <input type="search" required placeholder="Search" />
</label>
```

### Email input with icon and validator

```html
<label class="input validator">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="2.5"
      fill="none"
      stroke="currentColor"
    >
      <rect width="20" height="16" x="2" y="4" rx="2"></rect>
      <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
    </g>
  </svg>
  <input type="email" placeholder="[email protected]" required />
</label>
<div class="validator-hint hidden">Enter valid email address</div>
```

### Email input with icon, validator, button, join

```html
<div class="join">
  <div>
    <label class="input validator join-item">
      <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
        <g
          stroke-linejoin="round"
          stroke-linecap="round"
          stroke-width="2.5"
          fill="none"
          stroke="currentColor"
        >
          <rect width="20" height="16" x="2" y="4" rx="2"></rect>
          <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
        </g>
      </svg>
      <input type="email" placeholder="[email protected]" required />
    </label>
    <div class="validator-hint hidden">Enter valid email address</div>
  </div>
  <button class="btn btn-neutral join-item">Join</button>
</div>
```

### Password input with icon and validator

```html
<label class="input validator">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="2.5"
      fill="none"
      stroke="currentColor"
    >
      <path
        d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"
      ></path>
      <circle cx="16.5" cy="7.5" r=".5" fill="currentColor"></circle>
    </g>
  </svg>
  <input
    type="password"
    required
    placeholder="Password"
    minlength="8"
    pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
    title="Must be more than 8 characters, including number, lowercase letter, uppercase letter"
  />
</label>
<p class="validator-hint hidden">
  Must be more than 8 characters, including
  <br />At least one number <br />At least one lowercase letter <br />At least one uppercase letter
</p>
```

### Number input with validator

```html
<input
  type="number"
  class="input validator"
  required
  placeholder="Type a number between 1 to 10"
  min="1"
  max="10"
  title="Must be between be 1 to 10"
/>
<p class="validator-hint">Must be between be 1 to 10</p>
```

### Telephone number input with icon and validator

```html
<label class="input validator">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
    <g fill="none">
      <path
        d="M7.25 11.5C6.83579 11.5 6.5 11.8358 6.5 12.25C6.5 12.6642 6.83579 13 7.25 13H8.75C9.16421 13 9.5 12.6642 9.5 12.25C9.5 11.8358 9.16421 11.5 8.75 11.5H7.25Z"
        fill="currentColor"
      ></path>
      <path
        fill-rule="evenodd"
        clip-rule="evenodd"
        d="M6 1C4.61929 1 3.5 2.11929 3.5 3.5V12.5C3.5 13.8807 4.61929 15 6 15H10C11.3807 15 12.5 13.8807 12.5 12.5V3.5C12.5 2.11929 11.3807 1 10 1H6ZM10 2.5H9.5V3C9.5 3.27614 9.27614 3.5 9 3.5H7C6.72386 3.5 6.5 3.27614 6.5 3V2.5H6C5.44771 2.5 5 2.94772 5 3.5V12.5C5 13.0523 5.44772 13.5 6 13.5H10C10.5523 13.5 11 13.0523 11 12.5V3.5C11 2.94772 10.5523 2.5 10 2.5Z"
        fill="currentColor"
      ></path>
    </g>
  </svg>
  <input
    type="tel"
    class="tabular-nums"
    required
    placeholder="Phone"
    pattern="[0-9]*"
    minlength="10"
    maxlength="10"
    title="Must be 10 digits"
  />
</label>
<p class="validator-hint">Must be 10 digits</p>
```

### URL with icon and validator

```html
<label class="input validator">
  <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="2.5"
      fill="none"
      stroke="currentColor"
    >
      <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
      <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
    </g>
  </svg>
  <input
    type="url"
    required
    placeholder="https://"
    value="https://"
    pattern="^(https?://)?([a-zA-Z0-9]([a-zA-Z0-9\-].*[a-zA-Z0-9])?\.)+[a-zA-Z].*"
    title="Must be valid URL"
  />
</label>
<p class="validator-hint">Must be valid URL</p>
```





---



# Textarea

Textarea allows users to enter text in multiple lines.

## Component Details

| Class name         | Type      |                        |
| ------------------ | --------- | ---------------------- |
| textarea           | Component | For <textarea> element |
| textarea-ghost     | Style     | ghost style            |
| textarea-neutral   | Color     | neutral color          |
| textarea-primary   | Color     | primary color          |
| textarea-secondary | Color     | secondary color        |
| textarea-accent    | Color     | accent color           |
| textarea-info      | Color     | info color             |
| textarea-success   | Color     | success color          |
| textarea-warning   | Color     | warning color          |
| textarea-error     | Color     | error color            |
| textarea-xs        | Size      | Extra small size       |
| textarea-sm        | Size      | Small size             |
| textarea-md        | Size      | Medium size[Default]   |
| textarea-lg        | Size      | Large size             |
| textarea-xl        | Size      | Extra large size       |

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





---





# Toggle

Toggle is a checkbox that is styled to look like a switch button.

## Component Details

| Class name       | Type      |                             |
| ---------------- | --------- | --------------------------- |
| toggle           | Component | For <input type="checkbox"> |
| toggle-primary   | Color     | primary color               |
| toggle-secondary | Color     | secondary color             |
| toggle-accent    | Color     | accent color                |
| toggle-neutral   | Color     | neutral color               |
| toggle-success   | Color     | success color               |
| toggle-warning   | Color     | warning color               |
| toggle-info      | Color     | info color                  |
| toggle-error     | Color     | error color                 |
| toggle-xs        | Size      | Extra small size            |
| toggle-sm        | Size      | Small size                  |
| toggle-md        | Size      | Medium size[Default]        |
| toggle-lg        | Size      | Large size                  |
| toggle-xl        | Size      | Extra large size            |

## HTML Examples

### Toggle

```html
<input type="checkbox" checked="checked" class="toggle" />
```

### With fieldset and label

```html
<fieldset class="fieldset bg-base-100 border-base-300 rounded-box w-64 border p-4">
  <legend class="fieldset-legend">Login options</legend>
  <label class="label">
    <input type="checkbox" checked="checked" class="toggle" />
    Remember me
  </label>
</fieldset>
```

### Sizes

```html
<input type="checkbox" checked="checked" class="toggle toggle-xs" />
<input type="checkbox" checked="checked" class="toggle toggle-sm" />
<input type="checkbox" checked="checked" class="toggle toggle-md" />
<input type="checkbox" checked="checked" class="toggle toggle-lg" />
<input type="checkbox" checked="checked" class="toggle toggle-xl" />
```

### Colors

```html
<input type="checkbox" checked="checked" class="toggle toggle-primary" />
<input type="checkbox" checked="checked" class="toggle toggle-secondary" />
<input type="checkbox" checked="checked" class="toggle toggle-accent" />
<input type="checkbox" checked="checked" class="toggle toggle-neutral" />
<input type="checkbox" checked="checked" class="toggle toggle-info" />
<input type="checkbox" checked="checked" class="toggle toggle-success" />
<input type="checkbox" checked="checked" class="toggle toggle-warning" />
<input type="checkbox" checked="checked" class="toggle toggle-error" />
```

### Disabled

```html
<input type="checkbox" class="toggle" disabled />
<input type="checkbox" class="toggle" disabled checked="checked" />
```

### Indeterminate

```html
<!-- You can make a checkbox indeterminate using JS -->
<script>
  document.getElementById("my-toggle").indeterminate = true
</script>
<input type="checkbox" class="toggle" id="my-toggle" />
```

### Toggle with icons inside

```html
<label class="toggle text-base-content">
  <input type="checkbox" />
  <svg aria-label="enabled" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
    <g
      stroke-linejoin="round"
      stroke-linecap="round"
      stroke-width="4"
      fill="none"
      stroke="currentColor"
    >
      <path d="M20 6 9 17l-5-5"></path>
    </g>
  </svg>
  <svg
    aria-label="disabled"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="4"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="M18 6 6 18" />
    <path d="m6 6 12 12" />
  </svg>
</label>
```

### Toggle with custom colors

```html
<input
  type="checkbox"
  checked="checked"
  class="toggle border-indigo-600 bg-indigo-500 checked:border-orange-500 checked:bg-orange-400 checked:text-orange-800"
/>
```





---



# Validator

Validator class changes the color of form elements to error or success based on input's validation rules.

## Component Details

| Class name     | Type      |                                                              |
| -------------- | --------- | ------------------------------------------------------------ |
| validator      | Component | For input, select, textarea                                  |
| validator-hint | Part      | for the hint text that appears after the input if it's invalid |

## HTML Examples

### Validator

```html
<input class="input validator" type="email" required placeholder="[email protected]" />
```

### Validator and validator-hint

```html
<input class="input validator" type="email" required placeholder="[email protected]" />
<div class="validator-hint">Enter valid email address</div>
```

### Password requirement validator

```html
<input type="password" class="input validator" required placeholder="Password" minlength="8" 
  pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" 
  title="Must be more than 8 characters, including number, lowercase letter, uppercase letter" />
<p class="validator-hint">
  Must be more than 8 characters, including
  <br/>At least one number
  <br/>At least one lowercase letter
  <br/>At least one uppercase letter
</p>
```

### Username requirement validator

```html
<input type="text" class="input validator" required placeholder="Username" 
  pattern="[A-Za-z][A-Za-z0-9\-]*" minlength="3" maxlength="30" title="Only letters, numbers or dash" />
<p class="validator-hint">
  Must be 3 to 30 characters
  <br/>containing only letters, numbers or dash
</p>
```

### Phone Number requirement validator

```html
<input type="tel" class="input validator tabular-nums" required placeholder="Phone" 
  pattern="[0-9]*" minlength="10" maxlength="10" title="Must be 10 digits" />
<p class="validator-hint">Must be 10 digits</p>
```

### URL input requirement validator

```html
<input type="url" class="input validator" required placeholder="https://" value="https://"
  pattern="^(https?://)?([a-zA-Z0-9]([a-zA-Z0-9-].*[a-zA-Z0-9])?.)+[a-zA-Z].*" 
  title="Must be valid URL" />
<p class="validator-hint">Must be valid URL</p>
```

### Date input requirement validator

```html
<input type="date" class="input validator" required placeholder="Pick a date in 2025" 
min="2025-01-01" max="2025-12-31"
  title="Must be valid URL" />
<p class="validator-hint">Must be 2025</p>
```

### Number input requirement validator

```html
<input type="number" class="input validator" required placeholder="Type a number between 1 to 10" 
min="1" max="10"
  title="Must be between be 1 to 10" />
<p class="validator-hint">Must be between be 1 to 10</p>
```

### Checkbox requirement validator

```html
<input type="checkbox" class="checkbox validator" required title="Required" />
<p class="validator-hint">Required</p>
```

### Toggle requirement validator

```html
<input type="checkbox" class="toggle validator" required title="Required" />
<p class="validator-hint">Required</p>
```

### Select requirement validator

```html
<form>
  <select class="select validator" required>
    <option disabled selected value="">Choose:</option>
    <option>Tabs</option>
    <option>Spaces</option>
  </select>
  <p class="validator-hint">Required</p>
  <button class="btn" type="submit">Submit form</button>
</form>
```







