#!/usr/bin/env python3
"""
Test script to validate understanding of cjm-tailwind-utils library.

This script tests various patterns and methods to ensure correct usage
of the cjm-tailwind-utils library based on CLI tool research.
"""

from cjm_tailwind_utils.all import tw

def test_basic_methods():
    """Test basic single method calls that return strings directly."""
    print("=== Testing Basic Methods (Return Strings) ===")
    
    tests = [
        # Text utilities
        ("tw.text(size='xl')", tw.text(size="xl"), "text-xl"),
        ("tw.text(size='4xl')", tw.text(size="4xl"), "text-4xl"),
        ("tw.font('bold')", tw.font("bold"), "font-bold"),
        
        # Layout utilities  
        ("tw.flex()", tw.flex(), "flex"),
        ("tw.flex(direction='col')", tw.flex(direction="col"), "flex-col"),
        ("tw.flex(wrap='wrap')", tw.flex(wrap="wrap"), "flex-wrap"),
        ("tw.flex(direction='col', wrap='wrap')", tw.flex(direction="col", wrap="wrap"), "flex-col flex-wrap"),
        
        # Spacing
        ("tw.m(4)", tw.m(4), "m-4"),
        ("tw.m(8, 'b')", tw.m(8, "b"), "mb-8"),
        ("tw.p(6)", tw.p(6), "p-6"),
        ("tw.p(4, 'x')", tw.p(4, "x"), "px-4"),
        ("tw.gap(2)", tw.gap(2), "gap-2"),
        ("tw.space(6, 'y')", tw.space(6, "y"), "space-y-6"),
        
        # Sizing
        ("tw.w(12)", tw.w(12), "w-12"),
        ("tw.h(12)", tw.h(12), "h-12"),
        ("tw.min_h('screen')", tw.min_h("screen"), "min-h-screen"),
        
        # Positioning
        ("tw.position('sticky')", tw.position("sticky"), "sticky"),
        ("tw.inset(0, 'top')", tw.inset(0, "top"), "top-0"),
        ("tw.z(50)", tw.z(50), "z-50"),
        
        # Alignment
        ("tw.items('center')", tw.items("center"), "items-center"),
        ("tw.justify('end')", tw.justify("end"), "justify-end"),
        ("tw.justify('center')", tw.justify("center"), "justify-center"),
        
        # Styling
        ("tw.rounded('lg')", tw.rounded("lg"), "rounded-lg"),
        ("tw.shadow('xl')", tw.shadow("xl"), "shadow-xl"),
        ("tw.cursor('pointer')", tw.cursor("pointer"), "cursor-pointer"),
        
        # Grid
        ("tw.grid(cols=1)", tw.grid(cols=1), "grid grid-cols-1"),
    ]
    
    all_passed = True
    for test_name, actual, expected in tests:
        if actual == expected:
            print(f"✅ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
        else:
            print(f"❌ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
            all_passed = False
        print()
    
    return all_passed

def test_util_method():
    """Test the util method for raw CSS classes."""
    print("=== Testing Util Method ===")
    
    tests = [
        # Single class
        ("tw.util('btn')", tw.util("btn"), "btn"),
        
        # Multiple classes
        ("tw.util('btn', 'btn-primary')", tw.util("btn", "btn-primary"), "btn btn-primary"),
        
        # daisyUI classes
        ("tw.util('card', 'bg-base-100')", tw.util("card", "bg-base-100"), "card bg-base-100"),
        ("tw.util('navbar')", tw.util("navbar"), "navbar"),
        ("tw.util('mockup-code')", tw.util("mockup-code"), "mockup-code"),
        
        # Complex daisyUI classes
        ("tw.util('text-base-content/70')", tw.util("text-base-content/70"), "text-base-content/70"),
        ("tw.util('footer', 'footer-center')", tw.util("footer", "footer-center"), "footer footer-center"),
    ]
    
    all_passed = True
    for test_name, actual, expected in tests:
        if actual == expected:
            print(f"✅ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
        else:
            print(f"❌ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
            all_passed = False
        print()
    
    return all_passed

def test_chaining():
    """Test chaining methods using tw.chain()."""
    print("=== Testing Chaining ===")
    
    tests = [
        # Basic chaining
        ("tw.chain().text(size='xl').font('bold')", 
         tw.chain().text(size="xl").font("bold").build(), 
         "text-xl font-bold"),
        
        # Complex chaining
        ("tw.chain().flex().items('center').gap(2)", 
         tw.chain().flex().items("center").gap(2).build(), 
         "flex items-center gap-2"),
        
        # Chaining with positioning
        ("tw.chain().position('sticky').inset(0, 'top').z(50)", 
         tw.chain().position("sticky").inset(0, "top").z(50).build(), 
         "sticky top-0 z-50"),
        
        # Chaining with flex parameters
        ("tw.chain().flex(wrap='wrap').gap(4).justify('center')", 
         tw.chain().flex(wrap="wrap").gap(4).justify("center").build(), 
         "flex-wrap gap-4 justify-center"),
        
        # Chaining with flex direction
        ("tw.chain().flex(direction='col').items('center')", 
         tw.chain().flex(direction="col").items("center").build(), 
         "flex-col items-center"),
        
        # Mixed chaining with util
        ("tw.chain().w(12).h(12).rounded('lg').util('bg-primary')", 
         tw.chain().w(12).h(12).rounded("lg").util("bg-primary").build(), 
         "w-12 h-12 rounded-lg bg-primary"),
    ]
    
    all_passed = True
    for test_name, actual, expected in tests:
        if actual == expected:
            print(f"✅ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
        else:
            print(f"❌ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
            all_passed = False
        print()
    
    return all_passed

def test_string_concatenation():
    """Test proper string concatenation patterns."""
    print("=== Testing String Concatenation ===")
    
    tests = [
        # Util + single method
        ("tw.util('btn') + ' ' + tw.text(size='xl')", 
         tw.util("btn") + " " + tw.text(size="xl"), 
         "btn text-xl"),
        
        # Util + chained methods
        ("tw.util('card', 'bg-base-100') + ' ' + tw.chain().shadow('xl').p(4).build()", 
         tw.util("card", "bg-base-100") + " " + tw.chain().shadow("xl").p(4).build(), 
         "card bg-base-100 shadow-xl p-4"),
        
        # Multiple concatenations
        ("tw.util('navbar') + ' ' + tw.p(4, 'x') + ' ' + tw.z(10)", 
         tw.util("navbar") + " " + tw.p(4, "x") + " " + tw.z(10), 
         "navbar px-4 z-10"),
    ]
    
    all_passed = True
    for test_name, actual, expected in tests:
        if actual == expected:
            print(f"✅ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
        else:
            print(f"❌ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
            all_passed = False
        print()
    
    return all_passed

def test_responsive_variants():
    """Test responsive variant methods."""
    print("=== Testing Responsive Variants ===")
    
    tests = [
        # Medium screen variants
        ("tw.md(tw.grid(cols=2))", tw.md(tw.grid(cols=2)), "md:grid md:grid-cols-2"),
        
        # Large screen variants  
        ("tw.lg(tw.grid(cols=3))", tw.lg(tw.grid(cols=3)), "lg:grid lg:grid-cols-3"),
        
        # Mixed with util (responsive classes need util)
        ("tw.util('md:grid-cols-2', 'lg:grid-cols-3')", 
         tw.util("md:grid-cols-2", "lg:grid-cols-3"), 
         "md:grid-cols-2 lg:grid-cols-3"),
    ]
    
    all_passed = True
    for test_name, actual, expected in tests:
        if actual == expected:
            print(f"✅ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
        else:
            print(f"❌ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
            all_passed = False
        print()
    
    return all_passed

def test_type_safety():
    """Test type safety and error cases."""
    print("=== Testing Type Safety ===")
    
    # Test that these should work
    try:
        result1 = tw.text(size="xl")  # Valid size
        print(f"✅ tw.text(size='xl') -> '{result1}'")
    except Exception as e:
        print(f"❌ tw.text(size='xl') failed: {e}")
    
    try:
        result2 = tw.flex(direction="col")  # Valid direction
        print(f"✅ tw.flex(direction='col') -> '{result2}'")
    except Exception as e:
        print(f"❌ tw.flex(direction='col') failed: {e}")
    
    try:
        result3 = tw.flex(wrap="wrap")  # Valid wrap
        print(f"✅ tw.flex(wrap='wrap') -> '{result3}'")
    except Exception as e:
        print(f"❌ tw.flex(wrap='wrap') failed: {e}")
    
    print()

def test_common_patterns():
    """Test the patterns we actually use in the testing notebook."""
    print("=== Testing Common Patterns from Testing Notebook ===")
    
    tests = [
        # Title styling
        ("Title styling", 
         tw.chain().text(size="4xl").font("bold").m(8, "b").build(),
         "text-4xl font-bold mb-8"),
        
        # Flex container with items and gap
        ("Flex container",
         tw.chain().flex().items("center").gap(2).build(),
         "flex items-center gap-2"),
        
        # Button with daisyUI classes
        ("Button classes",
         tw.util("btn", "btn-primary"),
         "btn btn-primary"),
        
        # Card with mixed classes
        ("Card with shadow and padding",
         tw.util("card", "bg-base-100") + " " + tw.chain().shadow("xl").p(4).build(),
         "card bg-base-100 shadow-xl p-4"),
        
        # Grid with responsive
        ("Responsive grid",
         tw.chain().grid(cols=1).util("md:grid-cols-2", "lg:grid-cols-3").gap(6).build(),
         "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"),
        
        # Sticky positioning
        ("Sticky navbar",
         tw.chain().position("sticky").inset(0, "top").z(50).build(),
         "sticky top-0 z-50"),
        
        # Flex with wrap
        ("Flex wrap layout",
         tw.chain().flex(wrap="wrap").gap(4).justify("center").build(),
         "flex-wrap gap-4 justify-center"),
        
        # Color palette swatch
        ("Color swatch",
         tw.chain().w(12).h(12).rounded("lg").util("bg-primary").build(),
         "w-12 h-12 rounded-lg bg-primary"),
    ]
    
    all_passed = True
    for test_name, actual, expected in tests:
        if actual == expected:
            print(f"✅ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
        else:
            print(f"❌ {test_name}")
            print(f"   Expected: '{expected}'")
            print(f"   Actual:   '{actual}'")
            all_passed = False
        print()
    
    return all_passed

def main():
    """Run all tests and provide summary."""
    print("🧪 Testing cjm-tailwind-utils Understanding")
    print("=" * 50)
    print()
    
    test_results = [
        test_basic_methods(),
        test_util_method(), 
        test_chaining(),
        test_string_concatenation(),
        test_responsive_variants(),
        test_common_patterns(),
    ]
    
    # Type safety test doesn't return boolean
    test_type_safety()
    
    print("=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)
    
    passed_tests = sum(test_results)
    total_tests = len(test_results)
    
    if all(test_results):
        print(f"🎉 ALL TESTS PASSED! ({passed_tests}/{total_tests})")
        print()
        print("✅ Understanding of cjm-tailwind-utils is CORRECT")
        print("✅ Ready to use in cjm-fasthtml-daisyui project")
    else:
        print(f"⚠️  SOME TESTS FAILED ({passed_tests}/{total_tests})")
        print()
        print("❌ Understanding needs refinement")
        
        failed_tests = total_tests - passed_tests
        print(f"📝 {failed_tests} test section(s) need attention")

if __name__ == "__main__":
    main()