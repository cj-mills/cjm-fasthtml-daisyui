# daisyUI v5 Test Creation Guide

## Overview
This document provides guidelines for creating test functions for components in the `nbs/components/` notebooks using examples from the daisyUI v5 documentation.

## Key Principles

### 1. Test Function Structure
- Create multiple focused test functions per component rather than one monolithic function
- Name functions descriptively: `test_<component>_<example-name>_fasthtml_examples()`
- Group related examples logically (e.g., by variant, complexity, or feature type)
- Each test function should demonstrate a specific aspect or use case

### 2. Standard Import Pattern
Always include necessary imports at the beginning of test cells:
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

### 3. Creating Test Functions

#### Step-by-Step Process
1. Review the daisyUI v5 documentation for the component
2. Identify key features and variants to test
3. Create logical groupings for test functions
4. Implement examples from the documentation
5. Add comprehensive assertions to verify structure

#### Test Function Template
```python
def test_<component>_<example-name>_fasthtml_examples():
    """Test <component> <example-name> implementations based on daisyUI v5 examples."""
    print(f"Testing {<Component>.__name__} <example-name> examples")
    
    # Example 1: Basic implementation
    element = <Component>(
        "Content",
        cls="component-class",
        # Additional attributes
    )
    
    # Assertions
    assert element.tag == "expected_tag"
    assert "expected-class" in element.attrs['class']
    assert len(element.children) == expected_count
    
    # Example 2: More complex variant
    # ...
    
    print("✓ All <example-name> examples pass")
```

#### Complete Example: Badge with Icons
```python
#| export
def test_badge_icon_fasthtml_examples():
    """Test badge with icon from daisyUI v5 documentation."""
    from fasthtml.common import Div
    from fasthtml.svg import Svg, G, Circle, Path, Polyline, Rect, Line
    from cjm_fasthtml_tailwind.utilities.sizing import size_util
    from cjm_fasthtml_tailwind.utilities.svg import fill, stroke, stroke_width
    
    # Create reusable SVG icons
    info_icon = Svg(
        G(
            Circle(cx="12", cy="12", r="10", fill="none", stroke="currentColor", 
                   stroke_linecap="square", stroke_miterlimit="10", stroke_width="2"),
            Path(d="m12,17v-5.5c0-.276-.224-.5-.5-.5h-1.5", fill="none", stroke="currentColor", 
                 stroke_linecap="square", stroke_miterlimit="10", stroke_width="2"),
            Circle(cx="12", cy="7.25", r="1.25", fill="currentColor", stroke_width="2"),
            fill="currentColor", stroke_linejoin="miter", stroke_linecap="butt"
        ),
        cls=str(size_util("[1em]")), xmlns="http://www.w3.org/2000/svg", viewBox="0 0 24 24"
    )
    
    success_icon = Svg(
        G(
            Circle(cx="12", cy="12", r="10", fill="none", stroke="currentColor", 
                   stroke_linecap="square", stroke_miterlimit="10", stroke_width="2"),
            Polyline(points="7 13 10 16 17 8", fill="none", stroke="currentColor", 
                      stroke_linecap="square", stroke_miterlimit="10", stroke_width="2"),
            fill="currentColor", stroke_linejoin="miter", stroke_linecap="butt"
        ),
        cls=str(size_util("[1em]")), xmlns="http://www.w3.org/2000/svg", viewBox="0 0 24 24"
    )
    
    warning_icon = Svg(
        G(
            Path(d="M7.638,3.495L2.213,12.891c-.605,1.048,.151,2.359,1.362,2.359H14.425c1.211,0,1.967-1.31,1.362-2.359L10.362,3.495c-.605-1.048-2.119-1.048-2.724,0Z", 
                 fill="none", stroke="currentColor", stroke_linecap="round", stroke_linejoin="round", stroke_width="1.5"),
            Line(x1="9", y1="6.5", x2="9", y2="10", fill="none", stroke="currentColor", 
                 stroke_linecap="round", stroke_linejoin="round", stroke_width="1.5"),
            Path(d="M9,13.569c-.552,0-1-.449-1-1s.448-1,1-1,1,.449,1,1-.448,1-1,1Z", 
                 fill="currentColor", data_stroke="none", stroke="none"),
            fill="currentColor"
        ),
        cls=str(size_util("[1em]")), xmlns="http://www.w3.org/2000/svg", viewBox="0 0 18 18"
    )
    
    error_icon = Svg(
        G(
            Rect(x="1.972", y="11", width="20.056", height="2", 
                 transform="translate(-4.971 12) rotate(-45)", fill="currentColor", stroke_width="0"),
            Path(d="m12,23c-6.065,0-11-4.935-11-11S5.935,1,12,1s11,4.935,11,11-4.935,11-11,11Zm0-20C7.038,3,3,7.037,3,12s4.038,9,9,9,9-4.037,9-9S16.962,3,12,3Z", 
                 stroke_width="0", fill="currentColor"),
            fill="currentColor"
        ),
        cls=str(size_util("[1em]")), xmlns="http://www.w3.org/2000/svg", viewBox="0 0 24 24"
    )
    
    # Badge with icon
    info_badge = Div(
        info_icon,
        "Info",
        cls=combine_classes(badge, badge_colors.info)
    )
    assert info_badge.tag == "div"
    assert "badge" in info_badge.attrs['class']
    assert "badge-info" in info_badge.attrs['class']
    assert info_badge.children[0].tag == "svg"
    assert info_badge.children[1] == "Info"
    
    success_badge = Div(
        success_icon,
        "Success",
        cls=combine_classes(badge, badge_colors.success)
    )
    assert "badge-success" in success_badge.attrs['class']
    assert success_badge.children[0].tag == "svg"
    assert success_badge.children[1] == "Success"
    
    warning_badge = Div(
        warning_icon,
        "Warning",
        cls=combine_classes(badge, badge_colors.warning)
    )
    assert "badge-warning" in warning_badge.attrs['class']
    assert warning_badge.children[0].tag == "svg"
    assert warning_badge.children[1] == "Warning"
    
    error_badge = Div(
        error_icon,
        "Error",
        cls=combine_classes(badge, badge_colors.error)
    )
    assert "badge-error" in error_badge.attrs['class']
    assert error_badge.children[0].tag == "svg"
    assert error_badge.children[1] == "Error"
    
    # Return all elements in a Div
    return Div(
        info_badge,
        success_badge,
        warning_badge,
        error_badge
    )

# Run the tests
test_badge_icon_fasthtml_examples()
```

