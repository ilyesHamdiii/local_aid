# Neighborly Backend 🤝

A Django-powered backend API for a community platform that connects people who need help with those who can provide it. This repository contains the server-side implementation with Django templates for the web interface.

![Neighborly Hero](https://via.placeholder.com/800x400/6B73FF/FFFFFF?text=Neighborly+-+Backend+API)

> **Note**: Please note that the frontend interface is not part of this project and is maintained separately.



---

## 🤔 Why Neighborly?

In today's fast-paced world, communities often feel disconnected despite being more digitally connected than ever. People struggle with everyday tasks while their neighbors have the exact skills and time to help, but there's no efficient way to bridge this gap.

### The Problem We Solve

- **Isolation in Communities**: People don't know their neighbors or available local resources
- **Wasted Resources**: Skills, time, and tools go unused while others desperately need them
- **Barriers to Helping**: No easy way to offer help or find people who need assistance
- **Trust Issues**: Lack of reputation systems makes people hesitant to help strangers
- **Information Fragmentation**: Help requests scattered across multiple platforms and social media

### Our Solution

Neighborly creates a **trusted, organized, and efficient ecosystem** where:

- 🏠 **Local Focus**: Connect with people in your immediate community
- 🔍 **Smart Matching**: Find requests that match your skills and availability
- ⭐ **Reputation System**: Build trust through ratings and reviews
- 💬 **Direct Communication**: Seamless messaging between helpers and requesters
- 📱 **Easy Access**: Simple, intuitive platform that anyone can use

---

## 💡 Motivation

### Personal Stories That Inspired Us

Neighborly was born from real experiences of community disconnection and the powerful impact of neighbor-to-neighbor help:

> *"When I moved to a new city during the pandemic, I struggled to find help moving furniture up three flights of stairs. Meanwhile, my neighbor, a college athlete, was bored at home and would have gladly helped for the cost of a pizza. We just had no way to connect."* - **Sarah, Neighborly Co-founder**

> *"As a retired teacher, I have decades of tutoring experience but didn't know how to reach parents who needed help with their children's homework. Social media felt too impersonal, and formal tutoring services were too expensive for many families."* - **Community Beta Tester**

### The Vision Behind Neighborly

We believe that **every community has enough resources to solve its own problems** - they just need to be connected efficiently. Our motivation stems from several core beliefs:

#### 🌍 **Stronger Communities**
When neighbors help neighbors, it creates lasting relationships and more resilient communities. A single positive interaction can spark ongoing friendships and mutual support networks.

#### 🤝 **Mutual Benefit**
Helping others feels good and often comes back in unexpected ways. Neighborly creates a culture where giving and receiving help becomes natural and reciprocal.

#### 💰 **Economic Empowerment**
Many people have valuable skills but lack traditional employment opportunities. Neighborly enables micro-entrepreneurship and skill monetization at the community level.

#### 🚀 **Technology for Good**
We're tired of technology that divides us. Neighborly uses modern tech to bring people together in meaningful, real-world ways.

#### 🌱 **Sustainable Living**
By sharing resources and skills locally, we reduce waste, travel, and environmental impact while building more sustainable communities.

### What Drives Us Daily

- **Impact Stories**: Every successful connection reminds us why this matters
- **Community Feedback**: Users sharing how Neighborly changed their neighborhood experience
- **Growth Metrics**: Seeing organic community growth and repeat usage
- **Problem Solving**: Continuously improving how people connect and help each other

### Our Long-term Mission

To create a world where **no one struggles alone with problems their community can solve**, where **everyone's skills are valued and utilized**, and where **technology strengthens rather than weakens human connections**.

Neighborly isn't just a platform - it's a movement toward more connected, supportive, and resilient communities.

---

## 🌟 Features

### Core Backend Functionality
- **Request Management API** - Create, read, update, and delete help requests
- **User Profile System** - Comprehensive user profiles with stats and activity tracking
- **Category & Location Management** - Organized categorization and location-based filtering
- **Status Tracking** - Track request progress from open to completed
- **Database Management** - Robust data models and relationships

### Web Interface (Django Templates)
- **Browse Requests** - Server-rendered pages to discover help requests
- **Post Requests** - Form-based request submission with validation
- **User Profiles** - Template-based profile pages with stats and activity
- **Admin Interface** - Django admin for content management
- **Responsive Design** - Mobile-friendly template design

### Categories Supported
- 🛒 Errands & Shopping
- 🚚 Moving & Transportation
- 🐕 Pet Care
- 💻 Tech Help
- 🍕 Food & Meals
- 👶 Childcare
- 🏡 Home & Garden
- ⚡ Other

---

## 🚀 Tech Stack

### Backend Framework
- **Django 4.x** - Python web framework
- **Django Templates** - Server-side rendering
- **Django ORM** - Object-relational mapping
- **Django Admin** - Built-in administration interface
- **Django Forms** - Form handling and validation

### Database
- **SQLite** - Development database (default)
- **PostgreSQL** - Production database (recommended)

### Development Tools
- **Python 3.8+** - Programming language
- **pip** - Package management
- **Git** - Version control
- **Django Debug Toolbar** - Development debugging

### Styling
- **Tailwind CSS** - Utility-first CSS framework for templates
- **Custom CSS** - Additional styling for Django templates

---

## 📦 Installation

### Prerequisites
- **Python** (v3.8+)
- **pip** (Python package manager)
- **Git**

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Neighborly-backend.git
   cd Neighborly-backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   # Run migrations
   python manage.py makemigrations
   python manage.py migrate

   # Seed initial data
   python manage.py seed_data
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Web Interface: `http://localhost:8000`
   - Django Admin: `http://localhost:8000/admin`
   - API Endpoints: `http://localhost:8000/api/`

---

## 🏗️ Project Structure

```
Neighborly-backend/
├── aid/                      # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # URL routing
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin configuration
│   ├── migrations/          # Database migrations
│   └── management/          # Custom management commands
│       └── commands/
│           └── seed_data.py # Data seeding command
├── templates/aid/           # Django templates
│   ├── components/          # Template partials
│   │   ├── navbar.html
│   │   └── footer.html
│   ├── base.html           # Base template
│   ├── browse.html         # Browse requests page
│   ├── post_request.html   # Post request form
│   ├── my_requests.html    # User's requests
│   ├── profile_view.html   # User profile page
│   └── edit_request.html   # Edit request form
├── user/                   # User management app
│   ├── models.py           # User profile models
│   ├── views.py            # User-related views
│   └── urls.py             # User URL routing
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploads
├── requirements.txt        # Python dependencies
├── manage.py              # Django management script
└── settings.py            # Django settings
```

---

## 🎯 Usage

### For Developers

1. **API Development** - Use Django REST framework for API endpoints
2. **Template Development** - Create and customize Django templates
3. **Database Management** - Use Django ORM for data operations
4. **Admin Interface** - Manage content through Django admin

### For End Users (Web Interface)

1. **Browse Requests** - View community help requests
2. **Post Requests** - Submit new help requests via forms
3. **Manage Profiles** - Update user profiles and view stats
4. **Track Activity** - Monitor request status and responses

---

## 📱 API Endpoints

### Request Management
- `GET /aid/requests/` - List all requests
- `GET /aid/request/<id>/` - Get request details
- `POST /aid/post/` - Create new request
- `PUT /aid/request/<id>/edit/` - Update request
- `DELETE /aid/request/<id>/delete/` - Delete request

### User Management
- `GET /aid/profile/<username>/` - Get user profile
- `GET /aid/my-requests/` - Get current user's requests

### Admin Interface
- `GET /admin/` - Django admin interface
- `GET /admin/aid/request/` - Manage requests
- `GET /admin/aid/category/` - Manage categories
- `GET /admin/aid/location/` - Manage locations

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# For PostgreSQL production:
# DATABASE_URL=postgres://user:pass@localhost/dbname

# Media Settings
MEDIA_URL=/media/
MEDIA_ROOT=media/

# Static Files
STATIC_URL=/static/
STATIC_ROOT=staticfiles/
```

### Django Settings

Key configurations in `settings.py`:
- Database configuration
- Media file handling
- Static files configuration
- Template settings
- Authentication settings
- CORS settings (if needed for API)

---

## 🎨 Customization

### Templates
- Modify HTML templates in `templates/aid/`
- Customize styling in static CSS files
- Update base template for site-wide changes

### Models
- Extend existing models in `aid/models.py`
- Create new models for additional features
- Update admin interface in `aid/admin.py`

### Views
- Add new views in `aid/views.py`
- Create custom form handling
- Implement API endpoints

---

## 🧪 Testing

### Django Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test aid

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

### Test Categories
- **Model Tests** - Database model validation
- **View Tests** - URL routing and view logic
- **Form Tests** - Form validation and processing
- **Integration Tests** - End-to-end functionality

---

## 🚀 Deployment

### Production Setup

1. **Environment Configuration**
   ```bash
   # Set environment variables
   export DEBUG=False
   export DATABASE_URL=your-production-db-url
   export SECRET_KEY=your-production-secret-key
   ```

2. **Database Setup**
   ```bash
   # Run migrations
   python manage.py migrate

   # Collect static files
   python manage.py collectstatic --noinput
   ```

3. **Production Server**
   ```bash
   # Install production dependencies
   pip install gunicorn

   # Run with Gunicorn
   gunicorn project.wsgi:application --bind 0.0.0.0:8000
   ```

### Hosting Platforms
- **Railway** - Easy Django deployment
- **Heroku** - Platform as a service
- **DigitalOcean** - VPS hosting
- **AWS/GCP** - Cloud platform deployment

---

## 🤝 Contributing

We welcome contributions to the backend! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-backend-feature
   ```
3. **Make your changes**
   - Follow Django best practices
   - Add tests for new functionality
   - Update documentation as needed
4. **Run tests**
   ```bash
   python manage.py test
   ```
5. **Commit your changes**
   ```bash
   git commit -m 'Add amazing backend feature'
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/amazing-backend-feature
   ```
7. **Open a Pull Request**

### Code Style Guidelines
- Follow PEP 8 for Python code
- Use Django conventions and best practices
- Write comprehensive tests
- Document new features and APIs
- Use meaningful commit messages

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Django** - For the robust web framework
- **Python** - For the powerful programming language
- **Tailwind CSS** - For the utility-first CSS framework
- **Community Contributors** - For making this project better

---

## 📞 Support

- **Documentation**: Check this README and Django documentation
- **Issues**: Open an issue on GitHub for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Email**: [backend-support@Neighborly.com](mailto:backend-support@Neighborly.com)

---

## 🗺️ Roadmap

### Upcoming Backend Features
- [ ] REST API with Django REST Framework
- [ ] Real-time notifications system
- [ ] Advanced search and filtering APIs
- [ ] Payment integration backend
- [ ] Multi-language support
- [ ] Enhanced admin dashboard
- [ ] Analytics and reporting APIs
- [ ] WebSocket support for real-time features

### Version History
- **v1.0.0** - Initial Django backend with templates
- **v1.1.0** - User profiles and rating system
- **v1.2.0** - Enhanced messaging and notifications backend

---

**Built with ❤️ by the Neighborly Backend Team**

*Powering community connections through robust Django architecture.*

## Frontend

The frontend application for Neighborly is maintained as a separate project. If you're looking for the user interface, please refer to the frontend repository which contains the modern web application built with current frontend technologies.