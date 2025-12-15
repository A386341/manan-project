# URL Shortener - Microservices Application

A simple microservices-based URL shortener built with Python, Node.js, and React.

## Services

- **Link Service** (Python/Flask) - Port 3000
- **Analytics Service** (Node.js/Express) - Port 4000
- **Frontend** (React) - Port 80/3000

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL (remote database provided)

## Database Configuration

The application connects to a shared PostgreSQL database with the following credentials:
```
Host: 8.222.170.22
Port: 5432
Database: urlshortener
User: postgres
Password: postgres
```

These are configured as defaults in the services, but can be overridden using environment variables.

## Setup and Run

### 1. Link Service
```bash
cd link-service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Runs on: http://localhost:3000

### 2. Analytics Service
```bash
cd analytics-service
npm install
npm start
```

Runs on: http://localhost:4000

### 3. Frontend
```bash
cd frontend
npm install

# Create .env file
echo "REACT_APP_LINK_SERVICE_URL=http://localhost:3000" > .env
echo "REACT_APP_ANALYTICS_SERVICE_URL=http://localhost:4000" >> .env

npm start
```

Runs on: http://localhost:3000 (React dev server)

## Environment Variables

### Link Service
- `DB_HOST` - Database host (default: 8.222.170.22)
- `DB_PORT` - Database port (default: 5432)
- `DB_NAME` - Database name (default: urlshortener)
- `DB_USER` - Database user (default: postgres)
- `DB_PASSWORD` - Database password (default: postgres)
- `ANALYTICS_SERVICE_URL` - Analytics service URL (default: http://localhost:4000)
- `PORT` - Service port (default: 3000)

### Analytics Service
- `DB_HOST` - Database host (default: 8.222.170.22)
- `DB_PORT` - Database port (default: 5432)
- `DB_NAME` - Database name (default: urlshortener)
- `DB_USER` - Database user (default: postgres)
- `DB_PASSWORD` - Database password (default: postgres)
- `PORT` - Service port (default: 4000)

### Frontend
- `REACT_APP_LINK_SERVICE_URL` - Link service URL
- `REACT_APP_ANALYTICS_SERVICE_URL` - Analytics service URL

## Testing

1. Open http://localhost:3000 in browser
2. Enter a long URL and click "Shorten"
3. Click the generated short link to test redirection
4. Refresh the page to see updated click counts

## API Endpoints

### Link Service (Port 3000)
- `GET /health` - Health check
- `POST /api/shorten` - Create short URL
- `GET /:short_code` - Redirect to original URL
- `GET /api/links` - Get all links

### Analytics Service (Port 4000)
- `GET /health` - Health check
- `POST /api/track` - Track a click
- `GET /api/analytics/:short_code` - Get analytics for specific link
- `GET /api/analytics` - Get all analytics

## Project Structure
```
.
├── link-service/          # Python/Flask service
├── analytics-service/     # Node.js/Express service
├── frontend/              # React application
├── terraform/             # Infrastructure as code (for deployment)
├── .github/workflows/     # CI/CD pipelines (for deployment)
└── monitoring/            # Monitoring configuration (for deployment)
```