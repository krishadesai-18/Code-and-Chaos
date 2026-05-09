# HealthIntel — Healthcare Skill Intelligence System

HealthIntel is a web-based skill intelligence platform developed for **Problem Statement 3** of the Ingenious Hackathon.

The platform helps students and early-career professionals track skills, identify knowledge gaps, and receive personalized course recommendations related to healthcare informatics and healthcare technology careers.


## Features

- User signup and login
- Profile and skill management
- Career goal selection
- Skill-gap analysis
- Course recommendation engine
- Dashboard visualization
- Admin analytics


## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### Visualization
- Chart.js


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic requests python-dotenv
```

### 4. Run Backend Server

```bash
uvicorn main:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

### 5. Run Frontend

```bash
python -m http.server 5500
```

Open in browser:

```bash
http://127.0.0.1:5500
```


## Environment Variables

Create a `.env` file in the root directory:

```env
COURSERA_API_KEY=your_coursera_api_key_here
COURSERA_API_URL=https://api.coursera.org/api/courses.v1

DATABASE_URL=sqlite:///database.db

SECRET_KEY=your_secret_key_here

ENV=development
```


## Demo Credentials

```text
Email: demo@healthcare.com
Password: demo
```


## Future Improvements

- Database integration
- JWT authentication
- Password hashing
- AI-powered recommendations
- Real API integrations
- Deployment support
