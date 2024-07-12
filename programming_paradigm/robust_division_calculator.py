def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return "Error: Cannot divide by zero."
        return f"{num / den}"
    except ValueError:
        return "Error: Please enter numeric values only."
