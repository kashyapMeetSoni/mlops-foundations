# MLOps Foundations

This repository demonstrates a basic MLOps pipeline using GitHub Actions for continuous integration and continuous delivery (CI/CD). The project trains a simple machine learning model and includes linting, testing, and simulated deployment steps.

## Project Structure

-   **`model.py`:** Contains the code for a simple linear regression model using scikit-learn.
-   **`test_model.py`:** Includes unit tests for the model using `pytest`.
-   **`lint_model.py`:**  Runs `pylint` to enforce code style and quality.
-   **`deploy.py`:** Simulates model deployment.
-   **`data.csv`:** Sample data for training the model.
-   **`requirements.txt`:** Lists the Python dependencies for the project.
-   **`.pylintrc`:** Configuration file for `pylint`.
-   **`.github/workflows/main.yml`:** Defines the GitHub Actions workflow for CI/CD.

## CI/CD Pipeline

The GitHub Actions workflow defined in `main.yml` automates the following steps:

1.  **Linting:** Uses `pylint` to check for code style and potential errors.
2.  **Testing:** Executes unit tests using `pytest` to verify model functionality.
3.  **Deployment (Simulated):** Runs a script (`deploy.py`) to simulate model deployment.

The workflow is triggered on pushes to the `dev` and `main` branches.

## How to Run

1.  Clone the repository:

    ```bash
    git clone [invalid URL removed]
    ```

2.  Navigate to the project directory:

    ```bash
    cd mlops-foundations
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the model locally:

    ```bash
    python model.py
    ```
5.  Run tests:

    ```bash
    python -m pytest
    ```
6.  Run linter:

    ```bash
    python lint_model.py
    ```

## GitHub Actions

The CI/CD pipeline is defined in `.github/workflows/main.yml`. It automatically runs linting, testing, and simulated deployment on each push. You can view the workflow runs in the "Actions" tab of the repository.

## Notes

-   This is a basic example for demonstration purposes.
-   The deployment step is simulated. In a real-world scenario, you would deploy to a staging or production environment.
-   The CI/CD pipeline can be extended to include other steps, such as building and publishing Docker images, deploying to cloud platforms, and more.
