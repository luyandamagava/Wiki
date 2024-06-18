# Wiki Page Web Application

## Overview

Welcome to the Wiki Page Web Application! This project is a simple yet effective wiki platform that allows users to view various topics and navigate to dedicated information pages. Developed using Django, this application provides an intuitive interface for users to explore and contribute content.

## Features

- **Information Architecture:**
  - A robust database schema for storing topic titles, content, and relationships between topics (e.g., categories or links).

- **Dynamic Content Rendering:**
  - Utilizes Django's templating system to dynamically display topic listings and fetch relevant information pages.

- **User Content Creation:**
  - Forms and backend logic to allow users to contribute new topics and associated information.

## Technologies Used

- **Backend:**
  - Django REST Framework
  - Python
  - MySQL (or your chosen database)

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

## Getting Started

### Prerequisites

- Python 3.x
- Django
- MySQL (or your preferred database)
- Node.js (for installing required packages)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/luyandamagava/Wiki-Page-Web-Application.git
   ```

2. Navigate into the project directory:
   ```bash
   cd Wiki-Page-Web-Application
   ```

3. Create a virtual environment:
   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:
   - On Linux/macOS:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     env\Scripts\activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up your database (modify settings as needed for your database setup).

7. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

9. Start the development server:
   ```bash
   python manage.py runserver
   ```

10. Access the project in your web browser:
    ```http://127.0.0.1:8000/```

## Usage

1. **Create a New Account:**
   - Sign up using the provided form.

2. **Log In:**
   - Access the main dashboard after logging in.

3. **View Topics:**
   - Browse through the list of available topics.

4. **Create New Topics:**
   - Use the form to contribute new topics and associated information.

5. **Navigate to Information Pages:**
   - Click on topics to view detailed information.

## Contribution

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b my-new-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -am 'Add some feature'
   ```
4. Push your branch to your fork:
   ```bash
   git push origin my-new-feature
   ```
5. Create a new pull request.

## Future Development

- Enhanced Search: Implement search functionality for topics and information pages.
- User Profiles: Allow users to personalize their profiles.
- Content Moderation: Implement admin features for content approval and moderation.

## Contact

For questions, suggestions, or bug reports, please open an issue on the repository or contact me at luyandamagava@gmail.com.

## Show Your Support

If you find this project useful, please consider starring the repository!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
