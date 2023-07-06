Book Management API

This project is a Django-based RESTful API for managing a collection of books. It provides various endpoints to retrieve, create, update, and delete books.

Prerequisites

Before running the project, ensure you have the following prerequisites:

    Python 3.6+
    Django
    Django Rest Framework

API Documentation

The API provides the following endpoints:
Retrieve a list of all books

    URL: /books/
    Method: GET
    Description: Retrieves a list of all books in the collection.
    Response: Returns a JSON array containing book objects with attributes such as id, title, author, publication_date, and more.

Retrieve a single book by its ID

    URL: /books/{id}/
    Method: GET
    Description: Retrieves a single book by its unique ID.
    Response: Returns a JSON object containing the book details, including attributes such as id, title, author, publication_date, and more.

Create a new book

    URL: /books/
    Method: POST
    Description: Creates a new book in the collection.
    Request Body: Provide a JSON object containing the book details, including attributes such as title, author, publication_date, and more.
    Response: Returns a JSON object containing the newly created book's details, including the assigned id.

Update an existing book

    URL: /books/{id}/
    Method: PUT
    Description: Updates an existing book by its unique ID.
    Request Body: Provide a JSON object containing the updated book details, including attributes such as title, author, publication_date, and more.
    Response: Returns a JSON object containing the updated book's details.

Delete a book

    URL: /books/{id}/
    Method: DELETE
    Description: Deletes a book from the collection by its unique ID.
    Response: Returns a success message indicating the deletion was successful.

Refer to the API documentation for detailed information about request/response formats, parameters, and authentication requirements.

Usage

To run the project, follow these steps:

    Start the development server:
        
        py manage.py runserver

Open your browser and navigate to http://localhost:8000/ to access the API endpoints.

Use tools like Postman or curl to test the API endpoints.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Codemonk.        Back-end Intern Assignment
Assignment Description
Advanced Django Rest Framework Internship Project.
Project Requirements
1. API Creation:
- Create a Django project and configure it with Django Rest Framework.
- Design and implement a RESTful API to manage a collection of books.
- The API should support the following operations:
- Retrieve a list of all books.
- Retrieve a single book by its ID.
- Create a new book.
- Update an existing book.
- Delete a book.
2. Partial Update of Records with Validation:
- Extend the API to allow partial updates of book records.
- Implement an endpoint to update specific fields of a book record with proper validation.
- Validate input data based on predefined criteria (e.g., length, format, etc.).
- Return appropriate error responses for invalid data.
3. User Signup with Email Verification:
- Implement user signup functionality with email verification.
- Users should be able to create an account by providing their email and password.
- Send a verification email to the user's provided email address.
- Implement a verification process where users can verify their email addresses by clicking a link in the
email.
- Allow access to certain endpoints only after successful email verification.
4. Advanced Filtering:
- Implement advanced filtering options for the book collection.
- Allow users to filter books based on multiple criteria (e.g., title, author, publication year, etc.).
- Implement pagination to limit the number of results per page.
- Provide sorting options for the filtered results.
5. Pagination:
- Implement pagination for the API endpoints that return a list of books.
- Allow users to specify the number of results per page and navigate through the pages.
- Include metadata in the API response to provide information about pagination (e.g., total number of
books, current page, next page, previous page, etc.).
6. File Upload:
- Extend the API to support file uploads, such as book cover images or PDF files.
- Implement an endpoint for uploading files and associate them with book records.
- Handle file validation, including size limits, file type checks, and secure storage.
- Provide appropriate error responses for invalid or failed file uploads.