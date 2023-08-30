# Python Variable Annotations Project

This repository contains the Python Variable Annotations project, which focuses on enhancing your understanding of type annotations in Python 3. Through a series of tasks, you'll learn how to use type annotations effectively, work with various data types, and validate your code using tools like `mypy`. This README provides a concise overview of the project structure and how to get started.

## Learning Objectives

- Understand type annotations in Python 3.
- Utilize type annotations to specify function signatures and variable types.
- Implement duck typing and grasp its significance.
- Validate code using `mypy`.

## Project Structure

The project consists of tasks that involve writing type-annotated functions, working with complex data types, and practicing duck typing. Each task has specific requirements and test scripts to validate your implementations.

## Getting Started

1. Clone the repository.
2. Navigate to the task folder you want to work on.
3. Implement the function(s) according to the task requirements and annotate types.
4. Run the provided test script for the task to validate your code.
5. Adjust your code as necessary to meet the requirements.

## Running Tests

To run the test scripts for a specific task, use the following command:

```bash
./<task>-main.py
```

Replace `<task>` with the task number you want to test. Successful tests will display expected results and annotations used in the functions.

## Example Task

Let's take a look at how the tasks are structured:

### Task: Basic Annotations - add

Implement a function `add` that takes two float arguments and returns their sum.

**Example:**

```python
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
```

## Conclusion

The Python Variable Annotations project is designed to provide you with hands-on experience in working with type annotations and enhancing your coding skills. By completing the tasks and running tests, you'll gain practical knowledge that is essential for producing reliable and maintainable Python code.

Happy coding! 🐍💻
