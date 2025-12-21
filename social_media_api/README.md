# Social Media API

## Setup

1. **Install dependencies**:
   ```bash
   pip install django djangorestframework
   ```
   *Note: Using a virtual environment is recommended.*

2. **Database Migrations**:
   Navigate to the project directory and run:
   ```bash
   python manage.py migrate
   ```

3. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## User Authentication

The API uses Token Authentication.

### Endpoints

- **Register**: `POST /api/users/register/`
  - Body:
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword",
      "email": "youremail@example.com",
      "bio": "Optional bio",
      "profile_picture": "Optional file"
    }
    ```
  - Returns: User data and Auth Token.

- **Login**: `POST /api/users/login/`
  - Body:
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    ```
  - Returns: Auth Token.

- **Profile**: `GET /api/users/profile/`
  - Headers:
    `Authorization: Token <your_token>`
  - Returns: Authenticated user's profile.

## User Model

The `CustomUser` model extends Django's `AbstractUser` and includes:
- `bio`: User biography.
- `profile_picture`: User avatar.
- `followers`: ManyToMany relationship to other users.
