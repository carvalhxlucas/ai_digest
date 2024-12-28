# AI Digest

**AI Digest** is a smart newsletter platform powered by AI. It automates the generation of concise, relevant, and engaging content, focusing on technology and artificial intelligence.

## Features
- **Newsletter Subscription**: Users can subscribe using their email.
- **AI-Powered Content**: Automatically generates newsletter content using advanced AI algorithms.
- **Admin Panel**: Manage subscribers and content easily through Django's built-in admin interface.

## Project Structure
```
ai_digest/
├── manage.py                     # Django's management script
├── ai_digest/                    # Main project directory
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
├── newsletter/                   # App for managing the newsletter
│   ├── models.py                 # Database models
│   ├── views.py                  # Application views
│   ├── urls.py                   # App URL configuration
│   ├── forms.py                  # Forms for user interaction
│   ├── templates/                # HTML templates
│   │   └── newsletter/           # Newsletter-specific templates
│   ├── migrations/               # Database migrations
│   └── admin.py                  # Admin panel customization
├── db.sqlite3                    # SQLite database (or configured database)
└── README.md                     # Project documentation
```

## Installation

### Prerequisites
- Python 3.8+
- Django 4.0+

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-digest.git
   cd ai-digest
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`.

## Usage
- Visit the `/subscribe/` endpoint to sign up for the newsletter.
- Use the Django admin panel (`/admin/`) to manage subscribers and generated content.

## Future Improvements
- Integration with external AI APIs for more advanced content generation.
- Support for multiple newsletter categories.
- Enhanced analytics for subscriber engagement.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request to discuss any changes or improvements.
