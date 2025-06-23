# Insure Insurance Company Website

A Django-based web application for Insure Insurance Company, providing comprehensive insurance services and customer management.

## Features

- **Public Website**: Company information, services, and quote requests
- **Customer Portal**: Policy management and claims tracking
- **Admin Dashboard**: Policy administration and customer management
- **Quote System**: Online insurance quote calculator
- **Claims Processing**: Digital claims submission and tracking
- **Payment Integration**: Secure online payment processing

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Authentication**: Django's built-in authentication system
- **Deployment**: Docker-ready configuration

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourcompany/inure-insurance.git
   cd inure-insurance
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and secret key
   ```

5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Load sample data (optional)**
   ```bash
   python manage.py loaddata fixtures/initial_data.json
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to access the website.

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://username:password@localhost:5432/inure_db
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@company.com
EMAIL_HOST_PASSWORD=your-app-password
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```

## Project Structure

```
inure_insurance/
├── apps/
│   ├── accounts/          # User authentication and profiles
│   ├── policies/          # Insurance policies management
│   ├── claims/            # Claims processing
│   ├── quotes/            # Quote generation system
│   └── payments/          # Payment processing
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates
├── media/                 # User uploaded files
├── config/                # Django settings
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── docker-compose.yml    # Docker configuration
```

## Usage

### Admin Access
- Navigate to `/admin/` 
- Use superuser credentials created during setup

### Customer Features
- **Register/Login**: Create customer accounts
- **Get Quotes**: Request insurance quotes online
- **Manage Policies**: View and update policy information
- **File Claims**: Submit and track insurance claims
- **Make Payments**: Pay premiums securely online

## Development

### Running Tests
```bash
python manage.py test
```

### Code Formatting
```bash
black .
flake8 .
```

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Deployment

### Using Docker
```bash
docker-compose up --build
```

### Production Checklist
- [ ] Set `DEBUG=False` in production
- [ ] Configure proper database credentials
- [ ] Set up SSL certificates
- [ ] Configure email settings
- [ ] Set up backup procedures
- [ ] Configure monitoring and logging

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Support

For technical support or questions:
- **Email**: support@inureinsurance.com
- **Phone**: +1 (555) 123-4567
- **Documentation**: [docs.inureinsurance.com](https://docs.inureinsurance.com)

## License

This project is proprietary software owned by Insure Insurance Company. All rights reserved.

---

**Insure Insurance Company** - Protecting what matters most since 2020.