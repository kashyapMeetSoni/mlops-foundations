# lint_model.py

import pylint.lint

# Specify the files you want to lint
files_to_lint = ["model.py", "test_model.py"]

# Run pylint
pylint.lint.Run(files_to_lint, exit=False)
