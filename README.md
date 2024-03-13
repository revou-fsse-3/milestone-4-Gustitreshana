# Online Banking System

A simple online banking system built with Python, Flask, and MySQL.

## Key Features

* **User Management:**
* Secure user registration and login with password hashing.
* Ability to view and update user profiles.
* **Account Management:**
* Create multiple bank accounts per user (savings, checking, etc.).
* View account balances and details.
* **Transactions:**
* Transfer funds between a user's accounts.
* Withdraw funds from accounts with balance checks.
* Deposit funds into accounts.
* Comprehensive transaction history tracking.

## Technical Details

* **Languages/Frameworks:**
* Python
* Flask (RESTful API development)
* SQLAlchemy (Database ORM)
* **Database:**
* MySQL

## Getting Started

### Prerequisites

* Python 3.x
* MySQL
* Poetry [https://python-poetry.org/]

### Installation

1. Clone the repository.
2. Install dependencies: `poetry install`

### Database Setup

1. Create a MySQL database named `banking_system`.
2. Update database credentials in `Banking_app/.env`:

DATABASE_HOSTNAME=your_database_hostname
DATABASE_PORT=3306
DATABASE_USERNAME=your_database_username
DATABASE_PASSWORD=your_database_password
DATABASE_NAME=banking_system

### Running the Application

1. Start the Flask development server: `poetry run flask --app app run`

### API Documentation

For a comprehensive overview and usage examples of the API endpoints, please refer to the Postman documentation:

* **Postman Documentation:** [https://documenter.getpostman.com/view/29213022/2sA2xk1X6D]

## Additional Notes

* **Error Handling:**
* The API includes error handling for common issues like invalid input, insufficient funds, and resources not found.
  
* **Security:**
* Passwords are securely hashed using bcrypt.
* User authentication is implemented using JWTs.
* Input validation helps to prevent common vulnerabilities.
