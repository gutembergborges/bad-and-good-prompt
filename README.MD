# Prompt Engineering Essentials Examples

A collection of bad and good prompts to demonstrate how to create, modify, and improve code using AI assistants.

## 📁 Project Structure

```
├── bad-simple-prompt/
│   └── [filename].py       # Code generated from vague, unstructured prompts
├── improved-better-prompt/
│   └── [filename].py       # Code generated from clear, structured prompts
└── README.md
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

1. Navigate to any example folder
2. Compare `bad-simple-prompt/[file].py` with `improved-better-prompt/[file].py`
3. Review the prompt used for each (included as comments at the top of each file)
4. Observe differences in code quality, structure, and maintainability

## 📖 Best Practices Demonstrated

Each improved prompt follows these principles:

- **Specificity**: Clear task definition with measurable outcomes
- **Context**: Background information and use case
- **Constraints**: Limitations and requirements explicitly stated
- **Format**: Expected output structure defined
- **Examples**: Few-shot examples when applicable

## 🛠️ Running the Examples

```bash
# Navigate to an example
cd bad-simple-prompt

# Run the code (if applicable)
python3 [filename].py

# Compare with improved version
cd ../improved-better-prompt
python3 [filename].py
```

## 📝 Contributing

To add new examples:

1. Create a pair of files with the same name in both folders
2. Include the exact prompt used as a comment at the top
3. Ensure the bad prompt demonstrates common mistakes
4. Ensure the good prompt follows best practices

## 📄 License

MIT License - Feel free to use these examples in your learning or teaching.

---

**Tip**: Use this repo as a reference when crafting your own prompts. Remember: *garbage in, garbage out* applies to AI just as much as traditional programming.



