# Diff - HTML Examples

Diff component shows a side-by-side comparison of two items.

## Diff

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

## Diff text

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

