### Mockup

1. [Browser](#mockup-browser/)
2. [Code](#mockup-code/)
3. [Phone](#mockup-phone/)
4. [Window](#mockup-window/)



# Browser mockup

Browser mockup shows a box that looks like a browser window.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| mockup-browser | Component | Browser mockup |
| mockup-browser-toolbar | Part | Toolbar part which can include addressbar, etc |

## HTML Examples

### browser mockup with border

```html
<div class="mockup-browser border-base-300 border w-full">
  <div class="mockup-browser-toolbar">
    <div class="input">https://daisyui.com</div>
  </div>
  <div class="grid place-content-center border-t border-base-300 h-80">Hello!</div>
</div>
```

### browser mockup with background color

```html
<div class="mockup-browser border border-base-300 w-full">
  <div class="mockup-browser-toolbar">
    <div class="input">https://daisyui.com</div>
  </div>
  <div class="grid place-content-center h-80">Hello!</div>
</div>
```



---



# Code mockup

Code mockup is used to show a block of code in a box that looks like a code editor.

## Component Details

| Class name  | Type      |                      |
| ----------- | --------- | -------------------- |
| mockup-code | Component | Code terminal mockup |

## HTML Examples

### mockup code with line prefix

```html
<div class="mockup-code w-full">
  <pre data-prefix=""><code>npm i daisyui</code></pre>
</div>
```

### Multi line

```html
<div class="mockup-code w-full">
  <pre data-prefix=""><code>npm i daisyui</code></pre>
  <pre data-prefix=">" class="text-warning"><code>installing...</code></pre>
  <pre data-prefix=">" class="text-success"><code>Done!</code></pre>
</div>
```

### Highlighted line

```html
<div class="mockup-code w-full">
  <pre data-prefix="1"><code>npm i daisyui</code></pre>
  <pre data-prefix="2"><code>installing...</code></pre>
  <pre data-prefix="3" class="bg-warning text-warning-content"><code>Error!</code></pre>
</div>
```

### Long line will scroll

```html
<div class="mockup-code w-full">
  <pre
    data-prefix="~"><code>Magnam dolore beatae necessitatibus nemopsum itaque sit. Et porro quae qui et et dolore ratione.</code></pre>
</div>
```

### Without prefix

```html
<div class="mockup-code w-full">
  <pre><code>without prefix</code></pre>
</div>
```

### With color

```html
<div class="mockup-code bg-primary text-primary-content w-full">
  <pre><code>can be any color!</code></pre>
</div>
```





---



# Phone mockup

Phone mockup shows a mockup of an iPhone.

## Component Details

| Class name           | Type      |              |
| -------------------- | --------- | ------------ |
| mockup-phone         | Component | Phone mockup |
| mockup-phone-camera  | Part      | Camera part  |
| mockup-phone-display | Part      | Display part |

## HTML Examples

### iPhone mockup

```html
<div class="mockup-phone">
  <div class="mockup-phone-camera"></div>
  <div class="mockup-phone-display text-white grid place-content-center">It's Glowtime.</div>
</div>
```

### With color and wallpaper

```html
<div class="mockup-phone border-primary">
  <div class="mockup-phone-camera"></div>
  <div class="mockup-phone-display">
    <img alt="wallpaper" src="https://img.daisyui.com/images/stock/453966.webp"/>
  </div>
</div>
```





---





# Window mockup

Window mockup shows a box that looks like an operating system window.

## Component Details

| Class name    | Type      |                  |
| ------------- | --------- | ---------------- |
| mockup-window | Component | OS window mockup |

## HTML Examples

### window mockup with border

```html
<div class="mockup-window border border-base-300 w-full">
  <div class="grid place-content-center border-t border-base-300 h-80">Hello!</div>
</div>
```

### window mockup with background color

```html
<div class="mockup-window bg-base-100 border border-base-300">
  <div class="grid place-content-center h-80">Hello!</div>
</div>
```

