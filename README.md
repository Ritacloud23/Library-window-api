#  Library Management System

A Python-based Library Management System developed as a backend engineering assignment.

The project demonstrates fundamental backend concepts including authentication, role-based permissions, book management, borrowing and returning books, persistent data storage, request handling, response handling, validation, and error handling.

The application is designed using a modular architecture where each file has a specific responsibility.

[![wakatime](https://wakatime.com/badge/user/fe9d0a56-e366-4369-9030-c96eee51ac5b/project/8a043bd1-7a58-49a9-b1e5-e28d2b9f907d.svg)](https://wakatime.com/badge/user/fe9d0a56-e366-4369-9030-c96eee51ac5b/project/8a043bd1-7a58-49a9-b1e5-e28d2b9f907d)

---

#  Project Overview

The Library Management System is designed to manage the basic operations of a small library.

The system allows authorised users to:

- Sign in securely
- View books in the library
- Register new books
- Update existing book information
- Delete books when authorised
- Borrow books
- Return borrowed books
- Maintain book information after the application is restarted

The application also controls what users can and cannot do based on their assigned roles.

The two supported roles are:

- **Chief Librarian**
- **Member**

---

#  Project Objectives

The main objectives of this project are to demonstrate an understanding of backend programming and application structure.

The project focuses on:

- Python programming
- Modular programming
- Functions
- Dictionaries and lists
- Authentication
- Authorisation
- Role-based access control
- CRUD operations
- Book management
- Borrowing and returning
- JSON storage
- Data persistence
- Error handling
- Request and response handling
- HTTP-style status codes
- Separation of concerns

---

# Key Features

##  User Authentication

Users must provide valid credentials before accessing the library system.

The authentication system checks:

- Whether the username exists
- Whether the account is locked
- Whether the password is correct

Only authenticated users are allowed to perform library operations.

---

##  Account Lockout

The system provides a basic account protection mechanism.

A user is allowed a maximum of **three failed login attempts**.

After three incorrect attempts, the account becomes locked.

Once an account is locked, the user cannot continue logging in during that session, even if the correct password is provided afterwards.

This demonstrates how authentication systems can protect user accounts against repeated failed login attempts.

---

# 👥 User Roles

The system has two main user roles.

## Chief Librarian

The Chief Librarian has full access to the library operations.

The Chief Librarian can:

- View books
- Register books
- Update books
- Delete books
- Borrow books
- Return books

---

## 👤 Member

Members have access to normal library operations.

Members can:

- View books
- Register books
- Update books
- Borrow books
- Return books

Members cannot delete books.

When a Member attempts to delete a book, the system returns a **403 Forbidden** response.

---

# Project Architecture

The application follows a modular architecture.

Instead of putting all functionality inside one Python file, the project is divided into separate modules.

Each module is responsible for a specific part of the application.

The main components are:

- `user.py`
- `auth.py`
- `books.py`
- `library.py`
- `storage.py`
- `main.py`

This approach is known as **separation of concerns**.

Separation of concerns makes an application easier to:

- Understand
- Test
- Debug
- Maintain
- Modify
- Extend

---

# Project Structure

The project is organised into the following structure:

- `data/`
  - `books.json`

- `src/`
  - `windows_storage/`
    - `__init__.py`
    - `user.py`
    - `auth.py`
    - `books.py`
    - `library.py`
    - `storage.py`

- `main.py`
- `README.md`
- `pyproject.toml`

---

#  User Module

## `user.py`

The `user.py` module is responsible for storing information about the authorised library users.

It contains the users recognised by the system and their assigned roles.

The information associated with each user includes:

- Username
- Password
- Role

The module also provides functions that allow the application to:

- Retrieve a user's information
- Check whether a username exists

The purpose of keeping this information inside `user.py` is to prevent user information from being mixed with authentication or book-management logic.

---

# Authentication Module

## `auth.py`

The `auth.py` module is responsible for authentication and permissions.

Its responsibilities include:

- Validating usernames
- Validating passwords
- Tracking failed login attempts
- Locking accounts after three failed attempts
- Returning authenticated user information
- Checking user permissions

The authentication module uses the information provided by `user.py`.

---

# 🔄 Authentication Process

The authentication process follows a clear sequence.

### Step 1: User Provides Credentials

The user provides a username and password.

### Step 2: Check User

The system checks whether the username exists.

### Step 3: Check Account Status

The system checks whether the account has already been locked.

### Step 4: Check Password

The password provided by the user is compared with the stored password.

### Step 5: Handle Failed Login

If the password is incorrect, the system records the failed attempt.

### Step 6: Lock Account

If the user reaches three failed attempts, the account is locked.

### Step 7: Successful Login

If the credentials are correct, authentication succeeds and the user's role is returned.

---

# Authorisation and Permissions

Authentication and authorisation are two different concepts.

### Authentication

Authentication answers:

> Who are you?

It verifies the user's identity.

### Authorisation

Authorisation answers:

> What are you allowed to do?

It determines whether the authenticated user has permission to perform a particular action.

For example, a Member can successfully log in but still cannot delete a book.

The user is authenticated, but the requested action is not authorised.

---

#  Role-Based Access Control

The system uses role-based access control.

Permissions are assigned to roles rather than individual users.

This means the application checks the user's role before allowing certain actions.

For example:

- Chief Librarian → Delete Book → Allowed
- Member → Delete Book → Forbidden

This approach is better than creating separate permission rules for every individual user because it is easier to maintain and extend.

---

#  Book Management

## `books.py`

The `books.py` module is responsible for managing the library's book records.

It handles the basic book operations.

These operations include:

- Viewing books
- Finding a specific book
- Registering a new book
- Removing a book

Each book contains information such as:

- Book ID
- Title
- Author
- Availability status

---

# CRUD Operations

The system demonstrates CRUD operations.

CRUD stands for:

- **Create**
- **Read**
- **Update**
- **Delete**

## Create

A new book can be registered in the library.

## Read

Users can view all books or retrieve a specific book.

## Update

Existing book information can be updated.

For example, the title or author can be changed.

## Delete

Books can be removed from the library.

However, this operation is restricted to users with the appropriate permission.

---

# Library Operations

## `library.py`

The `library.py` module handles library-specific operations.

Its main responsibilities are:

- Borrowing books
- Returning books

This keeps borrowing and returning logic separate from general book-management logic.

---

# Borrowing Books

When a user borrows a book, the system checks whether the book exists and whether it is currently available.

If the book is available:

- The borrowing operation succeeds.
- The book's status changes.
- The updated information is saved.

If the book is already borrowed, the system rejects the request.

This prevents multiple users from borrowing the same book at the same time.

---

# Returning Books

When a user returns a book, the system checks the current state of the book.

If the book is currently borrowed:

- The return operation succeeds.
- The book becomes available again.
- The updated information is saved.

If the book is already available, the system rejects the request because there is nothing to return.

---

#  Persistent Storage

## `storage.py`

The `storage.py` module is responsible for persistent data storage.

The application uses a JSON file to store the library ledger.

The JSON file acts as the persistent record of the library's books.

---

#  Why Persistence Is Important

Without persistence, information would exist only while the Python program is running.

For example, if a new book was added and the program was closed, the book could disappear.

Persistent storage solves this problem.

The application saves changes to the JSON ledger.

When the application starts again, it loads the saved information.

This means changes remain available even after the application has been closed and reopened.

---

# Persistence Flow

The persistence process works as follows:

### Application Starts

The system loads the saved book ledger.

### User Makes a Change

The user adds, updates, deletes, borrows, or returns a book.

### Application Saves the Change

The updated book information is written to the JSON ledger.

### Application Closes

The information remains stored in the ledger.

### Application Starts Again

The saved information is loaded back into the application.

This demonstrates the difference between **temporary in-memory data** and **persistent data**.

---

#  Main Application Window

## `main.py`

The `main.py` file serves as the main entry point of the application.

It acts as the central window through which requests enter the system.

Its responsibility is to:

- Receive requests
- Authenticate users
- Check permissions when required
- Call the appropriate module
- Return a response
- Save changes when necessary

The actual business logic remains inside the specialised modules.

---

#  Request Handling

The system supports several request types.

The supported operations are:

- **GET**
- **POST**
- **PUT**
- **DELETE**
- **BORROW**
- **RETURN**

Each request is processed according to its purpose.

---

#  GET Request

The GET operation is used to retrieve information.

It can be used to:

- View all books
- View a specific book

If the requested book does not exist, the system returns a **404 Not Found** response.

---

# POST Request

The POST operation is used to register a new book.

The system validates:

- Title
- Author

The title and author cannot be empty.

If the information is valid, the book is registered and the updated ledger is saved.

---

#  PUT Request

The PUT operation is used to update an existing book.

The user can update:

- Title
- Author

The system first checks whether the book exists.

If the book does not exist, the system returns a **404 Not Found** response.

After a successful update, the new information is saved to the persistent ledger.

---

# DELETE Request

The DELETE operation removes a book from the library.

Before deleting the book, the system checks the user's permissions.

Only the Chief Librarian has permission to delete books.

If a Member attempts to delete a book, the system returns:

**403 Forbidden**

If the Chief Librarian has permission and the book exists, the book is deleted and the updated ledger is saved.

---

# BORROW Request

The BORROW operation allows an authenticated user to borrow a book.

The system checks:

- Whether the book exists
- Whether the book is available

If the book can be borrowed, its status is updated and the change is saved.

---

#  RETURN Request

The RETURN operation allows a user to return a borrowed book.

The system checks:

- Whether the book exists
- Whether the book is currently borrowed

After a successful return, the book becomes available again and the updated ledger is saved.

---

# HTTP-Style Status Codes

The application uses HTTP-style status codes to communicate the result of a request.

## 200 - Success

The operation was successfully completed.

Examples include:

- Successfully viewing a book
- Successfully registering a book
- Successfully updating a book
- Successfully borrowing a book
- Successfully returning a book
- Successfully deleting a book when authorised

---

## 400 - Bad Request

The request contains invalid or incomplete information.

Examples include:

- Missing book ID
- Empty title
- Empty author
- Invalid request type
- Attempting an invalid library operation

---

## 401 - Unauthorised

The user has not successfully authenticated.

Examples include:

- User not found
- Invalid password
- Missing username
- Missing password
- Locked account

---

## 403 - Forbidden

The user is authenticated but does not have permission to perform the requested operation.

The main example is:

**Member attempting to delete a book.**

---

## 404 - Not Found

The requested resource does not exist.

For example, when a user requests a book ID that is not present in the library ledger.

---

#  Complete Application Flow

The complete system works through several stages.

## Step 1 - Application Starts

The application starts from `main.py`.

The persistent library ledger is loaded.

---

## Step 2 - Request Is Received

A request is sent to the main application.

The request contains the required information such as:

- Request method
- Username
- Password
- Book ID
- Title
- Author

---

## Step 3 - Authentication

The application sends the login information to the authentication module.

The authentication module checks the user information.

---

## Step 4 - Authentication Result

If authentication fails, the system returns a 401 response.

If authentication succeeds, the system continues processing the request.

---

## Step 5 - Permission Check

If the requested operation requires a specific permission, the system checks the user's role.

For example, DELETE requires the appropriate librarian permission.

---

## Step 6 - Business Operation

The appropriate module performs the requested operation.

Book operations are handled by the book module.

Borrowing and returning are handled by the library module.

---

## Step 7 - Save Changes

If the operation changes the library data, the updated information is saved to the JSON ledger.

---

## Step 8 — Response

The system returns a response containing the result of the operation.

---

#  Testing Strategy

The project was developed and tested incrementally.

Instead of creating the entire application and testing everything at the end, each module was tested as it was implemented.

This made it easier to identify and correct errors.

---

#  User Testing

The user module was tested to confirm that:

- Authorised users exist
- User information can be retrieved
- Existing users are recognised
- Unknown users are rejected

---

#  Authentication Testing

Authentication was tested using:

- Correct username and password
- Incorrect password
- Unknown username
- Multiple failed attempts
- Locked account
- Correct password after account lockout

The tests confirmed that the authentication rules were being enforced.

---

# Permission Testing

Permission testing was performed for both roles.

## Member Testing

A Member was tested against normal library operations.

The Member was also tested when attempting to delete a book.

The system correctly returned **403 Forbidden** for the unauthorised DELETE operation.

## Chief Librarian Testing

The Chief Librarian was tested to confirm that the user could perform operations requiring librarian privileges.

---

# Book Testing

Book management was tested using:

- GET
- POST
- PUT
- DELETE

The tests also checked invalid book IDs and invalid book information.

---

# Borrow Testing

Borrowing was tested by:

- Borrowing an available book
- Trying to borrow a book that was already borrowed
- Trying to borrow a nonexistent book

The system correctly handled each situation.

---

# Return Testing

Returning was tested by:

- Returning a borrowed book
- Trying to return a book that was already available
- Trying to return a nonexistent book

The system correctly handled these scenarios.

---

# Persistence Testing

Persistence was tested by:

1. Making a change to a book.
2. Saving the change.
3. Closing the application.
4. Starting the application again.
5. Retrieving the same book.
6. Confirming that the previous change still existed.

This confirmed that the JSON ledger was being used as persistent storage.

---

#  Error Handling

The application includes validation and error handling for common problems.

The system handles:

- Unknown users
- Invalid passwords
- Locked accounts
- Missing credentials
- Missing book IDs
- Nonexistent books
- Empty titles
- Empty authors
- Unauthorised operations
- Invalid borrowing operations
- Invalid returning operations
- Invalid requests
- Invalid saved data

Instead of allowing the application to fail unexpectedly, the system returns meaningful responses.

---

# Separation of Concerns

One of the most important design principles demonstrated in this project is separation of concerns.

Each module has a specific responsibility.

## `user.py`

Responsible for user information.

## `auth.py`

Responsible for authentication and permissions.

## `books.py`

Responsible for book management.

## `library.py`

Responsible for borrowing and returning.

## `storage.py`

Responsible for persistent storage.

## `main.py`

Responsible for connecting the different components and handling requests.

This makes the application easier to maintain and understand.

---

# Why This Architecture Was Used

A single-file application could contain all of these functions, but that approach becomes difficult to maintain as the application grows.

For example, if authentication, books, borrowing, storage, and requests were all placed in one file, debugging would become harder.

By separating them, each module can be understood independently.

This also makes future improvements easier.

---

# Problems Encountered During Development

Several development issues were encountered while building the application.

## Import Errors

An import error occurred when a function was imported from the wrong module.

This demonstrated the importance of understanding which module owns a particular function.

Storage functions belong to the storage module, while book-management functions belong to the books module.

---

## Role Naming Issue

A permission issue occurred because the role name was not written consistently.

For example, the system treated different capitalisation of the same role as different values.

This demonstrated the importance of keeping role names consistent throughout an application.

---

## Authentication Testing

Testing authentication revealed how important it is to use the exact credentials defined for each authorised user.

A username may be correct while the password is incorrect, resulting in an authentication failure.

---

## Persistence

Another important issue was understanding the difference between changing data in memory and actually saving the change.

The solution was to connect the book operations with the persistent storage module.

---

# Development Process

The project was developed step by step.

## Step 1 - Project Setup

The project structure was created.

The source files were organised into the `src/windows_storage` package.

---

## Step 2 - User Management

The authorised users and their roles were defined.

The user module was tested independently.

---

## Step 3 - Authentication

The authentication system was implemented.

Login validation and failed attempts were tested.

---

## Step 4 - Account Lockout

The three-attempt lockout rule was implemented and tested.

---

## Step 5 - Permissions

Role-based permissions were introduced.

The difference between the Chief Librarian and Member roles was tested.

---

## Step 6 - Book Management

Book retrieval, registration, updating, and deletion were implemented.

---

## Step 7 - Borrowing and Returning

Library operations were added.

Book availability was checked before borrowing and returning.

---

## Step 8 - Persistent Storage

The JSON ledger was introduced.

The system was connected to the storage module.

---

## Step 9 - Request Handling

The different request types were connected through `main.py`.

---

## Step 10 - Complete Testing

All major operations were tested together.

This included:

- Authentication
- Permissions
- Book management
- Borrowing
- Returning
- Error handling
- Persistence

---

#  What I Learned

This project helped me understand several important backend development concepts.

## Modular Programming

I learned how to divide an application into smaller modules with clear responsibilities.

---

## Authentication

I learned how an application verifies the identity of a user before granting access.

---

## Authorisation

I learned the difference between authentication and authorisation.

Authentication determines who the user is.

Authorisation determines what the user is allowed to do.

---

## Role-Based Access Control

I learned how permissions can be assigned based on roles instead of individual users.

---

## CRUD

I learned how Create, Read, Update, and Delete operations form the foundation of many backend applications.

---

## Data Persistence

I learned why applications need persistent storage so that information survives after the program is closed.

---

## JSON

I learned how JSON can be used as a simple persistent data format for small applications.

---

## Error Handling

I learned how to handle invalid input and return meaningful responses instead of allowing the application to crash.

---

## HTTP Status Codes

I learned how status codes can communicate the outcome of a request.

---

## Debugging

I learned how to read Python error messages and identify which file or module is causing a problem.

---

#  Future Improvements

Although this project satisfies the assignment requirements, there are several ways it could be improved in a real production environment.

Possible improvements include:

- Using PostgreSQL instead of JSON storage
- Hashing passwords instead of storing plain-text passwords
- Implementing JWT authentication
- Building a REST API using FastAPI
- Adding automated unit tests
- Adding integration tests
- Adding API documentation
- Adding logging
- Using environment variables for sensitive configuration
- Adding Docker support
- Adding database migrations
- Adding user registration
- Adding book search
- Adding book categories
- Adding borrowing history
- Adding borrowing due dates
- Tracking overdue books
- Adding a frontend interface
- Deploying the application to the cloud

---

# 🌐 Possible Production Architecture

A future production version could be structured around:

**Frontend → REST API → Authentication → Business Logic → Database**

The current application is intentionally simpler because the main purpose is to demonstrate backend fundamentals.

---

# Project Status

**Status:** Completed

**Project Type:** Backend Engineering Assignment

**Programming Language:** Python

**Storage:** JSON

**Architecture:** Modular Python Application

**Authentication:** Username and Password

**Authorisation:** Role-Based Access Control

**Persistence:** JSON Ledger

---

# Final Checklist

The following project requirements have been implemented and tested:

- [x] Authorised users
- [x] User roles
- [x] User authentication
- [x] Password validation
- [x] Three-attempt account lockout
- [x] Role-based permissions
- [x] Book viewing
- [x] Book registration
- [x] Book updating
- [x] Book deletion
- [x] Member DELETE restriction
- [x] Book borrowing
- [x] Book returning
- [x] Input validation
- [x] Error handling
- [x] HTTP-style status codes
- [x] JSON storage
- [x] Persistent book ledger
- [x] Loading saved data
- [x] Saving changes
- [x] Modular project architecture
- [x] Complete system testing

---

# Conclusion

The Library Management System demonstrates how a small backend application can be organised into independent modules that work together.

The project separates user management, authentication, permissions, book management, library operations, storage, and request handling.

The most important architectural lesson from this project is the principle of **separation of concerns**.

Each part of the system has a clear responsibility, making the application easier to understand, test, debug, maintain, and extend.

The project also demonstrates important backend concepts such as authentication, authorisation, CRUD operations, persistent storage, validation, error handling, and HTTP-style responses.

Although the application currently uses JSON as its storage system, the architecture provides a foundation that can later be extended into a full REST API backed by a production database.

---

# 👩‍💻 Author

**Rita Nnenna**

Backend Development Learner

Nigeria 🇳🇬

---

#  Project Status

**Completed and Tested Successfully**
