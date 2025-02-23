### Employee Management

Employee Management System to manage and capture company structure and essential employee information.

## Table of Contents
- [API Documentation](#api-documentation)

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app employee_management
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/employee_management
pre-commit install
```

## API Documentation
[![Swagger Docs](https://img.shields.io/badge/Swagger-API%20Docs-blue)](https://ahmedshehab1.github.io/Employee-Management-System/)


Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

### Checklist of Completed Tasks

✔ CRUD Operations for Companies, Departments, Employees

✔ Applied Business Logic Validations

✔ Secured API Endpoints

✔ Comprehensive API Documentation

✔ Integrated API Documentation with GitHub Pages for Public Access

### License

unlicense
