def generate_explanation(result):
    explanation = ""

    explanation += f"The array has {result['length']} elements.\n"
    explanation += f"Total sum of elements is {result['sum']}.\n"

    if result["duplicates"]:
        explanation += f"Duplicate values found: {result['duplicates']}.\n"
    else:
        explanation += "No duplicates found.\n"

    explanation += (
        f"The longest consecutive sequence length is "
        f"{result['longest_consecutive']}.\n"
    )

    explanation += "This is computed using a HashSet for O(n) efficiency."

    return explanation