### 4. Common Implementation Patterns

#### HTML Attribute Handling
- FastHTML converts `for_` to `for-` in attributes
- Underscores in parameter names become hyphens in HTML
- Use `attrs` dict for accessing rendered attributes

#### Utility Class Usage
- **Display utilities**: Use `display_tw.flex`, `display_tw.block`, etc.
- **Semantic colors**: Use specialized factories like `text_dui.info`, `bg_dui.primary`
- **Arbitrary values**: Use function call syntax: `w("11/12")`, `size_util("1.2em")`
- **daisyUI classes**: Keep as strings for component-specific classes

#### Component Testing Strategy
- Test core functionality first (basic usage)
- Add variant tests (colors, sizes, styles)
- Include modifier tests (states, behaviors)
- Test complex compositions and real-world examples
- Verify accessibility attributes where applicable

### 5. Assertion Best Practices

#### Structure Verification
```python
# Tag verification
assert element.tag == "button"

# Attribute checking
assert element.attrs['id'] == "my_id"
assert element.attrs['type'] == "submit"

# Class verification
assert "btn" in element.attrs['class']
assert all(cls in element.attrs['class'] for cls in ["btn", "btn-primary"])

# Children inspection
assert len(element.children) == 2
assert element.children[0].tag == "span"
assert element.children[1] == "Text content"

# Nested structure
assert element.children[0].children[0].tag == "svg"
```

#### Content Verification
- Check text content directly for string children
- Verify nested component structure
- Validate SVG and icon implementations
- Ensure proper HTML5 semantic structure

### 6. Component Categories

#### Actions
- **Button**: Test variants, sizes, states, with icons
- **Dropdown**: Test placements, triggers, content types
- **Modal**: Test dialog method, close buttons, backdrops
- **Swap**: Test animation types, checkbox control, states
- **Theme Controller**: Test toggle types, value persistence

#### Data Display
- **Accordion**: Test collapse behavior, icons, join styles
- **Avatar**: Test sizes, shapes, groups, placeholders
- **Badge**: Test colors, sizes, positioning
- **Card**: Test layouts, images, actions, glass effect
- **Carousel**: Test navigation, indicators, snap behavior

#### Data Input
- **Checkbox**: Test sizes, colors, indeterminate state
- **File Input**: Test variants, sizes, validation states
- **Radio**: Test groups, custom designs, accessibility
- **Range**: Test steps, colors, tick marks
- **Select**: Test sizes, states, multiple selection
- **Text Input**: Test types, validation, helper text
- **Textarea**: Test resize behavior, states, character count
- **Toggle**: Test sizes, colors, with labels

