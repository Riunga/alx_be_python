def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return "Error: Division by zero is not allowed."
        return num / den
    except ValueError:
        return "Error: Non-numeric input provided."
