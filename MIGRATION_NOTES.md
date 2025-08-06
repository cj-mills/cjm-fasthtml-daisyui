# daisyUI v5 Test Migration Notes

## Overview
This document contains notes for migrating test functions in the `nbs/components/` notebooks to use examples from the daisyUI v5 documentation.

## Key Patterns and Lessons Learned

### 1. General Migration Strategy
- Replace single `test_<component>_practical_examples()` functions with multiple focused test functions
- Group examples logically by feature/complexity rather than having one large function
- Name functions descriptively: `test_<component>_<feature>_examples()`

### 2. Import Patterns
Always import utilities from the correct modules:
```python
# From cjm-fasthtml-tailwind
from cjm_fasthtml_tailwind.utilities.spacing import m, p, ps
from cjm_fasthtml_tailwind.utilities.layout import z, position, right, top, display_tw
from cjm_fasthtml_tailwind.utilities.sizing import w, h, max_w, size_util
from cjm_fasthtml_tailwind.utilities.typography import text, font
from cjm_fasthtml_tailwind.utilities.svg import fill, stroke, stroke_width
from cjm_fasthtml_tailwind.utilities.flexbox_and_grid import flex, items, justify
from cjm_fasthtml_tailwind.utilities.effects import shadow
from cjm_fasthtml_tailwind.utilities.backgrounds import bg
from cjm_fasthtml_tailwind.core.base import combine_classes

# From cjm-fasthtml-daisyui
from cjm_fasthtml_daisyui.core.utility_classes import bg_dui, text_dui, border_radius, glass
```

### 3. Common Gotchas

#### FastHTML Attribute Conversions
- `for_` becomes `for-` in attrs: `assert element.attrs['for-'] == "value"`
- Underscores in parameter names are converted to hyphens in HTML attributes

#### Display Utilities
- Use `display_tw.flex` not just `flex` for display utilities
- The `display_tw` factory provides: `block`, `inline`, `flex`, `grid`, `hidden`, etc.

#### Semantic Colors
- Use `text_dui.info` for semantic text colors (not `text.info`)
- Available semantic color factories: `bg_dui`, `text_dui`, `border_dui`, `fill_dui`, `stroke_dui`

#### Arbitrary Values
- Use parentheses for arbitrary values: `w("11/12")`, `size_util("1.2em")`
- Not subscript notation like `w['11/12']`

#### daisyUI-Specific Classes
Keep these as strings (they're not in the Tailwind factories):
- Component classes: `"menu"`, `"card"`, `"navbar"`, `"card-body"`, `"card-title"`
- Special classes: `"rounded-field"`, `"loading loading-spinner"`
- Component-specific modifiers that aren't in factories

### 4. Testing Patterns

#### Component Structure
- Test the HTML structure thoroughly
- Verify tag names: `assert element.tag == "dialog"`
- Check parent-child relationships
- Verify all expected CSS classes are present

#### Reusable Components
- Create SVG icons once and reuse them within the same test function
- Use helper functions to reduce duplication (e.g., `create_dropdown_content()`)

#### Assertion Patterns
```python
# Check tag type
assert element.tag == "button"

# Check attributes
assert element.attrs['id'] == "my_id"
assert element.attrs['class'] == "single-class"
assert "class-name" in element.attrs['class']  # When multiple classes

# Check children
assert len(element.children) == 3
assert element.children[0].tag == "input"
assert element.children[1].children[0] == "Text content"
```

### 5. Component-Specific Notes

#### Buttons
- Test all variants: colors, styles, sizes, modifiers, behaviors
- Test with different HTML elements (Button, A, Input)
- Remember disabled state can use attribute or class

#### Dropdowns
- Test all placement combinations (top/bottom/left/right + start/center/end)
- Include popover API example with anchor positioning
- Test both hover and click triggers

#### Modals
- Three methods: dialog (recommended), checkbox (legacy), anchor (legacy)
- Dialog method uses native HTML5 `<dialog>` element
- Test onclick handlers: `onclick="my_modal_1.showModal()"`

#### Swap
- Test with and without checkbox control
- Include rotate and flip animation effects
- Test class-based activation (`swap-active`)
- Don't forget indeterminate state support

### 6. File Organization
When creating new test functions:
1. Find the existing `test_<component>_practical_examples()` function
2. Get the cell ID using grep
3. Replace with multiple focused test functions
4. Insert additional functions after the first one
5. Update todo list to track progress

### 7. Testing Command
Always test code with `cjm-tailwind-explore test-code` before adding to notebook to catch syntax errors early.

### 8. Documentation References
- daisyUI v5 docs: Check each component's HTML examples section
- Use `cjm-tailwind-explore` to find correct factory names and usage
- Check `./nbs/core/utility_classes.ipynb` for daisyUI-specific utilities