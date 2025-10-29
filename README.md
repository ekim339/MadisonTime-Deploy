# MadisonTime

A comprehensive Django-based social platform designed for university students to manage their timetables, share posts, and engage with their community.

## 📋 Overview

MadisonTime is a full-stack web application that combines course scheduling with social networking features. Students can create personalized timetables, share posts with images, comment on content, and interact with their peers through likes and dislikes. The platform features real-time notifications using WebSocket connections and asynchronous task processing for optimal performance.

## ✨ Features

### Core Functionality
- **📅 Interactive Timetable**: Create and manage course schedules with custom colors and time slots
- **📝 Social Board**: Share posts with up to 3 images and rich text content
- **💬 Comments System**: Engage in discussions with nested comments
- **👍 Like/Dislike**: React to posts and comments with real-time updates
- **🔔 Real-time Notifications**: WebSocket-powered instant notifications for interactions
- **🔐 User Authentication**: Secure email-based registration and login via Django Allauth
- **✉️ Email Verification**: Account verification system for security

### Advanced Features
- **⚡ Async Operations**: Non-blocking database operations for better performance
- **🔄 Background Tasks**: Celery-powered asynchronous task processing
- **🎨 Custom Color Picker**: Colorful course categorization in timetables
- **📱 Responsive Design**: Mobile-friendly interface
- **🖼️ Image Uploads**: Support for multiple images per post
- **✏️ Edit Tracking**: Mark edited posts and comments with timestamps

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2.7
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Authentication**: Django Allauth
- **Async**: Channels + Daphne (ASGI server)
- **Task Queue**: Celery
- **Cache/Broker**: Redis
- **Static Files**: Whitenoise
- **Server**: Gunicorn (Production)

### Frontend
- **HTML5/CSS3**: Custom responsive design
- **JavaScript**: Vanilla JS with WebSocket integration
- **Templates**: Django Template Engine

### DevOps
- **Containerization**: Docker
- **Deployment**: Render.com
- **Storage**: AWS S3 (via boto3 & django-storages)

## 📦 Prerequisites

Before running this project, ensure you have:

- Python 3.11 or higher
- PostgreSQL 12+ (for production)
- Redis server
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

# Redis Configuration (for local development)
REDIS_URL=redis://localhost:6379/0

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

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

#### Option 1: Using the Development Script
```bash
./start_dev.sh
```

#### Option 2: Manual Start

1. **Start Redis Server** (in a separate terminal):
```bash
redis-server
```

2. **Start Celery Worker** (in a separate terminal):
```bash
celery -A MadisonTime worker --loglevel=info
```

3. **Start Django Development Server**:
```bash
# For ASGI (with WebSocket support)
daphne -b 0.0.0.0 -p 8000 MadisonTime.asgi:application

# OR for standard WSGI (without WebSocket)
python manage.py runserver
```

4. **Access the Application**:
   - Main site: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

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
- Launches Celery worker
- Collects static files
- Runs database migrations
- Starts the Daphne ASGI server

## 📁 Project Structure

```
MadisonTime/
├── backend/
│   └── MadisonTime/
│       ├── MadisonTime/          # Project settings
│       │   ├── settings.py
│       │   ├── settings_production.py
│       │   ├── urls.py
│       │   ├── asgi.py           # ASGI configuration
│       │   ├── wsgi.py
│       │   └── celery.py         # Celery configuration
│       ├── mt/                   # Main app
│       │   ├── models.py         # User, Post, Comment, Course models
│       │   ├── views.py          # Sync views
│       │   ├── async_views.py    # Async views
│       │   ├── consumers.py      # WebSocket consumers
│       │   ├── routing.py        # WebSocket routing
│       │   ├── tasks.py          # Celery tasks
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
- Real-time updates via WebSocket

### Real-time Notifications
- Instant notifications when someone likes your post
- Comment notifications
- WebSocket-based communication
- Persistent connection management
- Automatic reconnection handling

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

### Monitoring

#### Celery Monitoring
```bash
# Check active tasks
celery -A MadisonTime inspect active

# Monitor events
celery -A MadisonTime events
```

#### Redis Monitoring
```bash
# Check Redis status
redis-cli ping

# Monitor Redis operations
redis-cli monitor
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

### Async Endpoints
- `/async/like-post/<id>/` - Async post like
- `/async/dislike-post/<id>/` - Async post dislike
- `/async/like-comment/<id>/` - Async comment like
- `/async/dislike-comment/<id>/` - Async comment dislike

### WebSocket Endpoints
- `ws://localhost:8000/ws/notifications/` - User notifications
- `ws://localhost:8000/ws/posts/<id>/` - Post-specific updates

## 🐛 Troubleshooting

### Common Issues

#### 1. WebSocket Connection Fails
```bash
# Ensure Redis is running
redis-cli ping

# Check ASGI server is running
ps aux | grep daphne
```

#### 2. Celery Tasks Not Executing
```bash
# Restart Celery worker
celery -A MadisonTime worker --loglevel=debug
```

#### 3. Database Connection Issues
- Verify PostgreSQL is running
- Check database credentials in `.env`
- Ensure database exists

#### 4. Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

## 📈 Performance Considerations

- **Async Views**: Database operations are non-blocking
- **Redis Caching**: Fast access to frequently used data
- **Celery Tasks**: Heavy operations run in background
- **WebSocket**: Persistent connections reduce HTTP overhead
- **Static Files**: Served via Whitenoise for efficiency

## 🔐 Security

- CSRF protection enabled
- Password validation with custom validators
- Email verification required
- Session security
- SQL injection protection via Django ORM
- XSS protection via Django templates

## 🚢 Deployment on Render

1. **Create a new Web Service** on Render
2. **Connect your repository**
3. **Set Environment Variables**:
   - All variables from `.env` file
   - `PYTHON_VERSION=3.11.0`
4. **Build Command**: `pip install -r backend/MadisonTime/requirements.txt`
5. **Start Command**: `cd backend/MadisonTime && daphne -b 0.0.0.0 -p $PORT MadisonTime.asgi:application`
6. **Add PostgreSQL Database** from Render dashboard
7. **Add Redis Instance** from Render dashboard

## 📝 Additional Documentation

For detailed information about async features, see [ASYNC_SETUP.md](backend/MadisonTime/ASYNC_SETUP.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is part of an academic assignment for KCU (Korea Cyber University).

## 👥 Authors

- Development Team - KCU Students

## 🙏 Acknowledgments

- Django community for excellent documentation
- Channels team for WebSocket support
- Celery team for task queue functionality
- Django Allauth for authentication system

---

**Note**: This project is configured for deployment on Render.com with PostgreSQL. For local development, you can use SQLite by modifying the database settings in `settings.py`.

For questions or issues, please open an issue on the repository.
