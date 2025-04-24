# Blood Bank Management System

A Django-based web application for managing blood bank operations, donors, and patients.

## Features

- Multi-user system (Administrator, Donor, Patient, Blood Bank, Guest)
- Blood donation camp management
- Blood inventory tracking
- Complaint management system
- Donor and patient registration
- Feedback system
- Blood availability tracking with visualization

## Tech Stack

- Python 3.x
- Django 5.1.6
- SQLite3 Database
- Bootstrap 5
- ApexCharts for data visualization

## Project Structure

```
BloodBank/
├── Administrator/     # Admin management module
├── Bloodbankapp/     # Blood bank operations module
├── Donor/            # Donor management module
├── Guest/            # Public access module
├── Patient/          # Patient management module
└── BloodBank/        # Project settings and configuration
```

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv MainEnv
```

3. Activate the virtual environment:
```bash
# Windows
MainEnv\Scripts\activate

# Linux/Mac
source MainEnv/bin/activate
```

4. Install dependencies:
```bash
pip install django
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Environment Variables

The following environment variables should be configured:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: List of allowed hosts

## Database Schema

Key models include:
- Blood Bank
- Blood Donation
- Blood Camp
- Donor
- Patient
- Complaint
- Feedback

## Security Notice

This is a development setup. For production:
- Change the Django secret key
- Set DEBUG to False
- Configure proper ALLOWED_HOSTS
- Use a production-grade database
- Set up proper static file serving

## License

This project uses templates from:
- DarkPan - Bootstrap 5 Admin Template
- Kelly Bootstrap Template

For template licensing details, refer to their respective license files.