# Catalyst-Count

Catalyst-Count is a robust web application designed to streamline data management tasks by allowing users to register, upload CSV files, and filter data based on keywords. Built on a powerful stack including Python, Django, Django Rest Framework (DRF), PostgreSQL, JavaScript, HTML, CSS, Bootstrap, AJAX, and Django-allauth, Catalyst offers a seamless user experience coupled with advanced functionality.

## Key Features

- **User Registration and Authentication**:
  - Users can easily register on the platform and securely authenticate themselves using Django-allauth.
  - Admins have the authority to manage user accounts, including adding, deleting, and viewing user details.

- **File Upload and Management**:
  - Registered users can upload CSV files containing their data.
  - Catalyst efficiently manages and stores uploaded files in a PostgreSQL database.

- **Data Filtering**:
  - Users have the capability to filter data within uploaded CSV files based on specific keywords.
  - The application utilizes AJAX to ensure seamless and responsive filtering functionality.

## Technologies Used

- Python
- Django
- Django Rest Framework (DRF)
- PostgreSQL
- JavaScript
- HTML & CSS
- Bootstrap
- AJAX
- Django-allauth
- Chunked-upload

## Project Structure

- **Project Name**: catalyst_count
- **Total Apps**:
  - `authentication_login`
  - `upload_data`
  - `count_list_api`
  - `query_builder`
  - `user_management`

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- Virtual Environment

### Steps

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
