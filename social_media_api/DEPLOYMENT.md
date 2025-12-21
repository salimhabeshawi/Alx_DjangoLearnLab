# Deployment Guide

## Production Configuration

The application is configured for production deployment with the following features:

### Environment Variables

Set these environment variables in your production environment:

- `DEBUG`: Set to `'True'` for development, omit or set to `'False'` for production (default: False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (default: '*')
- `SECURE_SSL_REDIRECT`: Set to `'True'` to redirect HTTP to HTTPS (default: False)
- `SESSION_COOKIE_SECURE`: Set to `'True'` for HTTPS-only session cookies (default: False)
- `CSRF_COOKIE_SECURE`: Set to `'True'` for HTTPS-only CSRF cookies (default: False)

### Security Settings

The following security settings are enabled:
- `SECURE_BROWSER_XSS_FILTER = True`
- `X_FRAME_OPTIONS = 'DENY'`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`

### Deployment Steps

#### 1. Prepare the Application

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate
```

#### 2. Deploy to Heroku (Example)

```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit"

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
heroku config:set SECURE_SSL_REDIRECT=True
heroku config:set SESSION_COOKIE_SECURE=True
heroku config:set CSRF_COOKIE_SECURE=True

# Deploy
git push heroku main

# Run migrations on Heroku
heroku run python manage.py migrate
```

#### 3. Alternative: Deploy to AWS/DigitalOcean

For AWS Elastic Beanstalk or DigitalOcean:

1. Set up a PostgreSQL database
2. Configure environment variables in your hosting platform
3. Use Gunicorn as the WSGI server (already configured in Procfile)
4. Set up Nginx as a reverse proxy
5. Configure SSL/TLS certificates

### Running Locally with Production Settings

```bash
# Set environment variables
export DEBUG=False
export ALLOWED_HOSTS=localhost,127.0.0.1

# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn social_media_api.wsgi --bind 0.0.0.0:8000
```

### Deployment Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set up HTTPS/SSL certificates
- [ ] Enable security environment variables
- [ ] Run `collectstatic` for static files
- [ ] Run database migrations
- [ ] Set up monitoring and logging
- [ ] Configure database backups
- [ ] Review and rotate `SECRET_KEY`
