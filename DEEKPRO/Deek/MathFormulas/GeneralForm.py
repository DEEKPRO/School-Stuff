import re
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter equation: ").strip()
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
        
    # Remove all spaces for easier parsing
    eq = user_input.replace(" ", "")
    
    if '=' not in eq:
        print("Error: Invalid equation. Missing '=' sign.\n")
        continue
        
    try:
        # Split into left-hand side (LHS) and right-hand side (RHS)
        lhs, rhs = eq.split('=')
        
        # Regex to parse terms (captures the sign, number, and variable if present)
        # e.g., "+3x", "-5y", "+9", "-7"
        term_pattern = re.compile(r'([+-]?\d*[a-zA-Z]?|[+-]?\d+)')
        
        # Helper function to extract A, B, C coefficients from a side
        def extract_coefficients(side_str, multiply_by=1):
            a, b, c = 0, 0, 0
            # Find all matching terms on this side
            terms = term_pattern.findall(side_str)
            
            for term in terms:
                if not term:
                    continue
                if 'x' in term:
                    coeff = term.replace('x', '')
                    if coeff == '' or coeff == '+': coeff = '1'
                    elif coeff == '-': coeff = '-1'
                    a += int(coeff) * multiply_by
                elif 'y' in term:
                    coeff = term.replace('y', '')
                    if coeff == '' or coeff == '+': coeff = '1'
                    elif coeff == '-': coeff = '-1'
                    b += int(coeff) * multiply_by
                else:
                    c += int(term) * multiply_by
            return a, b, c

        # Terms on LHS keep their sign (multiply_by = 1)
        # Terms on RHS flip their sign when moved to LHS (multiply_by = -1)
        A1, B1, C1 = extract_coefficients(lhs, 1)
        A2, B2, C2 = extract_coefficients(rhs, -1)
        
        # Combine the coefficients on the left side
        A = A1 + A2
        B = B1 + B2
        C = C1 + C2
        
        # Standard convention: Keep the 'x' coefficient (A) positive
        if A < 0:
            A, B, C = -A, -B, -C
            
        # Format the final string nicely
        def format_term(val, var, is_first=False):
            if val == 0:
                return ""
            sign = "+" if val > 0 else "-"
            abs_val = abs(val)
            
            # Drop the '1' multiplier for variables (e.g., write 'x', not '1x')
            val_str = "" if (abs_val == 1 and var) else str(abs_val)
            
            if is_first:
                return f"-{val_str}{var}" if sign == "-" else f"{val_str}{var}"
            else:
                return f" {sign} {val_str}{var}"

        part_a = format_term(A, 'x', is_first=True)
        part_b = format_term(B, 'y', is_first=(A == 0))
        part_c = format_term(C, '', is_first=(A == 0 and B == 0))
        
        general_form = f"{part_a}{part_b}{part_c} = 0".strip()
        print(f"General Form: {general_form}\n")
        
    except Exception as e:
        print("Error: Could not parse equation. Check your format and try again.\n")