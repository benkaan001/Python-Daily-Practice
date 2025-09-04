# Python Daily Practice for Back-End Engineers

A curated collection of daily coding challenges designed for intermediate developers preparing for back-end engineering roles. This repository focuses on strengthening problem-solving skills in data structures, algorithms, and modern software engineering practices.

### Features & Philosophy

This is more than just a collection of solutions; it's a simulation of a professional engineering workflow.

* **Automated Testing (CI/CD):** Every push to the repository triggers a GitHub Action that automatically runs all tests with `pytest`, ensuring every solution is correct and no existing solutions have broken.
* **Code Quality Enforcement:** The pipeline also checks code style and quality using `flake8`, maintaining a high standard for readability and maintainability.
* **Test-Driven Development (TDD) Approach:** For each problem, a complete test suite is provided. Your goal is to write the solution code that makes all the tests pass, mirroring a professional TDD workflow.
* **Automated Code Formatting:** The project uses `black` and `pre-commit` to automatically format your code, so you can focus on problem-solving, not on style guides.

This repository is structured to practice that entire professional workflow every single day. Each problem is a self-contained module with:

1. **A Deep Dive (`README.md`):** A detailed explanation of the problem and the core concepts.
2. **A Test Suite (`test_solution.py`):** A pre-built set of tests that define the problem's requirements and edge cases.
3. **Your Implementation (`solution.py`):** Your mission is to write the code that satisfies the tests.
4. **A Sandbox (`practice.ipynb`):** An optional Jupyter Notebook for interactive exploration.

### How to Use This Repository

Follow these steps to get your local environment set up.

#### 1. Prerequisites

* Python 3.8+
* Git

#### 2. Local Setup

It is a best practice to use a virtual environment to keep project dependencies isolated.

```
# 1. Clone the repository to your local machine
git clone [https://github.com/benkaan001/Python-Daily-Practice.git](https://github.com/benkaan001/Python-Daily-Practice.git)

# 2. Navigate into the project directory
cd Python-Daily-Practice

# 3. Create a virtual environment
# The 'venv' folder will store all the project-specific packages
python -m venv venv

# 4. Activate the virtual environment
# On macOS and Linux:
source venv/bin/activate
# On Windows:
# .\\venv\\Scripts\\activate

# After activation, you will see (venv) at the beginning of your terminal prompt.

# 5. Install the required packages into your virtual environment
pip install -r requirements.txt

# 6. Set up the pre-commit hooks
pre-commit install

```

The `pre-commit install` command sets up a hook that will automatically format and lint your code every time you make a commit. When you are finished working on the project, you can deactivate the virtual environment by simply typing `deactivate`.

#### 3. Running Tests

You can verify your solutions at any time by running `pytest` from the root directory.

```
# Run all tests in the repository
pytest

# Run tests for a specific day
pytest practice/week_01_data_structures/day_001_reverse_string/

```

## Practice Problems Table of Contents

This index will be updated with each new problem.

### Week 1: Core Data Structures & Algorithms

| **Day** | **Problem Title**                                                                                 | **Key Concepts Covered** |
| ------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------ |
| 001           | [To Be Added](https://www.google.com/search?q=./practice/week_01_data_structures/day_001_placeholder/ "null") | `...`                        |
| 002           | ...                                                                                                     | `...`                        |

### Contributing & Feedback

This repository is a living project. If you find a bug, have a suggestion for a better solution, or want to recommend a problem, please feel free to open an issue!

### License

This project is licensed under the  **MIT License** . See the `LICENSE` file for details.
