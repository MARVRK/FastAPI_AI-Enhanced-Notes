# AI-Enhanced Notes

This project provides a system for managing and summarizing notes using AI. It integrates OpenAI's GPT models for text summarization and uses FastAPI with SQLAlchemy for database management.

## Features

- **CRUD Operations** – Create, Read, Update, and Delete notes.
- **AI-Powered Summarization** – Generate concise summaries of stored notes using OpenAI's GPT models.
- **Statistics & Analysis** – Retrieve insights, including word count, common words, and note lengths.

## Tech Stack

- **FastAPI** – Web framework for building APIs.
- **SQLAlchemy** – ORM for database interactions.
- **OpenAI** – AI-based text summarization.
- **NLTK** – Tokenization and word frequency analysis.
- **PostgreSQL** – Relational database for storing notes.

---

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/AI-Enhanced-Notes.git
cd AI-Enhanced-Notes
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the PostgreSQL Database
- Ensure PostgreSQL is running locally or via Docker.
- Update the `.env` file with the correct `DATABASE_URL` credentials.

### 5. Run Database Migrations
```bash
alembic upgrade head
```

### 6. Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

### 7. Access the API
- **Base URL:** `http://127.0.0.1:8000`
- **Swagger UI:** `http://127.0.0.1:8000/docs` (for testing API endpoints)