#### Layout
- **Artboard**: Test responsive sizes, phone mockups
- **Divider**: Test orientations, text content, styles
- **Drawer**: Test positions, overlay behavior, responsive
- **Footer**: Test columns, responsive layout, centering
- **Hero**: Test overlays, content positioning, backgrounds
- **Indicator**: Test positions, stacking, animations
- **Join**: Test orientations, responsive behavior
- **Mask**: Test shapes, sizes, custom paths
- **Stack**: Test stacking context, responsive behavior

#### Navigation
- **Breadcrumbs**: Test separators, icons, overflow
- **Bottom Navigation**: Test active states, labels, badges
- **Link**: Test colors, hover effects, underline styles
- **Menu**: Test orientations, collapsible, active items
- **Navbar**: Test responsive behavior, dropdowns, centering
- **Pagination**: Test styles, active state, size variants
- **Steps**: Test orientations, states, custom content
- **Tab**: Test styles, sizes, active states, content switching

#### Feedback
- **Alert**: Test types, icons, actions, closable
- **Chat**: Test bubbles, images, typing indicators
- **Collapse**: Test icons, open/close behavior, focus styles
- **Countdown**: Test formats, animations, labels
- **Diff**: Test component comparison visualization
- **Kbd**: Test key combinations, sizes, themes
- **Loading**: Test types, sizes, colors, text
- **Progress**: Test values, colors, indeterminate
- **Radial Progress**: Test values, size, custom content
- **Skeleton**: Test shapes, animations, responsive
- **Stat**: Test layouts, values, descriptions, trends
- **Table**: Test pinning, zebra stripes, responsive
- **Timeline**: Test layouts, icons, connectors
- **Toast**: Test positions, durations, stacking
- **Tooltip**: Test positions, triggers, custom content

#### Mockup
- **Browser**: Test address bar, tabs, content area
- **Code**: Test syntax highlighting, line numbers, selection
- **Phone**: Test screen content, responsive sizing
- **Window**: Test titlebar, actions, content scrolling

### 7. Development Workflow

#### Creating New Tests
1. Review daisyUI v5 documentation for the component
2. Use `cjm-tailwind-explore` to verify factory methods and class names
3. Write test functions following the patterns above
4. Test code with `cjm-tailwind-explore test-code` before adding to notebook
5. Run the test function to ensure all assertions pass
6. Commit changes with descriptive messages

#### Debugging Tips
- Print intermediate values to debug complex structures
- Use `element.attrs` to inspect all rendered attributes
- Check `element.children` for nested component structure
- Verify class combinations with `combine_classes` utility
- Test with different component configurations

### 8. Resources and References

#### Documentation
- daisyUI v5 Components: https://daisyui.com/components/
- FastHTML Documentation: https://docs.fastht.ml/
- Tailwind CSS Utilities: https://tailwindcss.com/docs

#### Internal References
- Utility classes: `./nbs/core/utility_classes.ipynb`
- Component implementations: `./nbs/components/`
- Factory exploration: Use `cjm-tailwind-explore` command

#### Testing Tools
- `cjm-tailwind-explore test-code`: Validate Python syntax
- `cjm-tailwind-explore`: Explore available factories and utilities
- Component playground: Test combinations interactively

### 9. Common Pitfalls to Avoid

#### Import Errors
- Don't forget to import component classes from their modules
- Ensure all utility imports are from correct packages
- Avoid importing from wrong namespace (e.g., `text.info` vs `text_dui.info`)

#### Class String Formatting
- Don't mix factory methods and string literals incorrectly
- Remember that some daisyUI classes don't have factory equivalents
- Use `combine_classes` for complex class combinations

#### Assertion Failures
- Remember FastHTML's attribute transformations
- Check for multiple classes with `in` operator, not equality
- Account for child element wrapping in some components

#### Component Structure
- Some components require specific HTML structure
- Maintain proper parent-child relationships
- Include necessary ARIA attributes for accessibility

### 10. Best Practices Summary

1. **Start Simple**: Begin with basic examples, then add complexity
2. **Test Thoroughly**: Cover all documented variants and states
3. **Be Descriptive**: Use clear test function and variable names
4. **Follow Patterns**: Maintain consistency with existing tests
5. **Document Edge Cases**: Add comments for non-obvious implementations
6. **Verify Accessibility**: Include ARIA attributes and semantic HTML
7. **Reuse Code**: Create helper functions for repeated patterns
8. **Test Incrementally**: Run tests frequently during development
9. **Reference Documentation**: Always check daisyUI v5 examples
10. **Maintain Structure**: Keep tests organized and logical