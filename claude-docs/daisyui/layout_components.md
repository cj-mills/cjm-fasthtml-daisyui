### Layout

1. [Divider](#divider/)
2. [Drawer](#drawer/)
3. [Footer](#footer/)
4. [Hero](#hero/)
5. [Indicator](#indicator/)
6. [Join (group items)](#join/)
7. [Mask](#mask/)
8. [Stack](#stack/)



# Divider

Divider will be used to separate content vertically or horizontally.

## Component Details

| Class name | Type |  |
| --- | --- | --- |
| divider | Component | A divider line between two elements |
| divider-neutral | Color | neutral color |
| divider-primary | Color | primary color |
| divider-secondary | Color | secondary color |
| divider-accent | Color | accent color |
| divider-success | Color | success color |
| divider-warning | Color | warning color |
| divider-info | Color | info color |
| divider-error | Color | error color |
| divider-vertical | direction | Divide vertical elements (on top of each other)[Default] |
| divider-horizontal | direction | Divide horizontal elements (next to each other) |
| divider-start | Placement | Pushes the divider text to the start |
| divider-end | Placement | Pushes the divider text to the end |

## HTML Examples

### Divider

```html
<div class="flex w-full flex-col">
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
  <div class="divider">OR</div>
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
</div>
```

### Divider horizontal

```html
<div class="flex w-full">
  <div class="card bg-base-300 rounded-box grid h-20 grow place-items-center">content</div>
  <div class="divider divider-horizontal">OR</div>
  <div class="card bg-base-300 rounded-box grid h-20 grow place-items-center">content</div>
</div>
```

### Divider with no text

```html
<div class="flex w-full flex-col">
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
  <div class="divider"></div>
  <div class="card bg-base-300 rounded-box grid h-20 place-items-center">content</div>
</div>
```

### responsive (lg:divider-horizontal)

```html
<div class="flex w-full flex-col lg:flex-row">
  <div class="card bg-base-300 rounded-box grid h-32 grow place-items-center">content</div>
  <div class="divider lg:divider-horizontal">OR</div>
  <div class="card bg-base-300 rounded-box grid h-32 grow place-items-center">content</div>
</div>
```

### Divider with colors

```html
<div class="flex w-full flex-col">
  <div class="divider">Default</div>
  <div class="divider divider-neutral">Neutral</div>
  <div class="divider divider-primary">Primary</div>
  <div class="divider divider-secondary">Secondary</div>
  <div class="divider divider-accent">Accent</div>
  <div class="divider divider-success">Success</div>
  <div class="divider divider-warning">Warning</div>
  <div class="divider divider-info">Info</div>
  <div class="divider divider-error">Error</div>
</div>
```

### Divider in different positions

```html
<div class="flex w-full flex-col">
  <div class="divider divider-start">Start</div>
  <div class="divider">Default</div>
  <div class="divider divider-end">End</div>
</div>
```

### Divider in different positions (horizontal)

```html
<div class="flex w-full">
  <div class="divider divider-horizontal divider-start">Start</div>
  <div class="divider divider-horizontal">Default</div>
  <div class="divider divider-horizontal divider-end">End</div>
</div>
```





---



# Drawer

Drawer is a grid layout that can show/hide a sidebar on the left or right side of the page.

## Component Details

| Class name     | Type      |                                                       |
| -------------- | --------- | ----------------------------------------------------- |
| drawer         | Component | The wrapper for sidebar and content                   |
| drawer-toggle  | Part      | The hidden checkbox that controls the state of drawer |
| drawer-content | Part      | Content part                                          |
| drawer-side    | Part      | Sidebar part                                          |
| drawer-overlay | Part      | Label that covers the page when drawer is open        |
| drawer-end     | Placement | puts drawer to the other side                         |
| drawer-open    | Modifier  | Forces the drawer to be open                          |

## HTML Examples

### Drawer

```html
<div class="drawer">
  <input id="my-drawer" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <!-- Page content here -->
    <label for="my-drawer" class="btn btn-primary drawer-button">Open drawer</label>
  </div>
  <div class="drawer-side">
    <label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
    <ul class="menu bg-base-200 text-base-content min-h-full w-80 p-4">
      <!-- Sidebar content here -->
      <li><a>Sidebar Item 1</a></li>
      <li><a>Sidebar Item 2</a></li>
    </ul>
  </div>
</div>
```

### Navbar menu for desktop + sidebar drawer for mobile

```html
<div class="drawer">
  <input id="my-drawer-3" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content flex flex-col">
    <!-- Navbar -->
    <div class="navbar bg-base-300 w-full">
      <div class="flex-none lg:hidden">
        <label for="my-drawer-3" aria-label="open sidebar" class="btn btn-square btn-ghost">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            class="inline-block h-6 w-6 stroke-current"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            ></path>
          </svg>
        </label>
      </div>
      <div class="mx-2 flex-1 px-2">Navbar Title</div>
      <div class="hidden flex-none lg:block">
        <ul class="menu menu-horizontal">
          <!-- Navbar menu content here -->
          <li><a>Navbar Item 1</a></li>
          <li><a>Navbar Item 2</a></li>
        </ul>
      </div>
    </div>
    <!-- Page content here -->
    Content
  </div>
  <div class="drawer-side">
    <label for="my-drawer-3" aria-label="close sidebar" class="drawer-overlay"></label>
    <ul class="menu bg-base-200 min-h-full w-80 p-4">
      <!-- Sidebar content here -->
      <li><a>Sidebar Item 1</a></li>
      <li><a>Sidebar Item 2</a></li>
    </ul>
  </div>
</div>
```

### Responsive

```html
<div class="drawer lg:drawer-open">
  <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content flex flex-col items-center justify-center">
    <!-- Page content here -->
    <label for="my-drawer-2" class="btn btn-primary drawer-button lg:hidden">
      Open drawer
    </label>
  </div>
  <div class="drawer-side">
    <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label>
    <ul class="menu bg-base-200 text-base-content min-h-full w-80 p-4">
      <!-- Sidebar content here -->
      <li><a>Sidebar Item 1</a></li>
      <li><a>Sidebar Item 2</a></li>
    </ul>
  </div>
</div>
```

### Drawer that opens from right side of page

```html
<div class="drawer drawer-end">
  <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <!-- Page content here -->
    <label for="my-drawer-4" class="drawer-button btn btn-primary">Open drawer</label>
  </div>
  <div class="drawer-side">
    <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
    <ul class="menu bg-base-200 text-base-content min-h-full w-80 p-4">
      <!-- Sidebar content here -->
      <li><a>Sidebar Item 1</a></li>
      <li><a>Sidebar Item 2</a></li>
    </ul>
  </div>
</div>
```





---



# Footer

Footer can contain logo, copyright notice, and links to other pages.

## Component Details

| Class name        | Type      |                                                          |
| ----------------- | --------- | -------------------------------------------------------- |
| footer            | Component | Footer                                                   |
| footer-title      | Part      | Title of a footer column                                 |
| footer-center     | Placement | Aligns footer content to center                          |
| footer-horizontal | direction | Puts footer columns next to each other horizontally      |
| footer-vertical   | direction | Puts footer columns under each other vertically[Default] |

## HTML Examples

### Footer (vertical by default, horizontal for sm and up)

```html
<footer class="footer sm:footer-horizontal bg-neutral text-neutral-content p-10">
  <nav>
    <h6 class="footer-title">Services</h6>
    <a class="link link-hover">Branding</a>
    <a class="link link-hover">Design</a>
    <a class="link link-hover">Marketing</a>
    <a class="link link-hover">Advertisement</a>
  </nav>
  <nav>
    <h6 class="footer-title">Company</h6>
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
    <a class="link link-hover">Press kit</a>
  </nav>
  <nav>
    <h6 class="footer-title">Legal</h6>
    <a class="link link-hover">Terms of use</a>
    <a class="link link-hover">Privacy policy</a>
    <a class="link link-hover">Cookie policy</a>
  </nav>
</footer>
```

### Footer with a logo section

```html
<footer class="footer sm:footer-horizontal bg-base-200 text-base-content p-10">
  <aside>
    <svg
      width="50"
      height="50"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      fill-rule="evenodd"
      clip-rule="evenodd"
      class="fill-current">
      <path
        d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
    </svg>
    <p>
      ACME Industries Ltd.
      <br />
      Providing reliable tech since 1992
    </p>
  </aside>
  <nav>
    <h6 class="footer-title">Services</h6>
    <a class="link link-hover">Branding</a>
    <a class="link link-hover">Design</a>
    <a class="link link-hover">Marketing</a>
    <a class="link link-hover">Advertisement</a>
  </nav>
  <nav>
    <h6 class="footer-title">Company</h6>
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
    <a class="link link-hover">Press kit</a>
  </nav>
  <nav>
    <h6 class="footer-title">Legal</h6>
    <a class="link link-hover">Terms of use</a>
    <a class="link link-hover">Privacy policy</a>
    <a class="link link-hover">Cookie policy</a>
  </nav>
</footer>
```

### Footer with a form

```html
<footer class="footer sm:footer-horizontal bg-base-200 text-base-content p-10">
  <nav>
    <h6 class="footer-title">Services</h6>
    <a class="link link-hover">Branding</a>
    <a class="link link-hover">Design</a>
    <a class="link link-hover">Marketing</a>
    <a class="link link-hover">Advertisement</a>
  </nav>
  <nav>
    <h6 class="footer-title">Company</h6>
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
    <a class="link link-hover">Press kit</a>
  </nav>
  <nav>
    <h6 class="footer-title">Legal</h6>
    <a class="link link-hover">Terms of use</a>
    <a class="link link-hover">Privacy policy</a>
    <a class="link link-hover">Cookie policy</a>
  </nav>
  <form>
    <h6 class="footer-title">Newsletter</h6>
    <fieldset class="w-80">
      <label>Enter your email address</label>
      <div class="join">
        <input
          type="text"
          placeholder="[email protected]"
          class="input input-bordered join-item" />
        <button class="btn btn-primary join-item">Subscribe</button>
      </div>
    </fieldset>
  </form>
</footer>
```

### Footer with logo and social icons

```html
<footer class="footer sm:footer-horizontal bg-neutral text-neutral-content p-10">
  <aside>
    <svg
      width="50"
      height="50"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      fill-rule="evenodd"
      clip-rule="evenodd"
      class="fill-current">
      <path
        d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
    </svg>
    <p>
      ACME Industries Ltd.
      <br />
      Providing reliable tech since 1992
    </p>
  </aside>
  <nav>
    <h6 class="footer-title">Social</h6>
    <div class="grid grid-flow-col gap-4">
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
        </svg>
      </a>
    </div>
  </nav>
</footer>
```

### Footer with copyright text

```html
<footer class="footer sm:footer-horizontal footer-center bg-base-300 text-base-content p-4">
  <aside>
    <p>Copyright © {new Date().getFullYear()} - All right reserved by ACME Industries Ltd</p>
  </aside>
</footer>
```

### Footer with copyright text and social icons

```html
<footer class="footer sm:footer-horizontal bg-neutral text-neutral-content items-center p-4">
  <aside class="grid-flow-col items-center">
    <svg
      width="36"
      height="36"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      fill-rule="evenodd"
      clip-rule="evenodd"
      class="fill-current">
      <path
        d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
    </svg>
    <p>Copyright © {new Date().getFullYear()} - All right reserved</p>
  </aside>
  <nav class="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
    <a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        class="fill-current">
        <path
          d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
      </svg>
    </a>
    <a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        class="fill-current">
        <path
          d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
      </svg>
    </a>
    <a>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
        class="fill-current">
        <path
          d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
      </svg>
    </a>
  </nav>
</footer>
```

### Footer with links and social icons

```html
<footer class="footer sm:footer-horizontal bg-base-300 text-base-content p-10">
  <nav>
    <h6 class="footer-title">Services</h6>
    <a class="link link-hover">Branding</a>
    <a class="link link-hover">Design</a>
    <a class="link link-hover">Marketing</a>
    <a class="link link-hover">Advertisement</a>
  </nav>
  <nav>
    <h6 class="footer-title">Company</h6>
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
    <a class="link link-hover">Press kit</a>
  </nav>
  <nav>
    <h6 class="footer-title">Social</h6>
    <div class="grid grid-flow-col gap-4">
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
        </svg>
      </a>
    </div>
  </nav>
</footer>
```

### Footer with 2 rows

```html
<footer class="footer sm:footer-horizontal bg-neutral text-neutral-content grid-rows-2 p-10">
  <nav>
    <h6 class="footer-title">Services</h6>
    <a class="link link-hover">Branding</a>
    <a class="link link-hover">Design</a>
    <a class="link link-hover">Marketing</a>
    <a class="link link-hover">Advertisement</a>
  </nav>
  <nav>
    <h6 class="footer-title">Company</h6>
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
    <a class="link link-hover">Press kit</a>
  </nav>
  <nav>
    <h6 class="footer-title">Legal</h6>
    <a class="link link-hover">Terms of use</a>
    <a class="link link-hover">Privacy policy</a>
    <a class="link link-hover">Cookie policy</a>
  </nav>
  <nav>
    <h6 class="footer-title">Social</h6>
    <a class="link link-hover">Twitter</a>
    <a class="link link-hover">Instagram</a>
    <a class="link link-hover">Facebook</a>
    <a class="link link-hover">GitHub</a>
  </nav>
  <nav>
    <h6 class="footer-title">Explore</h6>
    <a class="link link-hover">Features</a>
    <a class="link link-hover">Enterprise</a>
    <a class="link link-hover">Security</a>
    <a class="link link-hover">Pricing</a>
  </nav>
  <nav>
    <h6 class="footer-title">Apps</h6>
    <a class="link link-hover">Mac</a>
    <a class="link link-hover">Windows</a>
    <a class="link link-hover">iPhone</a>
    <a class="link link-hover">Android</a>
  </nav>
</footer>
```

### Centered footer with logo and social icons

```html
<footer class="footer footer-horizontal footer-center bg-primary text-primary-content p-10">
  <aside>
    <svg
      width="50"
      height="50"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      fill-rule="evenodd"
      clip-rule="evenodd"
      class="inline-block fill-current">
      <path
        d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
    </svg>
    <p class="font-bold">
      ACME Industries Ltd.
      <br />
      Providing reliable tech since 1992
    </p>
    <p>Copyright © {new Date().getFullYear()} - All right reserved</p>
  </aside>
  <nav>
    <div class="grid grid-flow-col gap-4">
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
        </svg>
      </a>
    </div>
  </nav>
</footer>
```

### Centered footer with social icons

```html
<footer class="footer footer-horizontal footer-center bg-base-200 text-base-content rounded p-10">
  <nav class="grid grid-flow-col gap-4">
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
    <a class="link link-hover">Press kit</a>
  </nav>
  <nav>
    <div class="grid grid-flow-col gap-4">
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
        </svg>
      </a>
    </div>
  </nav>
  <aside>
    <p>Copyright © {new Date().getFullYear()} - All right reserved by ACME Industries Ltd</p>
  </aside>
</footer>
```

### Two footer

```html
<footer class="footer sm:footer-horizontal bg-base-200 text-base-content p-10">
  <nav>
    <h6 class="footer-title">Services</h6>
    <a class="link link-hover">Branding</a>
    <a class="link link-hover">Design</a>
    <a class="link link-hover">Marketing</a>
    <a class="link link-hover">Advertisement</a>
  </nav>
  <nav>
    <h6 class="footer-title">Company</h6>
    <a class="link link-hover">About us</a>
    <a class="link link-hover">Contact</a>
    <a class="link link-hover">Jobs</a>
    <a class="link link-hover">Press kit</a>
  </nav>
  <nav>
    <h6 class="footer-title">Legal</h6>
    <a class="link link-hover">Terms of use</a>
    <a class="link link-hover">Privacy policy</a>
    <a class="link link-hover">Cookie policy</a>
  </nav>
</footer>
<footer class="footer bg-base-200 text-base-content border-base-300 border-t px-10 py-4">
  <aside class="grid-flow-col items-center">
    <svg
      width="24"
      height="24"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      fill-rule="evenodd"
      clip-rule="evenodd"
      class="fill-current">
      <path
        d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
    </svg>
    <p>
      ACME Industries Ltd.
      <br />
      Providing reliable tech since 1992
    </p>
  </aside>
  <nav class="md:place-self-center md:justify-self-end">
    <div class="grid grid-flow-col gap-4">
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
        </svg>
      </a>
      <a>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          class="fill-current">
          <path
            d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
        </svg>
      </a>
    </div>
  </nav>
</footer>
```





---



# Hero

Hero is a component for displaying a large box or image with a title and description.

## Component Details

| Class name   | Type      |                                          |
| ------------ | --------- | ---------------------------------------- |
| hero         | Component | Hero container                           |
| hero-content | Part      | content part                             |
| hero-overlay | Part      | Overlay that covers the background image |

## HTML Examples

### Centered hero

```html
<div class="hero bg-base-200 min-h-screen">
  <div class="hero-content text-center">
    <div class="max-w-md">
      <h1 class="text-5xl font-bold">Hello there</h1>
      <p class="py-6">
        Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
        quasi. In deleniti eaque aut repudiandae et a id nisi.
      </p>
      <button class="btn btn-primary">Get Started</button>
    </div>
  </div>
</div>
```

### Hero with figure

```html
<div class="hero bg-base-200 min-h-screen">
  <div class="hero-content flex-col lg:flex-row">
    <img
      src="https://img.daisyui.com/images/stock/photo-1635805737707-575885ab0820.webp"
      class="max-w-sm rounded-lg shadow-2xl"
    />
    <div>
      <h1 class="text-5xl font-bold">Box Office News!</h1>
      <p class="py-6">
        Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
        quasi. In deleniti eaque aut repudiandae et a id nisi.
      </p>
      <button class="btn btn-primary">Get Started</button>
    </div>
  </div>
</div>
```

### Hero with figure but reverse order

```html
<div class="hero bg-base-200 min-h-screen">
  <div class="hero-content flex-col lg:flex-row-reverse">
    <img
      src="https://img.daisyui.com/images/stock/photo-1635805737707-575885ab0820.webp"
      class="max-w-sm rounded-lg shadow-2xl"
    />
    <div>
      <h1 class="text-5xl font-bold">Box Office News!</h1>
      <p class="py-6">
        Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
        quasi. In deleniti eaque aut repudiandae et a id nisi.
      </p>
      <button class="btn btn-primary">Get Started</button>
    </div>
  </div>
</div>
```

### Hero with form

```html
<div class="hero bg-base-200 min-h-screen">
  <div class="hero-content flex-col lg:flex-row-reverse">
    <div class="text-center lg:text-left">
      <h1 class="text-5xl font-bold">Login now!</h1>
      <p class="py-6">
        Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
        quasi. In deleniti eaque aut repudiandae et a id nisi.
      </p>
    </div>
    <div class="card bg-base-100 w-full max-w-sm shrink-0 shadow-2xl">
      <div class="card-body">
        <fieldset class="fieldset">
          <label class="label">Email</label>
          <input type="email" class="input" placeholder="Email" />
          <label class="label">Password</label>
          <input type="password" class="input" placeholder="Password" />
          <div><a class="link link-hover">Forgot password?</a></div>
          <button class="btn btn-neutral mt-4">Login</button>
        </fieldset>
      </div>
    </div>
  </div>
</div>
```

### Hero with overlay image

```html
<div
  class="hero min-h-screen"
  style="background-image: url(https://img.daisyui.com/images/stock/photo-1507358522600-9f71e620c44e.webp);"
>
  <div class="hero-overlay"></div>
  <div class="hero-content text-neutral-content text-center">
    <div class="max-w-md">
      <h1 class="mb-5 text-5xl font-bold">Hello there</h1>
      <p class="mb-5">
        Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem
        quasi. In deleniti eaque aut repudiandae et a id nisi.
      </p>
      <button class="btn btn-primary">Get Started</button>
    </div>
  </div>
</div>
```





---



# Indicator

Indicators are used to place an element on the corner of another element.

## Component Details

| Class name       | Type      |                                         |
| ---------------- | --------- | --------------------------------------- |
| indicator        | Component | Container element                       |
| indicator-item   | Part      | will be placed on the corner of sibling |
| indicator-start  | Placement | align horizontally to the start         |
| indicator-center | Placement | align horizontally to the center        |
| indicator-end    | Placement | align horizontally to the end[Default]  |
| indicator-top    | Placement | align vertically to top[Default]        |
| indicator-middle | Placement | align vertically to middle              |
| indicator-bottom | Placement | align vertically to bottom              |

## HTML Examples

### Status Indicator

```html
<div class="indicator">
  <span class="indicator-item status status-success"></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### Badge as indicator

```html
<div class="indicator">
  <span class="indicator-item badge badge-primary">New</span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### for button

```html
<div class="indicator">
  <span class="indicator-item badge badge-secondary">12</span>
  <button class="btn">inbox</button>
</div>
```

### for tab

```html
<div class="tabs tabs-lift">
  <a class="tab">Messages</a>
  <a class="indicator tab tab-active">
    Notifications
    <span class="indicator-item badge">8</span>
  </a>
  <a class="tab">Requests</a>
</div>
```

### for avatar

```html
<div class="avatar indicator">
  <span class="indicator-item badge badge-secondary">Justice</span>
  <div class="h-20 w-20 rounded-lg">
    <img
      alt="Tailwind CSS examples"
      src="https://img.daisyui.com/images/profile/demo/[email protected]"
    />
  </div>
</div>
```

### for an input

```html
<div class="indicator">
  <span class="indicator-item badge">Required</span>
  <input type="text" placeholder="Your email address" class="input input-bordered" />
</div>
```

### A button as an indicator for a card

```html
<div class="indicator">
  <div class="indicator-item indicator-bottom">
    <button class="btn btn-primary">Apply</button>
  </div>
  <div class="card border-base-300 border shadow-sm">
    <div class="card-body">
      <h2 class="card-title">Job Title</h2>
      <p>Rerum reiciendis beatae tenetur excepturi</p>
    </div>
  </div>
</div>
```

### in center of an image

```html
<div class="indicator">
  <span class="indicator-item indicator-center indicator-middle">
    Only available for Pro users
  </span>
  <img
    alt="Tailwind CSS examples"
    src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
  />
</div>
```

### indicator-top (default) indicator-start

```html
<div class="indicator">
  <span class="indicator-item indicator-start badge badge-secondary"></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-top (default) indicator-center

```html
<div class="indicator">
  <span class="indicator-item indicator-center badge badge-secondary"></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-top (default) indicator-end (default)

```html
<div class="indicator">
  <span class="indicator-item badge badge-secondary"></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-middle indicator-start

```html
<div class="indicator">
  <span
    class="indicator-item indicator-middle indicator-start badge badge-secondary"
  ></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-middle indicator-center

```html
<div class="indicator">
  <span
    class="indicator-item indicator-middle indicator-center badge badge-secondary"
  ></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-middle indicator-end (default)

```html
<div class="indicator">
  <span class="indicator-item indicator-middle badge badge-secondary"></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-bottom indicator-start

```html
<div class="indicator">
  <span
    class="indicator-item indicator-bottom indicator-start badge badge-secondary"
  ></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-bottom indicator-center

```html
<div class="indicator">
  <span
    class="indicator-item indicator-bottom indicator-center badge badge-secondary"
  ></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### indicator-bottom indicator-end (default)

```html
<div class="indicator">
  <span class="indicator-item indicator-bottom badge badge-secondary"></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```

### multiple indicators

```html
<div class="indicator">
  <span class="indicator-item indicator-top indicator-start badge">↖︎</span>
  <span class="indicator-item indicator-top indicator-center badge">↑</span>
  <span class="indicator-item indicator-top indicator-end badge">↗︎</span>
  <span class="indicator-item indicator-middle indicator-start badge">←</span>
  <span class="indicator-item indicator-middle indicator-center badge">●</span>
  <span class="indicator-item indicator-middle indicator-end badge">→</span>
  <span class="indicator-item indicator-bottom indicator-start badge">↙︎</span>
  <span class="indicator-item indicator-bottom indicator-center badge">↓</span>
  <span class="indicator-item indicator-bottom indicator-end badge">↘︎</span>
  <div class="bg-base-300 grid h-32 w-60 place-items-center">Box</div>
</div>
```

### Responsive

```html
<div class="indicator">
  <span
    class="indicator-item indicator-start sm:indicator-middle md:indicator-bottom lg:indicator-center xl:indicator-end badge badge-secondary"
  ></span>
  <div class="bg-base-300 grid h-32 w-32 place-items-center">content</div>
</div>
```





---



# Join

Join is a container for grouping multiple items, it can be used to group buttons, inputs, etc. Join applies border radius to the first and last item. Join can be used to create a horizontal or vertical list of items.

## Component Details

| Class name      | Type      |                                                |
| --------------- | --------- | ---------------------------------------------- |
| join            | Component | For grouping multiple items                    |
| join-item       | Component | Item inside join. Can be a button, input, etc. |
| join-vertical   | direction | Show items vertically                          |
| join-horizontal | direction | Show items horizontally                        |

## HTML Examples

### Join

```html
<div class="join">
  <button class="btn join-item">Button</button>
  <button class="btn join-item">Button</button>
  <button class="btn join-item">Button</button>
</div>
```

### Group items vertically

```html
<div class="join join-vertical">
  <button class="btn join-item">Button</button>
  <button class="btn join-item">Button</button>
  <button class="btn join-item">Button</button>
</div>
```

### Responsive: it's vertical on small screen and horizontal on large screen

```html
<div class="join join-vertical lg:join-horizontal">
  <button class="btn join-item">Button</button>
  <button class="btn join-item">Button</button>
  <button class="btn join-item">Button</button>
</div>
```

### With extra elements in the group

```html
<div class="join">
  <div>
    <div>
      <input class="input join-item" placeholder="Search" />
    </div>
  </div>
  <select class="select join-item">
    <option disabled selected>Filter</option>
    <option>Sci-fi</option>
    <option>Drama</option>
    <option>Action</option>
  </select>
  <div class="indicator">
    <span class="indicator-item badge badge-secondary">new</span>
    <button class="btn join-item">Search</button>
  </div>
</div>
```

### Custom border radius

```html
<div class="join">
  <input class="input join-item" placeholder="Email" />
  <button class="btn join-item rounded-r-full">Subscribe</button>
</div>
```

### Join radio inputs with btn style

```html
<div class="join">
  <input class="join-item btn" type="radio" name="options" aria-label="Radio 1" />
  <input class="join-item btn" type="radio" name="options" aria-label="Radio 2" />
  <input class="join-item btn" type="radio" name="options" aria-label="Radio 3" />
</div>
```





---



# Mask

Mask crops the content of the element to common shapes.

## Component Details

| Class name      | Type      |                                    |
| --------------- | --------- | ---------------------------------- |
| mask            | Component | Masks the content with shape       |
| mask-squircle   | Style     | squircle                           |
| mask-heart      | Style     | heart                              |
| mask-hexagon    | Style     | hexagon vertical                   |
| mask-hexagon-2  | Style     | hexagon horizontal                 |
| mask-decagon    | Style     | decagon                            |
| mask-pentagon   | Style     | pentagon                           |
| mask-diamond    | Style     | diamond                            |
| mask-square     | Style     | square                             |
| mask-circle     | Style     | circle                             |
| mask-star       | Style     | star                               |
| mask-star-2     | Style     | star (bold)                        |
| mask-triangle   | Style     | triangle pointing top              |
| mask-triangle-2 | Style     | triangle pointing down             |
| mask-triangle-3 | Style     | triangle pointing left             |
| mask-triangle-4 | Style     | triangle pointing right            |
| mask-half-1     | Modifier  | Crops only the first half of mask  |
| mask-half-2     | Modifier  | Crops only the second half of mask |

## HTML Examples

### Squircle

```html
<img
  class="mask mask-squircle"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Heart

```html
<img
  class="mask mask-heart"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Hexagon

```html
<img
  class="mask mask-hexagon"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Hexagon-2 (horizontal hexagon)

```html
<img
  class="mask mask-hexagon-2"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Decagon

```html
<img
  class="mask mask-decagon"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Pentagon

```html
<img
  class="mask mask-pentagon"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Diamond

```html
<img
  class="mask mask-diamond"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Square

```html
<img
  class="mask mask-square"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Circle

```html
<img
  class="mask mask-circle"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Star

```html
<img
  class="mask mask-star"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Star-2 (bold star)

```html
<img
  class="mask mask-star-2"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Triangle (pointing top)

```html
<img
  class="mask mask-triangle"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Triangle-2 (pointing down)

```html
<img
  class="mask mask-triangle-2"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Triangle-3 (pointing left)

```html
<img
  class="mask mask-triangle-3"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```

### Triangle-4 (pointing right)

```html
<img
  class="mask mask-triangle-4"
  src="https://img.daisyui.com/images/stock/photo-1567653418876-5bb0e566e1c2.webp" />
```





---





# Stack

Stack visually puts elements on top of each other.

## Component Details

| Class name   | Type      |                                                          |
| ------------ | --------- | -------------------------------------------------------- |
| stack        | Component | Puts the children elements on top of each other          |
| stack-top    | Modifier  | Aligns the children elements to the top                  |
| stack-bottom | Modifier  | Aligns the children elements to the bottom[Default]      |
| stack-start  | Modifier  | Aligns the children elements to the start (horizontally) |
| stack-end    | Modifier  | Aligns the children elements to the end (horizontally)   |

## HTML Examples

### 3 divs in a stack

```html
<div class="stack h-20 w-32">
  <div class="bg-primary text-primary-content grid place-content-center rounded-box">1</div>
  <div class="bg-accent text-accent-content grid place-content-center rounded-box">2</div>
  <div class="bg-secondary text-secondary-content grid place-content-center rounded-box">
    3
  </div>
</div>
```

### stacked images

```html
<div class="stack w-48">
  <img src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp" class="rounded-box" />
  <img src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp" class="rounded-box" />
  <img src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp" class="rounded-box" />
</div>
```

### stacked cards

```html
<div class="stack size-28">
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">A</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">B</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">C</div>
  </div>
</div>
```

### stacked cards (top direction)

```html
<div class="stack stack-top size-28">
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">A</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">B</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">C</div>
  </div>
</div>
```

### stacked cards (start direction)

```html
<div class="stack stack-start size-28">
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">A</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">B</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">C</div>
  </div>
</div>
```

### stacked cards (end direction)

```html
<div class="stack stack-end size-28">
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">A</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">B</div>
  </div>
  <div class="border-base-content card bg-base-100 border text-center">
    <div class="card-body">C</div>
  </div>
</div>
```

### stacked cards with shadow

```html
<div class="stack">
  <div class="card bg-base-200 text-center shadow-md">
    <div class="card-body">A</div>
  </div>
  <div class="card bg-base-200 text-center shadow">
    <div class="card-body">B</div>
  </div>
  <div class="card bg-base-200 text-center shadow-sm">
    <div class="card-body">C</div>
  </div>
</div>
```

### stacked cards

```html
<div class="stack">
  <div class="card shadow-md bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Notification 1</h2>
      <p>You have 3 unread messages. Tap here to see.</p>
    </div>
  </div>
  <div class="card shadow-md bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Notification 2</h2>
      <p>You have 3 unread messages. Tap here to see.</p>
    </div>
  </div>
  <div class="card shadow-md bg-base-100">
    <div class="card-body">
      <h2 class="card-title">Notification 3</h2>
      <p>You have 3 unread messages. Tap here to see.</p>
    </div>
  </div>
</div>
```

