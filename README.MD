# GOOD AND BAD: Prompt Engineering Essentials Examples

A collection of bad and good prompts to demonstrate how to create, modify, and improve code using AI assistants.

## 📁 Project Structure

```
├── bad-prompt/
│   └── [filename].py       # Code generated from bad, vague, unstructured prompts
├── good-prompt/
│   └── [filename].py       # Code generated from good, clear, structured prompts
└── README.md
```

## 📝 File Structure & Prompt Location

**Crucial Detail:** To facilitate direct comparison, the **exact prompt used to generate the code** is included at the very top of each source file.

- **Location:** Lines 1–N of every `.py` (or code) file.
- **Format:** Enclosed in a comment (`#`) or multi-line comment block (`"""` or `'''`).
- **Purpose:** Allows you to immediately see the input (prompt) that resulted in the output (code) below it without needing external documentation.

### Example File Layout

#### Bad Prompt Example
```python
# BAD PROMPT USED:
# "Write a function to add two numbers."
# (This is a bad example: lacks type hints, error handling, and context)

def add(a, b):
    return a + b
```

#### Good Prompt Example
```python
"""
GOOD PROMPT USED:
"Act as a Senior Python Developer. Create a robust function to add two numbers for a financial calculation module.

Requirements:
1. Use type hints for inputs (int or float) and return value.
2. Include a detailed docstring explaining parameters and return values.
3. Implement error handling to raise a TypeError if inputs are not numeric.
4. Do not use external libraries.

Output the final code only."
"""

def add_numbers(a: int | float, b: int | float) -> int | float:
    """
    Adds two numeric values safely.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an int or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric (int or float).")
    
    return a + b
```

## 🎯 Purpose

This repository illustrates the difference between **poorly crafted prompts** and **well-engineered prompts** when using AI to generate or modify code. Each example pair shows the same task attempted with two different prompt qualities.

## 📚 What You'll Learn

- **Bad prompts**: Vague, lacking context, no constraints → unpredictable or incomplete code
- **Good prompts**: Clear role, specific requirements, output format → production-ready code

## 🔍 Example Comparison

| Aspect | Bad Prompt | Good Prompt |
|--------|-----------|-------------|
| **Role** | ❌ Not defined | ✅ "Act as a senior Python developer" |
| **Context** | ❌ Missing | ✅ "For a data validation module in a Flask API" |
| **Requirements** | ❌ Vague | ✅ "Validate email, age 18+, return JSON with error codes" |
| **Format** | ❌ Unspecified | ✅ "Return a function with docstring and type hints" |
| **Constraints** | ❌ None | ✅ "No external libraries, handle edge cases" |

## 🚀 How to Use

1. Open any file in `bad-simple-prompt/` and read the **comment block at the top** to see the input.
2. Compare it with the corresponding file in `improved-better-prompt/` to see the better input.
3. Analyze how the difference in the prompt directly affects the code quality below the comment block.

## 📖 Best Practices Demonstrated

Each improved prompt follows these principles:

- **Specificity**: Clear task definition with measurable outcomes
- **Context**: Background information and use case
- **Constraints**: Limitations and requirements explicitly stated
- **Format**: Expected output structure defined
- **Examples**: Few-shot examples when applicable

## 👁️ Seeing the Examples

```bash
# Navigate to an example
cd bad-prompt

# View the prompt and code
cat [filename].py 

# Compare with improved version
cd ../good-prompt
cat [filename].py
```

## 🛠️ Running the Examples

```bash
# Navigate to an example
cd bad-prompt

# Run the code (if applicable)
python3 [filename].py

# Compare with improved version
python3 ../good-prompt/[filename].py
```

## 📝 Contributing

To add new examples:

1. Create a pair of files with the same name in both folders.
2. **Mandatory:** Insert the exact prompt used as a multi-line comment at the very top of the file.
3. Ensure the bad prompt demonstrates common mistakes.
4. Ensure the good prompt follows best practices.

## 📄 License

MIT License - Feel free to use these examples in your learning or teaching.

---

**Tip 1**: Always read the prompt header first. The quality of the code below is a direct reflection of the instructions above.

**Tip 2**: Use this repo as a reference when crafting your own prompts. Remember: *garbage in, garbage out* applies to AI just as much as traditional programming.

