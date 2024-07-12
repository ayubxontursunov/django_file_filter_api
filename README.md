# FileFilter API


![Django REST framework Logo](https://www.django-rest-framework.org/img/logo.png)

FileFilter API is a Django REST framework-based application designed to handle file uploads and filtering file links to another file called `filter.txt`.

## Features

- Upload files through a REST API.
- Filter URLs from the uploaded files and save them to `filter.txt`.
- Robust URL extraction using regular expressions.

## Requirements

- Python 3.9
- Django 4.2
- Django REST framework 3.15.2
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ayubxontursunov/django_file_filter_api.git
    cd django_file_filter_api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Upload File

- **URL:** `/filter/`
- **Method:** `POST`
- **Description:** Upload a file to the server.

**Request:**

```http
POST /filter/
Content-Type: multipart/form-data
```
### Download filtered File
- **URL:** `/data/`
- **Method:** `GET`
- **Description:** Download a file from the server.

**Response:**

```http
GET /data/
Content-Type: multipart/form-data
```
## Contributing
We welcome contributions! Please read our Contributing Guidelines for more information.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Special thanks to the Django and Django REST framework communities for their excellent frameworks and documentation.
