# Notes API

A production-ready REST API built with FastAPI, featuring many-to-many relationships between notes and tags. This project demonstrates modern backend development practices including containerization, relational database design, and cloud deployment.

## Author

**Raji Olatubosun Joshua**

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Local Development Setup](#local-development-setup)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Docker Deployment](#docker-deployment)
- [AWS EC2 Deployment](#aws-ec2-deployment)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Notes API is a RESTful web service that allows users to create, read, update, and delete notes with associated tags. The application implements a many-to-many relationship pattern, enabling each note to have multiple tags and each tag to be associated with multiple notes.

This project serves as a practical demonstration of:
- Relational database design with association tables
- ORM usage with SQLAlchemy
- API development with FastAPI
- Containerization with Docker
- Cloud deployment on AWS EC2

## Features

- **Full CRUD Operations**: Create, read, update, and delete notes and tags
- **Many-to-Many Relationships**: Associate multiple tags with notes
- **Automatic Timestamps**: Track creation and modification times
- **Data Validation**: Request/response validation using Pydantic
- **Interactive API Documentation**: Auto-generated Swagger UI and ReDoc
- **Containerized Deployment**: Docker and Docker Compose support
- **Cloud-Ready**: Deployed and tested on AWS EC2
- **Pagination Support**: Efficient data retrieval with skip/limit parameters

## Architecture

The application follows a layered architecture pattern:

```
┌─────────────────┐
│   FastAPI       │  HTTP Layer (REST endpoints)
│   Routers       │
└────────┬────────┘
         │
┌────────▼────────┐
│   Pydantic      │  Validation Layer (schemas)
│   Schemas       │
└────────┬────────┘
         │
┌────────▼────────┐
│   CRUD          │  Business Logic Layer
│   Operations    │
└────────┬────────┘
         │
┌────────▼────────┐
│   SQLAlchemy    │  ORM Layer (models)
│   Models        │
└────────┬────────┘
         │
┌────────▼────────┐
│   PostgreSQL    │  Database Layer
└─────────────────┘
```

## Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.11** - Programming language
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server for running FastAPI

### Database
- **PostgreSQL 15** - Relational database management system
- **psycopg2-binary** - PostgreSQL adapter for Python

### DevOps
- **Docker** - Containerization platform
- **Docker Compose** - Multi-container orchestration
- **AWS EC2** - Cloud compute service

## Project Structure

```
notes-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database connection and session management
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic validation schemas
│   └── crud.py              # Database operations (Create, Read, Update, Delete)
├── routers/
│   ├── __init__.py
│   ├── notes.py             # Note-related endpoints
│   └── tags.py              # Tag-related endpoints
├── .env                     # Environment variables (not in version control)
├── .dockerignore            # Files to exclude from Docker builds
├── .gitignore               # Files to exclude from Git
├── docker-compose.yml       # Multi-container Docker configuration
├── Dockerfile               # Docker image definition
├── requirements.txt         # Python dependencies
├── create_tables.py         # Database initialization script
└── README.md                # Project documentation
```

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.11 or higher
- PostgreSQL 15 or higher
- Docker and Docker Compose (for containerized deployment)
- Git (for cloning the repository)

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/notes-api.git
cd notes-api
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
POSTGRES_PASSWORD=your_secure_password
DATABASE_URL=postgresql://notesuser:your_secure_password@localhost:5432/notesdb
```

### 5. Start PostgreSQL (Using Docker)

```bash
docker compose up -d postgres
```

### 6. Initialize Database Tables

```bash
python create_tables.py
```

### 7. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### 8. Access API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Documentation

The API provides interactive documentation through Swagger UI and ReDoc. Once the application is running, navigate to:

- **Swagger UI**: Interactive API exploration and testing interface
- **ReDoc**: Alternative documentation interface with a different layout

Both documentation interfaces are automatically generated from the API code and provide complete information about:
- Available endpoints
- Request/response schemas
- HTTP methods and status codes
- Authentication requirements (if applicable)

## Database Schema

The application uses three tables to implement the many-to-many relationship:

### Tables

#### notes
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT |
| title | VARCHAR | NOT NULL |
| content | TEXT | NOT NULL |
| created_at | TIMESTAMP WITH TIME ZONE | DEFAULT NOW() |
| updated_at | TIMESTAMP WITH TIME ZONE | DEFAULT NOW(), AUTO UPDATE |

#### tags
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT |
| name | VARCHAR | NOT NULL, UNIQUE |

#### note_tags (Association Table)
| Column | Type | Constraints |
|--------|------|-------------|
| note_id | INTEGER | FOREIGN KEY (notes.id), PRIMARY KEY |
| tag_id | INTEGER | FOREIGN KEY (tags.id), PRIMARY KEY |

### Relationships

- A **Note** can have multiple **Tags** (one-to-many from Note's perspective)
- A **Tag** can be associated with multiple **Notes** (one-to-many from Tag's perspective)
- The **note_tags** table creates the many-to-many relationship with a composite primary key

## Docker Deployment

### Build and Run with Docker Compose

The project includes a `docker-compose.yml` file that orchestrates both the FastAPI application and PostgreSQL database.

#### 1. Build the Images

```bash
docker compose build
```

#### 2. Start All Services

```bash
docker compose up -d
```

This command starts:
- PostgreSQL container on port 5432
- FastAPI application container on port 8000

#### 3. Initialize Database Tables

```bash
docker compose exec api python -c "from app.database import engine, Base; from app import models; Base.metadata.create_all(bind=engine)"
```

#### 4. View Logs

```bash
docker compose logs -f
```

#### 5. Stop All Services

```bash
docker compose down
```

To remove volumes (database data) as well:

```bash
docker compose down -v
```

### Docker Hub

The application image is available on Docker Hub:

```bash
docker pull yourusername/notes-api:latest
```

## AWS EC2 Deployment

### Prerequisites

- AWS account with EC2 access
- EC2 instance running Ubuntu 20.04 or higher
- Security group with inbound rules for ports 22 (SSH) and 8000 (API)
- SSH key pair (.pem file) for EC2 access

### Deployment Steps

#### 1. Connect to EC2 Instance

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

#### 2. Install Docker

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

Log out and back in for group changes to take effect.

#### 3. Install Docker Compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### 4. Create Application Directory

```bash
mkdir notes-api
cd notes-api
```

#### 5. Create docker-compose.yml

```bash
nano docker-compose.yml
```

Paste the docker-compose configuration (replace `yourusername` with your Docker Hub username):

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: notesuser
      POSTGRES_PASSWORD: your_secure_password
      POSTGRES_DB: notesdb
    volumes:
      - postgres_data:/var/lib/postgresql/data

  api:
    image: yourusername/notes-api:latest
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://notesuser:your_secure_password@postgres:5432/notesdb
    depends_on:
      - postgres

volumes:
  postgres_data:
```

#### 6. Start Services

```bash
docker-compose up -d
```

#### 7. Initialize Database

```bash
docker-compose exec api python -c "from app.database import engine, Base; from app import models; Base.metadata.create_all(bind=engine)"
```

#### 8. Configure Security Group

In AWS Console:
1. Navigate to EC2 > Security Groups
2. Select your instance's security group
3. Add inbound rule:
   - Type: Custom TCP
   - Port: 8000
   - Source: 0.0.0.0/0 (or restrict to your IP for security)

#### 9. Access Your API

Visit `http://your-ec2-public-ip:8000/docs` in your browser.

## Environment Variables

The application uses the following environment variables:

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| POSTGRES_PASSWORD | Password for PostgreSQL database | Yes | - |
| DATABASE_URL | Full PostgreSQL connection string | Yes | - |

Example `.env` file:

```env
POSTGRES_PASSWORD=your_secure_password
DATABASE_URL=postgresql://notesuser:your_secure_password@localhost:5432/notesdb
```

For Docker Compose, the hostname in DATABASE_URL should be `postgres` (the service name) instead of `localhost`.

## API Endpoints

### Notes Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| POST | `/notes` | Create a new note | `NoteCreate` | `NoteResponse` (201) |
| GET | `/notes` | Get all notes (paginated) | - | `List[NoteResponse]` (200) |
| GET | `/notes/{note_id}` | Get a specific note | - | `NoteResponse` (200) |
| PUT | `/notes/{note_id}` | Update a note | `NoteUpdate` | `NoteResponse` (200) |
| DELETE | `/notes/{note_id}` | Delete a note | - | No content (204) |
| POST | `/notes/{note_id}/tags/{tag_id}` | Assign tag to note | - | `NoteResponse` (201) |
| DELETE | `/notes/{note_id}/tags/{tag_id}` | Remove tag from note | - | No content (204) |

### Tags Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| POST | `/tags` | Create a new tag | `TagCreate` | `TagResponse` (201) |
| GET | `/tags` | Get all tags | - | `List[TagResponse]` (200) |
| GET | `/tags/{tag_id}` | Get a specific tag | - | `TagResponse` (200) |
| DELETE | `/tags/{tag_id}` | Delete a tag | - | No content (204) |

### Request/Response Schemas

#### NoteCreate
```json
{
  "title": "string",
  "content": "string"
}
```

#### NoteUpdate
```json
{
  "title": "string (optional)",
  "content": "string (optional)"
}
```

#### NoteResponse
```json
{
  "id": 1,
  "title": "string",
  "content": "string",
  "created_at": "2026-01-10T12:00:00Z",
  "updated_at": "2026-01-10T12:00:00Z",
  "tags": [
    {
      "id": 1,
      "name": "string"
    }
  ]
}
```

#### TagCreate
```json
{
  "name": "string"
}
```

#### TagResponse
```json
{
  "id": 1,
  "name": "string"
}
```

## Testing

### Manual Testing with Swagger UI

1. Start the application
2. Navigate to `http://localhost:8000/docs`
3. Use the interactive interface to test endpoints

### Testing with cURL

#### Create a note
```bash
curl -X POST "http://localhost:8000/notes" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Note","content":"This is a test"}'
```

#### Get all notes
```bash
curl -X GET "http://localhost:8000/notes"
```

#### Create a tag
```bash
curl -X POST "http://localhost:8000/tags" \
  -H "Content-Type: application/json" \
  -d '{"name":"work"}'
```

#### Assign tag to note
```bash
curl -X POST "http://localhost:8000/notes/1/tags/1"
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with dedication to learning and understanding modern backend development practices.**
