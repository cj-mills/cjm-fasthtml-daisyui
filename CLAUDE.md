This is an nbdev project, called `cjm-fasthtml-daisyui` (`cjm` is my initials).

The goal for this project is to provide a fully Python-abstracted UI component library that provides reusable components built with [Tailwind CSS v4](https://tailwindcss.com/blog/tailwindcss-v4) and [daisyUI v5](https://daisyui.com/docs/v5/) for [FastHTML](https://www.fastht.ml/docs/) projects.

Requirements the the project:

- Provide a complete abstraction system for dynamically creating components leveraging daisyUI and Tailwind
- Fully abstracted usage of [Tailwind CSS v4](https://tailwindcss.com/blog/tailwindcss-v4) through the [`cjm-tailwind-utils`](https://cj-mills.github.io/cjm-tailwind-utils/) library (already installed)
- Optimize for maintainability across daisyUI and Tailwind version changes
- Maximize easy-of-use for building FastHTML projects with the library
- Minimize code needed to use the library
- Full type safety throughout
- ALL CSS strings for daisyUI and Tailwind must be dynamically-generated through Python
- No hardcoded CSS strings needed to use the library.

Tailwind CSS-specific functionality is abstracted through the `cjm-tailwind-utils` library (which you can learn about with `cjm-tailwind-utils -h`). Use the `cjm-tailwind-utils` CLI tool as needed to understand proper usage.

An overview of [daisyUI v5](https://daisyui.com/docs/v5/) is available in the `./claude-docs/daisyUI-5-llms-txt.md` Markdown document  for you to access as needed.

Regarding daisyUI component coverage, I plan to have a dedicated notebook for each of the 61 daisyUI component types organized as follows:

```
nbs/
├── actions/
│   ├── button.ipynb 
│   ├── dropdown.ipynb 
│   ├── modal.ipynb 
│   ├── swap.ipynb 
│   └── theme_controller.ipynb 
├── data_display/
│   ├── accordion.ipynb 
│   ├── avatar.ipynb 
│   ├── badge.ipynb 
│   ├── card.ipynb 
│   ├── carousel.ipynb 
│   ├── chat.ipynb 
│   ├── collapse.ipynb 
│   ├── countdown.ipynb 
│   ├── diff.ipynb 
│   ├── kbd.ipynb 
│   ├── list.ipynb 
│   ├── stat.ipynb 
│   ├── status.ipynb 
│   ├── table.ipynb 
│   └── timeline.ipynb 
├── data_input/
│   ├── calendar.ipynb 
│   ├── checkbox.ipynb 
│   ├── fieldset.ipynb 
│   ├── file_input.ipynb 
│   ├── filter.ipynb 
│   ├── label.ipynb 
│   ├── radio.ipynb 
│   ├── range.ipynb 
│   ├── rating.ipynb 
│   ├── select.ipynb 
│   ├── text_input.ipynb 
│   ├── textarea.ipynb 
│   ├── toggle.ipynb 
│   └── validator.ipynb 
├── feedback/
│   ├── alert.ipynb 
│   ├── loading.ipynb 
│   ├── progress.ipynb 
│   ├── radial_progress.ipynb 
│   ├── skeleton.ipynb 
│   ├── toast.ipynb 
│   └── tooltip.ipynb 
├── layout/
│   ├── divider.ipynb 
│   ├── drawer.ipynb 
│   ├── footer.ipynb 
│   ├── hero.ipynb 
│   ├── indicator.ipynb 
│   ├── join.ipynb 
│   ├── mask.ipynb 
│   └── stack.ipynb 
├── mockup/
│   ├── mockup_browser.ipynb 
│   ├── mockup_code.ipynb 
│   ├── mockup_phone.ipynb 
│   └── mockup_window.ipynb 
└── navigation/
    ├── breadcrumbs.ipynb 
    ├── dock.ipynb 
    ├── link.ipynb 
    ├── menu.ipynb 
    ├── navbar.ipynb 
    ├── pagination.ipynb 
    ├── steps.ipynb 
    └── tab.ipynb 
```



Since this is an nbdev project, we make changes in the `.ipynb` Jupyter Notebooks in the `./nbs/` directory and do not directly change the auto-generated Python files.

Always use the NotebookRead tool to read any `.ipynb` files.

Always use the NotebookEdit tool to edit any `.ipynb` files.

Read the `nbs/index.ipynb` notebook for context about the current state of the `cjm-fasthtml-daisyui` project. The information `nbs/index.ipynb` notebook is auto-updated using the `nbdev-overview update-comprehensive` command.