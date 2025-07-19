#!/usr/bin/env python3
"""
Corrected test script for cjm-tailwind-utils library.

This script tests the CORRECT usage patterns based on the library's actual design.
"""

from cjm_tailwind_utils.all import tw

def test_corrected_patterns():
    """Test the corrected usage patterns."""
    print("=== Testing Corrected Usage Patterns ===")
    
    tests = [
        # CORRECTED: Font weight via text method
        ("Font weight", tw.text(weight="bold"), "font-bold"),
        ("Font family", tw.font("sans"), "font-sans"),
        
        # CORRECTED: Flex always includes base flex
        ("Flex with direction", tw.flex(direction="col"), "flex flex-col"),
        ("Flex with wrap", tw.flex(wrap="wrap"), "flex flex-wrap"),
        ("Flex with both", tw.flex(direction="col", wrap="wrap"), "flex flex-col flex-wrap"),
        
        # CORRECTED: Responsive with string classes  
        ("Responsive grid", tw.md("grid", "grid-cols-2"), "md:grid md:grid-cols-2"),
        ("Responsive lg", tw.lg("grid", "grid-cols-3"), "lg:grid lg:grid-cols-3"),
        
        # CORRECT: Title styling (using text method)
        ("Title styling", 
         tw.chain().text(size="4xl", weight="bold").m(8, "b").build(),
         "text-4xl font-bold mb-8"),
        
        # CORRECT: Flex wrap (includes base flex)
        ("Flex wrap layout",
         tw.chain().flex(wrap="wrap").gap(4).justify("center").build(),
         "flex flex-wrap gap-4 justify-center"),
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

def test_notebook_patterns():
    """Test patterns from our testing notebook with corrections."""
    print("=== Testing Notebook Patterns (Corrected) ===")
    
    tests = [
        # What we SHOULD use in the notebook
        ("Title (corrected)", 
         tw.chain().text(size="4xl", weight="bold").m(8, "b").build(),
         "text-4xl font-bold mb-8"),
        
        ("Flex container (already correct)",
         tw.chain().flex().items("center").gap(2).build(),
         "flex items-center gap-2"),
        
        ("Flex with wrap (corrected understanding)",
         tw.chain().flex(wrap="wrap").gap(4).justify("center").build(),
         "flex flex-wrap gap-4 justify-center"),
        
        # This is CORRECT - we should use util for responsive grid classes
        ("Responsive grid (using util - correct)",
         tw.chain().grid(cols=1).util("md:grid-cols-2", "lg:grid-cols-3").gap(6).build(),
         "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"),
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
    """Run corrected tests."""
    print("🔧 Testing CORRECTED cjm-tailwind-utils Usage")
    print("=" * 50)
    print()
    
    test_results = [
        test_corrected_patterns(),
        test_notebook_patterns(),
    ]
    
    print("=" * 50)
    print("📊 CORRECTED UNDERSTANDING SUMMARY")
    print("=" * 50)
    
    if all(test_results):
        print("🎉 ALL CORRECTED TESTS PASSED!")
        print()
        print("✅ Font weight: Use tw.text(weight='bold')")
        print("✅ Flex: tw.flex(direction='col') → 'flex flex-col' (includes base)")
        print("✅ Responsive: Use tw.util() for complex responsive classes")
        print("✅ Understanding is now CORRECT")
    else:
        print("❌ Still some issues to resolve")

if __name__ == "__main__":
    main()