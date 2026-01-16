def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * ((1 + r / 100) ** t) - p
    return (
        f"Simple Interest: {si}\n"
        f"Compound Interest: {ci}"
    )
