### Employee Management

Employee Management System to manage and capture company structure and essential employee information.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [API Documentation](#api-documentation)
- [Assumptions and Considerations](#assumptions-and-considerations)

## Overview
This **Employee Management System** is built using **Frappe** for backend logic and **Vue.js** for frontend interaction. It enables users to manage companies, departments, and employees while enforcing business logic and validations. The system includes **role-based access control (RBAC)** and a workflow for handling employee onboarding.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app employee_management
```
## Features
### Backend (Frappe)
#### Models:
- **User Accounts**: User Name, Email Address (Login ID), Role

- **Company**: Company Name, Number of Departments, Number of Employees

- **Department**: Company (Select), Department Name, Number of Employees

- **Employee**: Company (Select), Department (Select - dynamically filtered), Employee Status (via workflow), Employee Name, Email, Mobile, Address, Designation, Hired On, Days Employed

#### Business Logic & Validations:
- Required fields validation
- Email & mobile format validation
- Auto-calculate number of departments and employees
- Auto-calculate employee tenure (Days Employed)
- Restrict department selection to the selected company
- Handle cascading deletions (prevent deletion if dependencies exist)
- Proper error handling with clear messages

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


## Assumptions and Considerations
- Employees **must** belong to a department under the selected company.
- Employee tenure is calculated **only if hired**.
- Employees **must** belong to a department under the selected company.
- Employee tenure is calculated **only if hired**.
- A department will not be deleted if an employee is associated with it.
- A company will not be deleted if a department is associated with it.


### License

unlicense
