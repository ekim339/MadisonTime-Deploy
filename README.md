# MadisonTime

🔗 Deployed Website: https://madisontime-deploy-1.onrender.com/

A comprehensive Django-based social platform designed for university students to manage their timetables, share posts, and engage with their community.

## 📋 Overview

MadisonTime is a full-stack web application that combines course scheduling with social networking features. Students can create personalized timetables, share posts with images, comment on content, and interact with their peers through likes and dislikes.

## ✨ Features

### Core Functionality
- **📅 Interactive Timetable**: Create and manage course schedules with custom colors and time slots
- **📝 Social Board**: Share posts with up to 3 images and rich text content
- **💬 Comments System**: Engage in discussions with nested comments
- **👍 Like/Dislike**: React to posts and comments with real-time updates
- **🔐 User Authentication**: Secure email-based registration and login via Django Allauth
- **✉️ Email Verification**: Account verification system for security

### Advanced Features
- **🎨 Custom Color Picker**: Colorful course categorization in timetables
- **📱 Responsive Design**: Mobile-friendly interface
- **🖼️ Image Uploads**: Support for multiple images per post
- **✏️ Edit Tracking**: Mark edited posts and comments with timestamps

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2.7
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Authentication**: Django Allauth
- **Static Files**: Whitenoise
- **Server**: Gunicorn (Production)

### Frontend
- **HTML5/CSS3**: Custom responsive design
- **JavaScript**: Vanilla JS
- **Templates**: Django Template Engine

### DevOps
- **Containerization**: Docker
- **Deployment**: Render.com
- **Storage**: AWS S3 (via boto3 & django-storages)

## 📦 Prerequisites

Before running this project, ensure you have:

- Python 3.11 or higher
- PostgreSQL 12+ (for production)
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MadisonTime
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
cd backend/MadisonTime
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the `backend/MadisonTime` directory:

```env
# Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=5432

# Django Settings
SECRET_KEY=your_secret_key_here
DEBUG=True

# Email Configuration (optional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### 5. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser
```

### 6. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

## 🏃 Running the Application

### Development Mode

#### Using the Development Script
```bash
./start_dev.sh

### Production Mode

Use Docker for production deployment:

```bash
docker build -t madisontime .
docker run -p 8000:8000 --env-file .env madisontime
```

## 🐳 Docker Deployment

The project includes a Dockerfile for containerized deployment:

```bash
# Build the Docker image
docker build -t madisontime-app .

# Run the container
docker run -d -p 8000:8000 \
  -e DB_NAME=your_db \
  -e DB_USER=your_user \
  -e DB_PASSWORD=your_password \
  -e DB_HOST=your_host \
  -e DB_PORT=5432 \
  madisontime-app
```

The Docker container automatically:
- Starts Redis server
- Collects static files
- Runs database migrations

## 📁 Project Structure

```
MadisonTime/
├── backend/
│   └── MadisonTime/
│       ├── MadisonTime/          # Project settings
│       │   ├── settings.py
│       │   ├── settings_production.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       ├── mt/                   # Main app
│       │   ├── models.py         # User, Post, Comment, Course models
│       │   ├── views.py          # Sync views
│       │   ├── forms.py          # Django forms
│       │   ├── validators.py     # Custom validators
│       │   ├── static/           # Static files (CSS, JS)
│       │   └── templates/        # HTML templates
│       ├── media/                # User uploads
│       ├── staticfiles/          # Collected static files
│       ├── requirements.txt      # Python dependencies
│       ├── dockerfile            # Docker configuration
│       └── manage.py             # Django management script
├── HomePage/                     # Landing page assets
├── LoginPage/                    # Login page assets
├── BoardPage/                    # Board page assets
├── Timetable/                    # Timetable page assets
└── README.md                     # This file
```

## 🔑 Key Features Explained

### Timetable Management
- Create courses with custom names, locations, and colors
- Set specific time ranges (from/to)
- Select recurring days (Mon-Sun)
- Visual color-coding for easy identification
- Automatic time validation

### Social Board
- Create posts with titles and rich content
- Upload up to 3 images per post
- Edit posts (marked with edit indicator)
- Delete your own posts
- View post creation and update timestamps

### Comment System
- Add comments to any post
- Like/dislike comments
- Edit your own comments
- Delete your own comments

### User Authentication
- Email-based registration
- Email verification required
- Password strength validation
- Session management
- Remember me functionality
- Password reset via email

## 🔧 Development

### Running Tests

```bash
python manage.py test mt
```

### Database Management

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (careful!)
python manage.py flush
```

## 📚 API Endpoints

### Authentication
- `/accounts/signup/` - User registration
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/accounts/password/reset/` - Password reset

### Main Features
- `/` - Homepage
- `/board/` - Posts board
- `/timetable/` - Timetable management
- `/settings/` - User settings
